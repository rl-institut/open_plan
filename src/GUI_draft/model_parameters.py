from os import path
import pandas as pd

PACKAGE_DATA_PATH = path.join(
    path.dirname(path.dirname(path.abspath(path.curdir))), "docs", "_files"
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
        ":Definition:": "definition",
        "ref": "id",
    }
)

input_param_props = ["label", "id", "unit", "type", "default_value", "tooltip", "rtd"]
project_params = input_parameters.loc[
    input_parameters.internal_categorization == "project", input_param_props
]
project_params = project_params.to_dict("records")

scenario_params = input_parameters.loc[
    input_parameters.internal_categorization == "scenario", input_param_props
]
scenario_params = scenario_params.to_dict("records")


input_data_params = input_parameters.loc[
    input_parameters.internal_categorization == "scenario", input_param_props
]
input_data_params = input_data_params.to_dict("records")
