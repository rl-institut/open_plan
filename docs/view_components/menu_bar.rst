.. _menu_bar-label:

Menu Bar
--------

Menu bar is a set of options linked to actions, or submenus.

Attributes
^^^^^^^^^^

**The following are the menus available in the menu bar:**
    #. File
    #. Scenarios
    #. Preferences
    #. Help
***File* has the following submenus or options:**
    I. Load project
    II. New project
    III. Save project
    IV. Save project as
    V. Export project
    VI. Exit open_plan
***Scenarios* has the following submenus:**
    I. New scenario
    II. Load scenario
    III. Compare scenarios
    IV. ---- (separating horizontal line)
    V. List of scenarios in the system
***Preferences* has the following submenus:**
    I. Language
    II. Display
***Help* has the following submenus:**
    I. Read documentation
    II. Examples and use cases
    III. Contact developers
    IV. Feedback
    V. License information
    VI. About open_plan...

Actions
^^^^^^^

Clicking on any of the menus' option results in a drop-down list of sub-menu's options if applicable, otherwise trigger an action

File
    I. Load project
    II. New project
    III. Save project
    IV. Save project as
    V. Export project: display :ref:`export_project-label`
    VI. Exit open_plan
Scenarios
    I. New scenario: display :ref:`create_scenario-label`
    II. Load scenario: display :ref:`load_scenario-label`
    III. Compare scenarios: display view :ref:`scenario_comparison-label`
    IV. ---- (separating horizontal line)
    V. List of scenarios in the system
Preferences
    I. Language: not sure whether this will be implemented
    II. Display
Help
    I. Read documentation: redirect to `ReadTheDocs documentation <https://open-plan.readthedocs.io/en/latest/?badge=latest>`_
    II. Examples and use cases: redirect to ReadTheDocs usecases TODO: add link
    III. Contact developers: redirect to `Github issues <https://github.com/rl-institut/open_plan/issues/new/choose>`_
    IV. Feedback redirect to `Github issues <https://github.com/rl-institut/open_plan/issues/new/choose>`_
    V. License information: redirect to `Github license <https://github.com/rl-institut/open_plan/blob/dev/LICENSE>`_
    VI. About open_plan...: redirect to open_plan website TODO: add link


Requirement
^^^^^^^^^^^

1. The menu/submenu's options that are not applicable are greyed out or inactive and thus, nothing happens when clicked upon

Link with views
^^^^^^^^^^^^^^^

:ref:`scenario_comparison-label`


Link with other view-components
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:ref:`welcome-label`
    The welcome view-component can be re-enabled if it was disabled by the user from appearing everytime the tool is launched.

:ref:`progression_bar-label`

:ref:`export_project-label`

:ref:`create_scenario-label`

:ref:`load_scenario-label`


Rendering of the view-component
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Rectangular drop-down menu buttons present on a horizontal bar on top of the :ref:`main-window-def`
* Rendered on every view of the tool UI
* The current scenario is highlighted in the drop-down list which results when the *Scenarios* menu is clicked
