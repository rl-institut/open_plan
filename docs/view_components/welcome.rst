Welcome page
------------

This view-component is an introduction for the first-time users. It describes what they can expect from the tool.


Attributes
^^^^^^^^^^

**Welcome message**
    * A text

**Video intro message**
    * A short, 3 minute video clip that provides the important information such as tool features, capabilities, where to find help, etc., very briefly.
    * This clip is embedded into the welcome pop-up. The user can view it on YouTube (or Vimeo) on a separate tab of the browser by clicking on a link on the video.

**List of Hyperlinks**
    Clickable links to read more, documentation, examples, use-cases, video tutorials, code-base (GitHub repo) and contact us.

    Action index: 1

**Check-box: do not show again**
    Disable/enable the display of the welcome view-component when tool is started.

    Properties:
        * id `cb_welcome_show_again`
        * unticked by default

    Action index: 2

Actions
^^^^^^^

1. Clicking on the hyperlinks will open the respective topic in separate tabs of the browser.
2. Checking the `Do not show again` check-box would disable the display of this view component everytime the software is launched.
3. The user can close the welcome window by clicking the :guilabel:`&X` button in the top right corner.

Requirement
^^^^^^^^^^^

1. By default, the welcome view-component should be displayed to the user everytime the software is started.
2. If the user ticks the check-box *Do not show again*, the welcome view-component should not appear to the user during any subsequent launch of the tool.

Link with other views 
^^^^^^^^^^^^^^^^^^^^^

This window is displayed by default on top of everything every time the tool is launched.


Link with other view-components
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:ref:`landing-label`


:ref:`menu_bar-label`
      The user can later re-enable the appearance of the  welcome view-component by clicking *Display welcome view* in *Preferences* from the menu.

Rendering of the view-component
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This view-component could be either a popup on top of the :ref:`landing-view`, :ref:`widget-def` in the landing view or a :ref:`view-def` on its own.

The welcome message should be centered and not contain very long text, but rather bullet points with links to more detailed documentation. The video should be placed on the top left of the view-component and start automatically without the sound.

Below the welcome message the hyperlinks could be listed and centered.

The *Do not show again* check-box can be displayed on the bottom of the view-component (bottom-left?) with larger fontsize such that the user cannot miss it. It should be unticked by default.
