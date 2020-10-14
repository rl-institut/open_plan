..
    To insert the view component into the ReadTheDocs structure, please rename the file
    and replace <view_component> by the name of this file in the two lines below.
     _<view_component>-label:
    .. include:: view_components/<view_component>.rst
..
    Then move them to the file tool_interface.rst in the list under the title "
    View-components definition"
..
    one can then cross link to this view component by using
    :ref:`<view_component>-label`

..  change the title of your view component, make sure the number of "-" below matches exactly
    the number of character taken by your title

<Component title>
-----------------

Attributes
^^^^^^^^^^
.. Please refer to the definition of what an attribute is in the tool_interface.rst fileg
.. The properties should be filled in only if applicable.

**Attribute A**
    Description

    Properties:
        * Property 1
        * Property n

    Actions index:

    Requirements index:

.. [One liner] corresponding indexes from the Actions and Requirements paragraph

**Attribute B**
    Description

    Properties:
        * Property 1
        * Property n

    Actions index:

    Requirements index:

.. [One liner] corresponding indexes from the Actions and Requirements paragraph below

Actions
^^^^^^^
..
    an action is something one can perform directly from the view-component
    (i.e. "clicking on this attribute should update this other attribute")

1. Action 1
2. Action n

Requirements
^^^^^^^^^^^^
..
    a requirement is a binding rule which cannot be described directly by an action
    or which describes redundant actions
    (i.e. "it should not be possible to click on this attribute while the value of this other
    attribute is not defined", or "after changing the value of an already defined attribute,
    one should see a difference in the rendering of the attribute"

1. Requirement 1
2. Requirement n

Link with views
^^^^^^^^^^^^^^^^^^^^^
.. use :ref:`<view>-label` to cross link to the view's description directly

**:ref:`<view1>-label`**
    Description of the link

**:ref:`<view2>-label`**
    Description of the link

Link with other view-components
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. use :ref:`<view_component>-label` to cross link to the view-component's description directly

**:ref:`<view_component1>-label`**
    Description of the link

**:ref:`<view_component2>-label`**
    Description of the link

Rendering of the view-component
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. TBD
