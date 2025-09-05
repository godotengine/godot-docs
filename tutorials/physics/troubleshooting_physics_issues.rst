.. _doc_troubleshooting_physics_issues:

Troubleshooting physics issues
==============================

When working with a physics engine, you may encounter unexpected results.

While many of these issues can be resolved through configuration, some of them
are the result of engine bugs. For known issues related to the physics engine,
see
`open physics-related issues on GitHub <https://github.com/godotengine/godot/issues?q=is%3Aopen+is%3Aissue+label%3Atopic%3Aphysics>`__.
Looking through `closed issues
<https://github.com/godotengine/godot/issues?q=+is%3Aclosed+is%3Aissue+label%3Atopic%3Aphysics>`__
can also help answer questions related to physics engine behavior.

Objects are passing through each other at high speeds
-----------------------------------------------------

This is known as *tunneling*. Enabling **Continuous CD** in the RigidBody
properties can sometimes resolve this issue. If this does not help, there are
other solutions you can try:

- Make your static collision shapes thicker. For example, if you have a thin
  floor that the player can't get below in some way, you can make the collider
  thicker than the floor's visual representation.
- Modify your fast-moving object's collision shape depending on its movement
  speed. The faster the object moves, the larger the collision shape should
  extend outside of the object to ensure it can collide with thin walls more
  reliably.
- Increase :ref:`Physics Ticks per Second<class_ProjectSettings_property_physics/common/physics_ticks_per_second>`
  in the advanced Project Settings. While
  this has other benefits (such as more stable simulation and reduced input
  lag), this increases CPU utilization and may not be viable for mobile/web
  platforms. Multipliers of the default value of ``60`` (such as ``120``, ``180``
  or ``240``) should be preferred for a smooth appearance on most displays.

Stacked objects are unstable and wobbly
---------------------------------------

Despite seeming like a simple problem, stable RigidBody simulation with stacked
objects is difficult to implement in a physics engine. This is caused by
integrating forces going against each other. The more stacked objects are
present, the stronger the forces will be against each other. This eventually
causes the simulation to become wobbly, making the objects unable to rest on top
of each other without moving.

Increasing the physics simulation rate can help alleviate this issue. To do so,
increase :ref:`Physics Ticks per Second<class_ProjectSettings_property_physics/common/physics_ticks_per_second>`
in the advanced Project Settings. Note
that increases CPU utilization and may not be viable for mobile/web platforms.
Multipliers of the default value of ``60`` (such as ``120``, ``180`` or ``240``)
should be preferred for a smooth appearance on most displays.

In 3D, switching the physics engine from the default GodotPhysics to Jolt
can also improve stability. See :ref:`doc_using_jolt_physics` for more information.

Scaled physics bodies or collision shapes do not collide correctly
------------------------------------------------------------------

Godot does not currently support scaling of physics bodies or collision shapes.
As a workaround, change the collision shape's extents instead of changing its
scale. If you want the visual representation's scale to change as well, change
the scale of the underlying visual representation (Sprite2D, MeshInstance3D, …)
and change the collision shape's extents separately. Make sure the collision
shape is not a child of the visual representation in this case.

Since resources are shared by default, you'll have to make the collision shape
resource unique if you don't want the change to be applied to all nodes using
the same collision shape resource in the scene. This can be done by calling
``duplicate()`` in a script on the collision shape resource *before* changing
its size.

Thin objects are wobbly when resting on the floor
-------------------------------------------------

This can be due to one of two causes:

- The floor's collision shape is too thin.
- The RigidBody's collision shape is too thin.

In the first case, this can be alleviated by making the floor's collision shape
thicker. For example, if you have a thin floor that the player can't get below
in some way, you can make the collider thicker than the floor's visual
representation.

In the second case, this can usually only be resolved by increasing the physics
simulation rate (as making the shape thicker would cause a disconnect between
the RigidBody's visual representation and its collision).

In both cases, increasing the physics simulation rate can also help alleviate
this issue. To do so, increase
:ref:`Physics Ticks per Second<class_ProjectSettings_property_physics/common/physics_ticks_per_second>`
in the advanced
Project Settings. Note that this increases CPU utilization and may not be viable
for mobile/web platforms. Multipliers of the default value of ``60`` (such as
``120``, ``180`` or ``240``) should be preferred for a smooth appearance on most
displays.

Cylinder collision shapes are unstable
--------------------------------------

Switching the physics engine from the default GodotPhysics to Jolt
should make cylinder collision shapes more reliable.
See :ref:`doc_using_jolt_physics` for more information.

During the transition from Bullet to GodotPhysics in Godot 4, cylinder collision
shapes had to be reimplemented from scratch. However, cylinder collision shapes
are one of the most difficult shapes to support, which is why many other physics
engines don't provide any support for them. There are several known bugs with
cylinder collision shapes currently.

If you are sticking to GodotPhysics, we recommend using box or capsule collision
shapes for characters for now. Boxes generally provide the best reliability,
but have the downside of making the character take more space diagonally.
Capsule collision shapes do not have this downside, but their shape can make
precision platforming more difficult.

VehicleBody simulation is unstable, especially at high speeds
-------------------------------------------------------------

When a physics body moves at a high speed, it travels a large distance between
each physics step. For instance, when using the 1 unit = 1 meter convention in
3D, a vehicle moving at 360 km/h will travel 100 units per second. With the
default physics simulation rate of 60 Hz, the vehicle moves by ~1.67 units each
physics tick. This means that small objects may be ignored entirely by the
vehicle (due to tunneling), but also that the simulation has little data to work
with in general at such a high speed.

Fast-moving vehicles can benefit a lot from an increased physics simulation
rate. To do so, increase
:ref:`Physics Ticks per Second<class_ProjectSettings_property_physics/common/physics_ticks_per_second>`
in the advanced Project
Settings. Note that this increases CPU utilization and may not be viable for
mobile/web platforms. Multipliers of the default value of ``60`` (such as
``120``, ``180`` or ``240``) should be preferred for a smooth appearance on most
displays.

Collision results in bumps when an object moves across tiles
------------------------------------------------------------

This is a known issue in the physics engine caused by the object bumping on a
shape's edges, even though that edge is covered by another shape. This can occur
in both 2D and 3D.

The best way to work around this issue is to create a "composite" collider. This
means that instead of individual tiles having their collision, you create a
single collision shape representing the collision for a group of tiles.
Typically, you should split composite colliders on a per-island basis (which
means each group of touching tiles gets its own collider).

Using a composite collider can also improve physics simulation performance in
certain cases. However, since the composite collision shape is much more
complex, this may not be a net performance win in all cases.

.. tip::

    In Godot 4.5 and later, creating a composite collider is automatically done
    when using a TileMapLayer node. The chunk size (``16`` tiles on each axis
    by default) can be set using the **Physics Quadrant Size** property in the
    TileMapLayer inspector. Larger values provide more reliable collision,
    at the cost of slower updates when the TileMap is changed.

Framerate drops when an object touches another object
-----------------------------------------------------

This is likely due to one of the objects using a collision shape that is too
complex. Convex collision shapes should use a number of shapes as low as
possible for performance reasons. When relying on Godot's automatic generation,
it's possible that you ended up with dozens if not hundreds of shapes created
for a single convex shape collision resource.

In some cases, replacing a convex collider with a couple of primitive collision
shapes (box, sphere, or capsule) can deliver better performance.

This issue can also occur with StaticBodies that use very detailed trimesh
(concave) collisions. In this case, use a simplified representation of the level
geometry as a collider. Not only this will improve physics simulation
performance significantly, but this can also improve stability by letting you
remove small fixtures and crevices from being considered by collision.

In 3D, switching the physics engine from the default GodotPhysics to Jolt
can also improve performance. See :ref:`doc_using_jolt_physics` for more information.

Framerate suddenly drops to a very low value beyond a certain amount of physics simulation
------------------------------------------------------------------------------------------

This occurs because the physics engine can't keep up with the expected
simulation rate. In this case, the framerate will start dropping, but the engine
is only allowed to simulate a certain number of physics steps per rendered
frame. This snowballs into a situation where framerate keeps dropping until it
reaches a very low framerate (typically 1-2 FPS) and is called the *physics
spiral of death*.

To avoid this, you should check for situations in your project that can cause
excessive number of physics simulations to occur at the same time (or with
excessively complex collision shapes). If these situations cannot be avoided,
you can increase the **Max Physics Steps per Frame** project setting and/or
reduce **Physics Ticks per Second** to alleviate this.

Physics simulation is unreliable when far away from the world origin
--------------------------------------------------------------------

This is caused by floating-point precision errors, which become more pronounced
as the physics simulation occurs further away from the world origin. This issue
also affects rendering, which results in wobbly camera movement when far away
from the world origin. See :ref:`doc_large_world_coordinates` for more
information.
