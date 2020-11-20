Energy System network
---------------------

This view-component will help the user to define their energy system model


Attributes
^^^^^^^^^^

**list of energy busses**
    A list of energy busses
    
    Properties:
        * id: `es_bus_list`
        * each bus has a unique id
        * each bus has an associated :ref:`energy-type-def`

    Actions index: 1, 2, 4

    Requirements index:

**button** :guilabel:`&Add bus`

    Linked to the action of adding a bus to the `es_bus_list`

    Properties:
        * id `add_es_bus`

    Actions index: 1, 5, 6

    Requirements index:

**button** :guilabel:`&Remove bus`

    Linked to the action of removing a bus from the `es_bus_list`

    Properties:
        * id `remove_es_bus`

    Actions index: 2, 3

    Requirements index:

**list of energy system component**
    A list of *energy system components*
    
    Properties:
        * id: `es_component_list`
  
    Actions index: 1, 2, 4


**button** :guilabel:`&Add component`
    Linked to the action of adding an energy system component to the `es_component_list`

    Properties:
        * id `add_es_component`

    Actions index: 1, 5, 6

    Requirements index:

**button** :guilabel:`&Remove component`
    Linked to the action of removing an energy system component from the `es_component_list`

    Properties:
        * id `remove_es_component`

    Actions index: 2, 3

    Requirements index:

**Draw area**
    Area where the user could drag and drop components and connect them, or simply see a rendering
    of the energy system graph withtout being able to interact with it

    Properties:
        * id `network_schema`

    Actions index: 4.

    Requirements index:


**Text area**
    Displays potential error messages arising from wrong configuration of *energy system network* or single *energy system component*

    Properties:
        * id `error_log`


Actions
^^^^^^^

1. Clicking on the `add es_bus`/`add es_component` button adds a *Bus* or an *energy system component* to the `es_bus_list`/`es_component_list`, respectively.
2. Clicking on the `remove_es_bus`/`remove_es_component` button removes the currently selected *Bus* or *energy system component* from the `es_bus_list`/`es_component_list`, respectively.
3. Clicking on the `remove_es_bus`/`remove_es_component` button when no *Bus* or *energy system component* is currently selected sends a log message to the `error_log`.
4. Selecting a bus or an energy system component in `es_bus_list`, `es_component_list` or in `network_schema` allows the user to visualise and/or edit its properties in another view-component.
5. When a the user add a *Bus* or *energy system component* by clicking on the `add_es_bus`/`add_es_component`, they can visualise and/or edit its properties in another view-component.
6. When a the user add a *Bus* or *energy system component* by clicking on the `add_es_bus`/`add_es_component`, they can to see it in the `network_schema`.

Requirements
^^^^^^^^^^^^

1. If not defined by the user, an additional Sink component to dump excess energy flow is defined and connected automatically to one *Bus* in the *energy system network*
2. If not defined by the user, an additional Source component to provide slack energy flow is defined and connected automatically to one *Bus* in the *energy system network*
3. notifications informing the user about potential problems with their energy system model should be displayed in the `error_log` text area. Problems could be such as a failure to meet any of the other requirements, an undefined property value of an *energy system component*, or a *Bus* without connection to another *energy system component*


Link with other view-components
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
:ref:`es_component-label`

Rendering of the view-component
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The buttons need to be visible at all time, as the selection of *energy system components* or *Busses* can be done either from the lists `es_bus_list`, `es_component_list` or from `network_schema`, they do not necessarily need to be seen at the same time (they could be side by side or accessible via tabs)
