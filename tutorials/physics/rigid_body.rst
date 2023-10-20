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
Here is a custom ``look_at()`` method that will work reliably with rigid bodies:

.. tabs::
 .. code-tab:: gdscript GDScript

    extends RigidBody3D

    func look_follow(state, current_transform, target_position):
    	var facing_direction = current_transform.basis.z
    	var desired_direction = current_transform.origin.direction_to(target_position)
    	
    	var dot_product = facing_direction.dot(desired_direction)
    	var cross_product = facing_direction.cross(desired_direction)	
    	var facing_dir_magnitude = facing_direction.length()
    	var desired_dir_magnitude = desired_direction.length()
    	
    	# The difference from the current orientation to the desired orientation in radians
    	var angle_variance_radians = acos(dot_product / (facing_dir_magnitude * desired_dir_magnitude))
    	
    	# This will return positive or negative and give us an indication of direction that we can use to differentiate.  
    	# For example, we don't want to turn 270 degrees right, we want 90 degrees left, etc...	
    	var perpendicular_magnitude = cross_product / (facing_dir_magnitude * desired_dir_magnitude)
    
    	# Lerp has limited effect when used in the physics process instead of being called in _PhysicsProcess.
    	# Instead, we will shift the time step here to control/keep the entire movement from happening in a single frame.
    	# The higher this is, the slower the rotation will be.
    	var lerp_offset = 10
    	
    	# If input-based, it may be good to check that there is input as well
    	if (angle_variance_radians > 0):
    		state.angular_velocity = Vector3.UP * (angle_variance_radians / (state.step * lerp_offset)) \
    		# This bit controls the direction of turning
    		* sign(perpendicular_magnitude.y)

    func _integrate_forces(state):
	    look_follow(state, global_transform, TargetPosition)

 .. code-tab:: csharp

    using Godot;

    public partial class MyRigidBody3D : RigidBody3D
    {
        private void LookFollow(PhysicsDirectBodyState3D state, Transform3D currentTransform, Vector3 targetPosition)
        {
            var facingDirection = currentTransform.Basis.Z;
            var desiredDirection = (targetPosition - currentTransform.Origin).Normalized();
    
    		var dotProduct = facingDirection.Dot(desiredDirection);
    		var crossProduct = facingDirection.Cross(desiredDirection);
    		var facingDirMagnitude = facingDirection.Length();
    		var desiredDirMagnitude = desiredDirection.Length();
    
    		// The difference from the current orientation to the desired orientation in radians
    		var angleVarianceRadians = Mathf.Acos(dotProduct / (facingDirMagnitude * desiredDirMagnitude));
    
    		// This will return positive or negative and give us an indication of direction that we can use to differentiate.  
    		// For example, we don't want to turn 270 degrees right, we want 90 degrees left, etc...
    		var perpendicularMagnitude = crossProduct / (facingDirMagnitude * desiredDirMagnitude);
    
    		// Lerp has limited effect when used in the physics process instead of being called in _PhysicsProcess.
    		// Instead, we will shift the time step here to control/keep the entire movement from happening in a single frame.
    		// The higher this is, the slower the rotation will be.
    		var LerpOffset = 10f;
    
    		// If input-based, it may be good to check that there is input as well
    		if (angleVarianceRadians > 0f)
    		{
    			state.AngularVelocity = Vector3.Up * (angleVarianceRadians / (state.Step * LerpOffset)) 
    			// This bit controls the direction of turning
    			* Mathf.Sign(perpendicularMagnitude.Y);	
    		}
        }
    
        public override void _IntegrateForces(PhysicsDirectBodyState3D state)
        {
    		LookFollow(state, GlobalTransform, targetPosition);
        }
    }


This method uses the rigid body's ``angular_velocity`` property to rotate the body. It first calculates the difference between the current and desired angle and then adds the velocity needed to rotate by that amount in one frame's time.

.. note:: This script will not work with rigid bodies in *character mode* because then, the body's rotation is locked. In that case, you would have to rotate the attached mesh node instead using the standard Node3D methods.
