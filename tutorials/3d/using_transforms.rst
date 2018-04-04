.. _doc_using_transforms:

Using transforms for 3D games in Godot
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Introduction
------------

If you have never made 3D games before, the way to approach rotations with three dimensions can be very confusing at first.
Coming from 2D, the natural way of thinking is along the lines of *"Oh, it's just like roating in 2D, except now rotations happen in X, Y and Z"*.

At first this seems easy and, for simple games, this way of thinking may even be enough. Unfortunately, It's just very limiting and most often incorrect.

Angles in three dimensions are most commonly refered to as "Euler Angles".

.. image:: img/transforms_euler.png

Euler Angles were introduced by mathematician Leonhard Euler in the early 1700s.

.. image:: img/transforms_euler_himself.png

This way of representing a 3D rotation has several shortcomings when used in game development (which is to be expected from a guy with a funny hat), and
the idea of this document is to explain why, as well as outlining best practices for dealing with transforms when programming 3D games.


Problems of Euler Angles
------------------------

While it may seem very intuitive that each axis has a rotation, the truth is that it's just not practical.

Axis Order
==========

The main reason for this is that there isn't a *unique* way to construct an orientation from the angles. There isn't a standard mathematical function that 
takes all the angles togehter and produces an actual 3D rotation. The only way an orientation can be produced from angles is to rotate the object angle
by angle, in an *arbitrary order*.

This could be done by first rotating in *X*, then *Y* and then in *Z*. Alternatively, you could first rotate in *Y*, then in *Z* and finally in *X*. Anything really works,
but depending on the order, the final orientation of the object will *not necesarily be the same*. Indeed, this means that there are several ways to construct an orientation
from 3 different angles, depending on *the order the rotations happen*.

Following is a visualization of rotation axes (in X,Y,Z order) in a gimbal (from Wikipedia). As it can be appreciated, the orientation of each axis depends on the rotation of the previous one:

.. image:: img/transforms_gimbal.gif

You may be wondering how this might affect you, though. Let's go to a practical example, then.

Imagine you are working on a first person controller (FPS game). Moving the mouse left and right (2D screen X axis) controls your view angle based on the ground, while moving it up and down
makes the player head look actually up and down. 

In this case, to achieve the desired effect, rotation should be applied first in *Y* axis (Up in our case, as Godot uses Y-Up), and then in *X* axis.

.. image:: img/transforms_rotate1.gif

If we were to simply apply rotation in *X* axis first, then in *Y*, the effect would be undesired:

.. image:: img/transforms_rotate2.gif

Depending on the type of game or effect desired, the order in which you want axis rotations to be applied may differ. Just accessing rotations as X,Y and Z is not enough, you need a *rotation order*.


Interpolation
=============

Another problem of using euler angles is interpolation. Imagine you want to transition between two different camera or enemy positions (including rotations). The logical way one may
approach is is to just interpolate the angles from one position to to the next. One would expect it to look like this:

.. image:: img/transforms_interpolate1.gif


But this does not always have the expected effect when using angles:

.. image:: img/transforms_interpolate2.gif

The camera actually rotated the opposite direction! 

There are reasons for this to have happened:

* Rotations dont linearly map to orientation, so interpolating them does not always result in the closest path (ie, to go from 270 to 0 degrees is no the same as going from 270 to 360, even though angles are equivalent).
* Gimbal lock is at play (first and last rotated axis align, so a degree of freedom is lost).

Say no to Euler Angles
======================

This means, pretty much, just **don't use** the *rotation* property of :ref:`class_Spatial` nodes in Godot for games. It's there to be used mainly fromt the editor, coherence with the 2D engine and for very simple rotations (generally just 1 axis, 2 in limited cases). As much as it tempts you, don't use it. 

There is always a better way around Euler Angles for your specific problem waiting to be found by you.

Introducing Transforms
----------------------

Godot uses the :ref:`class_Transform` datatype for orientations. Each :ref:`class_Spatial` node contains one of those transforms (via *transform* property), which is relative to the parent transform (in case the parent is of Spatial or derived type too).

It is also possible to access the world coordinate transform (via *global_transform* property). 

A transform has a :ref:`class_Basis` (transform.basis sub-property), which consists of 3 :ref:`class_Vector3` vectors (transform.basis.x to transform.basis.z). Each points to the direction where each actual axis is rotated to, so they effectively contain a rotation. The scale (as long as it's uniform) can be also be inferred from the length of the axes. A *Basis* can also be interpreted as a 3x3 matrix (used as transform.basis[x][y]).

A default basis (unmodified) is akin to:

.. code-block:: python

    var basis = Basis()
    # Has these default values built-in (Below is redundant, but just to make it clear)
    basis.x = Vector3(1, 0, 0) # Vector pointing to X axis
    basis.y = Vector3(0, 1, 0) # Vector pointing to Y axis
    basis.z = Vector3(0, 0, 1) # Vector pointing to Z axis

This is also analog to an 3x3 identity matrix.

In Godot (following OpenGL convention), X is the *Right* axis, Y is the *Up* axis and Z is the *Forward* axis.

Together with the *Basis*, a transform also has an *origin*. This is a *Vector3* specifying how far away from the actual origin (0,0,0 in xyz) this transform is. Together with the *basis*, a *Transform* efficiently represents a unique translation, rotation and scale in space.

A simple way to visualize a transform is to just look at an object transform gizmo (in local mode). It will show the X, Y and Z axes (as red, green and blue respectively) of the basis as the arrows, while the origin is just the center of the gizmo (where arrows emerge) in space.

.. image:: img/transforms_gizmo.png

For more information on the mathematics of vectors and transforms, please read the :ref:`vector_math` tutorials.

Manipulating Transforms
=======================

Of course, transforms are not nearly as straightforward to manipulate as angles and have problems of their own.

It is possible to rotate a transform, by either multiplying it's basis by another (this is called accumulation), or just using the rotation methods.


.. code-block:: python

    # Rotate the transform in X axis
    transform.basis = Basis( Vector3(1,0,0), PI ) * transform.basis
    # Simplified
    transform.basis = transform.basis.rotated( Vector3(1,0,0), PI )

A method in Spatial simplifies this:

.. code-block:: python

    # Rotate the transform in X axis
    rotate( Vector3(1,0,0), PI )
    # or, just shortened 
    rotate_x( PI )

This will rotate the node relative to the parent node space. 
To rotate relative to object space (node's own transform) the following must be done.

.. code-block:: python

    # Rotate locally, notice multiplication order is inverted
    transform = transform * Basis( Vector3(1,0,0), PI )
    # or, shortened
    rotate_object_local( Vector3(1,0,0), PI )

Precision Errors
================

Doing successive operations on transforms will result in a precision degradation due to floating point error. This means scale of each axis may no longer be exactly 1.0, and not exactly 90 degrees from each other.

If a transform is rotated every frame, it will eventually start deforming slightly long term. This is unavoidable. 

There are however, two different ways to handle this. The first is to orthonormalize the transform after a while (maybe once per frame if you modify it every frame):

.. code-block:: python

    transform = transform.orthonormalized()

This will make all axes have 1.0 length again and be 90 degrees from each other. If the transform had scale, it will be lost, though. 

It is recommended you don't scale nodes that are going to be manipulated, scale their children nodes instead (like MeshInstance). If you absolutely must have scale, then re-apply it in the end:

.. code-block:: python

    transform = transform.orthonormalized()
    transform = transform.scaled( scale )


Obtaining Information
=====================

You might be thinking at this point: **"Ok, but how do I get angles from a transform?"**. Answer is again, you don't. You must do your best to stop thinking in angles. 

Imagine you need to shoot a bullet in the direction your player is looking towards to. Just use the forward axis (commonly Z or -Z for this).

.. code-block:: python

    bullet.transform = transform
    bullet.speed = transform.basis.z * BULLET_SPEED

So, is the enemy looking at my player? you can use dot product for this (dot product is explained in the vector math tutorial linked before):

.. code-block:: python

    if (enemy.transform.origin - player.transform.origin). dot( enemy.transform.basis.z ) > 0 ):
	enemy.im_watching_you(player)

Let's strafe left!

.. code-block:: python

    # Remember that X is Right
    if (Input.is_key_pressed("strafe_left")):
	translate_object_local( -transform.basis.x )

Time to jump..

.. code-block:: python

    # Keep in mind Y is up-axis
    if (Input.is_key_just_pressed("jump")):
        velocity.y = JUMP_SPEED

    velocity = move_and_slide( velocity )

All common behaviors and logic can be done with just vectors.

Setting Information
===================

There are, of course, cases where you want to set information to a transform. Imagine a first person controller or orbiting camera. Those are definitely done using angles, because you *do want*
the transforms to happen in a specific order.

For such cases, just keep the angles and rotations *outside* the transform and set them every frame. Don't try retrieve them and re-use them because the transform is not meant to be used this way.

Example of looking around, FPS style:

.. code-block:: python

    # accumulators
    var rot_x = 0
    var rot_y = 0
    
    func _input(ev):
    	
        if (ev is InputEventMouseMotion and ev.button_mask & 1):
            # modify accumulated mouse rotation
            rot_x += ev.relative.x * LOOKAROUND_SPEED
            rot_y += ev.relative.y * LOOKAROUND_SPEED
            transform.basis = Basis() # reset rotation
            rotate_object_local( Vector3(0,1,0), rot_x ) # first rotate in Y
            rotate_object_local( Vector3(1,0,0), rot_y ) # then rotate in X

As you can see, in such cases it's even simpler to keep the rotation outside, then use the transform as the *final* orientation.

Transforms are your friend
~~~~~~~~~~~~~~~~~~~~~~~~~~

Once you get used to transforms, you will appreciate their simplicity and power. Of course, for most starting with 3D games, getting used to them can take a while and it can be a bit tricky.
Don't hesitate to ask for help in this topic in many of our online communities and, once you become confident enough, please help others!

