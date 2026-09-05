.. _doc_advanced_physics_interpolation:

Advanced physics interpolation
==============================

Although the previous instructions will give satisfactory results in a lot of games,
in some cases you will want to go a stage further to get the best possible results
and the smoothest possible experience.

Exceptions to automatic physics interpolation
---------------------------------------------

Even with physics interpolation active, there may be some local situations where
you would benefit from disabling automatic interpolation for a
:ref:`Node<class_Node>` (or branch of the :ref:`SceneTree<class_SceneTree>`), and
have the finer control of performing interpolation manually.

This is possible using the :ref:`Node.physics_interpolation_mode<class_Node_property_physics_interpolation_mode>`
property which is present in all Nodes. If you for example, turn off interpolation
for a Node, the children will recursively also be affected (as they default to
inheriting the parent setting). This means you can easily disable interpolation for
an entire subscene.

.. figure:: img/physics_interpolation_mode.webp

It is worth noting that, both in 2D and 3D, physics interpolation is performed
on the **local transform** of each instance. During rendering, interpolated local
transforms are passed down to children.

This means that if a parent has ``physics_interpolation_mode`` set to ``On``,
but the child is set to ``Off``, the child's inherited transform will still be
interpolated if the parent is moving. *Only the child's local transform is
uninterpolated.* Controlling the on/off behavior of nodes therefore requires some
thought and planning.

.. note::

          Prior to Godot 4.5, parent nodes did not propagate physics-interpolated
          transforms to children in the scene tree. This could result in "clunking"
          in the first child with ``physics_interpolation_mode`` ``Off``.
          Because of this, early tutorials often recommended specifying
          non-interpolated cameras in global space (by e.g. setting
          :ref:`Node3D.top_level<class_Node3D_property_top_level>`).
          This behavior was fixed in Godot 4.5.

The most common situation where you may want to perform your own interpolation is
Cameras.

Cameras
~~~~~~~

:ref:`class_Camera3D` can use automatic interpolation just like any other
node. However, for best results, it is in many cases recommended that you take a
manual approach to camera interpolation, especially at low physics tick rates.

This is because viewers are very sensitive to camera movement. For instance, a
Camera3D that realigns slightly every 1/10th of a second (at 10tps tick rate) will
often be noticeable. You can get a much smoother result by moving the camera each
frame in ``_process``, and following an interpolated target manually.

Manual camera interpolation
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Typical example
^^^^^^^^^^^^^^^

A typical example of a custom approach is to use the ``look_at`` function in the
Camera3D every frame in ``_process()`` to look at a target node (such as the player).

But there is a problem. If we use the traditional ``get_global_transform()`` on a
Camera3D "target" node, this transform will only focus the Camera3D on the target *at
the current physics tick*. This is *not* what we want, as the camera will jump
about on each physics tick as the target moves. Even though the camera may be
updated each frame, this does not help give smooth motion if the *target* is only
changing each physics tick.

get_global_transform_interpolated()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

What we really want to focus the camera on, is not the position of the target on
the physics tick, but the *interpolated* position, i.e. the position at which the
target will be rendered.

We can do this using the :ref:`Node3D.get_global_transform_interpolated<class_Node3D_method_get_global_transform_interpolated>`
function. This acts exactly like getting :ref:`Node3D.global_transform<class_Node3D_property_global_transform>`
but it gives you the *interpolated* transform (during a ``_process()`` call).

.. important:: ``get_global_transform_interpolated()`` should only be used once or
               twice for special cases such as cameras. It should **not** be used
               all over the place in your code (both for performance reasons, and
               to give correct gameplay).

.. note:: Aside from exceptions like the camera, in most cases, your game logic
          should be in ``_physics_process()``. In game logic you should be calling
          ``get_global_transform()`` or ``get_transform()``, which will give the
          current physics transform (in global or local space respectively), which
          is usually what you will want for gameplay code.

Example manual camera script
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Here is a basic example of a camera which follows an interpolated target:

.. code-block:: gdscript

    extends Camera3D

    # Node that the camera will follow
    var _target

    # We will smoothly lerp to follow the target
    # rather than follow exactly
    var _target_pos : Vector3 = Vector3()

    func _ready() -> void:
        # Find the target node
        _target = get_node("../Player")

        # Turn off automatic physics interpolation for the Camera3D, manually.
        # This can alternatively be done in the Inspector.
        set_physics_interpolation_mode(Node.PHYSICS_INTERPOLATION_MODE_OFF)

    func _process(delta: float) -> void:
        # Find the current interpolated transform of the target
        var tr : Transform = _target.get_global_transform_interpolated()

        # Provide some delayed smoothed lerping towards the target position
        _target_pos = lerp(_target_pos, tr.origin, min(delta, 1.0))

        # Our interpolated target, and a vector pointing up.
        look_at(_target_pos, Vector3(0, 1, 0))

Mouse look
^^^^^^^^^^

Mouse look is a very common way of controlling cameras. But there is a problem.
Unlike keyboard input which can be sampled periodically on the physics tick, mouse
move events can come in continuously. The camera will be expected to react and
follow these mouse movements on the next frame, rather than waiting until the next
physics tick.

In this situation, it can be better to disable physics interpolation for the camera
node (using :ref:`Node.physics_interpolation_mode<class_Node_property_physics_interpolation_mode>`)
and directly apply the mouse input to the camera rotation, rather than apply it in
``_physics_process``.

Often, especially with cameras and camera rigs, you will want to use a combination of
interpolation and non-interpolation, as in these examples:

- First person camera: inherit the physics-interpolated position of a parent physics
  body, but perform rotation *without* interpolation, using a mouse.
- Third person camera: determine the target position (where is it looking at) by calling
  :ref:`Node3D.get_global_transform_interpolated <class_Node3D_method_get_global_transform_interpolated>`,
  but move the camera with the mouse and *without* interpolation.

Usually you can do this with a subscene arranged something like this:
*(where ``physics_interpolation_mode`` is specified in square brackets)*

.. code-block:: text

   PhysicsBody3D ["On"] (or inheriting "On")
   └── Node3D ["Off"] acting as a "rig" used to control yaw
       ├── MeshInstance3D ["Inherit"] for visuals
       └── Camera3D ["Inherit"] used to control pitch

With this setup, all children of the "rig" node will therefore inherit the
smoothed position from the parent ``PhysicsBody3D``, but can react immediately to
mouse movement because local transforms will be uninterpolated.

There are many permutations and variations of camera types, but it should be clear
that in many cases, disabling automatic physics interpolation and handling this
yourself can give a better result.

Disabling interpolation on other nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Although cameras are the most common example, there are a number of cases when you
may wish other nodes to control their own interpolation, or be non-interpolated.
Consider for example, a player in a top view game whose rotation is controlled by
mouse look. Disabling physics interpolation allows the player rotation to match the
mouse in real time. This would correspond to the "rig" in the earlier example, but
without a camera as a child.

MultiMeshes
~~~~~~~~~~~

Although most visual Nodes follow the single Node single visual instance paradigm,
MultiMeshes can control several instances from the same Node. Therefore, they have
some extra functions for controlling interpolation functionality on a
*per-instance* basis. You should explore these functions if you are using
interpolated MultiMeshes.

- :ref:`MultiMesh.reset_instance_physics_interpolation<class_MultiMesh_method_reset_instance_physics_interpolation>`
- :ref:`MultiMesh.set_buffer_interpolated<class_MultiMesh_method_set_buffer_interpolated>`

Full details are in the :ref:`MultiMesh<class_MultiMesh>` documentation.
