.. _doc_navigation_using_navigationregions:

Using NavigationRegions
=======================

NavigationRegions are the visual Node representation of a ``region`` of the navigation ``map`` on the NavigationServer.
Each NavigationRegion node holds a resource for the navigationmesh data.

Both 2D and 3D version are available as :ref:`NavigationRegion2D<class_NavigationRegion2D>`
and :ref:`NavigationRegion3D<class_NavigationRegion3D>` respectively.

Individual NavigationRegions upload their 2D NavigationPolygon or 3D NavigationMesh resource data to the NavigationServer.
The NavigationServer map turns this information into a combined navigation map for pathfinding.

To create a navigation region using the SceneTree add a ``NavigationRegion2D`` or ``NavigationRegion3D`` node to the scene.
All regions require a navigationmesh resource to function. See :ref:`doc_navigation_using_navigationmeshes` to learn how to create and apply navigationmeshes.

NavigationRegions will automatically push ``global_transform`` changes to the region on the NavigationServer which makes them suitable for moving platforms.
The NavigationServer will attempt to connect navmeshes of individual regions when they are close enough. For more detail see :ref:`doc_navigation_connecting_navmesh`.
To connect NavigationRegions over arbitrary distances see :ref:`doc_navigation_using_navigationlinks` to learn how to create and use ``NavigationLinks``.

.. warning::

    While changing the transform of a NavigationRegion node does update the region position on the
    NavigationServer changing the scale does not. A navigationmesh resource has no scale and needs
    to be fully updated when source geometry changes scale.

Regions can be enabled / disabled and if disabled will not contribute to future pathfinding queries.

.. note::

    Existing paths will not be automatically updated when a region gets enabled / disabled.

Creating new navigation regions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

New NavigationRegion nodes will automatically register to the default world navigation map for their 2D/3D dimension.

The region RID can then be obtained from NavigationRegion Nodes with ``get_region_rid()``.

.. tabs::
 .. code-tab:: gdscript GDScript

    extends NavigationRegion3D

    var navigationserver_region_rid: RID = get_region_rid()

New regions can also be created with the NavigationServer API and added to any existing map.

If regions are created with the NavigationServer API directly they need to be assigned a navigation map manually.

.. tabs::
 .. code-tab:: gdscript GDScript

    extends Node2D

    var new_2d_region_rid: RID = NavigationServer2D.region_create()
    var default_2d_map_rid: RID = get_world_2d().get_navigation_map()
    NavigationServer2D.region_set_map(new_2d_region_rid, default_2d_map_rid)

.. tabs::
 .. code-tab:: gdscript GDScript

    extends Node3D

    var new_3d_region_rid: RID = NavigationServer3D.region_create()
    var default_3d_map_rid: RID = get_world_3d().get_navigation_map()
    NavigationServer3D.region_set_map(new_3d_region_rid, default_3d_map_rid)

.. note::

    NavigationRegions can only be assigned to a single NavigationMap.
    If an existing region is assigned to a new map it will leave the old map.
