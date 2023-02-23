.. _doc_text_to_speech:

Text to speech
==============

Basic Usage
-----------

Basic usage of text-to-speech involves the following one-time steps:

- Query the system for a list of usable voices
- Store the ID of the voice you want to use

Once you have the voice ID, you can use it to speak some text:

::

    # One-time steps
    var voices:Array = DisplayServer.tts_get_voices()
    # Pick a voice. Here, we arbitrarily pick the first voice.
    var voice_data:Dictionary = voices[0]

    # Say "Hello, World!"
    DisplayServer.tts_speak("Hello, World!", voice_data["id"])

    # Say a longer sentence, and then interrupt it.
    # Note that this method is asynchronous: execution proceeds
    # to the next line immediately, before the voice finishes speaking.
    
    var long_message:String = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur"

    DisplayServer.tts_speak(long_message)

    # Immediately stop the current text mid-sentence and say goodbye instead
    DisplayServer.tts_stop()
    DisplayServer.tts_speak("Goodbye!", voice_data["id"])


Requirements for functionality
------------------------------

Godot includes text-to-speech functionality. You can find these under the :ref:`DisplayServer class <class_DisplayServer>`.

Godot depends on system libraries for text-to-speech functionality. These libraries are installed by default on Windows and macOS, but not on all Linux distributions. If they are not present, text-to-speech functionality will not work. Specifically, the ``tts_get_voices()`` method will return an empty list, indicating that there are no usable voices.

Both Godot users on Linux and end-users on Linux running Godot games need to ensure that their system includes the system libraries for text-to-speech to work. Please consult with your own distibution's documentation to determine what libraries you need to install.

For example, on Arch Linux-based systems, Godot requires ``spd-say``, ``festival``, and ``espeakup``.

Best practices
--------------

The best practices for text-to-speech, in terms of the ideal player experience for blind players, is to integrate directly with the screen-reader APIs (such as NVDA's API) to send output directly to it. This provides advanced functionality for blind players, such as being able to traverse previous output forwards and backwards, to replay, and to play at a faster or slower rate as suits them. Godot currently doesn't support screen-reader API integration.

With the current state of the Godot text-to-speech APIs, best practices include:

- Develop the game with text-to-speech enabled, and ensure that everything sounds correct
- Allow players to control which voice to use, and save/persist that selection across game sessions
- Allow players to control the speech rate, and save/persist that selection across game sessions

This provides your blind players with the most flexibility and comfort available when not using a screen reader, and minimizes the chance of frustrating and alienating them.

Caveats and Other Information
-----------------------------

- Expect delays when you call `tts_speak` and `tts_stop`. The actual delay time varies depending on both the OS and on your machine's specifications.
- Non-English text doesn't seem to be supported; even on Linux, with language-specific voices such as Arabic, the text reads out letter by letter.
- Non-ASCII characters, such as umlaut, are similarly not supported (e.g. ö reads as "o umlaut")
- Most blind players also use Windows with the NVDA screen reader.
- Windows text-to-speech APIs generally perform better than their equivalents on other systems (e.g. `tts_stop` followed by `tts_speak` immediately speaks the new message).
- Some systems, such as Linux, provide several voices, including voices with different accents and for different languages.
