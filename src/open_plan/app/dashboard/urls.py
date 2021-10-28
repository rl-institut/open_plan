from django.urls import path
from .views import *

urlpatterns = [
    path('scenario/results/visualize', scenario_visualize_results, name='scenario_visualize_results'),
    path('scenario/results/visualize/<int:scen_id>', scenario_visualize_results, name='scenario_visualize_results'),
    path('scenario/results/request/<int:scen_id>', scenario_request_results, name='scenario_request_results'),
    path('scenario/results/available/<int:scen_id>', scenario_available_results, name='scenario_available_results'),
    path('scenario/results/request_economic_data/<int:scen_id>', scenario_economic_results, name='scenario_economic_results'),
    
    path('scenario/results/download_scalars/<int:scen_id>', download_scalar_results, name='download_scalar_results'),
    path('scenario/results/download_costs/<int:scen_id>', download_cost_results, name='download_cost_results'),
    path('scenario/results/download_timeseries/<int:scen_id>', download_timeseries_results, name='download_timeseries_results'),
]
