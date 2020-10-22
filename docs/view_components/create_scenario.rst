Create Scenario
---------------

Create scenario view-component enables the user to create a new scenario object where the energy system can be implemented.

Attributes
^^^^^^^^^^

**Combination of a text field and Create button**
    The user can create a new scenario through this.

    Requirements index: 1

**Each scenario gets an unique ID**
    Alphanumeric string, can be used to reference the scenario object in other locations.

    Requirements index: 1

Actions
^^^^^^^

1. Allows user to navigate through the file system either graphically or through text inputs
2. Allows user to name the scenario object and write it to a chosen location in the computer's file system

Requirements
^^^^^^^^^^^^

1. User must provide a string containing the correct file path that leads to the folder that holds the scenario file(s)
2. After the user creates a scenario, they must be able to create another scenario following the same procedure, through this view-component
3. When a new scenario is created, it should appear in the the list of available scenarios within the :ref:project-label in the scenarios view
4. When a new scenario is created, it should be assigned with a unique ID

Link with views
^^^^^^^^^^^^^^^
.. use :ref:`<view>-label` to cross link to the view's description directly

**:ref:`<view1>-label`**
    Description of the link

**:ref:`<view2>-label`**
    Description of the link

Link with other view-components
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. use :ref:`<view_component>-label` to cross link to the view-component's description directly

**:ref:`<view_component1>-label`**
    Description of the link

**:ref:`<view_component2>-label`**
    Description of the link

Rendering of the view-component
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. TBD