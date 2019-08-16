.. _doc_state_design_pattern:

State Design Pattern
====================

Introduction
------------

Scripting a game can be difficult when there are many states that need to handled, but
only one script can be attached to a node at a time. Instead of creating a state machine
within the player's control script, it would make development simpler if the states were
separated out into different classes.

Script-Setup
------------

The feature of inheritance is useful for getting started with this design principle.
A class should be created that describes the base features of the player. For now, a
player will be limited to two actions: move left, move right. This means
there will be two states: idle and run.

Below is the generic state, from which all other states will inherit.

.. tabs::
  .. code-tab:: gdscript GDScript

    extends Node2D
    
    class_name State

    var change_state
    var animated_sprite
    var kinematic_body_2d
    var velocity

    func _physics_process(delta):
      kinematic_body_2d.move_and_slide(velocity, Vector2.UP)

    func setup(change_state, animated_sprite, kinematic_body_2d, velocity):
	self.change_state = change_state
	self.animated_sprite = animated_sprite
	self.kinematic_body_2d = kinematic_body_2d
        self.velocity = velocity

    func move_left():
	pass

    func move_right():
	pass

A few notes on the above script. First, this implementation uses a 
''setup(change_state, animated_sprite, kinematic_body_2d, velocity)'' method to assign
references. These references will be instantiated in the parent of this state. This helps with something 
in programming known as cohesion. The state of the player does not want the responsibility of creating 
these variables, but does want to be able to use them. However, this does make the state 'coupled' to the 
state's parent. This means that the state is highly reliant on whether it has a parent which contains 
these variables. So, remember that coupling and cohesion are important concepts when it comes to code management.

.. note:: 
  See the following page for more details on cohesion and coupling:
  https://courses.cs.washington.edu/courses/cse403/96sp/coupling-cohesion.html

Second, there are some methods in the script for moving, but no implementation. The state script
just uses 'pass' to show that it will not execute any instructions when the methods are called. This is important.

Third, the ''_physics_process(delta)'' method is actually implemented here. This allows the states to have a default
''_phyics_process(delta)'' implementation where a velocity is used to move the player. The way that the states can modify
the movement of the player is to use the velocity variable defined in their base class, then call their base class's
implementation of ''_physics_process(delta)''.

Finally, this script is actually being designated as a class named ''State''. This makes refactoring the code
easier, since the file path from using the 'load' and 'preload' functions in Godot will not be needed.

So, now that there is a base state, the three states discussed earlier can be implemented.

.. tabs::
  .. code-tab:: gdscript GDScript

    # filename: idle_state.gd

    extends State

    class_name IdleState

    func _ready():
      animated_sprite.play("idle")

    func _flip_direction():
      animated_sprite.flip_h = not animated_sprite.flip_h

    func move_left():
      if animated_sprite.flip_h:
        change_state.call_func("run")
      else:
        _flip_direction()

    func move_right():
      if not animated_sprite.flip_h:
        change_state.call_func("run")
      else:
        _flip_direction()

.. tabs::
  .. code-tab:: gdscript GDScript

    # filename: run_state.gd

    extends State

    class_name RunState

    var move_speed = Vector2(180, 0)
    var min_move_speed = 0.005
    var friction = 0.32

    func _ready():
      animated_sprite.play("run")
      if animated_sprite.flip_h:
         move_speed.x *= -1
      velocity += move_speed

    func _physics_process(delta):
      .physics_process(delta)
      if abs(velocity) < min_move_speed:
        change_state.call_func("idle")
      velocity.x *= friction
    
    func move_left():
      if animated_sprite.flip_h:
        velocity += move_speed
      else:
        change_state.call_func("idle")

    func move_right():
      if not animated_sprite.flip_h:
        velocity += move_speed
      else:
        change_state.call_func("idle")

There is a round-about method for obtaining a state instance. A state factory can be used.

.. tabs::
  .. code-tab:: gdscript GDScript

    #filename: state_factory.gd

    class_name StateFactory

    var states

    func _init():
      states = {
          "idle":IdleState,
          "run":RunState
      }

    func get_state(state_name):
      if states.has(state_name):
        return states.get(state_name)
      else:
        printerr("No state ", state_name, " in state factory!")

This will look for states in a dictionary and return the state if found.

Now that all the states are defined with their own scripts, it is time to figure out
how those references that passed to them will be instantiated. Since these references
will not change even the current state will, it makes sense to call this new script ''persistent state.gd''.

.. tabs::
  .. code-tab:: gdscript GDScript

    # filename: persistent_state.gd

    extends KinematicBody2D

    class_name PersistentState

    var state
    var state_factory

    var velocity = Vector2()

    func _ready():
      state_factory = StateFactory.new()
      change_state("idle")

    # Input code was placed here for tutorial purposes.
    func _process(delta):
      if Input.is_action_pressed("ui_left"):
        move_left()
      elif Input.is_action_pressed("ui_right"):
        move_right()

    func move_left():
      state.move_left()

    func move_right():
      state.move_right()

    func change_state(new_state_name):
      state.queue_free()
      state = state_factory.get_state(new_state_name).new()
      state.setup(funcref(self, "change_state"), $AnimatedSprite, self, velocity)
      state.name = "current_state"
      add_child(state)

.. note:: 
  The ''persisent_state.gd'' script contains code for detecting input. This was to make the tutorial simple, but it is not usually 
  best practice to do this.

Project-Setup
-------------

This tutorial made an assumption that the node it would be attached to contained a child node which is an :ref:'AnimatedSprite <class_AnimatedSprite>'. 
There is also the assumption that this ''AnimatedSprite'' has at least two animations, the idle and run animations. Also, the top-level node
is assumed to be a :ref:'KinematicBody2D <class_KinematicBody2D>'.

.. image:: img/llama_run.gif

.. note:: The zip file of the llama used in this tutorial is :download:'here <files/llama.zip>' and
  the source was from 'piskel_llama <https://www.piskelapp.com/p/agxzfnBpc2tlbC1hcHByEwsSBlBpc2tlbBiAgICfx5ygCQw/edit>'_
  I couldn't find the original creator information on that page though...
  There is also a good tutorial for sprite animation already. See :ref:'2D Sprite Animation <doc_2d_sprite_animation>'.

So, the only script that must be attached is 'persisent_state.gd', which  should be attached to the top node of the
player, which is a ''KinematicBody2D''.

.. image:: img/state_design_node_setup.png

.. image:: img/state_design_complete.gif

Now the player has utilized the state design pattern to implement its two different states. The nice part of this
pattern is that if one wanted to add another state, then it would invlove creating another class that need only
focus on itself and how it changes to another state. Each state is functionally separated and instantiated dynamically.

