Create Scenario
---------------

This view-component enables the user to create a new :ref:`scenario-label`.

Attributes
^^^^^^^^^^

**Scenario name text input**
    The user can provide a file path for the scenario they want to create

    Actions index: 2

    Requirements index: 1, 2, 3

**button** :guilabel:`&Browse`
    Triggers the selection the scenario name text input via a graphical file structure

    Actions index: 1

    Requirements index: 1, 2, 3


**button** :guilabel:`&Create`
    The user triggers the creation of the scenario

    Actions index: 3

    Requirements index: 4, 5, 6


Actions
^^^^^^^

1. User can navigate through the file system either graphically to input scenario name by clicking on :guilabel:`&Browse`
2. User can input scenario name in the input text
3. After clicking on :guilabel:`&Create`, a scenario is created in the backend, in the file system and the user is redirected to the view corresponding to the first step in the :ref:`progression_bar-label`

Requirements
^^^^^^^^^^^^

1. If user only provided a name and not a file path, then the scenario file/folder is created in a default location
2. If user provided a scenario file/folder path which does not exist yet, the missing folders in the path should be created
3. If user provided a scenario file/folder path which exists already, it should be warned and given the option ot overwrite or not
4. After the user clicked on :guilabel:`&Create`, they must still be able to create another scenario through this view-component if they wish it
5. When a new scenario is created, it should be assigned a unique id in the backend
6. When a new scenario is created, it should be possible for the user to access and edit its input parameters

Link with views
^^^^^^^^^^^^^^^
.. use :ref:`<view>-label` to cross link to the view's description directly

:ref:`landing-label`
    It should be possible to trigger the display of this view-component from the landing view


:ref:`<view1>-label`
    After clicking on :guilabel:`&Create`, the user is redirected to the view corresponding to the first step in the :ref:`progression_bar-label`
    TODO add link to this view



Link with other view-components
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. use :ref:`<view_component>-label` to cross link to the view-component's description directly

:ref:`menu_bar-label`
    It should be possible to trigger the display of this view-component from a sub-menu of the :ref:`menu_bar-label`


Rendering of the view-component
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
:guilabel:`&Browse` is on the right of the text input, the :guilabel:`&Create` is centered on the next line below