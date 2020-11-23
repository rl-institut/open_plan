.. _project_location-label:

Map with Project Location
-------------------------

A rectangular container that contains an interactive map.

This can be implemented for eg., with Leaflet or Folium libraries.

Attributes
^^^^^^^^^^

**Project area highlighted**
    The project area, obtained using coordinates supplied by the user and energy cell area, should be highlighted on the map as a polygon.

    Actions index: 1

    Requirements index: 1

Actions
^^^^^^^

1. User can zoom in, zoom out, pan around using the input from their mouse

Requirements
^^^^^^^^^^^^

1. User must provide the project location coordinates and energy cell area parameters in :ref:`load_project_parameters-label`

Link with views
^^^^^^^^^^^^^^^
.. use :ref:`<view>-label` to cross link to the view's description directly

:ref:`project_parameters-label`
    The parameters necessary to generate the project location map view-component are input by the user through this view-component

:ref:`load_project_parameters-label`
    Description of the link

Link with other view-components
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:ref:`<view_component1>-label`
    Description of the link

Rendering of the view-component
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As a rectangular container displaying an interactive map of the project location highlighted as either a point or as a polygonal area on the map.
