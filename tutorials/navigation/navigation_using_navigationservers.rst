.. _doc_navigation_using_navigationservers:

Using NavigationServer
======================

2D and 3D version of the NavigationServer are available as
:ref:`NavigationServer2D<class_NavigationServer2D>` and
:ref:`NavigationServer3D<class_NavigationServer3D>` respectively.

Both 2D and 3D use the same NavigationServer with NavigationServer3D being the primary server. The NavigationServer2D is a frontend that converts 2D positions into 3D positions and back.
Hence it is entirely possible (if not a little cumbersome) to exclusively use the NavigationServer3D API for 2D navigation.

Communicating with the NavigationServer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To work with the NavigationServer means to prepare parameters for a **query** that can be sent to the NavigationServer for updates or requesting data.

To reference the internal NavigationServer objects like maps, regions and agents RIDs are used as identification numbers.
Every navigation related node in the scene tree has a function that returns the RID for this node.

Threading and Synchronization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The NavigationServer does not update every change immediately but waits until
the end of the **physics frame** to synchronize all the changes together.

Waiting for synchronization is required to apply changes to all maps, regions and agents.
Synchronization is done because some updates like a recalculation of the entire navigation map are very expensive and require updated data from all other objects.
Also the NavigationServer uses a **threadpool** by default for some functionality like avoidance calculation between agents.

Waiting is not required for most ``get()`` functions that only request data from the NavigationServer without making changes.
Note that not all data will account for changes made in the same frame.
E.g. if an avoidance agent changed the navigation map this frame the ``agent_get_map()`` function will still return the old map before the synchronization.
The exception to this are nodes that store their values internally before sending the update to the NavigationServer.
When a getter on a node is used for a value that was updated in the same frame it will return the already updated value stored on the node.

The NavigationServer is **thread-safe** as it places all API calls that want to make changes in a queue to be executed in the synchronization phase.
Synchronization for the NavigationServer happens in the middle of the physics frame after scene input from scripts and nodes are all done.

.. note::
    The important takeaway is that most NavigationServer changes take effect after the next physics frame and not immediately.
    This includes all changes made by navigation related nodes in the scene tree or through scripts.

.. note::
    All setters and delete functions require synchronization.

2D and 3D NavigationServer differences
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

NavigationServer2D and NavigationServer3D are equivalent in functionality
for their dimension and both use the same NavigationServer behind the scene.

Strictly technical a NavigationServer2D is a myth.
The NavigationServer2D is a frontend to facilitate conversions of ``Vector2(x, y)`` to
``Vector3(x, 0.0, z)`` and back for the NavigationServer3D API. 2D uses a flat 3D mesh
pathfinding and the NavigationServer2D facilitates the conversions.
When a guide uses just NavigationServer without the 2D or 3D suffix it usually works for both servers
by exchange ``Vector2(x, y)`` with ``Vector3(x, 0.0, z)`` or reverse.

Technically it is possible to use the tools for creating navigation meshes in one dimension for the other
dimension, e.g. baking a 2D navigation mesh with the 3D NavigationMesh when using
flat 3D source geometry or creating 3D flat navigation meshes with the
polygon outline draw tools of NavigationRegion2D and NavigationPolygons.

Any RID created with the NavigationServer2D API works on the NavigationServer3D API
as well and both 2D and 3D avoidance agents can exist on the same map.

.. note::
    Regions created in 2D and 3D will merge their navigation meshes when placed on the same map and merge conditions apply.
    The NavigationServer does not discriminate between NavigationRegion2D and NavigationRegion3D nodes as both are regions on the server.
    By default those nodes register on different navigation maps so this merge can only happen when maps are changed manually e.g. with scripts.

    Actors with avoidance enabled will avoid both 2D and 3D avoidance agents when placed on the same map.

.. warning::
    It is not possible to use NavigationServer2D while disabling 3D on a Godot custom build.

Waiting for synchronization
~~~~~~~~~~~~~~~~~~~~~~~~~~~

At the start of the game, a new scene or procedural navigation changes any path query to a NavigationServer will return empty or wrong.

The navigation map is still empty or not updated at this point.
All nodes from the scene tree need to first upload their navigation related data to the NavigationServer.
Each added or changed map, region or agent need to be registered with the NavigationServer.
Afterward the NavigationServer requires a **physics frame** for synchronization to update the maps, regions and agents.

One workaround is to make a deferred call to a custom setup function (so all nodes are ready).
The setup function makes all the navigation changes, e.g. adding procedural stuff.
Afterwards the function waits for the next physics frame before continuing with path queries.

.. tabs::
 .. code-tab:: gdscript GDScript

    extends Node3D

    func _ready():
        # use call deferred to make sure the entire scene tree nodes are setup
        # else await / yield on 'physics_frame' in a _ready() might get stuck
        call_deferred("custom_setup")

    func custom_setup():

        # create a new navigation map
        var map: RID = NavigationServer3D.map_create()
        NavigationServer3D.map_set_up(map, Vector3.UP)
        NavigationServer3D.map_set_active(map, true)

        # create a new navigation region and add it to the map
        var region: RID = NavigationServer3D.region_create()
        NavigationServer3D.region_set_transform(region, Transform())
        NavigationServer3D.region_set_map(region, map)

        # create a procedural navigation mesh for the region
        var new_navigation_mesh: NavigationMesh = NavigationMesh.new()
        var vertices: PackedVector3Array = PackedVector3Array([
            Vector3(0,0,0),
            Vector3(9.0,0,0),
            Vector3(0,0,9.0)
        ])
        new_navigation_mesh.set_vertices(vertices)
        var polygon: PackedInt32Array = PackedInt32Array([0, 1, 2])
        new_navigation_mesh.add_polygon(polygon)
        NavigationServer3D.region_set_navigation_mesh(region, new_navigation_mesh)

        # wait for NavigationServer sync to adapt to made changes
        await get_tree().physics_frame

        # query the path from the navigationserver
        var start_position: Vector3 = Vector3(0.1, 0.0, 0.1)
        var target_position: Vector3 = Vector3(1.0, 0.0, 1.0)
        var optimize_path: bool = true

        var path: PackedVector3Array = NavigationServer3D.map_get_path(
            map,
            start_position,
            target_position,
            optimize_path
        )

        print("Found a path!")
        print(path)

Server Avoidance Callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~

If RVO avoidance agents are registered for avoidance callbacks the NavigationServer dispatches
their ``velocity_computed`` signals just before the PhysicsServer synchronization.

To learn more about NavigationAgents see :ref:`doc_navigation_using_navigationagents`.

The simplified order of execution for NavigationAgents that use avoidance:

- physics frame starts.
- ``_physics_process(delta)``.
- ``velocity`` property is set on NavigationAgent Node.
- Agent sends velocity and position to NavigationServer.
- NavigationServer waits for synchronization.
- NavigationServer synchronizes and computes avoidance velocities for all registered avoidance agents.
- NavigationServer sends safe velocity vector with signals for each registered avoidance agents.
- Agents receive the signal and move their parent e.g. with ``move_and_slide`` or ``linear_velocity``.
- PhysicsServer synchronizes.
- physics frame ends.

Therefore moving a physicsbody actor in the callback function with the safe velocity is perfectly thread- and physics-safe
as all happens inside the same physics frame before the PhysicsServer commits to changes and does its own calculations.
