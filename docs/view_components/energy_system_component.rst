Energy system component
-----------------------

Attributes
^^^^^^^^^^
.. Please refer to the definition of what an attribute is in the tool_interface.rst fileg
.. The properties should be filled in only if applicable.

:ref:`energy-type-def`

    Energy type linked to the different energy sectors (e.g. heat, electricity, ...)


**Component type**
    Can be one of (Source, sink, transformer, storage, bus)


**Unique id**
    A positive integer number to identify the component uniquely within the list of energy system component of the :ref:`es-network-label`


**Icon**
    An image which can be used for rendering of the view-component

    Properties:
        * path to the icon file

    Actions index:

    Requirements index:

**Inward energy connection**
    A list of other components's ids which are connected to this component and provide it with energy

    Requirements index: 1, 5, 6

**Outward energy connection**
    A list of other components's ids which are connected to this component and drain energy from it

    Requirements index: 1, 5, 6

Actions
^^^^^^^

1. Double-clicking on the rendering of the energy system component allow the user to edit its attributes (except id)

Requirements
^^^^^^^^^^^^
1. An energy system component cannot de defined without being connected to another energy system component
2. A component of type Source cannot be connected to a component of type Sink
3. A component which is not of type bus, should have at least one connection to component of type bus bus
4. A component which is of bus type, should have at least one source and one sink type connected to it
5. A component of type Sink do not have Outward energy connection
6. A component of type Source do not have Inward energy connection


Link with views
^^^^^^^^^^^^^^^

It is currently not directly linked to a view

Link with other view-components
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:ref:`es-network-label`
    Description of the link

Rendering of the view-component
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This energy system component can be rendered as a list item within :ref:`es-network-label`'s `es_component_list` attribute or via its icon within :ref:`es-network-label`'s `network_schema` attribute.