.. _doc_using_jolt_physics:

Using Jolt Physics
==================

Introduction
------------

The Jolt physics engine was added as an alternative to the existing Godot Physics
physics engine in 4.4. Jolt is developed by Jorrit Rouwe with a focus on games and
VR applications. Previously it was available as an extension but is now built into
Godot.

It is important to note that the built-in Jolt Physics module is considered
**not finished**, **experimental**, and **lacks feature parity** with both
Godot Physics and the Godot Jolt extension. Behavior may change as it is developed
further. Please keep that in mind when choosing what to use for your project.

The existing extension is now considered in maintenance mode. That means bug fixes
will be merged, and it will be kept compatible with new versions of Godot until
the built-in module has feature parity with the extension. The extension can be
found `here on GitHub <https://github.com/godot-jolt/godot-jolt>`_ and in Godot's asset
library.

To change the 3D physics engine to be Jolt Physics, set
:ref:`Project Settings > Physics > 3D > Physics Engine<class_ProjectSettings_property_physics/3D/Physics_Engine>`
to ``Jolt Physics``. Once you've done that, click the **Save & Restart** button.
When the editor opens again, 3D scenes should now be using Jolt for physics.

Notable differences to Godot Physics
------------------------------------

There are many differences between the existing Godot Physics engine and Jolt.

Joint properties
~~~~~~~~~~~~~~~~

The current interfaces for the 3D joint nodes don't quite line up with the interface
of Jolt's own joints. As such, there are a number of joint properties that are not
supported, mainly ones related to configuring the joint's soft limits.

The unsupported properties are:

- PinJoint3D: ``bias``, ``damping``, ``impulse_clamp``
- HingeJoint3D: ``bias``, ``softness``, ``relaxation``
- SliderJoint3D: ``angular_\*``, ``\*_limit/softness``, ``\*_limit/restitution``, ``\*_limit/damping``
- ConeTwistJoint3D: ``bias``, ``relaxation``, ``softness``
- Generic6DOFJoint3D: ``*_limit_*/softness``, ``*_limit_*/restitution``, ``*_limit_*/damping``, ``*_limit_*/erp``

Currently a warning is emitted if you set these properties to anything but their
default values.

Single-body joints
~~~~~~~~~~~~~~~~~~

You can, in Godot, omit one of the joint bodies for a two-body joint and effectively
have "the world" be the other body. However, the node path that you assign your body
to (:ref:`node_a<class_Joint3D_property_node_a>` vs :ref:`node_b<class_Joint3D_property_node_b>`)
is ignored. Godot Physics will always behave as if you
assigned it to ``node_a``, and since ``node_a`` is also what defines the frame of reference
for the joint limits, you end up with inverted limits and a potentially strange
limit shape, especially if your limits allow both linear and angular degrees of
freedom.

Jolt will behave as if you assigned the body to ``node_b`` instead, with ``node_a``
representing "the world". There is a project setting called :ref:`Physics > Jolt Physics 3D > Joints > World Node<class_ProjectSettings_property_physics/jolt_physics_3d/joints/world_node>`
that lets you toggle this behavior, if you need compatibility for an existing project.

Collision margins
~~~~~~~~~~~~~~~~~

Jolt (and other similar physics engines) uses something that Jolt refers to as
"convex radius" to help improve the performance and behavior of the types of
collision detection that Jolt relies on for convex shapes. Other physics engines
(Godot included) might refer to these as "collision margins" instead. Godot exposes
these as the ``margin`` property on every Shape3D-derived class, but Godot Physics
itself does not use them for anything.

What these collision margins sometimes do in other engines (as described in Godot's
documentation) is effectively add a "shell" around the shape, slightly increasing
its size while also rounding off any edges/corners. In Jolt however, these margins
are first used to shrink the shape, and then the "shell" is applied, resulting in
edges/corners being similarly rounded off, but without increasing the size of the
shape.

To prevent having to tweak this margin property manually, since its default value
can be problematic for smaller shapes, the Jolt module exposes a project setting
called :ref:`Physics > Jolt Physics 3D > Collisions > Collision Margin Fraction<class_ProjectSettings_property_physics/jolt_physics_3d/collisions/collision_margin_fraction>`
which is multiplied with the smallest axis of the shape's AABB to calculate the
actual margin. The margin property of the shape is then instead used as an upper
bound.

These margins should, for most use-cases, be more or less transparent, but can
sometimes result in odd collision normals when performing shape queries. You can
lower the above mentioned project setting to mitigate some of this, including
setting it to ``0.0``, but too small of a margin can also cause odd collision results,
so is generally not recommended.

Baumgarte stabilization
~~~~~~~~~~~~~~~~~~~~~~~

Baumgarte stabilization is a method to resolve penetrating bodies and push them to a
state where they are just touching. In Godot Physics this works like a spring. This
means that bodies can accelerate and may cause the bodies to overshoot and separate
completely. With Jolt, the stabilization is only applied to the position and not to
the velocity of the body. This means it cannot overshoot but it may take longer to
resolve the penetration.

The strength of this stabilization can be tweaked using the project setting
:ref:`Physics > Jolt Physics 3D > Simulation > Baumgarte Stabilization Factor<class_ProjectSettings_property_physics/jolt_physics_3d/simulation/baumgarte_stabilization_factor>`.
Setting this project setting to ``0.0`` will turn Baumgarte stabilization off.
Setting it to ``1.0`` will resolve penetration in 1 simulation step. This is fast
but often also unstable.

Ghost collisions
~~~~~~~~~~~~~~~~

Jolt employs two techniques to mitigate ghost collisions, meaning collisions with
internal edges of shapes/bodies that result in collision normals that oppose the
direction of movement.

The first technique, called "active edge detection", marks edges of triangles in
:ref:`class_ConcavePolygonShape3D` or :ref:`class_HeightMapShape3D` as either "active" or "inactive", based on
the angle to the neighboring triangle. When a collision happens with an inactive
edge the collision normal will be replaced with the triangle's normal instead, to
lessen the effect of ghost collisions.

The angle threshold for this active edge detection is configurable through the
project setting :ref:`Physics >Jolt Physics 3D > Collisions > Active Edge Threshold<class_ProjectSettings_property_physics/jolt_physics_3d/collisions/active_edge_threshold>`.

The second technique, called "enhanced internal edge removal", instead adds runtime
checks to detect whether an edge is active or inactive, based on the contact points
of the two bodies. This has the benefit of applying not only to collisions with
:ref:`class_ConcavePolygonShape3D` and :ref:`class_HeightMapShape3D`, but also edges between any shapes within
the same body.

Enhanced internal edge removal can be toggled on and off for the various contexts to
which it's applied, using the :ref:`Physics >Jolt Physics 3D > Simulation > Use Enhanced Internal Edge Removal<class_ProjectSettings_property_physics/jolt_physics_3d/simulation/use_enhanced_internal_edge_removal>`,
project setting, and the similar settings for :ref:`queries<class_ProjectSettings_property_physics/jolt_physics_3d/queries/use_enhanced_internal_edge_removal>`
and :ref:`motion queries<class_ProjectSettings_property_physics/jolt_physics_3d/motion_queries/use_enhanced_internal_edge_removal>`.

Note that neither the active edge detection nor enhanced internal edge removal apply
when dealing with ghost collisions between two different bodies.

Memory usage
~~~~~~~~~~~~

Jolt uses a stack allocator for temporary allocations within its simulation step.
This stack allocator requires allocating a set amount of memory up front, which can
be configured using the :ref:`Physics > Jolt Physics 3D > Limits > Temporary Memory Buffer Size<class_ProjectSettings_property_physics/jolt_physics_3d/limits/temporary_memory_buffer_size>`
project setting.

Ray-cast face index
~~~~~~~~~~~~~~~~~~~

The ``face_index`` property returned in the results of :ref:`intersect_ray()<class_PhysicsDirectSpaceState3D_method_intersect_ray>`
and RayCast3D will by default always be ``-1`` with Jolt. The project setting :ref:`Physics > Jolt Physics 3D > Queries > Enable Ray Cast Face Index<class_ProjectSettings_property_physics/jolt_physics_3d/queries/enable_ray_cast_face_index>`
will enable them.

Note that enabling this setting will increase the memory requirement of :ref:`class_ConcavePolygonShape3D`
with about 25%.

Kinematic RigidBody3D contacts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When using Jolt, a :ref:`class_RigidBody3D` frozen with :ref:`FREEZE_MODE_KINEMATIC<class_RigidBody3D_constant_FREEZE_MODE_KINEMATIC>`
will by default not report contacts from collisions with other static/kinematic
bodies, for performance reasons, even when setting a non-zero :ref:`max_contacts_reported<class_RigidBody3D_property_max_contacts_reported>`.
If you have many/large kinematic bodies overlapping with complex static geometry,
such as :ref:`class_ConcavePolygonShape3D` or :ref:`class_HeightMapShape3D`, you can
end up wasting a significant amount of CPU performance and memory without realizing
it.

For this reason this behavior is opt-in through the project setting
:ref:`Physics > Jolt Physics 3D > Simulation > Generate All Kinematic Contacts<class_ProjectSettings_property_physics/jolt_physics_3d/simulation/generate_all_kinematic_contacts>`.

Contact impulses
~~~~~~~~~~~~~~~~

Due to limitations internal to Jolt, the contact impulses provided by :ref:`PhysicsDirectBodyState3D.get_contact_impulse()<class_physicsdirectbodystate3d_method_get_contact_impulse>`
are estimated ahead of time based on things like the contact manifold and velocities
of the colliding bodies. This means that the reported impulses will only be accurate
in cases where the two bodies in question are not colliding with any other bodies.

Area3D and SoftBody3D
~~~~~~~~~~~~~~~~~~~~~

Jolt does not currently support any interactions between :ref:`class_SoftBody3D`
and :ref:`class_Area3D`, such as overlap events, or the wind properties found on
:ref:`class_Area3D`.

WorldBoundaryShape3D
~~~~~~~~~~~~~~~~~~~~

:ref:`class_WorldBoundaryShape3D`, which is meant to represent an infinite plane, is
implemented a bit differently in Jolt compared to Godot Physics. Both engines have
an upper limit for how big the effective size of this plane can be, but this size is
much smaller when using Jolt, in order to avoid precision issues.

You can configure this size using the :ref:`Physics > Jolt Physics 3D > Limits > World Boundary Shape Size<class_ProjectSettings_Property_physics/jolt_physics_3d/limits/world_boundary_shape_size>`
project setting.

Notable differences to the Godot Jolt extension
-----------------------------------------------

While the built-in Jolt module is largely a straight port of the Godot Jolt
extension, there are a few things that are different.

Project settings
~~~~~~~~~~~~~~~~

All project settings have been moved from the ``physics/jolt_3d`` category to
``physics/jolt_physics_3d``.

On top of that, there's been some renaming and refactoring of the individual project
settings as well. These include:

- ``sleep/enabled`` is now ``simulation/allow_sleep.``
- ``sleep/velocity_threshold`` is now ``simulation/sleep_velocity_threshold.``
- ``sleep/time_threshold`` is now ``simulation/sleep_time_threshold.``
- ``collisions/use_shape_margins`` is now ``collisions/collision_margin_fraction``,
  where a value of 0 is equivalent to disabling it.
- ``collisions/use_enhanced_internal_edge_removal`` is now ``simulation/use_enhanced_internal_edge_removal.``
- ``collisions/areas_detect_static_bodies`` is now ``simulation/areas_detect_static_bodies.``
- ``collisions/report_all_kinematic_contacts`` is now ``simulation/generate_all_kinematic_contacts.``
- ``collisions/soft_body_point_margin`` is now ``simulation/soft_body_point_radius.``
- ``collisions/body_pair_cache_enabled is now simulation/body_pair_contact_cache_enabled.``
- ``collisions/body_pair_cache_distance_threshold`` is ``now simulation/body_pair_contact_cache_distance_threshold.``
- ``collisions/body_pair_cache_angle_threshold is now simulation/body_pair_contact_cache_angle_threshold.``
- ``continuous_cd/movement_threshold`` is now ``simulation/continuous_cd_movement_threshold``,
  but expressed as a fraction instead of a percentage.
- ``continuous_cd/max_penetration`` is now ``simulation/continuous_cd_max_penetration``,
  but expressed as a fraction instead of a percentage.
- ``kinematics/use_enhanced_internal_edge_removal`` is now ``motion_queries/use_enhanced_internal_edge_removal.``
- ``kinematics/recovery_iterations`` is now ``motion_queries/recovery_iterations``,
  but expressed as a fraction instead of a percentage.
- ``kinematics/recovery_amount`` is now ``motion_queries/recovery_amount.``
- ``queries/use_legacy_ray_casting`` has been removed.
- ``solver/position_iterations`` is now ``simulation/position_steps.``
- ``solver/velocity_iterations`` is now ``simulation/velocity_steps.``
- ``solver/position_correction`` is now ``simulation/baumgarte_stabilization_factor``,
  but expressed as a fraction instead of a percentage.
- ``solver/active_edge_threshold`` is now ``collisions/active_edge_threshold.``
- ``solver/bounce_velocity_threshold`` is now ``simulation/bounce_velocity_threshold.``
- ``solver/contact_speculative_distance`` is now ``simulation/speculative_contact_distance.``
- ``solver/contact_allowed_penetration`` is now ``simulation/penetration_slop.``
- ``limits/max_angular_velocity`` is now stored as radians instead.
- ``limits/max_temporary_memory`` is now ``limits/temporary_memory_buffer_size.``

Joint nodes
~~~~~~~~~~~

The joint nodes that are exposed in the Godot Jolt extension (JoltPinJoint3D,
JoltHingeJoint3D, JoltSliderJoint3D, JoltConeTwistJoint3D, and JoltGeneric6DOFJoint)
have not been included in the Jolt module.

Thread safety
~~~~~~~~~~~~~

Unlike the Godot Jolt extension, the Jolt module does have thread-safety,
including support for the :ref:`Physics > 3D > Run On Separate Thread<class_ProjectSettings_Property_physics/3d/run_on_separate_thread>`
project setting. However this has not been tested very thoroughly, so it should be
considered experimental.
