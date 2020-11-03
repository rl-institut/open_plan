Input Parameter Field
---------------------

This view-component enables the user input appropriate data in different views.

Attributes
^^^^^^^^^^

**Label**
    Name of the parameter which would be displayed close to the input field


**Input Type**
    Type of input parameter. One of int, float, str, array of int, float or str, matrix of int or float, timeseries (an array with timestamp mapped to each values), csv file

    Requirements index: 1

**Input Unit**
    Unit of the input parameter

    Actions index: 4

    Requirements index: 5

**Input Field**
    An interactive GUI element via which the user can provide a value to the input parameter.

    It depends on input type in the following way

    .. csv-table:: Numbers
       :header: "Input type", "Input field"

             int,  Text input
             float, Text input
             str, Text input
             str, Text input
             array, :ref:`load_input_dataseries-label`
             matrix, :ref:`load_input_dataseries-label`
             timeseries, :ref:`load_input_dataseries-label`
             csv file, :ref:`load_input_dataseries-label`

    Requirements index: 1

**Default/Placeholder Value**
    The default value provided for each input parameter

    Actions index: 1

**Link to Documentation**
    Hyperlink that leads the user to the full documentation of the input parameter TODO: add link to RTD here

    Actions index: 3

**Helper icon**
    An image which can be used for rendering of this attribute

    Properties:
        - path to the icon file

    Actions index: 2

**Helper Text**
    A brief description of the parameter with the type of inputs and specifications, if any.

    Actions index: 2

**Boolean Mandatory Input**
    If true, the parameter must be defined by the user

    Requirements index: 2, 3

Actions
^^^^^^^
1. User can overwrite the default/placeholder value in the input field by a simple click
2. User can get brief information about the input parameter by hovering on the helper icon
3. User can directly navigate to the relevant sections of the documentation by clicking on the documentation link below the helper text (action 2. need to be performed before this one)
4. User can choose unit amongst a list of generic units, or input it by typing it in. (this is known as an editable combo box)

Requirements
^^^^^^^^^^^^
1. The field must change depending on the type of the input. Some inputs could just be one numeric value, while others might be a series of values in the form a CSV file
2. For mandatory input fields, the fields must be denoted by an asterisk adjacent to the field
3. If the user does not provide input for a mandatory field and tries to proceed further, the field should be highlighted so as to alert the user
4. The default/placeholder values for which the user has not provided any own-input must be rendered differently than the values in input fields with input objects supplied by the user
5. The physical units which are commonly used for energy and power should be available there (then converted internally to Joule and Watt)

Link with views
^^^^^^^^^^^^^^^

.. TBD

Link with other view-components
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:ref:`project_parameters-label`

:ref:`scenario_parameters-label`

Rendering of the view-component
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The label is placed above the input field and the helper icon to the right of the label. The helper text is displayed in a tooltip when user hover over the helper icon.
The link to documentation should be at the bottom of the tooltip with the text "More details...".
The rendering of the input field is either a text input or a :ref:`load_input_dataseries-label`. The parameter unit editable combobox is placed next to the input field.
An asterisk is placed next to the label (between label and helper icon) if the parameter input is mandatory.