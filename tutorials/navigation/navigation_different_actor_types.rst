.. _doc_navigation_different_actor_types:

Support different actor types
=============================

.. image:: img/nav_actor_sizes.png

To support different actor types due to e.g. their sizes each type requires its own 
navigation map and navigation mesh baked with an appropriated agent radius and height.
The same approach can be used to distinguish between e.g. landwalking, swimming or flying agents.

.. note::

   Agents are exclusively defined by a radius and height value for baking navmeshes, pathfinding and avoidance. More complex shapes are not supported.

.. tabs::
 .. code-tab:: gdscript GDScript

    # create navigationmesh resources for each actor size
    var navmesh_standard_size : NavigationMesh = NavigationMesh.new()
    var navmesh_small_size : NavigationMesh = NavigationMesh.new()
    var navmesh_huge_size : NavigationMesh = NavigationMesh.new()
    
    # set appropriated agent parameters
    navmesh_standard_size.agent_radius = 0.5
    navmesh_standard_size.agent_height = 1.8
    navmesh_small_size.agent_radius = 0.25
    navmesh_small_size.agent_height = 0.7
    navmesh_huge_size.agent_radius = 1.5
    navmesh_huge_size.agent_height = 2.5
    
    # get the root node for the baking to parse geometry
    var root_node : Node3D = get_node("NavmeshRootNode")
    
    # bake the navigation geometry for each agent size
    NavigationMeshGenerator.bake(navmesh_standard_size, root_node)
    NavigationMeshGenerator.bake(navmesh_small_size, root_node)
    NavigationMeshGenerator.bake(navmesh_huge_size, root_node)
    
    # create different navigation maps on the NavigationServer
    var nav_map_standard : RID = NavigationServer3D.map_create()
    var nav_map_small : RID = NavigationServer3D.map_create()
    var nav_map_huge : RID = NavigationServer3D.map_create()
    
    # create a region for each map
    var nav_map_standard_region : RID = NavigationServer3D.region_create()
    var nav_map_small_region : RID = NavigationServer3D.region_create()
    var nav_map_huge_region : RID = NavigationServer3D.region_create()
    
    # set navigationmesh for each region
    NavigationServer3D.region_set_navmesh(nav_map_standard_region, navmesh_standard_size)
    NavigationServer3D.region_set_navmesh(nav_map_small_region, navmesh_small_size)
    NavigationServer3D.region_set_navmesh(nav_map_huge_region, navmesh_huge_size)
    
    # add regions to maps
    nav_map_standard_region.region_set_map(nav_map_standard_region, nav_map_standard)
    nav_map_small_region.region_set_map(nav_map_small_region, nav_map_small)
    nav_map_huge_region.region_set_map(nav_map_huge_region, nav_map_huge)
    
    # wait a physics frame for sync
    await get_tree().physics_frame
    
    # query paths for each size
    var path_standard_agent = NavigationServer3D.map_get_path(nav_map_standard, start_pos, end_pos, true)
    var path_small_agent = NavigationServer3D.map_get_path(navmesh_small_size, start_pos, end_pos, true)
    var path_huge_agent = NavigationServer3D.map_get_path(nav_map_huge, start_pos, end_pos, true)
