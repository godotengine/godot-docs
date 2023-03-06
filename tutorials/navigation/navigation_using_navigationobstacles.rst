.. _doc_navigation_using_navigationobstacles:

Using NavigationObstacles
=========================

NavigationObstacles are used to set an avoidance radius around objects
that, due to their constant movement, cannot be efficiently (re)baked
to a 2D NavigationPolygon or 3D NavigationMesh.

2D and 3D versions of NavigationObstacles nodes are available as
:ref:`NavigationObstacle2D<class_NavigationObstacle2D>` and
:ref:`NavigationObstacle3D<class_NavigationObstacle3D>`  respectively.

NavigationObstacles are not intended for any kind of static geometry
or temporary barriers that may change their position occasionally.
Those changes should be (re)baked so actors can follow the outlines
of these objects at higher detail with navigation paths. The obstacle avoidance
should be seen as a last resort option intended for objects that are constantly moving.

To use NavigationObstacles for avoidance, place a NavigationObstacle2D/3D node
below a Node2D/3D inheriting parent node. While the obstacle node has an
option to ``estimate_radius`` from child collisions, prefer to set a
more reliable manual ``radius`` value. If estimated, the obstacle will use
a radius that encapsulates the entire parent node which can result in a very large
radius value if the parent is not a circle shape but e.g. a long rectangle shape.

.. note::

    The obstacle ``radius`` is the area that will be strictly avoided whenever possible.
    Do not set it too large. Agents start to avoid way before
    this radius depending on parameters and velocity.


While NavigationObstacle nodes do require a Node parent the NavigationServer obstacles do not.
New obstacles created in scripts require only a ``map``, ``radius`` and ``position``.
Obstacles can be placed directly on the NavigationMap with the NavigationServer API.

.. tabs::
 .. code-tab:: gdscript GDScript

    extends Node3D
    # create a new "obstacle" agent and place it on the default map``
    var new_agent_rid: RID = NavigationServer3D.agent_create()
    var default_3d_map_rid: RID = get_world_3d().get_navigation_map()

    NavigationServer3D.agent_set_map(new_agent_rid, default_3d_map_rid)
    NavigationServer3D.agent_set_radius(new_agent_rid, 0.5)
    NavigationServer3D.agent_set_position(new_agent_rid, global_transform.origin)

.. note::

    The NavigationServer API has no dedicated functions for obstacles.
    Obstacles are technically considered just normal agents.
    All "agent" prefixed functions are intended for obstacles as well.
