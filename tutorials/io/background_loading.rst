.. _doc_background_loading:

Background loading
==================

Commonly, games need to load resources asynchronously.
When switching the main scene of your game (e.g. going to a new
level), you might want to show a loading screen with some indication
that progress is being made, or you may want to load additional resources
during gameplay.

The standard load method
(:ref:`ResourceLoader.load <class_ResourceLoader_method_load>` or GDScript's simpler
:ref:`load <class_@GDScript_method_load>`) blocks your
thread, making your game appear unresponsive while the resource is being loaded.

One way around this is using ``ResourceLoader`` to load resources asynchronously
in background threads.

Using ResourceLoader
--------------------

Generally, you queue requests to load resources for a path using
:ref:`ResourceLoader.load_threaded_request <class_ResourceLoader_method_load_threaded_request>`,
which will then be loaded in threads in the background.

You can check the status with
:ref:`ResourceLoader.load_threaded_get_status <class_ResourceLoader_method_load_threaded_get_status>`.
Progress can be obtained by passing an array variable via progress which will return
a one element array containing the percentage.

Finally, you retrieve loaded resources by calling
:ref:`ResourceLoader.load_threaded_get <class_ResourceLoader_method_load_threaded_get>`.

Once you call ``load_threaded_get()``, either the resource finished loading in
the background and will be returned instantly or the load will block at this point like
``load()`` would. If you want to guarantee this does not block,
you either need to ensure there is enough time between requesting the load and
retrieving the resource or you need to check the status manually.

Example
-------

This example demonstrates how to load a scene in the background.
We will have a button spawn a enemy when pressed.
The enemy will be ``Enemy.tscn`` which we will load on ``_ready`` and instantiate when pressed.
The path will be ``"Enemy.tscn"`` which is located at ``res://Enemy.tscn``.

First, we will start a request to load the resource and connect the button:

::

    const ENEMY_SCENE_PATH : String = "Enemy.tscn"

    func _ready():
        ResourceLoader.load_threaded_request(ENEMY_SCENE_PATH)
        self.pressed.connect(_on_button_pressed)

Now ``_on_button_pressed`` will be called when the button is pressed.
This method will be used to spawn an enemy.

::

    func _on_button_pressed(): # Button was pressed
        # Obtain the resource now that we need it
        var enemy_scene = ResourceLoader.load_threaded_get(ENEMY_SCENE_PATH)
        # Instantiate the enemy scene and add it to the current scene
        var enemy = enemy_scene.instantiate()
        add_child(enemy)
