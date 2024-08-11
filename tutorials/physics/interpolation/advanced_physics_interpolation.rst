.. _doc_advanced_physics_interpolation:

Advanced physics interpolation
==============================

Although the previous instructions will give satisfactory results in a lot of
games, in some cases you will want to go a stage further to get the best
possible results and the smoothest possible experience.

.. note:: currently only 2D physics interpolation works in Godot.
          3D interpolation is expected to come in a future update.

Exceptions to automatic physics interpolation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Even with physics interpolation active, there may be some local situations
where you would benefit from disabling automatic interpolation for a
:ref:`Node<class_Node>` (or branch of the :ref:`SceneTree<class_SceneTree>`),
and have the finer control of performing interpolation manually.

This is possible using the :ref:`Node.physics_interpolation_mode<class_Node_property_physics_interpolation_mode>`
property which is present in all Nodes. If you for example, turn off
interpolation for a Node, the children will recursively also be affected (as
they default to inheriting the parent setting). This means you can easily
disable interpolation for an entire subscene.

The most common situation where you may want to perform your own
interpolation is Cameras.

Disabling interpolation on other nodes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Although Cameras are the most common example, there are a number of cases
when you may wish other nodes to control their own interpolation, or be
non-interpolated. Consider for example, a player in a top view game whose
rotation is controlled by mouse look. Disabling physics rotation allows the
player rotation to match the mouse in real-time.
