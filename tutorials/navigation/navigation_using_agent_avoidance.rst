.. _doc_navigation_using_agent_avoidance:

Using Agent Avoidance
=====================

This section is about how to use agent avoidance with the NavigationServer and
documents how agent avoidance is implemented in Godot.

For avoidance with NavigationAgents see :ref:`doc_navigation_using_navigationagents`.

Agent avoidance helps to prevent direct collision with other agents or moving obstacles
while the agents still follow their original velocity as best as possible.

Avoidance in Godot is implemented with the help of the RVO library (Reciprocal Velocity Obstacle).
RVO places agents on a flat RVO map and gives each agent a ``radius`` and a ``position``.
Agents with overlapping radius compute a ``safe_velocity`` from their
current ``velocity``. The ``safe_velocity`` then needs to replace the original
submitted ``velocity`` to move the actor behind the agent with custom movement code.

.. note::

    RVO avoidance is not involved in regular pathfinding, it is a completely separate system.
    If used inappropriately, the RVO avoidance can actively harm the perceived pathfinding quality.

Creating Avoidance Agents with Scripts
--------------------------------------

Agents and obstacles share the same NavigationServer API functions.

Creating agents on the NavigationServer is only required for avoidance but not for normal pathfinding.
Pathfinding is map and region navmesh based while avoidance is purely map and agent based.

.. tabs::
 .. code-tab:: gdscript GDScript

    extends Node3D

    var new_agent_rid: RID = NavigationServer3D.agent_create()
    var default_3d_map_rid: RID = get_world_3d().get_navigation_map()

    NavigationServer3D.agent_set_map(new_agent_rid, default_3d_map_rid)
    NavigationServer3D.agent_set_radius(new_agent_rid, 0.5)
    NavigationServer3D.agent_set_position(new_agent_rid, global_transform.origin)

To receive safe_velocity signals for avoidance for the agent a callback needs to be registered on the NavigationServer.

.. tabs::
 .. code-tab:: gdscript GDScript

    extends Node3D

    var agent_rid: RID = NavigationServer3D.agent_create()
    NavigationServer3D.agent_set_callback(agent_rid, self.on_safe_velocity_computed)

    func on_safe_velocity_computed(safe_velocity: Vector3):
        # do your avoidance movement

After the current and new calculated velocity needs to be passed to the NavigationServer each physics frame to trigger the safe_velocity callback when the avoidance processing is finished.

.. tabs::
 .. code-tab:: gdscript GDScript

    func _physics_process(delta):

        NavigationServer3D.agent_set_velocity(current_velocity)
        NavigationServer3D.agent_set_target_velocity(new_velocity)

.. warning::

    If _process() is used instead of _physics_process() at a higher framerate
    than physics the agent velocity should not be updated more than ones each
    physics frame e.g. by tracking the Engine.get_physics_frames().
