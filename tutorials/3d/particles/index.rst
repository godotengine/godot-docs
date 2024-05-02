:allow_comments: False

.. _doc_3d_particles:

Particle systems (3D)
=====================

This section of the tutorial covers (3D) GPU-accelerated particle systems. Most of the things
discussed here apply to CPU particles as well.

Introduction
------------

You can use particle systems to simulate complex physical effects like fire, sparks,
smoke, magical effects, and many more. They are very well suited for creating dynamic and organic
behavior and adding "life" to your scenes.

The idea is that a particle is emitted at a fixed interval and with a fixed lifetime. During
its lifetime, every particle will have the same base behavior. What makes each particle different
from the others and creates the organic look is the randomness that you can add to most of its
parameters and behaviors.

Every particle system you create in Godot consists of two main parts: particles and emitters.

Particles
~~~~~~~~~

A particle is the visible part of a particle system. It's what you see on the screen when a particle
system is active: The tiny specks of dust, the flames of a fire, the glowing orbs of a magical
effect. You can have anywhere between a couple hundred and tens of thousands of particles in a
single system. You can randomize a particle's size, its speed and movement direction, and change its
color over the course of its lifetime. When you think of a fire, you can think of all the little
embers flying away from it as individual particles.

Emitters
~~~~~~~~

An emitter is what's creating the particles. Emitters are usually not visible, but they can have
a shape. That shape controls where and how particles are spawned, for example whether they should fill
a room like dust or shoot away from a single point like a fountain. Going back to the fire example,
an emitter would be the heat at the center of the fire that creates the embers and the flames.

Node overview
~~~~~~~~~~~~~

.. figure:: img/particle_nodes.webp
   :alt: A list of nodes related to 3D particles
   :align: right

   All 3D particle nodes available in Godot

There are two types of 3D particle systems in Godot: :ref:`class_GPUParticles3D`, which are processed on the GPU,
and :ref:`class_CPUParticles3D`, which are processed on the CPU.

CPU particle systems are less flexible than their GPU counterpart, but they work on a wider range of hardware and
provide better support for older devices and mobile phones. Because they are processed on the CPU,
they are not as performant as GPU particle systems and can't render as many individual particles.
In addition they currently do not have all the available options GPU particles have for control.

GPU particle systems run on the GPU and can render hundreds of thousands of particles on modern
hardware. You can write custom particle shaders for them, which makes them very flexible. You can
also make them interact with the environment by using attractor and collision nodes.

There are three particle attractor nodes: :ref:`class_GPUParticlesAttractorBox3D`, :ref:`class_GPUParticlesAttractorSphere3D`,
and :ref:`class_GPUParticlesAttractorVectorField3D`. An attractor node applies a force to all particles
in its reach and pulls them closer or pushes them away based on the direction of that force.

There are several particle collision nodes. :ref:`class_GPUParticlesCollisionBox3D` and
:ref:`class_GPUParticlesCollisionSphere3D` are the simple ones. You can use them to create basic
shapes like boxes, a floor, or a wall that particles collide with. The other two nodes provide
more complex collision behavior. The :ref:`class_GPUParticlesCollisionSDF3D` is useful when you want
indoor scenes to collide with particles without having to create all the individual box and sphere
colliders by hand. If you want particles to collide with large outdoor scenes, you would use the
:ref:`class_GPUParticlesCollisionHeightField3D` node. It creates a heightmap of your world and the
objects in it and uses that for large-scale particle collisions.


Basic usage
-----------

.. toctree::
   :maxdepth: 1
   :name: toc-particles-basic

   creating_a_3d_particle_system
   properties
   process_material_properties

Advanced topics
---------------

.. toctree::
   :maxdepth: 1
   :name: toc-particles-advanced

   subemitters
   trails
   turbulence
   attractors
   collision
   complex_shapes
