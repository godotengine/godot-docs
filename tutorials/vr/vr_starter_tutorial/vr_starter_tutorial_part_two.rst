.. _doc_vr_starter_tutorial_part_two:

VR Starter Tutorial Part Two
============================

Introduction
------------

.. image:: img/starter_vr_tutorial_sword.png

In this part of the VR starter tutorial series, we will be adding a number of special :ref:`RigidBody <class_RigidBody>`-based nodes that can be used in VR.

This continues from where we left on in the last tutorial part, where we just finished getting the VR controllers working and defined a custom
class called ``VR_Interactable_Rigidbody``.

.. tip:: You can find the finished project on the `OpenVR GitHub repository <https://github.com/GodotVR/godot_openvr_fps>`_.


Adding destroyable targets
--------------------------

Before we make any of the special :ref:`RigidBody <class_RigidBody>`-based nodes, we need something for them to do. Let's make a simple sphere target that will break into a bunch of pieces
when destroyed.

Open up ``Sphere_Target.tscn``, which is in the ``Scenes`` folder. The scene is fairly simple, with just a :ref:`StaticBody <class_StaticBody>` with a sphere shaped
:ref:`CollisionShape <class_CollisionShape>`, a :ref:`MeshInstance <class_MeshInstance>` node displaying a sphere mesh, and an :ref:`AudioStreamPlayer3D <class_AudioStreamPlayer3D>` node.

The special :ref:`RigidBody <class_RigidBody>` nodes will handle damaging the sphere, which is why we are using a :ref:`StaticBody <class_StaticBody>` node instead of something like
an :ref:`Area <class_Area>` or :ref:`RigidBody <class_RigidBody>` node. Outside of that, there isn't really a lot to talk about, so let's move straight into writing the code.

Select the ``Sphere_Target_Root`` node and make a new script called ``Sphere_Target.gd``. Add the following code:

.. tabs::
 .. code-tab:: gdscript GDScript

    extends Spatial

    var destroyed = false
    var destroyed_timer = 0
    const DESTROY_WAIT_TIME = 80

    var health = 80

    const RIGID_BODY_TARGET = preload("res://Assets/RigidBody_Sphere.scn")


    func _ready():
        set_physics_process(false)


    func _physics_process(delta):
        destroyed_timer += delta
        if destroyed_timer >= DESTROY_WAIT_TIME:
            queue_free()


    func damage(damage):
        if destroyed == true:
            return
        
        health -= damage
        
        if health <= 0:
            
            get_node("CollisionShape").disabled = true
            get_node("Shpere_Target").visible = false
            
            var clone = RIGID_BODY_TARGET.instance()
            add_child(clone)
            clone.global_transform = global_transform
            
            destroyed = true
            set_physics_process(true)
            
            get_node("AudioStreamPlayer").play()
            get_tree().root.get_node("Game").remove_sphere()


Let's go over how this script works.

Explaining the Sphere Target code
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

First, let's go through all of the class variables in the script:

* ``destroyed``: A variable to track whether the sphere target has been destroyed.
* ``destroyed_timer``: A variable to track how long the sphere target has been destroyed.
* ``DESTROY_WAIT_TIME``: A constant to define the length of time the target can be destroyed for before it frees/deletes itself.
* ``health``: A variable to store the amount of health the sphere target has.
* ``RIGID_BODY_TARGET``: A constant to hold the scene of the destroyed sphere target.

.. note:: Feel free to check out the ``RIGID_BODY_TARGET`` scene. It is just a bunch of :ref:`RigidBody <class_RigidBody>` nodes and a broken sphere model.
          
          We'll be instancing this scene so when the target is destroyed, it looks like it broke into a bunch of pieces.


``_ready`` function step-by-step explanation
""""""""""""""""""""""""""""""""""""""""""""

All the ``_ready`` function does is that it stops the ``_physics_process`` from being called by calling ``set_physics_process`` and passing ``false``.
The reason we do this is because all of the code in ``_physics_process`` is for destroying this node when enough time has passed, which we only want to
do when the target has been destroyed.


``_physics_process`` function step-by-step explanation
""""""""""""""""""""""""""""""""""""""""""""""""""""""

First this function adds time, ``delta``, to the ``destroyed_timer`` variable. It then checks to see if ``destroyed_timer`` is greater than or equal to
``DESTROY_WAIT_TIME``. If ``destroyed_timer`` is greater than or equal to ``DESTROY_WAIT_TIME``, then the sphere target frees/deletes itself by calling
the ``queue_free`` function. 

``damage`` function step-by-step explanation
""""""""""""""""""""""""""""""""""""""""""""

The ``damage`` function will be called by the special :ref:`RigidBody <class_RigidBody>` nodes, which will pass the amount of damage done to the target, which is a function argument
variable called ``damage``. The ``damage`` variable will hold the amount of damage the special :ref:`RigidBody <class_RigidBody>` node did to the sphere target.

First this function checks to make sure the target is not already destroyed by checking if the ``destroyed`` variable is equal to ``true``. If ``destroyed`` is equal to ``true``, then
the function calls ``return`` so none of the other code is called. This is just a safety check so that if two things damage the target at exactly the same time, the target cannot be
destroyed twice.

Next the function removes the amount of damage taken, ``damage``, from the target's health, ``health``. If then checks to see if ``health`` is equal to zero or less, meaning that the
target has just been destroyed.

If the target has just been destroyed, then we disable the :ref:`CollisionShape <class_CollisionShape>` by setting it's ``disabled`` property to ``true``. We then make the ``Sphere_Target``
:ref:`MeshInstance <class_MeshInstance>` invisible by setting the ``visible`` property to ``false``. We do this so the target can no longer effect the physics world and so the non-broken target mesh is not visible.

After this the function then instances the ``RIGID_BODY_TARGET`` scene and adds it as a child of the target. It then sets the ``global_transform`` of the newly instanced scene, called ``clone``, to the
``global_transform`` of the non-broken target. This makes it where the broken target starts at the same position as the non-broken target with the same rotation and scale.

Then the function sets the ``destroyed`` variable to ``true`` so the target knows it has been destroyed and calls the ``set_physics_process`` function and passes ``true``. This will start
executing the code in ``_physics_process`` so that after ``DESTROY_WAIT_TIME`` seconds have passed, the sphere target will free/destroy itself.

The function then gets the :ref:`AudioStreamPlayer3D <class_AudioStreamPlayer3D>` node and calls the ``play`` function so it plays its sound.

Finally, the ``remove_sphere`` function is called in ``Game.gd``. To get ``Game.gd``, the code uses the scene tree and works its way from the root of the scene tree to the root of the
``Game.tscn`` scene.


Adding the ``remove_sphere`` function to ``Game.gd``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You may have noticed we are calling a function in ``Game.gd``, called ``remove_sphere``, that we have not defined yet. Open up ``Game.gd`` and
add the following additional class variables:

.. tabs::
 .. code-tab:: gdscript GDScript

    var spheres_left = 10
    var sphere_ui = null

- ``spheres_left``: The amount of sphere targets left in the world. In the provided ``Game`` scene, there are ``10`` spheres, so that is the initial value.
- ``sphere_ui``: A reference to the sphere UI. We will use this later in the tutorial to display the amount of spheres left in the world.

With these variables defined, we can now add the ``remove_sphere`` function. Add the following code to ``Game.gd``:

.. tabs::
 .. code-tab:: gdscript GDScript

    func remove_sphere():
        spheres_left -= 1

        if sphere_ui != null:
            sphere_ui.update_ui(spheres_left)


Let's go through what this function does real quick:

First, it removes one from the ``spheres_left`` variable. It then checks to see if the ``sphere_ui`` variable is not equal to ``null``, and if it is not
equal to ``null`` it calls the ``update_ui`` function on ``sphere_ui``, passing in the number of spheres as an argument to the function.

.. note:: We will add the code for ``sphere_ui`` later in this tutorial!

Now the ``Sphere_Target`` is ready to be used, but we don't have any way to destroy it. Let's fix that by adding some special :ref:`RigidBody <class_RigidBody>`-based nodes
that can damage the targets.


Adding a pistol
---------------

Let's add a pistol as the first interactable :ref:`RigidBody <class_RigidBody>` node. Open up ``Pistol.tscn``, which you can find in the ``Scenes`` folder.

Let's quickly go over a few things of note in ``Pistol.tscn`` real quick before we add the code.

All of the nodes in ``Pistol.tscn`` expect the root node are rotated. This is so the pistol is in the correct rotation relative to the VR controller when it is picked up. The root node
is a :ref:`RigidBody <class_RigidBody>` node, which we need because we're going to use the ``VR_Interactable_Rigidbody`` class we created in the last part of this tutorial series.

There is a :ref:`MeshInstance <class_MeshInstance>` node called ``Pistol_Flash``, which is a simple mesh that we will be using to simulate the muzzle flash on the end of the pistol's barrel.
A :ref:`MeshInstance <class_MeshInstance>` node called ``LaserSight`` is used to as a guide for aiming the pistol, and it follows the direction of the :ref:`Raycast <class_Raycast>` node,
called ``Raycast``, that the pistol uses to detect if its 'bullet' hit something. Finally, there is an :ref:`AudioStreamPlayer3D <class_AudioStreamPlayer3D>` node at the end of the
pistol that we will use to play the sound of the pistol firing.

Feel free to look at the other parts of the scene if you want. Most of the scene is fairly straightforward, with the major changes mentioned above. Select the :ref:`RigidBody <class_RigidBody>`
node called ``Pistol`` and make a new script called ``Pistol.gd``. Add the following code:

.. tabs::
 .. code-tab:: gdscript GDScript
    
    extends VR_Interactable_Rigidbody

    var flash_mesh
    const FLASH_TIME = 0.25
    var flash_timer = 0

    var laser_sight_mesh
    var pistol_fire_sound

    var raycast
    const BULLET_DAMAGE = 20
    const COLLISION_FORCE = 1.5


    func _ready():
        flash_mesh = get_node("Pistol_Flash")
        flash_mesh.visible = false
        
        laser_sight_mesh = get_node("LaserSight")
        laser_sight_mesh.visible = false
        
        raycast = get_node("RayCast")
        pistol_fire_sound = get_node("AudioStreamPlayer3D")


    func _physics_process(delta):
        if flash_timer > 0:
            flash_timer -= delta
            if flash_timer <= 0:
                flash_mesh.visible = false


    func interact():
        if flash_timer <= 0:
            
            flash_timer = FLASH_TIME
            flash_mesh.visible = true
            
            raycast.force_raycast_update()
            if raycast.is_colliding():
                
                var body = raycast.get_collider()
                var direction_vector = raycast.global_transform.basis.z.normalized()
                var raycast_distance = raycast.global_transform.origin.distance_to(raycast.get_collision_point())
                
                if body.has_method("damage"):
                    body.damage(BULLET_DAMAGE)
                elif body.has_method("apply_impulse"):
                    var collision_force = (COLLISION_FORCE / raycast_distance) * body.mass
                    body.apply_impulse((raycast.global_transform.origin - body.global_transform.origin).normalized(), direction_vector * collision_force)
            
            pistol_fire_sound.play()
            
            if controller != null:
                controller.rumble = 0.25


    func picked_up():
        laser_sight_mesh.visible = true


    func dropped():
        laser_sight_mesh.visible = false

Let's go over how this script works.


Explaining the Pistol code
^^^^^^^^^^^^^^^^^^^^^^^^^^

First, notice how instead of ``extends RigidBody``, we instead have ``extends VR_Interactable_Rigidbody``. This makes it where the pistol script extends the
``VR_Interactable_Rigidbody`` class so the VR controllers know this object can be interacted with and that the functions defined in ``VR_Interactable_Rigidbody``
can be called when this object is held by a VR controller.

Next, let's look at the class variables:

* ``flash_mesh``: A variable to hold the :ref:`MeshInstance <class_MeshInstance>` node that is used to simulate muzzle flash on the pistol.
* ``FLASH_TIME``: A constant to define how long the muzzle flash will be visible. This will also define how fast the pistol can fire.
* ``flash_timer``: A variable to hold the amount of time the muzzle flash has been visible for.
* ``laser_sight_mesh``: A variable to hold the :ref:`MeshInstance <class_MeshInstance>` node that acts as the pistol's 'laser sight'.
* ``pistol_fire_sound``: A variable to hold the :ref:`AudioStreamPlayer3D <class_AudioStreamPlayer3D>` node used for the pistol's firing sound.
* ``raycast``: A variable to hold the :ref:`Raycast <class_Raycast>` node that is used for calculating the bullet's position and normal when the pistol is fired.
* ``BULLET_DAMAGE``: A constant to define the amount of damage a single bullet from the pistol does.
* ``COLLISION_FORCE``: A constant that defines the amount of force that is applied to :ref:`RigidBody <class_RigidBody>` nodes when the pistol's bullet collides.

.. error:: TwistedTwigleg stopped editing here! Everything below this line is OLD tutorial!

Let's go over ``_ready``.

All we are doing here is getting the nodes and assigning them to the proper variables. We also make sure the flash and laser
sight meshes are invisible.

________

Next, let's look at ``_physics_process``.

Firstly, we check to see if the flash is visible. We do this by checking to see if ``flash_timer`` is more than zero. This is because ``flash_timer`` will be an inverted timer,
a timer that counts down instead of counting up.

If ``flash_timer`` is more than zero, we subtract ``delta`` from it and check to see whether it is equal to zero or less.
If it is, we make the flash mesh invisible.

This makes it where the flash mesh becomes invisible after ``FLASH_TIME`` many seconds have gone by.

________

Now, let's look at ``interact``, which is called when the trigger button on the VR controller is pressed and the pistol is being held.

Firstly, we check to see if the flash timer is less than or equal to zero. This check makes it where we cannot fire when the flash is visible, limiting how often
the pistol can fire.

If we can fire, we reset ``flash_timer`` by setting it to ``FLASH_TIME``, and we make the flash mesh visible.

We then update the :ref:`Raycast <class_Raycast>` and check to see if it is colliding with anything.

If the :ref:`Raycast <class_Raycast>` is colliding with something, we get the collider. We check to see if the collider has the ``damage`` function, and if it does, we call it.
If it does not, we then check to see if the collider has the ``apply_impulse`` function, and if it does, we call it after calculating the direction from the
:ref:`Raycast <class_Raycast>` to the collider.

Finally, regardless of whether the pistol hit something or not, we play the pistol firing sound.

________

Finally, let's look at ``picked_up`` and ``dropped``, which are called when the pistol is picked up and dropped, respectively.

All we are doing in these functions is making the laser pointer visible when the pistol is picked up, and making it invisible when the pistol is dropped.

________

.. image:: img/starter_vr_tutorial_pistol.png

With that done, go ahead and give the game a try! If you climb up the stairs and grab the pistols, you should be able to fire at the spheres and they will break!

Adding a shotgun
----------------

Let's add a different type of weapon :ref:`RigidBody <class_RigidBody>`: a shotgun. This is fairly straightforward, as almost everything is the same as the pistol.

Open up ``Shotgun.tscn``, which you can find in ``Scenes``. Notice how everything is more or less the same, but instead of a single :ref:`Raycast <class_Raycast>`,
there are five, and there is no laser pointer.
This is because a shotgun generally fires in a cone shape, and so we are going to emulate that by having several :ref:`Raycast <class_Raycast>` nodes, all rotated randomly
in a cone shape, and I removed the laser pointer so the player has to aim without knowing for sure where the shotgun is pointing.

Alright, select the ``Shotgun`` root node, the :ref:`RigidBody <class_RigidBody>` and make a new script called ``Shotgun.gd``. Add the following to ``Shotgun.gd``:

.. tabs::
 .. code-tab:: gdscript GDScript

    extends RigidBody

    onready var flash_mesh = $Shotgun_Flash
    onready var raycasts = $Raycasts

    const FLASH_TIME = 0.25
    var flash_timer = 0

    var BULLET_DAMAGE = 30

    func _ready():
        flash_mesh.visible = false

    func _physics_process(delta):
        if flash_timer > 0:
            flash_timer -= delta
            if flash_timer <= 0:
                flash_mesh.visible = false


    # Called when the interact button is pressed while the object is held.
    func interact():

        if flash_timer <= 0:

            flash_timer = FLASH_TIME
            flash_mesh.visible = true

            for raycast in raycasts.get_children():

                raycast.rotation_degrees = Vector3(90 + rand_range(10, -10), 0, rand_range(10, -10))

                raycast.force_raycast_update()
                if raycast.is_colliding():

                    var body = raycast.get_collider()

                    # If the body has the damage method, then use that; otherwise, use apply_impulse.
                    if body.has_method("damage"):
                        body.damage(raycast.global_transform, BULLET_DAMAGE)
                    elif body.has_method("apply_impulse"):
                        var direction_vector = raycast.global_transform.basis.z.normalized()
                        body.apply_impulse((raycast.global_transform.origin - body.global_transform.origin).normalized(), direction_vector * 4)

            $AudioStreamPlayer3D.play()


    func picked_up():
        pass


    func dropped():
        pass

You may have noticed this is almost exactly the same as the pistol, and indeed it is, so let's only go over what has changed.

- ``raycasts``: The node that holds all of the five :ref:`Raycast <class_Raycast>` nodes used for the shotgun's firing.

In ``_ready``, we get the ``Raycasts`` node, instead of just a single :ref:`Raycast <class_Raycast>`.

The only other change, besides there being nothing in ``picked_up`` and ``dropped``, is in ``interact``.

Now we go through each :ref:`Raycast <class_Raycast>` in ``raycasts``. We then rotate it on the X and Z axes, making within a 10 to ``-10`` cone.
From there, we process each :ref:`Raycast <class_Raycast>` like we did the single :ref:`Raycast <class_Raycast>` in the pistol, nothing changed at all,
we are just doing it five times, once for each :ref:`Raycast <class_Raycast>` in ``raycasts``.

________

Now you can find and fire the shotgun too! The shotgun is located around the back behind one of the walls (not in the building though!).

Adding a bomb
-------------

While both of those are well and good, let's add something we can throw next — a bomb!

Open up ``Bomb.tscn``, which you will find in the ``Scenes`` folder.

First, notice how there is a rather large :ref:`Area <class_Area>` node. This is the explosion radius for the bomb. Anything within this :ref:`Area <class_Area>` will be
effected by the explosion when the bomb explodes.

The other thing to note is how there are two sets of :ref:`Particles <class_Particles>`: one for smoke coming out of the fuse, and another for the explosion itself.
Feel free to take a look at the :ref:`Particles <class_Particles>` nodes if you want!

The only thing to notice is how long the explosion :ref:`Particles <class_Particles>` node will last, their lifetime, which is 0.75 seconds. We need to know this so we can time
the removal of the bomb with the end of the explosion :ref:`Particles <class_Particles>`.

Alright, now let's write the code for the bomb. Select the ``Bomb`` :ref:`RigidBody <class_RigidBody>` node and make a new script called ``Bomb.gd``. Add the following code to
``Bomb.gd``:

.. tabs::
 .. code-tab:: gdscript GDScript

    extends RigidBody

    onready var bomb_mesh = $Bomb
    onready var explosion_area = $Area
    onready var fuse_particles = $Fuse_Particles
    onready var explosion_particles = $Explosion_Particles

    const FUSE_TIME = 4
    var fuse_timer = 0

    var EXPLOSION_DAMAGE = 100
    var EXPLOSION_TIME = 0.75
    var explosion_timer = 0
    var explode = false
    var controller = null

    func _ready():
        set_physics_process(false)

    func _physics_process(delta):

        if fuse_timer < FUSE_TIME:

            fuse_timer += delta

            if fuse_timer >= FUSE_TIME:

                fuse_particles.emitting = false
                explosion_particles.one_shot = true
                explosion_particles.emitting = true
                bomb_mesh.visible = false

                collision_layer = 0
                collision_mask = 0
                mode = RigidBody.MODE_STATIC

                for body in explosion_area.get_overlapping_bodies():
                    if body == self:
                        pass
                    else:
                        if body.has_method("damage"):
                            body.damage(global_transform.looking_at(body.global_transform.origin, Vector3(0, 1, 0)), EXPLOSION_DAMAGE)
                        elif body.has_method("apply_impulse"):
                            var direction_vector = body.global_transform.origin - global_transform.origin
                            body.apply_impulse(direction_vector.normalized(), direction_vector.normalized() * 1.8)

                explode = true
                $AudioStreamPlayer3D.play()


        if explode:

            explosion_timer += delta
            if explosion_timer >= EXPLOSION_TIME:

                explosion_area.monitoring = false

                if controller:
                    controller.held_object = null
                    controller.hand_mesh.visible = true

                    if controller.grab_mode == "RAYCAST":
                        controller.grab_raycast.visible = true

                queue_free()


    func interact():
        set_physics_process(true)
        fuse_particles.emitting = true


    func picked_up():
        pass

    func dropped():
        pass

Let's go through what this script does, starting with the class variables:

- ``bomb_mesh``: The :ref:`MeshInstance <class_MeshInstance>` used for the bomb mesh.
- ``FUSE_TIME``: The length of time for which the fuse burns.
- ``fuse_timer``: A variable for tracking how long the fuse has been burning.
- ``explosion_area``: The :ref:`Area <class_Area>` node used for detecting what nodes are inside the explosion.
- ``EXPLOSION_DAMAGE``: The amount of damage the explosion does.
- ``EXPLOSION_TIME``: The length of time the explosion :ref:`Particles <class_Particles>` take (you can calculate this number by multiplying the particles ``lifetime`` by its ``speed scale``)
- ``explosion_timer``: A variable for tracking how long the explosion has lasted.
- ``explode``: A boolean for tracking whether the bomb has exploded.
- ``fuse_particles``: The fuse :ref:`Particles <class_Particles>` node.
- ``explosion_particles``: The explosion :ref:`Particles <class_Particles>` node.
- ``controller``: The controller that is currently holding the bomb, if there is one. This is set by the controller, so we do not need to check anything outside of checking if it is ``null``.

________

Let's go through ``_ready``.

Firstly, we get all the nodes and assign them to the proper variables for later use.

Then, we make sure ``_physics_process`` is not going to be called. We do this since we will be using ``_physics_process`` only for the fuse and
for destroying the bomb, so we do not want to trigger that early, we only want the fuse to start when the player interacts while holding a bomb.

________

Now, let's look at ``_physics_process``.

Firstly we check to see whether ``fuse_timer`` is less than ``FUSE_TIME``. If ``fuse_timer`` is less than ``FUSE_TIME``, then the bomb must be burning down the fuse.

We then add time to ``fuse_timer``, and check to see whether the bomb has waited long enough and has burned through the entire fuse.

If the bomb has waited long enough, then we need to explode the bomb. We do this first by stopping the smoke :ref:`Particles <class_Particles>` from emitting, and
making the explosion :ref:`Particles <class_Particles>` emit. We also hide the bomb mesh so it is no longer visible.

Next, we make the set the collision layer and mask to zero, and set the :ref:`RigidBody <class_RigidBody>` mode to static. This makes it where the now exploded bomb cannot
interact with the physics world, and so it will stay in place.

Then, we go through everything inside the explosion :ref:`Area <class_Area>`. We make sure the bodies inside the explosion :ref:`Area <class_Area>` are not the bomb itself, since we
do not want to explode the bomb with itself. We then check to see whether the bodies have the ``damage`` method/function, and if it does, we call that, while if it does not, we check to
see if it has the ``apply_impulse`` method/function, and call that instead.

Then, we set ``explode`` to true since the bomb has exploded, and we play a sound.

Next, we check to see if the bomb has exploded, as we need to wait until the explosion :ref:`Particles <class_Particles>` are done.

If the bomb has exploded, we add time to ``explosion_timer``. We then check to see if the explosion :ref:`Particles <class_Particles>` are done. If they are, we set the explosion
:ref:`Area <class_Area>`'s monitoring property to ``false`` to ensure we do not get any bugs in the debugger, we make the controller drop the bomb if it is holding onto it,
we make the grab :ref:`Raycast <class_Raycast>` visible if the grab mode is ``RAYCAST``, and we free/destroy the bomb using ``queue_free``.

________

Finally, let's look at ``interact``.

All we are doing here is making it where ``_physics_process`` will be called, which will start the fuse.
We also make the fuse :ref:`Particles <class_Particles>` start emitting, so smoke comes out the top of the bomb.

________

With that done, the bombs are ready to go! You can find them in the orange building. Because of how we are calculating velocity, it is easiest to throw bombs in a trusting-like
motion as opposed to a more natural throwing like motion. The smooth curve of a throwing-like motion is harder to track, and the because of how we are tracking velocity, it does
not always work.

Adding a sword
--------------

Finally, let's add a sword so we can slice through things!

Open up ``Sword.tscn``, which you will find in ``Scenes``.

There is not a whole lot to note here, but there is just one thing, and that is how the length of the blade of the sword is broken into several small :ref:`Area <class_Area>` nodes.
This is because we need to roughly know where on the blade the sword collided, and this is the easiest (and only) way I could figure out how to do this.

.. tip:: If you know how to find the point where an :ref:`Area <class_Area>` and a :ref:`CollisionObject <class_CollisionObject>` meet, please let me know and/or make a PR on the
         Godot documentation! This method of using several small :ref:`Area <class_Area>` nodes works okay, but it is not ideal.

Other than that, there really is not much of note, so let's write the code. Select the ``Sword`` root node, the :ref:`RigidBody <class_RigidBody>` and make a new script called
``Sword.gd``. Add the following code to ``Sword.gd``:

.. tabs::
 .. code-tab:: gdscript GDScript

    extends RigidBody

    const SWORD_DAMAGE = 20

    var controller

    func _ready():
        $Damage_Area_01.connect("body_entered", self, "body_entered_sword", ["01"])
        $Damage_Area_02.connect("body_entered", self, "body_entered_sword", ["02"])
        $Damage_Area_03.connect("body_entered", self, "body_entered_sword", ["03"])
        $Damage_Area_04.connect("body_entered", self, "body_entered_sword", ["04"])


    # Called when the interact button is pressed while the object is held.
    func interact():
        pass


    # Called when the object is picked up.
    func picked_up():
        pass


    # Called when the object is dropped.
    func dropped():
        pass


    func body_entered_sword(body, number):
        if body == self:
            pass
        else:

            var sword_part = null
            if number == "01":
                sword_part = get_node("Damage_Area_01")
            elif number == "02":
                sword_part = get_node("Damage_Area_02")
            elif number == "03":
                sword_part = get_node("Damage_Area_03")
            elif number == "04":
                sword_part = get_node("Damage_Area_04")

            if body.has_method("damage"):
                body.damage(sword_part.global_transform.looking_at(body.global_transform.origin, Vector3(0, 1, 0)), SWORD_DAMAGE)

                get_node("AudioStreamPlayer3D").play()

           elif body.has_method("apply_impulse"):

                var direction_vector = sword_part.global_transform.origin - body.global_transform.origin

                if not controller:
                    body.apply_impulse(direction_vector.normalized(), direction_vector.normalized() * self.linear_velocity)
                else:
                    body.apply_impulse(direction_vector.normalized(), direction_vector.normalized() * controller.controller_velocity)

                $AudioStreamPlayer3D.play()

Let's go over what this script does, starting with the two class variables:

- ``SWORD_DAMAGE``: The amount of damage a single sword slice does.
- ``controller``: The controller that is holding the sword, if there is one. This is set by the controller, so we do not need to set it here, in ``Sword.gd``.

________

Let's go over ``_ready`` next.

All we are doing here is connecting each of the :ref:`Area <class_Area>` nodes ``body_entered`` signal to the ``body_entered_sword`` function, passing in an additional argument,
which will be the number of the damage :ref:`Area <class_Area>`, so we can figure out where on the sword the body collided.

________

Now let's go over ``body_entered_sword``.

Firstly, we make sure the body the sword has collided with is not itself.

Then we figure out which part of the sword the body collided with, using the passed-in number.

Next, we check to see whether the body the sword collided with has the ``damage`` function, and if it does, we call it and play a sound.

If it does not have the damage function, we then check to see whether it has the ``apply_impulse`` function. If it does, we then calculate the direction from the sword part the
body collided with to the body. We then check to see whether the sword is being held or not.

If the sword is not being held, we use the :ref:`RigidBody <class_RigidBody>`'s velocity as the force in ``apply_impulse``, while if the sword is being held, we use the
controller's velocity as the force in the impulse.

Finally, we play a sound.

________

.. image:: img/starter_vr_tutorial_sword.png

With that done, you can now slice through the targets! You can find the sword in the corner in between the shotgun and the pistol.

Updating the target UI
----------------------

Okay, let's update the UI as the sphere targets are destroyed.

Open up ``Game.tscn`` and then expand the ``GUI`` :ref:`MeshInstance <class_MeshInstance>`. From there, expand the ``GUI`` :ref:`Viewport <class_Viewport>` node
and then select the ``Base_Control`` node. Add a new script called ``Base_Control``, and add the following:

.. tabs::
 .. code-tab:: gdscript GDScript

    extends Control

    var sphere_count_label = $Label_Sphere_Count

    func _ready():
        get_tree().root.get_node("Game").sphere_ui = self

    func update_ui(sphere_count):
        if sphere_count > 0:
            sphere_count_label.text = str(sphere_count) + " Spheres remaining"
        else:
            sphere_count_label.text = "No spheres remaining! Good job!"

Let's go over what this script does.

First, in ``_ready``, we get the :ref:`Label <class_Label>` that shows how many spheres are left and assign it to the ``sphere_count_label`` class variable.
Next, we get ``Game.gd`` by using ``get_tree().root`` and assign ``sphere_ui`` to this script.

In ``update_ui``, we change the sphere :ref:`Label <class_Label>`'s text. If there is at least one sphere remaining, we change the text to show how many spheres are still
left in the world. If there are no more spheres remaining, we change the text and congratulate the player.

Adding the final special RigidBody
----------------------------------

Finally, before we finish this tutorial, let's add a way to reset the game while in VR.

Open up ``Reset_Box.tscn``, which you will find in ``Scenes``. Select the ``Reset_Box`` :ref:`RigidBody <class_RigidBody>` node and make a new script called ``Reset_Box.gd``.
Add the following code to ``Reset_Box.gd``:

.. tabs::
 .. code-tab:: gdscript GDScript

    extends RigidBody

    var start_transform

    var reset_timer = 0
    const RESET_TIME = 120


    func _ready():
        start_transform = global_transform


    func _physics_process(delta):
        reset_timer += delta
        if reset_timer >= RESET_TIME:
            global_transform = start_transform
            reset_timer = 0


    # Called when the interact button is pressed while the object is held.
    func interact():
        get_tree().change_scene("res://Game.tscn")


    # Called when the object is picked up.
    func picked_up():
        pass


    # Called when the object is dropped.
    func dropped():
        global_transform = start_transform
        reset_timer = 0

Let's go over what this does.

First, we get the starting global :ref:`Transform <class_Transform>` in ``_ready``, and assign it to ``start_transform``. We will use this to reset the position of the reset box every so often.

In ``_physics_process``, we check to see if enough time has passed to reset. If it has, we reset the box's :ref:`Transform <class_Transform>` and then reset the timer.

If the player interacts while holding the reset box, we reset the scene by calling ``get_tree().change_scene`` and passing in the path to the current scene. This resets/restarts
the scene completely.

When the reset box is dropped, we reset the :ref:`Transform <class_Transform>` and timer.

________

With that done, when you grab and interact with the reset box, the entire scene will reset/restart and you can destroy all the targets again!

Final notes
-----------

.. image:: img/starter_vr_tutorial_sword.png

Whew! That was a lot of work. Now you have a  fully working VR project!

.. warning:: You can download the finished project for this tutorial series on the Godot OpenVR GitHub repository, under the releases tab!

This will hopefully serve as an introduction to making fully-featured VR games in Godot! The code written here can be expanded to make puzzle games, action games,
story-based games, and more!
