.. _doc_standard_material_3d:

Standard Material 3D and ORM Material 3D
========================================

Introduction
------------

``StandardMaterial3D`` and ``ORMMaterial3D`` (Occlusion, Roughness, Metallic)
are default 3D materials that aim to provide most of the features artists look
for in a material, without the need for writing shader code. However, they can
be converted to shader code if additional functionality is needed.

This tutorial explains the parameters present in both materials.

There are 4 ways to add these materials to an object. A material can be added in
the *Material* property of the mesh. It can be added in the *Material* property of
the node using the mesh (such as a MeshInstance3D node), the *Material Override* property
of the node using the mesh, and the *Material Overlay*.

.. image:: img/add_material.png

If you add a material to the mesh itself, every time that mesh is used it will have that
material. If you add a material to the node using the mesh, the material will only be used
by that node, it will also override the material property of the mesh. If a material is
added in the *Material Override* property of the node, it will only be used by that node.
It will also override the regular material property of the node and the material property of
the mesh.

The *Material Overlay* property will render a material **over** the current one being used by
the mesh. As an example, this can be used to put a transparent shield effect on a mesh.

BaseMaterial 3D Settings
------------------------

StandardMaterial3D has many settings that determine the look of a material. All of these are
under the BaseMaterial3D category

.. image:: img/spatial_material1.png

ORM materials are almost exactly the same with one difference. Instead of separate settings
and textures for occlusion, roughness, and metallic, there is a single ORM texture. The different
color channels of that texture are used for each parameter. Programs such as Substance Painter
and Armor Paint will give you the option to export in this format, for these two programs it's
with the export preset for unreal engine, which also uses ORM textures.

Transparency
------------

In Godot, materials are not transparent unless specifically configured to be.
The main reason behind this is that transparent materials are rendered
using a different technique (sorted from back to front and rendered in order).

This technique is less efficient (many state changes happen) and makes
the materials unusable with many mid- and post-processing effects
(such as SSAO, SSR, etc.) that require perfectly opaque geometry.

For this reason, materials in Godot are assumed opaque unless
specified otherwise. The main settings that enable transparency are:

* Transparency (this one)
* Blend mode set to other than "Mix"
* Enabling distance or proximity fade

When transparency other than ``0`` or ``1`` is not needed, it's possible to
set a threshold to prevent the object from rendering semi-transparent pixels
using the alpha scissor option.

.. image:: img/spatial_material12.png

This renders the object via the opaque pipeline when opaque pre-pass is on,
which is faster and allows it to use mid- and post-process effects such as
SSAO, SSR, etc.

Blend Mode
~~~~~~~~~~

Controls the blend mode for the material. Keep in mind that any mode
other than *Mix* forces the object to go through the transparent pipeline.

* **Mix:** Default blend mode, alpha controls how much the object is visible.
* **Add:** The final color of the object is added to the color of the screen,
  nice for flares or some fire-like effects.
* **Sub:** The final color of the object is subtracted from the color of the
  screen.
* **Mul:** The final color of the object is multiplied with the color of the
  screen.

.. image:: img/spatial_material8.png

Cull Mode
~~~~~~~~~

Determines which side of the object is not drawn when backfaces are rendered:

* **Back:** The back of the object is culled when not visible (default).
* **Front:** The front of the object is culled when not visible.
* **Disabled:** Used for objects that are double-sided (no culling is performed).

.. note::

  By default, Blender has backface culling disabled on materials and will
  export materials to match how they render in Blender. This means that
  materials in Godot will have their cull mode set to **Disabled**. This can
  decrease performance since backfaces will be rendered, even when they are
  being culled by other faces. To resolve this, enable **Backface Culling** in
  Blender's Materials tab, then export the scene to glTF again.

Depth Draw Mode
~~~~~~~~~~~~~~~

Specifies when depth rendering must take place.

* **Opaque Only (default):** Depth is only drawn for opaque objects.
* **Always:** Depth draw is drawn for both opaque and transparent objects.
* **Never:** No depth draw takes place
  (do not confuse this with the No Depth Test option above).
* **Depth Pre-Pass:** For transparent objects, an opaque pass is made first
  with the opaque parts, then transparency is drawn above.
  Use this option with transparent grass or tree foliage.

.. image:: img/material_depth_draw.png

No Depth Test
~~~~~~~~~~~~~

In order for close objects to appear over far away objects, depth testing
is performed. Disabling it has the result of objects appearing over
(or under) everything else.

Disabling this makes the most sense for drawing indicators in world space,
and works very well with the *Render Priority* property of Material
(see the bottom of this page).

.. image:: img/spatial_material3.png

Shading
-------

Shading mode
~~~~~~~~~~~~

Godot has a more or less uniform cost per pixel thanks to depth pre-pass. All
lighting calculations are made by running the lighting shader on every pixel.

As these calculations are costly, performance can be brought down considerably
in some corner cases such as drawing several layers of transparency (which is
common in particle systems). Switching to per-vertex lighting may help in these
cases.

Additionally, on low-end or mobile devices, switching to vertex lighting
can considerably increase rendering performance.

.. image:: img/spatial_material2.png

Keep in mind that when vertex lighting is enabled, only directional lighting
can produce shadows (for performance reasons).

However, in some cases you might want to show just the albedo (color) and
ignore the rest. To do this you can set the shading mode to unshaded

.. image:: img/spatial_material26.png

Diffuse Mode
~~~~~~~~~~~~

Specifies the algorithm used by diffuse scattering of light when hitting
the object. The default is *Burley*. Other modes are also available:

* **Burley:** Default mode, the original Disney Principled PBS diffuse algorithm.
* **Lambert:** Is not affected by roughness.
* **Lambert Wrap:** Extends Lambert to cover more than 90 degrees when
  roughness increases. Works great for hair and simulating cheap
  subsurface scattering. This implementation is energy conserving.
* **Oren Nayar:** This implementation aims to take microsurfacing into account
  (via roughness). Works well for clay-like materials and some types of cloth.
* **Toon:** Provides a hard cut for lighting, with smoothing affected by roughness.
  It is recommended you disable sky contribution from your environment's
  ambient light settings or disable ambient light in the StandardMaterial3D
  to achieve a better effect.

.. image:: img/spatial_material6.png

Specular Mode
~~~~~~~~~~~~~

Specifies how the specular blob will be rendered. The specular blob
represents the shape of a light source reflected in the object.

* **SchlickGGX:** The most common blob used by PBR 3D engines nowadays.
* **Blinn:** Common in previous-generation engines.
  Not worth using nowadays, but left here for the sake of compatibility.
* **Phong:** Same as above.
* **Toon:** Creates a toon blob, which changes size depending on roughness.
* **Disabled:** Sometimes the blob gets in the way. Begone!

.. image:: img/spatial_material7.png

Disable Ambient Light
~~~~~~~~~~~~~~~~~~~~~

Makes the object not receive any kind of ambient lighting that would
otherwise light it.

Vertex Color
------------

This setting allows choosing what is done by default to vertex colors that come
from your 3D modelling application. By default, they are ignored.

.. image:: img/spatial_material4.png

Use as Albedo
~~~~~~~~~~~~~

Choosing this option means vertex color is used as albedo color.

Is sRGB
~~~~~~~

Most 3D modeling software will likely export vertex colors as sRGB, so toggling
this option on will help them look correct.

Albedo
------

*Albedo* is the base color for the material, on which all the other settings
operate. When set to *Unshaded*, this is the only color that is visible. In
previous versions of Godot, this channel was named *Diffuse*. The change
of name mainly happened because, in PBR (Physically Based Rendering), this color affects many
more calculations than just the diffuse lighting path.

Albedo color and texture can be used together as they are multiplied.

*Alpha channel* in albedo color and texture is also used for the
object transparency. If you use a color or texture with *alpha channel*,
make sure to either enable transparency or *alpha scissoring* for it to work.

Metallic
--------

Godot uses a metallic model over competing models due to its simplicity.
This parameter defines how reflective the material is. The more reflective, the
less diffuse/ambient light affects the material and the more light is reflected.
This model is called "energy-conserving".

The *Specular* parameter is a general amount for the reflectivity (unlike
*Metallic*, this is not energy-conserving, so leave it at ``0.5`` and don't touch
it unless you need to).

The minimum internal reflectivity is ``0.04``, so it's impossible to make a
material completely unreflective, just like in real life.

.. image:: img/spatial_material13.png

Roughness
---------

*Roughness* affects the way reflection happens. A value of ``0`` makes it a
perfect mirror while a value of ``1`` completely blurs the reflection (simulating
natural microsurfacing). Most common types of materials can be achieved with
the right combination of *Metallic* and *Roughness*.

.. image:: img/spatial_material14.png

Emission
--------

*Emission* specifies how much light is emitted by the material (keep in mind this
does not include light surrounding geometry unless :ref:`VoxelGI <doc_using_voxel_gi>`
or :ref:`SDFGI <doc_using_sdfgi>` are used). This value is added to the resulting
final image and is not affected by other lighting in the scene.

.. image:: img/spatial_material15.png

Normal map
----------

Normal mapping allows you to set a texture that represents finer shape detail.
This does not modify geometry, only the incident angle for light. In Godot,
only the red and green channels of normal maps are used for better compression
and wider compatibility.

.. image:: img/spatial_material16.png

.. note::

  Godot requires the normal map to use the X+, Y+ and Z+ coordinates, this is
  known as OpenGL style. If you've imported a material made to be used with
  another engine it may be DirectX style, in which case the normal map needs to
  be converted so its Y axis is flipped.

  More information about normal maps (including a coordinate order table for
  popular engines) can be found
  `here <http://wiki.polycount.com/wiki/Normal_Map_Technical_Details>`__.

Rim
---

Some fabrics have small micro-fur that causes light to scatter around it. Godot
emulates this with the *Rim* parameter. Unlike other rim lighting implementations,
which just use the emission channel, this one actually takes light into account
(no light means no rim). This makes the effect considerably more believable.

.. image:: img/spatial_material17.png

Rim size depends on roughness, and there is a special parameter to specify how
it must be colored. If *Tint* is ``0``, the color of the light is used for the
rim. If *Tint* is ``1``, then the albedo of the material is used. Using
intermediate values generally works best.

Clearcoat
---------


The *Clearcoat* parameter is used to add a secondary pass of transparent coat
to the material. This is common in car paint and toys. In practice, it's a
smaller specular blob added on top of the existing material.

.. image:: img/clearcoat_comparison.png

Anisotropy
----------


This changes the shape of the specular blob and aligns it to tangent space.
Anisotropy is commonly used with hair, or to make materials such as brushed
aluminum more realistic. It works especially well when combined with flowmaps.

.. image:: img/spatial_material18.png

Ambient Occlusion
-----------------

It is possible to specify a baked ambient occlusion map. This map affects how
much ambient light reaches each surface of the object (it does not affect direct
light by default). While it is possible to use Screen-Space Ambient Occlusion
(SSAO) to generate ambient occlusion, nothing beats the quality of a well-baked
AO map. It is recommended to bake ambient occlusion whenever possible.

.. image:: img/spatial_material19.png

Height
------


Setting a depth map on a material produces a ray-marched search to emulate the
proper displacement of cavities along the view direction. This is not real
added geometry, but an illusion of depth. It may not work for complex objects,
but it produces a realistic depth effect for textures. For best results,
*Depth* should be used together with normal mapping.

.. image:: img/spatial_material20.png

Subsurface Scattering
---------------------


This effect emulates light that penetrates an object's surface, is scattered,
and then comes out. It is useful to create realistic skin, marble, colored
liquids, etc.

.. image:: img/spatial_material21.png

Back Lighting
-------------

This controls how much light from the lit side (visible to light) is transferred
to the dark side (opposite from the light). This works well for thin objects
such as plant leaves, grass, human ears, etc.

Refraction
----------


When refraction is enabled, it supersedes alpha blending, and Godot attempts to
fetch information from behind the object being rendered instead. This allows
distorting the transparency in a way similar to refraction in real life.

.. image:: img/spatial_material23.png

Detail
------

Godot allows using secondary albedo and normal maps to generate a detail
texture, which can be blended in many ways. By combining this with secondary
UV or triplanar modes, many interesting textures can be achieved.

.. image:: img/spatial_material24.png

There are several settings that control how detail is used.

Mask: The detail mask is a black and white image used to control where the
blending takes place on a texture. White is for the detail textures, Black
is for the regular material textures, different shades of gray are for
partial blending of the material textures and detail textures.

Blend Mode: These four modes control how the textures are blended together.

- Mix: Combines pixel values of both textures. At black, only show the material texture,
  at white, only show the detail texture. Values of gray create a smooth blend between
  the two.

- Add: Adds pixel values of one Texture with the other. Unlike mix mode
  both textures are completely mixed at white parts of a mask and not at gray
  parts. The original texture is mostly unchanged at black

- Sub: Subtracts pixel values of one texture with the other. The second
  texture is completely subtracted at white parts of a mask with only a little
  subtraction in black parts, gray parts being different levels of subtraction
  based on the exact texture.

- Mul: Multiplies the RGB channel numbers for each pixel from the top texture
  with the values for the corresponding pixel from the bottom texture.

Albedo: This is where you put an albedo texture you want to blend. If nothing
is in this slot it will be interpreted as white by default.

Normal: This is where you put a normal texture you want to blend. If nothing is
in this slot it will be interpreted as a flat normal map. This can still be used
even if the material does not have normal map enabled.

UV1 and UV2
-----------

Godot supports two UV channels per material. Secondary UV is often useful for
ambient occlusion or emission (baked light). UVs can be scaled and offset,
which is useful when using repeating textures.

.. _doc_standard_material_3d_triplanar_mapping:

Triplanar Mapping
~~~~~~~~~~~~~~~~~

Triplanar mapping is supported for both UV1 and UV2. This is an alternative way
to obtain texture coordinates, sometimes called "Autotexture". Textures are
sampled in X, Y and Z and blended by the normal. Triplanar mapping can be
performed in either world space or object space.

In the image below, you can see how all primitives share the same material with
world triplanar, so the brick texture continues smoothly between them.

.. image:: img/spatial_material25.png

World Triplanar
~~~~~~~~~~~~~~~

When using triplanar mapping, it is computed in object local space. This
option makes it use world space instead.

.. _doc_standard_material_3d_sampling:

Sampling
--------

Filter
~~~~~~

The filtering method for the textures used by the material. See :ref:`this page<class_BaseMaterial3D_property_texture_filter>`
for a full list of options and their description.

Repeat
~~~~~~

if the textures used by the material repeat, and how they repeat. See :ref:`this page<class_BaseMaterial3D_property_texture_repeat>`
for a full list of options and their description.

Shadows
-------

Do Not Receive Shadows
~~~~~~~~~~~~~~~~~~~~~~

Makes the object not receive any kind of shadow that would otherwise
be cast onto it.

Use Shadow to Opacity
~~~~~~~~~~~~~~~~~~~~~

Lighting modifies the alpha so shadowed areas are opaque and non-shadowed
areas are transparent. Useful for overlaying shadows onto a camera feed in AR.

Billboard
---------

Billboard Mode
~~~~~~~~~~~~~~

Enables billboard mode for drawing materials. This controls how the object
faces the camera:

* **Disabled:** Billboard mode is disabled.
* **Enabled:** Billboard mode is enabled, the object's -Z axis will always
  face the camera.
* **Y-Billboard:** The object's X axis will always be aligned with the camera.
* **Particles:** Most suited for particle systems, because it allows
  specifying animation options.

.. image:: img/spatial_material9.png

The above options are only enabled for Particle Billboard.

Billboard Keep Scale
~~~~~~~~~~~~~~~~~~~~

Enables scaling a mesh in billboard mode.

Grow
----

Grows the object vertices in the direction pointed by their normals:

.. image:: img/spatial_material10.png

This is commonly used to create cheap outlines. Add a second material pass,
make it black and unshaded, reverse culling (Cull Front), and add some grow:

.. image:: img/spatial_material11.png

Transform
---------

Fixed Size
~~~~~~~~~~

This causes the object to be rendered at the same size no matter the distance.
This is useful mostly for indicators (no depth test and high render priority)
and some types of billboards.

Use Point Size
~~~~~~~~~~~~~~~

This option is only effective when the geometry rendered is made of points
(generally it's made of triangles when imported from 3D modeling software). If
so, then those points can be resized (see below).

Point Size
~~~~~~~~~~

When drawing points, specify the point size in pixels.

Transmission
~~~~~~~~~~~~

This controls how much light from the lit side (visible to light) is transferred
to the dark side (opposite from the light). This works well for thin objects
such as plant leaves, grass, human ears, etc.

.. image:: img/spatial_material22.png

Proximity and Distance Fade
---------------------------

Godot allows materials to fade by proximity to each other as well as depending
on the distance from the viewer. Proximity fade is useful for effects such as
soft particles or a mass of water with a smooth blending to the shores.

.. image:: img/spatial_material_proxfade.gif

Distance fade is useful for light shafts or indicators that are only present
after a given distance.

Keep in mind enabling proximity fade or distance fade with **Pixel Alpha** mode
enables alpha blending. Alpha blending is more GPU-intensive and can cause
transparency sorting issues. Alpha blending also disables many material
features such as the ability to cast shadows.
To hide a character when they get too close to the camera, consider using
**Pixel Dither** or better, **Object Dither** (which is even faster than
**Pixel Dither**).

Material Settings
-----------------

Render priority
---------------

The rendering order of objects can be changed, although this is mostly
useful for transparent objects (or opaque objects that perform depth draw
but no color draw, such as cracks on the floor).

Next Pass
---------

Sets the material to be used for the next pass. This renders the object
again with a different material.
