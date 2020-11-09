.. _progression_bar-label:

Progression Bar
---------------

The Progression Bar displays the sequential steps the user should go through, in order to provide the input parameters required to describe an energy system and a :ref:`scenario-label` to simulate with this energy system model

This view-component allows the user to:

* Sequentially progress through the modeling and definition of their :ref:`scenario-label`
* Jump directly to previous steps to edit input parameters

Attributes
^^^^^^^^^^

**List of steps**
    For example the following steps:
    
    #. Project Setup
    #. Inputs
    #. System Inputs
    #. Visualization
    #. Constraints
    #. Simulations
    #. Results

    Properties:
        * Each step has an associated index (starting from 1), corresponding to its position in the list of steps
        * Each step in the progression bar is a link to a :ref:`view <views-label>`

    Actions index: 1, 2

**Current step index**
    The index of the currently selected step

    Requirements index: 1


Actions
^^^^^^^

1. Clicking on a step that has already been fulfilled, allows the user to make modifications to the inputs within this field
2. Clicking on a step which is disabled, make a small text bubble appear next to the step explaining why the user cannot click on that step

Requirement
^^^^^^^^^^^

1. To enable the next step, the user has to fulfill the requirements of the current step. Each step's requirements are defined in its respective :ref:`view <views-label>`

Link with views
^^^^^^^^^^^^^^^

Here will be a link to the views of each steps

:ref:`landing-label`
    It is not sure yet whether this view-component should be visible from start, join the on-going discussion `here <https://github.com/rl-institut/open_plan/issues/48>`_

Link with other view-components
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:ref:`menu_bar-label`


Rendering of the view-component
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Ribbon-like display of the progression bar where each step is delimited by an individual blob, the structure is identical throughout the different views. The term blob is employed to signify that the shape is up to a decision (non-exhaustive list of examples: a rectangle, an ellipse, a circle, an arrow)
* Indication of the steps order could be with arrow shaped blob, or with arrow symbols between the blobs
* Color coding of the blobs backgrounds can be used to indicate whether the step has already be visited, is not fulfilled yet, disabled or enabled
* The progression bar could be horizontal or vertical (it is assumed from left to right and top to bottom, but this can be debated)

Here is an example of one possible rendering, please note that this is not a final design, only an example

.. image:: _files/flow_chart.png
    :width: 400
    :alt: An example of the proposed rendering of the Progression bar
