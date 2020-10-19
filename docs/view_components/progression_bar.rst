.. _progression-bar-label:

Progression Bar
---------------

The Progression Bar is a view component that shows all the sequential steps of the tool in order to get results.

A Progression bar view-component has a number of advantages:

* Helps in sequentially progressing through the modeling and simulation process
* Allows the user to jump between different steps of the simulation
* Brings a design consistency and uniformity to the UI of the tool
* Splits the tool in different views which increases the user friendliness 

Attributes
^^^^^^^^^^

**Several simulation steps constitute the progression bar**
    #. Project Setup
    #. Inputs
    #. System Inputs
    #. Visualization
    #. Constraints
    #. Simulations
    #. Results
**Each step has an associated index, with the progression being bar considered as an array**
** The current state of the view depends on the index of the current step**

Actions
^^^^^^^

1. To make the next step of the Progression bar clickable, the user has to fulfill the requirements of the current step. Each step has various mandatory and optional fields.
2. Clicking on the steps of the Progression bar that have been fulfilled already allows the user to make modifications.
3. Clicking on the steps that are not clickable make a small text bubble appear saying the previous step needs to be fulfilled first.

Requirement
^^^^^^^^^^^

1. The user has to progress through the progression bar in order to successfully carry out the modeling and simulation
2. Each step has to be completed one at a time. Once a step has met its minimum requirements, the button of the next step becomes clickable. Therefore, the user can come back to the steps they have already seen but they cannot click on a random step.

Link with views
^^^^^^^^^^^^^^^

.. TBD

Link with other view-components
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:ref:`menu_bar-label`
.. TBD

Rendering of the view-component
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Ribbon-like display of the progression bar or Progression bar; identical throughout the different views
* Clickable buttons on the progression bar placed sequentially as per the simulation progression order
* Each button signifies a step in the simulation process
* Different coloring of the buttons depending on the simulation steps performed
* Horizontally placed just below the top margin of the view
* The progression bar or Progression bar is present on every view of the tool UI

.. image:: _files/flow_chart.png
    :width: 400
    :alt: An example of the proposed rendering of the Progression bar
