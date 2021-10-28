import uuid
from django.shortcuts import get_object_or_404
from projects.models import Bus, AssetType, Scenario, ConnectionLink, Asset
import json
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
from projects.forms import AssetCreateForm, BusForm, StorageForm
# region sent db nodes to js
from projects.dtos import convert_to_dto
from crispy_forms.templatetags import crispy_forms_filters
from django.http import JsonResponse
import logging

logger = logging.getLogger(__name__)


def handle_bus_form_post(request, scen_id=0, asset_type_name="", asset_uuid=None):
    if asset_uuid:
        existing_bus = get_object_or_404(Bus, pk=asset_uuid)
        form = BusForm(request.POST, asset_type=asset_type_name, instance=existing_bus)
    else:
        form = BusForm(request.POST, asset_type=asset_type_name)
    
    scenario = get_object_or_404(Scenario, pk=scen_id)
    if form.is_valid():
        bus = form.save(commit=False)
        bus.scenario = scenario
        try:
            bus.pos_x = float(form.data['pos_x'])
            bus.pos_y = float(form.data['pos_y'])
            bus.input_ports = int(float(form.data['input_ports']))
            bus.output_ports = int(float(form.data['output_ports']))
        except Exception as ex:
            logger.warning(f"Failed to set positioning for bus {bus.name} in scenario: {scen_id}.")
        bus.save()
        return JsonResponse({'success': True, "asset_id": bus.id}, status=200)
    logger.warning(f"The submitted bus has erroneous field values.")
    form_html = crispy_forms_filters.as_crispy_form(form)
    return JsonResponse({'success': False, 'form_html': form_html}, status=422)


def handle_storage_unit_form_post(request, scen_id=0, asset_type_name="", asset_uuid=None):
    form = StorageForm(request.POST, request.FILES, asset_type=asset_type_name)
    scenario = get_object_or_404(Scenario, pk=scen_id)
    if form.is_valid():
        try:
            # First delete all existing associated storage assets from the db
            if asset_uuid:
                existing_asset = get_object_or_404(Asset, unique_id=asset_uuid)
                existing_asset.delete()  # deletes also automatically all chidren using models.CASCADE

            # Create the ESS Parent Asset
            ess_asset = Asset.objects.create(
                name=form.cleaned_data['name'],
                asset_type=get_object_or_404(AssetType, asset_type=f"{asset_type_name}"),
                pos_x=float(form.data['pos_x']),
                pos_y=float(form.data['pos_y']),
                unique_id=asset_uuid or str(uuid.uuid4()), # if exising asset create an asset with the exact same unique_id else generate a new one
                scenario=scenario
            )

            # Create the ess chanrging power
            ess_charging_power_asset = Asset(
                name=f"{ess_asset.name} input power",
                asset_type=get_object_or_404(AssetType, asset_type="charging_power"),
                scenario=scenario,
                parent_asset=ess_asset
            )
            # Create the ess dischanrging power
            ess_discharging_power_asset = Asset(
                name=f"{ess_asset.name} output power",
                asset_type=get_object_or_404(AssetType, asset_type="discharging_power"),
                scenario=scenario,
                parent_asset=ess_asset
            )
            # Create the ess capacity
            ess_capacity_asset = Asset(
                name=f"{ess_asset.name} capacity",
                asset_type=get_object_or_404(AssetType, asset_type="capacity"),
                scenario=scenario,
                parent_asset=ess_asset
            )
            # Populate all subassets
            for key, value in form.cleaned_data.items():
                if key.startswith('cp_'):
                    setattr(ess_capacity_asset, key[3:], value)
                elif key.startswith('chp_'):
                    setattr(ess_charging_power_asset, key[4:], value)
                elif key.startswith('dchp_'):
                    setattr(ess_discharging_power_asset, key[5:], value)
            
            ess_capacity_asset.save()
            ess_charging_power_asset.save()
            ess_discharging_power_asset.save()
            return JsonResponse({'success': True, "asset_id": ess_asset.unique_id}, status=200)
        except Exception as ex:
            logger.warning(f"Failed to create storage asset {ess_asset.name} in scenario: {scen_id}.")
            return JsonResponse({'success': False, 'exception': ex}, status=422)
    logger.warning(f"The submitted asset has erroneous field values.")
    form_html = crispy_forms_filters.as_crispy_form(form)
    return JsonResponse({'success': False, 'form_html': form_html}, status=422)


def handle_asset_form_post(request, scen_id=0, asset_type_name="", asset_uuid=None):
    if asset_uuid:
        existing_asset = get_object_or_404(Asset, unique_id=asset_uuid)
        form = AssetCreateForm(request.POST, request.FILES, asset_type=asset_type_name, instance=existing_asset)
    else:
        form = AssetCreateForm(request.POST, request.FILES, asset_type=asset_type_name)

    asset_type = get_object_or_404(AssetType, asset_type=asset_type_name)
    scenario = get_object_or_404(Scenario, pk=scen_id)
    if form.is_valid():
        asset = form.save(commit=False)
        asset.scenario = scenario
        asset.asset_type = asset_type
        try:
            asset.pos_x = float(form.data['pos_x'])
            asset.pos_y = float(form.data['pos_y'])
        except Exception as ex:
            logger.warning(f"Failed to set positioning for asset {asset.name} in scenario: {scen_id}.")
        asset.save()
        return JsonResponse({'success': True, "asset_id": asset.unique_id}, status=200)
    logger.warning(f"The submitted asset has erroneous field values.")
    form_html = crispy_forms_filters.as_crispy_form(form)
    return JsonResponse({'success': False, 'form_html': form_html}, status=422)


def load_scenario_topology_from_db(scen_id):
    bus_nodes_list = db_bus_nodes_to_list(scen_id)
    asset_nodes_list = db_asset_nodes_to_list(scen_id)
    connection_links_list = db_connection_links_to_list(scen_id)
    return {"busses": bus_nodes_list, "assets": asset_nodes_list, "links": connection_links_list}


def db_bus_nodes_to_list(scen_id):
    all_db_busses = Bus.objects.filter(scenario_id=scen_id)
    bus_nodes_list = list()
    for db_bus in all_db_busses:
        db_bus_dict = {
            "name": "bus", 
            "pos_x": db_bus.pos_x, 
            "pos_y": db_bus.pos_y, 
            "input_ports": db_bus.input_ports,
            "output_ports": db_bus.output_ports,
            "data": {
                "name": db_bus.name, 
                "bustype": db_bus.type, 
                "databaseId": db_bus.id, 
                "parent_asset_id": db_bus.parent_asset_id if db_bus.parent_asset_id else ""
            }
        }
        bus_nodes_list.append(db_bus_dict)
    return bus_nodes_list


def db_asset_nodes_to_list(scen_id):
    all_db_assets = Asset.objects.filter(scenario_id=scen_id)
    # dont return children assets (i.e. for storage assets)
    no_storage_children_assets = all_db_assets.filter(parent_asset_id=None)
    asset_nodes_list = list()
    for db_asset in no_storage_children_assets:
        asset_type_obj = get_object_or_404(AssetType, pk=db_asset.asset_type_id)
        db_asset_dict = {
            "name": asset_type_obj.asset_type, 
            "pos_x": db_asset.pos_x, 
            "pos_y": db_asset.pos_y,
            "data": {
                'name': db_asset.name,
                'unique_id': db_asset.unique_id,
                "parent_asset_id": db_asset.parent_asset_id if db_asset.parent_asset_id else ""
            }
        }
        asset_nodes_list.append(db_asset_dict)
    return asset_nodes_list


def db_connection_links_to_list(scen_id):
    all_db_connection_links = ConnectionLink.objects.filter(scenario_id=scen_id)
    connections_list = list()
    for db_connection in all_db_connection_links:
        db_connection_dict = {"bus_id": db_connection.bus_id, "asset_id": db_connection.asset.unique_id,
                              "flow_direction": db_connection.flow_direction,
                              "bus_connection_port": db_connection.bus_connection_port}
        connections_list.append(db_connection_dict)
    return connections_list


# endregion db_nodes_to_js





# region Scenario Duplicate
def duplicate_scenario_objects(obj_list, scenario, asset_mapping_dict=None):
    """
    Implement the Node Level (Assets and Busses) duplication of the scenario.
    The functionality is utilized in the scenario search page for each project in the UI of EPA.
    :param obj_list: list of objects to duplicate, can be either bus objects list of assets list
    :param scenario: the scenario under which the assets will be created
    :param asset_mapping_dict: specifically for the case of busses which are part of a storage asset,
    the parent ESS asset id is required. This value is passed with a mapping dict.
    :return: a map dictionary between old and new nodes (assets or busses) ids.
    """

    storage_subasset_list = list()
    mapping_dict = dict()

    for obj in obj_list:
        old_id = obj.id

        if hasattr(obj, 'unique_id'):  # i.e. it's an asset
            obj.unique_id = str(uuid.uuid4())
        obj.id = None
        obj.scenario = scenario
        obj.save()
        mapping_dict[old_id] = obj.id
        if obj.parent_asset:
            storage_subasset_list.append(obj)

    # now properly update the parent id of all new storage assets
    for obj in storage_subasset_list:
        obj.parent_asset_id = asset_mapping_dict[obj.parent_asset_id] if type(obj) == Bus else mapping_dict[obj.parent_asset_id]
        obj.save()

    return mapping_dict


def duplicate_scenario_connections(connections_list, scenario, asset_map, bus_map):
    for connection in connections_list:
        old_asset_id = connection.asset_id
        old_bus_id = connection.bus_id
        connection.id = None
        connection.asset_id = asset_map[old_asset_id]
        connection.bus_id = bus_map[old_bus_id]
        connection.scenario = scenario
        connection.save()
# endregion


class NodeObject:
    def __init__(self, node_data=None):
        self.name = node_data['name']  # asset type name : e.g. bus, pv_plant, etc
        self.data = node_data['data']  # name: eg. demand_01, parent_asset_id, unique_id
        self.db_obj_id = self.uuid_2_db_id(node_data)
        self.group_id = (node_data['data']['parent_asset_id'] if 'parent_asset_id' in node_data['data'] else None)
        self.node_obj_type = 'bus' if self.name == 'bus' else 'asset'
        self.inputs = node_data['inputs']
        self.outputs = node_data['outputs']

    def __str__(self):
        return "\n".join(["name: " + self.name, "db_id: "+ str(self.db_obj_id), "group_id: " + str(self.group_id), "node type: " + str(self.node_obj_type)])

    @staticmethod
    def uuid_2_db_id(data):
        if 'db_id' in data and data['db_id']:
            if isinstance(data['db_id'], int):
                return data['db_id']
            elif isinstance(data['db_id'], str):
                asset = Asset.objects.filter(unique_id=data['db_id']).first()
                return asset.id if asset else None
            else:
                return None
        else:
            return None


    def create_connection_links(self, scen_id):
        """Create ConnectionLink from the node object (asset or bus) to all of its outputs"""
        for port_key, connections_list in self.outputs.items():
            for output_connection in connections_list:
                # node_obj is a bus connecting to asset(s)
                if self.node_obj_type == 'bus' and isinstance(output_connection['node'], str): # i.e. unique_id
                    ConnectionLink.objects.create(
                        bus=get_object_or_404(Bus, pk=self.db_obj_id),
                        asset=get_object_or_404(Asset, unique_id=output_connection['node']),
                        flow_direction='B2A',
                        bus_connection_port=port_key,
                        scenario=get_object_or_404(Scenario, pk=scen_id)
                    )
                # node_obj is an asset connecting to bus(ses)
                elif self.node_obj_type != 'bus' and isinstance(output_connection['node'], int):
                    ConnectionLink.objects.create(
                        bus=get_object_or_404(Bus, pk=output_connection['node']),
                        asset=get_object_or_404(Asset, pk=self.db_obj_id),
                        flow_direction='A2B',
                        bus_connection_port=output_connection['output'],
                        scenario=get_object_or_404(Scenario, pk=scen_id)
                    )
        logger.debug(f"Nodes interconnection links for {self.name} '{self.data['name']}' were created successfully in scenario: {scen_id}.")

    def assign_asset_to_proper_group(self, node_to_db_mapping):
        """Seems to be unused here"""
        try:
            if self.node_obj_type == "asset":
                asset = get_object_or_404(Asset, pk=self.db_obj_id)
                asset.parent_asset_id = node_to_db_mapping[self.group_id]["db_obj_id"] if self.group_id else None
                asset.save()
            else:  # i.e. "bus"
                bus = get_object_or_404(Bus, pk=self.db_obj_id)
                bus.parent_asset_id = node_to_db_mapping[self.group_id]["db_obj_id"] if self.group_id else None
                bus.save()
        except KeyError:
            return {"success": False, "obj_type": self.node_obj_type}
        except ValidationError:
            return {"success": False, "obj_type": self.node_obj_type}
        else:
            return {"success": True, "obj_type": self.node_obj_type}


def update_deleted_objects_from_database(scenario_id, topo_node_list):
    """Delete Database Scenario Related Objects which are not in the topology before inserting or updating data."""
    all_scenario_assets = Asset.objects.filter(scenario_id=scenario_id)
    # dont include storage unit children assets
    scenario_assets_ids_excluding_storage_children = all_scenario_assets.filter(parent_asset=None).values_list('id', flat=True)
    all_scenario_busses_ids = Bus.objects.filter(scenario_id=scenario_id).values_list('id', flat=True)

    # lists the DB ids of the assets and busses coming from the topology
    topology_asset_ids = list()
    topology_busses_ids = list()
    for node in topo_node_list:
        if node.name != 'bus' and node.db_obj_id:
            topology_asset_ids.append(node.db_obj_id)
        elif node.name == 'bus' and node.db_obj_id:
            topology_busses_ids.append(node.db_obj_id)

    # deletes asset or bus which DB id is not in the topology anymore (was removed by user)
    for asset_id in scenario_assets_ids_excluding_storage_children:
        if asset_id not in topology_asset_ids:
            logger.debug(f"Deleting asset {asset_id} of scenario {scenario_id} which was removed from the topology by the user.")
            Asset.objects.filter(id=asset_id).delete()

    for bus_id in all_scenario_busses_ids:
        if bus_id not in topology_busses_ids:
            logger.debug(f"Deleting bus {bus_id} of scenario {scenario_id} which was removed from the topology by the user.")
            Bus.objects.filter(id=bus_id).delete()


def create_ESS_objects(all_ess_assets_node_list, scen_id):
    ess_obj_list = list()

    charging_power_asset_id = AssetType.objects.get(asset_type="charging_power")
    discharging_power_asset_id = AssetType.objects.get(asset_type="discharging_power")
    capacity_asset_id = AssetType.objects.get(asset_type="capacity")

    scenario_connection_links = ConnectionLink.objects.filter(scenario_id=scen_id)
    cap_scenario_connection_links = scenario_connection_links.filter(asset__asset_type=capacity_asset_id)
    charge_scenario_connection_links = scenario_connection_links.filter(asset__asset_type=charging_power_asset_id)
    discharge_scenario_connection_links = scenario_connection_links.filter(asset__asset_type=discharging_power_asset_id)

    for asset in all_ess_assets_node_list:
        if asset.name == 'capacity':
            # check if there is a connection link to a bus
            pass


# Helper method to clean dict data from empty values
def remove_empty_elements(d):
    def empty(x):
        return x is None or x == {} or x == []

    if not isinstance(d, (dict, list)):
        return d
    elif isinstance(d, list):
        return [v for v in (remove_empty_elements(v) for v in d) if not empty(v)]
    else:
        return {k: v for k, v in ((k, remove_empty_elements(v)) for k, v in d.items()) if not empty(v)}


# Helper to convert Scenario data to MVS importable json
def get_topology_json(scenario_to_convert):
    mvs_request_dto = convert_to_dto(scenario_to_convert)
    dumped_data = json.loads(json.dumps(mvs_request_dto.__dict__, default=lambda o: o.__dict__))
    # Remove None values
    return remove_empty_elements(dumped_data)