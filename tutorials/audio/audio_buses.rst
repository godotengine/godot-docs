.. _doc_audio_buses:

Audio buses
===========

Introduction
------------

Godot's audio processing code has been written with games in mind, with the aim
of achieving an optimal balance between performance and sound quality.

Godot's audio engine allows any number of audio buses to be created and any
number of effect processors can be added to each bus. Only the hardware of the
device running your game will limit the number of buses and effects that can be
used before performance starts to suffer.

Decibel scale
-------------

Godot's sound interface is designed to meet the expectations of sound design
professionals. To this end, it primarily uses the decibel scale.

For those unfamiliar with it, it can be explained with a few facts:

- The decibel (dB) scale is a relative scale. It represents the ratio of
  sound power by using 20 times the base 10 logarithm of the ratio
  (20 × log\ :sub:`10`\ (P/P\ :sub:`0`\ )).
- For every 6 dB, sound amplitude doubles or halves. 12 dB represents a factor
  of 4, 18 dB a factor of 8, 20 dB a factor of 10, 40 dB a factor of 100, etc.
- Since the scale is logarithmic, true zero (no audio) can't be represented.
- 0 dB is the maximum amplitude possible in a digital audio system.
  This limit is not the human limit, but a limit from the sound hardware.
  Audio with amplitudes that are too high to be represented properly below 0 dB
  create a kind of distortion called *clipping*.
- To avoid clipping, your sound mix be arranged so that the output of the
  *master bus* (more on that later) never exceeds 0 dB.
- Every 6 dB below the 0 dB limit, sound energy is *halved*.
  It means the sound volume at -6 dB is half as loud as 0dB.
  -12 dB is half as loud as -6 dB and so on.
- When working with decibels, sound is considered no longer audible
  between -60 dB and -80 dB. This makes your working range generally
  between -60 dB and 0 dB.

This can take a bit getting used to, but it's friendlier in the end
and will allow you to communicate better with audio professionals.

Audio buses
-----------

Audio buses can be found in the bottom panel of the Godot editor:

.. image:: img/audio_buses1.png

An *audio bus* (also called an *audio channel*) can be considered a place that
audio is channeled through on the way to playback through a device's speakers.
Audio data can be *modified* and *re-routed* by an audio bus. An audio bus
has a VU meter (the bars that light up when sound is played) which indicates the
amplitude of the signal passing through.

The leftmost bus is the *master bus*. This bus outputs the mix to your speakers
so, as mentioned in the *Decibel scale* section above, make sure that your mix
level doesn't reach 0 dB in this bus. The rest of the audio buses can be
flexibly routed. After modifying the sound, they send it to another bus to
the left. The destination bus can be specified for each of the non-master audio
buses. Routing always passes audio from buses on the right to buses further
to the left. This avoids infinite routing loops.

.. image:: img/audio_buses2.png

In the above image, the output of *Bus 2* has been routed to the *Master* bus.

Playback of audio through a bus
-------------------------------

To test passing audio to a bus, create an AudioStreamPlayer node, load an
AudioStream and select a target bus for playback:

.. image:: img/audio_buses3.png

Finally, toggle the **Playing** property to **On** and sound will flow.

.. seealso::

    You may also be interested in reading about :ref:`doc_audio_streams` now.

Adding effects
--------------

Audio buses can contain all sorts of effects. These effects modify the sound in
one way or another and are applied in order.

.. image:: img/audio_buses4.png

Try them all out to get a sense of how they alter sound. Here follows a short
description of the available effects:

Amplify
~~~~~~~

Amplify changes the amplitude of the signal. Some care needs to be taken.
Setting the level too high can make the sound clip, which is usually
undesirable.

BandLimit and BandPass
~~~~~~~~~~~~~~~~~~~~~~

These are resonant filters which block frequencies around the *Cutoff* point.
BandPass can be used to simulate sound passing through an old telephone line or
megaphone. Modulating the BandPass frequency can simulate the sound of a wah-wah
guitar pedal, think of the guitar in Jimi Hendrix's *Voodoo Child (Slight
Return)*.

Chorus
~~~~~~

The Chorus effect duplicates the incoming audio, delays the duplicate slightly
and uses an LFO to continuously modulate the pitch of the duplicated signal
before mixing the duplicated signal(s) and the original together again. This
creates a shimmering effect and adds stereo width to the sound.

Compressor
~~~~~~~~~~

A dynamic range compressor automatically attenuates the level of the incoming
signal when its amplitude exceeds a certain threshold. The level of attenuation
applied is proportional to how far the incoming audio exceeds the threshold.
The compressor's Ratio parameter controls the degree of attenuation.
One of the main uses of a compressor is to reduce the dynamic range of signals
with very loud and quiet parts. Reducing the dynamic range of a signal
can make it easier to mix.

The compressor has many uses. For example:

- It can be used in the Master bus to compress the whole output.
- It can be used in voice channels to ensure they sound as even as possible.
- It can be *sidechained*. This means it can reduce the sound level
  of one signal using the level of another audio bus for threshold detection.
  This technique is very common in video game mixing to "duck" the level of
  music or sound effects when voices need to be heard.
- It can accentuate transients by using a slower attack.
  This can make sound effects more punchy.

.. note::

    If your goal is to prevent a signal from exceeding a given amplitude
    altogether, rather than to reduce the dynamic range of the signal,
    a :ref:`limiter <doc_audio_buses_limiter>` is likely a better choice
    than a compressor.


Delay
~~~~~

Adds an "echo" effect with a feedback loop. It can be used together
with *Reverb* to simulate wide rooms, canyons, etc. where sound bounces
are far apart.

Distortion
~~~~~~~~~~

Distortion effects make the sound "dirty". Godot offers several types of
distortion: *overdrive*, *tan* and *bit crushing*. Distortion can be used
to simulate sound coming through a low-quality speaker or device.

EQ
~~

EQ is what all other equalizers inherit from. It can be extended with with Custom
scripts to create an equalizer with a custom number of bands.

EQ6, EQ10, EQ21
~~~~~~~~~~~~~~~

Godot provides three equalizers with different numbers of bands. An equalizer on
the Master bus can be useful to cut frequencies that the device's speakers can't
reproduce well (e.g. a mobile phone's speakers won't reproduce bass content
well). The equalizer effect can be disabled when headphones are plugged in.

Filter
~~~~~~

Filter is what all other filters inherit from and should not be used directly.

HighPassFilter, HighShelfFilter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These are filters that cut frequencies below a specific *Cutoff* frequency.
HighPassFilter and HighShelfFilter are used to reduce the bass content of a
signal.

.. _doc_audio_buses_limiter:

Limiter
~~~~~~~

A limiter is similar to a compressor, but it's less flexible and designed to
prevent a signal's amplitude exceeding a given dB threshold. Adding a limiter to
the Master bus is a safeguard against clipping.

LowPassFilter, LowShelfFilter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These are the most common filters, they cut frequencies above a specific
*Cutoff* frequency and can also resonate (boost frequencies close to the
*Cutoff* frequency). Low pass filters can be used to simulate "muffled" sound.
For instance, underwater sounds, sounds blocked by walls, or distant sounds.

NotchFilter
~~~~~~~~~~~

The opposite of the BandPassFilter, it removes a band of sound from the
frequency spectrum at a given *Cutoff* frequency.

Panner
~~~~~~

The Panner allows the stereo balance of a signal to be adjusted between
the left and right channels (wear headphones to audition this effect).

Phaser
~~~~~~

It probably does not make much sense to explain that this effect is formed by
two signals being dephased and cancelling each other out. You can make a Darth
Vader voice with it, or jet-like sounds.

PitchShift
~~~~~~~~~~

This effect allows the adjustment of the signal's pitch independently of its
speed. All frequencies can be increased/decreased with minimal effect on
transients. PitchShift can be useful to create unusually high or deep voices.

Record
~~~~~~

The Record effect allows audio passing through the bus to be written to a file.

Reverb
~~~~~~

Reverb simulates rooms of different sizes. It has adjustable parameters that can
be tweaked to obtain the sound of a specific room. Reverb is commonly outputted
from :ref:`Areas <class_Area>`
(see :ref:`Reverb buses <doc_audio_streams_reverb_buses>`), or to apply
a "chamber" feel to all sounds.

SpectrumAnalyzer
~~~~~~~~~~~~~~~~

This effect doesn't alter audio, instead, you add this effect to buses you want
a spectrum analysis of. This would typically be used for audio visualization. A
demo project using this can be found `here <https://github.com/godotengine/godot-demo-projects/tree/master/audio/spectrum>`__.

StereoEnhance
~~~~~~~~~~~~~

This effect uses a few algorithms to enhance a signal's stereo spectrum.

Automatic bus disabling
-----------------------

There is no need to disable buses manually when not in use. Godot detects
that the bus has been silent for a few seconds and disables it (including
all effects).

.. figure:: img/audio_buses5.png

   Disabled buses have a blue VU meter instead of a red-green one.

Bus rearrangement
-----------------

Stream Players use bus names to identify a bus, which allows adding, removing
and moving buses around while the reference to them is kept. However, if a bus
is renamed, the reference will be lost and the Stream Player will output
to Master. This system was chosen because rearranging buses is a more common
process than renaming them.

Default bus layout
------------------

The default bus layout is automatically saved to the
``res://default_bus_layout.tres`` file. Custom bus arrangements can be saved
and loaded from disk.
