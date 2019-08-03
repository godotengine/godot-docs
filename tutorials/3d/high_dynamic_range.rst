.. _doc_high_dynamic_range:

High dynamic range
==================

Introduction
------------

Normally, an artist does all the 3D modelling, then all the texturing,
looks at their awesome looking model in the 3D DCC and says "looks
fantastic, ready for integration!" then goes into the game, lighting is
setup and the game runs.

So at what point does all this HDR business come into play? The idea is that
instead of doing a simple 1:1 mapping of scene intensities that range from some incredibly low
value to some incredibly large value to a display, a more complex transform happens. In any given game scene, ideas around
what is “white” or “black” do not exist. It’s up to a virtual camera to determine
what code values are mapped where!

To be more practical, imagine that in a regular scene, the intensity
of a light is set to 5.0. The whole scene will turn
very bright and look horrible if a simple or inappropriate camera rendering
transform is used. 

In a game engine or other physically plausible rendering engine, the scene values,
also known more appropriately as *scene referred* values, require mapping of their
intensities to the display. This last operation is sometimes oversimplified and called
tone-mapping, which doesn’t do justice to the full degree of manipulations a camera
rendering transform might apply to scene referred values.

.. image:: img/hdr_tonemap.png

In a game, a character may move through varying intensities of
illumination.

.. image:: img/hdr_cave.png

Additionally, it is possible to set a threshold value to send to the
glow buffer depending on the pixel luminance. This allows for more
realistic light bleeding effects in the scene.

Linear Transfer Characteristic
------------------

Computer monitors expect a
transfer function encoded set of values to compress the data. Artists
create their art on the screen too, so their art will typically have
had a series of nonlinear transfer functions applied
to their work.

sRGB is a common encoding for imagery. Many pieces of visual content that people have on their computers
or download from the internet such as photos or graphic design work
is encoded in accordance with this specification.

Sometimes the sRGB transfer function is oversimplified to a simple
power function in some software and even some inexpensive lower
quality displays. The nonlinearly encoded imagery is passed to the
sRGB display in this case, and the display “undoes” this transfer
characteristic to output linear light ratios.

.. image:: img/hdr_gamma.png

The mathematics of a scene referred model require that we multiply the scene by different
values to adjust the intensities and exposure to different light ranges.
The transfer function of the display cannot appropriately render
the wide dynamic range of the scene using a simple power function,
and therefore a more complex nonlinear approach is required.

Scene Linear & Asset Pipelines
------------------------------

Working in scene linear sRGB is not just pressing a switch. First, imported image
assets must be converted to linear light ratios on import. There are two ways
to do this:

sRGB Transfer Function to Display Linear on Image Import
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is the easiest, but not ideal, method of using sRGB assets. One issue with this
is loss of quality. Using 8
bits per channel to represent linear light ratios is not sufficient but
depth to quantise the values correctly. These textures might later be compressed
too, which exacerbates the problem worse.

In any case, though, this is the easiest solution.

Hardware sRGB Transfer Function to Display Linear Conversion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The GPU will do the conversion after reading the
texel using floating point. This works fine on PC and consoles, but most
mobile devices do no support it, or do not support it on compressed
texture format (iOS for example).

Scene Linear to Display Referred Nonlinear
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After all the rendering is done, the scene linear render requires transforming
to a suitable output such as an sRGB display. To do this, enable sRGB conversion in the
current :ref:`Environment <class_Environment>` (more on that below).

Keep in mind that sRGB -> Display Linear and Display Linear -> sRGB conversions
must always be **both** enabled. Failing to enable one of them will
result in horrible visuals suitable only for avant-garde experimental
indie games.

Parameters of HDR
-----------------

HDR setting can be found in the :ref:`Environment <class_Environment>`
resource. These are found most of the time inside a
:ref:`WorldEnvironment <class_WorldEnvironment>`
node or set in a camera. For more information see
:ref:`doc_environment_and_post_processing`.
