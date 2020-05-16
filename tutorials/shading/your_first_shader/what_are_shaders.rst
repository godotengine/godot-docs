.. _doc_what_are_shaders:

What are shaders?
=================

Introduction
------------

So, you have decided to give shaders a try. You have likely heard that they can be used to
create interesting effects that run incredibly fast. You have also likely heard that they
are terrifying. Both are true.

Shaders can be used to create a wide range of effects (in fact everything drawn in a modern
rendering engine is done with shaders).

Writing shaders can also be very difficult for people unfamiliar with them. Godot tries to make writing
shaders a little easier by exposing many useful built-in features and handling some of the
lower-level initialization work for you. However, GLSL (the OpenGL Shading Language, which Godot uses)
is still unintuitive and restricting, especially for users who are used to GDScript.

But what are they?
------------------

Shaders are a special kind of program that runs on Graphics Processing Units (GPUs). Most computers
have some sort of GPU, either one integrated into their CPU or discrete (meaning it is a separate
hardware component, for example, the typical graphics card). GPUs are especially useful for
rendering because they are optimized for running thousands of instructions in parallel.

The output of the shader is typically the colored pixels of the object drawn to the viewport. But some
shaders allow for specialized outputs (this is especially true for APIs like Vulkan). Shaders operate
inside the shader pipeline. The standard process is the vertex -> fragment shader pipeline. The vertex
shader is used to decided where each vertex (point in a 3D model, or corner of a Sprite) goes and the
fragment shader decides what color individual pixels receive.

Suppose you want to update all the pixels in a texture to a given color, on the CPU you would write:

::

  for x in range(width):
    for y in range(height):
      set_color(x, y, some_color)

In a shader you are given access only to the inside of the loop so what you write looks like this:

.. code-block:: glsl

  // function called for each pixel
  void fragment() {
    COLOR = some_color;
  }

You have no control over how this function is called. So you have to design your shaders
differently from how you would design programs on the CPU.

A consequence of the shader pipeline is that you cannot access the results from a previous
run of the shader, you cannot access other pixels from the pixel being drawn, and you cannot
write outside of the current pixel being drawn. This enables the GPU to execute the shader
for different pixels in parallel, as they do not depend on each other. This lack of
flexibility is designed to work with the GPU which allows shaders to be incredibly fast.

What can they do
^^^^^^^^^^^^^^^^

- position vertices very fast
- compute color very fast
- compute lighting very fast
- lots and lots of math

What can't they do
^^^^^^^^^^^^^^^^^^

- draw outside mesh
- access other pixels from current pixel (or vertices)
- store previous iterations
- update on the fly (they can, but they need to be compiled)

Structure of a shader
---------------------

In Godot, shaders are made up of 3 main functions: the ``vertex()`` function, the ``fragment()``
function and the ``light()`` function.

The ``vertex()`` function runs over all the vertices in the mesh and sets their positions as well
as some other per-vertex variables.

The ``fragment()`` function runs for every pixel that is covered by the mesh. It uses the variables
from the ``vertex()`` function to run. The variables from the ``vertex()`` function are interpolated
between the vertices to provide the values for the ``fragment()`` function.

The ``light()`` function runs for every pixel and for every light. It takes variables from the
``fragment()`` function and from previous runs of itself.

For more information about how shaders operate specifically in Godot see the :ref:`Shaders <doc_shaders>` doc.

Technical overview
------------------

GPUs are able to render graphics much faster than CPUs for a few reasons, but most notably,
because they are able to run calculations massively in parallel. A CPU typically has 4 or 8 cores
while a GPU typically has thousands. That means a GPU can do hundreds of tasks at once. GPU architects
have exploited this in a way that allows for doing many calculations very quickly, but only when
many or all cores are doing the same calculation at once, but with different data.

That is where shaders come in. The GPU will call the shader a bunch of times simultaneously, and then
operate on different bits of data (vertices, or pixels). These bunches of data are often called wavefronts.
A shader will run the same for every thread in the wavefront. For example, if a given GPU can handle 100
threads per wavefront, a wavefront will run on a 10×10 block of pixels together. It will continue to
run for all pixels in that wavefront until they are complete. Accordingly, if you have one pixel slower
than the rest (due to excessive branching), the entire block will be slowed down, resulting in massively
slower render times.

This is different from CPU-based operations. On a CPU, if you can speed up even one
pixel, the entire rendering time will decrease. On a GPU, you have to speed up the entire wavefront
to speed up rendering.
