-- noinspection SqlNoDataSourceInspectionForFile

delete from projects_assettype where 1=1;
delete from projects_valuetype where 1=1;

-- Providers
insert into projects_assettype(asset_type, energy_vector, asset_category, mvs_type, asset_fields, unit) values
('dso','Electricity', 'energy_provider', 'source', '[name,energy_price,feedin_tariff,peak_demand_pricing,peak_demand_pricing_period,renewable_share]', null );
insert into projects_assettype(asset_type, energy_vector, asset_category, mvs_type, asset_fields, unit) values
('gas_dso','Gas', 'energy_provider', 'source', '[name,energy_price,feedin_tariff,peak_demand_pricing,peak_demand_pricing_period,renewable_share]', null );
insert into projects_assettype(asset_type, energy_vector, asset_category, mvs_type, asset_fields, unit) values
('h2_dso','H2', 'energy_provider', 'source', '[name,energy_price,feedin_tariff,peak_demand_pricing,peak_demand_pricing_period,renewable_share]', null );
insert into projects_assettype(asset_type, energy_vector, asset_category, mvs_type, asset_fields, unit) values
('heat_dso','Heat', 'energy_provider', 'source', '[name,energy_price,feedin_tariff,peak_demand_pricing,peak_demand_pricing_period,renewable_share]', null );

-- Consumption
insert into projects_assettype(asset_type, energy_vector, asset_category, mvs_type, asset_fields, unit) values
('demand','Electricity', 'energy_consumption', 'sink', '[name,input_timeseries]', 'kWh' );
insert into projects_assettype(asset_type, energy_vector, asset_category, mvs_type, asset_fields, unit) values
('gas_demand','Gas', 'energy_consumption', 'sink', '[name,input_timeseries]', null );
insert into projects_assettype(asset_type, energy_vector, asset_category, mvs_type, asset_fields, unit) values
('h2_demand','H2', 'energy_consumption', 'sink', '[name,input_timeseries]', null );
insert into projects_assettype(asset_type, energy_vector, asset_category, mvs_type, asset_fields, unit) values
('heat_demand','Heat', 'energy_consumption', 'sink', '[name,input_timeseries]', null );

-- Conversion
insert into projects_assettype(asset_type, energy_vector, asset_category, mvs_type, asset_fields, unit) values
('transformer_station_in','Electricity', 'energy_conversion', 'transformer', '[name,age_installed,installed_capacity,capex_fix,capex_var,opex_fix,opex_var,lifetime,optimize_cap,efficiency]', 'kVA' );
insert into projects_assettype(asset_type, energy_vector, asset_category, mvs_type, asset_fields, unit) values
('transformer_station_out','Electricity', 'energy_conversion', 'transformer', '[name,age_installed,installed_capacity,capex_fix,capex_var,opex_fix,opex_var,lifetime,optimize_cap,efficiency]', 'kVA' );
insert into projects_assettype(asset_type, energy_vector, asset_category, mvs_type, asset_fields, unit) values
('storage_charge_controller_in','Electricity', 'energy_conversion', 'transformer', '[name,age_installed,installed_capacity,capex_fix,capex_var,opex_fix,opex_var,lifetime,optimize_cap,efficiency]', 'kVA' );
insert into projects_assettype(asset_type, energy_vector, asset_category, mvs_type, asset_fields, unit) values
('storage_charge_controller_out','Electricity', 'energy_conversion', 'transformer', '[name,age_installed,installed_capacity,capex_fix,capex_var,opex_fix,opex_var,lifetime,optimize_cap,efficiency]', 'kVA' );
insert into projects_assettype(asset_type, energy_vector, asset_category, mvs_type, asset_fields, unit) values
('solar_inverter','Electricity', 'energy_conversion', 'transformer', '[name,age_installed,installed_capacity,capex_fix,capex_var,opex_fix,opex_var,lifetime,optimize_cap,efficiency]', 'kVA' );
insert into projects_assettype(asset_type, energy_vector, asset_category, mvs_type, asset_fields, unit) values
('diesel_generator','Electricity', 'energy_conversion', 'transformer', '[name,age_installed,installed_capacity,capex_fix,capex_var,opex_fix,opex_var,lifetime,optimize_cap,efficiency]', 'kW (el)' );
insert into projects_assettype(asset_type, energy_vector, asset_category, mvs_type, asset_fields, unit) values
('fuel_cell','Electricity', 'energy_conversion', 'transformer', '[name,age_installed,installed_capacity,capex_fix,capex_var,opex_fix,opex_var,lifetime,optimize_cap,efficiency]', 'kW (el)' );
insert into projects_assettype(asset_type, energy_vector, asset_category, mvs_type, asset_fields, unit) values
('gas_boiler','Gas', 'energy_conversion', 'transformer', '[name,age_installed,installed_capacity,capex_fix,capex_var,opex_fix,opex_var,lifetime,optimize_cap,efficiency]', 'kW (therm)' );
insert into projects_assettype(asset_type, energy_vector, asset_category, mvs_type, asset_fields, unit) values
('electrolyzer','H2', 'energy_conversion', 'transformer', '[name,age_installed,installed_capacity,capex_fix,capex_var,opex_fix,opex_var,lifetime,optimize_cap,efficiency]', 'kgH2' );
insert into projects_assettype(asset_type, energy_vector, asset_category, mvs_type, asset_fields, unit) values
('heat_pump','Heat', 'energy_conversion', 'transformer', '[name,age_installed,installed_capacity,capex_fix,capex_var,opex_fix,opex_var,lifetime,optimize_cap,efficiency]', 'kW (therm)' );

-- Production
insert into projects_assettype(asset_type, energy_vector, asset_category, mvs_type, asset_fields, unit) values
('pv_plant','Electricity', 'energy_production', 'source', '[name,age_installed,installed_capacity,capex_fix,capex_var,opex_fix,opex_var,lifetime,optimize_cap, renewable_asset, input_timeseries]', 'kWh' );
insert into projects_assettype(asset_type, energy_vector, asset_category, mvs_type, asset_fields, unit) values
('wind_plant','Electricity', 'energy_production', 'source', '[name,age_installed,installed_capacity,capex_fix,capex_var,opex_fix,opex_var,lifetime,optimize_cap, renewable_asset, input_timeseries]', 'kWh' );
insert into projects_assettype(asset_type, energy_vector, asset_category, mvs_type, asset_fields, unit) values
('biogas_plant','Gas', 'energy_production', 'source', '[name,age_installed,installed_capacity,capex_fix,capex_var,opex_fix,opex_var,lifetime,optimize_cap, renewable_asset, input_timeseries]', null );
insert into projects_assettype(asset_type, energy_vector, asset_category, mvs_type, asset_fields, unit) values
('geothermal_conversion','Electricity', 'energy_production', 'source', '[name,age_installed,installed_capacity,capex_fix,capex_var,opex_fix,opex_var,lifetime,optimize_cap, renewable_asset, input_timeseries]', 'kWh' );
insert into projects_assettype(asset_type, energy_vector, asset_category, mvs_type, asset_fields, unit) values
('solar_thermal_plant','Heat', 'energy_production', 'source', '[name,age_installed,installed_capacity,capex_fix,capex_var,opex_fix,opex_var,lifetime,optimize_cap, renewable_asset, input_timeseries]', null );

-- Battery Energy Storage System
insert into projects_assettype(asset_type, energy_vector, asset_category, mvs_type, asset_fields, unit) values
('charging_power','Electricity', 'energy_storage', 'storage', '[name,age_installed,installed_capacity,capex_fix,capex_var,opex_fix,opex_var,lifetime,crate,efficiency]', 'kW' );
insert into projects_assettype(asset_type, energy_vector, asset_category, mvs_type, asset_fields, unit) values
('discharging_power','Electricity', 'energy_storage', 'storage', '[name,age_installed,installed_capacity,capex_fix,capex_var,opex_fix,opex_var,lifetime,crate,efficiency]', 'kW' );
insert into projects_assettype(asset_type, energy_vector, asset_category, mvs_type, asset_fields, unit) values
('capacity','Electricity', 'energy_storage', 'storage', '[name,age_installed,installed_capacity,capex_fix,capex_var,opex_fix,opex_var,lifetime,optimize_cap,efficiency,soc_max,soc_min]', 'kWh' );
insert into projects_assettype(asset_type, energy_vector, asset_category, mvs_type, asset_fields, unit) values
('bess','Electricity', 'energy_storage', 'storage', '[name]', 'kW (el)' );
-- Gas Energy Storage System
-- insert into projects_assettype(asset_type, energy_vector, asset_category, mvs_type, asset_fields, unit) values
-- ('g_charging_power','Gas', 'energy_storage', 'storage', '[name,age_installed,installed_capacity,capex_fix,capex_var,opex_fix,opex_var,lifetime,crate,efficiency]', 'l' );
-- insert into projects_assettype(asset_type, energy_vector, asset_category, mvs_type, asset_fields, unit) values
-- ('g_discharging_power','Gas', 'energy_storage', 'storage', '[name,age_installed,installed_capacity,capex_fix,capex_var,opex_fix,opex_var,lifetime,crate,efficiency]', 'l' );
-- insert into projects_assettype(asset_type, energy_vector, asset_category, mvs_type, asset_fields, unit) values
-- ('g_capacity','Gas', 'energy_storage', 'storage', '[name,age_installed,installed_capacity,capex_fix,capex_var,opex_fix,opex_var,lifetime,optimize_cap,efficiency,soc_max,soc_min]', 'kWh (chem)' );
insert into projects_assettype(asset_type, energy_vector, asset_category, mvs_type, asset_fields, unit) values
('gess','Gas', 'energy_storage', 'storage', '[name]', 'l' );
-- H2 Energy Storage System
-- insert into projects_assettype(asset_type, energy_vector, asset_category, mvs_type, asset_fields, unit) values
-- ('h2_charging_power','H2', 'energy_storage', 'storage', '[name,age_installed,installed_capacity,capex_fix,capex_var,opex_fix,opex_var,lifetime,crate,efficiency]', 'kgH2' );
-- insert into projects_assettype(asset_type, energy_vector, asset_category, mvs_type, asset_fields, unit) values
-- ('h2_discharging_power','H2', 'energy_storage', 'storage', '[name,age_installed,installed_capacity,capex_fix,capex_var,opex_fix,opex_var,lifetime,crate,efficiency]', 'kgH2' );
-- insert into projects_assettype(asset_type, energy_vector, asset_category, mvs_type, asset_fields, unit) values
-- ('h2_capacity','H2', 'energy_storage', 'storage', '[name,age_installed,installed_capacity,capex_fix,capex_var,opex_fix,opex_var,lifetime,optimize_cap,efficiency,soc_max,soc_min]', 'kgH2' );
insert into projects_assettype(asset_type, energy_vector, asset_category, mvs_type, asset_fields, unit) values
('h2ess','H2', 'energy_storage', 'storage', '[name]', 'kgH2' );
-- Heat Energy Storage System
-- insert into projects_assettype(asset_type, energy_vector, asset_category, mvs_type, asset_fields, unit) values
-- ('h_charging_power','Heat', 'energy_storage', 'storage', '[name,age_installed,installed_capacity,capex_fix,capex_var,opex_fix,opex_var,lifetime,crate,efficiency]', 'kW (therm)' );
-- insert into projects_assettype(asset_type, energy_vector, asset_category, mvs_type, asset_fields, unit) values
-- ('h_discharging_power','Heat', 'energy_storage', 'storage', '[name,age_installed,installed_capacity,capex_fix,capex_var,opex_fix,opex_var,lifetime,crate,efficiency]', 'kW (therm)' );
-- insert into projects_assettype(asset_type, energy_vector, asset_category, mvs_type, asset_fields, unit) values
-- ('h_capacity','Heat', 'energy_storage', 'storage', '[name,age_installed,installed_capacity,capex_fix,capex_var,opex_fix,opex_var,lifetime,optimize_cap,efficiency,soc_max,soc_min]', 'kWh (therm)' );
insert into projects_assettype(asset_type, energy_vector, asset_category, mvs_type, asset_fields, unit) values
('hess','Heat', 'energy_storage', 'storage', '[name]', 'kW (therm)' );

insert into projects_valuetype( unit, type) values ('year', 'duration' );
insert into projects_valuetype( unit, type) values ('', 'annuity_factor' );
insert into projects_valuetype( unit, type) values ('factor', 'discount' );
insert into projects_valuetype( unit, type) values ('factor', 'tax' );
insert into projects_valuetype( unit, type) values ('', 'crf' );
insert into projects_valuetype( unit, type) values ('factor of total capacity (kWh)', 'crate' );
insert into projects_valuetype( unit, type) values ('year', 'age_installed' );
insert into projects_valuetype( unit, type) values ('factor', 'soc_max' );
insert into projects_valuetype( unit, type) values ('factor', 'soc_min' );
insert into projects_valuetype( unit, type) values ('currency', 'capex_fix' );
insert into projects_valuetype( unit, type) values ('currency/unit/year', 'opex_var' );
insert into projects_valuetype( unit, type) values ('factor', 'efficiency' );
insert into projects_valuetype( unit, type) values ('unit', 'installed_capacity' );
insert into projects_valuetype( unit, type) values ('year', 'lifetime' );
insert into projects_valuetype( unit, type) values ('kW', 'maximum_capacity' );
insert into projects_valuetype( unit, type) values ('currency/kWh', 'energy_price' );
insert into projects_valuetype( unit, type) values ('currency/kWh', 'feedin_tariff' );
insert into projects_valuetype( unit, type) values ('bool', 'optimize_cap' );
insert into projects_valuetype( unit, type) values ('currency/kW', 'peak_demand_pricing' );
insert into projects_valuetype( unit, type) values ('times per year (1,2,3,4,6,12)', 'peak_demand_pricing_period' );
insert into projects_valuetype( unit, type) values ('factor', 'renewable_share' );
insert into projects_valuetype( unit, type) values ('currency/unit', 'capex_var' );
insert into projects_valuetype( unit, type) values ('currency/year', 'opex_fix' );
insert into projects_valuetype( unit, type) values ('currency/year', 'specific_costs_om' );
insert into projects_valuetype( unit, type) values ('kWh', 'input_timeseries' );
insert into projects_valuetype( unit, type) values ('days', 'evaluated_period' );
insert into projects_valuetype( unit, type) values ('bool', 'renewable_asset' );