Shader Materials
================

Introduction
------------

For the most common cases, [[Fixed Material]] are enough to create the
desired textures or look and feel. Shader materials are a step beyond
that adds a huge amount of flexibility. With them, it is possible to:

-  Create procedural texures.
-  Create complex texture blendings.
-  Create animated materials, or materials that change with time.
-  Create refractive effects or other advanced effects.
-  Create special lighting shaders for more exotic materials.
-  Animate vertices, like tree leaves or grass.
-  And much more!

Traditionally, most engines will ask you to learn GLSL, HLSL or CG,
which are pretty complex for the skillset of most artists. Godot uses a
simplified version of a shader language that will detect errors as you
type, so you can see your edited shaders in real-time. Additionally, it
is possible to edit shaders using a visual graph editor (NOTE: Currently
disabled! work in progress!).

Creating a ShaderMaterial
-------------------------

Create a new ShaderMaterial in some object of your choice. Go to the
"Shader" property, then create a new `Shader <>`__

.. image:: /img/shader_material_create.png

Edit the newly created shader, and the shader editor will open:

.. image:: /img/shader_material_editor.png

There are three code tabs open, the first is for the vertex shader, the
second for the fragment and the third for the lighting. The shader
language is documented in it's [[Shader]] so a small example will be
presented next.

Create a very simple fragment shader that writes a color:

::

    uniform color col;
    DIFFUSE = col.rgb;

Code changes take place in real-time. If the code is modified, it will
be instantly recompiled and the object will be updated. If a typo is
made, the editor will notify of the compilation failure:

.. image:: /img/shader_material_typo.png

Finally, go back and edit the material, and the exported uniform will be
instantly visible:

.. image:: /img/shader_material_col.png

This allows to very quickly create custom, complex materials for every
type of object.

*Juan Linietsky, Ariel Manzur, Distributed under the terms of the `CC
By <https://creativecommons.org/licenses/by/3.0/legalcode>`__ license.*


