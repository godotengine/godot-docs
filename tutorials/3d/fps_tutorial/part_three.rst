.. _doc_fps_tutorial_part_three:

Part 3
======

Part Overview
-------------

In this part we will be limiting our guns by giving them ammo. We will also
be giving the player the ability to reload, and we will be adding sounds when the
guns fire.

.. image:: img/PartThreeFinished.png

By the end of this part, the player will have limited ammo, the ability to reload,
and sounds will play when the player fires and changes weapons.

.. note:: You are assumed to have finished :ref:`doc_fps_tutorial_part_two` before moving on to this part of the tutorial.

Let's get started!


Changing levels
---------------

Now that we have a fully working FPS, let's move to a more FPS like level. Open up ``Test_Level.tscn``.
``Test_Level.tscn`` is a complete custom FPS level created for the purpose of this tutorial. Press ``F6`` to
play the open scene, or press the "play current scene button", and give it a whirl.

.. warning:: There will (likely) be the occasional random freeze as you go through the level. This is a known
             issue.

             If you find any way to solve it, please let me know on the Github repository, the Godot forums,
             or on Twitter! Be sure to include ``@TwistedTwigleg`` so I will have a greater chance of seeing it!

You might have noticed there are several boxes and cylinders placed throughout the level. They are :ref:`RigidBody <class_RigidBody>`
nodes we can place ``RigidBody_hit_test.gd`` on and then they will react to being hit with bullets, so lets do that!

Select ``Center_room`` and open it up. From there select ``Physics_objects`` and open that up. You'll find there are
``6`` crates in a seemingly random order. Go select one of them and press the "Open in Editor" button. It's the one that
looks like a little movie slide.

.. note:: The reason the objects seem to be placed in a random order is because all of the objects were copied and pasted around
          in the Godot editor to save on time. If you want to move any of the nodes around, it is highly suggested to just
          left click inside the editor viewport to get the node you want, and then move it around with the :ref:`Spatial <class_Spatial>` gizmo.

This will bring you to the crate's scene. From there, select the ``Crate`` :ref:`RigidBody <class_RigidBody>` (the one that is the root of the scene)
and scroll down in the inspector until you get to the script section. From there, click the drop down and select "Load". Chose
``RigidBody_hit_test.gd`` and then return to ``Test_Level.tscn``.

Now open ``Upper_room``, select ``Physics_objects``, and chose one of the cylinder :ref:`RigidBody <class_RigidBody>` nodes.
Press the "Open in Editor" button beside one of the cylinders. This will bring you to the cylinder's scene.

From there, select the ``Cylinder`` :ref:`RigidBody <class_RigidBody>` (the one that is the root of the scene)
and scroll down in the inspector until you get to the script section. From there, click the drop down and select "Load". Chose
``RigidBody_hit_test.gd`` and then return to ``Test_Level.tscn``.

Now you can fire at the boxes and cylinders and they will react to your bullets just like the cubes in ``Testing_Area.tscn``!


Adding ammo
-----------

Now that we've got working guns, lets give them a limited amount of ammo.

Lets define some more global variables in ``Player.gd``, ideally nearby the other gun related variables:

::

    var ammo_for_guns = {"PISTOL":60, "RIFLE":160, "KNIFE":1}
    var ammo_in_guns = {"PISTOL":20, "RIFLE":80, "KNIFE":1}
    const AMMO_IN_MAGS = {"PISTOL":20, "RIFLE":80, "KNIFE":1}


Here is what these variables will be doing for us:

- ``ammo_for_guns``: The amount of ammo we have in reserve for each weapon/gun.
- ``ammo_in_guns``: The amount of ammo currently inside the weapon/gun.
- ``AMMO_IN_MAGS``: How much ammo is in a fully filled weapon/gun.

.. note:: There is no reason we've included ammo for the knife, so feel free to remove the knife's ammo
          if you desire.

          Depending on how you program melee weapons, you may need to define an ammo count even if the
          weapon does not use ammo. Some games use extremely short range 'guns' as their melee weapons,
          and in those cases you may need to define ammo for your melee weapons.

_________

Now we need to add a few ``if`` checks to ``_physics_process``.

We need to make sure we have ammo in our gun before we try to fire a bullet.
Go find the line that checks for the fire action being pressed and add the following new
bits of code:

::

    # NOTE: You should have this if condition in your _physics_process function
    # Firing the weapons
    if Input.is_action_pressed("fire"):
        if current_gun == "PISTOL":
            if ammo_in_guns["PISTOL"] > 0: # NEW CODE
                if animation_manager.current_state == "Pistol_idle":
                    animation_manager.set_animation("Pistol_fire")

        elif current_gun == "RIFLE":
            if ammo_in_guns["RIFLE"] > 0: # NEW CODE
                if animation_manager.current_state == "Rifle_idle":
                    animation_manager.set_animation("Rifle_fire")

        elif current_gun == "KNIFE":
            if animation_manager.current_state == "Knife_idle":
                animation_manager.set_animation("Knife_fire")

These two additional ``if`` checks make sure we have a bullet to fire before setting our firing animation.

While we're still in ``_physics_process``, let's also add a way to track how much ammo we have. Find the line that
has ``UI_status_label.text = "HEALTH: " + str(health)`` in ``_physics_process`` and replace it with the following:

::

    # HUD (UI)
    if current_gun == "UNARMED" or current_gun == "KNIFE":
        UI_status_label.text = "HEALTH: " + str(health)
    else:
        UI_status_label.text = "HEALTH: " + str(health) + "\nAMMO:" + \
            str(ammo_in_guns[current_gun]) + "/" + str(ammo_for_guns[current_gun])

.. tip:: Did you now that you can combine two lines using ``\``? We're using it here
         so we do not have a extremely long line of code all on one line by splitting it
         into two lines!

This will show the player how much ammo they currently have and how much ammo they currently have in reserve, only for
the appropriate weapons (not unarmed or the knife). Regardless of the currently selected weapon/gun, we will always show
how much health the player has

.. note:: we cannot just add ``ammo_for_guns[current_gun]`` or ``ammo_in_guns[current_gun]`` to the ``string`` we
          are passing in to the :ref:`Label <class_Label>`. Instead we have to cast them from ``floats`` to ``strings``, which is what we are doing
          by using ``str()``.

          For more information on casting, see this page from wiki books:
          https://en.wikibooks.org/wiki/Computer_Programming/Type_conversion

.. warning:: We are currently not using the player's health just yet in the tutorial. We will start
             using health for the player and objects when we include turrets and targets in later parts.


Now we need to remove a bullet from the gun when we fire. To do that, we just need to add a few lines in
``fire_bullet``:

::

    func fire_bullet():
        if changing_gun == true:
            return

        # Pistol bullet handling: Spawn a bullet object!
        if current_gun == "PISTOL":
            var clone = bullet_scene.instance()
            var scene_root = get_tree().root.get_children()[0]
            scene_root.add_child(clone)

            clone.global_transform = get_node("Rotation_helper/Gun_fire_points/Pistol_point").global_transform
            # The bullet is a little too small (by default), so let's make it bigger!
            clone.scale = Vector3(4, 4, 4)

            ammo_in_guns["PISTOL"] -= 1 # NEW CODE

        # Rifle bullet handeling: Send a raycast!
        elif current_gun == "RIFLE":
                var ray = get_node("Rotation_helper/Gun_fire_points/Rifle_point/RayCast")
                ray.force_raycast_update()

                if ray.is_colliding():
                    var body = ray.get_collider()
                    if body.has_method("bullet_hit"):
                        body.bullet_hit(RIFLE_DAMAGE, ray.get_collision_point())

                ammo_in_guns["RIFLE"] -= 1 # NEW CODE

        # Knife bullet(?) handeling: Use an area!
        elif current_gun == "KNIFE":
            var area = get_node("Rotation_helper/Gun_fire_points/Knife_point/Area")
            var bodies = area.get_overlapping_bodies()

            for body in bodies:
                if body.has_method("bullet_hit"):
                    body.bullet_hit(KNIFE_DAMAGE, area.global_transform.origin)


Go play the project again! Now you'll lose ammo as you fire, until you reach zero and
cannot fire anymore.

Adding reloading
----------------

Now that we can empty our gun, we need a way to refill it!

First, let's start by
adding another global variable. Add ``var reloading_gun = false`` somewhere along with your
other global variables, preferably near the other gun related variables.

_________

Now we need to add several things to ``_physics_process``.

First, let's make sure we cannot change guns while reloading.
We need to change the weapon changing code to include the following:

::

    # Was "if changing_gun == false"
    if changing_gun == false and reloading_gun == false:
        if Input.is_key_pressed(KEY_1):
            current_gun = "UNARMED"
            changing_gun = true
        elif Input.is_key_pressed(KEY_2):
            current_gun = "KNIFE"
            changing_gun = true
        elif Input.is_key_pressed(KEY_3):
            current_gun = "PISTOL"
            changing_gun = true
        elif Input.is_key_pressed(KEY_4):
            current_gun = "RIFLE"
            changing_gun = true

Now the player cannot change guns while reloading.

_________

Ideally we want the player to be able to reload when they chose, so lets given them
the ability to reload when they press the ``reload`` action. Add the following
somewhere in ``_physics_process``, ideally nearby your other input related code:

::

    # Reloading
    if reloading_gun == false:
        if Input.is_action_just_pressed("reload"):
            if current_gun == "PISTOL" or current_gun == "RIFLE"
                if animation_manager.current_state != "Pistol_reload" and animation_manager.current_state != "Rifle_reload":
                    reloading_gun = true

First we see if the player is already reloading. If they are not, then we check if they've pressed
the reloading action. If they have pressed the ``reload`` action, we then check if they are using
a weapon that has the ability to be reloaded. Finally, we make sure they are not already
in a reloading animation. If they are not, we set ``reloading_gun`` to ``true``.

We do not want to do our reloading processing here with the input in an effort to keep game logic
separate from input logic. Keeping them separate makes the code easier to debug, and as a bonus it
keeps the input logic from being overly bloated.

_________

Finally, we need to add the code that actually handles reloading. Add the following code to ``_physics_process``,
ideally somewhere underneath the reloading input code you just inputted:

::

    # Reloading logic
    if reloading_gun == true:
        var can_reload = false

        if current_gun == "PISTOL":
            if animation_manager.current_state == "Pistol_idle":
                can_reload = true
        elif current_gun == "RIFLE":
            if animation_manager.current_state == "Rifle_idle":
                can_reload = true
        elif current_gun == "KNIFE":
            can_reload = false
            reloading_gun = false
        else:
            can_reload = false
            reloading_gun = false

        if ammo_for_guns[current_gun] <= 0 or ammo_in_guns[current_gun] == AMMO_IN_MAGS[current_gun]:
            can_reload = false
            reloading_gun = false


        if can_reload == true:
            var ammo_needed = AMMO_IN_MAGS[current_gun] - ammo_in_guns[current_gun]

            if ammo_for_guns[current_gun] >= ammo_needed:
                ammo_for_guns[current_gun] -= ammo_needed
                ammo_in_guns[current_gun] = AMMO_IN_MAGS[current_gun]
            else:
                ammo_in_guns[current_gun] += ammo_for_guns[current_gun]
                ammo_for_guns[current_gun] = 0

            if current_gun == "PISTOL":
                animation_manager.set_animation("Pistol_reload")
            elif current_gun == "RIFLE":
                animation_manager.set_animation("Rifle_reload")

            reloading_gun = false


Lets go over what this code does.

_________

First we check if ``reloading_gun`` is ``true``. If it is we then go through a series of checks
to see if we can reload or not. We use ``can_reload`` as a variable to track whether or not
it is possible to reload.

We go through series of checks for each weapon. For the pistol and the rifle we check if
we're in an idle state or not. If we are, then we set ``can_reload`` to ``true``.

For the knife we do not want to reload, because you cannot reload a knife, so we set ``can_reload`` and ``reloading_gun``
to ``false``. If we are using a weapon that we do not have a ``if`` or ``elif`` check for, we set
``can_reload`` and ``reloading_gun`` to ``false``, as we do not want to be able to reload a weapon we are unaware of.

Next we check if we have ammo in reserve for the gun in question. We also check to make sure the gun we are trying to reload
is not already full of ammo. If the gun does not have ammo in reserve or the gun is already full, we set
``can_reload`` and ``reloading_gun`` to ``false``.

If we've made it through all those checks and we can reload, then we have a few more steps to take.

First we assign the ammo we are needing to fill the gun fully to the ``ammo_needed`` variable.
We just subtract the amount of ammo we currently have in our gun by the amount of ammo in a full magazine.

Then we check if have enough ammo in reserves to fill the gun fully. If we do, we subtract the amount of ammo
we need to refill our gun from the reserves, and we set the amount of ammo in the gun to full.

If we do not have enough ammo in reserves to fill the gun, we add all of the ammo left in reserves to our
gun and then set the ammo in reserves to zero, making it empty.

Regardless of how much ammo we've added to the gun, we set our animation to the reloading animation for the current gun.

Finally, we set ``reloading_gun`` to false because we have finished reloading the gun.

_________

Go test the project again, and you'll find you can reload your gun when it is not
full and when there is ammo left in the ammo reserves.

_________

Personally, I like the guns to automatically start reloading if we try to fire them
when they have no ammo in them, so lets add that! Add the following code to the input code for
firing the guns:

::

    # Firing the weapons
    if Input.is_action_pressed("fire"):
        if current_gun == "PISTOL":
            if ammo_in_guns["PISTOL"] > 0:
                if animation_manager.current_state == "Pistol_idle":
                    animation_manager.set_animation("Pistol_fire")
            # NEW CODE!
            else:
                reloading_gun = true

        elif current_gun == "RIFLE":
            if ammo_in_guns["RIFLE"] > 0:
                if animation_manager.current_state == "Rifle_idle":
                    animation_manager.set_animation("Rifle_fire")
            # NEW CODE!
            else:
                reloading_gun = true

        elif current_gun == "KNIFE":
            if animation_manager.current_state == "Knife_idle":
                animation_manager.set_animation("Knife_fire")

Now whenever the player tries to fire the gun when it's empty, we automatically
set ``reloading_gun`` to true, which will reload the gun if possible.

Adding sounds
-------------

Finally, let's add some sounds that play when we are reloading, changing guns, and when we
are firing them.

.. tip:: There are no game sounds provided in this tutorial (for legal reasons).
         https://gamesounds.xyz/ is a collection of **"royalty free or public domain music and sounds suitable for games"**.
         I used Gamemaster's Gun Sound Pack, which can be found in the Sonniss.com GDC 2017 Game Audio Bundle.

         The video tutorial will briefly show how to edit the audio files for use in the tutorial.

Open up ``SimpleAudioPlayer.tscn``. It is simply a :ref:`Spatial <class_Spatial>` with a :ref:'AudioStreamPlayer <class_AudioStreamPlayer>' as it's child.

.. note:: The reason this is called a 'simple' audio player is because we are not taking performance into account
          and because the code is designed to provide sound in the simplest way possible. This will likely change
          in a future part.

If you want to use 3D audio, so it sounds like it's coming from a location in 3D space, right click
the :ref:'AudioStreamPlayer <class_AudioStreamPlayer>' and select "Change type".

This will open the node browser. Navigate to :ref:'AudioStreamPlayer3D <class_AudioStreamPlayer3D>' and select "change".
In the source for this tutorial, we will be using :ref:'AudioStreamPlayer <class_AudioStreamPlayer>', but you can optionally
use :ref:'AudioStreamPlayer3D <class_AudioStreamPlayer3D>' if you desire, and the code provided below will work regardless of which
one you chose.

Create a new script and call it "SimpleAudioPlayer.gd". Attach it to the :ref:`Spatial <class_Spatial>` in ``SimpleAudioPlayer.tscn``
and insert the following code:

::

    extends Spatial

    # All of the audio files.
    # You will need to provide your own sound files.
    var audio_pistol_shot = preload("res://path_to_your_audio_here")
    var audio_gun_cock = preload("res://path_to_your_audio_here")
    var audio_rifle_shot = preload("res://path_to_your_audio_here")

    var audio_node = null

    func _ready():
        audio_node = get_node("AudioStreamPlayer")
        audio_node.connect("finished", self, "destroy_self")
        audio_node.stop()


    func play_sound(sound_name, position=null):
        if sound_name == "Pistol_shot":
            audio_node.stream = audio_pistol_shot
        elif sound_name == "Rifle_shot":
            audio_node.stream = audio_rifle_shot
        elif sound_name == "Gun_cock":
            audio_node.stream = audio_gun_cock
        else:
            print ("UNKNOWN STREAM")
            queue_free()
            return

        # If you are using a AudioPlayer3D, then uncomment these lines to set the position.
        # if position != null:
        #	audio_node.global_transform.origin = position

        audio_node.play()


    func destroy_self():
        audio_node.stop()
        queue_free()


.. tip:: By setting ``position`` to ``null`` by default in ``play_sound``, we are making it an optional argument,
         meaning position doesn't necessarily have to be passed in to call the ``play_sound``.

Let's go over what's happening here:

_________

In ``_ready`` we get the :ref:'AudioStreamPlayer <class_AudioStreamPlayer>' and connect it's ``finished`` signal to ourselves.
It doesn't matter if it's :ref:'AudioStreamPlayer <class_AudioStreamPlayer>' or :ref:'AudioStreamPlayer3D <class_AudioStreamPlayer3D>' node,
as they both have the finished signal. To make sure it is not playing any sounds, we call ``stop`` on the :ref:'AudioStreamPlayer <class_AudioStreamPlayer>'.

.. warning:: Make sure your sound files are **not** set to loop! If it is set to loop
             the sounds will continue to play infinitely and the script will not work!

The ``play_sound`` function is what we will be calling from ``Player.gd``. We check if the sound
is one of the three possible sounds, and if it is we set the audio stream for our :ref:'AudioStreamPlayer <class_AudioStreamPlayer>'
to the correct sound.

If it is an unknown sound, we print an error message to the console and free ourselves.

If you are using a :ref:'AudioStreamPlayer3D <class_AudioStreamPlayer3D>', remove the ``#`` to set the position of
the audio player node so it plays at the correct position.

Finally, we tell the :ref:'AudioStreamPlayer <class_AudioStreamPlayer>' to play.

When the :ref:'AudioStreamPlayer <class_AudioStreamPlayer>' is finished playing the sound, it will call ``destroy_self`` because
we connected the ``finished`` signal in ``_ready``. We stop the :ref:'AudioStreamPlayer <class_AudioStreamPlayer>' and free ourself
to save on resources.

.. note:: This system is extremely simple and has some major flaws:
          One flaw is we have to pass in a string value to play a sound. While it is relatively simple
          to remember the names of the three sounds, it can be increasingly complex when you have more sounds.
          Ideally we'd place these sounds in some sort of container with exposed variables so we do not have
          to remember the name(s) of each sound effect we want to play.

          Another flaw is we cannot play looping sounds effects, nor background music easily with this system.
          Because we cannot play looping sounds, certain effects like footstep sounds are harder to accomplish
          because we then have to keep track of whether or not there is a sound effect *and* whether or not we
          need to continue playing it.

_________

With that done, lets open up ``Player.gd`` again.
First we need to load the ``SimpleAudioPlayer.tscn``. Place the following code in your global variables:

::

    var simple_audio_player = preload("res://SimpleAudioPlayer.tscn")

Now we just need to instance the simple audio player when we need it, and then call it's
``play_sound`` function and pass the name of the sound we want to play. To make the process simpler,
let's create a ``create_sound`` function:

::

    func create_sound(sound_name, position=null):
        var audio_clone = simple_audio_player.instance()
        var scene_root = get_tree().root.get_children()[0]
        scene_root.add_child(audio_clone)
        audio_clone.play_sound(sound_name, position)

Lets walk through what this function does:

_________

The first line instances the ``simple_audio_player.tscn`` scene and assigns it to a variable,
named ``audio_clone``.

The second line gets the scene root, using one large assumption. We first get this node's :ref:`SceneTree <class_SceneTree>`,
and then access the root node, which in this case is the :ref:`Viewport <class_Viewport>` this entire game is running under.
Then we get the first child of the :ref:`Viewport <class_Viewport>`, which in our case happens to be the root node in
``Test_Area.tscn`` or ``Test_Level.tscn``. We are making a huge assumption that the first child of the root
is the root node that our player is under, which could not always be the case.

If this doesn't make sense to you, don't worry too much about it. The second line of code only doesn't work
reliably if you have multiple scenes loaded as childs to the root node at a time, which will rarely happen for most projects. This is really
only potentially a issue depending on how you handle scene loading.

The third line adds our newly created ``SimpleAudioPlayer`` scene to be a child of the scene root. This
works exactly the same as when we are spawning bullets.

Finally, we call the ``play_sound`` function and pass in the arguments we're given. This will call
``SimpleAudioPlayer.gd``'s ``play_sound`` function with the passed in arguments.

_________

Now all that is left is playing the sounds when we want to. First, let's play the shooting sounds
when a bullet is fired. Go to ``fire_bullet`` and add the following:

::

    func fire_bullet():
        if changing_gun == true:
            return

        # Pistol bullet handling: Spawn a bullet object!
        if current_gun == "PISTOL":
            var clone = bullet_scene.instance()
            var scene_root = get_tree().root.get_children()[0]
            scene_root.add_child(clone)

            clone.global_transform = get_node("Rotation_helper/Gun_fire_points/Pistol_point").global_transform
            # The bullet is a little too small (by default), so let's make it bigger!
            clone.scale = Vector3(4, 4, 4)

            ammo_in_guns["PISTOL"] -= 1
            create_sound("Pistol_shot", clone.global_transform.origin); # NEW CODE

        # Rifle bullet handeling: Send a raycast!
        elif current_gun == "RIFLE":
            var ray = get_node("Rotation_helper/Gun_fire_points/Rifle_point/RayCast")
            ray.force_raycast_update()

            if ray.is_colliding():
                var body = ray.get_collider()
                if body.has_method("bullet_hit"):
                    body.bullet_hit(RIFLE_DAMAGE, ray.get_collision_point())

            ammo_in_guns["RIFLE"] -= 1
            create_sound("Rifle_shot", ray.global_transform.origin); # NEW CODE

        # Knife bullet(?) handeling: Use an area!
        elif current_gun == "KNIFE":
            var area = get_node("Rotation_helper/Gun_fire_points/Knife_point/Area")
            var bodies = area.get_overlapping_bodies()

            for body in bodies:
                if body.has_method("bullet_hit"):
                    body.bullet_hit(KNIFE_DAMAGE, area.global_transform.origin)

Now we will play the shooting noise for both the pistol and the rifle when a bullet is created.

.. note:: We are passing in the positions of the ends of the guns using the bullet object's
          global :ref:`Transform <class_transform>` and the :ref:`Raycast <class_raycast>`'s global :ref:`Transform <class_transform>`.
          If you are not using a :ref:`AudioStreamPlayer3D <class_AudioStreamPlayer3D>` node, you can optionally leave the positions out and only
          pass in the name of the sound you want to play.

Finally, lets play the sound of a gun being cocked when we reload and when we change weapons.
Add the following to our reloading logic section of ``_physics_process``:

::

    # Reloading logic
    if reloading_gun == true:
        var can_reload = false

        if current_gun == "PISTOL":
            if animation_manager.current_state == "Pistol_idle":
                can_reload = true
        elif current_gun == "RIFLE":
            if animation_manager.current_state == "Rifle_idle":
                can_reload = true
        elif current_gun == "KNIFE":
            can_reload = false
            reloading_gun = false
        else:
            can_reload = false
            reloading_gun = false

        if ammo_for_guns[current_gun] <= 0 or ammo_in_guns[current_gun] == AMMO_IN_MAGS[current_gun]:
            can_reload = false
            reloading_gun = false


        if can_reload == true:
            var ammo_needed = AMMO_IN_MAGS[current_gun] - ammo_in_guns[current_gun]

            if ammo_for_guns[current_gun] >= ammo_needed:
                ammo_for_guns[current_gun] -= ammo_needed
                ammo_in_guns[current_gun] = AMMO_IN_MAGS[current_gun]
            else:
                ammo_in_guns[current_gun] += ammo_for_guns[current_gun]
                ammo_for_guns[current_gun] = 0

            if current_gun == "PISTOL":
                animation_manager.set_animation("Pistol_reload")
            elif current_gun == "RIFLE":
                animation_manager.set_animation("Rifle_reload")

            reloading_gun = false
            create_sound("Gun_cock", camera.global_transform.origin) # NEW CODE

And add this code to the changing weapons section of ``_physics_process``:

::

    if changing_gun == true:
        if current_gun != "PISTOL":
            if animation_manager.current_state == "Pistol_idle":
                animation_manager.set_animation("Pistol_unequip")
        if current_gun != "RIFLE":
            if animation_manager.current_state == "Rifle_idle":
                animation_manager.set_animation("Rifle_unequip")
        if current_gun != "KNIFE":
            if animation_manager.current_state == "Knife_idle":
                animation_manager.set_animation("Knife_unequip")

        if current_gun == "UNARMED":
            if animation_manager.current_state == "Idle_unarmed":
                changing_gun = false

        elif current_gun == "KNIFE":
            if animation_manager.current_state == "Knife_idle":
                changing_gun = false
            if animation_manager.current_state == "Idle_unarmed":
                animation_manager.set_animation("Knife_equip")

        elif current_gun == "PISTOL":
            if animation_manager.current_state == "Pistol_idle":
                changing_gun = false
            if animation_manager.current_state == "Idle_unarmed":
                animation_manager.set_animation("Pistol_equip")

                create_sound("Gun_cock", camera.global_transform.origin) # NEW CODE

        elif current_gun == "RIFLE":
            if animation_manager.current_state == "Rifle_idle":
                changing_gun = false
            if animation_manager.current_state == "Idle_unarmed":
                animation_manager.set_animation("Rifle_equip")

                create_sound("Gun_cock", camera.global_transform.origin) # NEW CODE

Now whatever sound you have assigned to "Gun_cock" will play when you reload and when you
change to either the pistol or the rifle.


Final notes
-----------

.. image:: img/FinishedTutorialPicture.png

Now you have a fully working single player FPS!

You can find the completed project here: :download:`Godot_FPS_Finished.zip <files/Godot_FPS_Finished.zip>`

.. tip:: The finished project source is hosted on Github as well: https://github.com/TwistedTwigleg/Godot_FPS_Tutorial

You can also download all of the ``.blend`` files used here: :download:`Godot_FPS_BlenderFiles.zip <files/Godot_FPS_BlenderFiles.zip>`

.. note:: The finished project source files contain the same exact code, just written in a different order.
          This is because the finished project source files are what the tutorial is based on.

          The finished project code was written in the order that features were created, not necessarily
          in a order that is ideal for learning.

          Other than that, the source is exactly the same, just with helpful comments explaining what
          each part does.

The skybox is created by **StumpyStrust** and can be found at OpenGameArt.org. https://opengameart.org/content/space-skyboxes-0

The font used is **Titillium-Regular**, and is licensed under the SIL Open Font License, Version 1.1.

The skybox was convert to a 360 equirectangular image using this tool: https://www.360toolkit.co/convert-cubemap-to-spherical-equirectangular.html

While no sounds are provided, you can find many game ready sounds at https://gamesounds.xyz/

.. warning:: OpenGameArt.org, 360toolkit.co, the creator(s) of Titillium-Regular, and GameSounds.xyz are in no way involved in this tutorial.

__________

In future parts we will be adding the following:

- Adding a spawning system
- Adding grenades
- Adding turrets and targets
- Adding a sound manager
- Adding ammo and health pickups
- Refining and cleaning up the code

.. warning:: All plans are subject to change without warning!
