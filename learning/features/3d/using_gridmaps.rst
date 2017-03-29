.. _doc_using_gridmaps:

Using gridmaps
~~~~~~~~~~~~~~

Introduction
------------

:ref:`Gridmaps <class_GridMap>` are a simple and fast way to create 3D
game levels. Think of it as a 3D version of the :ref:`TileMap<doc_using_tilemaps>`
node. Similarly, you start with a predefined library of 3D meshes that
can be put on a grid, just like if you were building a level with an
unlimited amount of Lego blocks.

Collisions can also be added to the meshes, just like you would do with
the tiles of a tilemap.

Creating a MeshLibrary
----------------------

To begin, you need a :ref:`class_MeshLibrary`, which is a collection
of meshes that can be used in the gridmap. Here are some meshes you can
use to set it up.

.. image:: /img/meshes.png

Open a new scene and create a root node (this is important, as without
the root node, it will not be able to generate the MeshLibrary!). Then,
create a :ref:`class_MeshInstance` node:

.. image:: /img/mesh_meshlib.png

If you don't need to apply physics to the building blocks, that's all
you need to do. In most cases though, you will need your block to
generate collisions, so let's see how to add them.

Collisions
----------

To assign a :ref:`class_CollisionShape` and :ref:`class_PhysicsBody`
to the meshes, the simplest way is to do it while creating the
MeshLibrary. Alternatively, you can also edit an existing MeshLibrary
from within the GridMap inspector, but only CollisionShapes can be
defined there and not PhysicsBody.

To give the meshes a CollisionShape, you simply add children nodes to
the MeshInstance node. You would typically add the desired PhysicsBody
and CollisionShape in this order:

.. image:: /img/collide_mesh_meshlib.png

You can adjust the order according to your needs.

Exporting the MeshLibrary
-------------------------

To export, go to ``Scene > Convert To.. > MeshLibrary..``, and save it
as a resource.

.. image:: /img/export_meshlib.png

You are now ready to use the GridMap node.

Using the MeshLibrary in a GridMap
----------------------------------

Create a new scene using any node as root, then add a Gridmap node.
Then, load the MeshLibrary that you just exported.

.. image:: /img/load_meshlib.png

Now, you can build your own level as you see best fit. Use left click
to add tiles and right click to remove them. You can adjust the floor
level when you need to put meshes at specific heights.

.. image:: /img/gridmap.png

As mentioned above, you can also define new CollisionShapes at this
stage by doing the following steps:

.. image:: /img/load_collisionshape.png

There you are!

Reminder
--------

-  Be cautious before scaling meshes if you are not using uniform
   meshes.
-  There are many ways to make use of gridmaps, be creative!
