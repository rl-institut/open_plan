Load input data-series
----------------------

User loads a file containing a data-series as input for a relevant parameter and is able to quickly visualize the data.

Attributes
^^^^^^^^^^

**Label**
    Name of the parameter which would be displayed close to the input field


**Input field**
    Actions index: 1

    Requirements index:

**Input Unit**
    Unit of the input parameter

    Actions index: 1

    Requirements index: 2

**Load File button**
    Actions index: 2

    Requirements index:

**Visualize Data button**
    Actions index: 3

    Requirements index:

**Boolean Mandatory Input**
    If true, the parameter must be defined by the user

    Requirements index: 3, 4

Actions
^^^^^^^

1. User can directly provide the path of the file to be loaded as text in the text field
2. Clicking on Load File button will open a pop-up window **(link the vc (TBD) link here)**
3. Clicking on the Visualize Data button will open a pop-up window with a table and plot of the data-series :ref:`visualize_dataseries-label`
4. User can choose unit amongst a list of generic units, or input it by typing it in. (this is known as an editable combo box)

Requirements
^^^^^^^^^^^^

1. All parameters that require a data-series must be given input through this view-component
2. The physical units which are commonly used for energy and power should be available there (then converted internally to Joule and Watt)
3. For mandatory input fields, the fields must be denoted by an asterisk adjacent to the field
4. If the user does not provide input for a mandatory field and tries to proceed further, the field should be highlighted so as to alert the user
5. The Load File and Visualize Data buttons should be present adjacent to the Input Field

Link with views
^^^^^^^^^^^^^^^

:ref:`<view1>-label`
    Description of the link

:ref:`<view2>-label`
    Description of the link

Link with other view-components
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. use :ref:`<view_component>-label` to cross link to the view-component's description directly

:ref:`input_parameter_field-label`
    Both the view-components share some attributes

:ref:`<view_component2>-label`
    .. TBD (Link to the VC to browse and select files to be loaded)

:ref:`visualize_dataseries-label`
    A pop-up window displaying a sample of the input data-series file with a plot of the data alongside

Rendering of the view-component
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. TBD
