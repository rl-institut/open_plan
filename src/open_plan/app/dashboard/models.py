from django.db import models
from projects.models import Simulation

KPI_COSTS_TOOLTIPS = {
    "Replacement_costs_during_project_lifetime": "Costs for replacement of assets which occur over the project lifetime.",
    "annuity_om": "Annuity of the operation, maintenance and dispatch costs of the energy system, ie. Ballpoint number of the annual expenses for system operation.",
    "annuity_total": "Annuity of the net present costs (NPC) of the energy system.", 
    "costs_cost_om": "Costs for fix annual operation and maintenance costs over the whole project lifetime, that do not depend on the assets dispatch but solely on installed capacity.",
    "costs_dispatch": "Dispatch costs over the whole project lifetime including all expenditures that depend on the dispatch of assets, ie. fuel costs, electricity consumption from the external grid, costs for operation and maintainance that depend on the thoughput of an asset.",
    "costs_investment_over_lifetime": "Investment costs over the whole project lifetime, including all replacement costs.",
    "costs_om_total": "Costs for annual operation and maintenance costs as well as dispatch of all assets of the energy system, for the whole project duration.",
    "costs_total": "Net present costs of the system for the whole project duration, includes all operation, maintainance and dispatch costs as well as the investment costs (including replacements).",
    "costs_upfront_in_year_zero": "The costs which will have to be paid upfront when project begin, ie. In year 0.",
    "levelized_cost_of_energy_of_asset": "Cost per kWh thoughput though an asset, based on the assets costs during the project lifetime as well as the total thoughput though the asset in the project lifetime. For generation assets, equivalent to the levelized cost of generation."
}

KPI_COSTS_UNITS = {
    "Replacement_costs_during_project_lifetime": "€",
    "annuity_om": "€/annum",
    "annuity_total": "€/annum",
    "costs_cost_om": "€",
    "costs_dispatch": "€",
    "costs_investment_over_lifetime": "€",
    "costs_om_total": "€/annum",
    "costs_total": "€",
    "costs_upfront_in_year_zero": "€",
    "levelized_cost_of_energy_of_asset": "€/kWh", 
}

KPI_SCALAR_UNITS = {
    "Attributed costsElectricity": "€",
    "Degree of autonomy": "fraction",
    "Levelized costs of electricity equivalent": "€/kWh",
    "Levelized costs of electricity equivalentElectricity": "€/kWh",
    "Onsite energy fraction": "fraction",
    "Onsite energy matching": "fraction",
    "Renewable factor": "fraction",
    "Renewable share of local generation": "fraction",
    "Replacement_costs_during_project_lifetime": "€",
    "Specific emissions per electricity equivalent": "kg GHGeq/kWh",
    "Total emissions": "GHGeq/annum",
    "Total internal generation": "kWh/annum",
    "Total internal non-renewable generation": "kWh/annum",
    "Total internal renewable generation": "kWh/annum",
    "Total non-renewable energy use": "kWh/annum",
    "Total renewable energy use": "kWh/annum",
    "Total_demandElectricity": "kWh/annum",
    "Total_demandElectricity_electricity_equivalent": "kWh/annum",
    "Total_demand_electricity_equivalent": "kWh/annum",
    "Total_excessElectricity": "kWh/annum",
    "Total_excessElectricity_electricity_equivalent": "kWh/annum",
    "Total_excess_electricity_equivalent": "kWh/annum",
    "Total_feedinElectricity": "kWh/annum",
    "Total_feedinElectricity_electricity_equivalent": "kWh/annum",
    "Total_feedin_electricity_equivalent": "kWh/annum",
    "annuity_om": "€/annum",
    "annuity_total": "€/annum",
    "costs_cost_om": "€",
    "costs_dispatch": "€",
    "costs_investment_over_lifetime": "€",
    "costs_om_total": "€",
    "costs_total": "€",
    "costs_upfront_in_year_zero": "€"
}

KPI_SCALAR_TOOLTIPS = {
    "Attributed costsElectricity": "Costs attributed to supplying the electricity sectors demand, based on Net Present Costs of the energy system and the share of electricity compared to the overall system demand.",
    "Degree of autonomy": "A degree of autonomy close to zero shows high dependence on the DSO, while a degree of autonomy of 1 represents an autonomous or net-energy system and a degree of autonomy higher 1 a surplus-energy system",
    "Levelized costs of electricity equivalent": "Levelized cost of energy of the sector-coupled energy system, calculated from the systems annuity and the total system demand in electricity equivalent.",
    "Levelized costs of electricity equivalentElectricity": "Levelized cost of electricity, calculated from the levelized cost of energy and the share that the electricity demand has of the total energy demand of the system.",
    "Onsite energy fraction": "Onsite energy fraction is also referred to as self-consumption. It describes the fraction of all locally generated energy that is consumed by the system itself.",
    "Onsite energy matching": "The onsite energy matching is also referred to as â€œself-sufficiencyâ€. It describes the fraction of the total demand that can be covered by the locally generated energy. Notice that the feed into the grid should only be positive. https://mvs-eland.readthedocs.io/en/latest/MVS_Outputs.html#onsite-energy-matching-oem",
    "Renewable factor": "Describes the share of the energy influx to the local energy system that is provided from renewable sources. This includes both local generation as well as consumption from energy providers.",
    "Renewable share of local generation": "The renewable share of local generation describes how much of the energy generated locally is produced from renewable sources. It does not take into account the consumption from energy providers.",
    "Replacement_costs_during_project_lifetime": "Costs for replacement of assets which occur over the project lifetime.",
    "Specific emissions per electricity equivalent": "Specific GHG emissions per supplied electricity equivalent",
    "Total emissions": "Total greenhouse gas emissions in kg.",
    "Total internal generation": "Aggregated amount of energy generated within the energy system",
    "Total internal non-renewable generation": "Aggregated amount of non-renewable energy generated within the energy system",
    "Total internal renewable generation": "Aggregated amount of renewable energy generated within the energy system",
    "Total non-renewable energy use": "Aggregated amount of non-renewable energy used within the energy system (ie. Including local generation and external supply).",
    "Total renewable energy use": "Aggregated amount of renewable energy used within the energy system (ie. Including local generation and external supply).",
    "Total_demandElectricity": "Demand of electricity in local energy system.",
    "Total_demandElectricity_electricity_equivalent": "Demand of electricity in local energy system, in electricity equivalent. This is equivalent to Electricity feed-in.",
    "Total_demand_electricity_equivalent": "System wide demand from all energy vectors, in electricity equivalent.",
    "Total_excessElectricity": "Excess of electricity / unused electricity in local energy system.",
    "Total_excessElectricity_electricity_equivalent": "Excess of electricity / unused electricity in local energy system, in electricity equivalent. This is equivalent to Excess electricity.",
    "Total_excess_electricity_equivalent": "System-wide excess of energy / unused energy, in electricity equivalent.",
    "Total_feedinElectricity": "Feed-in of electricity into external grid.",
    "Total_feedinElectricity_electricity_equivalent": "Feed-in of electricity into external grid, in electricity equivalent. This is equivalent to Electricity feed-in.",
    "Total_feedin_electricity_equivalent": "System wide feed-in into external grids from all energy vectors, in electricity equivalent.",
    "annuity_om": "Annuity of the operation, maintenance and dispatch costs of the energy system, ie. Ballpoint number of the annual expenses for system operation.",
    "annuity_total": "Annuity of the net present costs (NPC) of the energy system.",
    "costs_cost_om": "Costs for fix annual operation and maintenance costs over the whole project lifetime, that do not depend on the assets dispatch but solely on installed capacity.",
    "costs_dispatch": "Dispatch costs over the whole project lifetime including all expenditures that depend on the dispatch of assets, ie. fuel costs, electricity consumption from the external grid, costs for operation and maintainance that depend on the thoughput of an asset",
    "costs_investment_over_lifetime": "Investment costs over the whole project lifetime, including all replacement costs.",
    "costs_om_total": "Costs for annual operation and maintenance costs as well as dispatch of all assets of the energy system, for the whole project duration.",
    "costs_total": "Net present costs of the system for the whole project duration, includes all operation, maintainance and dispatch costs as well as the investment costs (including replacements).",
    "costs_upfront_in_year_zero": "The costs which will have to be paid upfront when project begin, ie. In year 0."
}


class KPIScalarResults(models.Model):
    scalar_values = models.TextField()  # to store the scalars dict
    simulation = models.ForeignKey(Simulation, on_delete=models.CASCADE)


class KPICostsMatrixResults(models.Model):
    cost_values = models.TextField()  # to store the scalars dict
    simulation = models.ForeignKey(Simulation, on_delete=models.CASCADE)


class AssetsResults(models.Model):
    assets_list = models.TextField()  # to store the assets list
    simulation = models.ForeignKey(Simulation, on_delete=models.CASCADE)
