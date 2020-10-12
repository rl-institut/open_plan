.. _menu_bar-label:

Menu Bar
--------

Menu bar is a set of options linked to actions, or submenus.

Attributes
^^^^^^^^^^

* The following are the menus available in the menu bar:
    #. File
    #. Scenarios
    #. Preferences
    #. Help
* *File* has the following submenus or options:
    I. Load project
    II. New project
    III. Save project
    IV. Save project as
    V. Export project
    VI. Exit open_plan
* *Scenarios* has the following submenus:
    I. New scenario
    II. Load scenario
    III. ---- (separating horizontal line)
    IV. List of scenarios in the system

* *Preferences* has the following submenus:
    I. Language
    II. Display
* *Help* has the following submenus:
    I. Read documentation
    II. Examples and use cases
    III. Contact developers
    IV. Feedback
    V. License information
    VI. About open_plan...

Actions
^^^^^^^

* Clicking on any of the menus' option results in a drop-down list of sub-menu's options
* Clicking on *File* would show a drop-down list with the following submenus or options:
    I. Load project
    II. New project
    III. Save project
    IV. Save project as
    V. Export project
    VI. Exit open_plan
* clicking on *Preferences* would show a drop-down list with the following submenus or options:
    I. Language
    II. Display
* User can change the scenario by clicking on the specific scenario under the *Scenarios* menu or load their own scenario as well, or create a new scenario

Requirement
^^^^^^^^^^^

* The menu/submenu's options that are not applicable are greyed out or inactive and thus, nothing happens when clicked upon

Link with other view-components
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* :ref:`welcome-label`:
    The welcome view-component can be re-enabled if it was disabled by the user from appearing everytime the tool is launched.

* :ref:`flow_chart-label`

Rendering of the view-component
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Rectangular drop-down menu buttons present on a horizontal bar above the flow chart ribbon
* Rendered on every view of the tool UI
* The current scenario is highlighted in the drop-down list which results when the *Scenarios* menu is clicked
