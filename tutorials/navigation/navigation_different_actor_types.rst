.. _doc_navigation_different_actor_types:

Support different actor types
=============================

.. image:: img/nav_actor_sizes.png

To support different actor types due to e.g. their sizes each type requires its own
navigation map and navigation mesh baked with an appropriated agent radius and height.
The same approach can be used to distinguish between e.g. landwalking, swimming or flying agents.

.. note::

   Agents are exclusively defined by a radius and height value for baking navigation meshes, pathfinding and avoidance. More complex shapes are not supported.

.. tabs::
 .. code-tab:: gdscript GDScript

    # Create a navigation mesh resource for each actor size.
    var navigation_mesh_standard_size: NavigationMesh = NavigationMesh.new()
    var navigation_mesh_small_size: NavigationMesh = NavigationMesh.new()
    var navigation_mesh_huge_size: NavigationMesh = NavigationMesh.new()

    # Set appropriated agent parameters.
    navigation_mesh_standard_size.agent_radius = 0.5
    navigation_mesh_standard_size.agent_height = 1.8
    navigation_mesh_small_size.agent_radius = 0.25
    navigation_mesh_small_size.agent_height = 0.7
    navigation_mesh_huge_size.agent_radius = 1.5
    navigation_mesh_huge_size.agent_height = 2.5

    # Get the root node to parse geometry for the baking.
    var root_node: Node3D = get_node("NavigationMeshBakingRootNode")

    # Create the source geometry resource that will hold the parsed geometry data.
    var source_geometry_data: NavigationMeshSourceGeometryData3D = NavigationMeshSourceGeometryData3D.new()

    # Parse the source geometry from the scene tree on the main thread.
    # The navigation mesh is only required for the parse settings so any of the three will do.
    NavigationServer3D.parse_source_geometry_data(navigation_mesh_standard_size, source_geometry_data, root_node)

    # Bake the navigation geometry for each agent size from the same source geometry.
    # If required for performance this baking step could also be done on background threads.
    NavigationServer3D.bake_from_source_geometry_data(navigation_mesh_standard_size, source_geometry_data)
    NavigationServer3D.bake_from_source_geometry_data(navigation_mesh_small_size, source_geometry_data)
    NavigationServer3D.bake_from_source_geometry_data(navigation_mesh_huge_size, source_geometry_data)

    # Create different navigation maps on the NavigationServer.
    var navigation_map_standard: RID = NavigationServer3D.map_create()
    var navigation_map_small: RID = NavigationServer3D.map_create()
    var navigation_map_huge: RID = NavigationServer3D.map_create()

    # Set the new navigation maps as active.
    NavigationServer3D.map_set_active(navigation_map_standard, true)
    NavigationServer3D.map_set_active(navigation_map_small, true)
    NavigationServer3D.map_set_active(navigation_map_huge, true)

    # Create a region for each map.
    var navigation_region_standard: RID = NavigationServer3D.region_create()
    var navigation_region_small: RID = NavigationServer3D.region_create()
    var navigation_region_huge: RID = NavigationServer3D.region_create()

    # Add the regions to the maps.
    NavigationServer3D.region_set_map(navigation_region_standard, navigation_map_standard)
    NavigationServer3D.region_set_map(navigation_region_small, navigation_map_small)
    NavigationServer3D.region_set_map(navigation_region_huge, navigation_map_huge)

    # Set navigation mesh for each region.
    NavigationServer3D.region_set_navigation_mesh(navigation_region_standard, navigation_mesh_standard_size)
    NavigationServer3D.region_set_navigation_mesh(navigation_region_small, navigation_mesh_small_size)
    NavigationServer3D.region_set_navigation_mesh(navigation_region_huge, navigation_mesh_huge_size)

    # Create start and end position for the navigation path query.
    var start_pos: Vector3 = Vector3(0.0, 0.0, 0.0)
    var end_pos: Vector3 = Vector3(2.0, 0.0, 0.0)
    var use_corridorfunnel: bool = true

    # Query paths for each agent size.
    var path_standard_agent = NavigationServer3D.map_get_path(navigation_map_standard, start_pos, end_pos, use_corridorfunnel)
    var path_small_agent = NavigationServer3D.map_get_path(navigation_map_small, start_pos, end_pos, use_corridorfunnel)
    var path_huge_agent = NavigationServer3D.map_get_path(navigation_map_huge, start_pos, end_pos, use_corridorfunnel)
