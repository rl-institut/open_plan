.. _view_specific_documentation-label:

View Specific Documentation
---------------------------

This view-component lets the user access the specific sections of the documentation directly from within the tool UI. It serves as a tooltip for input parameters.

Attributes
^^^^^^^^^^

**Scroll Bar**
    This bar lets the user navigate the documentation content

    Actions index: 1

    Requirements index:

**Side navigation pane**
    This navigation pane is akin to a table of contents and lets the user jump to other sections of the documentation quickly

    Actions index: 2

**Content**
    Content of the documentation such as text, images, hyperlinks, etc., to be rendered

**button** :guilabel:`&Download PDF`
    Clicking this triggers the download of a pdf of the documentation

    Actions index: 3

    Requirements index:

Actions
^^^^^^^

1. User can scroll through the documentation using the scroll bar
2. User can jump to other sections of the documentation using the links in the navigation pane
3. User can click on the Download PDF button to obtain a local copy of the documentation

Requirements
^^^^^^^^^^^^

1. User must be able to open this view-component through clicking on links next to various elements in other views/view-components

Link with views
^^^^^^^^^^^^^^^
.. use :ref:`<view>-label` to cross link to the view's description directly

Link with other view-components
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:ref:`welcome-label`
    First view-component on the landing view of the tool, seen by the user. Contains link to documentation

:ref:`input_parameter_field-label`
    Generic view-component that describes the fields where user inputs are necessary

:ref:`load_input_parameter-label`
    Description of the link

:ref:`scenario_parameters-label`
    View-component where the user inputs the scenario-specific parameters

:ref:`project_parameters-label`
    View-component where the user inputs the project parameters

Rendering of the view-component
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This view-component could either be a pop-up on top of the view the user is currently in, or as a new tab on a browser window opening relevant sections of readthedocs directly
