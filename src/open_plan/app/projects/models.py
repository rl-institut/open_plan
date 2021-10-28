import uuid
import json
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from .constants import ASSET_CATEGORY, ASSET_TYPE, COUNTRY, CURRENCY, ENERGY_VECTOR, FLOW_DIRECTION, MVS_TYPE, SIMULATION_STATUS, TRUE_FALSE_CHOICES, USER_RATING




class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    feedback = models.TextField()
    rating = models.PositiveSmallIntegerField(choices=USER_RATING, null=True)



class EconomicData(models.Model):
    duration = models.PositiveSmallIntegerField()
    currency = models.CharField(max_length=3, choices=CURRENCY)
    discount = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    tax = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])


class Project(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=120)
    description = models.TextField()
    country = models.CharField(max_length=50, choices=COUNTRY)
    latitude = models.FloatField()
    longitude = models.FloatField()
    economic_data = models.OneToOneField(EconomicData, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    viewers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='viewer_projects')

    def __str__(self):
        return self.name


class Comment(models.Model):
    name = models.CharField(max_length=60)
    body = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Scenario(models.Model):
    name = models.CharField(max_length=60)

    start_date = models.DateTimeField()
    time_step = models.IntegerField(validators=[MinValueValidator(0)])
    capex_fix = models.FloatField(validators=[MinValueValidator(0.0)])
    capex_var = models.FloatField(validators=[MinValueValidator(0.0)])
    opex_fix = models.FloatField(validators=[MinValueValidator(0.0)])
    opex_var = models.FloatField(validators=[MinValueValidator(0.0)])
    evaluated_period = models.IntegerField(validators=[MinValueValidator(0)])
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class AssetType(models.Model):
    asset_type = models.CharField(max_length=30, choices=ASSET_TYPE, null=False, unique=True)
    asset_category = models.CharField(max_length=30, choices=ASSET_CATEGORY)
    energy_vector = models.CharField(max_length=20, choices=ENERGY_VECTOR)
    mvs_type = models.CharField(max_length=20, choices=MVS_TYPE)
    asset_fields = models.TextField(null=True)
    unit = models.CharField(max_length=30, null=True)


class TopologyNode(models.Model):
    name = models.CharField(max_length=60, null=False, blank=False)
    pos_x = models.FloatField(default=0.0)
    pos_y = models.FloatField(default=0.0)
    scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE,  null=False, blank=False)
    parent_asset = models.ForeignKey(to='Asset', on_delete=models.CASCADE, null=True, blank=True)
    class Meta:
        abstract = True


class ValueType(models.Model):
    type = models.CharField(max_length=30, null=False, unique=True)
    unit = models.CharField(max_length=30, null=True)


class Asset(TopologyNode):
    def save(self, *args, **kwargs):
        if self.asset_type.asset_type in ['dso', 'gas_dso', 'h2_dso', 'heat_dso']:
            self.optimize_cap = False
        super().save(*args, **kwargs)
    
    unique_id = models.CharField(max_length=120, default=uuid.uuid4, unique=True, editable=False)
    capex_fix = models.FloatField(null=True, blank=False, validators=[MinValueValidator(0.0)])  # development_costs
    capex_var = models.FloatField(null=True, blank=False, validators=[MinValueValidator(0.0)])  # specific_costs
    opex_fix = models.FloatField(null=True, blank=False, validators=[MinValueValidator(0.0)])  # specific_costs_om
    opex_var = models.FloatField(null=True, blank=False, validators=[MinValueValidator(0.0)])  # dispatch_price
    lifetime = models.IntegerField(null=True, blank=False, validators=[MinValueValidator(0)])
    input_timeseries = models.TextField(null=True, blank=False)#, validators=[validate_timeseries])
    crate = models.FloatField(null=True, blank=False, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    efficiency = models.FloatField(null=True, blank=False, validators=[MinValueValidator(0.0)])
    soc_max = models.FloatField(null=True, blank=False, validators=[MinValueValidator(0.0)])
    soc_min = models.FloatField(null=True, blank=False, validators=[MinValueValidator(0.0)])
    dispatchable = models.BooleanField(null=True, blank=False, choices=TRUE_FALSE_CHOICES, default=None)
    maximum_capacity = models.FloatField(null=True, blank=False, validators=[MinValueValidator(0.0)])
    energy_price = models.FloatField(null=True, blank=False, validators=[MinValueValidator(0.0)])
    feedin_tariff = models.FloatField(null=True, blank=False, validators=[MinValueValidator(0.0)])
    peak_demand_pricing = models.FloatField(null=True, blank=False, validators=[MinValueValidator(0.0)])
    peak_demand_pricing_period = models.SmallIntegerField(null=True, blank=False, validators=[MinValueValidator(0)])
    renewable_share = models.FloatField(null=True, blank=False, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    renewable_asset = models.BooleanField(null=True, blank=False, choices=TRUE_FALSE_CHOICES, default=None)
    asset_type = models.ForeignKey(AssetType, on_delete=models.CASCADE, null=False, blank=True)
    optimize_cap = models.BooleanField(null=True, blank=False, choices=TRUE_FALSE_CHOICES)
    installed_capacity = models.FloatField(null=True, blank=False, validators=[MinValueValidator(0.0)])
    age_installed = models.FloatField(null=True, blank=False, validators=[MinValueValidator(0.0)])
    
    @property
    def fields(self):
        return [f.name for f in self._meta.fields + self._meta.many_to_many]


class Bus(TopologyNode):
    type = models.CharField(max_length=20, choices=ENERGY_VECTOR)
    input_ports = models.IntegerField(null=False, default=1)
    output_ports = models.IntegerField(null=False, default=1)


class ConnectionLink(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, null=False)
    bus_connection_port = models.CharField(null=False, max_length=12)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, null=False)
    flow_direction = models.CharField(max_length=15, choices=FLOW_DIRECTION, null=False)
    scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE, null=False)


class Constraint(models.Model):
    scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE, null=False)
    activated = models.BooleanField(null=True, blank=False, choices=TRUE_FALSE_CHOICES, default=False)

    class Meta:
        abstract = True

class MinRenewableConstraint(Constraint):
    value = models.FloatField(null=False, blank=False, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)], default=0.2)
    unit = models.CharField(max_length=6, default='factor', editable=False)
    name = models.CharField(max_length=30, default='minimal_renewable_factor', editable=False)

class MaxEmissionConstraint(Constraint):
    value = models.FloatField(null=False, blank=False, validators=[MinValueValidator(0.0)], default=0.0)
    unit = models.CharField(max_length=9, default='kgCO2eq/a', editable=False)
    name = models.CharField(max_length=30, default='maximum_emissions', editable=False)

class MinDOAConstraint(Constraint):
    value = models.FloatField(null=False, blank=False, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)], default=0.3)
    unit = models.CharField(max_length=6, default='factor', editable=False)
    name = models.CharField(max_length=30, default='minimal_degree_of_autonomy', editable=False)

class NZEConstraint(Constraint):
    value = models.BooleanField(null=True, blank=False, choices=TRUE_FALSE_CHOICES, default=False)
    unit = models.CharField(max_length=4, default='bool', editable=False)
    name = models.CharField(max_length=30, default='net_zero_energy', editable=False)

class ScenarioFile(models.Model):
    title = models.CharField(max_length=50)
    file = models.FileField(upload_to='tempFiles/', null=True, blank=True)


class Simulation(models.Model):
    start_date = models.DateTimeField(auto_now_add=True, null=False)
    end_date = models.DateTimeField(null=True)
    elapsed_seconds = models.FloatField(null=True)
    mvs_token = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=20, choices=SIMULATION_STATUS, null=False)
    scenario = models.OneToOneField(Scenario, on_delete=models.CASCADE, null=False)
    user_rating = models.PositiveSmallIntegerField(null=True, choices=USER_RATING, default=None)
    results = models.TextField(null=True, max_length=30e6)
    errors = models.TextField(null=True)
