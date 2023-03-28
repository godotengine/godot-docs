:article_outdated: True

.. _doc_thread_safe_apis:

Thread-safe APIs
================

Some parts of Godot support the use of threads, or "threading", 
to balance processing power across a system's CPU cores,
leading to potentially improved performance.

Below lists some ways threads can be used in different areas of Godot.

Global Scope and Servers
------------------------

:ref:`Global Scope<class_@GlobalScope>` singletons are thread-safe. 
Accessing servers from threads is also supported.

This makes them ideal for code that creates thousands of instances in servers 
and controls them from threads, although this will require more code, 
as this is used directly and not within the scene tree.

.. note::

    For :ref:`RenderingServer<class_RenderingServer>` and Physics servers, 
    ensure threaded or thread-safe operation is enabled in the project settings!
    
Scene Tree
----------

Interaction with the active scene tree is *not* thread-safe. 
Ensure that :ref:`Mutexes<class_Mutex>` are used when data is sent between threads. 
If you want to call functions from a thread, the ``call_deferred`` function may be used:

::

    ## Unsafe:
    node.add_child(child_node)
    ## Safe:
    node.call_deferred("add_child", child_node)

Creating scene chunks (nodes in tree arrangement) outside the active tree is also fine. 
This way, parts of a scene can be built or instantiated in a thread, 
then added in the main thread:

::

    var enemy_scene = load("res://enemy_scene.scn")
    var enemy = enemy_scene.instantiate()
    ## Add a weapon to an enemy.
    enemy.add_child(weapon)
    world.call_deferred("add_child", enemy)

Still, this is only useful if you have **one** thread loading data.
Attempting to load or create scene chunks from multiple threads may work, but you risk
resources (which are only loaded once in Godot) tweaked by the multiple
threads, resulting in unexpected behaviors or crashes.

Only use more than one thread to generate scene data if you *really* know what
you're doing and are sure that a single resource is *not* being used or
set in multiple ones. Otherwise, you're safer using the servers API
(which is fully thread-safe) directly and not touching scene data or resources.

Rendering
---------

Instancing nodes that render anything in 2D or 3D (such as Sprite) is *not* thread-safe by default.
To make rendering thread-safe, set the **Rendering > Driver > Threads > Thread Model** project setting to **Multi-Threaded**.
(The **Advanced Settings** toggle also has to be enabled to see this setting.)

.. note::

    You may encounter bugs with the Multi-Threaded thread model,
    so it may not be usable in all scenarios.

GDScript arrays and dictionaries
--------------------------------

In GDScript, its okay to read and write elements from multiple threads, 
but anything that changes the container size (resizing, adding, or removing elements) 
requires locking a mutex.

Resources
---------

Modifying a unique resource from multiple threads is *not* supported. 
Handling references on multiple threads *is* supported, though, 
hence loading resources on a thread is as well - scenes, textures, meshes, etc. 
can be loaded and manipulated on a thread and then added to the active scene on the main thread. 

The limitation here is as described above. One must be careful not to load the 
same resource from multiple threads at once, 
therefore it is safer to use **one** thread to load and modify resources, 
and then the main thread to add them.
