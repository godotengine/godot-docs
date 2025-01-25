.. _doc_navigation_optimizing_performance:

Optimizing Navigation Performance
=================================

.. image:: img/nav_optimization.webp

Common Navigation related performance problems can be categorized into the following topics:

- Performance problems with parsing scene tree nodes for navigation mesh baking.
- Performance problems with baking the actual navigation mesh.
- Performance problems with NavigationAgent path queries.
- Performance problems with the actual path search.
- Performance problems with synchronizing the navigation map.

In the following sections information can be found on how to identify and fix or at least mitigate their impact on framerates.

Performance problems with parsing scene tree nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tip::

    Prefer using simple shapes with as few edges as possible e.g. nothing rounded like a circle, sphere or torus.
    
    Prefer using physics collision shapes over complex visual meshes as source geometry as meshes need to be copied from the GPU and are commonly much more detailed than necessary.

In general avoid using very complex geometry as source geometry for baking navigation meshes.
E.g. never use a very detailed visual mesh, as parsing its shape to data arrays and voxelizing it for the navigation mesh baking will take a long time for no real quality gain on the final navigation mesh.
Instead, use a very simplified level of detail version of a shape. Even better, use very primitive shapes like boxes and rectangles that only roughly cover the same geometry but still yield a baked result good enough for pathfinding.

Prefer using simple physics collision shapes over visual meshes, as the source geometry for baking navigation meshes.
Physics shapes are by default very limited and optimized shapes that are easy and quick to parse. A visual mesh on the other hand can range from simple to complex.
On top, to gain access to visual mesh data the parser needs to request the mesh data arrays from the RenderingServer as visual mesh data is stored directly on the GPU and is not cached on the CPU.
This requires locking the RenderingServer thread and can severely impact framerate at runtime while the rendering runs multi-threaded.
If the rendering runs single-threaded, the framerate impact might be even worse and the mesh parsing might freeze the entire game for a few seconds on complex meshes.

Performance problems with navigation mesh baking
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tip::

    At runtime, always prefer to use a background thread for baking navigation meshes.
    
    Increase NavigationMesh ``cell_size`` and ``cell_height`` to create less voxels.
    
    Change the ``SamplePartitionType`` from watershed to monotone or layers to gain baking performance.

.. warning::
    NEVER scale source geometry with nodes to avoid precision errors. Most scale applies only visually and shapes that are very large at their base scale require still a lot of extra processing even while downscaled.

Baking navigation meshes at runtime should always be done in a background thread if possible. Even small sized navigation meshes can take far longer to bake than what is possible to squeeze into a single frame, at least if the framerate should stay at a bearable level.

Complexity of source geometry data parsed from scene tree nodes has big impact on baking performance as everything needs to be mapped to a grid / voxels.
For runtime baking performance the NavigationMesh cell size and cell height should be set as high as possible without causing navigation mesh quality problems for a game.
If cell size or cell height is set too low the baking is forced to create an excessive amount of voxels to process the source geometry.
If the source geometry spans over a very large game world it is even possible that the baking process runs out off memory in the middle and crashes the game.
The partition type can also be lowered depending on how complex the games source geometry is to gain some performance.
E.g. games with mostly flat surfaces with blocky geometry can get away with the monotone or layers mode that are a lot faster to bake (e.g. because they require no distance field pass).

Never scale source geometry with nodes. Not only can it result in a lot of precision errors with wrongly matched vertices and edges but also some scaling only exists as visuals and not in the actual parsed data.
E.g. if a mesh is downscaled visually in the Editor, e.g. the scale set to 0.001 on a MeshInstance, the mesh still requires a gigantic and very complex voxel grid to be processed for the baking.

Performance problems with NavigationAgent path queries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tip::

    Avoid unnecessary path resets and queries every frame in NavigationAgent scripts.
    
    Avoid updating all NavigationAgent paths in the same frame.

Logical errors and wasteful operations in the custom NavigationAgent scripts are very common causes of performance issues, e.g. watch out for resetting the path every single frame.
By default NavigationAgents are optimized to only query new paths when the target position changes, the navigation map changes or they are forced too far away from the desired path distance.

E.g. when AI should move to the player, the target position should not be set to the player position every single frame as this queries a new path every frame.
Instead, the distance from the current target position to the player position should be compared and only when the player has moved too far away a new target position should be set.

Do not check beforehand if a target position is reachable every frame. What looks like an innocent check is the equivalent of an expensive path query behind the scene.
If the plan is to request a new path anyway should the position be reachable, a path should be queried directly.
By looking at the last position of the returned path and if that position is in a "reachable" distance to the checked position it answers the "is this position reachable?" question.
This avoids doing the equivalent of two full path queries every frame for the same NavigationAgent.

Divide the total number of NavigationAgents into update groups or use random timers so that they do not all request new paths in the same frame.

Performance problems with the actual path search
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tip::

    Optimize overdetailed navigation meshes by reducing the amount of polygons and edges.

The cost of the actual path search correlates directly with the amount of navigation mesh polygons and edges and not the real size of a game world.
If a giant game world uses very optimized navigation meshes with only few polygons that cover large areas, performance should be acceptable.
If the game world is splintered into very small navigation meshes that each have tiny polygons (like for TileMaps) pathfinding performance will be reduced.

A common problem is a sudden performance drop when a target position is not reachable in a path query.
This performance drop is "normal" and the result of a too large, too unoptimized navigation mesh with way to much polygons and edges to search through.
In normal path searches where the target position can be reached quickly the pathfinding will do an early exit as soon as the position is reached which can hide this lack of optimization for a while.
If the target position can not be reached the pathfinding has to do a far longer search through the available polygons to confirm that the position is absolutely not reachable.

Performance problems with navigation map synchronization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tip::

    Merge navigation meshes polygons by vertex instead of by edge connection wherever possible.

When changes are made to e.g. navigation meshes or navigation regions, the NavigationServer needs to synchronize the navigation map.
Depending on the complexity of navigation meshes, this can take a significant amount of time which may impact the framerate.

The NavigationServer merges navigation meshes either by vertex or by edge connection.
The merge by vertex happens when the two vertex of two different edges land in the same map grid cells. This is a rather quick and low-cost operation.
The merge by edge connection happens in a second pass for all still unmerged edges. All the free edges are checked for possible edge connections by both distance and angle which is rather costly.

So apart from the general rule to have as few polygon edges as possible, as many edges as possible should be merged by vertex upfront so only a few edges are left for the more costly edge connection calculation.
The debug Navigation PerformanceMonitor can be used to get statistics on how many polygons and edges are available and how many of them are unmerged or not merged by vertex.
If the ratio between vertex merged and edge connections is way off (vertex should be significantly higher) the navigation meshes are properly created or placed very inefficient.
