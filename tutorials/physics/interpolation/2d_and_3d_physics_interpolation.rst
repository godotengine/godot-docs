.. _doc_2d_and_3d_physics_interpolation:

2D and 3D physics interpolation
===============================

Generally 2D and 3D physics interpolation work in very similar ways. However,
there are a few differences, which will be described here.

.. note:: currently only 2D physics interpolation works in Godot.
          3D interpolation is expected to come in a future update.

Global versus local interpolation
---------------------------------

- In 3D, physics interpolation is performed *independently* on the **global
  transform** of each 3D instance.
- In 2D by contrast, physics interpolation is performed on the **local
  transform** of each 2D instance.

This has some implications:

- In 3D, it is easy to turn interpolation on and off at the level of each
  ``Node``, via the ``physics_interpolation_mode`` property in the Inspector,
  which can be set to ``On``, ``Off``, or ``Inherited``.

.. figure:: img/physics_interpolation_mode.webp
    :align: center

- However this means that in 3D, pivots that occur in the ``SceneTree``
  (due to parent child relationships) can only be interpolated
  **approximately** over the physics tick. In most cases this will not
  matter, but in some situations the interpolation can look slightly *off*.
- In 2D, interpolated local transforms are passed down to children during
  rendering. This means that if a parent is set to
  ``physics_interpolation_mode`` ``On``, but the child is set to ``Off``,
  the child will still be interpolated if the parent is moving. *Only the
  child's local transform is uninterpolated.* Controlling the on / off
  behaviour of 2D nodes therefore requires a little more thought and planning.
- On the positive side, pivot behaviour in the scene tree is perfectly
  preserved during interpolation in 2D, which gives super smooth behaviour.

reset_physics_interpolation()
-----------------------------

Whenever objects are moved to a completely new position, and interpolation is
not desired (so as to prevent a "streaking" artefact), it is the
responsibility of the user to call ``reset_physics_interpolation()``.

The good news is that in 2D, this is automatically done for you when nodes
first enter the tree. This reduces boiler plate, and reduces the effort
required to get an existing project working.

.. note:: If you move objects *after* adding to the scene tree, you will still
          need to call ``reset_physics_interpolation()`` as with 3D.

2D Particles
------------

Currently ``CPUParticles2D`` and ``Particles2D`` are not supported for physics
interpolation in 2D.
