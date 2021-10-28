import csv
import pickle
import os

from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column, Field, Fieldset, ButtonHolder
from django import forms
from django.forms import ModelForm
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.staticfiles.storage import staticfiles_storage
from projects.models import *
from projects.constants import MAP_EPA_MVS

from django.utils.translation import ugettext_lazy as _
from django.conf import settings as django_settings

PARAMETERS = {}
with open(staticfiles_storage.path("MVS_parameters_list.csv")) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for i, row in enumerate(csvreader):
        if i == 0:
            hdr = row
            label_idx = hdr.index("label")
        else:
            label = row[label_idx]
            PARAMETERS[label] = {k: v for k, v in zip(hdr, row)}

def gettext_variables(some_string, lang="de"):
    """Save some expressions to be translated to a temporary file
        Because django makemessages cannot detect gettext with variables
    """

    some_string = str(some_string)

    trans_file = os.path.join(django_settings.STATIC_ROOT, f'personal_translation_{lang}.pickle')

    if os.path.exists(trans_file):
        with open(trans_file, 'rb') as handle:
            trans_dict = pickle.load(handle)
    else:
        trans_dict = {}

    if some_string is not None:
        if some_string not in trans_dict:
            trans_dict[some_string] = ""

        with open(trans_file, 'wb') as handle:
            pickle.dump(trans_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)


for label in PARAMETERS:
    gettext_variables(PARAMETERS[label][":Definition:"])
    gettext_variables(PARAMETERS[label][":Unit:"])


def get_parameter_info(param_name, parameters=PARAMETERS):
    param_name = MAP_EPA_MVS.get(param_name, param_name)
    help_text = None
    unit = None
    verbose = None
    if param_name in PARAMETERS:
        print(param_name)
        help_text = PARAMETERS[param_name][":Definition:"]
        unit = PARAMETERS[param_name][":Unit:"]
        verbose = PARAMETERS[param_name]["verbose"]
        if unit == "None":
            unit = None
        elif unit == "Factor":
            unit = ""
        if verbose == "None":
            verbose = None
    else:
        print(f"{param_name} is not within range")

    return help_text, unit, verbose


class OpenPlanModelForm(ModelForm):
    """Class to automatize the assignation and translation of the labels, help_text and units"""
    def __init__(self, *args, **kwargs):
        super(OpenPlanModelForm, self).__init__(*args, **kwargs)
        for fieldname, field in self.fields.items():
            help_text, unit, verbose = get_parameter_info(fieldname)

            if verbose is not None:
                field.label = verbose
            if unit is not None:
                field.label = _(str(field.label)) + " (" + _(unit) + ")"
            else:
                field.label = _(str(field.label))

            if help_text is not None:
                field.help_text = _(help_text)

class OpenPlanForm(forms.Form):
    """Class to automatize the assignation and translation of the labels, help_text and units"""
    def __init__(self, *args, **kwargs):
        super(OpenPlanForm, self).__init__(*args, **kwargs)
        for fieldname, field in self.fields.items():
            help_text, unit, verbose = get_parameter_info(fieldname)

            if verbose is not None:
                field.label = verbose

            if unit is not None:
                field.label = _(str(field.label)) + " (" + _(unit) + ")"
            else:
                field.label = _(str(field.label))

            if help_text is not None:
                field.help_text = _(help_text)

class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        exclude=['id', 'rating']



class ProjectDetailForm(ModelForm):
    class Meta:
        model = Project
        exclude = ['date_created', 'date_updated', 'economic_data', 'user', 'viewers']

    def __init__(self, *args, **kwargs):
        super(ProjectDetailForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.disabled = True


class EconomicDataDetailForm(OpenPlanModelForm):
    class Meta:
        model = EconomicData
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EconomicDataDetailForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.disabled = True


economic_widgets = {
    'discount': forms.NumberInput(attrs={'placeholder': _('eg. 0.1'), 'min':'0.0', 'max':'1.0', 'step':'0.0001',
                                            'title': _('Investment Discount factor.')}),
    'tax': forms.NumberInput(attrs={'placeholder': 'eg. 0.3', 'min':'0.0', 'max':'1.0', 'step':'0.0001'}),
}

class EconomicDataUpdateForm(OpenPlanModelForm):
    class Meta:
        model = EconomicData
        fields = '__all__'
        widgets = economic_widgets


class ProjectCreateForm(OpenPlanForm):
    name = forms.CharField(label=_('Project Name'), widget=forms.TextInput(attrs={'placeholder': 'Name...', 'data-toggle': 'tooltip', 'title': _('A self explanatory name for the project.')}))
    description = forms.CharField(label=_('Project Description'),
                                  widget=forms.Textarea(attrs={'placeholder': 'More detailed description here...', 'data-toggle': 'tooltip', 'title': _('A description of what this project objectives or test cases.')}))
    country = forms.ChoiceField(label=_('Country'), choices=COUNTRY,
        widget=forms.Select(attrs={'data-toggle': 'tooltip', 'title': _('Name of the country where the project is being deployed')}))
    longitude = forms.FloatField(label=_('Location, longitude'),
                                 widget=forms.NumberInput(attrs={'placeholder': 'click on the map', 'readonly': '', 
                                 'data-toggle': 'tooltip', 'title': _("Longitude coordinate of the project's geographical location.")}))
    latitude = forms.FloatField(label=_('Location, latitude'),
                                widget=forms.NumberInput(attrs={'placeholder': 'click on the map', 'readonly': '',
                                'data-toggle': 'tooltip', 'title': _("Latitude coordinate of the project's geographical location.")}))
    duration = forms.IntegerField(label=_('Project Duration'),
                                  widget=forms.NumberInput(attrs={'placeholder': 'eg. 1', 'min':'0', 'max':'100', 'step':'1', 'data-toggle': 'tooltip',
                                  'title': _("The number of years the project is intended to be operational. The project duration also sets the installation time of the assets used in the simulation. After the project ends these assets are 'sold' and the refund is charged against the initial investment costs.")}))
    currency = forms.ChoiceField(label=_('Currency'), choices=CURRENCY,
        widget=forms.Select(attrs={'data-toggle': 'tooltip', 'title': _('The currency of the country where the project is implemented.')}))
    discount = forms.FloatField(label=_('Discount Factor'),
                                  widget=forms.NumberInput(attrs={'placeholder': 'eg. 0.1', 'min':'0.0', 'max':'1.0', 'step':'0.0001',
                                  'data-toggle': 'tooltip', 'title': _('Discount factor is the factor which accounts for the depreciation in the value of money in the future, compared to the current value of the same money. The common method is to calculate the weighted average cost of capital (WACC) and use it as the discount rate.')}))
    tax = forms.FloatField(label=_('Tax'),
                             widget=forms.NumberInput(attrs={'placeholder': 'eg. 0.3', 'min':'0.0', 'max':'1.0', 'step':'0.0001',
                             'data-toggle': 'tooltip', 'title': _('Tax factor')}))
    
    # Render form
    def __init__(self, *args, **kwargs):
        super(ProjectCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'project_form_id'
        # self.helper.form_class = 'blueForm'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-8'
        self.helper.field_class = 'col-lg-10'


class ProjectUpdateForm(OpenPlanModelForm):
    class Meta:
        model = Project
        exclude = ['date_created', 'date_updated', 'economic_data', 'user', 'viewers']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ['id', 'project']

# region Scenario
# TODO build this from the documentation with a for loop over the keys
scenario_widgets = {
    'name': forms.TextInput(attrs={'placeholder': 'Scenario name'}),
    'start_date': forms.DateInput(format='%Y-%m-%d',
                                  attrs={'class': 'TestDateClass', 'placeholder': 'Select a start date', 'type': 'date'}),
    'time_step': forms.NumberInput(attrs={'placeholder': 'eg. 120 minutes', 'min':'1', 'max':'600', 'step':'1', 'data-toggle': 'tooltip',
                                          'title': _('Length of the time-steps.')}),
    'evaluated_period': forms.NumberInput(attrs={'placeholder': 'eg. 10 days', 'min':'1', 'step':'1', 'data-toggle': 'tooltip',
                                                 'title': _("The number of days simulated with the energy system model.")}),
    'capex_fix': forms.NumberInput(attrs={'placeholder': 'e.g. 10000€', 'min':'0', 'data-toggle': 'tooltip',
                                          'title': _('A fixed cost to implement the asset, eg. planning costs which do not depend on the (optimized) asset capacity.')}),
    'capex_var': forms.NumberInput(attrs={'placeholder': 'e.g. 1000€', 'min':'0', 'data-toggle': 'tooltip',
                                          'title': _(' Actual CAPEX of the asset, i.e., specific investment costs')}),
    'opex_fix': forms.NumberInput(attrs={'placeholder': 'e.g. 0€', 'min':'0', 'data-toggle': 'tooltip',
                                         'title': _('Actual OPEX of the asset, i.e., specific operational and maintenance costs.')}),
    'opex_var': forms.NumberInput(attrs={'placeholder': 'e.g. 0.6€/kWh', 'min':'0', 'step':'0.00001', 'data-toggle': 'tooltip',
                                         'title': _('Variable cost associated with a flow through/from the asset.')}),
}

scenario_labels = {
    "project": _("Project"),
    "name": _("Scenario name"),
    'evaluated_period': _("Evaluated Period"),
    "time_step": _("Time Step"),
    "start_date": _("Start Date"),
    "capex_fix": _("Development costs"),
    "capex_var": _("Specific costs"),
    "opex_fix": _("Specific OM costs"),
    "opex_var": _("Dispatch price"),
}

scenario_field_order = ["project", "name", "evaluated_period", "time_step", "start_date", "capex_fix", "capex_var", "opex_fix", "opex_var"]

class ScenarioCreateForm(OpenPlanModelForm):
    field_order = scenario_field_order
    class Meta:
        model = Scenario
        exclude = ['id']
        widgets = scenario_widgets
        labels = scenario_labels

    def __init__(self, *args, **kwargs):
        project_queryset = kwargs.pop("project_queryset", None)
        super().__init__(*args, **kwargs)
        if project_queryset is not None:
            self.fields["project"].queryset = project_queryset
        else:
            self.fields["project"] = forms.ChoiceField(label="Project", choices=())
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class ScenarioUpdateForm(OpenPlanModelForm):
    field_order = scenario_field_order
    class Meta:
        model = Scenario
        exclude = ['id']
        widgets = scenario_widgets
        labels = scenario_labels

    def __init__(self, *args, **kwargs):
        project_queryset = kwargs.pop("project_queryset", None)
        super().__init__(*args, **kwargs)
        if project_queryset is not None:
            self.fields["project"].queryset = project_queryset
        else:
            self.fields["project"] = forms.ChoiceField(label="Project", choices=())

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_tag = False  # don't include <form> tag

# endregion Scenario


class MinRenewableConstraintForm(OpenPlanModelForm):
    class Meta:
        model = MinRenewableConstraint
        exclude = ['scenario']

class MaxEmissionConstraintForm(OpenPlanModelForm):
    class Meta:
        model = MaxEmissionConstraint
        exclude = ['scenario']


class MinDOAConstraintForm(OpenPlanModelForm):
    class Meta:
        model = MinDOAConstraint
        exclude = ['scenario']

class NZEConstraintForm(OpenPlanModelForm):
    class Meta:
        model = NZEConstraint
        exclude = ['scenario']




class BusForm(OpenPlanModelForm):
    def __init__(self, *args, **kwargs):
        bus_type_name = kwargs.pop('asset_type', None) # always = bus
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({f'df-{field}': ''})
    
    class Meta:
        model = Bus
        fields = ['name', 'type']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Bus Name',
                                           'style': 'font-weight:400; font-size:13px;'}),
            'type': forms.Select(choices=ENERGY_VECTOR,
                                    attrs={'data-toggle': 'tooltip', 'title': _('The energy Vector of the connected assets.'),
                                        'style': 'font-weight:400; font-size:13px;'})
        }
        labels = {
            "name": _("Name"),
            "type": _("Energy carrier"),
        }


class AssetCreateForm(OpenPlanModelForm):

    def __init__(self, *args, **kwargs):
        asset_type_name = kwargs.pop('asset_type', None)
        super().__init__(*args, **kwargs)
        asset_type = AssetType.objects.get(asset_type=asset_type_name)
        [self.fields.pop(field) for field in list(self.fields) if field not in asset_type.asset_fields]
        ''' DrawFlow specific configuration, add a special attribute to 
            every field in order for the framework to be able to export
            the data to json.
            !! This addition doesn't affect the previous behavior !!
        '''
        for field in self.fields:
            self.fields[field].widget.attrs.update({f'df-{field}': ''})
        ''' ----------------------------------------------------- '''

    def clean_input_timeseries(self):
        try:
            timeseries_file_str = self.files['input_timeseries'].read().decode('utf-8')
            input_timeseries_values = json.loads(timeseries_file_str)
            return input_timeseries_values
        except json.decoder.JSONDecodeError as ex:
            raise ValidationError(_("File not properly formatted. Please ensure you upload a comma seperated array of values. E.g. [1,2,0.32]"))
        except Exception as ex:
            raise ValidationError(_("Could not parse a file. Did you upload one?"))

    class Meta:
        model = Asset
        exclude = ['scenario']
        widgets = {
            'optimize_cap': forms.Select(choices=TRUE_FALSE_CHOICES,
                                         attrs={'data-toggle': 'tooltip', 'title': _('True if the user wants to perform capacity optimization for various components as part of the simulation.'),
                                                'style': 'font-weight:400; font-size:13px;'}),
            'dispatchable': forms.Select(choices=TRUE_FALSE_CHOICES),
            'renewable_asset': forms.Select(choices=TRUE_FALSE_CHOICES, 
                                            attrs={'data-toggle': 'tooltip', 'title': _('Indicate if the asset is renewable or not.'),
                                                'style': 'font-weight:400; font-size:13px;'}),
            'name': forms.TextInput(attrs={'placeholder': 'Asset Name',
                                           'style': 'font-weight:400; font-size:13px;'}),
            'capex_fix': forms.NumberInput(attrs={'placeholder': 'e.g. 10000', 'min': '0.0', 'step': '.01',
                                                  'data-toggle': 'tooltip', 'title': _(' A fixed cost to implement the asset, eg. planning costs which do not depend on the (optimized) asset capacity.'),
                                                  'style': 'font-weight:400; font-size:13px;'}),
            'capex_var': forms.NumberInput(attrs={'placeholder': 'e.g. 4000', 'min': '0.0', 'step': '.01',
                                                  'data-toggle': 'tooltip', 'title': _(' Actual CAPEX of the asset, i.e., specific investment costs.'),
                                                  'style': 'font-weight:400; font-size:13px;'}),
            'opex_fix': forms.NumberInput(attrs={'placeholder': 'e.g. 0', 'min': '0.0', 'step': '.01',
                                                 'data-toggle': 'tooltip', 'title': _('Actual OPEX of the asset, i.e., specific operational and maintenance costs.'),
                                                 'style': 'font-weight:400; font-size:13px;'}),
            'opex_var': forms.NumberInput(attrs={'placeholder': 'Currency', 'min': '0.0', 'step': '.01',
                                                 'data-toggle': 'tooltip', 'title': _('Variable cost associated with a flow through/from the asset.'),
                                                 'style': 'font-weight:400; font-size:13px;'}),
            'lifetime': forms.NumberInput(attrs={'placeholder': 'e.g. 10 years', 'min': '0', 'step': '1',
                                                 'data-toggle': 'tooltip', 'title': _('Number of operational years of the asset until it has to be replaced.'),
                                                 'style': 'font-weight:400; font-size:13px;'}),
            # TODO: Try changing this to FileInput
            'input_timeseries': forms.FileInput(),
            # 'input_timeseries': forms.Textarea(attrs={'placeholder': 'e.g. [4,3,2,5,3,...]',
            #                                           'style': 'font-weight:400; font-size:13px;'}),
            'crate': forms.NumberInput(attrs={'placeholder': 'factor of total capacity (kWh), e.g. 0.7', 'min': '0.0', 'max': '1.0', 'step': '.0001',
                                              'data-toggle': 'tooltip', 'title': _('C-rate is the rate at which the storage can charge or discharge relative to the nominal capacity of the storage. A c-rate of 1 implies that the battery can discharge or charge completely in a single timestep.'),
                                              'style': 'font-weight:400; font-size:13px;'}),
            'efficiency': forms.NumberInput(attrs={'placeholder': 'e.g. 0.99',
                                                   'data-toggle': 'tooltip', 'title': _('Ratio of energy output/energy input.'),
                                                   'style': 'font-weight:400; font-size:13px;', 'min': '0.0', 'step': '.0001'}),
            'soc_max': forms.NumberInput(attrs={'placeholder': 'e.g. 190', 'min': '0.0', 'step': '.01',
                                                'data-toggle': 'tooltip', 'title': _('The maximum permissible level of charge in the battery (generally, it is when the battery is filled to its nominal capacity), represented by the value 1.0. Users can  also specify a certain value as a factor of the actual capacity.'),
                                                'style': 'font-weight:400; font-size:13px;'}),
            'soc_min': forms.NumberInput(attrs={'placeholder': 'e.g. 20', 'min': '0.0', 'step': '.01',
                                                'data-toggle': 'tooltip', 'title': _('The minimum permissible level of charge in the battery as a factor of the nominal capacity of the battery.'),
                                                'style': 'font-weight:400; font-size:13px;'}),
            'maximum_capacity': forms.NumberInput(attrs={'placeholder': 'e.g. 1000', 'min': '0.0', 'step': '.01',
                                                         'data-toggle': 'tooltip', 'title': _('The maximum installable capacity.'),
                                                         'style': 'font-weight:400; font-size:13px;'}),
            'energy_price': forms.NumberInput(attrs={'placeholder': 'e.g. 0.1', 'min': '0.0', 'step': '.0001',
                                                     'data-toggle': 'tooltip', 'title': _('Price of electricity sourced from the utility grid.'),
                                                     'style': 'font-weight:400; font-size:13px;'}),
            'feedin_tariff': forms.NumberInput(attrs={'placeholder': 'e.g. 0.0', 'min': '0.0', 'step': '.0001',
                                                      'data-toggle': 'tooltip', 'title': _('Price received for feeding electricity into the grid.'),
                                                      'style': 'font-weight:400; font-size:13px;'}),
            'peak_demand_pricing': forms.NumberInput(attrs={'placeholder': 'e.g. 60', 'min': '0.0', 'step': '.01',
                                                            'data-toggle': 'tooltip', 'title': _('Price to be paid additionally for energy-consumption based on the peak demand of a period.'),
                                                            'style': 'font-weight:400; font-size:13px;'}),
            'peak_demand_pricing_period': forms.NumberInput(attrs={'placeholder': 'times per year, e.g. 2',
                                                                   'data-toggle': 'tooltip', 'title': _('Number of reference periods in one year for the peak demand pricing. Only one of the following are acceptable values: 1 (yearly), 2, 3 ,4, 6, 12 (monthly).'),
                                                                   'style': 'font-weight:400; font-size:13px;', 'min': '1', 'max': '12', 'step': '1'}),
            'renewable_share': forms.NumberInput(attrs={'placeholder': 'e.g. 0.1', 'min': '0.0', 'max': '1.0', 'step': '.0001',
                                                        'data-toggle': 'tooltip', 'title': 'The share of renewables in the generation mix of the energy supplied by the DSO (utility).',
                                                        'style': 'font-weight:400; font-size:13px;'}),
            'installed_capacity': forms.NumberInput(attrs={'placeholder': 'e.g. 50', 'min': '0.0', 'step': '.01',
                                                           'data-toggle': 'tooltip', 'title': _('The already existing installed capacity in-place, which will also be replaced after its lifetime.'),
                                                           'style': 'font-weight:400; font-size:13px;'}),
            'age_installed': forms.NumberInput(attrs={'placeholder': 'e.g. 10', 'min': '0.0', 'step': '1',
                                                      'data-toggle': 'tooltip', 'title': _('The number of years the asset has already been in operation.'),
                                                      'style': 'font-weight:400; font-size:13px;'}),
        }
        labels = {
            "name": _("Name"),
            "optimize_cap": _("Optimize cap"),
            "dispatchable": _("Dispatchable"),
            "renewable_asset": _("Renewable asset"),
            "capex_fix": _("Development costs"),
            "capex_var": _("Specific costs"),
            "opex_fix": _("Specific OM costs"),
            "opex_var": _("Dispatch price"),
            "lifetime": _("Asset Lifetime"),
            "input_timeseries": _("Timeseries vector"),
            "crate": _("Crate"),
            "efficiency": _("Efficiency"),
            "soc_max": _("SoC max"),
            "soc_min": _("SoC min"),
            "maximum_capacity": _("Maximum capacity"),
            "energy_price": _("Energy price"),
            "feedin_tariff": _("Feedin tariff"),
            "peak_demand_pricing": _("Peak demand pricing"),
            "peak_demand_pricing_period": _("Peak demand pricing period (times/year)"),
            "renewable_share": _("Renewable share"),
            "installed_capacity": _("installed capacity (kW)"),
            "age_installed": _("Age installed"),
        }


class StorageForm(OpenPlanForm):
    # ESS fields
    name = forms.CharField(label=_('ESS Name'), widget=forms.TextInput(attrs={'placeholder': 'Name...', 'data-toggle': 'tooltip', 'title': _('A mnemonic name for the ESS unit.')}))
    # Charging Power Fields - chp_... = discharging power
    # region charging power
    chp_installed_capacity = forms.FloatField(
        label=_('installed capacity (kW)'),
        widget=forms.NumberInput(attrs={
            'placeholder': 'e.g. 50', 'min': '0.0', 'step': '.01',
            'data-toggle': 'tooltip', 'title': _('The already existing installed capacity in-place, which will also be replaced after its lifetime.'),
            'style': 'font-weight:400; font-size:13px;'
        }),
        validators=[MinValueValidator(0.0)])
    chp_age_installed = forms.IntegerField(
        label=_('Age installed'),
        widget=forms.NumberInput(attrs={
            'placeholder': 'e.g. 10', 'min': '0.0', 'step': '1',
            'data-toggle': 'tooltip', 'title': _('The number of years the asset has already been in operation.'),
            'style': 'font-weight:400; font-size:13px;'
        }),
        validators=[MinValueValidator(0)])
    chp_capex_fix = forms.FloatField(
        label=_('Development costs'),
        widget=forms.NumberInput(attrs={
            'placeholder': 'e.g. 10000', 'min': '0.0', 'step': '.01',
            'data-toggle': 'tooltip', 'title': _(' A fixed cost to implement the asset, eg. planning costs which do not depend on the (optimized) asset capacity.'),
            'style': 'font-weight:400; font-size:13px;'
        }),
        validators=[MinValueValidator(0.0)])
    chp_capex_var = forms.FloatField(
        label=_('Specific costs'),
        widget=forms.NumberInput(attrs={
            'placeholder': 'e.g. 4000', 'min': '0.0', 'step': '.01',
            'data-toggle': 'tooltip', 'title': _(' Actual CAPEX of the asset, i.e., specific investment costs'),
            'style': 'font-weight:400; font-size:13px;'
        }),
        validators=[MinValueValidator(0.0)])
    chp_opex_fix = forms.FloatField(
        label=_('Specific OM costs'),
        widget=forms.NumberInput(attrs={
            'placeholder': 'e.g. 0', 'min': '0.0', 'step': '.01',
            'data-toggle': 'tooltip', 'title': _('Actual OPEX of the asset, i.e., specific operational and maintenance costs.'),
            'style': 'font-weight:400; font-size:13px;'
        }),
        validators=[MinValueValidator(0.0)])
    chp_opex_var = forms.FloatField(
        label=_('Dispatch price'),
        widget=forms.NumberInput(attrs={
            'placeholder': 'Currency', 'min': '0.0', 'step': '.01',
            'data-toggle': 'tooltip', 'title': _('Variable cost associated with a flow through/from the asset.'),
            'style': 'font-weight:400; font-size:13px;'
        }),
        validators=[MinValueValidator(0.0)])
    chp_lifetime = forms.IntegerField(
        label=_('Asset Lifetime'),
        widget=forms.NumberInput(attrs={
            'placeholder': 'e.g. 10 years', 'min': '0', 'step': '1',
            'data-toggle': 'tooltip', 'title': _('Number of operational years of the asset until it has to be replaced.'),
            'style': 'font-weight:400; font-size:13px;'
        }),
        validators=[MinValueValidator(0)])
    chp_crate = forms.FloatField(
        label=_('Crate'),
        widget=forms.NumberInput(attrs={
            'placeholder': 'factor of total capacity (kWh), e.g. 0.7', 'min': '0.0', 'max': '1.0', 'step': '.0001',
            'data-toggle': 'tooltip', 'title': _('C-rate is the rate at which the storage can charge or discharge relative to the nominal capacity of the storage. A c-rate of 1 implies that the battery can discharge or charge completely in a single timestep.'),
            'style': 'font-weight:400; font-size:13px;'}),
        validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    chp_efficiency = forms.FloatField(
        label=_('Efficiency'),
        widget=forms.NumberInput(attrs={
            'placeholder': 'e.g. 0.99',
            'data-toggle': 'tooltip', 'title': _('Ratio of energy output/energy input.'),
            'style': 'font-weight:400; font-size:13px;', 'min': '0.0', 'max': '1.0', 'step': '.0001'}),
        validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    chp_dispatchable = forms.ChoiceField(
        label=_('Dispatchable'),
        choices=TRUE_FALSE_CHOICES,
        widget=forms.Select(attrs={
            'style': 'font-weight:400; font-size:13px;'
        }))
    # endregion charging power
    
    # Discharging Power Fields - dchp_... = discharging power
    # region Discharging power
    dchp_installed_capacity = forms.FloatField(
        label=_('installed capacity (kW)'),
        widget=forms.NumberInput(attrs={
            'placeholder': 'e.g. 50', 'min': '0.0', 'step': '.01',
            'data-toggle': 'tooltip', 'title': _('The already existing installed capacity in-place, which will also be replaced after its lifetime.'),
            'style': 'font-weight:400; font-size:13px;'
        }),
        validators=[MinValueValidator(0.0)])
    dchp_age_installed = forms.IntegerField(
        label=_('Age installed'),
        widget=forms.NumberInput(attrs={
            'placeholder': 'e.g. 10', 'min': '0.0', 'step': '1',
            'data-toggle': 'tooltip', 'title': _('The number of years the asset has already been in operation.'),
            'style': 'font-weight:400; font-size:13px;'
        }),
        validators=[MinValueValidator(0)])
    dchp_capex_fix = forms.FloatField(
        label=_('Development costs'),
        widget=forms.NumberInput(attrs={
            'placeholder': 'e.g. 10000', 'min': '0.0', 'step': '.01',
            'data-toggle': 'tooltip', 'title': _(' A fixed cost to implement the asset, eg. planning costs which do not depend on the (optimized) asset capacity.'),
            'style': 'font-weight:400; font-size:13px;'
        }),
        validators=[MinValueValidator(0.0)])
    dchp_capex_var = forms.FloatField(
        label=_('Specific costs'),
        widget=forms.NumberInput(attrs={
            'placeholder': 'e.g. 4000', 'min': '0.0', 'step': '.01',
            'data-toggle': 'tooltip', 'title': _(' Actual CAPEX of the asset, i.e., specific investment costs'),
            'style': 'font-weight:400; font-size:13px;'
        }),
        validators=[MinValueValidator(0.0)])
    dchp_opex_fix = forms.FloatField(
        label=_('Specific OM costs'),
        widget=forms.NumberInput(attrs={
            'placeholder': 'e.g. 0', 'min': '0.0', 'step': '.01',
            'data-toggle': 'tooltip', 'title': _('Actual OPEX of the asset, i.e., specific operational and maintenance costs.'),
            'style': 'font-weight:400; font-size:13px;'
        }),
        validators=[MinValueValidator(0.0)])
    dchp_opex_var = forms.FloatField(
        label=_('Dispatch price'),
        widget=forms.NumberInput(attrs={
            'placeholder': 'Currency', 'min': '0.0', 'step': '.01',
            'data-toggle': 'tooltip', 'title': _('Variable cost associated with a flow through/from the asset.'),
            'style': 'font-weight:400; font-size:13px;'
        }),
        validators=[MinValueValidator(0.0)])
    dchp_lifetime = forms.IntegerField(
        label=_('Asset Lifetime'),
        widget=forms.NumberInput(attrs={
            'placeholder': 'e.g. 10 years', 'min': '0', 'step': '1',
            'data-toggle': 'tooltip', 'title': _('Number of operational years of the asset until it has to be replaced.'),
            'style': 'font-weight:400; font-size:13px;'
        }),
        validators=[MinValueValidator(0)])
    dchp_crate = forms.FloatField(
        label=_('Crate'),
        widget=forms.NumberInput(attrs={
            'placeholder': 'factor of total capacity (kWh), e.g. 0.7', 'min': '0.0', 'max': '1.0', 'step': '.0001',
            'data-toggle': 'tooltip', 'title': _('C-rate is the rate at which the storage can charge or discharge relative to the nominal capacity of the storage. A c-rate of 1 implies that the battery can discharge or charge completely in a single timestep.'),
            'style': 'font-weight:400; font-size:13px;'}),
        validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    dchp_efficiency = forms.FloatField(
        label=_('Efficiency'),
        widget=forms.NumberInput(attrs={
            'placeholder': 'e.g. 0.99',
            'data-toggle': 'tooltip', 'title': _('Ratio of energy output/energy input.'),
            'style': 'font-weight:400; font-size:13px;', 'min': '0.0', 'max': '1.0', 'step': '.0001'}),
        validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    dchp_dispatchable = forms.ChoiceField(
        label=_('Dispatchable'),
        choices=TRUE_FALSE_CHOICES,
        widget=forms.Select(attrs={
            'style': 'font-weight:400; font-size:13px;'
        }))
    # endregion Discharging power

    
    # Capacity Fields - cp_... = capacity
    # region Capacity
    cp_installed_capacity = forms.FloatField(
        label=_('installed capacity (kW)'),
        widget=forms.NumberInput(attrs={
            'placeholder': 'e.g. 50', 'min': '0.0', 'step': '.01',
            'data-toggle': 'tooltip', 'title': _('The already existing installed capacity in-place, which will also be replaced after its lifetime.'),
            'style': 'font-weight:400; font-size:13px;'
        }),
        validators=[MinValueValidator(0.0)])
    cp_age_installed = forms.IntegerField(
        label=_('Age installed'),
        widget=forms.NumberInput(attrs={
            'placeholder': 'e.g. 10', 'min': '0.0', 'step': '1',
            'data-toggle': 'tooltip', 'title': _('The number of years the asset has already been in operation.'),
            'style': 'font-weight:400; font-size:13px;'
        }),
        validators=[MinValueValidator(0)])
    cp_capex_fix = forms.FloatField(
        label=_('Development costs'),
        widget=forms.NumberInput(attrs={
            'placeholder': 'e.g. 10000', 'min': '0.0', 'step': '.01',
            'data-toggle': 'tooltip', 'title': _(' A fixed cost to implement the asset, eg. planning costs which do not depend on the (optimized) asset capacity.'),
            'style': 'font-weight:400; font-size:13px;'
        }),
        validators=[MinValueValidator(0.0)])
    cp_capex_var = forms.FloatField(
        label=_('Specific costs'),
        widget=forms.NumberInput(attrs={
            'placeholder': 'e.g. 4000', 'min': '0.0', 'step': '.01',
            'data-toggle': 'tooltip', 'title': _(' Actual CAPEX of the asset, i.e., specific investment costs'),
            'style': 'font-weight:400; font-size:13px;'
        }),
        validators=[MinValueValidator(0.0)])
    cp_opex_fix = forms.FloatField(
        label=_('Specific OM costs'),
        widget=forms.NumberInput(attrs={
            'placeholder': 'e.g. 0', 'min': '0.0', 'step': '.01',
            'data-toggle': 'tooltip', 'title': _('Actual OPEX of the asset, i.e., specific operational and maintenance costs.'),
            'style': 'font-weight:400; font-size:13px;'
        }),
        validators=[MinValueValidator(0.0)])
    cp_opex_var = forms.FloatField(
        label=_('Dispatch price'),
        widget=forms.NumberInput(attrs={
            'placeholder': 'Currency', 'min': '0.0', 'step': '.01',
            'data-toggle': 'tooltip', 'title': _('Variable cost associated with a flow through/from the asset.'),
            'style': 'font-weight:400; font-size:13px;'
        }),
        validators=[MinValueValidator(0.0)])
    cp_lifetime = forms.IntegerField(
        label=_('Asset Lifetime'),
        widget=forms.NumberInput(attrs={
            'placeholder': 'e.g. 10 years', 'min': '0', 'step': '1',
            'data-toggle': 'tooltip', 'title': _('Number of operational years of the asset until it has to be replaced.'),
            'style': 'font-weight:400; font-size:13px;'
        }),
        validators=[MinValueValidator(0)])
    cp_crate = forms.FloatField(
        label=_('Crate'),
        widget=forms.NumberInput(attrs={
            'placeholder': 'factor of total capacity (kWh), e.g. 0.7', 'min': '0.0', 'max': '1.0', 'step': '.0001',
            'data-toggle': 'tooltip', 'title': _('C-rate is the rate at which the storage can charge or discharge relative to the nominal capacity of the storage. A c-rate of 1 implies that the battery can discharge or charge completely in a single timestep.'),
            'style': 'font-weight:400; font-size:13px;'}),
        validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    cp_efficiency = forms.FloatField(
        label=_('Efficiency'),
        widget=forms.NumberInput(attrs={
            'placeholder': 'e.g. 0.99',
            'data-toggle': 'tooltip', 'title': _('Ratio of energy output/energy input.'),
            'style': 'font-weight:400; font-size:13px;', 'min': '0.0', 'max': '1.0', 'step': '.0001'}),
        validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    cp_dispatchable = forms.ChoiceField(
        label=_('Dispatchable'),
        choices=TRUE_FALSE_CHOICES,
        widget=forms.Select(attrs={
            'style': 'font-weight:400; font-size:13px;'
        }))
    cp_optimize_cap = forms.ChoiceField(
        label=_('Optimize cap'),
        choices=TRUE_FALSE_CHOICES, 
        widget=forms.Select(attrs={
            'data-toggle': 'tooltip', 'title': _('True if the user wants to perform capacity optimization for various components as part of the simulation.'),
            'style': 'font-weight:400; font-size:13px;'}))
    cp_soc_max = forms.FloatField(
        label=_('SoC max'),
        widget=forms.NumberInput(attrs={
            'placeholder': 'e.g. 190', 'min': '0.0', 'step': '.01',
            'data-toggle': 'tooltip', 'title': _('The maximum permissible level of charge in the battery (generally, it is when the battery is filled to its nominal capacity), represented by the value 1.0. Users can  also specify a certain value as a factor of the actual capacity.'),
            'style': 'font-weight:400; font-size:13px;'}),
        validators=[MinValueValidator(0.0)])
    cp_soc_min = forms.FloatField(
        label=_('SoC min'),
        widget=forms.NumberInput(attrs={
            'placeholder': 'e.g. 20', 'min': '0.0', 'step': '.01',
            'data-toggle': 'tooltip', 'title': _('The minimum permissible level of charge in the battery as a factor of the nominal capacity of the battery.'),
            'style': 'font-weight:400; font-size:13px;'}),
        validators=[MinValueValidator(0.0)])
    # endregion Capacity

    
    # Render form
    def __init__(self, *args, **kwargs):
        storage_asset_type_name = kwargs.pop('asset_type', None) # b(attery)ess or h(eat)ess or g(ass)ess or ... 
        super(StorageForm, self).__init__(*args, **kwargs)
        [self.fields[field].widget.attrs.update({f'df-{field}': ''}) for field in self.fields]
        # self.helper = FormHelper()
        # self.helper.form_id = 'storage_form_id'
        # self.helper.form_class = 'blueForm'
        # self.helper.form_method = 'post'
        # self.helper.add_input(Submit('submit', 'Save'))
        # self.helper.form_class = 'form-horizontal'
        # self.helper.label_class = 'col-lg-8'
        # self.helper.field_class = 'col-lg-10'




