.. _tool_interface:

**************************
Tool interface description
**************************

The tool should enable its users to model a local energy system (like an industry park or a district) with the possibility to include sector-coupling. This web-based tool is thought for planning purposes and not operation. It should allow the user to optimize the energy system model subject to equality constraints.

The optimization is taken care of in the backend with the `oemof <https://oemof.org/>`_ framework. The role of the interface is thus to gather the necessary input parameters and to provide a vizualization of the outputs.

It is wished that this interface helps several actors with different perspectives and backgrounds to run scenarios or re-run scenarios changing only a few input parameters, compare their results with other scenarios and possibly engage in a dialogue.

One way to fullfill this wish, is to design the tool's interface collaboratively: by inviting different actors in a dialogue about the interface's functionalities before implementing the interface itself.

We start by defining a few :ref:`concepts<concepts-menu>` which come handy when describing the interface and what the users will be able to interact with and see.
One of these concepts is the :ref:`view-component-def`, it is analoguous to a building block we can use to describe (and then implement) the user interface functionalities in a modular way.

It is possible to deploy an interactive presentation of the :ref:`views<view-def>` made with the help of the :ref:`view-component-def` by following `these step <https://github.com/rl-institut/open_plan/blob/dev/website/README.md>`_

We welcome feedback. 

.. _concepts-menu:

Concepts definition
===================

In order to describe the interface, a few definitions are required at first.

.. _view-def:

view
----
    Description of a given state of the user interface: what should the user be able to interact with in that *view*, which other *view* can the user visit from the current *view*. The collection of *views* form together the user interface. Note: the view does not describe how the interface looks like to the user, this is described in the *view-rendering*.

.. _view-component-def:

view-component
--------------
    A *view-component* is a part of a *view* which can be described independently from the view and could be reused in different *views* (a menu bar for example). A *view-component* is described in terms of its attributes and its actions. For example a menu bar has a nested list of items (each item can itself be a list of item: submenus). Each item, if not itself a list, consists of a label (what the user will see) and an action (what will be done upon clicking/selecting the item).

.. _attribute-def:

attribute
---------
    An attribute contains the essential information needed to characterize and render a :ref:`view-def` or a :ref:`view-component-def`. An attribute might be visible in the :ref:`view-def` or :ref:`view-component-def` but it can also just be information. An attribute can be linked to a certain number of :ref:`action-def` and to certain :ref:`requirement-def`.

.. _action-def:

action
------
    An action describes what the user can do in a certain :ref:`view-def` or :ref:`view-component-def`. Each action has an index which is used to link it to an :ref:`attribute-def`.

Example: [index] The user can click on button B to trigger action C

.. _requirement-def:

requirement
------------
A requirement describes specific conditions of a :ref:`view-def`, a :ref:`view-component-def`, an :ref:`action-def` or an :ref:`attribute-def` that should be met. Each requirement has an index which is used to link it to an :ref:`attribute-def`.
.. TODO : rework this sentence
    A requirement describes specific conditions of a :ref:`view-def`, a :ref:`view-component-def`, an :ref:`action-def` or an :ref:`attribute-def`. A requirement specifies necessary actions that need to be done by the user and explains what happens if the requirement is not met. Each requirement has an index which is used to link it to an :ref:`attribute-def`.
 Example: [index] The button B cannot be clicked unless text input C is not filled by user.

.. _view-rendering-def:

view-rendering
--------------
    Description of how a *view* or *component-view* will be rendered on the screen. This belongs to frontend and is where the details about color, size, font, placement on screen matter. For example a menu bar which is a *view-component* can have many different *view-rendering* (horizontal with buttons, expandable vertically only on hover, etc.).

.. _energy-type-def:

energy type
-----------
    An energy type is represented by a bus. It describes the energy carrier for an energy sector: heat, electricity, gas, biomass, H2O.

.. _main-window-def:

main window
-----------
    It is the window from which the user can interact with the open_plan tool on their computer.


.. _widget-def:

widget
------
    Smaller window within the tool's :ref:`main-window-def`.
    A *widget* can be moved around by the user within the :ref:`main-window-def` and collapsed into another *widget* (then each *widget* is accessible via tabs).

.. _views-label:

Views definition
================

.. contents::
   :local:
   :depth: 1

----

.. _landing-label:

.. include:: views/landing.rst


----

.. _scenario_comparison-label:

.. include:: views/scenario_comparison.rst


View-components definition
==========================

.. contents::
   :local:
   :depth: 1

.. it is important to have a blank line before and after the ----, otherwise the reference does not work!


----

.. _welcome-label:

.. include:: view_components/welcome.rst

----

.. _progression_bar-label:

.. include:: view_components/progression_bar.rst

----

.. _menu_bar-label:

.. include:: view_components/menu_bar.rst

----

.. _create_project-label:

.. include:: view_components/create_project.rst

----

.. _load_project-label:

.. include:: view_components/load_project.rst

----

.. _create_scenario-label:

.. include:: view_components/create_scenario.rst

----

.. _load_scenario-label:

.. include:: view_components/load_scenario.rst

----

.. _input_parameter_field-label:

.. include:: view_components/input_parameter_field.rst

----

.. _load_input_dataseries-label:

.. include:: view_components/load_input_dataseries.rst

----

.. _scenario_parameters-label:

.. include:: view_components/scenario_parameters.rst

----

.. _project_parameters-label:

.. include:: view_components/project_parameters.rst

----

.. _es_sector_selector-label:

.. include:: view_components/energy_system_sector_selector.rst

----

.. _es_network-label:

.. include:: view_components/energy_system_network.rst

----

.. _es_component-label:

.. include:: view_components/energy_system_component.rst

----

.. _export_project-label:

.. include:: view_components/export_project.rst

----

.. _view_specific_documentation-label:

.. include:: view_components/view_specific_documentation.rst

----

.. _visualize_dataseries-label:

.. include:: view_components/visualize_dataseries.rst

----

.. _project_location-label:

.. include:: view_components/project_location.rst

----

.. _read_write_files-label:

.. include:: view_components/read_write_files.rst

----

.. _project_list-label:

.. include:: view_components/project_list.rst

----

.. _scenario_list-label:

.. include:: view_components/scenario_list.rst

----


Abstract-components Definition
==============================


.. contents::
   :local:
   :depth: 1

----

.. _scenario-label:

.. include:: abstract_components/scenario_list.rst


Inputs definition
=================

.. contents::
   :local:
   :depth: 1

----

.. _inputs-label:

.. include:: input_output/inputs.rst