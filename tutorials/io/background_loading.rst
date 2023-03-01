.. _doc_background_loading:

Background loading
==================

When switching the main scene of your game (e.g. going to a new
level), you might want to show a loading screen with some indication
that progress is being made. The main load method
(``ResourceLoader::load`` or just ``load`` from GDScript) blocks your
thread, making your game appear frozen and unresponsive while the resource is being loaded. This
document discusses the alternative of using ``ResourceLoader``'s other methods class for smoother
load screens.

ResourceLoader
--------------
Usage
-----

Usage is generally as follows

Start a load request
~~~~~~~~~~~~~~~~~~~~

.. code-block:: gdscript

    func ResourceLoader.load_threaded_request(path: String, type_hint: String = "", use_sub_threads: bool = false, cache_mode: int = 1) -> int

This method will start to load the resource using thread(s).

Checking Status
~~~~~~~~~~~~~~~

.. code-block:: gdscript

    func ResourceLoader.load_threaded_get_status(path: String, progress: Array = []) -> int

Returns ``ResourceLoader.THREAD_LOAD_FAILED``, ``ResourceLoader.THREAD_LOAD_IN_PROGRESS``, 
``ResourceLoader.THREAD_LOAD_INVALID_RESOURCE``, or ``ResourceLoader.THREAD_LOAD_LOADED``.
The progress can be obtained by passing an array variable via progress which will return a one element array containing the percentage.

Getting the resource (forces completion)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: gdscript

    func ResourceLoader.load_threaded_get(path: String) -> Resource

To obtain the resource call this method. This will wait (block) until it can return the resource.

Example
-------

This example demonstrates how to load a scene in the background.
In this example we will have a button spawn a enemy when pressed.
The enemy will be ``Enemy.tscn`` which we will load on ``_ready`` and instantiate when pressed.
The path will be ``"Enemy.tscn"`` which is located at ``res://Enemy.tscn``.

First, we will start a request to load the resource and connect the button:

::

    # Define the path of the enemy
    const ENEMY_SCENE_PATH : String = "Enemy.tscn"
    # It isn't necessary to use constants but it can make it easier if the resource is moved around.

        func _ready():
            # Start the request for Enemy.tscn , this will not block
            ResourceLoader.load_threaded_request(ENEMY_SCENE_PATH)
            # Connect the button to our method on_button_pressed
            self.pressed.connect(on_button_pressed)

Now on_button_pressed will be called when the button is pressed.
This method will be used to spawn an enemy.

::

    func on_button_pressed(): # Button was pressed
        # Obtain the resource now that we need it
        var enemy_scene = ResourceLoader.load_threaded_get(ENEMY_SCENE_PATH)
        # Instantiate the enemy scene
        var enemy = enemy_scene.instantiate()
        # Add it to the current scene
        add_child(enemy)
        

**Note**: this code, in its current form, is not tested in real world
scenarios. If you run into any issues, ask for help in one of
`Godot's community channels <https://godotengine.org/community>`__.
