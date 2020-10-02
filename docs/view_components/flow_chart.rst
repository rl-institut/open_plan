.. _flowchart-label:

Flow-chart
----------
The flow chart is a map of all the sequential steps of the simulation in one view-component. The below sections present the proposed structure for this view-component.

The following are the advantages of the flow chart view-component:

* Helps in sequentially progressing through the modeling and simulation process
* Allows the user to jump between different steps of the simulation
* Brings a design consistency and uniformity to the UI of the tool
* Splits the tool in different views which increases the user friendliness 

Attributes
^^^^^^^^^^

* Clickable, identical buttons
* Ribbon shaped, clickable icons/buttons placed sequentially as per the simulation progression order.
* Each button is a step in the simulation process
* Each step has to be completed one at a time. Once a step has met its minimum requirements, the button of the next step becomes clickable. Therefore, the user can come back to the steps he has already seen but he cannot click a random step. 

Actions
^^^^^^^

* Clicking on the active (orange color) buttons alters the view to the corresponding view-component of the simulation. E.g.: Clicking on 'Project Setup' will alter to a view with the options to enter values for various project parameters.
* Clicking on the greyed-out (inactive) buttons does not elicit any response.

Requirement
^^^^^^^^^^^

Link with other view-components
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Rendering of the view-component
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: docs/assets/flow_chart.png
   :width: 400
   :alt: An example of the proposed rendering of the flow chart
