.. _doc_text_to_speech:

Text to Speech
==============

Requirements for functionality
------------------------------

Godot includes text-to-speech functionality. You can find these under the :ref:`DisplayServer class <class_DisplayServer>`.

Godot depends on system libraries for text-to-speech functionality. These libraries are installed by default on Windows and MacOS, but not on all Linux distros. If they are not present, text-to-speech functionality will not work. Speifically, the ``tts_get_voices`` method will return an empty list, indicating that there are no usable voices.

Both Godot users on Linux and end-users on Linux running Godot games need to ensure that their system includes the system libraries for text-to-speech to work. Please consult with your own distro's documentation to determine what libraries you need to install.

For example, on Arch-based systems, Godot requires ``spd-say``, ``festival``, and ``espeakup``.

Best Practices
--------------

The best practices for text-to-speech, in terms of the ideal player experience for blind players, is to integrate directly with the screen-reader APIs (such as NVDA's API) to send output directly to it. This provides advanced functionality for blind players, such as being able to traverse previous output forwards and backwards, to replay, and to play at a faster or slower rate as suits them. Godot currently doesn't support screen-reader API integration.

With the current state of the Godot text-to-speech APIs, best practices include:

- Develop the game with text-to-speech enabled, and ensure that everything sounds correct
- Allow players to control which voice to use, and save/persist that selection across game sessions
- Allow players to control the speech rate, and save/persist that selection across game sessions

This provides your blind players with the most flexibility and comfort available when not using a screen reader, and minimizes the chance of frustrating and alienating them.
