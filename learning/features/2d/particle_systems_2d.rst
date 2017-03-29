.. _doc_particle_systems_2d:

Particle Systems (2D)
=====================

Intro
-----

A simple (but flexible enough for most uses) particle system is
provided. Particle systems are used to simulate complex physical effects
such as sparks, fire, magic particles, smoke, mist, magic, etc.

The idea is that a "particle" is emitted at a fixed interval and with a
fixed lifetime. During his lifetime, every particle will have the same
base behavior. What makes every particle different and provides a more
organic look is the "randomness" associated to each parameter. In
essence, creating a particle system means setting base physics
parameters and then adding randomness to them.

Particles2D
~~~~~~~~~~~

Particle systems are added to the scene via the
:ref:`Particles2D <class_Particles2D>`
node. They are enabled by default and start emitting white points
downwards (as affected by the gravity). This provides a reasonable
starting point to start adapting it to our needs.

.. image:: /img/particles1.png

Texture
~~~~~~~

A particle system uses a single texture (in the future this might be
extended to animated textures via spritesheet). The texture is set via
the relevant texture property:

.. image:: /img/particles2.png

Physics variables
-----------------

Before taking a look at the global parameters for the particle system,
let's first see what happens when the physics variables are tweaked.

Direction
---------

This is the base angle at which particles emit. Default is 0 (down):

.. image:: /img/paranim1.gif

Changing it will change the emissor direction, but gravity will still
affect them:

.. image:: /img/paranim2.gif

This parameter is useful because, by rotating the node, gravity will
also be rotated. Changing direction keeps them separate.

Spread
------

Spread is the angle at which particles will randomly be emitted.
Increasing the spread will increase the angle. A spread of 180 will emit
in all directions.

.. image:: /img/paranim3.gif

Linear velocity
---------------

Linear velocity is the speed at which particles will be emitted (in
pixels/sec). Speed might later be modified by gravity or other
accelerations (as described further below).

.. image:: /img/paranim4.gif

Spin velocity
-------------

Spin velocity is the speed at which particles turn around their center
(in degrees/sec).

.. image:: /img/paranim5.gif

Orbit velocity
--------------

Orbit velocity is used to make particles turn around their center.

.. image:: /img/paranim6.gif

Gravity direction & strength
----------------------------

Gravity can be modified as in direction and strength. Gravity affects
every particle currently alive.

.. image:: /img/paranim7.gif

Radial acceleration
-------------------

If this acceleration is positive, particles are accelerated away from
the center. If negative, they are absorbed towards it.

.. image:: /img/paranim8.gif

Tangential acceleration
-----------------------

This acceleration will use the tangent vector to the center. Combining
with radial acceleration can do nice effects.

.. image:: /img/paranim9.gif

Damping
-------

Damping applies friction to the particles, forcing them to stop. It is
specially useful for sparks or explosions, which usually begin with a
high linear velocity and then stop as they fade.

.. image:: /img/paranim10.gif

Initial angle
-------------

Determines the initial angle of the particle (in degress). This parameter
is mostly useful randomized.

.. image:: /img/paranim11.gif

Initial & final size
--------------------

Determines the initial and final scales of the particle.

.. image:: /img/paranim12.gif

Color phases
------------

Particles can use up to 4 color phases. Each color phase can include
transparency.

Phases must provide an offset value from 0 to 1, and always in
ascending order. For example, a color will begin at offset 0 and end
in offset 1, but 4 colors might use different offsets, such as 0, 0.2,
0.8 and 1.0 for the different phases:

.. image:: /img/particlecolorphases.png

Will result in:

.. image:: /img/paranim13.gif

Global parameters
-----------------

These parameters affect the behavior of the entire system.

Lifetime
--------

The time in seconds that every particle will stay alive. When lifetime
ends, a new particle is created to replace it.

Lifetime: 0.5

.. image:: /img/paranim14.gif

Lifetime: 4.0

.. image:: /img/paranim15.gif

Timescale
---------

It happens often that the effect achieved is perfect, except too fast or
too slow. Timescale helps adjust the overall speed.

Timescale everything 2x:

.. image:: /img/paranim16.gif

Preprocess
----------

Particle systems begin with 0 particles emitted, then start emitting.
This can be an inconvenience when just loading a scene and systems like
a torch, mist, etc begin emitting the moment you enter. Preprocess is
used to let the system process a given amount of seconds before it is
actually shown the first time.

Emit timeout
------------

This variable will switch emission off after given amount of seconds
being on. When zero, itś disabled.

Offset
------

Allows to move the emission center away from the center

Half extents
------------

Makes the center (by default 1 pixel) wider, to the size in pixels
desired. Particles will emit randomly inside this area.

.. image:: /img/paranim17.gif

It is also possible to set an emission mask by using this value. Check
the "Particles" menu on the 2D scene editor viewport and select your
favorite texture. Opaque pixels will be used as potential emission
location, while transparent ones will be ignored:

.. image:: /img/paranim19.gif

Local space
-----------

By default this option is on, and it means that the space that particles
are emitted to is contained within the node. If the node is moved, all
particles are moved with it:

.. image:: /img/paranim20.gif

If disabled, particles will emit to global space, meaning that if the
node is moved, the emissor is moved too:

.. image:: /img/paranim21.gif

Explosiveness
-------------

If lifetime is 1 and there are 10 particles, it means every particle
will be emitted every 0.1 seconds. The explosiveness parameter changes
this, and forces particles to be emitted all together. Ranges are:

-  0: Emit all particles together.
-  1: Emit particles at equal interval.

Values in the middle are also allowed. This feature is useful for
creating explosions or sudden bursts of particles:

.. image:: /img/paranim18.gif

Randomness
----------

All physics parameters can be randomized. Random variables go from 0 to
1. the formula to randomize a parameter is:

::

    initial_value = param_value + param_value*randomness
