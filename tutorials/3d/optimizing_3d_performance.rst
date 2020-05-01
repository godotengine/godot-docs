.. meta::
    :keywords: optimization

.. _doc_optimizing_3d_performance:

Optimizing 3D performance
=========================

Introduction
~~~~~~~~~~~~

Godot follows a balanced performance philosophy. In the performance world,
there are always trade-offs, which consist of trading speed for
usability and flexibility. Some practical examples of this are:

-  Rendering objects efficiently in high amounts is easy, but when a
   large scene must be rendered, it can become inefficient. To solve
   this, visibility computation must be added to the rendering, which
   makes rendering less efficient, but, at the same time, fewer objects are
   rendered, so efficiency overall improves.
-  Configuring the properties of every material for every object that
   needs to be rendered is also slow. To solve this, objects are sorted
   by material to reduce the costs, but at the same time sorting has a
   cost.
-  In 3D physics a similar situation happens. The best algorithms to
   handle large amounts of physics objects (such as SAP) are slow
   at insertion/removal of objects and ray-casting. Algorithms that
   allow faster insertion and removal, as well as ray-casting, will not
   be able to handle as many active objects.

And there are many more examples of this! Game engines strive to be
general purpose in nature, so balanced algorithms are always favored
over algorithms that might be fast in some situations and slow in
others.. or algorithms that are fast but make usability more difficult.

Godot is not an exception and, while it is designed to have backends
swappable for different algorithms, the default ones (or more like, the
only ones that are there for now) prioritize balance and flexibility
over performance.

With this clear, the aim of this tutorial is to explain how to get the
maximum performance out of Godot.

Rendering
~~~~~~~~~

3D rendering is one of the most difficult areas to get performance from,
so this section will have a list of tips.

Reuse shaders and materials
---------------------------

The Godot renderer is a little different to what is out there. It's designed
to minimize GPU state changes as much as possible.
:ref:`class_SpatialMaterial`
does a good job at reusing materials that need similar shaders but, if
custom shaders are used, make sure to reuse them as much as possible.
Godot's priorities will be like this:

-  **Reusing Materials**: The fewer different materials in the
   scene, the faster the rendering will be. If a scene has a huge amount
   of objects (in the hundreds or thousands) try reusing the materials
   or in the worst case use atlases.
-  **Reusing Shaders**: If materials can't be reused, at least try to
   re-use shaders (or SpatialMaterials with different parameters but the same
   configuration).

If a scene has, for example, 20.000 objects with 20.000 different
materials each, rendering will be slow. If the same scene has
20.000 objects, but only uses 100 materials, rendering will be blazingly
fast.

Pixel cost vs vertex cost
-------------------------

It is a common thought that the lower the number of polygons in a model, the
faster it will be rendered. This is *really* relative and depends on
many factors.

On a modern PC and console, vertex cost is low. GPUs
originally only rendered triangles, so all the vertices:

1. Had to be transformed by the CPU (including clipping).

2. Had to be sent to the GPU memory from the main RAM.

Nowadays, all this is handled inside the GPU, so the performance is
extremely high. 3D artists usually have the wrong feeling about
polycount performance because 3D DCCs (such as Blender, Max, etc.) need
to keep geometry in CPU memory in order for it to be edited, reducing
actual performance. Truth is, a model rendered by a 3D engine is much
more optimal than how 3D DCCs display them.

On mobile devices, the story is different. PC and Console GPUs are
brute-force monsters that can pull as much electricity as they need from
the power grid. Mobile GPUs are limited to a tiny battery, so they need
to be a lot more power efficient.

To be more efficient, mobile GPUs attempt to avoid *overdraw*. This
means, the same pixel on the screen being rendered (as in, with lighting
calculation, etc.) more than once. Imagine a town with several buildings,
GPUs don't know what is visible and what is hidden until they
draw it. A house might be drawn and then another house in front of it
(rendering happened twice for the same pixel!). PC GPUs normally don't
care much about this and just throw more pixel processors to the
hardware to increase performance (but this also increases power
consumption).

On mobile, pulling more power is not an option, so a technique called
"Tile Based Rendering" is used (almost every mobile hardware uses a
variant of it), which divides the screen into a grid. Each cell keeps the
list of triangles drawn to it and sorts them by depth to minimize
*overdraw*. This technique improves performance and reduces power
consumption, but takes a toll on vertex performance. As a result, fewer
vertices and triangles can be processed for drawing.

Generally, this is not so bad, but there is a corner case on mobile that
must be avoided, which is to have small objects with a lot of geometry
within a small portion of the screen. This forces mobile GPUs to put a
lot of strain on a single screen cell, considerably decreasing
performance (as all the other cells must wait for it to complete in
order to display the frame).

To make it short, do not worry about vertex count so much on mobile, but
avoid concentration of vertices in small parts of the screen. If, for
example, a character, NPC, vehicle, etc. is far away (so it looks tiny),
use a smaller level of detail (LOD) model instead.

An extra situation where vertex cost must be considered is objects that
have extra processing per vertex, such as:

-  Skinning (skeletal animation)
-  Morphs (shape keys)
-  Vertex Lit Objects (common on mobile)

Texture compression
-------------------

Godot offers to compress textures of 3D models when imported (VRAM
compression). Video RAM compression is not as efficient in size as PNG
or JPG when stored, but increases performance enormously when drawing.

This is because the main goal of texture compression is bandwidth
reduction between memory and the GPU.

In 3D, the shapes of objects depend more on the geometry than the
texture, so compression is generally not noticeable. In 2D, compression
depends more on shapes inside the textures, so the artifacts resulting
from 2D compression are more noticeable.

As a warning, most Android devices do not support texture compression of
textures with transparency (only opaque), so keep this in mind.

Transparent objects
-------------------

As mentioned before, Godot sorts objects by material and shader to
improve performance. This, however, can not be done on transparent
objects. Transparent objects are rendered from back to front to make
blending with what is behind work. As a result, please try to keep
transparent objects to a minimum! If an object has a small section with
transparency, try to make that section a separate material.

Level of detail (LOD)
---------------------

As also mentioned before, using objects with fewer vertices can improve
performance in some cases. Godot has a simple system to change level
of detail,
:ref:`GeometryInstance <class_GeometryInstance>`
based objects have a visibility range that can be defined. Having
several GeometryInstance objects in different ranges works as LOD.

Use instancing (MultiMesh)
--------------------------

If several identical objects have to be drawn in the same place or
nearby, try using :ref:`MultiMesh <class_MultiMesh>`
instead. MultiMesh allows the drawing of dozens of thousands of objects at
very little performance cost, making it ideal for flocks, grass,
particles, etc.

Bake lighting
-------------

Small lights are usually not a performance issue. Shadows a little more.
In general, if several lights need to affect a scene, it's ideal to bake
it (:ref:`doc_baked_lightmaps`). Baking can also improve the scene quality by
adding indirect light bounces.

If working on mobile, baking to texture is recommended, since this
method is even faster.
