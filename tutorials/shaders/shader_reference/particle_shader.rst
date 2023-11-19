.. _doc_particle_shader:

Particle shaders
================

Particle shaders are a special type of shader that runs before the object is
drawn. They are used for calculating material properties such as color,
position, and rotation. They are drawn with any regular material for CanvasItem
or Spatial, depending on whether they are 2D or 3D.

Particle shaders are unique because they are not used to draw the object itself;
they are used to calculate particle properties, which are then used by a
CanvasItem or Spatial shader. They contain two processor functions: ``start()``
and ``process()``.

Unlike other shader types, particle shaders keep the data that was output the
previous frame. Therefore, particle shaders can be used for complex effects that
take place over multiple frames.

.. note::

    Particle shaders are only available with GPU-based particle nodes
    (:ref:`class_GPUParticles2D` and :ref:`class_GPUParticles3D`).

    CPU-based particle nodes (:ref:`class_CPUParticles2D` and
    :ref:`class_CPUParticles3D`) are *rendered* on the GPU (which means they can
    use custom CanvasItem or Spatial shaders), but their motion is *simulated*
    on the CPU.

Render modes
^^^^^^^^^^^^

+--------------------------+-------------------------------------------+
| Render mode              | Description                               |
+==========================+===========================================+
| **keep_data**            | Do not clear previous data on restart.    |
+--------------------------+-------------------------------------------+
| **disable_force**        | Disable attractor force.                  |
+--------------------------+-------------------------------------------+
| **disable_velocity**     | Ignore **VELOCITY** value.                |
+--------------------------+-------------------------------------------+
| **collision_use_scale**  | Scale the particle's size for collisions. |
+--------------------------+-------------------------------------------+

Built-ins
^^^^^^^^^

Values marked as "in" are read-only. Values marked as "out" are for optional writing and will
not necessarily contain sensible values. Values marked as "inout" provide a sensible default
value, and can optionally be written to. Samplers are not subjects of writing and they are
not marked.

Global built-ins
^^^^^^^^^^^^^^^^

Global built-ins are available everywhere, including custom functions.

+-------------------+----------------------------------------------------------------------------------------+
| Built-in          | Description                                                                            |
+===================+========================================================================================+
| in float **TIME** | Global time, in seconds.                                                               |
+-------------------+----------------------------------------------------------------------------------------+
| in float **PI**   | A ``PI`` constant (``3.141592``).                                                      |
|                   | A ration of circle's circumference to its diameter and amount of radians in half turn. |
+-------------------+----------------------------------------------------------------------------------------+
| in float **TAU**  | A ``TAU`` constant (``6.283185``).                                                     |
|                   | An equivalent of ``PI * 2`` and amount of radians in full turn.                        |
+-------------------+----------------------------------------------------------------------------------------+
| in float **E**    | A ``E`` constant (``2.718281``). Euler's number and a base of the natural logarithm.   |
+-------------------+----------------------------------------------------------------------------------------+

Start and Process built-ins
^^^^^^^^^^^^^^^^^^^^^^^^^^^

These properties can be accessed from both the ``start()`` and ``process()`` functions. 

+------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| Function                           | Description                                                                                                                             |
+====================================+=========================================================================================================================================+
| in float **LIFETIME**              | Particle lifetime.                                                                                                                      |
+------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| in float **DELTA**                 | Delta process time.                                                                                                                     |
+------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| in uint **NUMBER**                 | Unique number since emission start.                                                                                                     |
+------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| in uint **INDEX**                  | Particle index (from total particles).                                                                                                  |
+------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| in mat4 **EMISSION_TRANSFORM**     | Emitter transform (used for non-local systems).                                                                                         |
+------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| in uint **RANDOM_SEED**            | Random seed used as base for random.                                                                                                    |
+------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| inout bool **ACTIVE**              | ``true`` when the particle is active, can be set ``false``.                                                                             |
+------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| inout vec4 **COLOR**               | Particle color, can be written to and accessed in mesh's vertex function.                                                               |
+------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| inout vec3 **VELOCITY**            | Particle velocity, can be modified.                                                                                                     |
+------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| inout mat4 **TRANSFORM**           | Particle transform.                                                                                                                     |
+------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| inout vec4 **CUSTOM**              | Custom particle data. Accessible from shader of mesh as **INSTANCE_CUSTOM**.                                                            |
+------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| inout float **MASS**               | Particle mass, intended to be used with attractors. Equals ``1.0`` by default.                                                          |
+------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| in vec4 **USERDATAX**              | Vector that enables the integration of supplementary user-defined data into the particle process shader.                                |
|                                    | ``USERDATAX`` are six built-ins identified by number, ``X`` can be numbers between 1 and 6.                                             |
+------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| in uint **FLAG_EMIT_POSITION**     | A flag for using on the last argument of ``emit_subparticle`` function to assign a position to a new particle's transform.              |
+------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| in uint **FLAG_EMIT_ROT_SCALE**    | A flag for using on the last argument of ``emit_subparticle`` function to assign the rotation and scale to a new particle's transform.  |
+------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| in uint **FLAG_EMIT_VELOCITY**     | A flag for using on the last argument of ``emit_subparticle`` function to assign a velocity to a new particle.                          |
+------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| in uint **FLAG_EMIT_COLOR**        | A flag for using on the last argument of ``emit_subparticle`` function to assign a color to a new particle.                             |
+------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| in uint **FLAG_EMIT_CUSTOM**       | A flag for using on the last argument of ``emit_subparticle`` function to assign a custom data vector to a new particle.                |
+------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| in vec3 **EMITTER_VELOCITY**       | Velocity of the Particles node.                                                                                                         |
+------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| in float **INTERPOLATE_TO_END**    | Value of ``interp_to_end`` property of Particles node.                                                                                  |
+------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| in uint **AMOUNT_RATIO**           | Value of ``amount_ratio`` property of Particles node.                                                                                   |
+------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+

.. note:: In order to use the ``COLOR`` variable in a StandardMaterial3D, set ``vertex_color_use_as_albedo``
          to ``true``. In a ShaderMaterial, access it with the ``COLOR`` variable.

Start built-ins
^^^^^^^^^^^^^^^

+---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Built-in                        | Description                                                                                                                                                                           |
+=================================+=======================================================================================================================================================================================+
| in bool **RESTART_POSITION**    | ``true`` if particle is restarted, or emitted without a custom position (i.e. this particle was created by ``emit_subparticle()`` without the ``FLAG_EMIT_POSITION`` flag).           |
+---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| in bool **RESTART_ROT_SCALE**   | ``true`` if particle is restarted, or emitted without a custom rotation or scale (i.e. this particle was created by ``emit_subparticle()`` without the ``FLAG_EMIT_ROT_SCALE`` flag). |
+---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| in bool **RESTART_VELOCITY**    | ``true`` if particle is restarted, or emitted without a custom velocity (i.e. this particle was created by ``emit_subparticle()`` without the ``FLAG_EMIT_VELOCITY`` flag).           |
+---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| in bool **RESTART_COLOR**       | ``true`` if particle is restarted, or emitted without a custom color (i.e. this particle was created by ``emit_subparticle()`` without the ``FLAG_EMIT_COLOR`` flag).                 |
+---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| in bool **RESTART_CUSTOM**      | ``true`` if particle is restarted, or emitted without a custom property (i.e. this particle was created by ``emit_subparticle()`` without the ``FLAG_EMIT_CUSTOM`` flag).             |
+---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Process built-ins
^^^^^^^^^^^^^^^^^

+------------------------------------+-----------------------------------------------------------------------------------------------------+
| Built-in                           | Description                                                                                         |
+====================================+=====================================================================================================+
| in bool **RESTART**                | ``true`` if the current process frame is first for the particle.                                    |
+------------------------------------+-----------------------------------------------------------------------------------------------------+
| in bool **COLLIDED**               | ``true`` when the particle has collided with a particle collider.                                   |
+------------------------------------+-----------------------------------------------------------------------------------------------------+
| in vec3 **COLLISION_NORMAL**       | A normal of the last collision. If there is no collision detected it is equal to ``vec3(0.0)``.     |
+------------------------------------+-----------------------------------------------------------------------------------------------------+
| in float **COLLISION_DEPTH**       | A length of normal of the last collision. If there is no collision detected it is equal to ``0.0``. |
+------------------------------------+-----------------------------------------------------------------------------------------------------+
| in vec3 **ATTRACTOR_FORCE**        | A combined force of the attractors at the moment on that particle.                                  |
+------------------------------------+-----------------------------------------------------------------------------------------------------+

Process functions
^^^^^^^^^^^^^^^^^

``emit_subparticle`` is currently the only custom function supported by
particles shaders. It allows users to add a new particle with specified
parameters from a sub-emitter. The newly created particle will only use the
properties that match the ``flags`` parameter. For example, the
following code will emit a particle with a specified position, velocity, and
color, but unspecified rotation, scale, and custom value:

.. code-block:: glsl

    mat4 custom_transform = mat4(1.0);
    custom_transform[3].xyz = vec3(10.5, 0.0, 4.0);
    emit_subparticle(custom_transform, vec3(1.0, 0.5, 1.0), vec4(1.0, 0.0, 0.0, 1.0), vec4(1.0), FLAG_EMIT_POSITION | FLAG_EMIT_VELOCITY | FLAG_EMIT_COLOR);

+--------------------------------------------------------------------------------------------+--------------------------------------+
| Function                                                                                   | Description                          |
+============================================================================================+======================================+
| bool **emit_subparticle** (mat4 xform, vec3 velocity, vec4 color, vec4 custom, uint flags) | Emits a particle from a sub-emitter. |
+--------------------------------------------------------------------------------------------+--------------------------------------+
