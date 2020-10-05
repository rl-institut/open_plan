.. _es-network-label:


Energy System network
---------------------


Attributes
^^^^^^^^^^

#. **list of energy busses `es_bus_list`**
    properties:
        - each bus has a unique id
        - each bus has an associated :ref:`energy-type-def`

#. **button `add_es_bus`**

#. **button `remove_es_bus`**

#. **list of energy system component `es_component_list`**
    properties:
        - each energy system component has a unique id
        - each energy system component has a list of associated :ref:`energy-type-def`
        - each energy system component can have in and/or out connection to one of the energy busses or one of the other energy system components
        - each energy system component has a type (sink, source, transformer, storage)

#. **button `add_es_component`**

#. **button `remove_es_component`**

#. **draw area `network_schema`**
    properties:
        -

#. **text area `error_log`**
    displays potential error messages arising from wrong configuration of energy system network or single energy system component




Actions
^^^^^^^

#. Clicking on the `add bus`/`add component` button adds a bus or an energy system component to the energy system network, respectively.
#. Clicking on the `remove_es_bus`/`remove_es_component` button removes the currently selected bus or energy system component from the energy system network, respectively.
#. Clicking on the `remove_es_bus`/`remove_es_component` button when no bus or energy system component is currently selected sends a log message to the `error_log`.
#. Selecting a bus or an energy system component in `es_bus_list`, `es_component_list` or in `network_schema` allows the user to visualise and/or edit its properties in another view-component.
#. When a the user add a bus or an energy system component by clicking on the `add_es_bus`/`add_es_component`, they can visualise and/or edit its properties in another view-component.
#. When a the user add a bus or an energy system component by clicking on the `add_es_bus`/`add_es_component`, they can to see it in the `network_schema`.

Requirements
^^^^^^^^^^^^

* each energy bus needs to be connected to at least one energy system component of type source
* if the user does not provide an energy system component of type sink for an energy bus, the latter is created automatically
* notifications informing the user about potential problems with their energy system should be displayed in the `error_log` text area. Problems could be such as a failure to meet any of the other requirements, an undefined property value of an energy system component, or a bus connected to no energy system component


Link with other view-components
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- ref:`es-component-label`

Rendering of the view-component
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The buttons need to be visible at all time, as the selection of energy system components or busses can be done either from the lists `es_bus_list`, `es_component_list` or from `network_schema`, they do not necessarily need to be seen at the same time (they could be side by side or accessible via tabs)