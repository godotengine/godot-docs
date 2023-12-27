.. _doc_internal_audio_architecture:

Internal audio architecture
===========================

This page is a high-level overview of Godot 4's internal audio design.
It does not apply to previous Godot versions.

The goal of this page is to document design decisions taken to best suit
:ref:`Godot's design philosophy <doc_best_practices_for_engine_contributors>`,
while providing a starting point for new audio contributors.

The second starting point is the `Audio Issue Tracker <https://github.com/godotengine/godot/issues/76797>`__.

If you have questions about audio internals not answered here, feel free to
ask in the ``#audio`` channel of the
`Godot Contributors Chat <https://chat.godotengine.org/channel/audio>`__.

.. note::

    If you have difficulty understanding concepts on this page,
    it is recommended to go through an audio blog such as
    `Audio Sample Rate and Bit Depth <https://www.izotope.com/en/learn/digital-audio-basics-sample-rate-and-bit-depth.html>`__,
    `How Sound Works <https://audiouniversityonline.com/audio-basics-how-sound-works/>`__, and
    `An Introduction to Audio Electronics <https://www.allaboutcircuits.com/technical-articles/introduction-audio-electronics-sound-microphones-speakers-amplifiers>`__.


.. _doc_internal_audio_architecture_drivers:

Audio drivers
-------------

Supported
- Dummy (no audio output/input, used for headless mode)
- Linux/\*BSD

   - ALSA
   - PulseAudio
   - ALSA MIDI

- Windows + UWP

   - WASAPI
   - XAudio2 (`is broken and not compiled by default <https://github.com/godotengine/godot/issues/75109#issuecomment-1724273758>`__, and `may be removed in the future <https://github.com/godotengine/godot-docs/pull/7896#discussion_r1387906566>`__)
   - Win MIDI

- macOS + iOS

   - CoreAudio
   - Core MIDI

- Android

   - OpenSL ES


.. _doc_internal_audio_architecture_codecs:


Audio Codecs
------------


OGG Vorbis
^^^^^^^^^^

.. note::

    This is an audio format that takes more processing power than WAV to play back,
    but is smaller in file size than WAV and MP3. It's most suitable for
    playing background music.


**Why not vorbisfile?**
// TODO


WAV
^^^

.. note::

    This is an audio format that requires the least processing power to play back,
    but is larger in file size than Ogg Vorbis and MP3. It's most suitable for
    playing short sound effects.


MP3
^^^


.. _doc_internal_audio_architecture_servers:

AudioServer
-----------

Decoding
^^^^^^^^

Buffers
^^^^^^^

Kinds of buffers
- main buffer: is hardcoded to `512`

   - But the driver buffer size calculation is unique to each driver and depends on varying factors, such as:

      - but depends in general on: audio output latency, mix rate, channel count (which depends on the speaker count)

- lookahead buffer: We store the next few samples so we have some time to fade audio out if it ends abruptly at the beginning of the next mix.
- mix buffer: sum of main buffer and the lookahead buffer


The actual audio frames are written into the channels, which are split into left and right stereo pairs (i.e. physical speakers).


Mixing
^^^^^^

**Playback**
- Pausing triggers a fade out.
- Stopping a playing stream triggers a fade out as well and frees the associated memory.


**Fading**
- A fade is achieved by lerping the audio volume over multiple frames.


**Channels**
The channel count depends on the amount of speakers:
- stereo: 1

   - front-left speaker
   - front-right speaker

- surround 3.1: 2

   - above speakers, plus:
   - center speaker
   - subwoofer / LFE(low-frequency effects) is always at full volume

- surround 5.1: 3

   - above speakers, plus:
   - rear-left speaker
   - rear-right speaker

- surround 7.1: 4

   - above speakers, plus:
   - side-left speaker
   - side-right speaker

But those are not the total channels, as each has a left and right side (i.e. left and right speaker).
The total channels are twice the size mentioned above and equals the number of speakers.
Depending on the context, one or the other size logic is used.

The speaker mode is sometimes driver-dependent. All drivers lookup the mode by using the total number of channels.
Except ALSA, XAudio2, and OpenSL ES. These enforce stereo speaker mode and support only 2 total channels.


**Bus**
Godot as an internal bus logic to separately control volume and audio effects applied to audio streams.
All busses eventually feed into the master bus, which is output to the audio output device.


Seeking / Looping
^^^^^^^^^^^^^^^^^


SpatialSoundServer
^^^^^^^^^^^^^^^^^^


SpatialSound2DServer
^^^^^^^^^^^^^^^^^^^^


.. _doc_internal_audio_architecture_classes:

Core audio classes architecture
-------------------------------


.. _doc_internal_audio_architecture_2d_vs_3d:


2D and 3D audio separation
--------------------------


.. _doc_internal_audio_architecture_techniques:


2D audio techniques
-------------------


3D audio techniques
-------------------

SPCAP, Camera3D doppler tracking and the audio panning properties here


.. _doc_internal_audio_architecture_nodes:

Nodes
-----

AudioStreamPlayer
^^^^^^^^^^^^^^^^^


AudioStreamPolyphonic
^^^^^^^^^^^^^^^^^^^^^


.. _doc_internal_audio_architecture_other:

Other
-----

Notes
- recording
- input devices


Output devices
^^^^^^^^^^^^^^

Currently, Godot only allows one output device that can be set globally in the :ref:`AudioServer<class_AudioServer_property_output_device>`.

.. warning::

    Devices connected via bluetooth degrade audio quality
    and can cause audio pops which cannot be fixed in Godot.

    Furthermore, wireless headsets may enter a "snooze" state
    when no audio input is received.
    Once they receive audio input again, the device wakes up
    and may cause audio pops.
