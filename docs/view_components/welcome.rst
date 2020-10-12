.. _welcome-label:

Welcome page
------------

The welcome window serves as an orientation point or introduction for the user and let them know, in as brief words (and other audiovisual content) as possible, what to expect from the tool.


Attributes
^^^^^^^^^^

* **Welcome message**
    * A text

* **Video intro message**
    * A short, 3 minute video clip that provides the important information such as tool features, capabilities, where to find help, etc., very briefly
    * This clip is embedded into the welcome pop-up. The user can view it on YouTube (or Vimeo) on a separate tab of the browser by clicking on a link on the video

* **Check-box `Do not show again`**
    Disable/enable the display of the welcome view-component when tool is started.

* **Hyperlinks**
    * Clickable links to read more, documentation, examples, use-cases, video tutorials, code-base (GitHub repo) and contact us

Actions
^^^^^^^

* Checking the `Do not show again` check-box would disable the pop-up from appearing everytime the software is launched
* Clicking on the hyperlinks will open the respective topic in a separate tab on the browser (e.g.: GitHub repo)

Requirement
^^^^^^^^^^^

* By default, the welcome view-component should be displayed to the user everytime the software is started
* If the user ticks the check-box *Do not show again*, the welcome view-component should not appear to the user during any subsequent launch of the tool
* The user could later re-enable the appearance of the pop-up window through *Display* or *Preferences* menu in *Settings*

Link with other view-components
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ref:`landing-view`:

* ref:`file menu`:
     user can re-enable appearance of the welcome view-component through options within the file menu

Rendering of the view-component
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The welcome view component could be either a popup on top of the ref`:landing-view`, a part of the landing view or a view on its own.

.. image:: ../assets/welcome_popup.png
   :width: 400
   :alt: A snapshot of the proposed welcome pop-up window
