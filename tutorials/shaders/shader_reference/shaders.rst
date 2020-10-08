.. _doc_shaders:

Shaders
=======

Introduction
------------

Shaders are unique programs that run on the GPU. They are used to specify how to take mesh
data (vertex positions, colors, normals, etc.) and draw them to the screen. Shaders do not process
information the same way a normal program does because they are optimized for running on the GPU.
One consequence of this is that shaders do not retain their data after they run; they output a final
color to the screen and then move on. Accordingly, there is no way of accessing the color output from
the last run of the shader.

Godot uses a shader language very similar to GLSL, but with added functionality and slightly less
flexibility. The reason for doing this is that Godot integrates built-in functionality to make
writing complex shaders substantially easier. Godot wraps the user-written shader code in code
of its own. That way, Godot handles a lot of the low-level stuff that the user doesn't need to
worry about, and it is able to parse your shader code and use it to affect the rendering pipeline.
For more advanced shaders, you can turn this functionality off using a render_mode.

This document provides you with some information about shaders, specific to Godot. For a detailed
reference of the shading language in Godot see the :ref:`Godot shading language doc<doc_shading_language>`.

Shader types
------------

Instead of supplying a general purpose configuration for all uses (2D, 3D, particles),
Godot shaders must specify what they are intended for. Different types support different
render modes, built-in variables, and processing functions.

All shaders need to specify their type in the first line, in the following format:

.. code-block:: glsl

    shader_type spatial;

Valid types are:

* :ref:`spatial <doc_spatial_shader>`: For 3D rendering.
* :ref:`canvas_item <doc_canvas_item_shader>`: For 2D rendering.
* :ref:`particles <doc_particle_shader>`: For particle systems.

For detailed information on each shading type, see the corresponding reference document.

Render modes
------------

Different shader types support different render modes. They are optional and, if specified, must
be after the *shader_type*. Render modes are used to alter the way built-in functionality is handled.
For example, it is common to use the render mode ``unshaded`` to skip the built-in light processor
function.

Render modes are specified underneath the shader type:

.. code-block:: glsl

    shader_type spatial;
    render_mode unshaded, cull_disabled;

Each shader type has a different list of render modes available. See the document for each shader
type for a complete list of render modes.

Processor functions
-------------------

Depending on the shader type, different processor functions may be optionally overridden.
For "spatial" and "canvas_item", it is possible to override ``vertex``, ``fragment``, and ``light``.
For "particles", only ``vertex`` can be overridden.

Vertex processor
^^^^^^^^^^^^^^^^

The ``vertex`` processing function is called once for every vertex in "spatial" and "canvas_item" shaders.
For "particles" shaders, it is called once for every particle.

The ``vertex`` function is used to modify per-vertex information that will be passed on to the fragment
function. It can also be used to establish variables that will be sent to the fragment function by using
varyings(see other doc).

By default, Godot will take your vertex information and transform it accordingly to be drawn. If this is
undesirable, you can use render modes to transform the data yourself; see the
:ref:`Spatial shader doc <doc_spatial_shader>` for an example of this.

Fragment processor
^^^^^^^^^^^^^^^^^^

The ``fragment`` processing function is used to set up the Godot material parameters per pixel. This code
runs on every visible pixel the object or primitive draws. It is only available in "spatial" and
"canvas_item" shaders.

The standard use of the fragment function is to set up material properties that will be used to calculate
lighting. For example, you would set values for ``ROUGHNESS``, ``RIM``, or ``TRANSMISSION`` which would
tell the light function how the lights respond to that fragment. This makes it possible to control a complex
shading pipeline without the user having to write much code. If you don't need this built-in functionality,
you can ignore it and write your own light processing function and Godot will optimize it away. For example,
if you do not write a value to ``RIM``, Godot will not calculate rim lighting. During compilation, Godot checks
to see if ``RIM`` is used; if not, it cuts all the corresponding code out. Therefore, you will not
waste calculations on effects that you do not use.

Light processor
^^^^^^^^^^^^^^^

The ``light`` processor runs per pixel too, but also runs for every light that affects the object
(and does not run if no lights affect the object). It exists as a function called inside the
``fragment`` processor and typically operates on the material properties setup inside the ``fragment``
function.

The ``light`` processor works differently in 2D than it does in 3D; for a description of how it works
in each, see their documentation, :ref:`CanvasItem shaders <doc_canvas_item_shader>` and
:ref:`Spatial shaders <doc_spatial_shader>`, respectively.
