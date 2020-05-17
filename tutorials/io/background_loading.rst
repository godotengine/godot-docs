.. _doc_background_loading:

Background loading
==================

When switching the main scene of your game (e.g. going to a new
level), you might want to show a loading screen with some indication
that progress is being made. The main load method
(``ResourceLoader::load`` or just ``load`` from GDScript) blocks your
thread, making your game appear frozen and unresponsive while the resource is being loaded. This
document discusses the alternative of using the ``ResourceInteractiveLoader`` class for smoother
load screens.

ResourceInteractiveLoader
-------------------------

The ``ResourceInteractiveLoader`` class allows you to load a resource in
stages. Every time the method ``poll`` is called, a new stage is loaded,
and control is returned to the caller. Each stage is generally a
sub-resource that is loaded by the main resource. For example, if you're
loading a scene that loads 10 images, each image will be one stage.

Usage
-----

Usage is generally as follows

Obtaining a ResourceInteractiveLoader
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: cpp

    Ref<ResourceInteractiveLoader> ResourceLoader::load_interactive(String p_path);

This method will give you a ResourceInteractiveLoader that you will use
to manage the load operation.

Polling
~~~~~~~

.. code-block:: cpp

    Error ResourceInteractiveLoader::poll();

Use this method to advance the progress of the load. Each call to
``poll`` will load the next stage of your resource. Keep in mind that
each stage is one entire "atomic" resource, such as an image, or a mesh,
so it will take several frames to load.

Returns ``OK`` on no errors, ``ERR_FILE_EOF`` when loading is finished.
Any other return value means there was an error and loading has stopped.

Load progress (optional)
~~~~~~~~~~~~~~~~~~~~~~~~

To query the progress of the load, use the following methods:

.. code-block:: cpp

    int ResourceInteractiveLoader::get_stage_count() const;
    int ResourceInteractiveLoader::get_stage() const;

``get_stage_count`` returns the total number of stages to load.
``get_stage`` returns the current stage being loaded.

Forcing completion (optional)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: cpp

    Error ResourceInteractiveLoader::wait();

Use this method if you need to load the entire resource in the current
frame, without any more steps.

Obtaining the resource
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: cpp

    Ref<Resource> ResourceInteractiveLoader::get_resource();

If everything goes well, use this method to retrieve your loaded
resource.

Example
-------

This example demonstrates how to load a new scene. Consider it in the
context of the :ref:`doc_singletons_autoload` example.

First, we set up some variables and initialize the ``current_scene``
with the main scene of the game:

::

    var loader
    var wait_frames
    var time_max = 100 # msec
    var current_scene

    func _ready():
        var root = get_tree().get_root()
        current_scene = root.get_child(root.get_child_count() -1)

The function ``goto_scene`` is called from the game when the scene
needs to be switched. It requests an interactive loader, and calls
``set_process(true)`` to start polling the loader in the ``_process``
callback. It also starts a "loading" animation, which could show a
progress bar or loading screen.

::

    func goto_scene(path): # game requests to switch to this scene
        loader = ResourceLoader.load_interactive(path)
        if loader == null: # check for errors
            show_error()
            return
        set_process(true)

        current_scene.queue_free() # get rid of the old scene

        # start your "loading..." animation
        get_node("animation").play("loading")

        wait_frames = 1

``_process`` is where the loader is polled. ``poll`` is called, and then
we deal with the return value from that call. ``OK`` means keep polling,
``ERR_FILE_EOF`` means loading is done, anything else means there was an
error. Also note we skip one frame (via ``wait_frames``, set on the
``goto_scene`` function) to allow the loading screen to show up.

Note how we use ``OS.get_ticks_msec`` to control how long we block the
thread. Some stages might load fast, which means we might be able
to cram more than one call to ``poll`` in one frame; some might take way
more than your value for ``time_max``, so keep in mind we won't have
precise control over the timings.

::

    func _process(time):
        if loader == null:
            # no need to process anymore
            set_process(false)
            return

        if wait_frames > 0: # wait for frames to let the "loading" animation show up
            wait_frames -= 1
            return

        var t = OS.get_ticks_msec()
        while OS.get_ticks_msec() < t + time_max: # use "time_max" to control for how long we block this thread

            # poll your loader
            var err = loader.poll()

            if err == ERR_FILE_EOF: # Finished loading.
                var resource = loader.get_resource()
                loader = null
                set_new_scene(resource)
                break
            elif err == OK:
                update_progress()
            else: # error during loading
                show_error()
                loader = null
                break

Some extra helper functions. ``update_progress`` updates a progress bar,
or can also update a paused animation (the animation represents the
entire load process from beginning to end). ``set_new_scene`` puts the
newly loaded scene on the tree. Because it's a scene being loaded,
``instance()`` needs to be called on the resource obtained from the
loader.

::

    func update_progress():
        var progress = float(loader.get_stage()) / loader.get_stage_count()
        # Update your progress bar?
        get_node("progress").set_progress(progress)

        # ... or update a progress animation?
        var length = get_node("animation").get_current_animation_length()

        # Call this on a paused animation. Use "true" as the second argument to force the animation to update.
        get_node("animation").seek(progress * length, true)

    func set_new_scene(scene_resource):
        current_scene = scene_resource.instance()
        get_node("/root").add_child(current_scene)

Using multiple threads
----------------------

ResourceInteractiveLoader can be used from multiple threads. A couple of
things to keep in mind if you attempt it:

Use a semaphore
~~~~~~~~~~~~~~~

While your thread waits for the main thread to request a new resource,
use a ``Semaphore`` to sleep (instead of a busy loop or anything similar).

Not blocking main thread during the polling
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have a mutex to allow calls from the main thread to your loader
class, don't lock the main thread while you call ``poll`` on your loader class. When a
resource is done loading, it might require some resources from the
low-level APIs (VisualServer, etc), which might need to lock the main
thread to acquire them. This might cause a deadlock if the main thread
is waiting for your mutex while your thread is waiting to load a
resource.

Example class
-------------

You can find an example class for loading resources in threads here:
:download:`resource_queue.gd <files/resource_queue.gd>`. Usage is as follows:

::

    func start()

Call after you instance the class to start the thread.

::

    func queue_resource(path, p_in_front = false)

Queue a resource. Use optional argument "p_in_front" to put it in
front of the queue.

::

    func cancel_resource(path)

Remove a resource from the queue, discarding any loading done.

::

    func is_ready(path)

Returns ``true`` if a resource is fully loaded and ready to be retrieved.

::

    func get_progress(path)

Get the progress of a resource. Returns -1 if there was an error (for example if the
resource is not in the queue), or a number between 0.0 and 1.0 with the
progress of the load. Use mostly for cosmetic purposes (updating
progress bars, etc), use ``is_ready`` to find out if a resource is
actually ready.

::

    func get_resource(path)

Returns the fully loaded resource, or ``null`` on error. If the resource is
not fully loaded (``is_ready`` returns ``false``), it will block your thread
and finish the load. If the resource is not on the queue, it will call
``ResourceLoader::load`` to load it normally and return it.

Example:
~~~~~~~~

::

    # Initialize.
    queue = preload("res://resource_queue.gd").new()
    queue.start()

    # Suppose your game starts with a 10 second cutscene, during which the user can't interact with the game.
    # For that time, we know they won't use the pause menu, so we can queue it to load during the cutscene:
    queue.queue_resource("res://pause_menu.tres")
    start_cutscene()

    # Later, when the user presses the pause button for the first time:
    pause_menu = queue.get_resource("res://pause_menu.tres").instance()
    pause_menu.show()

    # when you need a new scene:
    queue.queue_resource("res://level_1.tscn", true) # Use "true" as the second argument to put it at the front
                                                     # of the queue, pausing the load of any other resource.

    # to check progress
    if queue.is_ready("res://level_1.tscn"):
        show_new_level(queue.get_resource("res://level_1.tscn"))
    else:
        update_progress(queue.get_progress("res://level_1.tscn"))

    # when the user walks away from the trigger zone in your Metroidvania game:
    queue.cancel_resource("res://zone_2.tscn")

**Note**: this code, in its current form, is not tested in real world
scenarios. If you run into any issues, ask for help in one of
`Godot's community channels <https://godotengine.org/community>`__.
