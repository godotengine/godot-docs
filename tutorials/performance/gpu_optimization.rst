.. _doc_gpu_optimization:

GPU optimization
================

Introduction
------------

The demand for new graphics features and progress almost guarantees that you
will encounter graphics bottlenecks. Some of these can be on the CPU side, for
instance in calculations inside the Godot engine to prepare objects for
rendering. Bottlenecks can also occur on the CPU in the graphics driver, which
sorts instructions to pass to the GPU, and in the transfer of these
instructions. And finally, bottlenecks also occur on the GPU itself.

Where bottlenecks occur in rendering is highly hardware-specific.
Mobile GPUs in particular may struggle with scenes that run easily on desktop.

Understanding and investigating GPU bottlenecks is slightly different to the
situation on the CPU. This is because, often, you can only change performance
indirectly by changing the instructions you give to the GPU. Also, it may be
more difficult to take measurements. In many cases, the only way of measuring
performance is by examining changes in the time spent rendering each frame.

Draw calls, state changes, and APIs
-----------------------------------

.. note:: The following section is not relevant to end-users, but is useful to
          provide background information that is relevant in later sections.

Godot sends instructions to the GPU via a graphics API (Vulkan, OpenGL, OpenGL
ES or WebGL). The communication and driver activity involved can be quite
costly, especially in OpenGL, OpenGL ES and WebGL. If we can provide these
instructions in a way that is preferred by the driver and GPU, we can greatly
increase performance.

Nearly every API command in OpenGL requires a certain amount of validation to
make sure the GPU is in the correct state. Even seemingly simple commands can
lead to a flurry of behind-the-scenes housekeeping. Therefore, the goal is to
reduce these instructions to a bare minimum and group together similar objects
as much as possible so they can be rendered together, or with the minimum number
of these expensive state changes.

2D batching
~~~~~~~~~~~

In 2D, the costs of treating each item individually can be prohibitively high -
there can easily be thousands of them on the screen. This is why 2D *batching*
is used. Multiple similar items are grouped
together and rendered in a batch, via a single draw call, rather than making a
separate draw call for each item. In addition, this means state changes,
material and texture changes can be kept to a minimum.

3D batching
~~~~~~~~~~~

In 3D, we still aim to minimize draw calls and state changes. However, it can be
more difficult to batch together several objects into a single draw call. 3D
meshes tend to comprise hundreds or thousands of triangles, and combining large
meshes in real-time is prohibitively expensive. The costs of joining them quickly
exceeds any benefits as the number of triangles grows per mesh. A much better
alternative is to **join meshes ahead of time** (static meshes in relation to each
other). This can be done by artists, or programmatically within Godot using an add-on.

There is also a cost to batching together objects in 3D. Several objects
rendered as one cannot be individually culled. An entire city that is off-screen
will still be rendered if it is joined to a single blade of grass that is on
screen. Thus, you should always take objects' locations and culling into account
when attempting to batch 3D objects together. Despite this, the benefits of
joining static objects often outweigh other considerations, especially for large
numbers of distant or low-poly objects.

For more information on 3D specific optimizations, see
:ref:`doc_optimizing_3d_performance`.

Reuse shaders and materials
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Godot renderer is a little different to what is out there. It's designed to
minimize GPU state changes as much as possible. :ref:`StandardMaterial3D
<class_StandardMaterial3D>` does a good job at reusing materials that need similar
shaders. If custom shaders are used, make sure to reuse them as much as
possible. Godot's priorities are:

-  **Reusing Materials:** The fewer different materials in the
   scene, the faster the rendering will be. If a scene has a huge amount
   of objects (in the hundreds or thousands), try reusing the materials.
   In the worst case, use atlases to decrease the amount of texture changes.
-  **Reusing Shaders:** If materials can't be reused, at least try to reuse
   shaders. Note: shaders are automatically reused between
   StandardMaterial3Ds that share the same configuration (features
   that are enabled or disabled with a check box) even if they have different
   parameters.

If a scene has, for example, 20,000 objects with 20,000 different
materials each, rendering will be slow. If the same scene has 20,000
objects, but only uses 100 materials, rendering will be much faster.

Pixel cost versus vertex cost
-----------------------------

You may have heard that the lower the number of polygons in a model, the faster
it will be rendered. This is *really* relative and depends on many factors.

On a modern PC and console, vertex cost is low. GPUs originally only rendered
triangles. This meant that every frame:

1. All vertices had to be transformed by the CPU (including clipping).
2. All vertices had to be sent to the GPU memory from the main RAM.

Nowadays, all this is handled inside the GPU, greatly increasing performance. 3D
artists usually have the wrong feeling about polycount performance because 3D
modeling software (such as Blender, 3ds Max, etc.) need to keep geometry in CPU
memory for it to be edited, reducing actual performance. Game engines rely on
the GPU more, so they can render many triangles much more efficiently.

On mobile devices, the story is different. PC and console GPUs are
brute-force monsters that can pull as much electricity as they need from
the power grid. Mobile GPUs are limited to a tiny battery, so they need
to be a lot more power efficient.

To be more efficient, mobile GPUs attempt to avoid *overdraw*. Overdraw occurs
when the same pixel on the screen is being rendered more than once. Imagine a
town with several buildings. GPUs don't know what is visible and what is hidden
until they draw it. For example, a house might be drawn and then another house
in front of it (which means rendering happened twice for the same pixel). PC
GPUs normally don't care much about this and just throw more pixel processors to
the hardware to increase performance (which also increases power consumption).

Using more power is not an option on mobile so mobile devices use a technique
called *tile-based rendering* which divides the screen into a grid. Each cell
keeps the list of triangles drawn to it and sorts them by depth to minimize
*overdraw*. This technique improves performance and reduces power consumption,
but takes a toll on vertex performance. As a result, fewer vertices and
triangles can be processed for drawing.

Additionally, tile-based rendering struggles when there are small objects with a
lot of geometry within a small portion of the screen. This forces mobile GPUs to
put a lot of strain on a single screen tile, which considerably decreases
performance as all the other cells must wait for it to complete before
displaying the frame.

To summarize, don't worry about vertex count on mobile, but
**avoid concentration of vertices in small parts of the screen**.
If a character, NPC, vehicle, etc. is far away (which means it looks tiny), use
a smaller level of detail (LOD) model. Even on desktop GPUs, it's preferable to
avoid having triangles smaller than the size of a pixel on screen.

Pay attention to the additional vertex processing required when using:

-  Skinning (skeletal animation)
-  Morphs (shape keys)
-  Vertex-lit objects (common on mobile)

Pixel/fragment shaders and fill rate
------------------------------------

In contrast to vertex processing, the costs of fragment (per-pixel) shading have
increased dramatically over the years. Screen resolutions have increased: the
area of a 4K screen is 8,294,400 pixels, versus 307,200 for an old 640×480 VGA
screen. That is 27 times the area! Also, the complexity of fragment shaders has
exploded. Physically-based rendering requires complex calculations for each
fragment.

You can test whether a project is fill rate-limited quite easily. Turn off
V-Sync to prevent capping the frames per second, then compare the frames per
second when running with a large window, to running with a very small window.
You may also benefit from similarly reducing your shadow map size if using
shadows. Usually, you will find the FPS increases quite a bit using a small
window, which indicates you are to some extent fill rate-limited. On the other
hand, if there is little to no increase in FPS, then your bottleneck lies
elsewhere.

You can increase performance in a fill rate-limited project by reducing the
amount of work the GPU has to do. You can do this by simplifying the shader
(perhaps turn off expensive options if you are using a :ref:`StandardMaterial3D
<class_StandardMaterial3D>`), or reducing the number and size of textures used.
Also, when using non-unshaded particles, consider forcing vertex shading in
their material to decrease the shading cost.

.. seealso::

    On supported hardware, :ref:`doc_variable_rate_shading` can be used to
    reduce shading processing costs without impacting the sharpness of edges on
    the final image.

**When targeting mobile devices, consider using the simplest possible shaders
you can reasonably afford to use.**

Reading textures
~~~~~~~~~~~~~~~~

The other factor in fragment shaders is the cost of reading textures. Reading
textures is an expensive operation, especially when reading from several
textures in a single fragment shader. Also, consider that filtering may slow it
down further (trilinear filtering between mipmaps, and averaging). Reading
textures is also expensive in terms of power usage, which is a big issue on
mobiles.

**If you use third-party shaders or write your own shaders, try to use
algorithms that require as few texture reads as possible.**

Texture compression
~~~~~~~~~~~~~~~~~~~

By default, Godot compresses textures of 3D models when imported using video RAM
(VRAM) compression. Video RAM compression isn't as efficient in size as PNG or
JPG when stored, but increases performance enormously when drawing large enough
textures.

This is because the main goal of texture compression is bandwidth reduction
between memory and the GPU.

In 3D, the shapes of objects depend more on the geometry than the texture, so
compression is generally not noticeable. In 2D, compression depends more on
shapes inside the textures, so the artifacts resulting from 2D compression are
more noticeable.

As a warning, most Android devices do not support texture compression of
textures with transparency (only opaque), so keep this in mind.

.. note::

   Even in 3D, "pixel art" textures should have VRAM compression disabled as it
   will negatively affect their appearance, without improving performance
   significantly due to their low resolution.

Post-processing and shadows
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Post-processing effects and shadows can also be expensive in terms of fragment
shading activity. Always test the impact of these on different hardware.

**Reducing the size of shadowmaps can increase performance**, both in terms of
writing and reading the shadowmaps. On top of that, the best way to improve
performance of shadows is to turn shadows off for as many lights and objects as
possible. Smaller or distant OmniLights/SpotLights can often have their shadows
disabled with only a small visual impact.

Transparency and blending
-------------------------

Transparent objects present particular problems for rendering efficiency. Opaque
objects (especially in 3D) can be essentially rendered in any order and the
Z-buffer will ensure that only the front most objects get shaded. Transparent or
blended objects are different. In most cases, they cannot rely on the Z-buffer
and must be rendered in "painter's order" (i.e. from back to front) to look
correct.

Transparent objects are also particularly bad for fill rate, because every item
has to be drawn even if other transparent objects will be drawn on top
later on.

Opaque objects don't have to do this. They can usually take advantage of the
Z-buffer by writing to the Z-buffer only first, then only performing the
fragment shader on the "winning" fragment, the object that is at the front at a
particular pixel.

Transparency is particularly expensive where multiple transparent objects
overlap. It is usually better to use transparent areas as small as possible to
minimize these fill rate requirements, especially on mobile, where fill rate is
very expensive. Indeed, in many situations, rendering more complex opaque
geometry can end up being faster than using transparency to "cheat".

Multi-platform advice
---------------------

If you are aiming to release on multiple platforms, test *early* and test
*often* on all your platforms, especially mobile. Developing a game on desktop
but attempting to port it to mobile at the last minute is a recipe for disaster.

In general, you should design your game for the lowest common denominator, then
add optional enhancements for more powerful platforms. For example, you may want
to use the Compatibility rendering method for both desktop and mobile platforms
where you target both.

Mobile/tiled renderers
----------------------

As described above, GPUs on mobile devices work in dramatically different ways
from GPUs on desktop. Most mobile devices use tile renderers. Tile renderers
split up the screen into regular-sized tiles that fit into super fast cache
memory, which reduces the number of read/write operations to the main memory.

There are some downsides though. Tiled rendering can make certain techniques
much more complicated and expensive to perform. Tiles that rely on the results
of rendering in different tiles or on the results of earlier operations being
preserved can be very slow. Be very careful to test the performance of shaders,
viewport textures and post processing.
