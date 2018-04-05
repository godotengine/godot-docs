.. _doc_fps_tutorial_part_one:

Part 1
======

Tutorial introduction
---------------------

.. image:: img/FinishedTutorialPicture.png

This tutorial series will show you how to make a single player FPS game.

Throughout the course of these tutorials, we will cover how:

- To make a first person character, with sprinting and a flash light.
- To make a simple animation state machine for handling animation transitions.
- To add a pistol, rifle, and knife to the first person character.
- To add ammo and reloading to weapons that consume ammo.
- To add sounds that play when the guns fire.

.. note:: While this tutorial can be completed by beginners, it is highly
          advised to complete :ref:`doc_your_first_game`,
          if you are new to Godot and/or game development **before** going through
          this tutorial series.

          Remember: Making 3D games is much harder than making 2D games. If you do not know
          how to make 2D games you will likely struggle making 3D games.

          This tutorial assumes you know have experience working with the Godot editor,
          have basic programming experience in GDScript, and have basic experience in game development.

You can find the start assets for this parts 1 through 3 here: :download:`Godot_FPS_Starter.zip <files/Godot_FPS_Starter.zip>`

.. warning:: A video version of this tutorial series is coming soon!

The provided starter assets contain a animated 3D model, a bunch of 3D models for making levels,
and a few scenes already configured for this tutorial.

All assets provided are created by me (TwistedTwigleg) unless otherwise noted, and are
released under the ``MIT`` license.

.. note:: The skybox is created by **StumpyStrust** on OpenGameArt. The skybox used is
          licensed under ``CC0``.

          The font used is **Titillium-Regular**, and is licensed under the ``SIL Open Font License, Version 1.1``.

.. note:: You can find the finished project for parts 1 through 3 at the bottom of
          :ref:`doc_fps_tutorial_part_three`.

Part Overview
-------------

In this part we will be making a first person player that can move around
the environment.

.. image:: img/PartOneFinished.png

By the end of this part you will have a working first person character with a
mouse based camera that can walk, jump, and sprint around the game environment in
any direction

Getting everything setup
------------------------
Launch Godot and open up the project included in the starter assets.

.. note:: While these assets are not necessarily required to use the scripts provided in this tutorial,
          they will make the tutorial much easier to follow as there are several pre-setup scenes we
          will be using throughout the tutorial series.

First, go open the project settings and go to the "Input Map" tab. You'll find several
actions have already been defined. We will be using these actions for our player.
Feel free to change the keys bound to these actions if you want.

While we still have the project settings open, quickly go check if MSAA (MultiSample Anti-Aliasing)
is turned off. We want to make sure MSAA is off because otherwise we will get strange red lines
between the tiles in our level later.

.. tip:: The reason we get those red lines is because we are using lowpoly models
        with low resolution textures. MSAA tries to reduce jagged edges between models and
        because we are using lowpoly and low resolution textures in this project,
        we need to turn it off to avoid texture bleeding.

        A bonus with turning off MSAA is we get a more 'retro' looking result.

_________

Lets take a second to see what we have in the starter assets.

Included in the starter assets are five scenes: ``BulletScene.tscn``, ``Player.tscn``,
``SimpleAudioPlayer.tscn``, ``TestingArea.tscn``, and ``TestLevel.tscn``.

We will visit all of these scenes later, but for now open up ``Player.tscn``.

.. note:: There are a bunch of scenes and a few textures in the ``Assets`` folder. You can look at these if you want,
          but we will not be directly using them in this tutorial.

Making the FPS movement logic
-----------------------------

Once you have ``Player.tscn`` open, let's take a quick look at how it is setup

.. image:: img/PlayerSceneTree.png

First, notice how the player's collision shapes are setup. Using a vertical pointing
capsule as the collision shape for the player is fairly common in most first person games.

We are adding a small square to the 'feet' of the player so the player does not
feel like they are balancing on a single point.

.. note:: Many times player will notice how the collision shape being circular when
          they walk to an edge and slide off. We are adding the small square at the
          bottom of the capsule to reduce sliding on, and around, edges.

Another thing to notice is how many nodes are children of ``Rotation_helper``. This is because
``Rotation_helper`` contains all of the nodes we want to rotate on the ``X`` axis (up and down).
The reason behind this is so we rotate ``Player`` on the ``Y`` axis, and ``Rotation_helper`` on
the ``X`` axis.

.. note:: If we did not use ``Rotation_helper`` then we'd likely have cases where we are rotating
          both the ``X`` and ``Y`` axes at the same time. This can lead to undesirable results, as we then
          could rotate on all three axes in some cases.

_________

Attach a new script to the ``Player`` node and call it ``Player.gd``.

Lets program our player by adding the ability to move around, look around with the mouse, and jump.
Add the following code to ``Player.gd``:

::

    extends KinematicBody

    const norm_grav = -24.8
    var vel = Vector3()
    const MAX_SPEED = 20
    const JUMP_SPEED = 18
    const ACCEL = 3.5

    const DEACCEL= 16
    const MAX_SLOPE_ANGLE = 40

    var camera
    var camera_holder

    # You may need to adjust depending on the sensitivity of your mouse
    const MOUSE_SENSITIVITY = 0.05

    var flashlight

    func _ready():
        camera = $Rotation_helper/Camera
        camera_holder = $Rotation_helper
        
        Input.set_mouse_mode(Input.MOUSE_MODE_CAPTURED)
        
        flashlight = $Rotation_helper/Flashlight

    func _physics_process(delta):
        var dir = Vector3()
        var cam_xform = camera.get_global_transform()

        if Input.is_action_pressed("movement_forward"):
            dir += -cam_xform.basis.z.normalized()
        if Input.is_action_pressed("movement_backward"):
            dir += cam_xform.basis.z.normalized()
        if Input.is_action_pressed("movement_left"):
            dir += -cam_xform.basis.x.normalized()
        if Input.is_action_pressed("movement_right"):
            dir += cam_xform.basis.x.normalized()

        if is_on_floor():
            if Input.is_action_just_pressed("movement_jump"):
                vel.y = JUMP_SPEED

        if Input.is_action_just_pressed("flashlight"):
    		if flashlight.is_visible_in_tree():
    			flashlight.hide()
    		else:
    			flashlight.show()

        dir.y = 0
        dir = dir.normalized()

        var grav = norm_grav
        vel.y += delta*grav

        var hvel = vel
        hvel.y = 0

        var target = dir
        target *= MAX_SPEED

        var accel
        if dir.dot(hvel) > 0:
            accel = ACCEL
        else:
            accel = DEACCEL

        hvel = hvel.linear_interpolate(target, accel*delta)
        vel.x = hvel.x
        vel.z = hvel.z
        vel = move_and_slide(vel,Vector3(0,1,0), 0.05, 4, deg2rad(MAX_SLOPE_ANGLE))

        # (optional, but highly useful) Capturing/Freeing the cursor
        if Input.is_action_just_pressed("ui_cancel"):
            if Input.get_mouse_mode() == Input.MOUSE_MODE_VISIBLE:
                Input.set_mouse_mode(Input.MOUSE_MODE_CAPTURED)
            else:
                Input.set_mouse_mode(Input.MOUSE_MODE_VISIBLE)

    func _input(event):
        if event is InputEventMouseMotion && Input.get_mouse_mode() == Input.MOUSE_MODE_CAPTURED:
            camera_holder.rotate_x(deg2rad(event.relative.y * MOUSE_SENSITIVITY))
            self.rotate_y(deg2rad(event.relative.x * MOUSE_SENSITIVITY * -1))

            var camera_rot = camera_holder.rotation_degrees
            camera_rot.x = clamp(camera_rot.x, -70, 70)
            camera_holder.rotation_degrees = camera_rot

This is a lot of code, so let's break it down from top to bottom:

_________

First, we define some global variables to dictate how our player will move about the world.

.. note:: Throughout this tutorial, *variables defined outside functions will be
          referred to as "global variables"*. This is because we can access any of these
          variables from any place in the script. We can "globally" access them, hence the
          name.

Lets go through each of the global variables:

- ``norm_grav``: How strong gravity pulls us down while we are walking.
- ``vel``: Our :ref:`KinematicBody <class_KinematicBody>`'s velocity.
- ``MAX_SPEED``: The fastest speed we can reach. Once we hit this speed, we will not go any faster.
- ``JUMP_SPEED``: How high we can jump.
- ``ACCEL``: How fast we accelerate. The higher the value, the faster we get to max speed.
- ``DEACCEL``: How fast we are going to decelerate. The higher the value, the faster we will come to a complete stop.
- ``MAX_SLOPE_ANGLE``: The steepest angle we can climb.
- ``camera``: The :ref:`Camera <class_Camera>` node.
- ``rotation_helper``: A :ref:`Spatial <class_Spatial>` node holding everything we want to rotate on the X axis (up and down).
- ``MOUSE_SENSITIVITY``: How sensitive the mouse is. I find a value of ``0.05`` works well for my mouse, but you may need to change it based on how sensitive your mouse is.
- ``flashlight``: A :ref:`Spotlight <class_Spotlight>` node that will act as our player's flashlight.

You can tweak many of these variables to get different results. For example, by lowering ``normal_gravity`` and/or
increasing ``JUMP_SPEED`` you can get a more 'floaty' feeling character.
Feel free to experiment!

_________

Now lets look at the ``_ready`` function:

First we get the ``camera`` and ``rotation_helper`` nodes and store them into their variables.
Then we need to set the mouse mode to captured.

This will hide the mouse and keep it at the center of the screen. We do this for two reasons:
The first reason being we do not want to the player to see their mouse cursor as they play.
The second reason is because we do not want the cursor to leave the game window. If the cursor leaves
the game window there could be instances where the player clicks outside the window, and then the game
would lose focus. To assure neither of these issues happen, we capture the mouse cursor.

.. note:: see :ref:`Input documentation <class_Input>` for the various mouse modes. We will only be using
          ``MOUSE_MODE_CAPTURED`` and ``MOUSE_MODE_VISIBLE`` in this tutorial series.

We need to use ``_input`` so we can rotate the player and
camera when there is mouse motion.

_________

Next is ``_physics_process``:

We define a directional vector (``dir``) for storing the direction the player intends to move.

Next we get the camera's global transform and store it as well, into the ``cam_xform`` variable.

Now we check for directional input. If we find that the player is moving, we get the ``camera``'s directional
vector in the direction we are wanting to move towards and add (or subtract) it to ``dir``.

Many have found directional vectors confusing, so lets take a second to explain how they work:

_________

World space can be defined as: The space in which all objects are placed in, relative to a constant origin point.
Every object, no matter if it is 2D or 3D, has a position in world space.

To put it another way: world space is the space in a universe where every object's position, rotation, and scale
can be measured by a known, fixed point called the origin.

In Godot, the origin is at position ``(0, 0, 0)`` with a rotation of ``(0, 0, 0)`` and a scale of ``(1, 1, 1)``.

.. note:: When you open up the Godot editor and select a :ref:`Spatial <class_Spatial>` based node, a gizmo pops up.
          Each of the arrows points using world space directions by default.

If you want to move using the world space directional vectors, you'd do something like this:

::

    if Input.is_action_pressed("movement_forward"):
        node.translate(Vector3(0, 0, 1))
    if Input.is_action_pressed("movement_backward"):
        node.translate(Vector3(0, 0, -1))
    if Input.is_action_pressed("movement_left"):
        node.translate(Vector3(1, 0, 0))
    if Input.is_action_pressed("movement_right"):
        node.translate(Vector3(-1, 0, 0))

.. note:: Notice how we do not need to do any calculations to get world space directional vectors.
          We can just define a few :ref:`Vector3 <class_Vector3>` variables and input the values pointing in each direction.

Here is what world space looks like in 2D:

.. note:: The following images are just examples. Each arrow/rectangle represents a directional vector

.. image:: img/WorldSpaceExample.png

And here is what it looks like for 3D:

.. image:: img/WorldSpaceExample_3D.png

Notice how in both examples, the rotation of the node does not change the directional arrows.
This is because world space is a constant. No matter how you translate, rotate, or scale an object, world
space will *always point in the same direction*.

Local space is different, because it takes the rotation of the object into account.

Local space can be defined as follows:
The space in which a object's position is the origin of the universe. Because the position
of the origin can be at ``N`` many locations, the values derived from local space change
with the position of the origin.

.. note:: This stack overflow question has a much better explanation of world space and local space.

          https://gamedev.stackexchange.com/questions/65783/what-are-world-space-and-eye-space-in-game-development
          (Local space and eye space are essentially the same thing in this context)

To get a :ref:`Spatial <class_Spatial>` node's local space, we need to get its :ref:`Transform <class_Transform>`, so then we
can get the :ref:`Basis <class_Basis>` from the :ref:`Transform <class_Transform>`.

Each :ref:`Basis <class_Basis>` has three vectors: ``X``, ``Y``, and ``Z``.
Each of those vectors point towards each of the local space vectors coming from that object.

To use the a :ref:`Spatial <class_Spatial>` node's local directional vectors, we use this code:

::

    if Input.is_action_pressed("movement_forward"):
        node.translate(node.global_transform.basis.z.normalized())
    if Input.is_action_pressed("movement_backward"):
        node.translate(-node.global_transform.basis.z.normalized())
    if Input.is_action_pressed("movement_left"):
        node.translate(node.global_transform.basis.x.normalized())
    if Input.is_action_pressed("movement_right"):
        node.translate(-node.global_transform.basis.x.normalized())

Here is what local space looks like in 2D:

.. image:: img/LocalSpaceExample.png

And here is what it looks like for 3D:

.. image:: img/LocalSpaceExample_3D.png

Here is what the :ref:`Spatial <class_Spatial>` gizmo shows when you are using local space mode.
Notice how the arrows follow the rotation of the object on the left, which looks exactly
the same as the 3D example for local space.

.. note:: You can change between local and world space modes by pressing the little cube button
          when you have a :ref:`Spatial <class_Spatial>` based node selected.

.. image:: img/LocalSpaceExampleGizmo.png

Local vectors are confusing even for more experienced game developers, so do not worry if this all doesn't make a
lot of sense. The key thing to remember about local vectors is that we are using local coordinates to get direction
from the object's point of view, as opposed to using world vectors which give direction from the world's point of view.

_________

Back to ``_physics_process``:

When the player pressed any of the directional movement actions, we get the local vector pointing in that direction
and add it to ``dir``.

.. note:: Because the camera is rotated by ``-180`` degrees, we have to flip the directional vectors.
          Normally forward would be the positive Z axis, so using ``basis.z.normalized()`` would work,
          but we are using ``-basis.z.normalized()`` because our camera's Z axis faces backwards in relation
          to the rest of the player.

Next we check if the player is on the floor using :ref:`KinematicBody <class_KinematicBody>`'s ``is_on_floor`` function. If it is, then we
check to see if the "movement_jump" action has just been pressed. If it has, then we set our ``Y`` velocity to
``JUMP_SPEED``.

Next we check if the flash light action was just pressed. If it was, we then check if the flash light
is visible, or hidden. If it is visible, we hide it. If it is hidden, we make it visible.

Next we assure that our movement vector does not have any movement on the ``Y`` axis, and then we normalize it.
We set a variable to our normal gravity and apply that gravity to our velocity.

After that we assign our velocity to a new variable (called ``hvel``) and remove any movement on the ``Y`` axis.
Next we set a new variable (``target``) to our direction vector. Then we multiply that by our max speed
so we know how far we will can move in the direction provided by ``dir``.

After that we make a new variable for our acceleration, named ``accel``. We then take the dot product
of ``hvel`` to see if we are moving according to ``hvel``. Remember, ``hvel`` does not have any
``Y`` velocity, meaning we are only checking if we are moving forwards, backwards, left, or right.
If we are moving, then we set ``accel`` to our ``ACCEL`` constant so we accelerate, otherwise we set ``accel` to
our ``DEACCEL`` constant so we decelerate.

Finally, we interpolate our horizontal velocity, set our ``X`` and ``Z`` velocity to the interpolated horizontal velocity,
and then call ``move_and_slide`` to let the :ref:`KinematicBody <class_KinematicBody>` handle moving through the physics world.

.. tip:: All of the code in ``_physics_process`` is almost exactly the same as the movement code from the Kinematic Character demo!
         The only thing that is different is how we use the directional vectors, and the flash light!

You can optionally add some code to capture and free the mouse cursor when "ui_cancel" is
pressed. While entirely optional, it is highly recommended for debugging purposes.

_________

The final function we have is the ``_input`` function, and thankfully it's fairly short:

First we make sure that the event we are dealing with is a :ref:`InputEventMouseMotion <class_InputEventMouseMotion>` event.
We also want to check if the cursor is captured, as we do not want to rotate if it is not.

.. tip:: See :ref:`Mouse and input coordinates <doc_mouse_and_input_coordinates>` for a list of
         possible input events.

If the event is indeed a mouse motion event and the cursor is captured, we rotate
based on the mouse motion provided by :ref:`InputEventMouseMotion <class_InputEventMouseMotion>`.

First we rotate the ``rotation_helper`` node on the ``X`` axis, using the relative mouse motion's
``Y`` value, provided by :ref:`InputEventMouseMotion <class_InputEventMouseMotion>`.

Then we rotate the entire :ref:`KinematicBody <class_KinematicBody>` on the ``Y`` axis by the relative mouse motion's ``X`` value.

.. tip:: Godot converts relative mouse motion into a :ref:`Vector2 <class_Vector2>` where mouse movement going
         up and down is ``1`` and ``-1`` respectively. Right and Left movement is
         ``1`` and ``-1`` respectively.

         Because of how we are rotating the player, we multiply the relative mouse motion's
         ``X`` value by ``-1`` so mouse motion going left and right rotates the player left and right
         in the same direction.

Finally, we clamp the ``rotation_helper``'s ``X`` rotation to be between ``-70`` and ``70``
degrees so we cannot rotate ourselves upside down.

_________

To test the code open up the scene named ``Testing_Area.tscn`` if it's not already opened up. We will be using
this scene as we go through the tutorial, so be sure to keep it open in one of your scene tabs.

Go ahead and test your code either by pressing ``F4`` with ``Testing_Area.tscn`` as the open tab, by pressing the
play button in the top right corner, or by pressing ``F6``.
You should now be able to walk around, jump in the air, and look around using the mouse.

Giving the player the option to sprint
--------------------------------------

Before we get to making the weapons work, there is one more thing we should add.
Many FPS games have an option to sprint, and we can easily add sprinting to our player,
so let's do that!

First we need a few more global variables in our player script:

::

    const MAX_SPRINT_SPEED = 30
    const SPRINT_ACCEL = 18
    var is_sprinting = false

All of these variables work exactly the same as the non sprinting variables with
similar names. The only that's different is ``is_sprinting``, which is a boolean to track
whether the player is currently sprinting.

Now we just need to change some of the code in our ``_physics_process`` function
so we can add the ability to sprint.

The first thing we need to do is add the following code, preferably by the other input related code:

::

    if Input.is_action_pressed("movement_sprint"):
        is_sprinting = true
    else:
        is_sprinting = false;


This will set ``is_sprinting`` to true when we are holding down the ``movement_sprint`` action, and false
when the ``movement_sprint`` action is released.

Next we need to set our max speed to the higher speed if we are sprinting, and we also need
to change our acceleration to the new acceleration:

::

    var target = dir
    # NEW CODE. Replaces "target *= MAX_SPEED"
    if is_sprinting:
        target *= MAX_SPRINT_SPEED
    else:
        target *= MAX_SPEED

    # Same code as before:
    var accel
    if dir.dot(hvel) > 0:
        # New code. Replaces "accel = ACCEL"
        if is_sprinting:
            accel = SPRINT_ACCEL
        else:
            accel = ACCEL
    else:
        accel = DEACCEL

Now you should be able to sprint if you press the shift button! Go give it a
whirl! You can change the sprint related global variables to make the player faster when sprinting!

Phew! That was a lot of work. Now you have a fully working first person character!

In :ref:`doc_fps_tutorial_part_two` we will add some guns to our player character.

.. note:: At this point we've recreated the Kinematic character demo with sprinting!

.. tip:: Currently the player script would be at an ideal state for making all sorts of
         first person games. For example: Horror games, platformer games, adventure games, and more!

.. warning:: If you ever get lost, be sure to read over the code again! You can also
             download the finished project at the bottom of :ref:`doc_fps_tutorial_part_three`.
