.. _doc_navigation_overview:

Navigation Overview
===================

Godot provides multiple objects, classes and servers to facilitate grid-based- or mesh-based navigation and pathfinding for 2D and 3D games.
The following section provides a quick overview over all available navigation related objects in Godot and their primary use.

2D Navigation Overview
----------------------

Godot provides the following objects and classes for 2D navigation:

- :ref:`Astar2D<class_Astar2D>`
    ``Astar2D`` objects provide an option to find the shortest path in a graph of weighted **points**.
    
    The AStar2D class is best suited for cellbased 2D gameplay that does not require actors to reach any possible position within an area but only predefined, distinct positions.

- :ref:`NavigationServer2D<class_NavigationServer2D>`
    ``NavigationServer2D`` provides a powerful server API to find the shortest path between two positions on a navigationmesh defined area.
    
    The NavigationServer is best suited for 2D realtime gameplay that does require actors to reach any possible position within an navmesh defined area.
    Meshbased navigation scales well with large gameworlds as a large area can often be defined with a single polygon when it would require many, many grid cells.
    
    The NavigationServer holds different navigation maps that each consist of regions that hold navigationmesh data.
    Agents can be placed on a map for avoidance calculation.
    RIDs are used to reference the internal maps, regions and agents when communicating with the server.
    
    The following NavigationServer RID types are available.
        - NavMap RID
            Reference to a specific navigation map that holds regions and agents.
            The map will attempt to join changed navigationmeshes of regions by proximity.
            The map will synchronise regions and agents each physics frame.
        - NavRegion RID
            Reference to a specific navigation region that can hold navigationmesh data.
            The region can be enabled / disabled or the use restricted with a navigationlayer bitmask.
        - NavAgent RID
            Reference to a specific avoidance agent with a radius value use solely in avoidance.

The following SceneTree Nodes are available as helpers to work with the NavigationServer2D API.

- :ref:`NavigationRegion2D<class_NavigationRegion2D>` Node
    A Node that holds a NavigationPolygon resource that defines a navigationmesh for the NavigationServer2D.
    The region can be enabled / disabled.
    The use in pathfinding can be further restricted through the navigationlayers bitmask.
    Regions can join their navigationmeshes by proximity for a combined navigationmesh.

-  :ref:`NavigationAgent2D<class_NavigationAgent2D>` Node
    An optional helper Node to facilitate common NavigationServer2D API calls for pathfinding and avoidance for a Node2D inheriting parent Node.

-  :ref:`NavigationObstacle2D<class_NavigationObstacle2D>` Node
    A Node that acts as an agent with avoidance radius for a Node2D inheriting parent Node.
    Obstacles are intended as a last resort option for constantly moving objects that cannot be re(baked) to a navigationmesh efficiently.

The 2D navigationmeshes are defined with the following resources:

- :ref:`NavigationPolygon<class_NavigationPolygon>` Resource
    A resource that holds 2D navigationmesh data and provides polygon drawtools to define navigation areas inside the Editor as well as at runtime.
    
    - The NavigationRegion2D Node uses this resource to define its navigation area.
    - The NavigationServer2D uses this resource to update navmesh of individual regions.
    - The TileSet Editor creates and uses this resource internally when defining tile navigation areas.

3D Navigation Overview
----------------------

Godot provides the following objects and classes for 3D navigation:

- :ref:`Astar3D<class_Astar3D>`
    ``Astar3D`` objects provide an option to find the shortest path in a graph of weighted **points**.
    
    The AStar3D class is best suited for cellbased 3D gameplay that does not require actors to reach any possible position within an area but only predefined, distinct positions.

- :ref:`NavigationServer3D<class_NavigationServer3D>`
    ``NavigationServer3D`` provides a powerful server API to find the shortest path between two positions on a navigationmesh defined area.
    
    The NavigationServer is best suited for 3D realtime gameplay that does require actors to reach any possible position within an navmesh defined area.
    Meshbased navigation scales well with large gameworlds as a large area can often be defined with a single polygon when it would require many, many grid cells.
    
    The NavigationServer holds different navigation maps that each consist of regions that hold navigationmesh data.
    Agents can be placed on a map for avoidance calculation.
    RIDs are used to reference the internal maps, regions and agents when communicating with the server.

    The following NavigationServer RID types are available.
        - NavMap RID
            Reference to a specific navigation map that holds regions and agents.
            The map will attempt to join changed navigationmeshes of regions by proximity.
            The map will synchronise regions and agents each physics frame.
        - NavRegion RID
            Reference to a specific navigation region that can hold navigationmesh data.
            The region can be enabled / disabled or the use restricted with a navigationlayer bitmask.
        - NavAgent RID
            Reference to a specific avoidance agent with a radius value use solely in avoidance.

The following SceneTree Nodes are available as helpers to work with the NavigationServer3D API.

- :ref:`NavigationRegion3D<class_NavigationRegion3D>` Node
    A Node that holds a NavigationMesh resource that defines a navigationmesh for the NavigationServer3D.
    The region can be enabled / disabled.
    The use in pathfinding can be further restricted through the navigationlayers bitmask.
    Regions can join their navigationmeshes by proximity for a combined navigationmesh.

-  :ref:`NavigationAgent3D<class_NavigationAgent3D>` Node
    An optional helper Node to facilitate common NavigationServer3D API calls for pathfinding and avoidance for a Node3D inheriting parent Node.

-  :ref:`NavigationObstacle3D<class_NavigationObstacle3D>` Node
    A Node that acts as an agent with avoidance radius for a Node3D inheriting parent Node.
    Obstacles are intended as a last resort option for constantly moving objects that cannot be re(baked) to a navigationmesh efficiently.

The 3D navigationmeshes are defined with the following resources:

- :ref:`NavigationMesh<class_NavigationMesh>` Resource
    A resource that holds 3D navigationmesh data and provides 3D geometry baking options to define navigation areas inside the Editor as well as at runtime.
    
    - The NavigationRegion3D Node uses this resource to define its navigation area.
    - The NavigationServer3D uses this resource to update navmesh of individual regions.
    - The GridMap Editor uses this resource when specific navigationmeshes are defined for each gridcell.
