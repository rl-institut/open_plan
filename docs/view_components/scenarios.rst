.. reference for this view-component
.. you can refer to this component using :ref:`<component_name>-label`

.. _scenarios-label:


Scenarios
---------
* This component depends a lot on the tool mechanism which has not been discussed deeply yet.
* Each project consists of a model that is run in a simulation following a specific scenario.

Attributes
^^^^^^^^^^
*This section will be filled automatically with the input/output excel sheet, here is one example:*

* Source power mix: Percentage of each source of power (inclusive % from Grid)

Actions
^^^^^^^
* Source power mix: Input percentage of each source of power


Requirement
^^^^^^^^^^^

*Source power mix: We should determine for each attribute if it is a requirement or optional for the simulation (depends on the tool mechanism)*

Link with other view-components
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* Each Source power mix depends on the technology put in the model by the user
* Each simulation ( :ref:`simulation-label` ) can be run with a different scenario but the same energy system model
* The different simulations run with the different scenarios can then be compared to each other via the scenario-comparison ( :ref:`scenario_comparison-label` ).

Rendering of the view-component
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* Source power mix: Input number box as % for each technology