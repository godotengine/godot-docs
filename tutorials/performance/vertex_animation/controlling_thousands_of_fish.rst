:article_outdated: True

.. _doc_controlling_thousands_of_fish:

Controlling thousands of fish with Particles
============================================

The problem with :ref:`MeshInstance3D <class_MeshInstance3D>` is that it is expensive to
update their transform array. It is great for placing many static objects around the
scene. But it is still difficult to move the objects around the scene.

To make each instance move in an interesting way, we will use a
:ref:`GPUParticles3D <class_GPUParticles3D>` node. Particles take advantage of GPU acceleration
by computing and setting the per-instance information in a :ref:`Shader <class_Shader>`.

First create a Particles node. Then, under "Draw Passes" set the Particle's "Draw Pass 1" to your
:ref:`Mesh <class_Mesh>`. Then under "Process Material" create a new
:ref:`ShaderMaterial <class_ShaderMaterial>`.

Set the ``shader_type`` to ``particles``.

.. code-block:: glsl

  shader_type particles

Then add the following two functions:

.. code-block:: glsl

  float rand_from_seed(in uint seed) {
    int k;
    int s = int(seed);
    if (s == 0)
      s = 305420679;
    k = s / 127773;
    s = 16807 * (s - k * 127773) - 2836 * k;
    if (s < 0)
      s += 2147483647;
    seed = uint(s);
    return float(seed % uint(65536)) / 65535.0;
  }

  uint hash(uint x) {
    x = ((x >> uint(16)) ^ x) * uint(73244475);
    x = ((x >> uint(16)) ^ x) * uint(73244475);
    x = (x >> uint(16)) ^ x;
    return x;
  }

These functions come from the default :ref:`ParticleProcessMaterial <class_ParticleProcessMaterial>`.
They are used to generate a random number from each particle's ``RANDOM_SEED``.

A unique thing about particle shaders is that some built-in variables are saved across frames.
``TRANSFORM``, ``COLOR``, and ``CUSTOM`` can all be accessed in the shader of the mesh, and
also in the particle shader the next time it is run.

Next, setup your ``start()`` function. Particles shaders contain a ``start()`` function and a
``process()`` function.

The code in the ``start()`` function only runs when the particle system starts.
The code in the ``process()`` function will always run.

We need to generate 4 random numbers: 3 to create a random position and one for the random
offset of the swim cycle.

First, generate 4 seeds inside the ``start()`` function using the ``hash()`` function provided above:

.. code-block:: glsl

  uint alt_seed1 = hash(NUMBER + uint(1) + RANDOM_SEED);
  uint alt_seed2 = hash(NUMBER + uint(27) + RANDOM_SEED);
  uint alt_seed3 = hash(NUMBER + uint(43) + RANDOM_SEED);
  uint alt_seed4 = hash(NUMBER + uint(111) + RANDOM_SEED);

Then, use those seeds to generate random numbers using ``rand_from_seed``:

.. code-block:: glsl

  CUSTOM.x = rand_from_seed(alt_seed1);
  vec3 position = vec3(rand_from_seed(alt_seed2) * 2.0 - 1.0,
                       rand_from_seed(alt_seed3) * 2.0 - 1.0,
                       rand_from_seed(alt_seed4) * 2.0 - 1.0);

Finally, assign ``position`` to ``TRANSFORM[3].xyz``, which is the part of the transform that holds
the position information.

.. code-block:: glsl

  TRANSFORM[3].xyz = position * 20.0;

Remember, all this code so far goes inside the ``start()`` function.

The vertex shader for your mesh can stay the exact same as it was in the previous tutorial.

Now you can move each fish individually each frame, either by adding to the ``TRANSFORM`` directly
or by writing to ``VELOCITY``.

Let's transform the fish by setting their ``VELOCITY`` in the ``start()`` function.

.. code-block:: glsl

  VELOCITY.z = 10.0;

This is the most basic way to set ``VELOCITY`` every particle (or fish) will have the same velocity.

Just by setting ``VELOCITY`` you can make the fish swim however you want. For example, try the code
below.

.. code-block:: glsl

  VELOCITY.z = cos(TIME + CUSTOM.x * 6.28) * 4.0 + 6.0;

This will give each fish a unique speed between ``2`` and ``10``.

You can also let each fish change its velocity over time if you set the velocity in the ``process()``
function.

If you used ``CUSTOM.y`` in the last tutorial, you can also set the speed of the swim animation based
on the ``VELOCITY``. Just use ``CUSTOM.y``.

.. code-block:: glsl

  CUSTOM.y = VELOCITY.z * 0.1;

This code gives you the following behavior:

.. image:: img/scene.gif

Using a ParticleProcessMaterial you can make the fish behavior as simple or complex as you like. In this
tutorial we only set Velocity, but in your own Shaders you can also set ``COLOR``, rotation, scale
(through ``TRANSFORM``). Please refer to the :ref:`Particles Shader Reference <doc_particle_shader>`
for more information on particle shaders.
