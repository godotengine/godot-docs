.. _doc_introduction_to_shaders:

Introduction to shaders
=======================

This page explains what shaders are and will give you an overview of how they
work in Godot. For a detailed reference of the engine's shading language, see
:ref:`doc_shading_language`.

Shaders are a special kind of program that runs on Graphics Processing Units
(GPUs). They were initially used to shade 3D scenes but can nowadays do much
more. You can use them to control how the engine draws geometry and pixels on
the screen, allowing you to achieve all sorts of effects.

Modern rendering engines like Godot draw everything with shaders: graphics cards
can run thousands of instructions in parallel, leading to incredible rendering
speed.

Because of their parallel nature, though, shaders don't process information the
way a typical program does. Shader code runs on each vertex or pixel in
isolation. You cannot store data between frames either. As a result, when
working with shaders, you need to code and think differently from other
programming languages.

Suppose you want to update all the pixels in a texture to a given color. In
GDScript, your code would use ``for`` loops::

  for x in range(width):
    for y in range(height):
      set_color(x, y, some_color)

Your code is already part of a loop in a shader, so the corresponding code would
look like this.

.. code-block:: glsl

  void fragment() {
    COLOR = some_color;
  }

.. note::

   The graphics card calls the ``fragment()`` function once or more for each
   pixel it has to draw. More on that below.

Shaders in Godot
----------------

Godot provides a shading language based on the popular OpenGL Shading Language
(GLSL) but simplified. The engine handles some of the lower-level initialization
work for you, making it easier to write complex shaders.

In Godot, shaders are made up of main functions called "processor functions".
Processor functions are the entry point for your shader into the program. There
are seven different processor functions.

1. The ``vertex()`` function runs over all the vertices in the mesh and sets
   their positions and some other per-vertex variables. Used in
   :ref:`canvas_item shaders <doc_canvas_item_shader>` and
   :ref:`spatial shaders <doc_spatial_shader>`.

2. The ``fragment()`` function runs for every pixel covered by the mesh. It uses
   values output by the ``vertex()`` function, interpolated between the
   vertices. Used in :ref:`canvas_item shaders <doc_canvas_item_shader>` and
   :ref:`spatial shaders <doc_spatial_shader>`.

3. The ``light()`` function runs for every pixel and for every light. It takes
   variables from the ``fragment()`` function and from its previous runs. Used
   in :ref:`canvas_item shaders <doc_canvas_item_shader>` and
   :ref:`spatial shaders <doc_spatial_shader>`.

4. The ``start()`` function runs for every particle in a particle system once
   when the particle is first spawned. Used in
   :ref:`particles shaders <doc_particle_shader>`.

5. The ``process()`` function runs for every particle in a particle system for
   each frame. Used in :ref:`particles shaders <doc_particle_shader>`.

6. The ``sky()`` function runs for every pixel in the radiance cubemap when the
   radiance cubemap needs to be updated, and for every pixel on the current
   screen. Used in :ref:`sky shaders <doc_sky_shader>`.

7. The ``fog()`` function runs for every froxel in the volumetric fog froxel
   buffer that intersects with the :ref:`FogVolume <class_FogVolume>`. Used by
   :ref:`fog shaders <doc_fog_shader>`.

.. warning::

    The ``light()`` function won't run if the ``vertex_lighting`` render mode is
    enabled, or if **Rendering > Quality > Shading > Force Vertex Shading** is
    enabled in the Project Settings. It's enabled by default on mobile
    platforms.

.. note::

   Godot also exposes an API for users to write totally custom GLSL shaders. For
   more information see :ref:`doc_compute_shaders`.

Shader types
------------

Instead of supplying a general-purpose configuration for all uses (2D, 3D,
particles, sky, fog), you must specify the type of shader you're writing.
Different types support different render modes, built-in variables, and
processing functions.

In Godot, all shaders need to specify their type in the first line, like so:

.. code-block:: glsl

    shader_type spatial;

Here are the available types:

* :ref:`spatial <doc_spatial_shader>` for 3D rendering.
* :ref:`canvas_item <doc_canvas_item_shader>` for 2D rendering.
* :ref:`particles <doc_particle_shader>` for particle systems.
* :ref:`sky <doc_sky_shader>` to render :ref:`Skies <class_Sky>`.
* :ref:`fog <doc_fog_shader>` to render :ref:`FogVolumes <class_FogVolume>`

Render modes
------------

Shaders have optional render modes you can specify on the second line, after the
shader type, like so:

.. code-block:: glsl

    shader_type spatial;
    render_mode unshaded, cull_disabled;

Render modes alter the way Godot applies the shader. For example, the
``unshaded`` mode makes the engine skip the built-in light processor function.

Each shader type has different render modes. See the reference for each shader
type for a complete list of render modes.

Vertex processor
^^^^^^^^^^^^^^^^

The ``vertex()`` processing function is called once for every vertex in
``spatial`` and ``canvas_item`` shaders.

Each vertex in your world's geometry has properties like a position and color.
The function modifies those values and passes them to the fragment function. You
can also use it to send extra data to the fragment function using varyings.

By default, Godot transforms your vertex information for you, which is necessary
to project geometry onto the screen. You can use render modes to transform the
data yourself; see the :ref:`Spatial shader doc <doc_spatial_shader>` for an
example.

Fragment processor
^^^^^^^^^^^^^^^^^^

The ``fragment()`` processing function is used to set up the Godot material
parameters per pixel. This code runs on every visible pixel the object or
primitive draws. It is only available in ``spatial``, ``canvas_item``, and ``sky`` shaders.

The standard use of the fragment function is to set up material properties used
to calculate lighting. For example, you would set values for ``ROUGHNESS``,
``RIM``, or ``TRANSMISSION``, which would tell the light function how the lights
respond to that fragment. This makes it possible to control a complex shading
pipeline without the user having to write much code. If you don't need this
built-in functionality, you can ignore it and write your own light processing
function, and Godot will optimize it away. For example, if you do not write a
value to ``RIM``, Godot will not calculate rim lighting. During compilation,
Godot checks to see if ``RIM`` is used; if not, it cuts all the corresponding
code out. Therefore, you will not waste calculations on the effects that you do
not use.

Light processor
^^^^^^^^^^^^^^^

The ``light()`` processor runs per pixel too, and it runs once for every light
that affects the object. It does not run if no lights affect the object. It
exists as a function called inside the ``fragment()`` processor and typically
operates on the material properties setup inside the ``fragment()`` function.

The ``light()`` processor works differently in 2D than it does in 3D; for a
description of how it works in each, see their documentation, :ref:`CanvasItem
shaders <doc_canvas_item_shader>` and :ref:`Spatial shaders
<doc_spatial_shader>`, respectively.
