.. _doc_state_design_pattern:

State Design Pattern
====================

Introduction
------------

Scripting a game can be difficult when there are many states that need to handled, but
only one script can be attached to a node at a time. Instead of creating a state machine
within your player's control script, it would development simpler if the states were
separated out into different classes.

Setup
-----

The feature of inheritance is useful for getting started with this design priniciple.
A class should be created that describes the base features of the player. For now, a
player will be limited to three actions: move left, move right and jump. This means
there will be three states: idle, run and jump.

Below is the generic state, from which all other states will inherit.

.. tabs::
  .. code-tab:: gdscript GDScript

    extends Node2D
    
    class_name State

    var change_state
    var kinematic_body_2d
    var velocity

    var gravity = Vecotr2(0, 8)

    func _physics_process(delta):
      kinematic_body_2d.move_and_slide(velocity, Vector2.UP)
      velocity += gravity
      if (kinematic_body_2d.is_on_floor()):
        _on_ground()

    func _on_ground():
      velocity.y = 0

    func _idle():
      change_state.call_func("idle")

    func _run():
      change_state.call_func("run")

    func setup(change_state, animated_sprite, kinematic_body_2d, velocity):
	self.change_state = change_state
	self.animated_sprite = animated_sprite
	self.kinematic_body_2d = kinematic_body_2d
        self.velocity = velocity

    func move_left():
	pass

    func move_right():
	pass

    func jump():
	pass

A few notes on the above script. First, this implementation uses a 'setup' method to assign
references. These references will be instantiated in the parent of this state. This helps with something 
in programming known as cohesion. The state of the player does not want the responsibility of creating 
these variables, but does want to be able to use them. However, this does make the state 'coupled' to the 
state's parent. This means that the state is highly reliant on whether it has a parent which contains 
these variables. So, remember that coupling and cohesion are important concepts when it comes to code management.

Second, there are some methods in the script for moving and jumping, but no implementation. The state script
just uses 'pass' to show that it will not execute any instructions when the methods are called. This is important.

Third, the '_physics_process' method is actually implemented here. This allows the states to have a default
'_phyics_process' implementation where gravity is constantly applied to the player. The way that the states can modify
the movement of the player is to use the velocity variable defined in their base class, then call their base class'
implementation of '_physics_process'.

Finally, this script is actually being designated as a class named 'State'. This makes refactoring the code
easier, since the file path from using the 'load' and 'preload' functions in Godot will not be needed.

So, now that there is a base state, the three states discussed earlier can be implemented.

.. tabs::
  .. code-tab:: gdscript GDScript

    # filename: ground_idle_state.gd

    extends State

    class_name GroundIdleState

    func _ready():
      animated_sprite.play("idle")

    func _flip_direction():
      animated_sprite.flip_h = not animated_sprite.flip_h

    func move_left():
      if animated_sprite.flip_h:
        _run()
      else:
        _flip_direction()

    func move_right():
      if not animated_sprite.flip_h:
        _run()
      else:
        _flip_direction()

    func jump():
      change_state.call_func("jump")

.. tabs::
  .. code-tab:: gdscript GDScript

    # filename: ground_run_state.gd

    extends State

    class_name GroundRunState

    var move_speed = Vector2(180, 0)
    var min_move_speed = 0.005
    var friction = 0.32

    func _ready():
      animated_sprite.play("run")
      if animated_sprite.flip_h:
         move_speed.x *= -1

    func _physics_process(delta):
      .physics_process(delta)
      if abs(velocity) < min_move_speed:
        _idle()
      velocity.x *= friction
    
    func move_left():
      if animated_sprite.flip_h:
        velocity += move_speed
      else:
        _idle()

    func move_right():
      if not animated_sprite.flip_h:
        velocity += move_speed
      else:
        _idle()

    func jump():
      change_state.call_func("jump")

.. tabs::
  .. code-tab:: gdscript GDScript

    # filename: aerial_jump_state.gd

    extends State

    class_name AerialJumpState

    var jump_force = Vector2(0, 450)
    var move_speed = Vector2(180, 0)
    var aerial_friction = 0.5

    func _ready():
      animated_sprite.play("jump")
      velocity += jump_force

    func _physics_process(delta):
      .physics_process(delta)
      velocity.x *= aerial_friction  

    func _on_ground():
      ._on_ground()
      change_state.call_func("idle")

    func move_left():
      velocity -= move_speed

    func move_right():
      velocity += move_speed

There is a round-about method for obtaining a state instance. A state factory can be used.

.. tabs::
  .. code-tab:: gdscript GDScript

    #filename: state_factory.gd

    class_name StateFactory

    var states

    func _init():
      states = {
          "idle":GroundIdleState,
          "run":GroundRunState,
          "jump":AerialJumpState
      }

    func get_state(state_name):
      if states.has(state_name):
        return states.get(state_name)
      else:
        printerr("No state ", state_name, " in state factory!")

This will look for states in a dictionary and return the state if found.

Now that all the states are defined with their own scripts, it is time to figure out
how those references that passed to them will be instantiated. Since these references
will not change even the current state will, we can call this new script 'persistant state'.

.. tabs::
  .. code-tab:: gdscript GDScript

    # filename: persistant_state.gd

    extends KinematicBody2D

    class_name PersistantState

    var state
    var state_factory

    var velocity = Vector2()

    func _ready():
      state_factory = StateFactory.new()
      change_state("idle")

    func change_state(new_state_name):
      state.queue_free()
      state = state_factory.get_state(new_state_name)
      state.setup(funcref(self, "change_state"), $AnimatedSprite, self, velocity)
      state.name = "current_state"
      add_child(state)

