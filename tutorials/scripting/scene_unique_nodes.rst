.. _doc_scene_unique_nodes:

Scene Unique Nodes
==================

Introduction
------------

There are times in a project where a node needs to be called
from a script, however it's position in the tree might change
over time as adjustments are made to a scene, such as a
button in a UI scene.

In situations like this a node can be turned into a scene
unique node to avoid updating a script multiple times.

Creating and using them
-----------------------

In the scene tree of a project right click on a node and
from the dropdown menu select "Access as Scene Unique Name".

.. image:: img/unique_name.png

After checking this the node will now have a **%** next to its
name in the scene tree

.. image:: img/percent.png

To use a unique node in a script use the `%` symbol and the nodes
name in the path for `get_node`. For example:

.. tabs::
 .. code-tab:: gdscript GDScript
    get_node("%RedButton").text = "Hello"
