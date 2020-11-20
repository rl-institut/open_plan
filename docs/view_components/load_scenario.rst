Load Scenario
-------------

This view-component enables the user to load a :ref:`scenario-label`.


Attributes
^^^^^^^^^^

**Scenario name text input**
    The user must provide a file path for the scenario they want to load

    Actions index: 2

    Requirements index: 1, 2, 3

**button** :guilabel:`&Browse`
    Triggers the selection the scenario name text input via a graphical file structure

    Actions index: 1

    Requirements index: 1, 2, 3


**button** :guilabel:`&Load`
    The user triggers the creation of the scenario

    Actions index: 3

    Requirements index: 4, 5, 6

Actions
^^^^^^^

1. User can navigate through the file system either graphically to input scenario name by clicking on :guilabel:`&Browse`
2. User can input scenario name in the input text
3. After clicking on :guilabel:`&Load`, a scenario is created in the backend with loaded parameters. The user is redirected to the view corresponding to the last step before running the simulation in the :ref:`progression_bar-label`

Requirements
^^^^^^^^^^^^

1. If user provided a scenario file/folder path which does not exist yet, an error message should be displayed
2. If user provided a scenario file/folder path which exists already, it should be warned and given the option ot overwrite or not
3. After the user clicked on :guilabel:`&Load`, they must still be able to load another scenario through this view-component if they wish it
4. When a scenario is loaded, it should be assigned a unique id in the backend
5. When a scenario is loaded, it should be possible for the user to access and edit its input parameters


Link with views
^^^^^^^^^^^^^^^
.. use :ref:`<view>-label` to cross link to the view's description directly

:ref:`landing-label`
    It should be possible to trigger the display of this view-component from the landing view


:ref:`<view1>-label`
    After clicking on :guilabel:`&Load`, the user is redirected to the view corresponding to the last step before running the simulation in the :ref:`progression_bar-label`
    TODO add link to this view


Link with other view-components
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. use :ref:`<view_component>-label` to cross link to the view-component's description directly

:ref:`menu_bar-label`
    It should be possible to trigger the display of this view-component from a sub-menu of the :ref:`menu_bar-label`


Rendering of the view-component
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:guilabel:`&Browse` is on the right of the text input, the :guilabel:`&Load` is centered on the next line below
