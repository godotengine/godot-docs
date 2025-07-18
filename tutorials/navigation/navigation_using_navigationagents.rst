.. _doc_navigation_using_navigationagents:

Using NavigationAgents
======================

NavigationsAgents are helper nodes that combine functionality
for pathfinding, path following and agent avoidance for a Node2D/3D inheriting parent node.
They facilitate common calls to the NavigationServer API on
behalf of the parent actor node in a more convenient manner for beginners.

2D and 3D version of NavigationAgents are available as
:ref:`NavigationAgent2D<class_NavigationAgent2D>` and
:ref:`NavigationAgent3D<class_NavigationAgent3D>` respectively.

New NavigationAgent nodes will automatically join the default navigation map on the :ref:`World2D<class_World2D>`/:ref:`World3D<class_World3D>`.

NavigationsAgent nodes are optional and not a hard requirement to use the navigation system.
Their entire functionality can be replaced with scripts and direct calls to the NavigationServer API.

.. tip::

    For more advanced uses consider :ref:`doc_navigation_using_navigationpathqueryobjects` over NavigationAgent nodes.

NavigationAgent Pathfinding
---------------------------

NavigationAgents query a new navigation path on their current navigation map when their ``target_position`` is set with a global position.

The result of the pathfinding can be influenced with the following properties.

- The ``navigation_layers`` bitmask can be used to limit the navigation meshes that the agent can use.
- The ``pathfinding_algorithm`` controls how the pathfinding travels through the navigation mesh polygons in the path search.
- The ``path_postprocessing`` sets if or how the raw path corridor found by the pathfinding is altered before it is returned.
- The ``path_metadata_flags`` enable the collection of additional path point meta data returned by the path.
- The ``simplify_path`` and ``simplify_epsilon`` properties can be used to remove less critical points from the path.

.. warning::

    Disabling path meta flags will disable related signal emissions on the agent.

NavigationAgent Pathfollowing
-----------------------------

After a ``target_position`` has been set for the agent, the next position to follow in the path
can be retrieved with the ``get_next_path_position()`` function.

Once the next path position is received, move the parent actor node of the agent
towards this path position with your own movement code.

.. note::

    The navigation system never moves the parent node of a NavigationAgent.
    The movement is entirely in the hands of users and their custom scripts.

NavigationAgents have their own internal logic to proceed with the current path and call for updates.

The ``get_next_path_position()`` function is responsible for updating many of the agent's internal states and properties.
The function should be repeatedly called *once* every ``physics_process`` until ``is_navigation_finished()`` tells that the path is finished.
The function should not be called after the target position or path end has been reached
as it can make the agent jitter in place due to the repeated path updates.
Always check very early in script with ``is_navigation_finished()`` if the path is already finished.

The following distance properties influence the path following behavior.

- At ``path_desired_distance`` from the next path position, the agent advances its internal path index to the subsequent next path position.
- At ``target_desired_distance`` from the target path position, the agent considers the target position to be reached and the path at its end.
- At ``path_max_distance`` from the ideal path to the next path position, the agent requests a new path because it was pushed too far off.

The important updates are all triggered with the ``get_next_path_position()`` function
when called in ``_physics_process()``.

NavigationAgents can be used with ``process`` but are still limited to a single update that happens in ``physics_process``.

Script examples for various nodes commonly used with NavigationAgents can be found further below.

Pathfollowing common problems
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are some common user problems and important caveats to consider when writing agent movement scripts.

- The path is returned empty
    If an agent queries a path before the navigation map synchronisation, e.g. in a ``_ready()`` function, the path might return empty. In this case the ``get_next_path_position()`` function will return the same position as the agent parent node and the agent will consider the path end reached. This is fixed by making a deferred call or using a callback e.g. waiting for the navigation map changed signal.

- The agent is stuck dancing between two positions
    This is usually caused by very frequent path updates every single frame, either deliberate or by accident (e.g. max path distance set too short). The pathfinding needs to find the closest position that are valid on navigation mesh. If a new path is requested every single frame the first path positions might end up switching constantly in front and behind the agent's current position, causing it to dance between the two positions.

- The agent is backtracking sometimes
    If an agent moves very fast it might overshoot the path_desired_distance check without ever advancing the path index. This can lead to the agent backtracking to the path point now behind it until it passes the distance check to increase the path index. Increase the desired distances accordingly for your agent speed and update rate usually fixes this as well as a more balanced navigation mesh polygon layout with not too many polygon edges cramped together in small spaces.

- The agent is sometimes looking backwards for a frame
    Same as with stuck dancing agents between two positions, this is usually caused by very frequent path updates every single frame. Depending on your navigation mesh layout, and especially when an agent is directly placed over a navigation mesh edge or edge connection, expect path positions to be sometimes slightly "behind" your actors current orientation. This happens due to precision issues and can not always be avoided. This is usually only a visible problem if actors are instantly rotated to face the current path position.

NavigationAgent Avoidance
-------------------------

This section explains how to use the navigation avoidance specific to NavigationAgents.

In order for NavigationAgents to use the avoidance feature the ``avoidance_enabled`` property must be set to ``true``.

.. image:: img/agent_avoidance_enabled.png

The ``velocity_computed`` signal of the NavigationAgent node must be connected to receive the safe velocity calculation result.

.. image:: img/agent_safevelocity_signal.png

Set the ``velocity`` of the NavigationAgent node in ``_physics_process()`` to update the agent with the current velocity of the agent's parent node.

While avoidance is enabled on the agent the ``safe_velocity`` vector will be received with the velocity_computed signal every physics frame.
This velocity vector should be used to move the NavigationAgent's parent node in order to avoidance collision with other avoidance using agents or avoidance obstacles.

.. note::

    Only other agents on the same map that are registered for avoidance themself will be considered in the avoidance calculation.

The following NavigationAgent properties are relevant for avoidance:

  - The property ``height`` is available in 3D only. The height together with the current global y-axis position of the agent determines the vertical placement of the agent in the avoidance simulation. Agents using the 2D avoidance will automatically ignore other agents or obstacles that are below or above them.
  - The property ``radius`` controls the size of the avoidance circle, or in case of 3D sphere, around the agent. This area describes the agents body and not the avoidance maneuver distance.
  - The property ``neighbor_distance`` controls the search radius of the agent when searching for other agents that should be avoided. A lower value reduces processing cost.
  - The property ``max_neighbors`` controls how many other agents are considered in the avoidance calculation if they all have overlapping radius.
    A lower value reduces processing cost but a too low value may result in agents ignoring the avoidance.
  - The properties ``time_horizon_agents`` and ``time_horizon_obstacles`` control the avoidance prediction time for other agents or obstacles in seconds. When agents calculate their safe velocities they choose velocities that can be kept for this amount of seconds without colliding with another avoidance object. The prediction time should be kept as low as possible as agents will slow down their velocities to avoid collision in that timeframe.
  - The property ``max_speed`` controls the maximum velocity allowed for the agents avoidance calculation.
    If the agents parents moves faster than this value the avoidance ``safe_velocity`` might not be accurate enough to avoid collision.
  - The property ``use_3d_avoidance`` switches the agent between the 2D avoidance (xz axis) and the 3D avoidance (xyz axis) on the next update.
    Note that 2D avoidance and 3D avoidance run in separate avoidance simulations so agents split between them do not affect each other.
  - The properties ``avoidance_layers`` and ``avoidance_mask`` are bitmasks similar to e.g. physics layers. Agents will only avoid other avoidance objects that are on an avoidance layer that matches at least one of their own avoidance mask bits.
  - The ``avoidance_priority`` makes agents with a higher priority ignore agents with a lower priority. This can be used to give certain agents more importance in the avoidance simulation, e.g. important non-playable characters, without constantly changing their entire avoidance layers or mask.


Avoidance exists in its own space and has no information from navigation meshes or physics collision.
Behind the scene avoidance agents are just circles with different radius on a flat 2D plane or spheres in an otherwise empty 3D space.
NavigationObstacles can be used to add some environment constrains to the avoidance simulation, see :ref:`doc_navigation_using_navigationobstacles`.

.. note::

    Avoidance does not affect the pathfinding. It should be seen as an additional option for constantly moving objects that cannot be (re)baked to a navigation mesh efficiently in order to move around them.

.. note::

    RVO avoidance makes implicit assumptions about natural agent behavior. E.g. that agents move on reasonable passing sides that can be assigned when they encounter each other.
    This means that very clinical avoidance test scenarios will commonly fail. E.g. agents moved directly against each other with perfect opposite velocities will fail because the agents can not get their passing sides assigned.

Using the NavigationAgent ``avoidance_enabled`` property is the preferred option
to toggle avoidance. The following code snippets can be used to
toggle avoidance on agents, create or delete avoidance callbacks or switch avoidance modes.

.. tabs::
 .. code-tab:: gdscript 2D GDScript

    extends NavigationAgent2D

    func _ready() -> void:
        var agent: RID = get_rid()
        # Enable avoidance
        NavigationServer2D.agent_set_avoidance_enabled(agent, true)
        # Create avoidance callback
        NavigationServer2D.agent_set_avoidance_callback(agent, Callable(self, "_avoidance_done"))

        # Disable avoidance
        NavigationServer2D.agent_set_avoidance_enabled(agent, false)
        # Delete avoidance callback
        NavigationServer2D.agent_set_avoidance_callback(agent, Callable())

 .. code-tab:: csharp 2D C#

    using Godot;

    public partial class MyNavigationAgent2D : NavigationAgent2D
    {
        public override void _Ready()
        {
            Rid agent = GetRid();
            // Enable avoidance
            NavigationServer2D.AgentSetAvoidanceEnabled(agent, true);
            // Create avoidance callback
            NavigationServer2D.AgentSetAvoidanceCallback(agent, Callable.From(AvoidanceDone));

            // Disable avoidance
            NavigationServer2D.AgentSetAvoidanceEnabled(agent, false);
            //Delete avoidance callback
            NavigationServer2D.AgentSetAvoidanceCallback(agent, default);
        }

        private void AvoidanceDone() { }
    }

 .. code-tab:: gdscript 3D GDScript

    extends NavigationAgent3D

    func _ready() -> void:
        var agent: RID = get_rid()
        # Enable avoidance
        NavigationServer3D.agent_set_avoidance_enabled(agent, true)
        # Create avoidance callback
        NavigationServer3D.agent_set_avoidance_callback(agent, Callable(self, "_avoidance_done"))
        # Switch to 3D avoidance
        NavigationServer3D.agent_set_use_3d_avoidance(agent, true)

        # Disable avoidance
        NavigationServer3D.agent_set_avoidance_enabled(agent, false)
        # Delete avoidance callback
        NavigationServer3D.agent_set_avoidance_callback(agent, Callable())
        # Switch to 2D avoidance
        NavigationServer3D.agent_set_use_3d_avoidance(agent, false)

 .. code-tab:: csharp 3D C#

    using Godot;

    public partial class MyNavigationAgent3D : NavigationAgent3D
    {
        public override void _Ready()
        {
            Rid agent = GetRid();
            // Enable avoidance
            NavigationServer3D.AgentSetAvoidanceEnabled(agent, true);
            // Create avoidance callback
            NavigationServer3D.AgentSetAvoidanceCallback(agent, Callable.From(AvoidanceDone));
            // Switch to 3D avoidance
            NavigationServer3D.AgentSetUse3DAvoidance(agent, true);

            // Disable avoidance
            NavigationServer3D.AgentSetAvoidanceEnabled(agent, false);
            //Delete avoidance callback
            NavigationServer3D.AgentSetAvoidanceCallback(agent, default);
            // Switch to 2D avoidance
            NavigationServer3D.AgentSetUse3DAvoidance(agent, false);
        }

        private void AvoidanceDone() { }
    }

NavigationAgent Script Templates
--------------------------------

The following sections provides script templates for nodes commonly used with NavigationAgents.

.. tabs::

   .. tab:: 2D GDScript

      .. tabs::

         .. code-tab:: gdscript Node2D

            extends Node2D

            @export var movement_speed: float = 4.0
            @onready var navigation_agent: NavigationAgent2D = get_node("NavigationAgent2D")
            var movement_delta: float

            func _ready() -> void:
                navigation_agent.velocity_computed.connect(Callable(_on_velocity_computed))

            func set_movement_target(movement_target: Vector2):
                navigation_agent.set_target_position(movement_target)

            func _physics_process(delta):
                # Do not query when the map has never synchronized and is empty.
                if NavigationServer2D.map_get_iteration_id(navigation_agent.get_navigation_map()) == 0:
                    return
                if navigation_agent.is_navigation_finished():
                    return

                movement_delta = movement_speed * delta
                var next_path_position: Vector2 = navigation_agent.get_next_path_position()
                var new_velocity: Vector2 = global_position.direction_to(next_path_position) * movement_delta
                if navigation_agent.avoidance_enabled:
                    navigation_agent.set_velocity(new_velocity)
                else:
                    _on_velocity_computed(new_velocity)

            func _on_velocity_computed(safe_velocity: Vector2) -> void:
                global_position = global_position.move_toward(global_position + safe_velocity, movement_delta)

         .. code-tab:: gdscript CharacterBody2D

            extends CharacterBody2D

            @export var movement_speed: float = 4.0
            @onready var navigation_agent: NavigationAgent2D = get_node("NavigationAgent2D")

            func _ready() -> void:
                navigation_agent.velocity_computed.connect(Callable(_on_velocity_computed))

            func set_movement_target(movement_target: Vector2):
                navigation_agent.set_target_position(movement_target)

            func _physics_process(delta):
                # Do not query when the map has never synchronized and is empty.
                if NavigationServer2D.map_get_iteration_id(navigation_agent.get_navigation_map()) == 0:
                    return
                if navigation_agent.is_navigation_finished():
                    return

                var next_path_position: Vector2 = navigation_agent.get_next_path_position()
                var new_velocity: Vector2 = global_position.direction_to(next_path_position) * movement_speed
                if navigation_agent.avoidance_enabled:
                    navigation_agent.set_velocity(new_velocity)
                else:
                    _on_velocity_computed(new_velocity)

            func _on_velocity_computed(safe_velocity: Vector2):
                velocity = safe_velocity
                move_and_slide()

         .. code-tab:: gdscript RigidBody2D

            extends RigidBody2D

            @export var movement_speed: float = 4.0
            @onready var navigation_agent: NavigationAgent2D = get_node("NavigationAgent2D")

            func _ready() -> void:
                navigation_agent.velocity_computed.connect(Callable(_on_velocity_computed))

            func set_movement_target(movement_target: Vector2):
                navigation_agent.set_target_position(movement_target)

            func _physics_process(delta):
                # Do not query when the map has never synchronized and is empty.
                if NavigationServer2D.map_get_iteration_id(navigation_agent.get_navigation_map()) == 0:
                    return
                if navigation_agent.is_navigation_finished():
                    return

                var next_path_position: Vector2 = navigation_agent.get_next_path_position()
                var new_velocity: Vector2 = global_position.direction_to(next_path_position) * movement_speed
                if navigation_agent.avoidance_enabled:
                    navigation_agent.set_velocity(new_velocity)
                else:
                    _on_velocity_computed(new_velocity)

            func _on_velocity_computed(safe_velocity: Vector2):
                linear_velocity = safe_velocity

   .. tab:: 2D C#

      .. tabs::

         .. code-tab:: csharp Node2D

            using Godot;

            public partial class MyNode2D : Node2D
            {
                [Export]
                public float MovementSpeed { get; set; } = 4.0f;
                NavigationAgent2D _navigationAgent;
                private float _movementDelta;

                public override void _Ready()
                {
                    _navigationAgent = GetNode<NavigationAgent2D>("NavigationAgent2D");
                    _navigationAgent.VelocityComputed += OnVelocityComputed;
                }

                private void SetMovementTarget(Vector2 movementTarget)
                {
                    _navigationAgent.TargetPosition = movementTarget;
                }

                public override void _PhysicsProcess(double delta)
                {
                    // Do not query when the map has never synchronized and is empty.
                    if (NavigationServer2D.MapGetIterationId(_navigationAgent.GetNavigationMap()) == 0)
                    {
                        return;
                    }

                    if (_navigationAgent.IsNavigationFinished())
                    {
                        return;
                    }

                    _movementDelta = MovementSpeed * (float)delta;
                    Vector2 nextPathPosition = _navigationAgent.GetNextPathPosition();
                    Vector2 newVelocity = GlobalPosition.DirectionTo(nextPathPosition) * _movementDelta;
                    if (_navigationAgent.AvoidanceEnabled)
                    {
                        _navigationAgent.Velocity = newVelocity;
                    }
                    else
                    {
                        OnVelocityComputed(newVelocity);
                    }
                }

                private void OnVelocityComputed(Vector2 safeVelocity)
                {
                    GlobalPosition = GlobalPosition.MoveToward(GlobalPosition + safeVelocity, _movementDelta);
                }
            }

         .. code-tab:: csharp CharacterBody2D

            using Godot;

            public partial class MyCharacterBody2D : CharacterBody2D
            {
                [Export]
                public float MovementSpeed { get; set; } = 4.0f;
                NavigationAgent2D _navigationAgent;

                public override void _Ready()
                {
                    _navigationAgent = GetNode<NavigationAgent2D>("NavigationAgent2D");
                    _navigationAgent.VelocityComputed += OnVelocityComputed;
                }

                private void SetMovementTarget(Vector2 movementTarget)
                {
                    _navigationAgent.TargetPosition = movementTarget;
                }

                public override void _PhysicsProcess(double delta)
                {
                    // Do not query when the map has never synchronized and is empty.
                    if (NavigationServer2D.MapGetIterationId(_navigationAgent.GetNavigationMap()) == 0)
                    {
                        return;
                    }

                    if (_navigationAgent.IsNavigationFinished())
                    {
                        return;
                    }

                    Vector2 nextPathPosition = _navigationAgent.GetNextPathPosition();
                    Vector2 newVelocity = GlobalPosition.DirectionTo(nextPathPosition) * MovementSpeed;
                    if (_navigationAgent.AvoidanceEnabled)
                    {
                        _navigationAgent.Velocity = newVelocity;
                    }
                    else
                    {
                        OnVelocityComputed(newVelocity);
                    }
                }

                private void OnVelocityComputed(Vector2 safeVelocity)
                {
                    Velocity = safeVelocity;
                    MoveAndSlide();
                }
            }

         .. code-tab:: csharp RigidBody2D

            using Godot;

            public partial class MyRigidBody2D : RigidBody2D
            {
                [Export]
                public float MovementSpeed { get; set; } = 4.0f;
                NavigationAgent2D _navigationAgent;

                public override void _Ready()
                {
                    _navigationAgent = GetNode<NavigationAgent2D>("NavigationAgent2D");
                    _navigationAgent.VelocityComputed += OnVelocityComputed;
                }

                private void SetMovementTarget(Vector2 movementTarget)
                {
                    _navigationAgent.TargetPosition = movementTarget;
                }

                public override void _PhysicsProcess(double delta)
                {
                    // Do not query when the map has never synchronized and is empty.
                    if (NavigationServer2D.MapGetIterationId(_navigationAgent.GetNavigationMap()) == 0)
                    {
                        return;
                    }

                    if (_navigationAgent.IsNavigationFinished())
                    {
                        return;
                    }

                    Vector2 nextPathPosition = _navigationAgent.GetNextPathPosition();
                    Vector2 newVelocity = GlobalPosition.DirectionTo(nextPathPosition) * MovementSpeed;
                    if (_navigationAgent.AvoidanceEnabled)
                    {
                        _navigationAgent.Velocity = newVelocity;
                    }
                    else
                    {
                        OnVelocityComputed(newVelocity);
                    }
                }

                private void OnVelocityComputed(Vector2 safeVelocity)
                {
                    LinearVelocity = safeVelocity;
                }
            }

   .. tab:: 3D GDScript

      .. tabs::

         .. code-tab:: gdscript Node3D

            extends Node3D

            @export var movement_speed: float = 4.0
            @onready var navigation_agent: NavigationAgent3D = get_node("NavigationAgent3D")
            var physics_delta: float

            func _ready() -> void:
                navigation_agent.velocity_computed.connect(Callable(_on_velocity_computed))

            func set_movement_target(movement_target: Vector3):
                navigation_agent.set_target_position(movement_target)

            func _physics_process(delta):
                # Save the delta for use in _on_velocity_computed.
                physics_delta = delta
                # Do not query when the map has never synchronized and is empty.
                if NavigationServer3D.map_get_iteration_id(navigation_agent.get_navigation_map()) == 0:
                    return
                if navigation_agent.is_navigation_finished():
                    return

                var next_path_position: Vector3 = navigation_agent.get_next_path_position()
                var new_velocity: Vector3 = global_position.direction_to(next_path_position) * movement_speed
                if navigation_agent.avoidance_enabled:
                    navigation_agent.set_velocity(new_velocity)
                else:
                    _on_velocity_computed(new_velocity)

            func _on_velocity_computed(safe_velocity: Vector3) -> void:
                global_position = global_position.move_toward(global_position + safe_velocity, physics_delta * movement_speed)

         .. code-tab:: gdscript CharacterBody3D

            extends CharacterBody3D

            @export var movement_speed: float = 4.0
            @onready var navigation_agent: NavigationAgent3D = get_node("NavigationAgent3D")

            func _ready() -> void:
                navigation_agent.velocity_computed.connect(Callable(_on_velocity_computed))

            func set_movement_target(movement_target: Vector3):
                navigation_agent.set_target_position(movement_target)

            func _physics_process(delta):
                # Do not query when the map has never synchronized and is empty.
                if NavigationServer3D.map_get_iteration_id(navigation_agent.get_navigation_map()) == 0:
                    return
                if navigation_agent.is_navigation_finished():
                    return

                var next_path_position: Vector3 = navigation_agent.get_next_path_position()
                var new_velocity: Vector3 = global_position.direction_to(next_path_position) * movement_speed
                if navigation_agent.avoidance_enabled:
                    navigation_agent.set_velocity(new_velocity)
                else:
                    _on_velocity_computed(new_velocity)

            func _on_velocity_computed(safe_velocity: Vector3):
                velocity = safe_velocity
                move_and_slide()

         .. code-tab:: gdscript RigidBody3D

            extends RigidBody3D

            @export var movement_speed: float = 4.0
            @onready var navigation_agent: NavigationAgent3D = get_node("NavigationAgent3D")

            func _ready() -> void:
                navigation_agent.velocity_computed.connect(Callable(_on_velocity_computed))

            func set_movement_target(movement_target: Vector3):
                navigation_agent.set_target_position(movement_target)

            func _physics_process(delta):
                # Do not query when the map has never synchronized and is empty.
                if NavigationServer3D.map_get_iteration_id(navigation_agent.get_navigation_map()) == 0:
                    return
                if navigation_agent.is_navigation_finished():
                    return

                var next_path_position: Vector3 = navigation_agent.get_next_path_position()
                var new_velocity: Vector3 = global_position.direction_to(next_path_position) * movement_speed
                if navigation_agent.avoidance_enabled:
                    navigation_agent.set_velocity(new_velocity)
                else:
                    _on_velocity_computed(new_velocity)

            func _on_velocity_computed(safe_velocity: Vector3):
                linear_velocity = safe_velocity

   .. tab:: 3D C#

      .. tabs::

         .. code-tab:: csharp Node3D

            using Godot;

            public partial class MyNode3D : Node3D
            {
                [Export]
                public float MovementSpeed { get; set; } = 4.0f;
                NavigationAgent3D _navigationAgent;
                private float _movementDelta;

                public override void _Ready()
                {
                    _navigationAgent = GetNode<NavigationAgent3D>("NavigationAgent3D");
                    _navigationAgent.VelocityComputed += OnVelocityComputed;
                }

                private void SetMovementTarget(Vector3 movementTarget)
                {
                    _navigationAgent.TargetPosition = movementTarget;
                }

                public override void _PhysicsProcess(double delta)
                {
                    // Do not query when the map has never synchronized and is empty.
                    if (NavigationServer3D.MapGetIterationId(_navigationAgent.GetNavigationMap()) == 0)
                    {
                        return;
                    }

                    if (_navigationAgent.IsNavigationFinished())
                    {
                        return;
                    }

                    _movementDelta = MovementSpeed * (float)delta;
                    Vector3 nextPathPosition = _navigationAgent.GetNextPathPosition();
                    Vector3 newVelocity = GlobalPosition.DirectionTo(nextPathPosition) * _movementDelta;
                    if (_navigationAgent.AvoidanceEnabled)
                    {
                        _navigationAgent.Velocity = newVelocity;
                    }
                    else
                    {
                        OnVelocityComputed(newVelocity);
                    }
                }

                private void OnVelocityComputed(Vector3 safeVelocity)
                {
                    GlobalPosition = GlobalPosition.MoveToward(GlobalPosition + safeVelocity, _movementDelta);
                }
            }

         .. code-tab:: csharp CharacterBody3D

            using Godot;

            public partial class MyCharacterBody3D : CharacterBody3D
            {
                [Export]
                public float MovementSpeed { get; set; } = 4.0f;
                NavigationAgent3D _navigationAgent;

                public override void _Ready()
                {
                    _navigationAgent = GetNode<NavigationAgent3D>("NavigationAgent3D");
                    _navigationAgent.VelocityComputed += OnVelocityComputed;
                }

                private void SetMovementTarget(Vector3 movementTarget)
                {
                    _navigationAgent.TargetPosition = movementTarget;
                }

                public override void _PhysicsProcess(double delta)
                {
                    // Do not query when the map has never synchronized and is empty.
                    if (NavigationServer3D.MapGetIterationId(_navigationAgent.GetNavigationMap()) == 0)
                    {
                        return;
                    }

                    if (_navigationAgent.IsNavigationFinished())
                    {
                        return;
                    }

                    Vector3 nextPathPosition = _navigationAgent.GetNextPathPosition();
                    Vector3 newVelocity = GlobalPosition.DirectionTo(nextPathPosition) * MovementSpeed;
                    if (_navigationAgent.AvoidanceEnabled)
                    {
                        _navigationAgent.Velocity = newVelocity;
                    }
                    else
                    {
                        OnVelocityComputed(newVelocity);
                    }
                }

                private void OnVelocityComputed(Vector3 safeVelocity)
                {
                    Velocity = safeVelocity;
                    MoveAndSlide();
                }
            }

         .. code-tab:: csharp RigidBody3D

            using Godot;

            public partial class MyRigidBody3D : RigidBody3D
            {
                [Export]
                public float MovementSpeed { get; set; } = 4.0f;
                NavigationAgent3D _navigationAgent;

                public override void _Ready()
                {
                    _navigationAgent = GetNode<NavigationAgent3D>("NavigationAgent3D");
                    _navigationAgent.VelocityComputed += OnVelocityComputed;
                }

                private void SetMovementTarget(Vector3 movementTarget)
                {
                    _navigationAgent.TargetPosition = movementTarget;
                }

                public override void _PhysicsProcess(double delta)
                {
                    // Do not query when the map has never synchronized and is empty.
                    if (NavigationServer3D.MapGetIterationId(_navigationAgent.GetNavigationMap()) == 0)
                    {
                        return;
                    }

                    if (_navigationAgent.IsNavigationFinished())
                    {
                        return;
                    }

                    Vector3 nextPathPosition = _navigationAgent.GetNextPathPosition();
                    Vector3 newVelocity = GlobalPosition.DirectionTo(nextPathPosition) * MovementSpeed;
                    if (_navigationAgent.AvoidanceEnabled)
                    {
                        _navigationAgent.Velocity = newVelocity;
                    }
                    else
                    {
                        OnVelocityComputed(newVelocity);
                    }
                }

                private void OnVelocityComputed(Vector3 safeVelocity)
                {
                    LinearVelocity = safeVelocity;
                }
            }
