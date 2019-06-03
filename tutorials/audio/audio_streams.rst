.. _doc_audio-streams:

Audio streams
=============

Introduction
------------

As you might have already read in the :ref:`Audio Buses Tutorial<doc_audio-buses>`,
sound is sent to each bus via an AudioStreamPlayer.

There are different kinds of AudioStreamPlayer. Each one loads
an AudioStream and plays it back.

AudioStream
-----------

An audio stream is an abstract object that emits sound. The sound can come from many places, but most commonly
from the filesystem. Audio files, such as .wav or .ogg, can be loaded as AudioStreams and placed
inside an AudioStreamPlayer.

Here is a comparison of the two types of file to help you choose the one that fits your use case best:

* Audio files of type *.wav* are quite large, but use little CPU power to play back. Hundreds of them can be played simultaneously with little impact to performance. This format is usually best for short sound effects.
* Audio files of type *.ogg* are much smaller, but use considerably more CPU power to play back, so only a few can be played back (especially on mobile!). This format works well for music, long sound effect sequences, and voice at relatively low bitrates.

Keep in mind neither .wav nor .ogg usually contains looping information. If looping is desired it must be set up using the import options of each file type:

.. image:: img/audio_stream_import.png

There are other types of AudioStreamPlayer, such as AudioStreamRandomPitch. This one makes a random adjustment to the sound's pitch every time it's played back. This can be helpful for adding interest to sounds that are played back often.

AudioStreamPlayer
-----------------

This is the standard stream player; it can play to any bus. In 5.1 sound, it can send to stereo mix or front speakers.

AudioStreamPlayer2D
-------------------

This is a variant of AudioStreamPlayer, but emits sound in a 2D positional environment. When close to the left of the screen, the panning will go left. When close to the right side, it will go right.

.. note:: Area2Ds can be used to divert sound from any AudioStreamPlayer2Ds they contain to specific buses. This makes it possible to create buses with different reverb or sound qualities to handle action happening in a particular parts of your game world.

.. image:: img/audio_stream_2d_area.png

AudioStreamPlayer3D
-------------------

This is a variant of AudioStreamPlayer, but emits sound in a 3D positional environment. Depending on the location of the player relative to the screen, it can position sound in Stereo, 5.1 or 7.1 depending
on the chosen audio setup.

Similar to AudioStreamPlayer2D, an Area can divert the sound to an audio bus.

.. image:: img/audio_stream_3d_area.png

Unlike for 2D, the 3D version of AudioStreamPlayer has a few more advanced options:

Reverb buses
~~~~~~~~~~~~

Godot allows 3D Audio Streams that enter a specific *Area* to send dry and wet audio to separate buses. This is useful when you have several reverb configurations for different types of rooms.
This is done by enabling this type of reverb in the *Reverb Bus* section of *Area* properties:

.. image:: img/audio_stream_reverb_bus.png

At the same time, a special bus layout is created where each area receives the reverb info from each area. A Reverb effect needs to be created and configured in each reverb bus to complete the setup for the desired effect:

.. image:: img/audio_stream_reverb_bus2.png

The Area Reverb Bus section also has a parameter named "Uniformity". Some types of rooms bounce sounds more than others (like a warehouse), so reverberation can be heard
almost uniformly across the room even though the source may be far away. Playing around with this parameter can simulate that effect.

Doppler
~~~~~~~

When the relative velocity between an emitter and listener changes, this is perceived as an increase or decrease in the pitch of the emitted sound. Godot can track changes in velocities of *AudioStreamPlayer3D* or *Camera*.
Both have this property, which must be enabled manually:

.. image:: img/audio_stream_doppler.png

Enable it by setting it depending on how objects will be moved (whether on regular *process* or *physics_process* step) and the tracking will happen automatically.
