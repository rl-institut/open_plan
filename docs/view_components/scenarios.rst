.. reference for this view-component
.. you can refer to this component using :ref:`<component_name>-label`

.. _<scenarios>-label:


Scenarios
----------
This component depends a lot on the tool mechanism which has not been discussed deeply yet.

Attributes
^^^^^^^^^^
* Each project consists of a model that is run in a simulation following a specific scenario.
* Each scenario is a combination of various parameters (or assumptions) set by the user.
* Each simulation ( :ref:`simulation-label` ) can be run with a different scenario but the same energy system model
* The different simulations run with the different scenarios can then be compared to each other via the scenario-comparison ( :ref:`<scenario_comparison>-label` ).

Actions
^^^^^^^


Requirement
^^^^^^^^^^^
A certain number of criteria have to be fulfilled:

* Economic: increase in costs, etc.
* Environmental: Max CO2 emission ?
* Technical: Share of a specific generation technology?

Link with other view-components
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Rendering of the view-component
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
