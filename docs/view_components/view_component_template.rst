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

.. [One liner] corresponding indexes from the Actions and Requirements paragraph

Actions
^^^^^^^
1. Action 1
2. Action n

Requirements
^^^^^^^^^^^^
1. Requirement 1
2. Requirement n

Link with views
^^^^^^^^^^^^^^^^^^^^^
**View A**
    Description of the link

**View B**
    Description of the link

Link with other view-components
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**View component A**
    Description of the link

**View component B**
    Description of the link

Rendering of the view-component
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. TBD
