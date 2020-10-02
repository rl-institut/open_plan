.. _es-network-label:


Energy System network
---------------------


Attributes
^^^^^^^^^^

#. **list of energy busses**
    properties:
        - each bus has a unique id
        - each bus has an associated :ref:`energy-type-def`

#. **button `add bus`**

#. **button `remove bus`**

#. **list of energy system component**
    properties:
        - each energy system component has a unique id
        - each energy system component has a list of associated :ref:`energy-type-def`
        - each energy system component can have in and/or out connection to one of the energy busses or one of the other energy system components
        - each energy system component has a type (sink, source, transformer, storage)

#. **button `add energy system component`**

#. **button `remove energy system component`**

Actions
^^^^^^^

#. The user should be able to add a bus or an energy system component to the energy system network by clicking on the `add bus`/`add component` button resp.
#. The user should be able to remove a selected bus or energy system component from the energy system network by clicking on the `remove bus`/`remove component` button resp.
#. The user should be able to select a bus or an energy system component and this should allow visualisation or edition of the properties in another view-component displaying.

Requirements
^^^^^^^^^^^^

* each energy bus needs to be connected to at least one energy system component of type source
* if the user does not provide an energy system component of type sink for an energy bus, the latter is created automatically


Link with other view-components
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- ref:`es-component-label`

Rendering of the view-component
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^