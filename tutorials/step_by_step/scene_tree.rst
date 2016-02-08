:: _doc_scene_tree:

SceneTree
=========

Introduction
------------

| This is where things start getting abstract, but don't panic, as
  there's not really more depth than this.
| In previous tutorials, everything revolves around the concept of
  Nodes, scenes are made of them, and they become active once they enter
  the *Scene Tree*.

This deserves going a little more into depth. In fact, the scene system
is not even a core component of Godot, as it is possible to skip it and
make a script (or C++ code) that talks directly to the [[Servers]]. But
making a game that way would be a lot of work and is reserved for other
uses.

MainLoop
--------

| The way Godot works internally is as follows. There is the the
  `OS <https://github.com/okamstudio/godot/wiki/class_os>`__ class,
  which is the only instance that runs at the beginning. Afterwards, all
  drivers, servers, scripting languages, scene system, etc are loaded.
| When initialization is complete,
  `OS <https://github.com/okamstudio/godot/wiki/class_os>`__ needs to be
  supplied a
  `MainLoop <https://github.com/okamstudio/godot/wiki/class_mainloop>`__
  to run. Up to this point, all this is internals working (you can check
  main/main.cpp file in the source code if you are ever interested to
  see how this works internally).

The user program, or game, starts in the MainLoop. This class has a few
methods, for initialization, idle (frame-syncronized callback), fixed
(physics-synchronized callback), and input. Again, this is really low
level and when making games in Godot, writing your own MainLoop does not
even make sense.

SceneTree
---------

| One of the ways to explain how Godot works, is that it's a high level
  game engine over a low level middleware.
| The scene system is the game engine, while the
  `OS <https://github.com/okamstudio/godot/wiki/class_os>`__ and servers
  are the low level API.

| In any case, the scene system provides it's own main loop to OS,
  `SceneTree <https://github.com/okamstudio/godot/wiki/class_scenetree>`__.
| This is automatically instanced and set when running a scene, no need
  to do any extra work.

It's important to know that this class exists because it has a few
important uses:

-  It contains the root
   `Viewport <https://github.com/okamstudio/godot/wiki/class_viewport>`__,
   when a scene is first opened, it's added as a child of it to become
   part of the *Scene Tree* (more on that next)
-  It contains information about the groups, and has means to call all
   nodes in a group, or get a list of them.
-  It contains some global state functionality, such as setting pause
   mode, or quitting the process.

When a node is part of the Scene Tree, the
`SceneTree <https://github.com/okamstudio/godot/wiki/class_scenemainloop>`__
singleton can be obtained by simply calling
`Node.get\_tree() <https://github.com/okamstudio/godot/wiki/class_node#get_tree>`__.

Root Viewport
-------------

The root
`Viewport <https://github.com/okamstudio/godot/wiki/class_viewport>`__
is always a top of the scene. From a node, it can be obtained in two
different ways:

::

        get_tree().get_root() # access via scenemainloop
        get_node("/root") # access via absolute path

This node contains the main viewport, anything that is a child of a
`Viewport <https://github.com/okamstudio/godot/wiki/class_viewport>`__
is drawn inside of it by default, so it makes sense that the top of all
nodes is always a node of this type, otherwise nothing would be seen!

While other viewports can be created in the scene (for split-screen
effects and such), this one is the only one that is never created by the
user. It's created automatically inside SceneTree.

Scene Tree
----------

| When a node is connected, directly or indirectly, to the root
  viewport, it becomes part of the *Scene Tree*.
| This means that, as explained in previous tutorials, will get the
  \_enter\_tree() and \_ready() callbacks (as well as \_exit\_tree()).

.. image:: /img/activescene.png

When nodes enter the *Scene Tree*, they become active. They get access
to everything they need to process, get input, display 2D and 3D,
notifications, play sound, groups, etc. When they are removed from the
*Scene Tree*, they lose it.

Tree Order
----------

Most node operations in Godot, such as drawing 2D, processing or getting
notifications are done in tree order. This means that parents and
siblings with less order will get notified before the current node.

.. image:: /img/toptobottom.png

"Becoming Active" by entering the *Scene Tree* In Detail
--------------------------------------------------------

#. A scene is loaded from disk or created by scripting.
#. The root node of that scene (only one root, remember?) is added as
   either a child of the "root" Viewport (from SceneTree), or to any
   child or grand-child of it.
#. Every node of the newly added scene, will receive the "enter\_tree"
   notification ( \_enter\_tree() callback in GDScript) in top-to-bottom
   order.
#. An extra notification, "ready" ( \_ready() callback in GDScript) is
   provided for convenience, when a node and all it"™s children are
   inside the active scene.
#. When a scene (or part of it) is removed, they receive the "exit
   scene" notification ( \_exit\_tree() callback in GDScript) in
   bottom-to-top order

Changing Current Scene
----------------------

After a scene is loaded, it is often desired to change this scene for
another one. The simple way to do this to use the
`SceneTree.change\_scene <https://github.com/okamstudio/godot/wiki/class_scenetree#change_scene>`__
function:

::

    func _my_level_was_completed():
        get_tree().change_scene("res://levels/level2.scn")

This is a quick and useful way to switch scenes, but has the drawback
that the game will stall until the new scene is loaded and running. At
some point in your game, it may be desired to create proper loading
screens with progress bar, animated indicators or thread (background)
loading. This must be done manually using autoloads (see next chapter!)
and [[Background Loading]].



