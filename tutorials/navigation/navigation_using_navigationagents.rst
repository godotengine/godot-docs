.. _doc_navigation_using_navigationagents:

Using NavigationAgents
======================

NavigationsAgents are helper nodes to facilitate common calls to the NavigationServer API
on behalf of the parent actor node in a more convenient manner for beginners.

2D and 3D version of NavigationAgents are available as
:ref:`NavigationAgent2D<class_NavigationAgent2D>` and
:ref:`NavigationAgent3D<class_NavigationAgent3D>` respectively.

NavigationsAgents are entirely optional for navigation pathfinding.
The functionality of NavigationsAgents can be recreated with scripts and direct
calls to the NavigationServer API. If the default NavigationsAgent does not do what you want
for your game feel free to design your own NavigationsAgent with scripts.

.. warning::

    NavigationsAgent nodes and NavigationServer ``agents`` are not the same.
    The later is an RVO avoidance agent and solely used for avoidance.
    RVO avoidance agents are not involved in regular pathfinding.

NavigationAgent Pathfinding
---------------------------

To use NavigationAgents for pathfinding, place a NavigationAgent2D/3D Node below a Node2D/3D inheriting parent node.

To have the agent query a path to a target position use the ``set_target_position()`` method.
Once the target has been set, the next position to follow in the path
can be retrieved with the ``get_next_path_position()`` function. Move the parent actor node
to this position with your own movement code. On the next ``physics_frame``, call
``get_next_path_position()`` again for the next position and repeat this until the path ends.

NavigationAgents have their own internal logic to proceed with the current path and call for updates.
NavigationAgents recognize by distance when a path point or the final target is reached.
NavigationAgents refresh a path automatically when too far away from the current pathpoint.
The important updates are all triggered with the ``get_next_path_position()`` function
when called in ``_physics_process()``.

Be careful calling other NavigationAgent functions not required for path movement
while the actor is following a path, as many function trigger a full path refresh.

.. note::

    New NavigationAgents will automatically join the
    default navigation map for their 2D/3D dimension.

.. warning::

    Resetting the path every frame (by accident) might get the actor to stutter or spin around in place.

NavigationAgents were designed with ``_physics_process()`` in mind to keep in sync with both :ref:`NavigationServer3D<class_NavigationServer3D>` and :ref:`PhysicsServer3D<class_PhysicsServer3D>`.

They work well out of the box with :ref:`CharacterBody2D<class_CharacterBody2D>` and :ref:`CharacterBody3D<class_CharacterBody3D>` as well as any rigid bodies.

.. warning::

    The important restriction for non-physics characters is that the NavigationAgent node only accepts a single update each ``physics_frame`` as further updates will be blocked.

.. warning::

    If a NavigationAgent is used with ``_process()`` at high framerate make sure to accumulate the values of multiple frames and call the NavigationAgent function only once each ``physics_frame``.

.. _doc_navigation_script_templates:


NavigationAgent Avoidance
-------------------------

This section explains how to use the built-in avoidance specific
to NavigationAgent nodes. For general avoidance use and more technical details
on RVO avoidance see :ref:`doc_navigation_using_agent_avoidance`.


In order for NavigationAgents to use the avoidance feature the ``enable_avoidance`` property must be set to ``true``.

.. image:: img/agent_avoidance_enabled.png

.. note::

    Only other agents on the same map that are registered for avoidance themself will be considered in the avoidance calculation.

The following NavigationAgent properties are relevant for avoidance:

  - The property ``radius`` controls the size of the avoidance circle around the agent. This area describes the agents body and not the avoidance maneuver distance.
  - The property ``neighbor_distance`` controls the search radius of the agent when searching for other agents that should be avoided. A lower value reduces processing cost.
  - The property ``max_neighbors`` controls how many other agents are considered in the avoidance calculation if they all have overlapping radius.
    A lower value reduces processing cost but a too low value may result in agents ignoring the avoidance.
  - The property ``time_horizion`` controls the avoidance maneuver start and end distance.
    How early and for how long an agents reacts to other agents within the ``neighbor_distance`` radius to correct its own velocity.
    A lower value results in avoidance kicking in with a very intense velocity change at a short distance while a high value results in very early but small velocity changes.
  - The property ``max_speed`` controls the maximum velocity assumed for the agents avoidance calculation.
    If the agents parents moves faster than this value the avoidance ``safe_velocity`` might not be accurate enough to avoid collision.

The ``velocity_computed`` signal of the agent node must be connected to receive the ``safe_velocity`` calculation result.

.. image:: img/agent_safevelocity_signal.png

Additional the current velocity of the agents parent must be set for the agent in ``_physics_process()`` with ``set_velocity()``.

After a short wait for processing the avoidance (still in the same frame) the ``safe_velocity`` vector will be received with the signal.
This velocity vector should be used to move the NavigationAgent's parent node in order to avoidance collision with other avoidance registered agents in proximity.

RVO exists in its own space and has no information from navigation meshes or physics collision.
Behind the scene avoidance agents are just circles with different radius on a flat plane.
In narrow places obstructed with collision objects, the avoidance maneuver radius needs to be
reduced considerably or disabled else the avoidance velocity will get actors stuck on collision easily.

.. note::

    Avoidance should be seen as a last resort option for constantly moving objects that cannot be re(baked) to a navigationmesh efficiently in order to move around them.

.. warning::

    Actors that move according to their avoidance agent velocity will not move at
    full speed, can leave the navigation mesh bounds and can make movement
    pauses when the avoidance simulation becomes unsolvable.

Using the NavigationAgent ``enable_avoidance`` property is the preferred option
to toggle avoidance but the following scripts for NavigationAgents can be
used to create or delete avoidance callbacks for the agent RID.

.. tabs::
 .. code-tab:: gdscript GDScript

    extends NavigationAgent2D

    var agent: RID = get_rid()
    # Enable
    NavigationServer2D::get_singleton()->agent_set_callback(agent, self._avoidance_done)
    # Disable
    NavigationServer2D::get_singleton()->agent_set_callback(agent, Callable())

.. tabs::
 .. code-tab:: gdscript GDScript

    extends NavigationAgent3D

    var agent: RID = get_rid()
    # Enable
    NavigationServer3D::get_singleton()->agent_set_callback(agent, self._avoidance_done)
    # Disable
    NavigationServer3D::get_singleton()->agent_set_callback(agent, Callable())

NavigationAgent Script Templates
--------------------------------

The following sections provides script templates for nodes commonly used with NavigationAgents.

Actor as Node3D
~~~~~~~~~~~~~~~

This script adds basic navigation movement to a Node3D with a NavigationAgent3D child node.

.. tabs::
 .. code-tab:: gdscript GDScript

    extends Node3D

    @export var movement_speed: float = 4.0
    @onready var navigation_agent: NavigationAgent3D = get_node("NavigationAgent3D")
    var movement_delta: float

    func _ready() -> void:
        navigation_agent.velocity_computed.connect(Callable(_on_velocity_computed))

    func set_movement_target(movement_target: Vector3):
        navigation_agent.set_target_position(movement_target)

    func _physics_process(delta):
        if navigation_agent.is_navigation_finished():
            return

        movement_delta = movement_speed * delta
        var next_path_position: Vector3 = navigation_agent.get_next_path_position()
        var current_agent_position: Vector3 = global_position
        var new_velocity: Vector3 = (next_path_position - current_agent_position).normalized() * movement_delta
        if navigation_agent.avoidance_enabled:
            navigation_agent.set_velocity(new_velocity)
        else:
            _on_velocity_computed(new_velocity)

    func _on_velocity_computed(safe_velocity: Vector3) -> void:
        global_position = global_position.move_toward(global_position + safe_velocity, movement_delta)

Actor as CharacterBody3D
~~~~~~~~~~~~~~~~~~~~~~~~

This script adds basic navigation movement to a CharacterBody3D with a NavigationAgent3D child node.

.. tabs::
 .. code-tab:: gdscript GDScript

    extends CharacterBody3D

    @export var movement_speed: float = 4.0
    @onready var navigation_agent: NavigationAgent3D = get_node("NavigationAgent3D")

    func _ready() -> void:
        navigation_agent.velocity_computed.connect(Callable(_on_velocity_computed))

    func set_movement_target(movement_target: Vector3):
        navigation_agent.set_target_position(movement_target)

    func _physics_process(delta):
        if navigation_agent.is_navigation_finished():
            return

        var next_path_position: Vector3 = navigation_agent.get_next_path_position()
        var current_agent_position: Vector3 = global_position
        var new_velocity: Vector3 = (next_path_position - current_agent_position).normalized() * movement_speed
        if navigation_agent.avoidance_enabled:
            navigation_agent.set_velocity(new_velocity)
        else:
            _on_velocity_computed(new_velocity)

    func _on_velocity_computed(safe_velocity: Vector3):
        velocity = safe_velocity
        move_and_slide()

Actor as RigidBody3D
~~~~~~~~~~~~~~~~~~~~

This script adds basic navigation movement to a RigidBody3D with a NavigationAgent3D child node.

.. tabs::
 .. code-tab:: gdscript GDScript

    extends RigidBody3D

    @export var movement_speed: float = 4.0
    @onready var navigation_agent: NavigationAgent3D = get_node("NavigationAgent3D")

    func _ready() -> void:
        navigation_agent.velocity_computed.connect(Callable(_on_velocity_computed))

    func set_movement_target(movement_target: Vector3):
        navigation_agent.set_target_position(movement_target)

    func _physics_process(delta):
        if navigation_agent.is_navigation_finished():
            return

        var next_path_position: Vector3 = navigation_agent.get_next_path_position()
        var current_agent_position: Vector3 = global_position
        var new_velocity: Vector3 = (next_path_position - current_agent_position).normalized() * movement_speed
        if navigation_agent.avoidance_enabled:
            navigation_agent.set_velocity(new_velocity)
        else:
            _on_velocity_computed(new_velocity)

    func _on_velocity_computed(safe_velocity: Vector3):
        linear_velocity = safe_velocity
