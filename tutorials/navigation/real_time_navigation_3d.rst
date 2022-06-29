.. _doc_real_time_navigation_3d:

Real Time Navigation (3D)
=========================

Introduction
------------

Pathfinding in a 3D environment is crucial for many games, it's commonly
how non directly controlled characters or entities find their way around
an environment. Godot provides several nodes for this purpose:

-  :ref:`Navigation<class_Navigation>` (deprecated)
-  :ref:`NavigationMeshInstance<class_NavigationMeshInstance>`
-  :ref:`NavigationAgent<class_NavigationAgent>`
-  :ref:`NavigationObstacle<class_NavigationObstacle>`

The map and navigation regions
------------------------------

The "map" is the entire world for navigation, it's similar to "space" for
the physics engine. It's comprised of navigation regions, these regions
define parts of the world that can be navigated around by navigation
agents.

To create a navigation region add the :ref:`NavigationMeshInstance<class_NavigationMeshInstance>`
node to a 3D scene. Next in the inspector for that mesh create or add a
:ref:`NavigationMesh<class_NavigationMesh>`. The navmesh contains options
for how it will be generated when it's baked. The geometry options control
which nodes, and types of nodes, are used to bake the mesh. A full
description of each setting and how it works can be found in the :ref:`NavigationMesh class reference<class_NavigationMesh>`.

Once the settings have been properly configured press the "Bake NavMesh"
button at the top of the inspector to generate it.

.. image:: img/bake_navmesh.png

.. note::

    It can also be generated at runtime using the `bake_navigation_region()`
    method of the navigation region node.

Once the mesh has finished generating you should see the transparent
navigation mesh above the areas in the scene that can be navigated to.

.. image:: img/baked_navmesh.png

Keep in mind that the navmesh shows where the center of an entity can
go. For example, if you set the agent radius to 0.5 then the
navigation mesh will have a distance of 0.5 from any ledges or walls
to prevent clipping into the wall or hanging off of the edge.

Navigation agents can moved from one region to another if they are next
to each other. Additionally a baked navmesh can be moved at runtime and
agents will still be able to navigate onto it from another region.
For example, navigating onto a moving platform that has stopped will work.

NavigationAgent3D
-----------------

Navigation agent nodes are what actually does the pathfinding in a scene,
one can be attached to the root node of an entity that needs to navigate.

To have it pathfind use its `set_target_location` method. Once the target
has been set a path will be generated to the node using navigation regions,
with several points on the way to the final destination.

RVO processing
--------------

RVO stands for reciprocal velocity obstacle. RVO processing is a way to
pathfind while taking into account other agents and physics bodies that
are also moving.

To use it set a target like normal. Then an agent needs to fetch its next
nav path location, and compute its velocity to that location. Instead
of using that value to move use it to set the velocity on the agent
with `set_velocity`. Then a new velocity that takes into account other
agents and obstacles is generated and emitted with the signal `velocity_computed`.

However agents can only take into account a set number of other nearby
agents, this is the :ref:`max neighbors<class_NavigationAgent_property_max_neighbors>`
property of an agent and can be adjusted. This is **not** a limit for
how many agents can use a navigation region at the same time.

NavigationObstacle3D
--------------------

This node is used to mark physics bodies that move around a navigation area
that agents need to avoid (this will only work if you use RVO processing).
For example, this node would be useful for pieces of debris in a destructible
environment. Add it as the child of a physics body and navigation agent
nodes will avoid it while pathfinding.

Generating a path (old method)
------------------------------

This is the old method for generating a navigation path, it will be
removed in Godot 4. First, add a navigation node to the scene, then
add a navigation mesh instance as it's child and set up a navigation
mesh. 

To get a path between two areas on a map you use the navigation node
method ``get_simple_path()``. The first argument is a Vector3 of the
starting location, the next is a Vector3 of the end location. And the
last argument is a boolean for whether or not agent properties of a
navmesh are considered when generating a path.

The method will return a :ref:`PoolVector3Array <class_PoolVector3Array>` consisting of
points that make a path. If there is no way to navigate to the end
location the method will return a blank :ref:`PoolVector3Array <class_PoolVector3Array>`.
