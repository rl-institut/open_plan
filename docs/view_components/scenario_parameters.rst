Scenario parameters
-------------------
Inputs parameters to describe a :ref:`scenario-label`. The do not contain the information about the energy system, which is defined in the :ref:`es_network` view-component.


Attributes
^^^^^^^^^^

**List of input parameters**

    Each input parameter will be available to the user via :ref:`input_parameter_field-label`

    Properties of each input:
        - Input type
        - Input default value
        - Help text
        - If it is mandatory or optional
        - Link in documentation


As the parameters in this list should also be accessible in a more general parameter documentation in ReadTheDocs, they will be automatically listed here from either a .yml or csv file.


Actions
^^^^^^^
1. User can edit the value of the input parameters manually.
2. User can edit the value of the input parameters by loading a scenario from :ref:`load_scenario-label`


Requirement
^^^^^^^^^^^
1. The requirements of :ref:`input_parameter_field-label` apply for each input parameter

Link with other view-components
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Rendering of the view-component
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The rendering of :ref:`input_parameter_field-label` apply for each input parameter
