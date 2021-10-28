from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    # Project
    path('project/create/', project_create, name='project_create'),
    path('notimplementedyet/', not_implemented, name='not_implemented'),
    path('project/search/', project_search, name='project_search'),
    path('project/search/<int:proj_id>', project_search, name='project_search'),
    path('project/update/<int:proj_id>', project_update, name='project_update'),
    path('project/detail/<int:proj_id>', project_detail, name='project_detail'),
    path('project/duplicate/<int:proj_id>', project_duplicate, name='project_duplicate'),
    path('project/delete/<int:proj_id>', project_delete, name='project_delete'),
    path('project/project_members_list/<int:proj_id>', project_members_list, name='project_members_list'),
    path('project/share/<int:proj_id>', project_share, name='project_share'),
    path('project/unshare/<int:proj_id>', project_revoke_access, name='project_revoke_access'),
    # Comment
    path('comment/create/<int:proj_id>', comment_create, name='comment_create'),
    path('comment/update/<int:com_id>', comment_update, name='comment_update'),
    path('comment/delete/<int:com_id>', comment_delete, name='comment_delete'),
    # Scenario
    path('project/<int:proj_id>/scenario/create/step', scenario_steps, name='scenario_steps'),
    path('project/<int:proj_id>/scenario/create/step/<int:step_id>', scenario_steps, name='scenario_steps'),
    path('project/<int:proj_id>/scenario/<int:scen_id>/edit/step/<int:step_id>', scenario_steps, name='scenario_steps_edit'),
    path('project/<int:proj_id>/scenario/create_parameters', scenario_create_parameters, name='scenario_create_parameters'),
    path('project/<int:proj_id>/scenario/create_topology', scenario_create_topology, name='scenario_create_topology'),
    path('project/<int:proj_id>/scenario/create_constraints>', scenario_create_constraints, name='scenario_create_constraints'),
    path('project/<int:proj_id>/scenario/create_parameters/<int:scen_id>', scenario_create_parameters, name='scenario_create_parameters'),
    path('project/<int:proj_id>/scenario/create_parameters/<scen_id>', scenario_create_parameters, name='scenario_create_parameters'),
    path('project/<int:proj_id>/scenario/create_topology/<int:scen_id>', scenario_create_topology, name='scenario_create_topology'),
    path('project/<int:proj_id>/scenario/create_constraints/<int:scen_id>/', scenario_create_constraints, name='scenario_create_constraints'),
    path('project/<int:proj_id>/scenario/review/<int:scen_id>/', scenario_review, name='scenario_review'),
    path('scenario/update/<int:scen_id>', scenario_update, name='scenario_update'),
    path('scenario/delete/<int:scen_id>', scenario_delete, name='scenario_delete'),
    path('scenario/duplicate/<int:scen_id>', scenario_duplicate, name='scenario_duplicate'),
    path('scenario/export', scenario_export, name='scenario_export'),
    # path('scenario/upload/<int:proj_id>', LoadScenarioFromFileView.as_view(), name='scenario_upload'),
    # Grid Model (Assets Creation)
    re_path(r'^asset/get_form/(?P<asset_type_name>\w+)?(/(?P<asset_uuid>[0-9a-f-]+))?$', get_asset_create_form, name='get_asset_create_form'),
    re_path(r'^asset/create_or_update_post/(?P<scen_id>\d+)/(?P<asset_type_name>\w+)?(/(?P<asset_uuid>[0-9a-f-]+))?$', asset_create_or_update, name='asset_create_or_update'),
    # MVS Simulation
    path('view_mvs_data_input/<int:scen_id>', view_mvs_data_input, name='view_mvs_data_input'),
    path('topology/mvs_simulation/<int:scenario_id>', request_mvs_simulation, name='request_mvs_simulation'),
    path('topology/update_simulation_rating/', update_simulation_rating, name='update_simulation_rating'),
    # path('topology/simulation_status/<int:scen_id>', check_simulation_status, name='check_simulation_status'),
    re_path(r'^topology/simulation_status/(?P<scen_id>\d+)?$', check_simulation_status, name='check_simulation_status_regex'),
    path('topology/simulation_status/<int:scen_id>', check_simulation_status, name='check_simulation_status'),
    path('project/<int:proj_id>/scenario/<int:scen_id>', update_simulation_results, name='update_simulation_results'),
    # User Feedback
    path('user_feedback', user_feedback, name='user_feedback'),
   
]
