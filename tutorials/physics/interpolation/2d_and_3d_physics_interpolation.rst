.. _doc_2d_and_3d_physics_interpolation:

2D and 3D physics interpolation
===============================

Generally 2D and 3D physics interpolation work in very similar ways. However, there
are a few differences, which will be described here.

2D Particles
------------

Currently only ``CPUParticles2D`` are supported for physics interpolation in 2D. It
is recommended to use a physics tick rate of at least 20-30 ticks per second to
keep particles looking fluid.

``Particles2D`` (GPU particles) are not yet interpolated, so for now it is
recommended to convert to ``CPUParticles2D`` (but keep a backup of your
``Particles2D`` in case we get these working).

Other
-----

- ``get_global_transform_interpolated()`` is currently only available for 3D.
- ``MultiMeshes`` are supported in both 2D and 3D.
- Physics interpolation in 2D is implemented on the server side, which means it's
  effective on physics bodies created using :ref:`low-level servers <doc_using_servers>`.
  In contrast, physics interpolation in 3D is implemented on the scene side.
  This means it does not affect physics bodies created using servers. These must be
  interpolated manually instead. See the
  `pull request description <https://github.com/godotengine/godot/pull/104269>`__
  for the rationale on this design decision.
