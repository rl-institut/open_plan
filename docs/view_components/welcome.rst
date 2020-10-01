.. _welcome-label:

Welcome page
------------

The welcome window serves as an orientation point for the user and let them know, in as brief words (and other audiovisual content) as possible, what to expect from the tool. It is also the launch point from where the user begins their energy systems simulation.

The welcome page is to be implemented as an optional pop-up that springs up on the landing page when the user launches the tool. In this section, a structure for the welcome page is proposed, subject to further discussion with the stakeholders.

Attributes
^^^^^^^^^^

#. **Welcome message on the pop-up**
    * A single line text message

#. **Video intro message**
    * A short, 3 minute video clip that provides the important information such as tool features, capabilities, where to find help, etc., very briefly
    * This clip is embedded into the welcome pop-up. The user can view it on YouTube (or Vimeo) on a separate tab of the browser by clicking on a link on the video

#. **Check-box to disable the welcome pop-up**

#. **Hyperlinks**
    * Clickable links to read more, documentation, examples, use-cases, video tutorials, code-base (GitHub repo) and contact us

Actions
^^^^^^^

* Pop-up that springs up everytime the software is launched freshly
* Checking the tick-box would disable the pop-up from appearing everytime the software is launched
* The user could later re-enable the appearance of the pop-up window through *Display* or *Preferences* menu in *Settings*
* Clicking on the hyperlinks will open the respective topic in a separate tab on the browser (e.g.: GitHub repo)

Rendering of the view-component
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: docs/assets/welcome_popup.png
   :width: 400
   :alt: A snapshot of the proposed welcome pop-up window
