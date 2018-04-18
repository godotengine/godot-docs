.. _doc_fps_tutorial_part_six:

Part 6
======

Part Overview
-------------

In this part we're going to add a main menu and pause menu,
add a respawn system for the player, and change/move the sound system so we can use it from any script.

This is the last part of the FPS tutorial, by the end of this you will have a solid base to build amazing FPS games with Godot!

.. image:: img/FinishedTutorialPicture.png

.. error:: TODO: replace this image

.. note:: You are assumed to have finished :ref:`doc_fps_tutorial_part_five` before moving on to this part of the tutorial.
          
          The finished project from :ref:`doc_fps_tutorial_part_four` will be the starting project for part 6
          
Let's get started!

Adding the main menu
--------------------

First, open up ``Main_Menu.tscn`` and take a look at how the scene is set up.

The main menu is broken up into three different panels, each representing a different
'screen' of our main menu.

.. note:: The ``Background_Animation`` node is just so the background of the menu is a bit more interesting than a solid color.
          It's just a camera looking around the skybox, nothing fancy.

Feel free to expand all of the nodes and see how their set up. Just remember to keep only ``Start_Menu`` visible
when you're done, as that's the screen we want to show first when we enter the main menu.

Select ``Main_Menu`` (the root node) and create a new script called ``Main_Menu.gd``. Add the following:

::
    
    extends Control

    var start_menu
    var level_select_menu
    var options_menu

    export (String, FILE) var testing_area_scene
    export (String, FILE) var space_level_scene
    export (String, FILE) var ruins_level_scene

    func _ready():
        start_menu = $Start_Menu
        level_select_menu = $Level_Select_Menu
        options_menu = $Options_Menu
        
        $Start_Menu/Button_Start.connect("pressed", self, "start_menu_button_pressed", ["start"])
        $Start_Menu/Button_Open_Godot.connect("pressed", self, "start_menu_button_pressed", ["open_godot"])
        $Start_Menu/Button_Options.connect("pressed", self, "start_menu_button_pressed", ["options"])
        $Start_Menu/Button_Quit.connect("pressed", self, "start_menu_button_pressed", ["quit"])
        
        $Level_Select_Menu/Button_Back.connect("pressed", self, "level_select_menu_button_pressed", ["back"])
        $Level_Select_Menu/Button_Level_Testing_Area.connect("pressed", self, "level_select_menu_button_pressed", ["testing_scene"])
        $Level_Select_Menu/Button_Level_Space.connect("pressed", self, "level_select_menu_button_pressed", ["space_level"])
        $Level_Select_Menu/Button_Level_Ruins.connect("pressed", self, "level_select_menu_button_pressed", ["ruins_level"])
        
        $Options_Menu/Button_Back.connect("pressed", self, "options_menu_button_pressed", ["back"])
        $Options_Menu/Button_Fullscreen.connect("pressed", self, "options_menu_button_pressed", ["fullscreen"])
        $Options_Menu/Check_Button_VSync.connect("pressed", self, "options_menu_button_pressed", ["vsync"])
        $Options_Menu/Check_Button_Debug.connect("pressed", self, "options_menu_button_pressed", ["debug"])
        
        Input.set_mouse_mode(Input.MOUSE_MODE_VISIBLE)
        
        var globals = get_node("/root/Globals")
        $Options_Menu/HSlider_Mouse_Sensitivity.value = globals.mouse_sensitivity
        $Options_Menu/HSlider_Joypad_Sensitivity.value = globals.joypad_sensitivity


    func start_menu_button_pressed(button_name):
        if button_name == "start":
            level_select_menu.visible = true
            start_menu.visible = false
        elif button_name == "open_godot":
            OS.shell_open("https://godotengine.org/")
        elif button_name == "options":
            options_menu.visible = true
            start_menu.visible = false
        elif button_name == "quit":
            get_tree().quit()


    func level_select_menu_button_pressed(button_name):
        if button_name == "back":
            start_menu.visible = true
            level_select_menu.visible = false
        elif button_name == "testing_scene":
            set_mouse_and_joypad_sensitivity()
            get_node("/root/Globals").load_new_scene(testing_area_scene)
        elif button_name == "space_level":
            set_mouse_and_joypad_sensitivity()
            get_node("/root/Globals").load_new_scene(space_level_scene)
        elif button_name == "ruins_level":
            set_mouse_and_joypad_sensitivity()
            get_node("/root/Globals").load_new_scene(ruins_level_scene)


    func options_menu_button_pressed(button_name):
        if button_name == "back":
            start_menu.visible = true
            options_menu.visible = false
        elif button_name == "fullscreen":
            OS.window_fullscreen = !OS.window_fullscreen
        elif button_name == "vsync":
            OS.vsync_enabled = $Options_Menu/Check_Button_VSync.pressed
        elif button_name == "debug":
            pass


    func set_mouse_and_joypad_sensitivity():
        var globals = get_node("/root/Globals")
        globals.mouse_sensitivity = $Options_Menu/HSlider_Mouse_Sensitivity.value
        globals.joypad_sensitivity = $Options_Menu/HSlider_Joypad_Sensitivity.value


Most of the code here relates to making UIs, which is really outside of the purpose of this tutorial series.
**We're only going to look at the UI related code briefly.**

.. tip:: See :ref:`doc_ui_main_menu` and the tutorials following for better ways to make GUIs and UIs!

Let's look at the global variables first.

* ``start_menu``: A variable to hold the ``Start_Menu`` :ref:`Panel <class_Panel>`.
* ``level_select_menu``: A variable to hold the ``Level_Select_Menu`` :ref:`Panel <class_Panel>`.
* ``options_menu``: A variable to hold the ``Options_Menu`` :ref:`Panel <class_Panel>`.
* ``testing_area_scene``: The path to the ``Testing_Area.tscn`` file, so we can change to it from this scene.
* ``space_level_scene``: The path to the ``Space_Level.tscn`` file, so we can change to it from this scene.
* ``ruins_level_scene``: The path to the ``Ruins_Level.tscn`` file, so we can change to it from this scene.

.. warning:: You'll have to set the paths to the correct files in the editor before testing this script! Otherwise it will not work!

______

Now let's go over ``_ready``

First we get all of the :ref:`Panel <class_Panel>` nodes and assign them to the proper variables.

Next we connect all of the buttons ``pressed`` signals to their respective ``[panel_name_here]_button_pressed`` functions.

We then set the mouse mode to ``MOUSE_MODE_VISIBLE`` to ensure whenever we return to this scene our mouse will be visible.

Then we get a singleton, called ``Globals``. We then set the values for the :ref:`HSlider <class_HSlider>` nodes so their values line up with the mouse and joypad sensitivity
in the singleton.

.. note:: We have not made the ``Globals`` singleton yet, so don't worry! We're going to make it soon!

______

In ``start_menu_pressed``, we check to see which button is pressed.

Based on the button pressed, we either change the currently visible panel, quit the application, or open the Godot engine website.

______

In ``level_select_menu_button_pressed``, we check to see which button is pressed.

If the ``back`` button has been pressed, we change the currently visible panels so we return to the main menu.

If one of the scene changing buttons are pressed, we fist call ``set_mouse_and_joypad_sensitivity`` so our singleton has the values from the :ref:`HSlider <class_HSlider>` nodes.
Then we tell the singleton to change nodes using it's ``load_new_scene`` function, passing in the file path of the scene we're wanting to change to.

.. note:: Don't worry about the singleton, we'll get there soon!

______

In ``options_menu_button_pressed``, we check to see which button is pressed.

If the ``back`` button has been pressed, we change the currently visible panels so we return to the main menu.

If the ``fullscreen`` button is pressed we toggle the :ref:`OS <class_OS>`'s full screen mode by setting it to the flipped version of it's current value.

If the ``vsync`` button is pressed we set the :ref:`OS <class_OS>`'s Vsync based on the state of the Vsync check button.

______

Finally, lets take a look at ``set_mouse_and_joypad_sensitivity``.

First we get the ``Globals`` singleton and assign it to a local variable.

We then set the ``mouse_sensitivity`` and ``joypad_sensitvity`` variables to the values in their respective :ref:`HSlider <class_HSlider>` node counterparts.

Making the ``Globals`` singleton
--------------------------------

Now, for this all to work we really need to make the ``Globals`` singleton. Make a new script in the ``Script`` tab and call it ``Globals.gd``.

Add the following to ``Globals.gd``.

::
    
    extends Node

    var mouse_sensitivity = 0.08
    var joypad_sensitivity = 2

    func _ready():
        pass

    func load_new_scene(new_scene_path):
        # Change scenes
        get_tree().change_scene(new_scene_path)

As you can see, it's really quite small and simple. As this part progresses we will
keeping adding complexities to ``Global.gd``, but for now all it really is doing is holding two variables for us, and abstracting how we change scenes.

* ``mouse_sensitivity``: The current sensitivity for our mouse, so we can load it in ``Player.gd``.
* ``joypad_sensitivity``: The current sensitivity for our joypad, so we can load it in ``Player.gd``.

Right now all we're using ``Globals.gd`` for is a way to carry variables across scenes. Because the sensitivity for our mouse and joypad are
stored in ``Globals.gd``, any changes we make in one scene (like ``Main_Menu``) effect the sensitivity for our player.

All we're doing in ``load_new_scene`` is calling :ref:`SceneTree <class_SceneTree>`'s ``change_scene`` function, passing in the scene path given in ``load_new_scene``.

That's all of the code needed for ``Globals.gd`` right now! Before we can test the main menu, we first need to set ``Globals.gd`` as an autoload script.

Open up the project settings and click the ``AutoLoad`` tab.

.. Error:: add picture here!

Then select the path to ``Globals.gd`` in the ``Path`` field by clicking the button beside it. Make sure the name in the ``Node Name`` field is ``Globals``. If you
have everything like the picture below, then press ``Add``!

This will make ``Globals.gd`` a singleton/autoload script, which will allow us to access it from anywhere in any scene.

.. tip:: For more information on singleton/autoload scripts, see :ref:`doc_singletons_autoload`.

Now that ``Globals.gd`` is a singleton/autoload script, you can test the main menu!

You may also want to change the main scene from ``Testing_Area.tscn`` to ``Main_Menu.tscn`` so when we export the game we start at the main menu. You can do this
through the project settings, under the ``General`` tab. Then in the ``Application`` category, click the ``Run`` subcategory and you can change the main scene by changing
the value in ``Main Scene``.

.. warning:: You'll have to set the paths to the correct files in ``Main_Menu`` in the editor before testing the main menu!
            Otherwise you will not be able to change scenes from the level select menu/screen.

Adding the debug menu
---------------------

Now let's add a simple debugging scene so we can track things like FPS in game. Open up ``Debug_Display.tscn``.

You can see it's a :ref:`Panel <class_Panel>` positioned in the top right corner of the screen. It has three :ref:`Labels <class_Label>`,
one for displaying the FPS the game is running at, one for showing what OS the game is running on, and a label for showing the Godot version the game is running with.

Let's add the code needed to fill these :ref:`Labels <class_Label>`. Select ``Debug_Display`` and create a new script called ``Debug_Display.gd``. Add the following:

::
    
    extends Control

    func _ready():
        $OS_Label.text = "OS:" + OS.get_name()
        $Engine_Label.text = "Godot version:" + Engine.get_version_info()["string"]

    func _process(delta):
        $FPS_Label.text = "FPS:" + str(Engine.get_frames_per_second())

Let's go over what this script does.

______

In ``_ready`` we set the ``OS_Label``'s text to the name provided in :ref:`OS <class_OS>` using the ``get_name`` function. This will return the
name of the OS (or Operating System) that Godot was compiled for. For example, when you are running Windows it will return ``Windows``, while when you
are running Linux it will return ``X11``.

Then we set the ``Engine_Label``'s text to the version info provided by ``Engine.get_version_info``. ``Engine.get_version_info`` returns a dictionary full
of useful information about the version Godot is currently running with. We only care for the string version for the purposes of this display, so we get the string
and assign that as the ``text`` in ``Engine_Label``. See :ref:`Engine <class_Engine>` for more information on the values ``get_version_info`` returns.

In ``_process`` we set the text of the ``FPS_Label`` to ``Engine.get_frames_per_second``, but because ``get_frames_per_second`` returns a int, we have to cast
it to a string using ``str`` before we can add it to our label.

______

Now let's jump back to ``Main_Menu.gd`` and change the following in ``options_menu_button_pressed``:

::
    
    elif button_name == "debug":
        pass

to this instead:

::
    
    elif button_name == "debug":
        get_node("/root/Globals").set_debug_display($Options_Menu/Check_Button_Debug.pressed)

This will call a new function in our singleton called ``set_debug_display``, so let's add that next!

______

Open up ``Globals.gd`` and add the following global variables:

::
    
    # ------------------------------------
    # All of the GUI/UI related variables
    
    var canvas_layer = null
    
    const DEBUG_DISPLAY_SCENE = preload("res://Debug_Display.tscn")
    var debug_display = null
    
    # ------------------------------------

* ``canvas_layer``: A canvas layer so our GUI/UI is always drawn on top.
* ``DEBUG_DISPLAY``: The debug display scene we worked on earlier.
* ``debug_display``: A variable to hold the debug display when there is one.

Now that we have our global variables defined, we need to add a few lines to ready so we have a canvas layer to use in ``canvas_layer``.
Change ``_ready`` to the following:

::
    
    func _ready():
        canvas_layer = CanvasLayer.new()
        add_child(canvas_layer)

Now in ``_ready`` we're creating a new canvas layer and adding it as a child of the autoload script.

The reason we're adding a :ref:`CanvasLayer <class_CanvasLayer>` is so all of our GUI and UI nodes we instance/spawn in ``Globals.gd``
are always drawn on top of everything else.

When adding nodes to a singleton/autoload, you have to be careful not to lose reference to any of the child nodes.
This is because nodes will not be freed/destroyed when you change scene, meaning you can run into memory problems if you are
instancing/spawning lots of nodes and are not freeing them.

______
        
Now we just need to add ``set_debug_display`` to ``Globals.gd``:

::
    
    func set_debug_display(display_on):
        if display_on == false:
            if debug_display != null:
                debug_display.queue_free()
                debug_display = null
        else:
            if debug_display == null:
                debug_display = DEBUG_DISPLAY_SCENE.instance()
                canvas_layer.add_child(debug_display)
                
Let's go over what's happening.

First we check to see if we're trying to turn on the debug display, or turn it off.

If we are turning off the display, we then check to see if ``debug_display`` is not equal to ``null``. If ``debug_display`` is not equal to ``null``, then we
most have a debug display currently active. If we have a debug display active, we free it using ``queue_free`` and then assign ``debug_display`` to ``null``.

If we are turning on the display, we then check to make sure we do not already have a debug display active. We do this by making sure ``debug_display`` is equal to ``null``.
If ``debug_display`` is ``null``, we instance a new ``DEBUG_DISPLAY_SCENE``, and add it as a child of ``canvas_layer``.

______

With that done, we can now toggle the debug display on and off by switching the :ref:`CheckButton <class_CheckButton>` in the ``Options_Menu`` panel. Go give it a try!

Notice how the debug display stays even when you change scenes from the ``Main_Menu.tscn`` to another scene (like ``Testing_Area.tscn``). This is the beauty of
instancing/spawning nodes in a singleton/autoload and adding them as children to the singleton/autoload. Any of the nodes added as children of the singleton/autoload will
stay for as long as the game is running, without any additional work on our part!

Adding a pause menu
-------------------

Let's add a pause menu so we can return to the main menu when we press the ``ui_cancel`` action.

Open up ``Pause_Popup.tscn``.

Notice how the root node in ``Pause_Popup`` is a :ref:`WindowDialog <class_WindowDialog>`. :ref:`WindowDialog <class_WindowDialog>` inherits from
:ref:`Popup <class_Popup>`, which means :ref:`WindowDialog <class_WindowDialog>` can act like a popup.

Select ``Pause_Popup`` and scroll down all the way till you get to the ``Pause`` menu in the inspector. Notice how the pause mode is set to
``process`` instead of ``inherit`` like it is normally set by default. This makes it where it will continue to process even when the game is paused,
which we need in order to interact with the UI elements.

Now that we've looked at how ``Pause_Popup.tscn`` is set up, lets write the code to make it work. Normally we'd attach a script to the root node of
the scene, ``Pause_Popup`` in this case, but since we'll be needed to receive a couple signals in ``Globals.gd``, we'll write all of the code for
the pop up there.

Open up ``Globals.gd`` and add the following global variables:

::
    
    const MAIN_MENU_PATH = "res://Main_Menu.tscn"
    const POPUP_SCENE = preload("res://Pause_Popup.tscn")
    var popup = null

* ``MAIN_MENU_PATH``: The path to the main menu scene.
* ``POPUP_SCENE``: The pop up scene we looked at earlier.
* ``popup``: A variable to hold the pop up scene.

Now we need to add ``_process`` to ``Globals.gd`` so we can respond when the ``ui_cancel`` action is pressed.
Add the following to ``_process``:

::
    
    func _process(delta):
        if Input.is_action_just_pressed("ui_cancel"):
            if popup == null:
                popup = POPUP_SCENE.instance()
                
                popup.get_node("Button_quit").connect("pressed", self, "popup_quit")
                popup.connect("popup_hide", self, "popup_closed")
                popup.get_node("Button_resume").connect("pressed", self, "popup_closed")
                
                canvas_layer.add_child(popup)
                popup.popup_centered()
                
                Input.set_mouse_mode(Input.MOUSE_MODE_VISIBLE)
                
                get_tree().paused = true

Let's go over what's happening here.

______

First we check to see if the ``ui_cancel`` action is pressed. Then we check to make sure we do not already
have a ``popup`` open by checking to see if ``popup`` is equal to ``null``.

If we do not have a pop up open, we instance ``POPUP_SCENE`` and assign it to ``popup``.

We then get the quit button and assign it's ``pressed`` signal to ``popup_quit``, which we will be adding shortly.

Next we assign both the ``popup_hide`` signal from the :ref:`WindowDialog <class_WindowDialog>` and the ``pressed`` signal from the resume button
to ``popup_closed``, which we will be adding shortly.

Then we add ``popup`` as a child of ``canvas_layer`` so it's drawn on top. We then tell ``popup`` to pop up at the center of the screen using ``popup_centered``.

Next we make sure the mouse mode is ``MOUSE_MODE_VISIBLE`` to we can interact with the pop up. If we did not do this, we would not be able to interact with the pop up
in any scene where the mouse mode is ``MOUSE_MODE_CAPTURED``.

Finally, get pause the entire :ref:`SceneTree <class_SceneTree>`.

.. note:: For more information on pausing in Godot, see :ref:`doc_pausing_games`

______

Now we need to add the functions we've connected the signals to. Let's add ``popup_closed`` first.

Add the following to ``Globals.gd``:

::
    
    func popup_closed():
        get_tree().paused = false

        if popup != null:
            popup.queue_free()
            popup = null
            
``popup_closed`` will resume the game and destroy the pop up if there is one.
    
``popup_quit`` is very similar, but we're also making sure the mouse is visible and changing scenes to the title screen.

Add the following to ``Globals.gd``:

::
    
    func popup_quit():
        get_tree().paused = false

        Input.set_mouse_mode(Input.MOUSE_MODE_VISIBLE)

        if popup != null:
            popup.queue_free()
            popup = null

        load_new_scene(MAIN_MENU_PATH)
        
``popup_quit`` will resume the game, set the mouse mode to ``MOUSE_MODE_VISIBLE`` to ensure the mouse is visible in the main menu, destroy
the pop up if there is one, and change scenes to the main menu.

______

Before we're ready to test the pop up, we should change one thing in ``Player.gd``.

Open up ``Player.gd`` and in ``process_input``, change the code for capturing/freeing the cursor to the following:

::
    
    if Input.get_mouse_mode() == Input.MOUSE_MODE_VISIBLE:
		Input.set_mouse_mode(Input.MOUSE_MODE_CAPTURED)

Now instead of capturing/freeing the mouse, we check to see if the current mouse mode is ``MOUSE_MODE_VISIBLE``. If it is, we set it back to
``MOUSE_MODE_CAPTURED``.

Because the pop up makes the mouse mode ``MOUSE_MODE_VISIBLE`` whenever you pause, we no longer have to worry about freeing the cursor in ``Player.gd``.

______

Now the pause menu pop up is finished. You can now pause at any point in the game and return to the main menu!

Starting the respawn system
---------------------------

Since our player can lose all their health, it would be ideal if our players died and respawned too, so let's add that!

First, open up ``Player.tscn`` and expand ``HUD``. Notice how there's a :ref:`ColorRect <class_ColorRect>` called ``Death_Screen``.
When the player dies, we're going to make ``Death_Screen`` visible, and show them how long they have to wait before they're able to respawn.

Open up ``Player.gd`` and add the following global variables:

::
    
    const RESPAWN_TIME = 4
    var dead_time = 0
    var is_dead = false
    
    var globals

* ``RESPAWN_TIME``: The amount of time (in seconds) it takes to respawn.
* ``dead_time``: A variable to track how long the player has been dead.
* ``is_dead``: A variable to track whether or not the player is currently dead.
* ``globals``: A variable to hold the ``Globals.gd`` singleton.

______

We now need to add a couple lines to ``_ready``, so we can use ``Globals.gd``. Add the following to ``_ready``:

::
    
    globals = get_node("/root/Globals")
	global_transform.origin = globals.get_respawn_position()
    

Now we're getting the ``Globals.gd`` singleton and assigning it to ``globals``. We also set our global position
using the origin from our global :ref:`Transform <class_Transform>` to the position returned by ``globals.get_respawn_position``.

.. note:: Don't worry, we'll add ``get_respawn_position`` further below!
    
______
    
Next we need to make a few changes to ``physics_process``. Change ``physics_processing`` to the following:

::
    
    func _physics_process(delta):
	
        if !is_dead:
            process_input(delta)
            process_view_input(delta)
            process_movement(delta)

        if (grabbed_object == null):
            process_changing_weapons(delta)
            process_reloading(delta)

        process_UI(delta)
        process_respawn(delta)

Now we're not processing input or movement input when we're dead. We're also now calling ``process_respawn``, but we haven't written
``process_respawn`` yet, so let's change that.

______

Let's add ``process_respawn``. Add the following to ``Player.gd``:

::
    
    func process_respawn(delta):
    
        # If we just died
        if health <= 0 and !is_dead:
            $Body_CollisionShape.disabled = true
            $Feet_CollisionShape.disabled = true
            
            changing_weapon = true
            changing_weapon_name = "UNARMED"
            
            $HUD/Death_Screen.visible = true
            
            $HUD/Panel.visible = false
            $HUD/Crosshair.visible = false
            
            dead_time = RESPAWN_TIME
            is_dead = true
            
            if grabbed_object != null:
                grabbed_object.mode = RigidBody.MODE_RIGID
                grabbed_object.apply_impulse(Vector3(0,0,0), -camera.global_transform.basis.z.normalized() * OBJECT_THROW_FORCE / 2)
                
                grabbed_object.collision_layer = 1
                grabbed_object.collision_mask = 1
                
                grabbed_object = null
        
        if is_dead:
            dead_time -= delta
            
            var dead_time_pretty = str(dead_time).left(3)
            $HUD/Death_Screen/Label.text = "You died\n" + dead_time_pretty + " seconds till respawn"
            
            if dead_time <= 0:
                global_transform.origin = globals.get_respawn_position()
                
                $Body_CollisionShape.disabled = false
                $Feet_CollisionShape.disabled = false
                
                $HUD/Death_Screen.visible = false
                
                $HUD/Panel.visible = true
                $HUD/Crosshair.visible = true
                
                for weapon in weapons:
                    var weapon_node = weapons[weapon]
                    if weapon_node != null:
                        weapon_node.reset_weapon()
                
                health = 100
                grenade_amounts = {"Grenade":2, "Sticky Grenade":2}
                current_grenade = "Grenade"
                
                is_dead = false

Let's go through what this function is doing.

______

First we check to see if we just died by checking to see if ``health`` is equal or less than ``0`` and ``is_dead`` is ``false``.

If we just died, we disable our collision shapes for the player. We do this to make sure we're not blocking anything with our dead body.

We next set ``changing_weapon`` to ``true`` and set ``changing_weapon_name`` to ``UNARMED``. This is so if we are using a weapon, we put it away
when we die.

We then make the ``Death_Screen`` :ref:`ColorRect <class_ColorRect>` visible so we get a nice grey overlay over everything. We then make the rest of the UI,
the ``Panel`` and ``Crosshair`` nodes, invisible.

Next we set ``dead_time`` to ``RESPAWN_TIME`` so we can start counting down how long we've been dead. We also set ``is_dead`` to ``true`` so we know we've died.

If we are holding an object when we died, we need to throw it. We first check to see if we are holding an object or not. If we are, we then throw it,
using the same code as the throwing code we added in :ref:`doc_fps_tutorial_part_five`.

______

Then we check to see if we are dead. If we are, we then remove ``delta`` from ``dead_time``.

We then make a new variable called ``dead_time_pretty``, where we convert ``dead_time`` to a string, using only the first three characters starting from the left. This gives
us a nice looking string showing how much time we have left to wait before we respawn.

We then change the :ref:`Label <class_Label>` in ``Death_Screen`` to show how much time we have left.

Next we check to see if we've waited long enough and can respawn. We do this by checking to see if ``dead_time`` is ``0`` or less.

If we have waited long enough to respawn, we set the player's position to a new respawn position provided by ``get_respawn_position``.

We then enable both of our collision shapes so the player can collide with the environment.

Next we make the ``Death_Screen`` invisible and make the rest of the UI, the ``Panel`` and ``Crosshair`` nodes, visible again.

We then go through each weapon and call it's ``reset_weapon`` function. We'll add ``reset_weapon`` soon.

Then we reset ``health`` to ``100``, ``grenade_amounts`` to it's default values, and change ``current_grenade`` to ``Grenade``.

Finally, we set ``is_dead`` to ``false``.

______

Before we leave ``Player.gd``, we need to add one quick thing to ``_input``. Add the following at the beginning of ``_input``:

::
    
    if is_dead:
		return

Now when we're dead we cannot look around with the mouse.

Finishing the respawn system
----------------------------

First let's open ``Weapon_Pistol.gd`` and add the ``reset_weapon`` function. Add the following:

::
    
    func reset_weapon():
        ammo_in_weapon = 10
        spare_ammo = 20

Now when we call ``reset_weapon``, the ammo in our weapon and the ammo in the spares will be reset to their default values.

Now let's add ``reset_weapon`` in ``Weapon_Rifle.gd``:

::
    
    func reset_weapon():
        ammo_in_weapon = 50
        spare_ammo = 100

And add the following to ``Weapon_Knife.gd``:

::
    
    func reset_weapon():
        ammo_in_weapon = 1
        spare_ammo = 1

Now our weapons will reset when we die.

______

Now we need to add a few things to ``Globals.gd``. First, add the following global variable:

::
    
    var respawn_points = null

* ``respawn_points``: A variable to hold all of the respawn points in a level

Because we're getting a random spawn point each time, we need to randomize the number generator. Add the following to ``_ready``:

::
    
    randomize()

``randomize`` will get us a new random seed so we get a (relatively) random string of numbers when we using any of the random functions.

Now let's add ``get_respawn_position`` to ``Globals.gd``:

::
    
    func get_respawn_position():
        if respawn_points == null:
            return Vector3(0, 0, 0)
        else:
            var respawn_point = rand_range(0, respawn_points.size()-1);
            return respawn_points[respawn_point].global_transform.origin;

Let's go over what this function does.

______

First we check to see if we have any ``respawn_points`` by checking to see if ``respawn_points`` is ``null`` or not.

If ``respawn_points`` is ``null``, we return a position of empty :ref:`Vector 3 <class_Vector3>` with the position ``(0, 0, 0)``.

If ``respawn_points`` is not ``null``, we then get a random number between ``0`` and the number of elements we have in ``respawn_points``, minus ``1`` since
most programming languages (including ``GDScript``) start counting from ``0`` when you are accessing elements in a list.

We then return the position of the :ref:`Spatial <class_Spatial>` node at ``respawn_point`` position in ``respawn_points``.

______

Before we're done with ``Globals.gd``. We need to add the following to ``load_new_scene``:

::
    
    respawn_points = null

We set ``respawn_points`` to ``null`` so when/if we get to a level with no respawn points, we do not respawn
at the respawn points in the level prior.

______

Now all we need is a way to set the respawn points. Open up ``Ruins_Level.tscn`` and select ``Spawn_Points``. Add a new script called
``Respawn_Point_Setter.gd`` and attach it to ``Spawn_Points``. Add the following to ``Respawn_Point_Setter.gd``:

::
    
    extends Spatial

    func _ready():
        var globals = get_node("/root/Globals")
        globals.respawn_points = get_children()
        
Now when a node with ``Respawn_Point_Setter.gd`` has it's ``_ready`` function called, all of the children
nodes of the node with ``Respawn_Point_Setter.gd``, ``Spawn_Points`` in the case of ``Ruins_Level.tscn``, we be added
to ``respawn_points`` in ``Globals.gd``.

.. warning:: Any node with ``Respawn_Point_Setter.gd`` has to be above the player in the :ref:`SceneTree <class_SceneTree>` so the respawn points are set
             before the player needs them in the player's ``_ready`` function.

______

Now when you die you'll respawn after waiting ``4`` seconds!

.. note:: No spawn points are already set up for any of the levels besides ``Ruins_Level.tscn``!
          Adding spawn points to ``Space_Level.tscn`` is left as an exercise for the reader.
                
Writing a sound system we can use anywhere
------------------------------------------

Finally, lets make a sound system so we can play sounds from anywhere, without having to use the player.

First, open up ``SimpleAudioPlayer.gd`` and change it to the following:

::
    
    extends Spatial

    var audio_node = null
    var should_loop = false
    var globals = null

    func _ready():
        audio_node = $Audio_Stream_Player
        audio_node.connect("finished", self, "sound_finished")
        audio_node.stop()
        
        globals = get_node("/root/Globals")


    func play_sound(audio_stream, position=null):
        if audio_stream == null:
            print ("No audio stream passed, cannot play sound")
            globals.created_audio.remove(globals.created_audio.find(self))
            queue_free()
            return
        
        audio_node.stream = audio_stream
        
        # If you are using a AudioPlayer3D, then uncomment these lines to set the position.
        # if position != null:
        #	audio_node.global_transform.origin = position
        
        audio_node.play(0.0)


    func sound_finished():
        if should_loop:
            audio_node.play(0.0)
        else:
            globals.created_audio.remove(globals.created_audio.find(self))
            audio_node.stop()
            queue_free()

            
There's several changes from the old version, first and foremost being we're no longer storing the sound files in ``SimpleAudioPlayer.gd`` anymore.
This is much better for performance since we're no longer loading each audio clip when we create a sound, but instead we're forcing a audio stream to be passed
in to ``play_sound``.

Another change is we have a new global variable called ``should_loop``. Instead of just destroying the audio player every time it's finished, we instead want check to
see if we are set to loop or not. This allows us to have audio like looping background music without having to spawn a new audio player with the music
when the old one is finished.

Finally, instead of being instanced/spawned in ``Player.gd``, we're instead going to be spawned in ``Globals.gd`` so we can create sounds from any scene. We now need
to store the ``Globals.gd`` singleton so when we destroy the audio player, we also remove it from a list in ``Globals.gd``.

Let's go over the changes.

______

For the global variables
we removed all of the ``audio_[insert name here]`` variables since we will instead have these passed in to.
We also added two new global variables, ``should_loop`` and ``globals``. We'll use ``should_loop`` to tell whether we want to loop when the sound has
finished, and ``globals`` will hold the ``Globals.gd`` singleton.

The only change in ``_ready`` is now we're getting the ``Globals.gd`` singleton and assigning it to ``globals``

In ``play_sound`` we now expect a audio stream, named ``audio_stream``, to be passed in, instead of ``sound_name``. Instead of checking the
sound name and setting the stream for the audio player, we instead check to make sure an audio stream was passed in. If a audio stream is not passed
in, we print an error message, remove the audio player from a list in the ``Globals.gd`` singleton called ``created_audio``, and then free the audio player.

Finally, in ``sound_finished`` we first check to see if we are supposed to loop or not using ``should_loop``. If we are supposed to loop, we play the sound
again from the start of the audio, at position ``0.0``. If we are not supposed to loop, we remove the audio player from a list in the ``Globals.gd`` singleton
called ``created_audio``, and then free the audio player.

______

Now that we've finished our changes to ``SimpleAudioPlayer.gd``, we now need to turn our attention to ``Globals.gd``. First, add the following global variables:

::
    
    # ------------------------------------
    # All of the audio files.

    # You will need to provide your own sound files.
    var audio_clips = {
        "pistol_shot":null, #preload("res://path_to_your_audio_here!")
        "rifle_shot":null, #preload("res://path_to_your_audio_here!")
        "gun_cock":null, #preload("res://path_to_your_audio_here!")
    }

    const SIMPLE_AUDIO_PLAYER_SCENE = preload("res://Simple_Audio_Player.tscn")
    var created_audio = []
    # ------------------------------------

Lets go over these global variables.

* ``audio_clips``: A dictionary holding all of the audio clips we can play.
* ``SIMPLE_AUDIO_PLAYER_SCENE``: The simple audio player scene.
* ``created_audio``: A list to hold all of the simple audio players we create

.. note:: If you want to add additional audio, you just need to add it to ``audio_clips``. No audio files are provided in this tutorial,
          so you will have to provide your own.
          
          One site I'd recommend is **GameSounds.xyz**.
          I'm using the Gamemaster audio gun sound pack included in the Sonniss' GDC Game Audio bundle for 2017.
          The tracks I've used (with some minor editing) are as follows:
          
          * gun_revolver_pistol_shot_04,
          * gun_semi_auto_rifle_cock_02,
          * gun_submachine_auto_shot_00_automatic_preview_01

______
          
Now we need to add a new function called ``play_sound`` to ``Globals.gd``:

::
    
    func play_sound(sound_name, loop_sound=false, sound_position=null):
        if audio_clips.has(sound_name):
            var new_audio = SIMPLE_AUDIO_PLAYER_SCENE.instance()
            new_audio.should_loop = loop_sound
            
            add_child(new_audio)
            created_audio.append(new_audio)
            
            new_audio.play_sound(audio_clips[sound_name], sound_position)
        
        else:
            print ("ERROR: cannot play sound that does not exist in audio_clips!")

Let's go over what this script does.

First we check to see if we have a audio clip with the name ``sound_name`` in ``audio_clips``. If we do not, we print an error message.

If we do have a audio clip with the name ``sound_name``, we then instance/spawn a new ``SIMPLE_AUDIO_PLAYER_SCENE`` and assign it to ``new_audio``.

We then set ``should_loop``, and add ``new_audio`` as a child of ``Globals.gd``.

.. note:: Remember, we have to be careful adding nodes to a singleton, since these nodes will not be destroyed when changing scenes.

We then call ``play_sound``, passing in the audio clip associated with ``sound_name``, and the sound position.

______

Before we leave ``Globals.gd``, we need to add a few lines of code to ``load_new_scene`` so when we change scenes, we destroy all of the audio.

Add the following to ``load_new_scene``:

::
    
    # Delete all of the sounds
    for sound in created_audio:
        if (sound != null):
            sound.queue_free()
    created_audio.clear()
    
Now before we change scenes we go through each simple audio player in ``created_sounds`` and free/destroy them. Once we've gone through
all of the sounds in ``created_audio``, we clear ``created_audio`` so it no longer holds any references to any of the previously created simple audio players.

______

Let's change ``create_sound`` in ``Player.gd`` to use this new system. First, remove ``simple_audio_player`` from ``Player.gd``'s global variables, since we will
no longer be directly instancing/spawning sounds from ``Player.gd``.

Now, change ``create_sound`` to the following:

::
    
    func create_sound(sound_name, position=null):
        globals.play_sound(sound_name, false, position)

Now whenever ``create_sound`` is called, we simply call ``play_sound`` in ``Globals.gd``, passing in all of the arguments we've revived.

______

Now all of the sounds in our FPS can be played from anywhere. All we have to do is get the ``Globals.gd`` singleton, and call ``play_sound``, passing in the name of the sound
we want to play, whether we want it to loop or not, and the position to play the sound from.

For example, if you want to play an explosion sound when the grenades explode you'd need to add a new sound to ``audio_clips`` in ``Globals.gd``,
get the ``Globals.gd`` singleton, and then you just need to add something like
``globals.play_sound("explosion", false, global_transform.origin)`` in the grenades
``_process`` function, right after the grenade damages all of the bodies within it's blast radius.

Final notes
-----------

.. image:: img/FinishedTutorialPicture.png

.. error:: TODO: replace this image!

Now you have a fully working single player FPS!

At this point you have a good base to build more complicated FPS games.

.. warning:: If you ever get lost, be sure to read over the code again!

             You can download the finished project for the entire tutorial **here**
             
             TODO: Add the finished project for part 6!

.. tip:: The finished project source is hosted on Github as well: https://github.com/TwistedTwigleg/Godot_FPS_Tutorial
         
         **Please note that the code in Github may or may not be in sync with the tutorial on the documentation**.
         
         The code in the documentation is likely better managed and/or more up to date.
         If you are unsure on which to use, use the project(s) provided in the documentation as they are maintained by the Godot community.

You can download all of the ``.blend`` files used in this tutorial here: :download:`Godot_FPS_BlenderFiles.zip <files/Godot_FPS_BlenderFiles.zip>`

.. error:: TODO: update the blender files!

.. note:: The finished project source files contain the same exact code, just written in a different order.
          This is because the finished project source files are what the tutorial is based on.

          The finished project code was written in the order that features were created, not necessarily
          in a order that is ideal for learning.

          Other than that, the source is exactly the same, just with helpful comments explaining what
          each part does.

All assets provided in the started assets (unless otherwise noted) were **originally created by TwistedTwigleg, with changes/additions by the Godot community.**
All original assets provided for this tutorial are released under the ``MIT`` license.

Feel free to use these assets however you want! They belong to the Godot community!
          
The skybox is created by **StumpyStrust** and can be found at OpenGameArt.org. https://opengameart.org/content/space-skyboxes-0
. The skybox is licensed under the ``CC0`` license.

The font used is **Titillium-Regular**, and is licensed under the ``SIL Open Font License, Version 1.1``.

The skybox was convert to a 360 equirectangular image using this tool: https://www.360toolkit.co/convert-cubemap-to-spherical-equirectangular.html

While no sounds are provided, you can find many game ready sounds at https://gamesounds.xyz/

.. warning:: **OpenGameArt.org, 360toolkit.co, the creator(s) of Titillium-Regular, StumpyStrust, and GameSounds.xyz are in no way involved in this tutorial.**

