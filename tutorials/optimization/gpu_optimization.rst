.. _doc_gpu_optimization:

GPU Optimizations
=================

Introduction
~~~~~~~~~~~~

The demand for new graphics features and progress almost guarantees that you
will encounter graphics bottlenecks. Some of these can be CPU side, for instance
in calculations inside the Godot engine to prepare objects for rendering.
Bottlenecks can also occur on the CPU in the graphics driver, which sorts
instructions to pass to the GPU, and in the transfer of these instructions. And
finally bottlenecks also occur on the GPU itself.

Where bottlenecks occur in rendering is highly hardware specific. Mobile GPUs in
particular may struggle with scenes that run easily on desktop.

Understanding and investigating GPU bottlenecks is slightly different to the
situation on the CPU, because often you can only change performance indirectly,
by changing the instructions you give to the GPU, and it may be more difficult
to take measurements. Often the only way of measuring performance is by
examining changes in frame rate.

Drawcalls, state changes, and APIs
==================================

.. note:: The following section is not relevant to end-users, but is useful to
          provide background information that is relevant in later sections.

Godot sends instructions to the GPU via a graphics API (OpenGL, GLES2, GLES3,
Vulkan). The communication and driver activity involved can be quite costly,
especially in OpenGL. If we can provide these instructions in a way that is
preferred by the driver and GPU, we can greatly increase performance.

Nearly every API command in OpenGL requires a certain amount of validation, to
make sure the GPU is in the correct state. Even seemingly simple commands can
lead to a flurry of behind the scenes housekeeping. Therefore the name of the
game is reduce these instructions to a bare minimum, and group together similar
objects as much as possible so they can be rendered together, or with the
minimum number of these expensive state changes.

2D batching
~~~~~~~~~~~

In 2d, the costs of treating each item individually can be prohibitively high -
there can easily be thousands on screen. This is why 2d batching is used -
multiple similar items are grouped together and rendered in a batch, via a
single drawcall, rather than making a separate drawcall for each item. In
addition this means that state changes, material and texture changes can be kept
to a minimum.

For more information on 2D batching see :ref:`doc_batching`.

3D batching
~~~~~~~~~~~

In 3d, we still aim to minimize draw calls and state changes, however, it can be
more difficult to batch together several objects into a single draw call. 3d
meshes tend to comprise hundreds or thousands of triangles, and combining large
meshes at runtime is prohibitively expensive. The costs of joining them quickly
exceeds any benefits as the number of triangles grows per mesh. A much better
alternative is to join meshes ahead of time (static meshes in relation to each
other). This can either be done by artists, or programmatically within Godot.

There is also a cost to batching together objects in 3d. Several objects
rendered as one cannot be individually culled. An entire city that is off screen
will still be rendered if it is joined to a single blade of grass that is on
screen. So attempting to batch together 3d objects should take account of their
location and effect on culling. Despite this, the benefits of joining static
objects often outweigh other considerations, especially for large numbers of low
poly objects. 

For more information on 3D specific optimizations, see
:ref:`doc_optimizing_3d_performance`.

Reuse Shaders and Materials
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Godot renderer is a little different to what is out there. It's designed to
minimize GPU state changes as much as possible. :ref:`SpatialMaterial
<class_SpatialMaterial>` does a good job at reusing materials that need similar
shaders but, if custom shaders are used, make sure to reuse them as much as
possible. Godot's priorities are:

-  **Reusing Materials**: The fewer different materials in the
   scene, the faster the rendering will be. If a scene has a huge amount
   of objects (in the hundreds or thousands) try reusing the materials
   or in the worst case use atlases.
-  **Reusing Shaders**: If materials can't be reused, at least try to
   re-use shaders (or SpatialMaterials with different parameters but the same
   configuration).

If a scene has, for example, ``20,000`` objects with ``20,000`` different
materials each, rendering will be slow. If the same scene has ``20,000``
objects, but only uses ``100`` materials, rendering will be much faster.

Pixel cost vs vertex cost
=========================

You may have heard that the lower the number of polygons in a model, the faster
it will be rendered. This is *really* relative and depends on many factors.

On a modern PC and console, vertex cost is low. GPUs originally only rendered
triangles, so every frame all the vertices:

1. Had to be transformed by the CPU (including clipping).

2. Had to be sent to the GPU memory from the main RAM.

Now all this is handled inside the GPU, so the performance is much higher. 3D
artists usually have the wrong feeling about polycount performance because 3D
DCCs (such as Blender, Max, etc.) need to keep geometry in CPU memory in order
for it to be edited, reducing actual performance. Game engines rely on the GPU
more so they can render many triangles much more efficiently.

On mobile devices, the story is different. PC and Console GPUs are
brute-force monsters that can pull as much electricity as they need from
the power grid. Mobile GPUs are limited to a tiny battery, so they need
to be a lot more power efficient.

To be more efficient, mobile GPUs attempt to avoid *overdraw*. This means, the
same pixel on the screen being rendered more than once. Imagine a town with
several buildings, GPUs don't know what is visible and what is hidden until they
draw it. A house might be drawn and then another house in front of it (rendering
happened twice for the same pixel!). PC GPUs normally don't care much about this
and just throw more pixel processors to the hardware to increase performance
(but this also increases power consumption).

Using more power is not an option on mobile so mobile devices use a technique
called "Tile Based Rendering" which divides the screen into a grid. Each cell
keeps the list of triangles drawn to it and sorts them by depth to minimize
*overdraw*. This technique improves performance and reduces power consumption,
but takes a toll on vertex performance. As a result, fewer vertices and
triangles can be processed for drawing.

Additionally, Tile Based Rendering struggles when there are small objects with a
lot of geometry within a small portion of the screen. This forces mobile GPUs to
put a lot of strain on a single screen tile which considerably decreases
performance as all the other cells must wait for it to complete in order to
display the frame.

In summary, do not worry about vertex count on mobile, but avoid concentration
of vertices in small parts of the screen. If a character, NPC, vehicle, etc. is
far away (so it looks tiny), use a smaller level of detail (LOD) model.

Pay attention to the additional vertex processing required when using:

-  Skinning (skeletal animation)
-  Morphs (shape keys)
-  Vertex-lit objects (common on mobile)

Pixel / fragment shaders - fill rate
====================================

In contrast to vertex processing, the costs of fragment shading has increased
dramatically over the years. Screen resolutions have increased (the area of a 4K
screen is ``8,294,400`` pixels, versus ``307,200`` for an old ``640x480`` VGA
screen, that is 27x the area), but also the complexity of fragment shaders has
exploded. Physically based rendering requires complex calculations for each
fragment.

You can test whether a project is fill rate limited quite easily. Turn off vsync
to prevent capping the frames per second, then compare the frames per second
when running with a large window, to running with a postage stamp sized window
(you may also benefit from similarly reducing your shadow map size if using
shadows). Usually you will find the fps increases quite a bit using a small
window, which indicates you are to some extent fill rate limited. If on the
other hand there is little to no increase in fps, then your bottleneck lies
elsewhere.

You can increase performance in a fill rate limited project by reducing the
amount of work the GPU has to do. You can do this by simplifying the shader
(perhaps turn off expensive options if you are using a :ref:`SpatialMaterial
<class_SpatialMaterial>`), or reducing the number and size of textures used.

Consider shipping simpler shaders for mobile.

Reading textures
~~~~~~~~~~~~~~~~

The other factor in fragment shaders is the cost of reading textures. Reading
textures is an expensive operation (especially reading from several in a single
fragment shader), and also consider the filtering may add expense to this
(trilinear filtering between mipmaps, and averaging). Reading textures is also
expensive in power terms, which is a big issue on mobiles.

Texture compression
~~~~~~~~~~~~~~~~~~~

Godot compresses textures of 3D models when imported (VRAM compression) by
default. Video RAM compression is not as efficient in size as PNG or JPG when
stored, but increases performance enormously when drawing.

This is because the main goal of texture compression is bandwidth reduction
between memory and the GPU.

In 3D, the shapes of objects depend more on the geometry than the texture, so
compression is generally not noticeable. In 2D, compression depends more on
shapes inside the textures, so the artifacts resulting from 2D compression are
more noticeable.

As a warning, most Android devices do not support texture compression of
textures with transparency (only opaque), so keep this in mind.

Post processing / shadows
~~~~~~~~~~~~~~~~~~~~~~~~~

Post processing effects and shadows can also be expensive in terms of fragment
shading activity. Always test the impact of these on different hardware.

Reducing the size of shadow maps can increase performance, both in terms of
writing, and reading the maps.

Transparency / blending
=======================

Transparent items present particular problems for rendering efficiency. Opaque
items (especially in 3d) can be essentially rendered in any order and the
Z-buffer will ensure that only the front most objects get shaded. Transparent or
blended objects are different - in most cases they cannot rely on the Z-buffer
and must be rendered in "painter's order" (i.e. from back to front) in order to
look correct.

The transparent items are also particularly bad for fill rate, because every
item has to be drawn, even if later transparent items will be drawn on top.

Opaque items don't have to do this. They can usually take advantage of the
Z-buffer by writing to the Z-buffer only first, then only performing the
fragment shader on the 'winning' fragment, the item that is at the front at a
particular pixel.

Transparency is particularly expensive where multiple transparent items overlap.
It is usually better to use as small a transparent area as possible in order to
minimize these fill rate requirements, especially on mobile, where fill rate is
very expensive. Indeed, in many situations, rendering more complex opaque
geometry can end up being faster than using transparency to "cheat".

Multi-Platform Advice
=====================

If you are aiming to release on multiple platforms, test `early` and test
`often` on all your platforms, especially mobile. Developing a game on desktop
but attempting to port to mobile at the last minute is a recipe for disaster.

In general you should design your game for the lowest common denominator, then
add optional enhancements for more powerful platforms. For example, you may want
to use the GLES2 backend for both desktop and mobile platforms where you target
both.

Mobile / tile renderers
=======================

GPUs on mobile devices work in dramatically different ways from GPUs on desktop.
Most mobile devices use tile renderers. Tile renderers split up the screen into
regular sized tiles that fit into super fast cache memory, and reduce the reads
and writes to main memory.

There are some downsides though, it can make certain techniques much more
complicated and expensive to perform. Tiles that rely on the results of
rendering in different tiles or on the results of earlier operations being
preserved can be very slow. Be very careful to test the performance of shaders,
viewport textures and post processing.
