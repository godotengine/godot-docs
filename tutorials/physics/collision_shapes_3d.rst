.. _doc_collision_shapes_3d:

Collision shapes (3D)
=====================

This guide explains:

- The types of collision shapes available in 3D in Godot.
- Using a convex or a concave mesh as a collision shape.
- Performance considerations regarding 3D collisions.

Godot provides many kinds of collision shapes, with different performance and
accuracy tradeoffs.

You can define the shape of a :ref:`class_PhysicsBody3D` by adding one or more
:ref:`CollisionShape3Ds <class_CollisionShape3D>` as child nodes. Note that you must
add a :ref:`class_Shape3D` *resource* to collision shape nodes in the Inspector
dock.

.. note::

    When you add multiple collision shapes to a single PhysicsBody, you don't
    have to worry about them overlapping. They won't "collide" with each other.

Primitive collision shapes
--------------------------

Godot provides the following primitive collision shape types:

- :ref:`class_BoxShape3D`
- :ref:`class_SphereShape3D`
- :ref:`class_CapsuleShape3D`
- :ref:`class_CylinderShape3D`

You can represent the collision of most smaller objects using one or more
primitive shapes. However, for more complex objects, such as a large ship or a
whole level, you may need convex or concave shapes instead. More on that below.

We recommend favoring primitive shapes for dynamic objects such as RigidBodies
and CharacterBodies as their behavior is the most reliable. They often provide
better performance as well.

Convex collision shapes
-----------------------

:ref:`Convex collision shapes <class_ConvexPolygonShape3D>` are a compromise
between primitive collision shapes and concave collision shapes. They can
represent shapes of any complexity, but with an important caveat. As their name
implies, an individual shape can only represent a *convex* shape. For instance,
a pyramid is *convex*, but a hollow box is *concave*. To define a concave object
with a single collision shape, you need to use a concave collision shape.

Depending on the object's complexity, you may get better performance by using
multiple convex shapes instead of a concave collision shape. Godot lets you use
*convex decomposition* to generate convex shapes that roughly match a hollow
object. Note this performance advantage no longer applies after a certain amount
of convex shapes. For large and complex objects such as a whole level, we
recommend using concave shapes instead.

You can generate one or several convex collision shapes from the editor by
selecting a MeshInstance3D and using the **Mesh** menu at the top of the 3D
viewport. The editor exposes two generation modes:

- **Create Single Convex Collision Sibling** uses the Quickhull algorithm. It
  creates one CollisionShape node with an automatically generated convex
  collision shape. Since it only generates a single shape, it provides good
  performance and is ideal for small objects.

- **Create Multiple Convex Collision Siblings** uses the V-HACD algorithm. It
  creates several CollisionShape nodes, each with a convex shape. Since it
  generates multiple shapes, it is more accurate for concave objects at the cost
  of performance. For objects with medium complexity, it will likely be faster
  than using a single concave collision shape.

Concave or trimesh collision shapes
-----------------------------------

:ref:`Concave collision shapes <class_ConcavePolygonShape3D>`, also called trimesh
collision shapes, can take any form, from a few triangles to thousands of
triangles. Concave shapes are the slowest option but are also the most accurate
in Godot. **You can only use concave shapes within StaticBodies.** They will not
work with CharacterBodies or RigidBodies unless the RigidBody's mode is Static.

.. note::

    Even though concave shapes offer the most accurate *collision*, contact
    reporting can be less precise than primitive shapes.

When not using GridMaps for level design, concave shapes are the best approach
for a level's collision. That said, if your level has small details, you may
want to exclude those from collision for performance and game feel. To do so,
you can build a simplified collision mesh in a 3D modeler and have Godot
generate a collision shape for it automatically. More on that below

Note that unlike primitive and convex shapes, a concave collision shape doesn't
have an actual "volume". You can place objects both *outside* of the shape as
well as *inside*.

You can generate a concave collision shape from the editor by selecting a
MeshInstance3D and using the **Mesh** menu at the top of the 3D viewport. The
editor exposes two options:

- **Create Trimesh Static Body** is a convenient option. It creates a StaticBody
  containing a concave shape matching the mesh's geometry.

- **Create Trimesh Collision Sibling** creates a CollisionShape node with a
  concave shape matching the mesh's geometry.

.. seealso::

    See :ref:`doc_importing_3d_scenes` for information on how to export models
    for Godot and automatically generate collision shapes on import.

Performance caveats
-------------------

You aren't limited to a single collision shape per PhysicsBody. Still, we
recommend keeping the number of shapes as low as possible to improve
performance, especially for dynamic objects like RigidBodies and
CharacterBodies. On top of that, avoid translating, rotating, or scaling
CollisionShapes to benefit from the physics engine's internal optimizations.

When using a single non-transformed collision shape in a StaticBody, the
engine's *broad phase* algorithm can discard inactive PhysicsBodies. The *narrow
phase* will then only have to take into account the active bodies' shapes. If a
StaticBody has many collision shapes, the broad phase will fail. The narrow
phase, which is slower, must then perform a collision check against each shape.

If you run into performance issues, you may have to make tradeoffs in terms of
accuracy. Most games out there don't have a 100% accurate collision. They find
creative ways to hide it or otherwise make it unnoticeable during normal
gameplay.
