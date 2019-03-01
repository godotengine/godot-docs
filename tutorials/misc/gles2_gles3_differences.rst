.. _doc_gles2_gles3_differences:

Differences between GLES2 and GLES3
===================================

This page documents the differences between GLES2 and GLES3 that are by design and are not the result
of bugs. There may be differences that are unintentional, but they should be reported as bugs.

.. note:: "GLES2" and "GLES3" are the names used in Godot for the two OpenGL-based rendering backends.
          In terms of graphics APIs, the GLES2 backend maps to OpenGL 2.1 on desktop, OpenGL ES 2.0 on
          mobile and WebGL 1.0 on the web. The GLES3 backend maps to OpenGL 3.3 on desktop, OpenGL ES
          3.0 on mobile and WebGL 2.0 on the web.

Particles
---------

GLES2 cannot use the :ref:`Particles <class_Particles>` or :ref:`Particles2D <class_Particles2D>` nodes
as they require advanced GPU features. Instead, use :ref:`CPUParticles <class_CPUParticles>` or
`:ref:`CPUParticles2D <class_CPUParticles2D>`, which provides a similar interface to a
:ref:`ParticlesMaterial <class_ParticlesMaterial>`.

.. tip:: Particles and Particles2D can be converted to their CPU equivalent node with the "Convert to
         CPUParticles" option in the editor.

SCREEN_TEXTURE mip-maps
-----------------------

In GLES2, ``SCREEN_TEXTURE`` (accessed via a :ref:`ShaderMaterial <class_ShaderMaterial>`) does not have
computed mip-maps. So when accessing at a different LOD, the texture will not appear blurry. 

Color space
-----------

Shading in GLES3 takes place in linear color space while in GLES2 it takes place in sRGB space.
While this is a very important distinction for graphics programmers, for everyone else it means
that, in GLES3 shaders, you need to convert to sRGB before outputting your final color or else
your colors will appear washed out and over-bright. 

You do so with the following line of code at the end of the fragment shader:

.. code-block:: glsl

    ALBEDO = mix(pow((ALBEDO + vec3(0.055)) * (1.0 / (1.0 + 0.055)), vec3(2.4)), ALBEDO * (1.0 / 12.92), lessThan(ALBEDO, vec3(0.04045)));

GLES2 does not need this. If your game is going to use both GLES2 and GLES3, wrap it in an ``if`` 
statement checking to see if the output is in sRGB, using ``OUTPUT_IS_SRGB``. 

.. code-block:: glsl

    if (!OUTPUT_IS_SRGB) {
        ALBEDO = mix(pow((ALBEDO + vec3(0.055)) * (1.0 / (1.0 + 0.055)), vec3(2.4)), ALBEDO * (1.0 / 12.92), lessThan(ALBEDO, vec3(0.04045)));
  }

``OUTPUT_IS_SRGB`` is ``true`` in GLES2 and ``false`` in GLES3.

SpatialMaterial features
------------------------

In GLES2, the following advanced rendering features in the :ref:`SpatialMaterial <class_SpatialMaterial>` are missing:

- Refraction
- Subsurface scattering
- Anisotropy
- Clearcoat
- Depth mapping

The option to use them may appear in custom :ref:`ShaderMaterials <class_ShaderMaterial>`, however, they 
will be non-functional. For example, you will still be able to set ``SSS`` (which normally adds 
subsurface scattering) in your shader, but nothing will happen.

Environment features
--------------------

In GLES2, the following features in the :ref:`Environment <class_Environment>` are missing:

- Auto exposure
- Tonemapping
- Screen space reflections
- Screen space ambient occlusion
- Depth of field
- Glow (also known as bloom)
- Adjustment
 
That means that in GLES2 environments you can only set:

- Sky (including procedural sky)
- Ambient light
- Fog
