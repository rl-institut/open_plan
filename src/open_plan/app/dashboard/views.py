from django.core.exceptions import PermissionDenied
from django.http.response import Http404, HttpResponse
from dashboard.helpers import storage_asset_to_list
from dashboard.models import AssetsResults, KPICostsMatrixResults, KPIScalarResults, KPI_COSTS_TOOLTIPS, KPI_COSTS_UNITS, KPI_SCALAR_TOOLTIPS, KPI_SCALAR_UNITS
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from jsonview.decorators import json_view
from projects.models import Scenario, Simulation
from projects.services import excuses_design_under_development
from dashboard.helpers import kpi_scalars_list
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe
from io import BytesIO
import xlsxwriter
import json
import datetime
import logging

logger = logging.getLogger(__name__)


@login_required
@json_view
@require_http_methods(["GET"])
def scenario_available_results(request, scen_id):

    scenario = get_object_or_404(Scenario, pk=scen_id)
    if (scenario.project.user != request.user) and (request.user not in scenario.project.viewers.all()):
        raise PermissionDenied
    
    try:
        assets_results_obj = AssetsResults.objects.get(simulation=scenario.simulation)
        assets_results_json = json.loads(assets_results_obj.assets_list)

        # bring all storage subasset one level up to show their flows.
        storage_asset_to_list(assets_results_json)

        # Generate available asset category JSON
        asset_category_json = [{'assetCategory': asset_category} for asset_category in assets_results_json.keys()]
        # Generate available asset type JSON
        assets_names_json = [
            [
                {
                    'assetCategory': asset_category,
                    'assetName': asset['label']
                }
                for asset in assets_results_json[asset_category]
                # show only assets of a certain Energy Vector
                if asset['energy_vector'] == request.GET['energy_vector']
                and any(key in ['flow','timeseries_soc'] for key in asset.keys())
            ]
            for asset_category in assets_results_json.keys()
        ]
        response_json = {'options': assets_names_json, 'optgroups': asset_category_json}
        return JsonResponse(response_json, status=200, content_type='application/json')
    except Exception as e:
        logger.error(f"Dashboard ERROR: MVS Req Id: {scenario.simulation.mvs_token}. Thrown Exception: {e}")
        return JsonResponse({"error": "Could not retrieve asset names and categories."},
                            status=404, content_type='application/json')


@login_required
@json_view
@require_http_methods(["GET"])
def scenario_request_results(request, scen_id):
    scenario = get_object_or_404(Scenario, pk=scen_id)

    # if scenario.project.user != request.user:
    #     return HttpResponseForbidden()
    if (scenario.project.user != request.user) and (request.user not in scenario.project.viewers.all()):
        raise PermissionDenied
    
    # real data
    try:
        asset_name_list = request.GET.get('assetNameList').split(',')
        assets_results_obj = AssetsResults.objects.get(simulation=scenario.simulation)
        assets_results_json = json.loads(assets_results_obj.assets_list)

        # Generate available asset category list
        asset_category_list = [asset_category for asset_category in assets_results_json.keys()]
        
        # bring all storage subasset one level up to show their flows.
        storage_asset_to_list(assets_results_json)

        # Asset category to asset type
        asset_name_to_category = {
                asset_name['label']: asset_category
                for asset_category in asset_category_list
                for asset_name in assets_results_json[asset_category]
            }

        # Create the datetimes index. Constrains: step in minutes and evaluated_period in days
        base_date = scenario.start_date
        datetime_list = [
            datetime.datetime.timestamp(base_date + datetime.timedelta(minutes=step)) 
            for step in range(0, 24*scenario.evaluated_period*scenario.time_step, scenario.time_step)
            ]

        # Generate results JSON per asset name
        results_json = [
            {
                'xAxis':
                    {
                        'values': datetime_list,
                        'label': 'Time'
                    },
                'yAxis':
                    {
                        'values': asset['flow']['value'] if 'flow' in asset else asset['timeseries_soc']['value'],
                        'label': asset['flow']['unit'] if 'flow' in asset else asset['timeseries_soc']['unit'],  # 'Power'
                    },
                'title': asset_name
            }
            for asset_name in asset_name_list
            for asset in assets_results_json[asset_name_to_category[asset_name]]
            if asset['label'] == asset_name
        ]

        return JsonResponse(results_json, status=200, content_type='application/json', safe=False)
    except Exception as e:
        logger.error(f"Dashboard ERROR: MVS Req Id: {scenario.simulation.mvs_token}. Thrown Exception: {e}")
        return JsonResponse({"Error":"Could not retrieve timeseries data."}, status=404, content_type='application/json', safe=False)



@login_required
@require_http_methods(["GET"])
def scenario_visualize_results(request, scen_id=None):

    if scen_id is None:
        excuses_design_under_development(request)

        answer = render(request, 'scenario/scenario_results_page.html')
    else:
        scenario = get_object_or_404(Scenario, pk=scen_id)
        proj_id = scenario.project.id

        if (scenario.project.user != request.user) and (request.user not in scenario.project.viewers.all()):
            raise PermissionDenied

        qs = Simulation.objects.filter(scenario=scenario)
        if qs.exists():
            kpi_scalar_results_obj = KPIScalarResults.objects.get(simulation=scenario.simulation)
            kpi_scalar_values_dict = json.loads(kpi_scalar_results_obj.scalar_values)

            scalar_kpis_json = kpi_scalars_list(kpi_scalar_values_dict, KPI_SCALAR_UNITS, KPI_SCALAR_TOOLTIPS)

            answer = render(request, 'scenario/scenario_visualize_results.html',
                          {'scen_id': scen_id, 'scalar_kpis': scalar_kpis_json, 'project_id': proj_id})
        else:
            # redirect to the page where the simulation is started, or results fetched again
            messages.error(request, _("Your scenario was never simulated, the results are still pending or there is an error in the simulation. Please click on 'Run simulation', 'Update results' or 'Check status' button "))
            answer = HttpResponseRedirect(reverse('scenario_review', args=[proj_id, scen_id]))

    return answer



@login_required
@json_view
@require_http_methods(["GET"])
def scenario_economic_results(request, scen_id):
    """
    This view gathers all simulation specific cost matrix KPI results
    and sends them to the client for representation.
    """
    scenario = get_object_or_404(Scenario, pk=scen_id)

    # if scenario.project.user != request.user:
    #     return HttpResponseForbidden()
    if (scenario.project.user != request.user) and (request.user not in scenario.project.viewers.all()):
        raise PermissionDenied
    
    try:
        kpi_cost_results_obj = KPICostsMatrixResults.objects.get(simulation=scenario.simulation)
        kpi_cost_values_dict = json.loads(kpi_cost_results_obj.cost_values)

        new_dict = dict()
        for asset_name in kpi_cost_values_dict.keys():
            for category,v in kpi_cost_values_dict[asset_name].items():
                new_dict.setdefault(category, {})[asset_name] = v
        
        # non-dummy data
        results_json = [
            {
                'values': [(round(value,3) if '€/kWh' in KPI_COSTS_UNITS[category] else round(value,2)) for value in new_dict[category].values()],
                'labels': [asset.replace('_',' ').upper() for asset in new_dict[category].keys()],
                'type': 'pie',
                'title': category.replace('_',' ').upper(),
                'titleTooltip': KPI_COSTS_TOOLTIPS[category],
                'units': [KPI_COSTS_UNITS[category] for _ in new_dict[category].keys()]
            }
            for category in new_dict.keys()
            if category in KPI_COSTS_UNITS.keys() and sum(new_dict[category].values()) > 0.0  # there is at least one non zero value
            and len(list(filter(lambda asset_name: new_dict[category][asset_name] > 0.0 ,new_dict[category]))) > 1.0
            # there are more than one assets with value > 0
        ]
        return JsonResponse(results_json, status=200, content_type='application/json', safe=False)
    except Exception as e:
        logger.error(f"Dashboard ERROR: MVS Req Id: {scenario.simulation.mvs_token}. Thrown Exception: {e}")
        return JsonResponse({"error":f"Could not retrieve kpi cost data."}, status=404, content_type='application/json', safe=False)



@login_required
@require_http_methods(["GET"])
def download_scalar_results(request, scen_id):
    scenario = get_object_or_404(Scenario, pk=scen_id)

    if (scenario.project.user != request.user) and (request.user not in scenario.project.viewers.all()):
        raise PermissionDenied
    
    try:
        kpi_scalar_results_obj = KPIScalarResults.objects.get(simulation=scenario.simulation)
        kpi_scalar_values_dict = json.loads(kpi_scalar_results_obj.scalar_values)
        scalar_kpis_json = kpi_scalars_list(kpi_scalar_values_dict, KPI_SCALAR_UNITS, KPI_SCALAR_TOOLTIPS)
        
        output = BytesIO()
        workbook = xlsxwriter.Workbook(output)
        worksheet = workbook.add_worksheet('Scalars')

        for idx, kpi_obj in enumerate(scalar_kpis_json):
            if idx==0:
                worksheet.write_row(0, 0, kpi_obj.keys())
            worksheet.write_row(idx+1, 0, kpi_obj.values())
        
        workbook.close()
        output.seek(0)
    except Exception as e:
        logger.error(f"Dashboard ERROR: Could not generate KPI Scalars download file with Scenario Id: {scen_id}. Thrown Exception: {e}")
        raise Http404()

    

    filename = 'kpi_scalar_results.xlsx'
    response = HttpResponse(
        output,
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = f'attachment; filename={filename}'

    return response


@login_required
@require_http_methods(["GET"])
def download_cost_results(request, scen_id):
    scenario = get_object_or_404(Scenario, pk=scen_id)

    if (scenario.project.user != request.user) and (request.user not in scenario.project.viewers.all()):
        raise PermissionDenied
    
    try:
        kpi_cost_results_obj = KPICostsMatrixResults.objects.get(simulation=scenario.simulation)
        kpi_cost_values_dict = json.loads(kpi_cost_results_obj.cost_values)
        
        output = BytesIO()
        workbook = xlsxwriter.Workbook(output)
        worksheet = workbook.add_worksheet('Costs')

        for col, asset in enumerate(kpi_cost_values_dict.items()):
            asset_name, asset_dict = asset
            if col == 0:
                worksheet.write_column(1, 0, asset_dict.keys())
                worksheet.write_row(0, 1, kpi_cost_values_dict.keys())
            worksheet.write_column(1, col+1, asset_dict.values())
        
        workbook.close()
        output.seek(0)
    except Exception as e:
        logger.error(f"Dashboard ERROR: Could not generate KPI Costs download file with Scenario Id: {scen_id}. Thrown Exception: {e}")
        raise Http404()

    

    filename = 'kpi_individual_costs.xlsx'
    response = HttpResponse(
        output,
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = f'attachment; filename={filename}'

    return response


@login_required
@require_http_methods(["GET"])
def download_timeseries_results(request, scen_id):
    scenario = get_object_or_404(Scenario, pk=scen_id)

    if (scenario.project.user != request.user) and (request.user not in scenario.project.viewers.all()):
        raise PermissionDenied
    
    try:
        assets_results_obj = AssetsResults.objects.get(simulation=scenario.simulation)
        assets_results_json = json.loads(assets_results_obj.assets_list)
        # Create the datetimes index. Constrains: step in minutes and evaluated_period in days
        base_date = scenario.start_date
        datetime_list = [
            datetime.datetime.timestamp(base_date + datetime.timedelta(minutes=step)) 
            for step in range(0, 24*scenario.evaluated_period*scenario.time_step, scenario.time_step)
        ]

        output = BytesIO()
        workbook = xlsxwriter.Workbook(output)
        merge_format = workbook.add_format({
            'bold':     True,
            'align':    'center',
            'valign':   'vcenter',
        })

        KEY1, KEY2, KEY3, KEY4 = ('timeseries_soc', 'input power', 'output power' ,'storage capacity')

        for key in assets_results_json.keys():
            worksheet = workbook.add_worksheet(key)
            worksheet.write(0, 0, 'Timestamp')
            if key != 'energy_storage':
                worksheet.write_column(2, 0, datetime_list)
                for col, asset in enumerate(assets_results_json[key]):
                    if all(key in asset.keys() for key in ['label','flow']):
                        worksheet.write(0, col+1, asset['label'])
                        worksheet.write(1, col+1, asset['flow']['unit'])
                        worksheet.write_column(2, col+1, asset['flow']['value'])
            else:
                worksheet.write_column(3, 0, datetime_list)
                col = 0
                for idx, storage_asset in enumerate(assets_results_json[key]):
                    if all(key in storage_asset.keys() for key in ['label', KEY1, KEY2, KEY3, KEY4]):
                        worksheet.merge_range(0, col+1, 0, col+4, storage_asset['label'], merge_format)
                        
                        worksheet.write(1, col+1, KEY1)
                        worksheet.write(2, col+1, storage_asset[KEY1]['unit'])
                        worksheet.write_column(3, col+1, storage_asset[KEY1]['value'])

                        worksheet.write(1, col+2, KEY2)
                        worksheet.write(2, col+2, storage_asset[KEY2]['flow']['unit'])
                        worksheet.write_column(3, col+2, storage_asset[KEY2]['flow']['value'])

                        worksheet.write(1, col+3, KEY3)
                        worksheet.write(2, col+3, storage_asset[KEY3]['flow']['unit'])
                        worksheet.write_column(3, col+3, storage_asset[KEY3]['flow']['value'])

                        worksheet.write(1, col+4, KEY4)
                        worksheet.write(2, col+4, storage_asset[KEY4]['flow']['unit'])
                        worksheet.write_column(3, col+4, storage_asset[KEY3]['flow']['value'])

                        col+=5

        workbook.close()
        output.seek(0)

        filename = 'timeseries_results.xlsx'
        response = HttpResponse(
            output,
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = f'attachment; filename={filename}'

        return response
    except Exception as e:
        logger.error(f"Dashboard ERROR: Could not generate Timeseries Results file for the Scenario with Id: {scen_id}. Thrown Exception: {e}")
        raise Http404()

