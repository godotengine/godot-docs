.. _doc_collision_shapes_2d:

Collision shapes (2D)
=====================

This guide explains:

- The types of collision shapes available in 2D in Godot.
- Using an image converted to a polygon as a collision shape.
- Performance considerations regarding 2D collisions.

Godot provides many kinds of collision shapes, with different performance and
accuracy tradeoffs.

You can define the shape of a :ref:`class_PhysicsBody2D` by adding one or more
:ref:`CollisionShape2Ds <class_CollisionShape2D>` or
:ref:`CollisionPolygon2Ds <class_CollisionPolygon2D>` as child nodes.
Note that you must add a :ref:`class_Shape2D` *resource* to collision shape
nodes in the Inspector dock.

.. note::

    When you add multiple collision shapes to a single PhysicsBody2D, you don't
    have to worry about them overlapping. They won't "collide" with each other.

Primitive collision shapes
--------------------------

Godot provides the following primitive collision shape types:

- :ref:`class_RectangleShape2D`
- :ref:`class_CircleShape2D`
- :ref:`class_CapsuleShape2D`
- :ref:`class_SegmentShape2D`
- :ref:`class_SeparationRayShape2D` (designed for characters)
- :ref:`class_WorldBoundaryShape2D` (infinite plane)

You can represent the collision of most smaller objects using one or more
primitive shapes. However, for more complex objects, such as a large ship or a
whole level, you may need convex or concave shapes instead. More on that below.

We recommend favoring primitive shapes for dynamic objects such as RigidBodies
and CharacterBodies as their behavior is the most reliable. They often provide
better performance as well.

Convex collision shapes
-----------------------

.. warning::

    Godot currently doesn't offer a built-in way to create 2D convex collision
    shapes. This section is mainly here for reference purposes.

:ref:`Convex collision shapes <class_ConvexPolygonShape2D>` are a compromise
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

Concave or trimesh collision shapes
-----------------------------------

:ref:`Concave collision shapes <class_ConcavePolygonShape2D>`, also called trimesh
collision shapes, can take any form, from a few triangles to thousands of
triangles. Concave shapes are the slowest option but are also the most accurate
in Godot. **You can only use concave shapes within StaticBodies.** They will not
work with CharacterBodies or RigidBodies unless the RigidBody's mode is Static.

.. note::

    Even though concave shapes offer the most accurate *collision*, contact
    reporting can be less precise than primitive shapes.

When not using TileMaps for level design, concave shapes are the best approach
for a level's collision.

You can configure the CollisionPolygon2D node's *build mode* in the inspector.
If it is set to **Solids** (the default), collisions will include the polygon
and its contained area. If it is set to **Segments**, collisions will only
include the polygon edges.

You can generate a concave collision shape from the editor by selecting a Sprite2D
and using the **Sprite2D** menu at the top of the 2D viewport. The Sprite2D menu
dropdown exposes an option called **Create CollisionPolygon2D Sibling**.
Once you click it, it displays a menu with 3 settings:

- **Simplification:** Higher values will result in a less detailed shape, which
  improves performance at the cost of accuracy.
- **Shrink (Pixels):** Higher values will shrink the generated collision polygon
  relative to the sprite's edges.
- **Grow (Pixels):** Higher values will grow the generated collision polygon
  relative to the sprite's edges. Note that setting Grow and Shrink to equal
  values may yield different results than leaving both of them on 0.

.. note::

    If you have an image with many small details, it's recommended to create a
    simplified version and use it to generate the collision polygon. This
    can result in better performance and game feel, since the player won't
    be blocked by small, decorative details.

    To use a separate image for collision polygon generation, create another
    Sprite2D, generate a collision polygon sibling from it then remove the Sprite2D
    node. This way, you can exclude small details from the generated collision.

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
