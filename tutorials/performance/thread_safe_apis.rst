.. _doc_thread_safe_apis:

Thread-safe APIs
================

Threads
-------

Threads are used to balance processing power across CPUs and cores.
Godot supports multithreading, but not in the whole engine.

Below is a list of ways multithreading can be used in different areas of Godot.

Global scope
------------

:ref:`Global Scope<class_@GlobalScope>` singletons are all thread-safe. Accessing servers from threads is supported (for VisualServer and Physics servers, ensure threaded or thread-safe operation is enabled in the project settings!).

This makes them ideal for code that creates dozens of thousands of instances in servers and controls them from threads. Of course, it requires a bit more code, as this is used directly and not within the scene tree.

Scene tree
----------

Interacting with the active scene tree is **NOT** thread-safe. Make sure to use mutexes when sending data between threads. If you want to call functions from a thread, the *call_deferred* function may be used:

::

    # Unsafe:
    node.add_child(child_node)
    # Safe:
    node.call_deferred("add_child", child_node)

However, creating scene chunks (nodes in tree arrangement) outside the active tree is fine. This way, parts of a scene can be built or instantiated in a thread, then added in the main thread:

::

    var enemy_scene = load("res://enemy_scene.scn").instance()
    var enemy = enemy_scene.instance()
    enemy.add_child(weapon) # Set a weapon.
    world.call_deferred("add_child", enemy)

Still, this is only really useful if you have **one** thread loading data.
Attempting to load or create scene chunks from multiple threads may work, but you risk
resources (which are only loaded once in Godot) tweaked by the multiple
threads, resulting in unexpected behaviors or crashes.

Only use more than one thread to generate scene data if you *really* know what
you are doing and you are sure that a single resource is not being used or
set in multiple ones. Otherwise, you are safer just using the servers API
(which is fully thread-safe) directly and not touching scene or resources.

GDScript arrays, dictionaries
-----------------------------

In GDScript, reading and writing elements from multiple threads is ok, but anything that changes the container size (resizing, adding or removing elements) requires locking a mutex.

Resources
---------

Modifying a unique resource from multiple threads is not supported. However handling references on multiple threads is supported, hence loading resources on a thread is as well - scenes, textures, meshes, etc - can be loaded and manipulated on a thread and then added to the active scene on the main thread. The limitation here is as described above, one must be careful not to load the same resource from multiple threads at once, therefore it is easiest to use **one** thread for loading and modifying resources, and then the main thread for adding them.
