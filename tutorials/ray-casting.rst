.. _doc_ray-casting:

Ray-casting
===========

Introduction
------------

One of the most common tasks in game development is casting a ray (or
custom shaped object) and checking what it hits. This enables complex
behaviors, AI, etc. to take place. This tutorial will explain how to
do this in 2D and 3D.

Godot stores all the low level game information in servers, while the
scene is just a frontend. As such, ray casting is generally a
lower-level task. For simple raycasts, node such as
:ref:`RayCast <class_RayCast>` and :ref:`RayCast2D <class_RayCast2D>`
will work, as they will return every frame what the result of a raycast
is.

Many times, though, ray-casting needs to be a more interactive process
so a way to do this by code must exist.

Space
-----

In the physics world, Godot stores all the low level collision and
physics information in a *space*. The current 2d space (for 2D Physics)
can be obtained by calling
:ref:`CanvasItem.get_world_2d().get_space() <class_CanvasItem_get_world_2d>`.
For 3D, it's :ref:`Spatial.get_world().get_space() <class_Spatial_get_world>`.

The resulting space :ref:`RID <class_RID>` can be used in
:ref:`PhysicsServer <class_PhysicsServer>` and
:ref:`Physics2DServer <class_Physics2DServer>` respectively for 3D and 2D.

Accessing space
--------------

Godot physics runs by default in the same thread as game logic, but may
be set to run on a separate thread to work more efficiently. Due to
this, the only time accessing space is safe is during the
:ref:`Node._fixed_process() <class_Node__fixed_process>`
callback. Accessing it from outside this function may result in an error
due to space being *locked*.

To perform queries into physics space, the
:ref:`Physics2DDirectSpaceState <class_Physics2DDirectSpaceState>`
and :ref:`PhysicsDirectSpaceState <class_PhysicsDirectSpaceState>`
must be used.

In code, for 2D spacestate, this code must be used:

::

    func _fixed_process(delta):
        var space_rid = get_world_2d().get_space()
        var space_state = Physics2DServer.space_get_direct_state(space_rid)

Of course, there is a simpler shortcut:

::

    func _fixed_process(delta):
        var space_state = get_world_2d().get_direct_space_state()

For 3D:

::

    func _fixed_process(delta):
        var space_state = get_world().get_direct_space_state()

Raycast query
-------------

For performing a 2D raycast query, the method
:ref:`Physics2DDirectSpaceState.intersect_ray() <class_Physics2DDirectSpaceState_intersect_ray>`
must be used, for example:

::

    func _fixed_process(delta):
        var space_state = get_world().get_direct_space_state()
        # use global coordinates, not local to node
        var result = space_state.intersect_ray( Vector2(0,0), Vector2(50,100) )

Result is a dictionary. If the ray didn't hit anything, the dictionary will
be empty. If it did hit something it will contain collision information:

::

        if (not result.empty()):
            print("Hit at point: ",result.position)

The collision result dictionary, when something hit, has this format:

::

    {
       position:Vector2 # point in world space for collision
       normal:Vector2 # normal in world space for collision
       collider:Object # Object collided or null (if unassociated)
       collider_id:ObjectID # Object it collided against
       rid:RID # RID it collided against
       shape:int # shape index of collider
       metadata:Variant() # metadata of collider
    }

    # in case of 3D, Vector3 is returned.

Collision exceptions
--------------------

It is a very common case to attempt casting a ray from a character or
another game scene to try to infer properties of the world around it.
The problem with this is that the same character has a collider, so the
ray can never leave the origin (it will keep hitting it's own collider),
as evidenced in the following image.

.. image:: /img/raycast_falsepositive.png

To avoid self-intersection, the intersect_ray() function can take an
optional third parameter which is an array of exceptions. This is an
example of how to use it from a KinematicBody2D or any other
collisionobject based node:

::

    extends KinematicBody2D

    func _fixed_process(delta):
        var space_state = get_world().get_direct_space_state()
        var result = space_state.intersect_ray( get_global_pos(), enemy_pos, [ self ] )

The extra argument is a list of exceptions, can be objects or RIDs.

3D ray casting from screen
--------------------------

Casting a ray from screen to 3D physics space is useful for object
picking. There is not much of a need to do this because
:ref:`CollisionObject <class_CollisionObject>`
has an "input_event" signal that will let you know when it was clicked,
but in case there is any desire to do it manually, here's how.

To cast a ray from the screen, the :ref:`Camera <class_Camera>` node
is needed. Camera can be in two projection modes, perspective and
orthogonal. Because of this, both the ray origin and direction must be
obtained. (origin changes in orthogonal, while direction changes in
perspective):

.. image:: /img/raycast_projection.png

To obtain it using a camera, the following code can be used:

::

    const ray_length = 1000

    func _input(ev):
        if ev.type==InputEvent.MOUSE_BUTTON and ev.pressed and ev.button_index==1:

              var camera = get_node("camera")
              var from = camera.project_ray_origin(ev.pos)
              var to = from + camera.project_ray_normal(ev.pos) * ray_length

Of course, remember that during ``_input()``, space may be locked, so save
your query for ``_fixed_process()``.
