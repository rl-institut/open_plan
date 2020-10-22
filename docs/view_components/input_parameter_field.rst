Input Parameter Field
---------------------

This view-component enables the user input appropriate data in different views.

Attributes
^^^^^^^^^^

**Label**
    Each field has a label or keyword that describes the parameter or input for which a single alphanumeric value object,
    i.e., a scalar input or an object holding a data series must be provided by user

    Actions index:

    Requirements index:

**Input Type**
    Type of input object, such as whether it is a numeric or string or data series

    Actions index:

    Requirements index: 1


**Input Field**
    The GUI element where the input object is entered by the user. Changes, depending on input type

    Actions index:

    Requirements index: 1

**Default/Placeholder Value**
    The default value provided for each input field

    Actions index: 1

    Requirements index:

**Helper/Prompt Text**
    A brief definition/description of the parameter with the type of inputs and specifications, if any

    Actions index:

    Requirements index:

**Link to Documentation**
    A clickable icon or text as with hyperlink that leads the user the user to a section of the tool documentation where
    a thorough description of the label/parameter is provided

    Actions index: 2

    Requirements index:

**Mandatory Input Indicator**
    An asterisk or exclamatory mark signifying to the user that it is obligatory to provide an input

    Actions index:

    Requirements index: 2, 3


Actions
^^^^^^^
1. User can overwrite the default/placeholder values in the input fields and input appropriate data objects
2. User can directly navigate to the relevant sections of the documentation by clicking an icon next to the field label

Requirements
^^^^^^^^^^^^
1. The field must change depending on the type of the input. Some inputs could just be one numeric value, while others might be a series of values in the form a CSV file
2. For mandatory input fields, the fields must be denoted by an asterisk adjacent to the field
3. If the user does not provide input for a mandatory field and tries to proceed further, the field should be highlighted so as to alert the user
4. The default/placeholder values for which the user has not provided any own-input must be rendered differently than the values in input fields with input objects supplied by the user

Link with views
^^^^^^^^^^^^^^^

.. TBD

Link with other view-components
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. TBD

Rendering of the view-component
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Rectangular box with the label placed above, and the helper text placed below
* Icon linking to docs placed next to the label above the rectangular input field
* In case of non-scalar inputs, 'Upload' button is placed to the right of the input field

