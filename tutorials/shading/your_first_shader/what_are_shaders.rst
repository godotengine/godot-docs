.. _doc_what_are_shaders:

What are shaders
================

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

But what are they
-----------------

Shaders are a special kind of program that runs on the GPU. 

Objects are drawn using an associated shader. The output of the shader is the pixel colors drawn
to the viewport. Shaders do not save their results, nor can they be used to draw outside their
corresponding mesh. The lack of flexibility allows shaders to be incredibly fast. 

What can they do
----------------
- position vertices very fast
- compute color very fast
- compute lighting very fast

What can't they do
------------------
- cant draw outside mesh
- cant access other pixels from current pixel (or vertices)
- cant store previous iterations
- update on the fly (they can, but they need to be compiled)
 
Technical overview
------------------

GPUs are able to render graphics much faster than CPUs for a few reasons, but most notably,
because they are able to run calculations massively in parallel. A CPU typically has 4 or 8 cores
while a GPU typically has hundreds. That means a GPU can do hundreds of tasks at once. GPU architects
have exploited this in a way that allows for doing many calculations very quickly, but only when
many or all cores are doing the same calculation at once, but with different data.

That is where shaders come in. The GPU will call the shader a bunch of times simultaneously, and then
operate on different bits of data (vertices, or pixels). These bunches of data are often called wavefronts.
A shader will run the same for every thread in the wavefront. For example, if a given GPU can handle 100 
threads per wavefront, a wavefront will run on a 10x10 block of pixels together. And it will continue to
run for all pixels in that wavefront until they are complete. Accordingly, if you have one pixel slower 
than the rest (due to excessive branching), the entire block will be slowed down, resulting in massively
slower render times. This is different than CPU based operations, on a CPU if you can speed up even one
pixel the entire rendering time will decrease. On a GPU, you have to speed up the entire wavefront
to speed up rendering.

