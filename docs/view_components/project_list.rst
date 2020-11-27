.. _project_list-label:

List of Projects
----------------

This view-component displays a list of open_plan project (or project files in accepted formats) objects one of which can can be loaded as the current project.

Attributes
^^^^^^^^^^
.. Please refer to the definition of what an attribute is in the tool_interface.rst file
.. The properties should be filled in only if applicable.

**Select**
    Allows the user to select the project object to be loaded as the current project

**Delete**
    Allows the user to delete the saved project object from the disk

**Show**
    Allows the user to quickly preview the project object selected

**Edit**
    Allows the user to quickly edit the main project parameters

Actions
^^^^^^^
..
    an action is something one can perform directly from the view-component
    (i.e. "clicking on this attribute should update this other attribute")

1. Action 1
2. Action 2

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

:ref:`landing-label`
    Landing page view of which this view-component is a part of

Link with other view-components
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:ref:`project-label`
    The abstract component describing the project object

:ref:`read_write_files-label`
    VIew-component through which the project objects could be loaded from the disk or written to the disk


Rendering of the view-component
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Rendered as a list which displays all the project objects already saved in the system or currently created

2. Currently selected project is highlighted separately