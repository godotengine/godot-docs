.. _doc_spatial_material:

Spatial Material
================

Introduction
------------

For Godot 3, instead of following the trend and focusing on shader graphs,
we put in most of the work offering a default material that covers far
more use cases. This replaces the old "FixedMaterial" in Godot 2.x

SpatialMaterial is a 3D material and aims to have most features
artists look for in a material. Additionally, it can be converted
to shader code and be further modified if desired.

This tutorial will attempt to cover most parameters present in SpatialMaterial.

Flags
-----

Spatial materials have many flags determining the general usage of a material.

.. image:: img/spatial_material1.png

Transparent
~~~~~~~~~~~

In Godot, materials are not transparent unless specifically toggled as such.
The main reason behind this is that transparent materials are rendered
using a different technique (sorted from back to front and rendered in order).

This technique is less efficient (many state changes happen) and makes the materials
unusable with many mid and post processing effects (such as SSAO, SSR, etc) that
require perfectly opaque geometry.

For this reason, materials in Godot are assumed opaque unless specified otherwise.
The main settings that enable transparency are:

* Transparent flag (this one)
* Blend mode set to other than Mix
* Enabling distance or proximity fade

Unshaded
~~~~~~~~

In most cases, it is common for materials to be affected by lighting (shaded).

Sometimes, however, one might want to show just the albedo (color) and ignore the rest. Toggling this flag on will remove all
shading and show pure, unlit, color.

.. image:: img/spatial_material26.png

Vertex Lighting
~~~~~~~~~~~~~~~

Godot has a more or less uniform cost per pixel (thanks to depth pre pass), all lighting calculations are made
by running the lighting shader on every pixel.

As these calculations are costly, performance can be brought down considerably in some corner cases such as drawing
several layers of transparency (common in particle systems). Switching to per vertex lighting may help these cases.

Additionally, on very low end devices such as mobile, switching to vertex lighting can considerably increase rendering performance.


.. image:: img/spatial_material2.png

Keep in mind that, when vertex lighting is enabled, only directional lighting can produce shadows (for performance reasons).

No Depth Test
~~~~~~~~~~~~~

In order for close objects to appear over far away objects, depth testing is performed.
Disabling it has the result of objects appearing over (or under) everything else.

Disabling this makes the most sense for drawing indicators in world space, and works
very well with the "render priority" property of Material (see bottom).

.. image:: img/spatial_material3.png

Use Point Size
~~~~~~~~~~~~~~~

This option is only active when the geometry rendered is made of points (it generally is just made of triangles when imported from 3D DCCs).
If so, then points can be sized (see below).

World Triplanar
~~~~~~~~~~~~~~~

When using triplanar mapping (see below, in the UV1 and UV2 settings) triplanar is computed in object local space. This option
makes triplanar work in world space.

Fixed Size
~~~~~~~~~~

Makes the object rendered at the same size no matter the distance. This is, again, useful mostly for indicators (no depth test and high render priority)
and some types of billboards.

Vertex Color
------------

This menu allows choosing what is done by default to vertex colors that come from your 3D modelling application. By default, they are ignored.

.. image:: img/spatial_material4.png

Use as Albedo
~~~~~~~~~~~~~

Vertex color is used as albedo color.

Is SRGB
~~~~~~~

Most 3D DCCs will likely export vertex colors as SRGB, so toggling this option on will help them
look correct.


Parameters
-----------

SpatialMaterial also has several configurable parameters to tweak many aspects of the rendering:

.. image:: img/spatial_material5.png

Diffuse Mode
~~~~~~~~~~~~

Specifies the algorithm used by diffuse scattering of light when hitting the object. The
default one is Burley. Other modes are also available:

* **Burley:** Default mode, the original Disney Principled PBS diffuse algorithm.
* **Lambert:** Is not affected by roughness.
* **Lambert Wrap:** Extends Lambert to cover more than 90 degrees when roughness increases. Works great for hair and simulating cheap subsurface scattering. This implementation is energy conserving.
* **Oren Nayar:** This implementation aims to take microsurfacing into account (via roughness). Works really well for clay-like materials and some types of cloth.
* **Toon:** Provides a hard cut for lighting, with smoothing affected by roughness.

.. image:: img/spatial_material6.png

Specular Mode
~~~~~~~~~~~~~

Specifies how the specular blob will be rendered. The specular blob represents the shape of a light source reflected in the object.

* **ShlickGGX:** The most common blob used by PBR 3D engines nowadays.
* **Blinn:** Common in previous-generation engines. Not worth using nowadays, but left here for the sake of compatibility.
* **Phong:** Same as above.
* **Toon:** Creates a toon blob, which changes size depending on roughness.
* **Disabled:** Sometimes, that blob gets in the way. Be gone!

.. image:: img/spatial_material7.png


Blend Mode
~~~~~~~~~~

Controls the blend mode for the material. Keep in mind that any mode other than Mix forces the object to go through transparent pipeline.

* Mix: Default blend mode, alpha controls how much the object is visible.
* Add: Object is blended additively, nice for flares or some fire-like effects.
* Sub: Object is subtracted.
* Mul: Object is multiplied.

.. image:: img/spatial_material8.png

Cull Mode
~~~~~~~~~

Determines which side of the object is not drawn when back-faces are rendered:

* Back: Back of the object is culled when not visible (default)
* Front: Front of the object is culled when not visible
* Disabled: Used for objects that are double sided (no culling is performed)

Depth Draw Mode
~~~~~~~~~~~~~~~

Specifies when depth rendering must take place.

* Opaque Only (default): Depth is only drawn for opaque objects
* Always: Depth draw is drawn for both opaque and transparent objects
* Never: No depth draw takes place (note: do not confuse with depth test option above)
* Depth Pre-Pass: For transparent objects, an opaque pass is made first with the opaque parts,
  then tranparency is drawn above. Use this option with transparent grass or tree foliage.

.. image:: img/material_depth_draw.png

Line Width
~~~~~~~~~~

When drawing lines, specify the width of the lines being drawn. This option is not available in most modern hardware.

Point Size
~~~~~~~~~~

When drawing points, specify the point size in pixels.

Billboard Mode
~~~~~~~~~~~~~~

Enables billboard mode for drawing materials. This control how the object faces the camera:

* Disabled: Billboard mode is disabled
* Enabled: Billboard mode is enabled, object -Z axis will always face the camera.
* Y-Billboard: Object X axis will always be aligned with the camera
* Particles: When using particle systems, this type of billboard is best, because it allows specifying animation options.

.. image:: img/spatial_material9.png

Above options are only enabled for Particle Billboard.

Grow
~~~~

Grows the object vertices in the direction pointed by their normals:

.. image:: img/spatial_material10.png

This is commonly used to create cheap outlines. Add a second material pass, make it black an unshaded, reverse culling (Cull Front), and
add some grow:

.. image:: img/spatial_material11.png


Use Alpha Scissor
~~~~~~~~~~~~~~~~~

When transparency other than 0 or 1 is not needed, it's possible to set a threshold to avoid the object from rendering these pixels.

.. image:: img/spatial_material12.png

This renders the object via the opaque pipeline, which is faster and allows it to do mid and post process effects such as SSAO, SSR, etc.

Material colors, maps and channels
----------------------------------

Besides the parameters, what defines materials themselves are the colors, textures and channels. Godot supports a very extensive list
of them (arguably far more than any of the other prominent game engines). They will be described in detail below:

Albedo
~~~~~~

Albedo is the base color for the material. Everything else works based on it. When set to *unshaded* this is the only color that is visible as-is.
In previous versions of Godot, this channel was named *diffuse*. The change of name mainly happens because, in PBR rendering, this color affects many more
calculations than just the diffuse lighting path.

Albedo color and texture can be used together, as they are multiplied.

*Alpha channel* in albedo color and texture is also used for the object transparency. If you use a color or texture with *alpha channel*, make sure to either enable
transparency or *alpha scissoring* for it to work.

Metallic
~~~~~~~~

Godot uses a Metallic model over competing models due to it's simplicity. This parameter pretty much defines how reflective the materials is. The more reflective it is, the least diffuse/ambient
light and the more reflected light. This model is called "energy conserving".

The "specular" parameter here is just a general amount of for the reflectivity (unlike *metallic*, this one is not energy conserving, so simply leave it as 0.5 and don't touch it unless you need to).

The minimum internal reflectivity is 0.04, so (just like in real life) it's impossible to make a material completely unreflective.

.. image:: img/spatial_material13.png

Roughness
~~~~~~~~~

Roughness affects mainly the way reflection happens. A value of 0 makes it a perfect mirror, while a value of 1 completely blurs the reflection (simulating the natural microsurfacing).
Most common types of materials can be achieved from the right combination of *Metallic* and *Roughness*.

.. image:: img/spatial_material14.png

Emission
~~~~~~~~

Emission specifies how much light is emitted by the material (keep in mind this does not do lighting on surrounding geometry unless GI Probe is used). This value is just added to the resulting
final image, and is not affected by other lighting in the scene.


.. image:: img/spatial_material15.png


Normalmap
~~~~~~~~~

Normal mapping allows to set a texture that represents finer shape detail. This does not modify geometry, just the incident angle for light.
In Godot, only R and G are used for normalmaps, in order to attain better compatibility.

.. image:: img/spatial_material16.png

Rim
~~~

Some fabrics have small micro fur that causes light to scatter around it. Godot emulates this with the *rim* parameter. Unlike other rim lighting implementations
which just use the emission channel, this one actually takes light into account (no light means no rim). This makes the effect considerably more believable.

.. image:: img/spatial_material17.png

Rim size depends on roughness and there is a special parameter to specify how it must be colored. If *tint* is 0, the color of the light is used for the rim. If *tint* is 1,
then the albedo of the material is used. Using intermediate values generally works best.

Clearcoat
~~~~~~~~~

The *clearcoat* parameter is used mostly to add a *secondary* pass of transparent coat to the material. This is very common in car paint and toys.
In practice, it's a smaller specular blob added on top of the existing material.

Anisotropy
~~~~~~~~~~

Changes the shape of the specular blow and aligns it to tangent space. Anisotropy is commonly used with hair, or to make materials such as brushed aluminium more realistic.
It works especially well when combined with flowmaps.

.. image:: img/spatial_material18.png


Ambient Occlusion
~~~~~~~~~~~~~~~~~~

In Godot's new PBR workflow, it is possible to specify a pre-baked ambient occlusion map. This map affects how much ambient light reaches each surface of the object (it does not affect direct light).
While it is possible to use Screen Space Ambient Occlusion (SSAO) to generate AO, nothing will beat the quality of a nicely baked AO map. It is recommended to pre-bake AO whenever possible.

.. image:: img/spatial_material19.png

Depth
~~~~~

Setting a depth map to a material produces a ray-marched search to emulate the proper displacement of cavities along the view direction. This is not real added geometry, but an illusion of depth.
It may not work for complex objets, but it produces a realistic depth effect for textues. For best results, *Depth* should be used together with normal mapping.

.. image:: img/spatial_material20.png

Subsurface Scattering
~~~~~~~~~~~~~~~~~~~~~

This effect emulates light that goes beneath an object's surface, is scattered, and then comes out. It's very useful to make realistic skin, marble, colored liquids, etc.

.. image:: img/spatial_material21.png


Transmission
~~~~~~~~~~~~

Controls how much light from the lit side (visible to light) is transferred to the dark side (opposite side to light). This works very well for thin objects such as tree/plant leaves,
grass, human ears, etc.

.. image:: img/spatial_material22.png

Refraction
~~~~~~~~~~~

When refraction is enabled, it supersedes alpha blending and Godot attempts to fetch information from behind the object being rendered instead. This allows distorting the transparency
in a way very similar to refraction.

.. image:: img/spatial_material23.png

Detail
~~~~~~

Godot allows using secondary albedo and normal maps to generate a detail texture, which can be blended in many ways. Combining with secondary UV or triplanar modes, many interesting textures can be achieved.

.. image:: img/spatial_material24.png

UV1 and UV2
~~~~~~~~~~~~

Godot supports 2 UV channels per material. Secondary UV is often useful for AO or Emission (baked light). UVs can be scaled and offseted, which is useful in textures with repeat.

Triplanar Mapping
~~~~~~~~~~~~~~~~~

Triplanar mapping is supported for both UV1 and UV2. This is an alternative way to obtain texture coordinates, often called "Autotexture". Textures are sampled in X,Y and Z and blended by the normal.
Triplanar can be either worldspace or object space.

In the image below, you can see how all primitives share the same material with world triplanar, so bricks continue smoothly between them.

.. image:: img/spatial_material25.png

Proximity and Distance Fade
----------------------------

Godot allows materials to fade by proximity to another, as well as depending on the distance to the viewer.
Proximity fade is very useful for effects such as soft particles, or a mass of water with a smooth blending to the shores.
Distance fade is useful for light shafts or indicators that are only present after a given distance.

Keep in mind enabling these enables alpha blending, so abusing them for a whole scene is not generally a good idea.

.. image:: img/spatial_material_proxfade.gif

Render Priority
---------------

Rendering order can be changed for objects, although this is mostly useful for transparent objects (or opaque objects that do depth draw but no color draw, useful for cracks on the floor).
