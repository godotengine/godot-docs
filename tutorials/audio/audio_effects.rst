:article_outdated: True

.. _doc_audio_effects:

Audio effects
=============

Godot includes several audio effects that can be added to an audio bus to
alter every sound file that goes through that bus.

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

Capture
~~~~~~~

The Capture effect copies the audio frames of the audio bus that it is on into
an internal buffer. This can be used to capture data from the microphone
or to transmit audio over the network in real-time.

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

Makes the sound distorted. Godot offers several types of distortion: *overdrive*,
*tan* and *bit crushing*. Distortion can be used to simulate sound coming through
a low-quality speaker or device.

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

HighPassFilter
~~~~~~~~~~~~~~

Cuts frequencies below a specific *Cutoff* frequency.
HighPassFilter is used to reduce the bass content of a
signal.

HighShelfFilter
~~~~~~~~~~~~~~~

Reduces all frequencies above a specific *Cutoff* frequency.

.. _doc_audio_buses_limiter:

Limiter
~~~~~~~

A limiter is similar to a compressor, but it's less flexible and designed to
prevent a signal's amplitude exceeding a given dB threshold. Adding a limiter to
the Master bus is a safeguard against clipping.

LowPassFilter
~~~~~~~~~~~~~

Cuts frequencies above a specific *Cutoff* frequency and can also resonate
(boost frequencies close to the *Cutoff* frequency). Low pass filters can be
used to simulate "muffled" sound. For instance, underwater sounds, sounds
blocked by walls, or distant sounds.

LowShelfFilter
~~~~~~~~~~~~~~

Reduces all frequencies below a specific *Cutoff* frequency.

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

The Record effect allows the user to record sound from a microphone.

Reverb
~~~~~~

Reverb simulates rooms of different sizes. It has adjustable parameters that can
be tweaked to obtain the sound of a specific room. Reverb is commonly outputted
from :ref:`Area3Ds <class_Area3D>`
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
