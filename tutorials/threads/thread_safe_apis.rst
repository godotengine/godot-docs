.. _doc_thread_safe_apis:

Thread Safe APIs
================

Threads
-------

Using threads is a common way to balance processing scatter it across CPUs and cores.
Godot supports multi threading, but not in the whole engine.

Below is a list of the areas in Godot and how they can be used with threads.

Global Scope
------------

:ref:`Global Scope<class_@GlobalScope>` singletons are all thread safe. Accessing servers from threads is supported (for VisualServer and Physics servers, ensure threaded or thread safe operation is enabled in the project settings!).

This makes them ideal for code that creates dozens of thousands of instances in servers and controls them from threads. Of course, it requires a bit more code, as this is used directly and not within the scene tree.

Scene Tree
----------

Interacting with the active scene tree is **NOT** thread safe. Make sure to use mutexes when sending data between threads. If you want to call functions from a thread, the *call_deferred* function may be used:

::

	# unsafe:
        node.add_child(child_node)
 	# safe:
	node.call_deferred("add_child",child_node)

However, creating scene chunks (nodes in tree arrangement) outside the active tree is fine. This way, parts of a scene can be built or instantiated in a thread, then added in the main thread:

::

	var enemy_scene = load("res://enemy_scene.scn").instance()
        var enemy = enemy_scene.instance()
	enemy.add_child(weapon) #set a weapon
	world.call_deferred("add_child",enemy)

GDScript Arrays, Dictionaries:
-------------------------------

In GDScript, reading and writing elements from multiple threads is ok, but anything that changes the container size (resizing, adding or removing elements) requires locking a mutex.

Resources
---------

Modifying a unique resource from multiple threads is not supported, but loading them on threads or handling a reference is perfectly supported. Scenes, textures, meshes, etc. Can be loaded and manipulated on threads, then added to the active scene in the main thread.


