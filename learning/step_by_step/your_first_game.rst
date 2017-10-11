.. _doc_your_first_game:

Your First Game
===============

Overview
--------

This tutorial will guide you through making your first Godot Engine
project. You will learn how the Godot Engine editor works, how to structure
a project, and how to build a 2D game.

.. note:: This project is an introduction to the Godot Engine. It 
          assumes that you have some programming experience already. If 
          you're new to programming entirely, you should start here:
          :ref:`doc_scripting`.

The game is called *"Dodge the Creeps"*. Your character must move and
avoid the enemies for as long as possible. Here is a preview of the
final result:

.. image:: /img/dodge_preview.gif

**Why 2D?** 
    3D games are much more complex than 2D ones. You should stick to 2D 
    until you have a good understanding of the game development process.

Project Setup
-------------

Launch Godot and create a new project. Then, download
:download:`dodge_assets.zip </files/dodge_assets.zip>` - the images and sounds you'll be
using to make the game. Unzip these files in your new project folder.

.. note:: For this tutorial, we will assume you are already familiar with the
          Godot Engine editor. If you haven't read :ref:`doc_scenes_and_nodes`, do so now
          for an explanation of setting up a project and using the editor.

This game will use "portrait" mode, so we need to adjust the size of the
game window. Click on Project -> Project Settings -> Display -> Window and
set ``Width`` to ``480`` and ``Height`` to ``720``.

Organizing the Project
~~~~~~~~~~~~~~~~~~~~~~

In this project, we will make 3 independent scenes: ``Player``,
``Mob``, and ``HUD``, which we will combine into the game's ``Main``
scene. In a larger project, it might be useful to make folders to hold
the various scenes and their scripts, but for this relatively small
game, you can save your scenes and scripts in the root folder, which is
referred to as ``res://``.  You can see your project folders in the Filesystem 
Dock in the upper left corner:

.. image:: /img/filesystem_dock.png

Player Scene
------------

The first scene we make defines the "Player" object. One of the benefits
of creating a separate Player scene is that we can test it separately, even
before we've created the other parts of the game.

Node Structure
~~~~~~~~~~~~~~

To begin, click the "Add/Create a New Node" button and add an :ref:`Area2D <class_Area2D>`
node to the scene.

.. image:: /img/add_node.png

With ``Area2D`` we can detect other objects that overlap or run into the player. 
Change its name to ``Player``. This is the scene's "root" or top-level node. 
We can add additional nodes to the player to add functionality.

Save the scene (click Scene -> Save, or press ``Meta-s``).

.. note:: In this project, we will be following the Godot Engine naming 
          conventions. Classes (Nodes) use ``CapWords``, variables and 
          functions use ``snake_case``, and constants use ``ALL_CAPS``.

Sprite Animation
~~~~~~~~~~~~~~~~

Click on the ``Player`` node and add an :ref:`AnimatedSprite <class_AnimatedSprite>` node as a
child. The ``AnimatedSprite`` will handle the appearance and animations
for our player. Notice that there is a warning symbol next to the node.
An ``AnimatedSprite`` requires a :ref:`SpriteFrames <class_SpriteFrames>` resource, which is a
list of the animation(s) it can display. To create one, find the
``Frames`` property in the Inspector and click "<null>" ->
"New SpriteFrames". Next, in the same location, click
``<SpriteFrames>`` to open the "SpriteFrames" panel:

.. image:: /img/spriteframes_panel.png


On the left is a list of animations. Click the "default" one and rename
it to "right". Then click the "Add" button to create a second animation
named "up". Drag the two images for each animation into "Animation
Frames" side of the panel:

.. image:: /img/spriteframes_panel2.png


Finally, add a :ref:`CollisionShape2D <class_CollisionShape2D>` as a child 
of the ``Player``. This will determine the player's "hitbox", or the 
bounds of its collision area.  For this character, a ``CapsuleShape2D`` 
gives the best fit, so next to "Shape" in the Inspector, click 
"<null>"" -> "New CapsuleShape2D".  Resize the shape to cover the sprite:

.. image:: /img/player_coll_shape.png

.. warning:: Remember not to scale the shape's outline! Only use the
             size handles (red) to adjust the shape!

When you're finished, your ``Player`` scene should look like this:

.. image:: /img/player_scene_nodes.png

Moving the Player
~~~~~~~~~~~~~~~~~

Now we need to add some functionality that we can't get from a built-in
node, so we'll add a script. Click the ``Player`` node and click the
"Add Script" button:

.. image:: /img/add_script_button.png

In the script settings window, you can leave the default settings, just
click "Create": 

.. image:: /img/attach_node_window.png

.. note:: If this is your first time encountering GDScript please read
          :ref:`doc_scripting` first.

Start by declaring the member variables this object will need:

::

    extends Area2D

    var SPEED = 400  # how fast the player will move (pixels/sec)
    var velocity = Vector2()  # the player's movement vector
    var screensize  # size of the game window

The ``_ready()`` function is called when a node enters the scene tree, so 
that's a good time to find the size of the game window:

::

    func _ready():
        screensize = get_viewport_rect().size

Now we can use the ``_process()`` function to define what the player will do.
The ``_process()`` function is called on every frame, so we'll use it to update
elements of our game which we expect to be changing often. Here we'll have it:

- check for input 
- move in the given direction 
- play the appropriate animation.

First, we need to check the inputs - is the player pressing a key? For
this game, we have 4 direction inputs to check. Input actions are defined 
in the Project Settings under "Input Map". You can define custom events and 
assign different keys, mouse events, or other inputs to them. For this demo, 
we will use the default events that are assigned to the arrow keys on the 
keyboard.

You can detect whether a key is pressed using
``Input.is_action_pressed()``, which returns ``true`` if it is pressed
or ``false`` if it isn't.

::

    func _process(delta):
        velocity = Vector2()
        if Input.is_action_pressed("ui_right"):
            velocity.x += 1
        if Input.is_action_pressed("ui_left"):
            velocity.x -= 1
        if Input.is_action_pressed("ui_down"):
            velocity.y += 1
        if Input.is_action_pressed("ui_up"):
            velocity.y -= 1
        if velocity.length() > 0:
            velocity = velocity.normalized() * SPEED
            $AnimatedSprite.play()
        else:
            $AnimatedSprite.stop()

We check each input and add/subtract from the ``velocity`` to obtain a
total direction. For example, if you hold ``right`` and ``down`` at
the same time, the resulting ``velocity`` vector will be ``(1, 1)``. In
this case, since we're adding a horizontal and a vertical movement, the
player would move *faster* than if it just moved horizontally.

We can prevent that if we *normalize* the velocity, which means we set
its *length* to ``1``, and multiply by the desired speed. This means no
more fast diagonal movement.

.. tip:: If you've never used vector math before (or just need a refresher)
         you can see an explanation of vector usage in Godot at :ref:`doc_vector_math`.
         It's good to know but won't be necessary for the rest of this tutorial.

We also check whether the player is moving so we can start or stop the
AnimatedSprite animation.

Now that we have a movement direction, we can update the player's position
and use ``clamp()`` to prevent it from leaving the screen:

::

        position += velocity * delta
        position.x = clamp(position.x, 0, screensize.x)
        position.y = clamp(position.y, 0, screensize.y)

    
.. tip:: *Clamping* a value means restricting it to a given minimum/maximum range.

Click "Play the Edited Scene. (F6)" and confirm you can move the player
around the screen in all directions.

Choosing Animations
~~~~~~~~~~~~~~~~~~~

Now that the player can move, we need to change which animation the
AnimatedSprite is playing based on direction. We have a "right"
animation, which should be flipped horizontally (using the ``flip_h``
property) for left movement, and an "up" animation, which should be
flipped vertically (``flip_v``) for downward movement.
Let's place this code at the end of our ``_process()`` function:

::

        if velocity.x != 0:
            $AnimatedSprite.animation = "right"
            $AnimatedSprite.flip_v = false
            $AnimatedSprite.flip_h = velocity.x < 0
        elif velocity.y != 0:
            $AnimatedSprite.animation = "up"
            $AnimatedSprite.flip_v = velocity.y > 0

Play the scene again and check that the animations are correct in each
of the directions.

Preparing for Collisions
~~~~~~~~~~~~~~~~~~~~~~~~

We want the player to detect when it is hit by an enemy, but we haven't
made any enemies yet! That's OK because we're going to use Godot's
*signal* functionality to make it work.

Add the following at the top of the script (after ``extends Area2d``):

::

    signal hit

This defines a custom signal called "hit" that we will have our player
emit (send out) when it collides with an enemy. We will use the Area2D to 
detect the collision. Select the ``Player`` node and click the "Node" tab 
next to the Inspector to see the list of signals the player can emit:

.. image:: /img/player_signals.png

Notice our custom "hit" signal is there as well! Since our enemies are
going to be ``RigidBody2D`` nodes, we want the
``body_entered( Object body )`` signal - that will be emitted when a
body contacts the player. Click "Connect.." and then "Connect" again on
the "Connecting Signal" window - we don't need to change any of those
settings. Godot will automatically create a function called
``_on_Player_body_entered`` in your player's script.

.. tip:: When connecting a signal, instead of having Godot create a
         function for you, you can also give the name of an existing 
         function that you want to link the signal to.

Add this code to the function:

::

    func _on_Player_body_entered( area ):
        hide() # Player disappears after being hit
        emit_signal("hit")
        monitoring = false

.. warning:: Disabling the ``monitoring`` property of an ``Area2D`` means 
             it won't detect collisions. By turning it off, we make
             sure we don't trigger the ``hit`` signal more than once. However,
             changing the property in the midst of an ``area_entered`` signal 
             will result in an error, because the engine hasn't finished 
             processing the current frame yet.
    
Instead, you can *defer* the change, which will tell the game engine to
wait until it's safe to set monitoring to ``false``. Change the line to
this:

::

        call_deferred("set_monitoring", false)

The last piece for our player is to add a function we can call to reset
the player when starting a new game.

::

    func start(pos):
        position = pos
        show()
        monitoring = true

Enemy Scene
-----------

Now it's time to make the enemies our player will have to dodge. Their
behavior will not be very complex: mobs will spawn randomly at the edges
of the screen and move in a straight line (in a random direction), then
despawn when they go offscreen.

We will build this into a ``Mob`` scene, which we can then *instance* to
create any number of independent mobs in the game.

Node Setup
~~~~~~~~~~

Click Scene -> New Scene and we'll create the Mob!

The Mob scene will use the following nodes:

-  :ref:`RigidBody2D <class_RigidBody2D>` (named ``Mob``)

   -  :ref:`AnimatedSprite <class_AnimatedSprite>`
   -  :ref:`CollisionShape2D <class_CollisionShape2D>`
   -  :ref:`VisibilityNotifier2D <class_VisibilityNotifier2D>` (named ``Visibility``)

In the :ref:`RigidBody2D <class_RigidBody2D>` properties, set ``Gravity Scale`` to ``0`` (so
that the mob will not fall downward). In addition, under the
``PhysicsBody2D`` section of the Inspector, click the ``Mask`` property and
uncheck the first box. This will ensure that the mobs do not collide with each other.

.. image:: /img/set_collision_mask.png

Set up the :ref:`AnimatedSprite <class_AnimatedSprite>` like you did for the player.
This time, we have 3 animations: "fly", "swim", and "walk". Set the ``Playing``
property in the Inspector to "On" and adjust the "Speed (FPS)" setting as shown below.
We'll select one of these randomly so that the mobs will have some variety.

.. image:: /img/mob_animations.gif

As in the ``Player`` scene, add a ``CapsuleShape2D`` for the
collision and then save the scene.

Enemy Script
~~~~~~~~~~~~

Add a script to the ``Mob`` and add the following member variables:

::

    extends RigidBody2D

    var MIN_SPEED = 150  # minimum speed range
    var MAX_SPEED = 250  # maximum speed range
    var mob_types = ["walk", "swim", "fly"]

We'll pick a random value between ``MIN_SPEED`` and ``MAX_SPEED`` for
how fast each mob will move (it would be boring if they were all moving
at the same speed). We also have an array containing the names of the three
animations, which we'll use to select a random one.

Now let's look at the rest of the script. In ``_ready()`` we choose a
random one of the three animation types:

::

    func _ready():
        $AnimatedSprite.animation = mob_types[randi() % mob_types.size()]

.. note:: You must use ``randomize()`` if you want
          your sequence of "random" numbers to be different every time you run
          the scene. We're going to use ``randomize()`` in our ``Main`` scene,
          so we won't need it here. ``randi() % n`` is the standard way to get
          a random integer between ``0`` and ``n-1``.

The last piece is to make the mobs delete themselves when they leave the
screen. Connect the ``screen_exited()`` signal of the ``Visibility``
node and add this code:

::

    func _on_Visible_screen_exited():
        queue_free()
        
That completes the `Mob` scene. 

Main Scene
----------

Now it's time to bring it all together. Create a new scene and add a
:ref:`Node <class_Node>` named ``Main``. Click the "Instance" button and select your
saved ``Player.tscn``.

.. image:: /img/instance_scene.png

.. note:: See :ref:`doc_instancing` to learn more about instancing.

Now add the following nodes as children of ``Main``, and name them as
shown (values are in seconds):

-  :ref:`Timer <class_Timer>` (named ``MobTimer``) - to control how often mobs spawn
-  :ref:`Timer <class_Timer>` (named ``ScoreTimer``) - to increment the score every second
-  :ref:`Timer <class_Timer>` (named ``StartTimer``) - to give a delay before starting
-  :ref:`Position2D <class_Position2D>` (named ``StartPosition``) - to indicate the player's start position

Set the ``Wait Time`` property of each of the ``Timer`` nodes as
follows:

-  ``MobTimer``: ``0.5``
-  ``ScoreTimer``: ``1``
-  ``StartTimer``: ``2``

In addition, set the ``One Shot`` property of ``StartTimer`` to "On" and
set ``Position`` of the ``StartPosition`` node to ``(240, 450)``.

Spawning Mobs
~~~~~~~~~~~~~

The Main node will be spawning new mobs, and we want them to appear at a
random location on the edge of the screen. Add a :ref:`Path2D <class_Path2D>` named
``MobPath`` as a child of ``Main``. When you select the ``Path2D`` node
you will see some new buttons appear at the top of the editor:

.. image:: /img/path2d_buttons.png

Select the middle one ("Add Point") and draw the path by clicking to add
the points shown. To have the points snap to the grid, make sure "Use Snap" is
checked. This option can be found under the "Edit" button to the left of the Path2D buttons.

.. image:: /img/draw_path2d.png

.. important:: Draw the path in *clockwise* order, or your mobs will spawn 
               pointing *outwards* instead of *inwards*!

Now that the path is defined, add a :ref:`PathFollow2D <class_PathFollow2D>` 
node as a child of ``MobPath`` and name it ``MobSpawnLocation``. This node will
automatically rotate and follow the path you've drawn, so we can use it
to select a random position and direction along the path.

Main Script
~~~~~~~~~~~

Add a script to ``Main``. At the top of the script we use
``export (PackedScene)`` to allow us to choose the Mob scene we want to
instance.

::

    extends Node

    export (PackedScene) var Mob
    var score

    func _ready():
        randomize()

Using ``export`` lets you set the value of a variable in the Inspector
like so:

.. image:: /img/load_mob_scene.png

Click on "<null>"" and choose "Load", then select ``Mob.tscn``.

Next, click on the Player and connect the ``hit`` signal to the
``game_over`` function, which will handle what needs to happen when a
game ends. We will also have a ``new_game`` function to set everything
up for a new game:

::

    func new_game():
        score = 0
        $Player.start($StartPosition.position)
        $StartTimer.start()

    func game_over():
        $ScoreTimer.stop()
        $MobTimer.stop()

Now connect the ``timeout()`` signal of each of the Timer nodes.
``StartTimer`` will start the other two timers. ``ScoreTimer`` will
increment the score by 1.

::

    func _on_StartTimer_timeout():
        $MobTimer.start()
        $ScoreTimer.start()

    func _on_ScoreTimer_timeout():
        score += 1

In ``_on_MobTimer_timeout()`` we will create a mob instance, pick a
random starting location along the ``Path2D``, and set the mob in
motion. The ``PathFollow2D`` node will automatically rotate as it
follows the path, so we will use that to select the mob's direction as 
well as its position.

Note that a new instance must be added to the scene using
``add_child()``.

::

    func _on_MobTimer_timeout():
        # choose a random location on the Path2D
        $"MobPath/MobSpawnLocation".set_offset(randi())
        # create a Mob instance and add it to the scene
        var mob = Mob.instance()
        add_child(mob)
        # choose a direction and position
        var direction = $"MobPath/MobSpawnLocation".rotation
        mob.position = $"MobPath/MobSpawnLocation".position
        # add some randomness to the direction
        direction += rand_range(-PI/4, PI/4)
        # textures are oriented pointing up, so add 90 degrees
        mob.rotation = direction + PI/2
        # choose the velocity
        mob.set_linear_velocity(Vector2(rand_range(mob.MIN_SPEED, mob.MAX_SPEED), 0).rotated(direction))

.. important:: In functions requiring angles, GDScript uses *radians*, 
               not degrees. If you're more comfortable working with 
               degrees, you'll need to use the ``deg2rad()`` and 
               ``rad2deg()`` functions to convert between the two measures.

HUD
---

The final piece our game needs is a UI: an interface to display things
like score, a "game over" message, and a restart button. Create a new
scene, and add a :ref:`CanvasLayer <class_CanvasLayer>` node named ``HUD`` ("HUD" stands for
"heads-up display", meaning an informational display that appears as an
overlay, on top of the game view).

The :ref:`CanvasLayer <class_CanvasLayer>` node lets us draw our UI elements on
the layer above the rest of the game so that the information it displays doesn't get
covered up by any game elements like the player or the mobs.

The HUD displays the following information:

-  Score, changed by ``ScoreTimer``
-  A message, such as "Game Over" or "Get Ready!"
-  A "Start" button to begin the game

The basic node for UI elements is :ref:`Control <class_Control>`. To create our UI,
we'll use two types of :ref:`Control <class_Control>` nodes: The :ref:`Label <class_Label>`
and the :ref:`Button <class_Button>`.

Create the following children of the ``HUD`` node:

-  :ref:`Label <class_Label>` (named ``ScoreLabel``)
-  :ref:`Label <class_Label>` (named ``MessageLabel``)
-  :ref:`Button <class_Button>` (named ``StartButton``)
-  :ref:`Timer <class_Timer>` (named ``MessageTimer``)

.. note:: **Anchors and Margins** ``Control`` nodes have a position and size,
          but they also have anchors and margins. Anchors define the
          origin, or the reference point for the edges of the node. Margins
          update automatically when you move or resize a control node. They
          represent the distance from the control node's edges to its anchor.
          See :ref:`doc_gui_tutorial` for more details.

Arrange the nodes as shown below. Click the "Anchor" button to
set a Control node's anchor:

.. image:: /img/ui_anchor.png

You can drag the nodes to place them manually, or for more precise
placement, use the following settings:

ScoreLabel
~~~~~~~~~~

-  ``Anchor``: "Center Top"
-  ``Margin``:

   -  Left: ``-240``
   -  Top: ``0``
   -  Right: ``240``
   -  Bottom: ``100``

-  Text: ``0``

MessageLabel
~~~~~~~~~~~~

-  ``Anchor``: "Center"
-  ``Margin``:

   -  Left: ``-240``
   -  Top: ``-260``
   -  Right: ``240``
   -  Bottom: ``60``

-  Text: ``Dodge the Creeps!``

StartButton
~~~~~~~~~~~

-  ``Anchor``: "Center"
-  ``Margin``:

   -  Left: ``-60``
   -  Top: ``70``
   -  Right: ``60``
   -  Bottom: ``150``

-  Text: ``Start``

The default font for ``Control`` nodes is very small and doesn't scale
well. There is a font file included in the game assets called
"Xolonium-Regular.ttf". To use this font, do the following for each of
the three ``Control`` nodes:

1. Under "Custom Fonts", choose "New DynamicFont" 

.. image:: /img/custom_font1.png

2. Click on the "DynamicFont" you just added, and under "Font Data",
   choose "Load" and select the "Xolonium-Regular.ttf" file. You must
   also set the font's ``Size``. A setting of ``64`` works well. 
   
.. image:: /img/custom_font2.png

Now add this script to the ``HUD``:

::

    extends CanvasLayer

    signal start_game

The ``start_game`` signal tells the ``Main`` node that the button
has been pressed.

::

    func show_message(text):
        $MessageLabel.text = text
        $MessageLabel.show()
        $MessageTimer.start()

This function is called when we want to display a message
temporarily, such as "Get Ready". On the ``MessageTimer``, set the
``Wait Time`` to ``2`` and check ``One Shot``.

::

    func show_game_over():
        show_message("Game Over")
        yield($MessageTimer, "timeout")
        $StartButton.show()
        $MessageLabel.text = "Dodge the\nCreeps!"
        $MessageLabel.show()

This function is called when the player loses. It will show "Game
Over" for 2 seconds, and then return to the game title and show the
"Start" button.

::

    func update_score(score):
        $ScoreLabel.text = str(score)

This function is called in ``Main`` whenever the score changes.

Connect the ``timout()`` signal of ``MessageTimer`` and the
``pressed()`` signal of ``StartButton``.

::

    func _on_StartButton_pressed():
        $StartButton.hide()
        emit_signal("start_game")

    func _on_MessageTimer_timeout():
        $MessageLabel.hide()

Connecting HUD to Main
~~~~~~~~~~~~~~~~~~~~~~

Now that we're done creating the ``HUD`` scene, save it and go back to ``Main``.
Instance the ``HUD`` scene in ``Main`` like you did the ``Player`` scene, and place it at the
bottom of tree. The full tree should look like this, so make sure you didn't miss anything!

.. image:: /img/completed_main_scene.png

Now we need to connect the ``HUD`` functionality to our ``Main`` script.
This requires a few additions to the ``Main`` scene:

In the Node tab, connect the HUD's ``start_game`` signal to the
``new_game()`` function.

In ``new_game()``, update the score display and show the "Get Ready"
message:

::

        $HUD.update_score(score)
        $HUD.show_message("Get Ready")

In ``game_over()`` we need to call the corresponding ``HUD`` function:

::

        $HUD.show_game_over()

Finally, add this to ``_on_ScoreTimer_timeout()`` to keep the display in
sync with the changing score:

::

        $HUD.update_score(score)

Finishing Up
------------

We've now completed all the functionality for our game. Below are some
remaining steps to add a bit more "juice" and improve the game
experience. Feel free to expand the gameplay with your own ideas.

Background
~~~~~~~~~~

The default gray background is not very appealing, so let's change its
color. One way to do this is to use a :ref:`ColorRect <class_ColorRect>` node. Make it the
first node under ``Main`` so that it will be drawn behind the other
nodes. ``ColorRect`` only has one property: ``Color``. Choose a color
you like and drag the size of the ``ColorRect`` so that it covers the
screen.

You can also add a background image, if you have one, by using a
``Sprite`` node.

Sound Effects
~~~~~~~~~~~~~

Sound and music can be the single most effective way to add appeal to
the game experience. In your game assets folder, you have two sound
files: "House In a Forest Loop.ogg", for background music, and
"gameover.wav" for when the player loses.

Add two :ref:`AudioStreamPlayer <class_AudioStreamPlayer>` nodes as children of ``Main``. Name one of
them ``Music`` and the other ``DeathSound``. On each one, click on the
``Stream`` property, select "Load" and choose the corresponding audio
file.

To play the music, add ``$Music.play()`` in the ``new_game()`` function
and ``$Music.stop()`` in the ``game_over()`` function.

Finally, add ``$DeathSound.play()`` in the ``game_over()`` function as
well.

Particles
~~~~~~~~~

For one last bit of visual appeal, let's add a trail effect to the
player's movement. Choose your ``Player`` scene and add a
:ref:`Particles2D <class_Particles2D>` node named ``Trail``.

There are a very large number of properties to choose from when
configuring particles. Feel free to experiment and create different
effects. For the effect in the example, use the following settings:

.. image:: /img/particle_trail_settings.png
   
You also need to create a ``Material`` by clicking on ``<null>`` and
then "New ParticlesMaterial". The settings for that are below:

.. image:: /img/particle_trail_settings2.png

.. seealso:: See :ref:`Particles2D <class_Particles2D>` for more details on using
             particle effects.

Project Files
-------------

You can find a completed version of this project here:
https://github.com/kidscancode/Godot3_dodge/releases
