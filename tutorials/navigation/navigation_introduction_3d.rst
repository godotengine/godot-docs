.. _doc_navigation_overview_3d:

3D navigation overview
======================

Godot provides multiple objects, classes and servers to facilitate grid-based or mesh-based navigation and pathfinding for 2D and 3D games.
The following section provides a quick overview over all available navigation related objects in Godot for 3D scenes and their primary use.

Godot provides the following objects and classes for 3D navigation:

- :ref:`Astar3D<class_Astar3D>`
    ``Astar3D`` objects provide an option to find the shortest path in a graph of weighted **points**.

    The AStar3D class is best suited for cell-based 3D gameplay that does not require actors to reach any possible position within an area but only predefined, distinct positions.

- :ref:`NavigationServer3D<class_NavigationServer3D>`
    ``NavigationServer3D`` provides a powerful server API to find the shortest path between two positions on an area defined by a navigation mesh.

    The NavigationServer is best suited for 3D realtime gameplay that does require actors to reach any possible position within a navigation mesh defined area.
    Mesh-based navigation scales well with large game worlds as a large area can often be defined with a single polygon when it would require many, many grid cells.

    The NavigationServer holds different navigation maps that each consist of regions that hold navigation mesh data.
    Agents can be placed on a map for avoidance calculation.
    RIDs are used to reference internal maps, regions, and agents when communicating with the server.

    The following NavigationServer RID types are available.
        - NavMap RID
            Reference to a specific navigation map that holds regions and agents.
            The map will attempt to join the navigation meshes of the regions by proximity.
            The map will synchronize regions and agents each physics frame.
        - NavRegion RID
            Reference to a specific navigation region that can hold navigation mesh data.
            The region can be enabled / disabled or the use restricted with a navigation layer bitmask.
        - NavLink RID
            Reference to a specific navigation link that connects two navigation mesh positions over arbitrary distances.
        - NavAgent RID
            Reference to a specific avoidance agent.
            The avoidance is defined by a radius value.
        - NavObstacle RID
            Reference to a specific avoidance obstacle used to affect and constrain the avoidance velocity of agents.

The following scene tree nodes are available as helpers to work with the NavigationServer3D API.

- :ref:`NavigationRegion3D<class_NavigationRegion3D>` Node
    A Node that holds a Navigation Mesh resource that defines a navigation mesh for the NavigationServer3D.

    - The region can be enabled / disabled.
    - The use in pathfinding can be further restricted through the ``navigation_layers`` bitmask.
    - The NavigationServer3D will join the navigation meshes of regions by proximity for a combined navigation mesh.

- :ref:`NavigationLink3D<class_NavigationLink3D>` Node
    A Node that connects two positions on navigation meshes over arbitrary distances for pathfinding.

    - The link can be enabled / disabled.
    - The link can be made one-way or bidirectional.
    - The use in pathfinding can be further restricted through the ``navigation_layers`` bitmask.

    Links tell the pathfinding that a connection exists and at what cost. The actual agent handling and movement needs to happen in custom scripts.

-  :ref:`NavigationAgent3D<class_NavigationAgent3D>` Node
    A helper Node used to facilitate common NavigationServer3D API calls for pathfinding and avoidance.
    Use this Node with a Node3D inheriting parent Node.

-  :ref:`NavigationObstacle3D<class_NavigationObstacle3D>` Node
    A Node that can be used to affect and constrain the avoidance velocity of avoidance enabled agents.
    This Node does NOT affect the pathfinding of agents. You need to change the navigation meshes for that instead.

The 3D navigation meshes are defined with the following resources:

- :ref:`NavigationMesh<class_NavigationMesh>` Resource
    A resource that holds 3D navigation mesh data.
    It provides 3D geometry baking options to define navigation areas inside the Editor as well as at runtime.

    - The NavigationRegion3D Node uses this resource to define its navigation area.
    - The NavigationServer3D uses this resource to update the navigation mesh of individual regions.
    - The GridMap Editor uses this resource when specific navigation meshes are defined for each grid cell.

.. seealso::

    You can see how 3D navigation works in action using the
    `3D Navigation demo project <https://github.com/godotengine/godot-demo-projects/tree/master/3d/navigation>`__.

Setup for 3D scene
------------------

The following steps show a basic setup for minimal viable navigation in 3D.
It uses the NavigationServer3D and a NavigationAgent3D for path movement.

#. Add a NavigationRegion3D Node to the scene.

#. Click on the region node and add a new :ref:`NavigationMesh<class_NavigationMesh>` Resource to
   the region node.

   .. image:: img/nav_3d_min_setup_step1.png

#. Add a new MeshInstance3D node as a child of the region node.

#. Select the MeshInstance3D node and add a new PlaneMesh and increase the xy size to 10.

#. Select the region node again and press the "Bake Navmesh" button on the top bar.

   .. image:: img/nav_3d_min_setup_step2.png

#. Now a transparent navigation mesh appears that hovers some distance on top of the PlaneMesh.

   .. image:: img/nav_3d_min_setup_step3.png

#. Add a CharacterBody3D node in the scene with a basic collision shape and some mesh for visuals.

#. Add a NavigationAgent3D node below the character node.

   .. image:: img/nav_3d_min_setup_step4.webp

#. Add a script to the CharacterBody3D node with the following content. We make sure to set a
   movement target after the scene has fully loaded and the NavigationServer had time to sync.
   Also, add a Camera3D and some light and environment to see something.

.. tabs::
 .. code-tab:: gdscript GDScript

    extends CharacterBody3D

    var movement_speed: float = 2.0
    var movement_target_position: Vector3 = Vector3(-3.0,0.0,2.0)

    @onready var navigation_agent: NavigationAgent3D = $NavigationAgent3D

    func _ready():
        # These values need to be adjusted for the actor's speed
        # and the navigation layout.
        navigation_agent.path_desired_distance = 0.5
        navigation_agent.target_desired_distance = 0.5

        # Make sure to not await during _ready.
        call_deferred("actor_setup")

    func actor_setup():
        # Wait for the first physics frame so the NavigationServer can sync.
        await get_tree().physics_frame

        # Now that the navigation map is no longer empty, set the movement target.
        set_movement_target(movement_target_position)

    func set_movement_target(movement_target: Vector3):
        navigation_agent.set_target_position(movement_target)

    func _physics_process(delta):
        if navigation_agent.is_navigation_finished():
            return

        var current_agent_position: Vector3 = global_position
        var next_path_position: Vector3 = navigation_agent.get_next_path_position()

        velocity = current_agent_position.direction_to(next_path_position) * movement_speed
        move_and_slide()

 .. code-tab:: csharp C#

    using Godot;

    public partial class MyCharacterBody3D : CharacterBody3D
    {
        private NavigationAgent3D _navigationAgent;

        private float _movementSpeed = 2.0f;
        private Vector3 _movementTargetPosition = new Vector3(-3.0f, 0.0f, 2.0f);

        public Vector3 MovementTarget
        {
            get { return _navigationAgent.TargetPosition; }
            set { _navigationAgent.TargetPosition = value; }
        }

        public override void _Ready()
        {
            base._Ready();

            _navigationAgent = GetNode<NavigationAgent3D>("NavigationAgent3D");

            // These values need to be adjusted for the actor's speed
            // and the navigation layout.
            _navigationAgent.PathDesiredDistance = 0.5f;
            _navigationAgent.TargetDesiredDistance = 0.5f;

            // Make sure to not await during _Ready.
            Callable.From(ActorSetup).CallDeferred();
        }

        public override void _PhysicsProcess(double delta)
        {
            base._PhysicsProcess(delta);

            if (_navigationAgent.IsNavigationFinished())
            {
                return;
            }

            Vector3 currentAgentPosition = GlobalTransform.Origin;
            Vector3 nextPathPosition = _navigationAgent.GetNextPathPosition();

            Velocity = currentAgentPosition.DirectionTo(nextPathPosition) * _movementSpeed;
            MoveAndSlide();
        }

        private async void ActorSetup()
        {
            // Wait for the first physics frame so the NavigationServer can sync.
            await ToSignal(GetTree(), SceneTree.SignalName.PhysicsFrame);

            // Now that the navigation map is no longer empty, set the movement target.
            MovementTarget = _movementTargetPosition;
        }
    }

.. note::

    On the first frame the NavigationServer map has not synchronized region data and any path query will return empty. Wait for the NavigationServer synchronization by awaiting one frame in the script.
