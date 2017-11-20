.. _doc_reflection_probes:

Reflection Probes
=========

Introduction
------------

As stated in the :ref:`doc_spatial_materials`, objects can show reflected or diffuse light.
Reflection Probes are used as a source of reflected and ambient light for objects inside their area of influence.

A probe of this type captures the surroundings (as a sort of 360 degrees image), and stores versions
of it with increasing levels of *blur*. This is used to simulate roughness in materials, as well as ambient lighting.

While these probes are a very efficient way of storing reflections, they have a few shortcomings:

* They are efficient to render, but expensive to compute. This leads to a default behavior where they only capture on scene load.
* They work best for rectangular shaped rooms or places, otherwise the reflections shown are not as faithful (specially when roughness is 0).

Setting Up
----------

Setting up reflection probes is really easy! Just create a ReflectionProbe node, and wrap it around the area where you want to have reflections:

.. image:: /img/refprobe_setup.png

This should result in immediate local reflections. If you are using a Sky texture, reflections are by default blended. with it. 

By default, or interiors, reflections may appear to not have much consistence. In this scenario, make sure to tick the *"Box Correct"* property.

.. image:: /img/refprobe_box_property.png


This setting changes the reflection from an infinite skybox to reflecting a box the size of the probe:

.. image:: /img/refprobe_boxcorrect.png

Adjusting the box walls may help improve the reflection a bit, but it will always look the best in box shaped rooms.

The probe captures the surrounding from the center of the gizmo. If, for some reason, the room shape or contents occlude the center, it
can be displaced to an empty place by moving the handles in the center:

.. image:: /img/refprobe_center_gizmo.png

By default, shadow mapping is disabled when rendering probes (only in the rendered image inside the probe, not the actual scene). This is
a simple way to save on performance and memory. If you really want shadows in the probe, they can be toggled on/of with the *Enable Shadow* setting:

.. image:: /img/refprobe_shadows.png

Finally, keep in mind that you may not want the Reflection Probe to render some objects. A typical scenario is an enemy inside the room which will
move around. To keep objects from being rendered in the reflections, use the *Cull Mask* setting:

.. image:: /img/refprobe_cullmask.png

Interior vs Exterior
--------------------

If you are using reflection probes in an interior setting, it is recommended that the **Interior** property is enabled. This makes
the probe not render the sky, and also allows custom amibent lighting settings.

.. image:: /img/refprobe_cullmask.png

When probes are set to **Interior**, custom constant ambient lighting can be specified per probe. Just choose a color and an energy.
Optionally, you can blend this ambient light with the probe diffuse capture by tweaking the **Ambient Contribution* property (0.0 means, pure ambient color, while 1.0 means pure diffuse capture).


Blending
--------

Multiple reflection probes can be used and Godot will blend them where they overlap using a smart algorithm:

.. image:: /img/refprobe_blending.png

As you can see, this blending is never perfect (after all, these are box reflections, not real reflections), but these arctifacts
are only visible when using perfectly mirrored reflections. Normally, scenes have normal mapping and varying levels of roughness which
can hide this. 

Alternatively, Reflection Probes work very well blended together with Screen Space Reflections to solve these problems. Combining them makes local reflections appear
more faithful, while probes only used as fallback when no screen-sace information is found:

.. image:: /img/refprobe_ssr.png

Finally, blending interior and exterior probes is a recommended approach when making levels that combine both interiors and exteriors. Near the door, a probe can
be marked as *exterior* (so it will get sky reflections), while on the inside it can be interior.

Reflection Atlas
-----------------

In the current renderer implementation, all probes are the same size and they are fit into a Reflection Atlas. The size and amount of probes can be
customized in Project Settings -> Quality -> Reflections

.. image:: /img/refprobe_atlas.png










Materials can be applied to most visible 3D objects. Basically they
describe how light interacts with that object. There are many
types of materials, but the main ones are the
:ref:`FixedMaterial <class_FixedMaterial>` and the
:ref:`ShaderMaterial <class_ShaderMaterial>`.
Tutorials for each of them exist :ref:`doc_fixed_materials` and :ref:`doc_shader_materials`.

This tutorial is about the basic properties shared between them.

.. image:: /img/material_flags.png

Flags
-----

Materials, no matter which type they are, have an associated set of flags.
Their use will be explained in the following.

Visible
~~~~~~~

Toggles whether the material is visible. If unchecked, the object will
not be shown.

Double sided & inverted faces
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Godot by default only shows geometry faces (triangles) when their front-side
faces the camera. If looking at the front-side of a face, its vertices
have to be oriented clockwise by definition. For closed objects, the
back-side of faces is never visible because they are hidden by other
faces. SO not drawing invisible triangles (whose vertices are oriented
counter-clockwise on the view plane) saves a lot of GPU power.

However, for flat or open objects, the back-side of faces might be visible
and needs to be drawn as well. The "double sided" flag makes sure that no matter the facing,
the triangle will always be drawn. It is also possible to invert this
check and draw only counter-clockwise looking faces, though it's not
very useful except for a few cases (like drawing outlines).

Unshaded
~~~~~~~~

Objects are always black unless light affects them, and their shading
changes according to the type and direction of lights. When this flag is
turned on, the diffuse color is displayed right the same as it appears
in the texture or parameter:

.. image:: /img/material_unshaded.png

On top
~~~~~~

When this flag is turned on, the object will be drawn after everything
else has been drawn and without a depth test. This is generally useful
for objects which shall never be hidden by other objects such as HUD effects
or gizmos.

Ligthmap on UV2
~~~~~~~~~~~~~~~

When using lightmapping (see the :ref:`doc_light_baking` tutorial), this option
determines that the lightmap should be accessed on the UV2 array instead
of regular UV.

Parameters
----------

Some parameters also exist for controlling drawing and blending:

Blend mode
~~~~~~~~~~

Objects are usually blended in Mix mode. Other blend modes (Add and Sub)
exist for special cases (usually particle effects, light rays, etc.) but
materials can be set to them:

.. image:: /img/fixed_material_blend.png

Line width
~~~~~~~~~~

When drawing lines, the size of them can be adjusted here per material.

Depth draw mode
~~~~~~~~~~~~~~~

This is a tricky but very useful setting. By default, opaque objects are
drawn using the depth buffer and translucent objects are not (but are
sorted by depth). This behavior can be changed here. The options are:

-  **Always**: Draw objects with depth always, even those with alpha.
   This often results in glitches like the one in the first image (which
   is why it's not the default).
-  **Opaque Only**: Draw objects with depth only when they are opaque,
   and do not set depth for alpha. This is the default because it's fast,
   but it's not the most correct setting. Objects with transparency that
   self-intersect will always look wrong, especially those that mix
   opaque and transparent areas, like grass, tree leaves, etc. Objects
   with transparency also can't cast shadows, this is evident in the
   second image.
-  **Alpha Pre-Pass**: The same as above, but a depth pass is performed
   for the opaque areas of objects with transparency. This makes objects
   with transparency look much more correct. In the third image it is
   evident how the leaves cast shadows between them and into the floor.
   This setting is turned off by default because, while on PC this is
   not very costly, mobile devices suffer a lot when this setting is
   turned on, so use it with care.
-  **Never**: Never use the depth buffer for this material. This is
   mostly useful in combination with the "On Top" flag explained above.

.. image:: /img/material_depth_draw.png
