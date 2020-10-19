Energy sector selector
----------------------

Attributes
^^^^^^^^^^

**list of available energy sectors `es_sector_avail_list`**
    Contains the possible energy sectors a user can choose from

    properties:
        - each sector has an associated :ref:`energy-type-def`

**list of selected energy sectors `es_sector_select_list`**
    Contains the choices selected by the user from the `es_sector_avail_list`
    properties:
        - each sector has an associated :ref:`energy-type-def`



Actions
^^^^^^^

1. The user can select the sector they want to include in their energy system from the `es_sector_avail_list`

Requirement
^^^^^^^^^^^

1. Any `es_sector_select_list` items has to provide from `es_sector_avail_list`.

Link with other view-components
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:ref:`es-network-label`

Rendering of the view-component
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
