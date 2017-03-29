.. _doc_lighting:

Lighting
========

Introduction
------------

Lights emit light that mix with the materials and produces a visible
result. Light can come from several types of sources in a scene:

-  From the Material itself, in the form of the emission color (though
   it does not affect nearby objects unless baked).
-  Light Nodes: Directional, Omni and Spot.
-  Ambient Light in the
   :ref:`Environment <class_Environment>`.
-  Baked Light (read :ref:`doc_light_baking`).

The emission color is a material property. You can read more about it
in the :ref:`doc_fixed_materials` tutorial.

Light nodes
-----------

As mentioned before, there are three types of light nodes: Directional,
Omni and Spot. Each has different uses and will be described in
detail below, but first let's take a look at the common parameters for
lights:

.. image:: /img/light_params.png

Each one has a specific function:

-  **Enabled**: Light is emitted only if this flag is set.
-  **Bake Mode**: When using the light baker, the role of this light can
   be defined in this enumerator. The role will be followed even if the
   light is disabled, which allows to configure a light and then disable
   it for baking.
-  **Energy**: This value is a multiplier for the light, it's specially
   useful for :ref:`doc_high_dynamic_range` and for Spot and Omni lights, because it can
   create very bright spots near the emitter.
-  **Diffuse and Specular**: These light values get multiplied by the
   material light and diffuse colors. A white value does not mean
   that light will be white, but that the material color will be kept.
-  **Operator**: It is possible to make some lights negative for a
   darkening effect.
-  **Projector**: Lights can project a texture for the diffuse light
   (currently only supported in Spot light).

Directional light
~~~~~~~~~~~~~~~~~

This is the most common type of light and represents a light source 
very far away (such as the sun). It is also
the cheapest light to compute and should be used whenever possible
(although it's not the cheapest shadow-map to compute, but more on that
later). 

Directional light models an infinite number of parallel light rays
covering the whole scene. The directional light node is represented by a big arrow, which
indicates the direction of the light rays. However, the position of the node
does not affect the lighting at all, and can be anywhere.

.. image:: /img/light_directional.png

Every face whose front-side is hit by the light rays is lit, the others stay dark.
Most light types
have specific parameters but directional lights are pretty simple in
nature so they don't.

Omni light
~~~~~~~~~~

Omni light is a point source that emits light spherically in all directions up to a given
radius (distance from the node's position). The radius is a parameter of the light and
can be controlled by the user. Just as in real life, the intensity of omni light
decreases with the distance and vanishes at the defined radius. Omni light sources
should be used to represent lamps or bulbs or any other light source that originates
approximately in a point.

.. image:: /img/light_omni.png

In reality, the attenuation of omni light is proportional to the squared distance
from the point source. This can be easily understood if you imagine a sphere around
the omni light with a certain radius. No matter how large the sphere is, the number
of rays passing through it is always the same. If the radius of the sphere is doubled,
the area of the sphere increases by four. In other words, the density of rays
(the number of rays per square area) decreases quadratically with the distance.

Inverse-quadratic attenuation curves are inconvenient for artists: they
never reach zero and have almost infinitely large values near the emitter.
So Godot simulates omni light with an artist-controlled exponential curve
instead.

.. image:: /img/light_attenuation.png

Spot light
~~~~~~~~~~

Spot lights are similar to omni lights, except they emit light only into a cone
(or "cutoff"). They are useful to simulate flashlights,
car lights, etc. This kind of light is also attenuated towards the
opposite direction it points to.

.. image:: /img/light_spot.png

Ambient light
-------------

Ambient light can be found in the properties of a WorldEnvironment
(remember only one of such can be instanced per scene). Ambient light
consists of a uniform light and energy. This light is applied the same
to every single pixel of the rendered scene, except to objects that used
baked light.

Baked light
-----------

Baked light stands for pre-computed ambient light. It can serve multiple
purposes, such as baking light emitters that are not going to be used in
real-time, and baking light bounces from real-time lights to add more
realism to a scene (see :ref:`doc_light_baking` tutorial for more information).
