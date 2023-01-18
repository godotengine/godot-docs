.. _doc_using_character_body_2d:

<<<<<<< HEAD
Using CharacterBody2D/3D
========================
=======
Using CharacterBody2D
=====================
>>>>>>> ecd1fe77e (Update development/compiling/compiling_for_windows.rst)

Introduction
------------

Godot offers several collision objects to provide both collision detection
and response. Trying to decide which one to use for your project can be confusing.
You can avoid problems and simplify development if you understand how each of them
works and what their pros and cons are. In this tutorial, we'll look at the
:ref:`CharacterBody2D <class_CharacterBody2D>` node and show some examples
of how to use it.

<<<<<<< HEAD
.. note:: While this document uses ``CharacterBody2D`` in its examples, the same
          concepts apply in 3D as well.
=======
.. note:: This document assumes you're familiar with Godot's various physics
          bodies. Please read :ref:`doc_physics_introduction` first.
>>>>>>> ecd1fe77e (Update development/compiling/compiling_for_windows.rst)

What is a character body?
-------------------------

``CharacterBody2D`` is for implementing bodies that are controlled via code.
Character bodies detect collisions with other bodies when moving, but are not affected by
engine physics properties, like gravity or friction. While this means that you
have to write some code to create their behavior, it also means you have more
precise control over how they move and react.

<<<<<<< HEAD
.. note:: This document assumes you're familiar with Godot's various physics
          bodies. Please read :ref:`doc_physics_introduction` first, for an overview
          of the physics options.

=======
>>>>>>> ecd1fe77e (Update development/compiling/compiling_for_windows.rst)
.. tip:: A `CharacterBody2D` can be affected by gravity and other forces,
        but you must calculate the movement in code. The physics engine will
        not move a `CharacterBody2D`.

Movement and collision
----------------------

When moving a ``CharacterBody2D``, you should not set its ``position`` property
directly. Instead, you use the ``move_and_collide()`` or ``move_and_slide()`` methods.
<<<<<<< HEAD
These methods move the body along a given vector and detect collisions.

.. warning:: You should handle physics body movement in the ``_physics_process()`` callback.
=======
These methods move the body along a given vector and instantly stop if
a collision is detected with another body. After a CharacterBody2D has collided,
any *collision response* must be coded manually.

.. warning:: You should only do Kinematic body movement in the ``_physics_process()`` callback.
>>>>>>> ecd1fe77e (Update development/compiling/compiling_for_windows.rst)

The two movement methods serve different purposes, and later in this tutorial, you'll
see examples of how they work.

<<<<<<< HEAD
move_and_collide
~~~~~~~~~~~~~~~~

This method takes one required parameter: a :ref:`Vector2 <class_Vector2>` indicating
the body's relative movement. Typically, this is your velocity vector multiplied by the
=======
``move_and_collide``
~~~~~~~~~~~~~~~~~~~~

This method takes one parameter: a :ref:`Vector2 <class_Vector2>` indicating the body's
relative movement. Typically, this is your velocity vector multiplied by the
>>>>>>> ecd1fe77e (Update development/compiling/compiling_for_windows.rst)
frame timestep (``delta``). If the engine detects a collision anywhere along
this vector, the body will immediately stop moving. If this happens, the
method will return a :ref:`KinematicCollision2D <class_KinematicCollision2D>` object.

``KinematicCollision2D`` is an object containing data about the collision
and the colliding object. Using this data, you can calculate your collision
response.

<<<<<<< HEAD
``move_and_collide`` is most useful when you just want to move the body and
detect collision, but don't need any automatic collision response. For example,
if you need a bullet that ricochets off a wall, you can directly change the angle
of the velocity when you detect a collision. See below for an example.

move_and_slide
~~~~~~~~~~~~~~
=======
``move_and_slide``
~~~~~~~~~~~~~~~~~~
>>>>>>> ecd1fe77e (Update development/compiling/compiling_for_windows.rst)

The ``move_and_slide()`` method is intended to simplify the collision
response in the common case where you want one body to slide along the other.
It is especially useful in platformers or top-down games, for example.

.. tip:: ``move_and_slide()`` automatically calculates frame-based movement
         using ``delta``. Do *not* multiply your velocity vector by ``delta``
         before passing it to ``move_and_slide()``.

<<<<<<< HEAD
When calling ``move_and_slide()``, the function uses a number of node properties
to calculate its slide behavior. These properties can be found in the Inspector,
or set in code.

- ``velocity`` - *default value:* ``Vector2( 0, 0 )``

    This property represents the body's velocity vector in pixels per second.
    ``move_and_slide()`` will modify this value automatically when colliding.

- ``motion_mode`` - *default value:* ``MOTION_MODE_GROUNDED``

    This property is typically used to distinguish between side-scrolling and
    top-down movement. When using the default value, you can use the ``is_on_floor()``,
    ``is_on_wall()``, and ``is_on_ceiling()`` methods to detect what type of
    surface the body is in contact with, and the body will interact with slopes.
    When using ``MOTION_MODE_FLOATING``, all collisions will be considered "walls".

- ``up_direction`` - *default value:* ``Vector2( 0, -1 )``

    This property allows you to define what surfaces the engine should consider
    being the floor. Its value lets you use the ``is_on_floor()``, ``is_on_wall()``,
    and ``is_on_ceiling()`` methods to detect what type of surface the body is
    in contact with. The default value means that the top side of horizontal surfaces
    will be considered "ground".

- ``floor_stop_on_slope`` - *default value:* ``true``

    This parameter prevents a body from sliding down slopes when standing still.

- ``wall_min_slide_angle`` - *default value:* ``0.261799`` (in radians, equivalent to ``15`` degrees)

    This is the minimum angle where the body is allowed to slide when it hits a
    slope.
=======
In addition to the velocity vector, ``move_and_slide()`` takes a number of
other parameters allowing you to customize the slide behavior:

- ``up_direction`` - *default value:* ``Vector2( 0, 0 )``

    This parameter allows you to define what surfaces the engine should consider
    being the floor. Setting this lets you use the ``is_on_floor()``, ``is_on_wall()``,
    and ``is_on_ceiling()`` methods to detect what type of surface the body is
    in contact with. The default value means that all surfaces are considered walls.

- ``stop_on_slope`` - *default value:* ``false``

    This parameter prevents a body from sliding down slopes when standing still.

- ``max_slides`` - *default value:* ``4``

    This parameter is the maximum number of collisions before the body stops moving. Setting
    it too low may prevent movement entirely.
>>>>>>> ecd1fe77e (Update development/compiling/compiling_for_windows.rst)

- ``floor_max_angle`` - *default value:* ``0.785398`` (in radians, equivalent to ``45`` degrees)

    This parameter is the maximum angle before a surface is no longer considered a "floor."

<<<<<<< HEAD
There are many other properties that can be used to modify the body's behavior under
specific circumstances. See the :ref:`CharacterBody2D <class_CharacterBody2D>` docs
for full details.
=======
- ``infinite_inertia`` - *default value:* ``true``

    When this parameter is ``true``, the body can push :ref:`RigidBody2D <class_RigidBody2D>`
    nodes, ignoring their mass, but won't detect collisions with them. If it's ``false``
    the body will collide with rigid bodies and stop.

``move_and_slide_with_snap``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This method adds some additional functionality to ``move_and_slide()`` by adding
the ``snap`` parameter. As long as this vector is in contact with the ground, the
body will remain attached to the surface. Note that this means you must disable
snapping when jumping, for example. You can do this either by setting ``snap``
to ``Vector2.ZERO`` or by using ``move_and_slide()`` instead.

>>>>>>> ecd1fe77e (Update development/compiling/compiling_for_windows.rst)

Detecting collisions
--------------------

When using ``move_and_collide()`` the function returns a ``KinematicCollision2D``
directly, and you can use this in your code.

When using ``move_and_slide()`` it's possible to have multiple collisions occur,
<<<<<<< HEAD
as the slide response is calculated. To process these collisions, use ``get_slide_collision_count()``
=======
as the slide response is calculated. To process these collisions, use ``get_slide_count()``
>>>>>>> ecd1fe77e (Update development/compiling/compiling_for_windows.rst)
and ``get_slide_collision()``:

.. tabs::
 .. code-tab:: gdscript GDScript

    # Using move_and_collide.
    var collision = move_and_collide(velocity * delta)
    if collision:
<<<<<<< HEAD
        print("I collided with ", collision.get_collider().name)

    # Using move_and_slide.
    move_and_slide()
    for i in get_slide_count():
        var collision = get_slide_collision(i)
        print("I collided with ", collision.get_collider().name)
=======
        print("I collided with ", collision.collider.name)

    # Using move_and_slide.
    velocity = move_and_slide(velocity)
    for i in get_slide_count():
        var collision = get_slide_collision(i)
        print("I collided with ", collision.collider.name)
>>>>>>> ecd1fe77e (Update development/compiling/compiling_for_windows.rst)

 .. code-tab:: csharp

    // Using MoveAndCollide.
<<<<<<< HEAD
    var collision = MoveAndCollide(Velocity * (float)delta);
    if (collision != null)
    {
        GD.Print("I collided with ", ((Node)collision.GetCollider()).Name);
    }

    // Using MoveAndSlide.
    MoveAndSlide();
    for (int i = 0; i < GetSlideCount(); i++)
    {
        var collision = GetSlideCollision(i);
        GD.Print("I collided with ", ((Node)collision.GetCollider()).Name);
    }

.. note:: `get_slide_collision_count()` only counts times the body has collided and changed direction.
=======
    var collision = MoveAndCollide(velocity * delta);
    if (collision != null)
    {
        GD.Print("I collided with ", ((Node)collision.Collider).Name);
    }

    // Using MoveAndSlide.
    velocity = MoveAndSlide(velocity);
    for (int i = 0; i < GetSlideCount(); i++)
    {
        var collision = GetSlideCollision(i);
        GD.Print("I collided with ", ((Node)collision.Collider).Name);
    }

.. note:: `get_slide_count()` only counts times the body has collided and changed direction.
>>>>>>> ecd1fe77e (Update development/compiling/compiling_for_windows.rst)

See :ref:`KinematicCollision2D <class_KinematicCollision2D>` for details on what
collision data is returned.

Which movement method to use?
-----------------------------

A common question from new Godot users is: "How do you decide which movement
function to use?" Often, the response is to use ``move_and_slide()`` because
it seems simpler, but this is not necessarily the case. One way to think of it
is that ``move_and_slide()`` is a special case, and ``move_and_collide()``
is more general. For example, the following two code snippets result in
the same collision response:

.. image:: img/k2d_compare.gif

.. tabs::
 .. code-tab:: gdscript GDScript

    # using move_and_collide
    var collision = move_and_collide(velocity * delta)
    if collision:
<<<<<<< HEAD
        velocity = velocity.slide(collision.get_normal())

    # using move_and_slide
    move_and_slide()
=======
        velocity = velocity.slide(collision.normal)

    # using move_and_slide
    velocity = move_and_slide(velocity)
>>>>>>> ecd1fe77e (Update development/compiling/compiling_for_windows.rst)

 .. code-tab:: csharp

    // using MoveAndCollide
<<<<<<< HEAD
    var collision = MoveAndCollide(Velocity * (float)delta);
    if (collision != null)
    {
        velocity = velocity.Slide(collision.GetNormal());
    }
    // using MoveAndSlide
    MoveAndSlide();
=======
    var collision = MoveAndCollide(velocity * delta);
    if (collision != null)
    {
        velocity = velocity.Slide(collision.Normal);
    }
    // using MoveAndSlide
    velocity = MoveAndSlide(velocity);
>>>>>>> ecd1fe77e (Update development/compiling/compiling_for_windows.rst)

Anything you do with ``move_and_slide()`` can also be done with ``move_and_collide()``,
but it might take a little more code. However, as we'll see in the examples below,
there are cases where ``move_and_slide()`` doesn't provide the response you want.

<<<<<<< HEAD
In the example above, ``move_and_slide()`` automatically alters the ``velocity``
variable. This is because when the character collides with the environment,
the function recalculates the speed internally to reflect
=======
In the example above, we assign the velocity that ``move_and_slide()`` returns
back into the ``velocity`` variable. This is because when the character collides
with the environment, the function recalculates the speed internally to reflect
>>>>>>> ecd1fe77e (Update development/compiling/compiling_for_windows.rst)
the slowdown.

For example, if your character fell on the floor, you don't want it to
accumulate vertical speed due to the effect of gravity. Instead, you want its
vertical speed to reset to zero.

``move_and_slide()`` may also recalculate the kinematic body's velocity several
times in a loop as, to produce a smooth motion, it moves the character and
<<<<<<< HEAD
collides up to five times by default. At the end of the process, the character's
new velocity is available for use on the next frame.
=======
collides up to five times by default. At the end of the process, the function
returns the character's new velocity that we can store in our ``velocity``
variable, and use on the next frame.
>>>>>>> ecd1fe77e (Update development/compiling/compiling_for_windows.rst)

Examples
--------

To see these examples in action, download the sample project:
:download:`using_kinematic2d.zip <files/using_kinematic2d.zip>`.

Movement and walls
~~~~~~~~~~~~~~~~~~

If you've downloaded the sample project, this example is in "BasicMovement.tscn".

For this example, add a ``CharacterBody2D`` with two children: a ``Sprite2D`` and a
``CollisionShape2D``. Use the Godot "icon.png" as the Sprite2D's texture (drag it
from the Filesystem dock to the *Texture* property of the ``Sprite2D``). In the
``CollisionShape2D``'s *Shape* property, select "New RectangleShape2D" and
size the rectangle to fit over the sprite image.

.. note:: See :ref:`doc_2d_movement` for examples of implementing 2D movement schemes.

Attach a script to the CharacterBody2D and add the following code:

.. tabs::
 .. code-tab:: gdscript GDScript

    extends CharacterBody2D

<<<<<<< HEAD
    var speed = 300

    func get_input():
        var input_dir = Input.get_vector("ui_left", "ui_right", "ui_up", "ui_down")
        velocity = input_dir * speed
=======
    var speed = 250
    var velocity = Vector2()

    func get_input():
        # Detect up/down/left/right keystate and only move when pressed.
        velocity = Vector2()
        if Input.is_action_pressed('ui_right'):
            velocity.x += 1
        if Input.is_action_pressed('ui_left'):
            velocity.x -= 1
        if Input.is_action_pressed('ui_down'):
            velocity.y += 1
        if Input.is_action_pressed('ui_up'):
            velocity.y -= 1
        velocity = velocity.normalized() * speed
>>>>>>> ecd1fe77e (Update development/compiling/compiling_for_windows.rst)

    func _physics_process(delta):
        get_input()
        move_and_collide(velocity * delta)

 .. code-tab:: csharp

    using Godot;
<<<<<<< HEAD

    public partial class CBExample : CharacterBody2D
    {
        public int Speed = 300;

        public void GetInput()
        {
            Vector2 inputDir = Input.GetVector("ui_left", "ui_right", "ui_up", "ui_down");
            Velocity = inputDir * Speed;
        }

        public override void _PhysicsProcess(double delta)
        {
            GetInput();
            MoveAndCollide(Velocity * (float)delta);
=======
    using System;

    public class KBExample : CharacterBody2D
    {
        public int Speed = 250;
        private Vector2 _velocity = new Vector2();

        public void GetInput()
        {
            // Detect up/down/left/right keystate and only move when pressed
            _velocity = new Vector2();

            if (Input.IsActionPressed("ui_right"))
                _velocity.x += 1;

            if (Input.IsActionPressed("ui_left"))
                _velocity.x -= 1;

            if (Input.IsActionPressed("ui_down"))
                _velocity.y += 1;

            if (Input.IsActionPressed("ui_up"))
                _velocity.y -= 1;
            _velocity = _velocity.Normalized() * Speed;
        }

        public override void _PhysicsProcess(float delta)
        {
            GetInput();
            MoveAndCollide(_velocity * delta);
>>>>>>> ecd1fe77e (Update development/compiling/compiling_for_windows.rst)
        }
    }


Run this scene and you'll see that ``move_and_collide()`` works as expected, moving
the body along the velocity vector. Now let's see what happens when you add
some obstacles. Add a :ref:`StaticBody2D <class_StaticBody2D>` with a
rectangular collision shape. For visibility, you can use a sprite, a
Polygon2D, or turn on "Visible Collision Shapes" from the "Debug" menu.

Run the scene again and try moving into the obstacle. You'll see that the ``CharacterBody2D``
can't penetrate the obstacle. However, try moving into the obstacle at an angle and
you'll find that the obstacle acts like glue - it feels like the body gets stuck.

This happens because there is no *collision response*. ``move_and_collide()`` stops
the body's movement when a collision occurs. We need to code whatever response we
want from the collision.

<<<<<<< HEAD
Try changing the function to ``move_and_slide()`` and running again.
=======
Try changing the function to ``move_and_slide(velocity)`` and running again.
Note that we removed ``delta`` from the velocity calculation.
>>>>>>> ecd1fe77e (Update development/compiling/compiling_for_windows.rst)

``move_and_slide()`` provides a default collision response of sliding the body along the
collision object. This is useful for a great many game types, and may be all you need
to get the behavior you want.

Bouncing/reflecting
~~~~~~~~~~~~~~~~~~~

What if you don't want a sliding collision response? For this example ("BounceandCollide.tscn"
in the sample project), we have a character shooting bullets and we want the bullets to
bounce off the walls.

This example uses three scenes. The main scene contains the Player and Walls.
The Bullet and Wall are separate scenes so that they can be instanced.

The Player is controlled by the `w` and `s` keys for forward and back. Aiming
uses the mouse pointer. Here is the code for the Player, using ``move_and_slide()``:

.. tabs::
 .. code-tab:: gdscript GDScript

    extends CharacterBody2D

    var Bullet = preload("res://Bullet.tscn")
    var speed = 200
<<<<<<< HEAD

    func get_input():
        # Add these actions in Project Settings -> Input Map.
        var input_dir = Input.get_axis("backward", "forward")
        velocity = transform.x * input_dir * speed
        if Input.is_action_just_pressed("shoot"):
=======
    var velocity = Vector2()

    func get_input():
        # Add these actions in Project Settings -> Input Map.
        velocity = Vector2()
        if Input.is_action_pressed('backward'):
            velocity = Vector2(-speed/3, 0).rotated(rotation)
        if Input.is_action_pressed('forward'):
            velocity = Vector2(speed, 0).rotated(rotation)
        if Input.is_action_just_pressed('mouse_click'):
>>>>>>> ecd1fe77e (Update development/compiling/compiling_for_windows.rst)
            shoot()

    func shoot():
        # "Muzzle" is a Marker2D placed at the barrel of the gun.
        var b = Bullet.instantiate()
        b.start($Muzzle.global_position, rotation)
<<<<<<< HEAD
        get_tree().root.add_child(b)
=======
        get_parent().add_child(b)
>>>>>>> ecd1fe77e (Update development/compiling/compiling_for_windows.rst)

    func _physics_process(delta):
        get_input()
        var dir = get_global_mouse_position() - global_position
        # Don't move if too close to the mouse pointer.
        if dir.length() > 5:
            rotation = dir.angle()
<<<<<<< HEAD
            move_and_slide()
=======
            velocity = move_and_slide(velocity)
>>>>>>> ecd1fe77e (Update development/compiling/compiling_for_windows.rst)

 .. code-tab:: csharp

    using Godot;
<<<<<<< HEAD

    public partial class CBExample : CharacterBody2D
    {
        private PackedScene _bullet = (PackedScene)GD.Load("res://Bullet.tscn");
        public int Speed = 200;

        public void GetInput()
        {
            // Add these actions in Project Settings -> Input Map.
            float inputDir = Input.GetAxis("backward", "forward");
            Velocity = Transform.x * inputDir * Speed;
            if (Input.IsActionPressed("shoot"))
=======
    using System;

    public class KBExample : CharacterBody2D
    {
        private PackedScene _bullet = (PackedScene)GD.Load("res://Bullet.tscn");
        public int Speed = 200;
        private Vector2 _velocity = new Vector2();

        public void GetInput()
        {
            // add these actions in Project Settings -> Input Map
            _velocity = new Vector2();
            if (Input.IsActionPressed("backward"))
            {
                _velocity = new Vector2(-Speed/3, 0).Rotated(Rotation);
            }
            if (Input.IsActionPressed("forward"))
            {
                _velocity = new Vector2(Speed, 0).Rotated(Rotation);
            }
            if (Input.IsActionPressed("mouse_click"))
>>>>>>> ecd1fe77e (Update development/compiling/compiling_for_windows.rst)
            {
                Shoot();
            }
        }

        public void Shoot()
        {
<<<<<<< HEAD
            // "Muzzle" is a Marker2D placed at the barrel of the gun.
            var b = (Bullet)_bullet.Instantiate();
            b.Start(GetNode<Node2D>("Muzzle").GlobalPosition, Rotation);
            GetTree().Root.AddChild(b);
        }

        public override void _PhysicsProcess(double delta)
        {
            GetInput();
            var dir = GetGlobalMousePosition() - GlobalPosition;
            // Don't move if too close to the mouse pointer.
            if (dir.Length() > 5)
            {
                Rotation = dir.Angle();
                MoveAndSlide();
=======
            // "Muzzle" is a Marker2D placed at the barrel of the gun
            var b = (Bullet)_bullet.Instantiate();
            b.Start(GetNode<Node2D>("Muzzle").GlobalPosition, Rotation);
            GetParent().AddChild(b);
        }

        public override void _PhysicsProcess(float delta)
        {
            GetInput();
            var dir = GetGlobalMousePosition() - GlobalPosition;
            // Don't move if too close to the mouse pointer
            if (dir.Length() > 5)
            {
                Rotation = dir.Angle();
                _velocity = MoveAndSlide(_velocity);
>>>>>>> ecd1fe77e (Update development/compiling/compiling_for_windows.rst)
            }
        }
    }


And the code for the Bullet:

.. tabs::
 .. code-tab:: gdscript GDScript

    extends CharacterBody2D

    var speed = 750
<<<<<<< HEAD

    func start(_position, _direction):
        rotation = _direction
        position = _position
=======
    var velocity = Vector2()

    func start(pos, dir):
        rotation = dir
        position = pos
>>>>>>> ecd1fe77e (Update development/compiling/compiling_for_windows.rst)
        velocity = Vector2(speed, 0).rotated(rotation)

    func _physics_process(delta):
        var collision = move_and_collide(velocity * delta)
        if collision:
<<<<<<< HEAD
            velocity = velocity.bounce(collision.get_normal())
            if collision.get_collider().has_method("hit"):
                collision.get_collider().hit()

    func _on_VisibilityNotifier2D_screen_exited():
        # Deletes the bullet when it exits the screen.
=======
            velocity = velocity.bounce(collision.normal)
            if collision.collider.has_method("hit"):
                collision.collider.hit()

    func _on_VisibilityNotifier2D_screen_exited():
>>>>>>> ecd1fe77e (Update development/compiling/compiling_for_windows.rst)
        queue_free()

 .. code-tab:: csharp

    using Godot;
<<<<<<< HEAD

    public partial class Bullet : CharacterBody2D
    {
        public int Speed = 750;

        public void Start(Vector2 position, float direction)
        {
            Rotation = direction;
            Position = position;
            Velocity = new Vector2(speed, 0).Rotated(Rotation);
        }

        public override void _PhysicsProcess(double delta)
        {
            var collision = MoveAndCollide(Velocity * (float)delta);
            if (collision != null)
            {
                Velocity = Velocity.Bounce(collision.GetNormal());
                if (collision.GetCollider().HasMethod("Hit"))
                {
                    collision.GetCollider().Call("Hit");
=======
    using System;

    public class Bullet : CharacterBody2D
    {
        public int Speed = 750;
        private Vector2 _velocity = new Vector2();

        public void Start(Vector2 pos, float dir)
        {
            Rotation = dir;
            Position = pos;
            _velocity = new Vector2(speed, 0).Rotated(Rotation);
        }

        public override void _PhysicsProcess(float delta)
        {
            var collision = MoveAndCollide(_velocity * delta);
            if (collision != null)
            {
                _velocity = _velocity.Bounce(collision.Normal);
                if (collision.Collider.HasMethod("Hit"))
                {
                    collision.Collider.Call("Hit");
>>>>>>> ecd1fe77e (Update development/compiling/compiling_for_windows.rst)
                }
            }
        }

        public void OnVisibilityNotifier2DScreenExited()
        {
<<<<<<< HEAD
            // Deletes the bullet when it exits the screen.
=======
>>>>>>> ecd1fe77e (Update development/compiling/compiling_for_windows.rst)
            QueueFree();
        }
    }


The action happens in ``_physics_process()``. After using ``move_and_collide()``, if a
collision occurs, a ``KinematicCollision2D`` object is returned (otherwise, the return
is ``Nil``).

If there is a returned collision, we use the ``normal`` of the collision to reflect
the bullet's ``velocity`` with the ``Vector2.bounce()`` method.

If the colliding object (``collider``) has a ``hit`` method,
we also call it. In the example project, we've added a flashing color effect to
the Wall to demonstrate this.

.. image:: img/k2d_bullet_bounce.gif

Platformer movement
~~~~~~~~~~~~~~~~~~~

Let's try one more popular example: the 2D platformer. ``move_and_slide()``
is ideal for quickly getting a functional character controller up and running.
<<<<<<< HEAD
If you've downloaded the sample project, you can find this in "platformer.tscn".

For this example, we'll assume you have a level made of one or more ``StaticBody2D``
objects. They can be any shape and size. In the sample project, we're using
=======
If you've downloaded the sample project, you can find this in "Platformer.tscn".

For this example, we'll assume you have a level made of ``StaticBody2D`` objects.
They can be any shape and size. In the sample project, we're using
>>>>>>> ecd1fe77e (Update development/compiling/compiling_for_windows.rst)
:ref:`Polygon2D <class_Polygon2D>` to create the platform shapes.

Here's the code for the player body:


.. tabs::
 .. code-tab:: gdscript GDScript

    extends CharacterBody2D

<<<<<<< HEAD
    var speed = 300.0
    var jump_speed = -400.0

    # Get the gravity from the project settings so you can sync with rigid body nodes.
    var gravity = ProjectSettings.get_setting("physics/2d/default_gravity")


    func _physics_process(delta):
        # Add the gravity.
        velocity.y += gravity * delta

        # Handle Jump.
        if Input.is_action_just_pressed("jump") and is_on_floor():
            velocity.y = jump_speed

        # Get the input direction.
        var direction = Input.get_axis("ui_left", "ui_right")
        velocity.x = direction * speed

        move_and_slide()
=======
    export (int) var run_speed = 100
    export (int) var jump_speed = -400
    export (int) var gravity = 1200

    var velocity = Vector2()
    var jumping = false

    func get_input():
        velocity.x = 0
        var right = Input.is_action_pressed('ui_right')
        var left = Input.is_action_pressed('ui_left')
        var jump = Input.is_action_just_pressed('ui_select')

        if jump and is_on_floor():
            jumping = true
            velocity.y = jump_speed
        if right:
            velocity.x += run_speed
        if left:
            velocity.x -= run_speed

    func _physics_process(delta):
        get_input()
        velocity.y += gravity * delta
        if jumping and is_on_floor():
            jumping = false
        velocity = move_and_slide(velocity, Vector2(0, -1))
>>>>>>> ecd1fe77e (Update development/compiling/compiling_for_windows.rst)

 .. code-tab:: csharp

    using Godot;
<<<<<<< HEAD

    public partial class CBExample : CharacterBody2D
    {
        public float Speed = 100.0f;
        public float JumpSpeed = -400.0f;

        // Get the gravity from the project settings so you can sync with rigid body nodes.
        public float Gravity = ProjectSettings.GetSetting("physics/2d/default_gravity").AsSingle();

        public override void _PhysicsProcess(double delta)
        {
            Vector2 velocity = Velocity;

            // Add the gravity.
            velocity.y += Gravity * (float)delta;

            // Handle jump.
            if (Input.IsActionJustPressed("jump") && IsOnFloor())
                velocity.y = JumpSpeed;

            // Get the input direction.
            Vector2 direction = Input.GetAxis("ui_left", "ui_right");
            velocity.x = direction * Speed;

            Velocity = velocity;
            MoveAndSlide();
=======
    using System;

    public class KBExample : CharacterBody2D
    {
        [Export] public int RunSpeed = 100;
        [Export] public int JumpSpeed = -400;
        [Export] public int Gravity = 1200;

        Vector2 velocity = new Vector2();
        bool jumping = false;

        public void GetInput()
        {
            velocity.x = 0;
            bool right = Input.IsActionPressed("ui_right");
            bool left = Input.IsActionPressed("ui_left");
            bool jump = Input.IsActionPressed("ui_select");

            if (jump && IsOnFloor())
            {
                jumping = true;
                velocity.y = JumpSpeed;
            }

            if (right)
                velocity.x += RunSpeed;
            if (left)
                velocity.x -= RunSpeed;
        }

        public override void _PhysicsProcess(float delta)
        {
            GetInput();
            velocity.y += Gravity * delta;
            if (jumping && IsOnFloor())
                jumping = false;
            velocity = MoveAndSlide(velocity, new Vector2(0, -1));
>>>>>>> ecd1fe77e (Update development/compiling/compiling_for_windows.rst)
        }
    }

.. image:: img/k2d_platform.gif

<<<<<<< HEAD
In this code we're using ``move_and_slide()`` as described above - to move the body
along its velocity vector, sliding along any collision surfaces such as the ground
or a platform. We're also using ``is_on_floor()`` to check if a jump should be
allowed. Without this, you'd be able to "jump" in midair; great if you're making
Flappy Bird, but not for a platformer game.

There is a lot more that goes into a complete platformer character: acceleration,
double-jumps, coyote-time, and many more. The code above is just a starting point.
You can use it as a base to expand into whatever movement behavior you need for
your own projects.
=======
When using ``move_and_slide()``, the function returns a vector representing the
movement that remained after the slide collision occurred. Setting that value back
to the character's ``velocity`` allows us to move up and down slopes smoothly. Try
removing ``velocity =`` and see what happens if you don't do this.

Also note that we've added ``Vector2(0, -1)`` as the floor normal. This vector points
straight upward. As a result, if the character collides with an object
that has this normal, it will be considered a floor.

Using the floor normal allows us to make jumping work, using ``is_on_floor()``.
This function will only return ``true`` after a ``move_and_slide()`` collision
where the colliding body's normal is within 45 degrees of the given floor
vector. You can control the maximum angle by setting ``floor_max_angle``.

This angle also allows you to implement other features like wall jumps using
``is_on_wall()``, for example.
>>>>>>> ecd1fe77e (Update development/compiling/compiling_for_windows.rst)
