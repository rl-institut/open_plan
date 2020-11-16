Energy sector selector
----------------------

The user can choose which :ref:`energy-type-def` they would like to use in their energy system. This choice will impact which components of the energy system model are available.

Attributes
^^^^^^^^^^

**list of available energy sectors**
    Contains the possible energy sectors a user can choose from

    Properties:
        * id `es_sector_avail_list`
        * each sector has an associated :ref:`energy-type-def`
        * each sector has an associated icon

**list of selected energy sectors**
    Contains the choices selected by the user from the `es_sector_avail_list`
    
    Properties:
        * id `es_sector_select_list`
        * each sector has an associated :ref:`energy-type-def`

**list of connection between selected energy sectors**
    Indicates whether there is a coupling between two sectors

    Properties:
        * id `es_sector_coupling_list`
        * each element is a list of two interconnected sectors
        * an empty list means that all sectors are independent

Actions
^^^^^^^

1. The user can select the sector they want to include in their energy system model from the `es_sector_avail_list` by clicking on the list item
2. The user should be able to indicate if two sectors are interconnected (could be clicking on greyed-out line connecting sectors visually)

Requirement
^^^^^^^^^^^

1. Any `es_sector_select_list` item has to be an item of `es_sector_avail_list`.


Link with other view-components
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:ref:`es_network-label`
    Only :ref:`es_component` compatible with the selected energy sectors can be included in the energy system

Rendering of the view-component
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Each sector in the list is represented by its icon. The energy sectors in the `es_sector_select_list` are rendered in color and the remaining energy sectors (in `es_sector_avail_list` but not in `es_sector_select_list`) are rendered in shades of grey.
Each sector is visually connected to all the other sectors by a greyed-out line (no active sector coupling), If the line is display in bright color (e.g. after an activating click on it by the user) it means the two sectors are interconnected directly.
