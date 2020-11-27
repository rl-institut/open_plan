.. _scenario_list-label:

List of Scenarios
-----------------

This view-component shows the list of scenario objects, both created through the tool within the current project or loaded from file, available for further steps in the simulation.

Attributes
^^^^^^^^^^

**Select**
    Allows the user to select the scenario object to be loaded as the current project

**Delete**
    Allows the user to delete the saved scenario object from the disk

**Show**
    Allows the user to quickly preview the scenario object selected

**Edit**
    Allows the user to quickly edit the main scenario parameters

Actions
^^^^^^^

1. Select the current scenario object
2. Show the main parameters of any scenario object that the user selects in the list of scenarios
3. View the list of scenarios objects created in the present project or available on the disk
4. Delete a scenario object, both saved and unsaved ones

Requirements
^^^^^^^^^^^^
..
    a requirement is a binding rule which cannot be described directly by an action
    or which describes redundant actions
    (i.e. "it should not be possible to click on this attribute while the value of this other
    attribute is not defined", or "after changing the value of an already defined attribute,
    one should see a difference in the rendering of the attribute"

1. Requirement 1
2. Requirement 2

Link with views
^^^^^^^^^^^^^^^
.. use :ref:`<view>-label` to cross link to the view's description directly

Link with other view-components
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:ref:`scenario-label`
    The abstract component describing the scenario objects part of this view-component

:ref:`read_write_files-label`
    VIew-component through which the project objects could be loaded from the disk or written to the disk

Rendering of the view-component
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Rendered as a list which displays all the scenario objects loaded and/or created in the current project

2. Currently selected scenario is highlighted separately
