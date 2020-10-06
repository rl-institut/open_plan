.. _flowchart-label:

Flow-chart
----------
The flow chart is a view component that shows all the sequential steps of the tool in order to get results.

A flow chart view-component has a number of advantages:

* Helps in sequentially progressing through the modeling and simulation process
* Allows the user to jump between different steps of the simulation
* Brings a design consistency and uniformity to the UI of the tool
* Splits the tool in different views which increases the user friendliness 

Attributes
^^^^^^^^^^

* Each button is a step in the simulation process
* The list of steps in the progression bar are as follows:
    #. Project Setup
    #. Inputs
    #. System Inputs
    #. Visualization
    #. Constraints
    #. Simulations
    #. Results
* Each step has an associated index, with the progression being bar considered as an array
* The current state of the view depends on the index of the current step
* Each step has to be completed one at a time. Once a step has met its minimum requirements, the button of the next step becomes clickable. Therefore, the user can come back to the steps he has already seen but he cannot click a random step. 

Actions
^^^^^^^

* To make the next step of the flowchart clickable, the user has to fulfill the requirements of the current step. Each step has various mandatory and optional fields.
* Clicking on the steps of the flowchart that have been fulfilled already allows the user to make modifications. 
* Clicking on the steps that are not clickable make a small text bubble appear saying the previous step needs to be fulfilled first.

Requirement
^^^^^^^^^^^

Link with other view-components
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Rendering of the view-component
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Ribbon-like display of the progression bar or flow chart; identical throughout the different views
* Clickable buttons on the progression bar placed sequentially as per the simulation progression order
* Different coloring of the buttons depending on the simulation steps performed
* Horizontally placed just below the top margin of the view

.. image:: docs/assets/flow_chart.png
   :width: 400
   :alt: An example of the proposed rendering of the flow chart