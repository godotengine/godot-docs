.. _doc_collision_shapes_3d:

Collision shapes (3D)
=====================

Godot provides many kinds of collision shapes, with different performance and
accuracy tradeoffs.

You can define the body form of a :ref:`class_PhysicsBody` by adding one or more
:ref:`CollisionShapes <class_CollisionShape>` as child nodes. These nodes act as
shape holders. In these child nodes, you must add a :ref:`class_Shape`
*resource* that will define the actual shape of the collision.

.. note::

    When you add multiple collision shapes to a single PhysicsBody, you don't
    have to worry about overlapping shapes since these won't "collide" with each
    other.

Primitive collision shapes
--------------------------

Godot provides the following primitive collision shape types:

- :ref:`class_BoxShape`
- :ref:`class_SphereShape`
- :ref:`class_CapsuleShape`
- :ref:`class_CylinderShape` (only when using the Bullet physics engine)

Using one or several primitive collision shapes, you can represent the collision
of most smaller objects well. However, for more complex objects such as a large
ship or a whole level, you may want to use convex shapes or concave shapes
instead (see below).

Primitive shapes are recommended for dynamic objects such as RigidBodies and
KinematicBodies, as their behavior usually is the most reliable and predictable.
On top of that, they often provide better performance as well.

Convex collision shapes
-----------------------

:ref:`Convex collision shapes <class_ConvexPolygonShape>` are a compromise
between primitive collision shapes and concave collision shapes. They can
represent shapes of any complexity, but with an important caveat. As their name
implies, an individual shape can only represent a *convex* shape. For instance,
a pyramid is *convex* but a hollow box is *concave*. To represent a concave
object with a single collision shape, you need to use a concave collision shape
(see below).

However, depending on the object's complexity, you may get better performance by
using multiple convex shapes instead of a concave collision shape. This is why
Godot lets you make use of *convex decomposition* to generate convex shapes that
roughly match a concave object. That said, this performance advantage no longer
applies after a certain amount of convex shapes. Due to this, for large and
complex objects such as a whole level, it's recommended to use concave shapes
instead.

You can generate one or several convex collision shapes from the editor by
selecting a MeshInstance and using the **Mesh** menu at the top of the 3D
viewport. The editor exposes two generation modes:

- **Create Single Convex Collision Sibling** uses the Quickhull algorithm.
  It creates one CollisionShape node with an automatically generated convex
  collision shape. Since it only generates a single shape, it provides better
  performance and is recommended for small objects.

- **Create Multiple Convex Collision Siblings** uses the V-HACD algorithm.
  It creates several CollisionShape nodes, each with their own convex collision
  shape. Since it generates multiple shapes, it is more accurate for concave
  objects at the cost of performance. For objects with medium complexity, it
  will likely be faster than using a single concave collision shape.

Concave (trimesh) collision shapes
----------------------------------

:ref:`Concave collision shapes <class_ConcavePolygonShape>` (also called trimesh
collision shapes) can take any form, from a few triangles to thousands of
triangles. Concave shapes are the slowest option, but are also the most accurate
collision shapes available in Godot. **Concave shapes can only be used within
StaticBodies.** They will not work with KinematicBodies or RigidBodies unless
the RigidBody's mode is set to Static.

.. note::

    Even though concave shapes offer the most accurate *collision*, contact
    reporting can be less accurate compared to primitive shapes.

When not using GridMaps for level design, concave collision shapes are usually
the best approach for level collision. That said, if your level has small
details, you will probably want to exclude those from collision for better
performance and reliability. To do so, you can build a simplified collision mesh
in a 3D modeler and have Godot generate a collision shape for it automatically
(see below).

Note that unlike primitive and convex shapes, a concave collision shape doesn't
have an actual "volume". Objects can be placed both *outside* of the shape as
well as *inside*.

You can generate a concave collision shape from the editor by selecting a
MeshInstance and using the **Mesh** menu at the top of the 3D viewport.
The editor exposes two generation options:

- **Create Trimesh Static Body** is a convenience option. It will create a
  StaticBody containing a concave shape matching the mesh's geometry.

- **Create Trimesh Collision Sibling** will create a CollisionShape node
  containing the a concave shape matching the mesh's geometry.

.. note::

    If you need to make a RigidBody *slide* on a concave collision shape, you
    may notice that sometimes, the RigidBody will bump upwards. To solve this,
    open **Project > Project Settings** and enable
    **Physics > 3d > Smooth Trimesh Collision**.

    Once you've enabled smooth trimesh collision, make sure the concave shape is
    the only shape of your StaticBody and that it's at located at its origin
    without any rotation. This way, the RigidBody should slide perfectly on the
    StaticBody.

.. seealso::

    Godot can generate collision shapes for your imported 3D scenes
    automatically. See :ref:`doc_importing_scenes_import_hints` in the
    documentation for more information.

Performance caveats
-------------------

While you aren't limited to a single collision shape per PhysicsBody, it's
recommended to keep the number of shapes as low as possible to improve
performance. This is especially true for dynamic objects such as RigidBodies and
KinematicBodies. On top of that, avoid translating, rotating or scaling
CollisionShapes to benefit from the physics engine's internal optimizations.

When a single non-transformed collision shape is used in a StaticBody, the
engine's *broad phase* algorithm can discard inactive PhysicsBodies. The *narrow
phase* will then only have to take into account the active bodies's shapes. If a
StaticBody has many collision shapes, the broad phase would fail and the narrow
phase (which is slower) must perform a collision check against each shape.

If you run into performance issues, you may have to make tradeoffs in terms of
accuracy. Most games out there don't actually have 100% accurate collision. They
just find creative ways to hide it or otherwise make it unnoticeable during
normal gameplay :)
