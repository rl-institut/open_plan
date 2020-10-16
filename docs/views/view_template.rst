.. To insert the view into the ReadTheDocs structure, please use this template and replace <view_name> by the name of your file when copying the following line in tool_interface.rst.:
    .. include:: views/<view_name>.rst

.. Refer to this view using :ref:`<view_name>-label`
.. Change <view_template> for the title of your view

.. _view_template-label:

View template
-------------
.. Put the name of your view here instead of <view_template>. Make sure the number of "-" below matches exactly
    the number of character taken by your title

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

Actions
^^^^^^^
.. an action is something one can perform directly from the view-component
    (i.e. "clicking on this attribute should update this other attribute")

1. Action 1
2. Action n

Requirement
^^^^^^^^^^^
.. a requirement is a binding rule which cannot be described directly by an action
    or which describes redundant actions
    (i.e. "it should not be possible to click on this attribute while the value of this other
    attribute is not defined", or "after changing the value of an already defined attribute,
    one should see a difference in the rendering of the attribute"

1. Requirement 1
2. Requirement n

Active view-components
^^^^^^^^^^^^^^^^^^^^^^
.. use :ref:`<view_component>-label` to cross link to the view-component's description directly
.. Actions and requirements of active view components are described in the view component description

* View component A
* View component B

Link with other views
^^^^^^^^^^^^^^^^^^^^^
.. use :ref:`<view>-label` to cross link to the view's detailed description directly

**View A**
    Description of the link

Rendering of the view
^^^^^^^^^^^^^^^^^^^^^
.. TBD