from os import path
import pandas as pd

PACKAGE_DATA_PATH = path.join(
    path.dirname(path.dirname(path.dirname(path.abspath(__file__)))), "docs", "_files"
)

path_csv = path.join(PACKAGE_DATA_PATH, "input_parameters_list.csv")

input_parameters = pd.read_csv(path_csv)


rtd_base_url = "https://open-plan.readthedocs.io/en/latest/parameters.html#"

prefix = "in_"

# Prepare what will be the parameter ID variable
input_parameters["ref"] = input_parameters.label.apply(
    lambda x: prefix + x.lower().replace(" ", "_")
)

# Prepare link to RTD
input_parameters["rtd"] = rtd_base_url + input_parameters.ref.apply(
    lambda x: x.lower().replace("_", "-")
)

# Fill the parameter definition where the tooltip is not defined
input_parameters.loc[input_parameters.tooltip.isna(), "tooltip"] = input_parameters.loc[
    input_parameters.tooltip.isna(), ":Definition:"
]

# Rename columns names
input_parameters = input_parameters.rename(
    columns={
        ":Unit:": "unit",
        ":Type:": "type",
        ":Default:": "default_value",
        ":Definition_DE:": "definition",
        "ref": "id",
        "label": "label_EN",
    }
)

input_parameters = input_parameters.rename(
    columns={
        ":label_DE:": "label",
    }
)


input_parameters.loc[input_parameters.unit.isna(), ["unit"]] = ""

input_param_props = ["label", "id", "unit", "type", "default_value", "tooltip", "rtd"]
project_params = input_parameters.loc[
    input_parameters.internal_categorization == "project", input_param_props
]
project_params = project_params.to_dict("records")

project_params = [
    {
        "label": "Project name",
        "id": "in_project_name",
        "unit": "",
        "type": "str",
        "default_value": "Enter a name",
        "tooltip": "A name to identify your scenario",
        "rtd": "",
    },
    {
        "label": "Project description",
        "id": "in_project_description",
        "unit": "",
        "type": "text",
        "default_value": "Enter a description",
        "tooltip": "A small text to describe your scenario",
        "rtd": "",
    },
] + project_params


scenario_params = input_parameters.loc[
    input_parameters.internal_categorization == "scenario", input_param_props
]
scenario_params = scenario_params.to_dict("records")

scenario_params = [
    {
        "label": "Scenario name",
        "id": "in_scenario_name",
        "unit": "",
        "type": "str",
        "default_value": "Enter a name",
        "tooltip": "A name to identify your scenario",
        "rtd": "",
    },
    {
        "label": "Scenario description",
        "id": "in_scenario_description",
        "unit": "",
        "type": "text",
        "default_value": "Enter a description",
        "tooltip": "A small text to describe your scenario",
        "rtd": "",
    },
] + scenario_params + [
    {
        "label": "Start date",
        "id": "in_start_date",
        "unit": "",
        "type": "str",
        "default_value": "Enter a date in YYYY-MM_DD",
        "tooltip": "The starting date of your simulation",
        "rtd": "",
    },
    {
        "label": "Evaluated period",
        "id": "in_evaluated_period",
        "unit": "day",
        "type": "str",
        "default_value": "Enter a number of days",
        "tooltip": "The total length of the simulation",
        "rtd": "",
    },
]


input_data_params = input_parameters.loc[
    input_parameters.internal_categorization == "scenario", input_param_props
]
input_data_params = input_data_params.to_dict("records")


constraints_params = input_parameters.loc[
    input_parameters.internal_categorization == "constraint", input_param_props
]
constraints_params = constraints_params.to_dict("records")






path_csv = path.join(PACKAGE_DATA_PATH, "output_parameters_list.csv")

output_parameters = pd.read_csv(path_csv)


rtd_base_url = "https://open-plan.readthedocs.io/en/latest/parameters.html#"

prefix = "out_"

# Prepare what will be the parameter ID variable
output_parameters["ref"] = output_parameters.label.apply(
    lambda x: prefix + x.lower().replace(" ", "_")
)

# Prepare link to RTD
output_parameters["rtd"] = rtd_base_url + output_parameters.ref.apply(
    lambda x: x.lower().replace("_", "-")
)

# Fill the parameter definition where the tooltip is not defined
output_parameters.loc[output_parameters.tooltip.isna(), "tooltip"] = output_parameters.loc[
    output_parameters.tooltip.isna(), ":Definition:"
]

# Rename columns names
output_parameters = output_parameters.rename(
    columns={
        ":Unit:": "unit",
        ":Type:": "type",
        ":Default:": "default_value",
        ":Definition_DE:": "definition",
        "ref": "id",
        "label": "label_EN",
    }
)

output_parameters = output_parameters.rename(
    columns={
        ":label_DE:": "label",
    }
)


output_parameters.loc[output_parameters.unit.isna(), ["unit"]] = ""

output_param_props = ["label", "id", "unit", "type", "default_value", "tooltip", "rtd"]

output_params = output_parameters.loc[output_parameters.internal_categorization != "hidden", output_param_props].to_dict("records")


def scenario_model(id, name, params):
    return dict(id=id, name=name, params=params)
