.. _doc_using_gridmaps:

Using gridmaps
~~~~~~~~~~~~~~

Introduction
------------

Gridmap is a simple and quick way to create 3D game levels. Think it as a 3D version of tilemap. Similarly, you start with a set of 3D meshes that can be put in a grid, it's like playing with unlimited among of Lego.

Collisions can also be added to the meshes.

Creating a meshlibrary 
----------------

To begin, you need a meshlibrary. Here are some meshes for creating it.

.. image:: /img/meshes.png

Open a new scene and create a root node(this is important, without the root node, it will not export!). Then, create a meshInstance node.

.. image:: /img/mesh_meshlib.png

If you don't need to apply physics to the building blocks. That's all you need to do. Usually you will need to add physics, let's try do add it.

Collision
---------

There are two ways to give the meshes a collision shape and physicsBody, you either add it when creating the meshLibrary or edit the meshLibrary inside the Gridmap node(only collision shape can be set, therefore, it's necessary to define the physicsBody when creating the meshLibrary. Let's go by the former method.

To give the meshes a collision shape. You simply add more nodes to the meshInstance node. You add the desired physicsBody and collision shape in this order: 

.. image:: /img/collide_mesh_meshlib.png

You can adjust the order according to your needs.

To export, go to scene>covert to>meshLibrary

.. image:: /img/export_meshlib.png

You are now ready to use the Gridmap node.

Using the MeshLibrary in a GridMap
------------------------------

Create a new scene, use any node as root, then create a Gridmap node. Then, load the specific MeshLibrary.

.. image:: /img/load_meshlib.png

Now, you can build your own world in whatever way you wish. Leftclick to add and rightclick to remove. You can adjust the floor when you need to put some meshes at specific height.

.. image:: /img/gridmap.png

As mention above, you can define the collision shape ins this stage, do the following steps:

.. image:: /img/load_collisionshape.png

Ta Da.

Reminder
------------------------------

-Beware of the scale of the meshes, if you are not using uniform meshes.

-There are many ways to make use of the Gridmap, be creative.
