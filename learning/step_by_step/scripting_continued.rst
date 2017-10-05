.. _doc_scripting_continued:

Scripting (continued)
=====================

Processing
----------

Several actions in Godot are triggered by callbacks or virtual
functions, so there is no need to check for writing code that runs all
the time. Additionally, a lot can be done with animation players.

However, it is still a very common case to have a script process on every
frame. There are two types of processing: idle processing and physics
processing.

Idle processing is activated automatically when the method :ref:`Node._process() <class_Node__process>`
is found in a script. It can be turned off (and back on) with the
:ref:`Node.set_process() <class_Node_set_process>` function.

This method will be called every frame drawn, so it's fully depend on the
frames per second (FPS) of the application:

::

    func _process(delta):
        # do something...

The delta parameter describes the time elapsed (in seconds, as
floating point) since the previous call to "_process()".

Physics processing is similar, but it should be used for all the processes that
must happen before each physics step. For example, to move a character.
It is always runs before a physics step and it is called at fixed time intervals,
60 times per second by default. Change the value in the Project Settings.

The function _process() instead is not sync with physics, and its frame rate is not constant and depend by hardware and game optimization.
Its execution is done after physics step on single thread games.

A simple way to test this is to create a scene with a single Label node,
with the following script:

::

    extends Label

    var accum=0

    func _process(delta):
        accum += delta
        text = str(accum) # text is a built-in label property

Which will show a counter increasing each frame.

Groups
------

Nodes can be added to groups (as many as desired per node). This is a
simple yet useful feature for organizing large scenes. There are two
ways to do this: the first is from the UI, from the Groups button under the Node panel:

.. image:: /img/groups_in_nodes.PNG

And the second from code. One useful example would be to tag scenes
which are enemies.

::

    func _ready():
        add_to_group("enemies")

This way, if the player is discovered sneaking into the secret base,
all enemies can be notified about the alarm sounding, by using
:ref:`SceneTree.call_group() <class_SceneTree_call_group>`:

::

    func _on_discovered(): # this is a fictional function
        get_tree().call_group("guards", "player_was_discovered")

The above code calls the function "player_was_discovered" on every
member of the group "guards".

Optionally, it is possible to get the full list of "guards" nodes by
calling
:ref:`SceneTree.get_nodes_in_group() <class_SceneTree_get_nodes_in_group>`:

::

    var guards = get_tree().get_nodes_in_group("guards")

More will be added about
:ref:`SceneTree <class_SceneTree>`
later.

Notifications
-------------

Godot has a system of notifications. This is usually not needed for
scripting, as it's too low level and virtual functions are provided for
most of them. It's just good to know they exist. Simply
add a
:ref:`Object._notification() <class_Object__notification>`
function in your script:

::

    func _notification(what):
        if (what == NOTIFICATION_READY):
            print("This is the same as overriding _ready()...")
        elif (what == NOTIFICATION_PROCESS):
            var delta = get_process_time()
            print("This is the same as overriding _process()...")

The documentation of each class in the :ref:`Class Reference <toc-class-ref>`
shows the notifications it can receive. However, for most cases GDScript
provides simpler overrideable functions.

Overrideable functions
----------------------

Nodes provide many useful overrideable functions, which are described as
follows:

::

    func _enter_tree():
        # When the node enters the _Scene Tree_, it becomes active
        # and  this function is called. Children nodes have not entered
        # the active scene yet. In general, it's better to use _ready()
        # for most cases.
        pass

    func _ready():
        # This function is called after _enter_tree, but it ensures
        # that all children nodes have also entered the _Scene Tree_,
        # and became active.
        pass

    func _exit_tree():
        # When the node exits the _Scene Tree_, this function is called.
        # Children nodes have all exited the _Scene Tree_ at this point
        # and all became inactive.
        pass

    func _process(delta):
        # This function is called every frame.
        pass

    func _physics_process(delta):
        # This is called every physics frame.
        pass

    func _paused():
        # Called when game is paused. After this call, the node will not receive
        # any more process callbacks.
        pass

    func _unpaused():
        # Called when game is unpaused.
        pass

As mentioned before, it's best to use these functions.

Creating nodes
--------------

To create a node from code, just call the ".new()" method (like for any
other class-based datatype). Example:

::

    var s
    func _ready():
        s = Sprite.new() # create a new sprite!
        add_child(s) # add it as a child of this node

To delete a node, be it inside or outside the scene, "free()" must be
used:

::

    func _someaction():
        s.free() # immediately removes the node from the scene and frees it

When a node is freed, it also frees all its children nodes. Because of
this, manually deleting nodes is much simpler than it appears. Just free
the base node and everything else in the sub-tree goes away with it.

However, it might happen very often that we want to delete a node that
is currently "blocked", because it is emitting a signal or calling a
function. This will result in crashing the game. Running Godot
in the debugger often will catch this case and warn you about it.

The safest way to delete a node is by using
:ref:`Node.queue_free() <class_Node_queue_free>`.
This erases the node safely during idle.

::

    func _someaction():
        s.queue_free() # remove the node and delete it while nothing is happening

Instancing scenes
-----------------

Instancing a scene from code is pretty easy and done in two steps. The
first one is to load the scene from disk.

::

    var scene = load("res://myscene.tscn") # will load when the script is instanced

Preloading it can be more convenient sometimes, as it happens at parse
time.

::

    var scene = preload("res://myscene.tscn") # will load when parsing the script

But 'scene' is not yet a node for containing subnodes. It's packed in a
special resource called :ref:`PackedScene <class_PackedScene>`.
To create the actual node, the function
:ref:`PackedScene.instance() <class_PackedScene_instance>`
must be called. This will return the tree of nodes that can be added to
the active scene:

::

    var node = scene.instance()
    add_child(node)

The advantage of this two-step process is that a packed scene may be
kept loaded and ready to use, so it can be used to create as many
instances as desired. This is especially useful to quickly instance
several enemies, bullets, etc., in the active scene.
