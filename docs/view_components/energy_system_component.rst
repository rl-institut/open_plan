Energy system component
-----------------------

Define the view a user has when creating or editing a component of its energy system

Attributes
^^^^^^^^^^
.. Please refer to the definition of what an attribute is in the tool_interface.rst fileg
.. The properties should be filled in only if applicable.

**Energy type**
    ref:`energy-type-def` linked to the different energy sectors (e.g. heat, electricity, ...)


**Component type**
    Can be one of [Source, Sink, Transformer, Storage, Bus]


**Unique id**
    A positive integer number to identify the component uniquely within the list of energy system components of the :ref:`es_network-label` 


**Icon**
    An image which can be used for rendering of the view-component

    Properties:
        * path to the icon file

    Actions index:

    Requirements index:

**Input energy flow**
    A list of other components's ids which are connected to this component and provide it with energy

    Requirements index: 1, 5, 6

**Output energy flow**
    A list of other components's ids which are connected to this component and drain energy from it

    Requirements index: 1, 5, 6

Actions
^^^^^^^

1. Double-clicking on the rendering of the *energy system component* allow the user to edit its attributes (except id)

Requirements
^^^^^^^^^^^^
1. As long as the *energy system component* is not connected correctly to another *energy system component* the Icon-frame is displayed in another colour
2. An *energy system component* which is not of *component type* Bus can not be connected to another *energy system component*, which is not of *component type* Bus
3. An *energy system component* which is not of *component type* Bus, should have at least one connection to an *energy system component* of *component type* Bus
5. An *energy system component* of *component type* Sink has a connection to *Input energy flow*, but no connection to *Output energy flow*
6. An *energy system component* of *component type* Source has a connection *Output Energy flow*, but no connection to *Input energy flow*


Link with views
^^^^^^^^^^^^^^^

It is currently not directly linked to a view

Link with other view-components
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:ref:`es_network-label`
   The component is inserted within the energy system model described in this other view-component

Rendering of the view-component
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This *energy system component* can be rendered as a list item within :ref:`es_network-label`'s `es_component_list` attribute or via its icon within :ref:`es_network-label`'s `network_schema` attribute.
