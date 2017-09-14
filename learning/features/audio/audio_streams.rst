.. _doc_audio-streams:

Audio Streams
===========

Introduction
------------

As you might have read already in the :ref:`Audio Buses Tutorial<doc_audio-buses>`Audio Buses Tutorial,
sound is sent to each bus via an AudioStreamPlayer.

There are many types of AudioStreamPlayers which will be explained in detail. Each of it loads
an AudioStream and plays it back.

AudioStream
-----------

An audio stream is an abstract object that emits sound. It can come from many places, but most commonly
from the filesystem. Audio files such as .wav or .ogg can be loaded as AudioStreams and placed
inside an AudioStreamPlayer.

When using these kind of files, you should choose which one is best for your specific use case:

* Audio files of type *.wav* are considerably big, but use very little amount of your CPU to play. Hundreds of them can be played simultaneously with little impact to performance. This format is usually best for short sound effects, as the importer will trim them and convert them to IMA-ADPCM.
* Audio files of type *.ogg* are much smaller, but use considerably more amount of CPU power to play back, so only a few can be played back (specially on mobile!). This format is usually best for music or long sound effect sequences. It also works well for voice at relatively low bitrates.

Keep in mind both .wav and .ogg generally don't contain looping information, so this information must be set on the import options of each:

.. image:: /img/audio_stream_import.png

There are other types of AudioStreams, such as AudioStreamRandPitch, which takes an existing AudioStream and modulates the pitch every time it's played back randomly (great for some sound effects),
and more will keep appearing in the future.

AudioStreamPlayer
-----------------

This is the standard stream player, it can play to any given bus. In 5.1 sound, it can send to stereo mix or front speakers.

AudioStreamPlayer2D
-------------------

This is a variant of AudioStreamPlayer but emits sound in a 2D positional environment. When close to the left of the screen, the panning will go left. When close to the right side, it will go right.

While it's possible to send these effects to specific audio buses, one of the best strategies is to use an Area2D to divert sound to a specific bus. This allows to create buses with different
reverb or sound qualities and make the emitter will automatically send to them when entering the Area2D shapes.

.. image:: /img/audio_stream_2d_area.png

AudioStreamPlayer3D
-------------------

This is a variant of AudioStreamPlayer but emits sound in a 3D positional environment. Depending on the location of the player relative of the screen, it can position sound in Stereo, 5.1 or 7.1 depending
on the chosen audio setup.

Similar to AudioStreamPlayer2D, an Area can divert the sound to an audio bus.

.. image:: /img/audio_stream_3d_area.png

Unlike for 2D, the 3D version of AudioStreamPlayer has a few more advanced options:

Reverb Buses
~~~~~~~~~~~~

Godot allows 3D Audio Streams that enter a specific *Area* to send dry and wet audio to separate buses. This is really useful when you have several reverb configurations for different types of rooms.
This is done by enabling this type of reverb in the *Reverb Bus* section of *Area* properties:

.. image:: /img/audio_stream_reverb_bus.png

At the same time, a special buys layout is created where each area receives the reverb info from each area. Of course, an actual Reverb effect must be created in that bus for anything to happen:

.. image:: /img/audio_stream_reverb_bus2.png

The Area Reverb Bus section has also a specific parameter named "Uniformity". Some types of rooms bounce sounds more than others (like for example, a typical warehouse), so reverberation can be heard 
almost uniformly across the room even though the source is far away. Playing around with this parameter can simulate that effect.

Doppler
~~~~~~~

When the relative velocity between an emitter and listener changes, this is perceived as an increase or decrease of the pitch shift. Godot can track changes in velocities of *AudioStreamPlayer3D* or *Camera*.
Both have this property, which must be enabled manually:

.. image:: /img/audio_stream_doppler.png

Simply enable it by setting it depending on how objects will be moved (whether on regular *process* or *fixed_process* step) and the tracking will happen automatically!















Begining Godot 3.0, the audio engine has been rewritten from scratch.
The aim now is to present an interface much friendlier to sound design
professionals. To achieve this, the audio engine contains a virtual rack
where unlimited audio buses can be created and, on each of it, unlimited
amount of effect processors can be added (or more like, as long as your
GPU holds up!)

The implementation in Godot is pretty efficient and has been written
entirely from the ground up, without relying on any existing audio libraries.

Even the effect processors were written exclusively for Godot (save for
the pitch shifting library), with games in mind. This allows
a very efficient tradeoff between performance and sound quality.

Decibel Scale
-------------

The new audio engine works primarily using the decibel scale. We have
chosen this over linear representation of amplitude because it's
more intuitive for audio professionals.

For those unfamiliar with it, it can be explained with a few facts:

* Decibel scale is a relative scale, every 6dB (dB means decibel), sound doubles or halves.
* The scale is logarithmic, so true zero (no audio) can't be represented.
* 0dB is considered the maximum audible volume without *clipping*. This limit is not the human limit but a limit from the sound hardware. Your sound output simply can't output any sound louder than 0dB without distorting it (clipping it).
* Because of the above, your sound mix should work in a way where the sound output of the *Master Bus* (more on that later), should never be above 0dB.
* Every 6dB below the 0dB limit, sound energy is *halved*. It means the sound volume at -6dB is half as loud as 0dB. -12dB is half as loud as -6dB and so on.
* When working with decibels, sound is considered no longer audible between -60dB and -80dB. This makes your working range generally between -60dB and 0dB.

This can take a bit getting used to, but it's friendlier in the end and will allow you to communicate better with audio professionals.

Audio Buses
------------

Audio buses can be found in the bottom panel of Godot Editor:

.. image:: /img/audio_buses1.png

An *Audio Bus* bus (often called "Audio Channels" too) is a device where audio is channeled. Audio data passes through it and can be *modified* and *re-routed*. A VU-Meter (the bars that go up and down when sound is played) can measure the loudness of the sound in Decibel scale.
rythm of sound)
The leftmost bus is the *Master Bus*. This bus outputs the mix to your speakers so, as mentioned in the item above (Decibel Scale), make sure that your mix rarely or never goes above 0dB in this bus. 
The rest of the audio buses are used for *routing*. This means that, after modifying the sound, they must send it to another bus to the left. Routing is always from right to left without exception as this
avoids creating infinite routing loops!

.. image:: /img/audio_buses2.png

In the above image, *Bus 2* is routing it's output to *Master* bus. 

Playbck of Audio to a Bus
--------------------------

To test playback to a bus, create an AudioStreamPlayer node, load an AudioStream and select a target bus for playback:

.. image:: /img/audio_buses3.png

Finally toggle the "playing" property to on and sound will flow.

To learn more about *Audio Streams*, please read the related tutorial later! (@TODO link to audio streams tute)

Adding Effects
--------------

Audio buses can contain all sorts of effects. These effects modify the sound in one way or another and are applied in order.

.. image:: /img/audio_buses4.png

Follownig is a short description of available effects:

Amplify
~~~~~~~

It's the most basic effect, it changes the sound volume. Amplifying too much can make the sound clip, so be wary of that.

BandLimit and BandPass
~~~~~~~~~~~~~~~~~~~~~~

These are resonant filters which block frequencies around the *Cutoff* point. BandPass is resonant, while BandLimit stretches to the sides.

Chorus
~~~~~~

This effect adds extra voices, detuned by LFO and with a small delay, to add more richness to the sound harmonics and stereo width.

Compressor
~~~~~~~~~~

The aim of a dynamic range compressor is to reduce the level of the sound when the amplitude goes over a certain threshold in Decibels.
One of the main uses of a compressor is to increase the dynamic range while clipping the least possible (when sound goes over 0dB).

Compressor has may uses in the mix, for example:
* It can be used in the Master bus to compress the whole output (Although a Limiter is probably better)
* It can be used in voice channels to ensure they sound as even as possible.
* It can be *Sidechained*. This means, it can reduce the sound level using another audio bus for threshold detection. This technique is
very common in video game mixing to download the level of Music/SFX while voices are being heard.
* It can accentuate transients by using a bit wider attack, meaning it can make sound effects sound more punchy.

There is a lot of bibliography written about compressors, and Godot implementation is rather standard.

Delay
~~~~~

Adds an "Echo" effect with a feedback loop. It can be used, together with Reverb, to simulate very wide rooms, canyons, etc. where sound bounces are far apart.

Distortion
~~~~~~~~~~

Adds classical effects to modify the sound and make it dirty. Godot supports effects like overdrive, tan, or bit crushing.
For games, it can simulate sound coming from some saturated device or speaker very efficiently.

EQ6, EQ10, EQ21
~~~~~~~~~~~~~~~

Godot provides three model of equalizers with different band counts. Equalizers are very useful on the Master Bus to completely master a mix and give it character. They are
also very useful when a game is run on a mobile device, to adjust the mix to that kind of speakers (it can be added but disabled when headphones are plugged).

HighPassFilter, HighShelfFilter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These are filters that cut frequencies below a specific *Cutoff*. A common use of high pass filters is to add it to effects (or voice) that were recorded too close too a mic and need
to sound more realistic. It is commonly used for some types of environment like space.

Limiter
~~~~~~~

A limiter is similar to a compressor, but it's less flexible and designed to disallow sound going over a given dB threshold. Adding one in the *Master Bus* is always recommended
to reduce the effects of clipping.

LowPassFilter, LowShelfFilter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These are the most common filters, they cut frequencies above a specific *Cutoff* and can also resonate. They can be used for a wide amount of effects, from underwater sound to simulating
a sound coming from far away.

NotchFilter
~~~~~~~~~~~

The opposite to the BandPassFilter, it removes a band of sound from the frequency spectrum at a given *Cutoff*.

Panner
~~~~~~

This is a simple helper to pan sound left or right.

Phaser
~~~~~~

It probably does not make much sense to explain that this effect is formed by two signals being dephased and cancelling each other out.
It will be sufficient to note that you can make a Darth Vader voice with it, or jet-like sounds.

PitchShift
~~~~~~~~~~

This effect allows modulating pitch separatedly from tempo. All frequencies can go and up and down with transients kept as bet as possible. It's amazing for making funny voices!

Reverb
~~~~~~

Reverb simulates rooms of different sizes. It has adjustable parameters that can be tweaked to obtain the sound of a specific room. Reverb is commonly outputed from Areas (@TODO LINK TO TUTORIAL WHEN DONE), or
to apply chamber feel to all sounds.

StereoEnhance
~~~~~~~~~~~~~

This effect has a few algorithms available to enhance the stereo spectrum, in case this is needed.

Automatic Bus Disabling
-----------------------

There is no need to disable buses manually when not in use, Godot detects that the bus has been silent for a few seconds and disable it (including all effects).

.. image:: /img/audio_buses5.png

Bus Rearrangement
-----------------

Stream Players use bus names to identify a bus, which allows adding, removing and moving buses around while the reference to them is kept.
If a bus is renamed, however, the reference will be lost and the Stream Player will output to Master. This system was chosen because rearranging buses is a more common process than renaming them.

Default Bus Layout
-------------------

The default bus layout is automatically saved to the "res://default_bus_layout.res" file. Other bus layouts can be saved/retrieved from files in case of having
to change snapshots, but in most cases this is not necessary.

