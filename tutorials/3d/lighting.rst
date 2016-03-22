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

The emission color is a material property, as seen in the previous
tutorials about materials (go read them if you didn't at this point!).

Light nodes
-----------

As mentioned before, there are three types of light nodes: Directional,
Ambient and Spot. Each has different uses and will be described in
detail below, but first let's take a look at the common parameters for
lights:

.. image:: /img/light_params.png

Each one has a specific function:

-  **Enabled**: Lights can be disabled at any time.
-  **Bake Mode**: When using the light baker, the role of this light can
   be defined in this enumerator. The role will be followed even if the
   light is disabled, which allows to configure a light and then disable
   it for baking.
-  **Energy**: This value is a multiplier for the light, it's specially
   useful for :ref:`doc_high_dynamic_range` and for Spot and Omni lights, because it can
   create very bright spots near the emissor.
-  **Diffuse and Specular**: These light values get multiplied by the
   material light and diffuse colors, so a white value does not mean
   that light will be white, but that the original color will be kept.
-  **Operator**: It is possible to make some lights negative for a
   darkening effect.
-  **Projector**: Lights can project a texture for the diffuse light
   (currently only supported in Spot light).

Directional light
~~~~~~~~~~~~~~~~~

This is the most common type of light and represents the sun. It is also
the cheapest light to compute and should be used whenever possible
(although it's not the cheapest shadow-map to compute, but more on that
later). Directional light nodes are represented by a big arrow, which
represent the direction of the light, however the position of the node
does not affect the lighting at all, and can be anywhere.

.. image:: /img/light_directional.png

Basically what faces the light is lit, what doesn't is dark. Most lights
have specific parameters but directional lights are pretty simple in
nature so they don't.

Omni light
~~~~~~~~~~

Omni light is a point that throws light all around it up to a given
radius (distance) that can be controlled by the user. The light
attenuates with the distance and reaches 0 at the edge. It represents
lamps or any other light source that comes from a point.

.. image:: /img/light_omni.png

The attenuation curve for these kind of lights in nature is computed
with an inverse-quadratic function that never reaches zero and has
almost infinitely large values near the emissor.

This makes them considerably inconvenient to tweak for artists, so
Godot simulates them with an artist-controlled exponential curve
instead.

.. image:: /img/light_attenuation.png

Spot light
~~~~~~~~~~

Spot lights are similar to Omni lights, except they only operate between
a given angle (or "cutoff"). They are useful to simulate flashlights,
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
purposes, such as baking light emissors that are not going to be used in
real-time, and baking light bounces from real-time lights to add more
realism to a scene (see Baked Light]] tutorial for more information).
