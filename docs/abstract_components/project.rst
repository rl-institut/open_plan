Project
-------

..
    Insert definition of the project here, once it is agreed upon.

Attributes
^^^^^^^^^^

    **Project as an object**
        Project is an object that exists in the computer's temporary memory (RAM). It can be considered as the a concept that holds one or more scenarios of the energy system simulation sharing some common characteristics.

        It could be saved to the permanent memory by saving the data the object holds to disk as a file of an appropriate format.

Actions
^^^^^^^

1. Existing project object can be loaded through the *load_project* view component in the Landing Page view
2. New project object can be created through the UI of the tool using the *create_project* view component in the Landing Page view
3. Current project object can be saved to the disk by the user through the *Save Project* button that connects to the *read_write_files* view-component


Requirements
^^^^^^^^^^^^

1. The objects must be accessible to other relevant view components
2. External project objects created in other software that are to be imported into open_plan should adhere to the data standards
3. The project object be saved to disk in an appropriate format before exiting the tool in order to be accessible later

Link with views
^^^^^^^^^^^^^^^

:ref:`read_write_files-label`


Link with other view-components
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:ref:`read_write_files-label`
    This view-component is required to read and write files from and to the disk respectively