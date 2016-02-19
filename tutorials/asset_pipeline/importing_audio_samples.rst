.. _doc_importing_audio_samples:

Importing audio samples
=======================

Why importing?
--------------

Importing Audio Samples into the game engine is a process that should be
easier than it really is. Most readers are probably thinking "Why not
just copying the .wav files to a folder inside the project and be over
with it?".

It's not usually that simple. Most game engines use uncompressed audio
(in memory at least) for sound effects. The reason for this is because
it's really cheap to play back and resample. Compressed streamed audio
(such as .ogg files) takes a large amount of processor to decode so no
more than one or two are streamed simultaneously. However, with sound
effects, one expects a dozen of them to be playing at the same time in
several situations.

Because of this, sound effects are loaded uncompressed into memory, and
here is where the problems begin.

As is usual with graphics, the situation where programmers don't really
know about audio and audio engineers don't know about programming is
also common in the industry. This leads to a scenario where a project
ends up wasting resources unnecessarily.

To be more precise, sfx artists tend to work with audio formats that
give them a lot of room for tweaking the audio with a low noise floor
minimum aliasing, such as 96khz, 24 bits. In many cases, they work in
stereo too. Added to that, many times they add effects with an infinite
or really long fadeout, such as reverb, which take a long time to fade
out. Finally, many DAWs also add silence at the beginning when
normalizing to wav.

This results in extremely large files to integrate more often than
desired, with sound effects taking dozens of megabytes.

How much does quality matter?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First of all, it is important to know that Godot has an internal reverb
generator. Sound effects can go to four different setups (small, medium
and large room as well as hall), with different send amounts. This saves
sfx artists the need to add reverb to the sound effects, reducing their
size greatly and ensuring correct trimming. Say no to SFX with baked
reverb!

.. image:: /img/reverb.png

Another common problem is that, while it's useful for working inside a
DAW, high dynamic range (24 bits) and high sampling rate (96khz) is
completely unnecessary for use in a game, as there is no `audible
difference <http://www.youtube.com/watch?v=cIQ9IXSUzuM>`__. If
positional sound is going to be used (for 2D and 3D), the panning and
stereo reverb will be provided by the engine, so there is little need
for stereo sound. How does this affect the resource usage? Look at the
following comparison:

+---------------------------+---------------------+--------------+
| Format                    | 1 Second of Audio   | Frame Size   |
+===========================+=====================+==============+
| 24 bits, 96 khz, Stereo   | 576kb               | 12           |
+---------------------------+---------------------+--------------+
| 16 bits, 44 khz, Mono     | 88kb                | 2            |
+---------------------------+---------------------+--------------+
| 16 bits, IMA-ADPCM        | 22kb                | 1/2          |
+---------------------------+---------------------+--------------+

As seen, for being no audible difference, the 16 bits, 44khz takes *6
times less memory* than the 24 bits, 96khz, Stereo version. The
IMA-ADPCM version takes *24 times less memory* than what was exported
from the DAW.

Trimming
~~~~~~~~

One last issue that happens often is that the waveform files received
have silences at the beginning and at the end. These are inserted by
DAWs when saving to a waveform, increase their size unnecessarily and
add latency to the moment they are played back. Trimming them solves
this, but it takes effort for the sfx artist, as they have to do it in a
separate application. In the worst case, they may not even know the
silences are being added.

.. image:: /img/trim.png

Importing audio samples
-----------------------

Godot has a simple screen for importing audio samples to the engine. SFX
artists only have to save the .wav files to a folder outside the
project, and the import dialog will fix the files for inclusion, as well
as doing it automatically every time they are modified and re-imported.

.. image:: /img/importaudio.png

In this screen, the quality of the audio can be limited to what is
needed, and trimming is done automatically. As a plus, several samples
can be loaded and batch-converted, just like textures.

Looping
~~~~~~~

Godot supports looping in the samples (Tools such as Sound Forge or
Audition can add loop points to .wav files). This is useful for sound
effects such as engines, machine guns, etc. Ping-pong looping is also
supported.

As an alternative, the import screen has a "loop" option that enables
looping for the entire sample when importing.
