.. _doc_physics_interpolation_quick_start_guide:

Quick start guide
=================

.. note:: currently only 2D physics interpolation works in Godot.
          3D interpolation is expected to come in a future update.

- Turn on physics interpolation: :ref:`ProjectSettings.physics/common/physics_interpolation<class_ProjectSettings_property_physics/common/physics_interpolation>`
- Make sure you move objects and run your game logic in
  ``_physics_process()`` rather than ``_process()``. This includes moving
  objects directly *and indirectly* (by e.g. moving a parent, or using
  another mechanism to automatically move nodes).
- Be sure to call :ref:`Node.reset_physics_interpolation<class_Node_method_reset_physics_interpolation>`
  on nodes *after* you first position or teleport them, to prevent
  "streaking"
- Temporarily try setting :ref:`ProjectSettings.physics/common/physics_ticks_per_second<class_ProjectSettings_property_physics/common/physics_ticks_per_second>`
  to 10 to see the difference with and without interpolation.
