.. _doc_particle_systems_2d:

Particle Systems (2D)
=====================

Intro
-----

A simple (but flexible enough for most uses) particle system is
provided. Particle systems are used to simulate complex physical effects
such as sparks, fire, magic particles, smoke, mist, magic, etc.

The idea is that a "particle" is emitted at a fixed interval and with a
fixed lifetime. During its lifetime, every particle will have the same
base behavior. What makes every particle different and provides a more
organic look is the "randomness" associated to each parameter. In
essence, creating a particle system means setting base physics
parameters and then adding randomness to them.

Particles2D
~~~~~~~~~~~

Particle systems are added to the scene via the
:ref:`Particles2D <class_Particles2D>`
node. However, after creating that node you will notice that only a white dot was created, 
and that there is a warning icon next to your Particles2D node in the inspector. This 
is because the node needs a ParticlesMaterial to function.

ParticlesMaterial
~~~~~~~~~~~~~~~~~

To add a process material to your particles node, go to Process Material in
your inspector panel. Click on the box next to material, and from the dropdown
menu select New Particles Material. 

.. image:: img/particles_material.png

Your Particles2D node should now be emitting
white points downward.

.. image:: img/particles1.png

Texture
~~~~~~~

A particle system uses a single texture (in the future this might be
extended to animated textures via spritesheet). The texture is set via
the relevant texture property:

.. image:: img/particles2.png

Time Parameters
===============

Lifetime
--------

The time in seconds that every particle will stay alive. When lifetime
ends, a new particle is created to replace it.

Lifetime: 0.5

.. image:: img/paranim14.gif

Lifetime: 4.0

.. image:: img/paranim15.gif

One Shot
--------

When enabled, a Particles2D node will emit all of it's particles once 
and then never again.

Preprocess
----------

Particle systems begin with 0 particles emitted, then start emitting.
This can be an inconvenience when just loading a scene and systems like
a torch, mist, etc begin emitting the moment you enter. Preprocess is
used to let the system process a given amount of seconds before it is
actually shown the first time.

Speed Scale
-----------

The speed scale has a default value of 1, and is used to adjust the 
speed of a particle system. Lowering the value will make the particles 
slower, increaseing the value will make the particles much faster.

Explosiveness
-------------

If lifetime is 1 and there are 10 particles, it means every particle
will be emitted every 0.1 seconds. The explosiveness parameter changes
this, and forces particles to be emitted all together. Ranges are:

-  0: Emit all particles together.
-  1: Emit particles at equal interval.

Values in the middle are also allowed. This feature is useful for
creating explosions or sudden bursts of particles:

.. image:: img/paranim18.gif

Randomness
----------

All physics parameters can be randomized. Random variables go from 0 to
1. The formula to randomize a parameter is:

::

    initial_value = param_value + param_value*randomness

Fixed FPS
---------

This setting can be used to set the particle system to render at a fixed 
FPS. For instance, changing the FPS to 2 will make the particles render 
every 2 frames a second, however it will not slow down. 

Fract Delta
-----------

This can be used to turn Fract Delta on or off.

Drawing Parameters 
==================

Visability Rect
---------------
 
The W and H values control width and height of the visability rectnagle 
respectively. The X and Y values control the position of the Upper left 
corner of the visability rectangle relative to the particle emitter.

Local Coords
------------

By default this option is on, and it means that the space that particles
are emitted to is contained within the node. If the node is moved, all
particles are moved with it:

.. image:: img/paranim20.gif

If disabled, particles will emit to global space, meaning that if the
node is moved, the emissor is moved too:

.. image:: img/paranim21.gif

Draw Order
----------

The particle draw order can be set to index or lifetime.

ParticlesMaterial settings
==========================

Direction
---------

This is the base angle at which particles emit. Default is 0 (down):

.. image:: img/paranim1.gif

Changing it will change the emissor direction, but gravity will still
affect them:

.. image:: img/paranim2.gif

This parameter is useful because, by rotating the node, gravity will
also be rotated. Changing direction keeps them separate.

Spread
------

Spread is the angle at which particles will randomly be emitted.
Increasing the spread will increase the angle. A spread of 180 will emit
in all directions.

.. image:: img/paranim3.gif

Gravity
-------

The gravity applied to every particle. 

.. image:: img/paranim7.gif

Initial Velocity
----------------

Linear velocity is the speed at which particles will be emitted (in
pixels/sec). Speed might later be modified by gravity or other
accelerations (as described further below).

.. image:: img/paranim4.gif

Angular Velocity
----------------

Angular velocity is the inital angular velocity applied to particles.

Spin Velocity
-------------

Spin velocity is the speed at which particles turn around their center
(in degrees/sec).

.. image:: img/paranim5.gif

Orbit Velocity
--------------

Orbit velocity is used to make particles turn around their center.

.. image:: img/paranim6.gif

Linear Acceleration
-------------------

The linear acceleration applied to each particle.

Radial Acceleration
-------------------

If this acceleration is positive, particles are accelerated away from
the center. If negative, they are absorbed towards it.

.. image:: img/paranim8.gif

Tangential Acceleration
-----------------------

This acceleration will use the tangent vector to the center. Combining
with radial acceleration can do nice effects.

.. image:: img/paranim9.gif

Damping
-------

Damping applies friction to the particles, forcing them to stop. It is
especially useful for sparks or explosions, which usually begin with a
high linear velocity and then stop as they fade.

.. image:: img/paranim10.gif

Angle
-----

Determines the initial angle of the particle (in degress). This parameter
is mostly useful randomized.

.. image:: img/paranim11.gif

Scale
-----

Determines the initial scale of the particles.

.. image:: img/paranim12.gif

Color
-----

Used to change the color of the particles being emitted.

Hue variation
-------------

The variation value sets the inital hue variation applied to each 
particle. The Variation rand value controls the hue variation
randomness ratio.