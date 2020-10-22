Project parameters
------------------

Inputs parameters to set the context of the project.


Attributes
^^^^^^^^^^

**List of input parameters**

    Each input parameter will be available to the user via :ref:`input_parameter_field-label`

    Properties of each input:
        - Input type
        - Input default value
        - Help text
        - If it is mandatory or optional
        - Link in documentation


As the parameters in this list should also be accessible in a more general parameter documentation in ReadTheDocs, they will be automatically listed here from either a .yml or csv file.

The following inputs stay here for the moment and will be reformated then

- Localisation
    | The geographical localisation of the project.
    | This can allow to download appropriate dataset.
- Project lifetime
     This can be used for calculations?
- Weighted Average Cost of Capital
     This can be used for calculations?
- Project name
     Give a name to that project.
- Project description (optional)
    Give a short description of the project

Actions
^^^^^^^
1. User can edit the value of the input parameters manually.
2. User can edit the value of the input parameters by loading a project from :ref:`load_project-label`


Requirement
^^^^^^^^^^^
1. The requirements of :ref:`input_parameter_field-label` apply for each input parameter

Link with other view-components
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Rendering of the view-component
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The rendering of :ref:`input_parameter_field-label` apply for each input parameter
