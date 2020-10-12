.. _scenarios-label:

Scenarios
---------
* This component depends a lot on the tool mechanism which has not been discussed deeply yet.
* Each project consists of a model that is run in a simulation following a specific scenario.

Attributes
^^^^^^^^^^
*This section will be filled automatically with the input/output excel sheet, here is one example:*

**Source power mix**

* Percentage of each source of power (inclusive % from Grid)

Actions
^^^^^^^
**Source power mix**

* The user can view and edit the default value
* The user can click on a "?" icon next to the attribute to learn more about it and explains the requirements.


Requirement
^^^^^^^^^^^
**Source power mix**

* The input value needs to be in % and the sum of all input fields for this attribute need to make 100%. If these requirements are not met, the input field should be highlighted in red.

Link with other view-components
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**Source power mix**

* Each Source power mix depends on the technologies put in the model by the user


Rendering of the view-component
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**Source power mix**

* Input number box as % for each technology+
* All boxes are displayed vertically like:

+-----------------+---------------+------------+
| Technology 1:   |  input box    |  "?" icon  |
+-----------------+---------------+------------+
