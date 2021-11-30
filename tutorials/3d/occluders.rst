.. _doc_occluders:

Occluder Nodes
==============

In addition to occlusion via :ref:`doc_rooms_and_portals`, Godot also has the ability to provide basic occlusion using simple geometric ``Occluder`` nodes. These are geometric shapes that are shown in the editor using gizmos, but are invisible at runtime.

Any object that is fully occluded by the shape (behind or in some cases inside) will be culled at runtime. They are designed to be simple to use and inexpensive at runtime, but the trade off is they may not be as effective at culling as :ref:`doc_rooms_and_portals`. Nevertheless they can still significantly boost performance in some situations.

.. note:: It is important to understand that geometric occluders work by testing the axis aligned bounding box (``AABB``) of the occludee against the occluder. The AABB must be *fully occluded* to be culled. The consequence of this is that smaller objects are more likely to be effectively culled than larger objects.

A major advantage to Occluder nodes is that they are fully dynamic. For example if you place an occluder node as a child of a spaceship, it will move as you move the parent object.

The reason that Occluder nodes are so cheap in performance terms is that the engine dynamically chooses the most relevant occluders at runtime, based on the current viewpoint of the Camera. This means you can often have hundreds of occluders present in the scene. Only the most relevant will be active at any one time.

The Occluder node itself is a holder for an OccluderShape resource, which determines the functionality. To get started, add an Occluder node to your scene tree.

.. tip:: You will see a yellow warning triangle that lets you know that you must set an OccluderShape from the inspector before the ``Occluder`` becomes functional.

OccluderShapeSphere
-------------------

The sphere is one of the simplest and fastest occluders, and is easy to setup and position. The downside is that the sphere only tends to make sense in certain game level designs, and is more suited to terrain or organic background geometry.

Once you have added an OccluderNode and chosen to add a new ``OccluderShapeSphere`` in the inspector, click the OccluderShapeSphere in the inspector to bring up the parameters.

.. image:: img/occluder_shape_sphere_inspector.png

Unlike many Nodes, the ``OccluderShapeSphere`` can store multiple spheres in the same object. This is more efficient in the engine, and keeps your SceneTree clearer. You don't have to store all your spheres in one Occluder as it could become tricky to manage, but it is perfectly reasonable to add 10 or so spheres or more. They are very cheap, and often the more you place, the better the match you will get to your geometry.

In order to store multiple spheres, they are stored as an Array. If you click on the Array in the inspector, you can increase the size of the Array to add one.

.. image:: img/occluder_shape_sphere_terrain.png

The sphere will appear as a small pink spherical object in the editor window. There are two handles on each sphere. The larger middle handle enables you to move the sphere around in the local space of the Occluder, and the small handle enables you to adjust the radius.

Although you can change the position of the sphere using the Occluder Node transform in the inspector, this moves *the entire array* of spheres. When you want to use multiple spheres in one occluder, the handles do this job. In order to allow positioning in 3D, the gizmo will only move the 3D position in the two principal axes depending on the viewpoint in the editor. This is easier for you to get the hang of by trying it out than by explanation.

.. tip:: There is one more handy function in the editor when using multiple spheres. If you click the `Center Node` toolbar button it will recalculate the local positions of the spheres relative to the average of the entire node, and change the transform of the Occluder Node. This is a handy convenience function to make it easier to place them.

At runtime the spheres can be switched on and off changing the Occluder node visibility, and the Node can be moved and scaled and rotated etc.

A common use case for occluder spheres is providing occlusion on mountainous / hilly terrain. By placing spheres inside mountains you can prevent trees, plants, building and objects rendering behind mountains. With some creativity they can also be used for moving objects such as large spacecraft, planets etc.
