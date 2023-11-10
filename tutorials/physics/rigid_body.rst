.. _doc_rigid_body:

Using RigidBody
===============

What is a rigid body?
---------------------

A rigid body is one that is directly controlled by the physics engine in order to simulate the behavior of physical objects.
In order to define the shape of the body, it must have one or more :ref:`Shape3D <class_Shape3D>` objects assigned. Note that setting the position of these shapes will affect the body's center of mass.

How to control a rigid body
---------------------------

A rigid body's behavior can be altered by setting its properties, such as mass and weight.
A physics material needs to be added to the rigid body to adjust its friction and bounce,
and set if it's absorbent and/or rough. These properties can be set in the Inspector or via code.
See :ref:`RigidBody3D <class_RigidBody3D>` and :ref:`PhysicsMaterial <class_PhysicsMaterial>` for
the full list of properties and their effects.

There are several ways to control a rigid body's movement, depending on your desired application.

If you only need to place a rigid body once, for example to set its initial location, you can use the methods provided by the :ref:`Node3D <class_Node3D>` node, such as ``set_global_transform()`` or ``look_at()``. However, these methods cannot be called every frame or the physics engine will not be able to correctly simulate the body's state.
As an example, consider a rigid body that you want to rotate so that it points towards another object. A common mistake when implementing this kind of behavior is to use ``look_at()`` every frame, which breaks the physics simulation. Below, we'll demonstrate how to implement this correctly.

The fact that you can't use ``set_global_transform()`` or ``look_at()`` methods doesn't mean that you can't have full control of a rigid body. Instead, you can control it by using the ``_integrate_forces()`` callback. In this method, you can add *forces*, apply *impulses*, or set the *velocity* in order to achieve any movement you desire.

The "look at" method
--------------------

As described above, using the Node3D's ``look_at()`` method can't be used each frame to follow a target.
Here is a custom ``look_at()`` method called ``look_follow()`` that will work with rigid bodies:

.. tabs::
 .. code-tab:: gdscript GDScript

    extends RigidBody3D

    var speed: float = 0.1

    func look_follow(state: PhysicsDirectBodyState3D, current_transform: Transform3D, target_position: Vector3) -> void:
        var forward_local_axis: Vector3 = Vector3(1, 0, 0)
        var forward_dir: Vector3 = (current_transform.basis * forward_local_axis).normalized()
        var target_dir: Vector3 = (target_position - current_transform.origin).normalized()
        var local_speed: float = clampf(speed, 0, acos(forward_dir.dot(target_dir)))
        if forward_dir.dot(target_dir) > 1e-4:
            state.angular_velocity = local_speed * forward_dir.cross(target_dir) / state.step
    
    func _integrate_forces(state):
        var target_position = $my_target_node3d_node.global_transform.origin
        look_follow(state, global_transform, target_position)

 .. code-tab:: csharp

    using Godot;

    public partial class MyRigidBody3D : RigidBody3D
    {
        private float _speed = 0.1f;
        private void LookFollow(PhysicsDirectBodyState3D state, Transform3D currentTransform, Vector3 targetPosition)
        {
            Vector3 forwardLocalAxis = new Vector3(1, 0, 0);
            Vector3 forwardDir = (currentTransform.Basis * forwardLocalAxis).Normalized();
            Vector3 targetDir = (targetPosition - currentTransform.Origin).Normalized();
            float localSpeed = Mathf.Clamp(_speed, 0.0f, Mathf.Acos(forwardDir.Dot(targetDir)));
            if (forwardDir.Dot(targetDir) > 1e-4)
            {
                state.AngularVelocity = forwardDir.Cross(targetDir) * localSpeed / state.Step;
            }
        }

        public override void _IntegrateForces(PhysicsDirectBodyState3D state)
        {
            Vector3 targetPosition = GetNode<Node3D>("MyTargetNode3DNode").GlobalTransform.Origin;
            LookFollow(state, GlobalTransform, targetPosition);
        }
    }


This method uses the rigid body's ``angular_velocity`` property to rotate the body. 
The axis to rotate around is given by the cross product between the current forward direction and the direction one wants to look in. 
The ``clamp`` is a simple method used to prevent the amount of rotation from going past the direction which is wanted to be looked in, 
as the total amount of rotation needed is given by the arccosine of the dot product. 
This method can be used with ``axis_lock_angular_*`` as well. If more precise control is needed, solutions such as ones relying on :ref:`class_Quaternion` may be required, 
as discussed in :ref:`doc_using_transforms`.
