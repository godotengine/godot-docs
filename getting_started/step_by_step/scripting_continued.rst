.. _doc_scripting_continued:

Scripting (continued)
=====================

Processing
----------

Several actions in Godot are triggered by callbacks or virtual functions, 
so there is no need to write code that runs all the time. Additionally, a 
lot can be done with animation players.

However, it is still a very common case to have a script process on every
frame. There are two types of processing: idle processing and physics
processing.

Idle processing is activated automatically when the method :ref:`Node._process() <class_Node__process>`
is found in a script. It can be turned off (and back on) with the
:ref:`Node.set_process() <class_Node_set_process>` function.

This method will be called every frame drawn, so it's fully depend on the
frames per second (FPS) of the application:

.. tabs::
 .. code-tab:: gdscript GDScript

    func _process(delta):
        # do something...
        pass

 .. code-tab:: csharp
    
    public override void _Process(float delta)
    {
        // do something...
    }

The delta parameter describes the time elapsed (in seconds, as a
floating point) since the previous call to "_process()".

This delta parameter can be used to make sure things always take the same time,
regardless of the hardware the game is running on.

For example, movement is often multiplied with the time delta to make the movement
constant and independent from the frame rate.

Physics processing (``_physics_process()``) is similar, but it should be used for all the processes that
must happen before each physics step. For example, to move a character.
It always runs before a physics step and it is called at fixed time intervals,
60 times per second by default. Change the value in the Project Settings.

The function _process() instead is not synced with physics. Its frame rate is not constant and dependent on hardware and game optimization.
Its execution is done after the physics step on single thread games.

A simple way to test this is to create a scene with a single Label node,
with the following script:

.. tabs::
 .. code-tab:: gdscript GDScript

    extends Label

    var accum = 0

    func _process(delta):
        accum += delta
        text = str(accum) # text is a built-in label property

 .. code-tab:: csharp
    
    public class CustomLabel : Label
    {
        private int _accum;

        public override void _Process(float delta)
        {
            _accum++;
            Text = _accum.ToString();
        }
    }

Which will show a counter increasing each frame.

Groups
------

Nodes can be added to groups (as many as desired per node). This is a
simple yet useful feature for organizing large scenes. There are two
ways to do this: the first is from the UI, from the Groups button under the Node panel:

.. image:: img/groups_in_nodes.png

And the second from code. One useful example would be to tag scenes
which are enemies.

.. tabs::
 .. code-tab:: gdscript GDScript

    func _ready():
        add_to_group("enemies")

 .. code-tab:: csharp
        
    public override void _Ready()
    {
        base._Ready();
        
        AddToGroup("enemies");
    }

This way, if the player is discovered sneaking into the secret base,
all enemies can be notified about the alarm sounding, by using
:ref:`SceneTree.call_group() <class_SceneTree_call_group>`:

.. tabs::
 .. code-tab:: gdscript GDScript

    func _on_discovered(): # this is a fictional function
        get_tree().call_group("enemies", "player_was_discovered")

 .. code-tab:: csharp
    
    public void _OnDiscovered() // this is a fictional function
    {
        GetTree().CallGroup("enemies", "player_was_discovered");
    }

The above code calls the function "player_was_discovered" on every
member of the group "enemies".

Optionally, it is possible to get the full list of "enemies" nodes by
calling
:ref:`SceneTree.get_nodes_in_group() <class_SceneTree_get_nodes_in_group>`:

.. tabs::
 .. code-tab:: gdscript GDScript

    var enemies = get_tree().get_nodes_in_group("enemies")

 .. code-tab:: csharp
    
    var enemies = GetTree().GetNodesInGroup("enemies");

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

.. tabs::
 .. code-tab:: gdscript GDScript

    func _notification(what):
        match what:
            NOTIFICATION_READY:
                print("This is the same as overriding _ready()...")
            NOTIFICATION_PROCESS:
                print("This is the same as overriding _process()...")

 .. code-tab:: csharp

    public override void _Notification(int what)
    {
        base._Notification(what);

        switch (what)
        {
            case NotificationReady:
                GD.Print("This is the same as overriding _Ready()...");
                break;
            case NotificationProcess:
                var delta = GetProcessDeltaTime();
                GD.Print("This is the same as overriding _Process()...");
                break;
        }
    }

The documentation of each class in the :ref:`Class Reference <toc-class-ref>`
shows the notifications it can receive. However, for most cases GDScript
provides simpler overrideable functions.

Overrideable functions
----------------------

Nodes provide many useful overrideable functions, which are described as
follows:

.. tabs::
 .. code-tab:: gdscript GDScript

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

 .. code-tab:: csharp
 
    public override void _EnterTree()
    {
        // When the node enters the _Scene Tree_, it becomes active
        // and  this function is called. Children nodes have not entered
        // the active scene yet. In general, it's better to use _ready()
        // for most cases.
        base._EnterTree();
    }

    public override void _Ready()
    {
        // This function is called after _enter_tree, but it ensures
        // that all children nodes have also entered the _Scene Tree_,
        // and became active.
        base._Ready();
    }

    public override void _ExitTree()
    {
        // When the node exits the _Scene Tree_, this function is called.
        // Children nodes have all exited the _Scene Tree_ at this point
        // and all became inactive.
        base._ExitTree();
    }

    public override void _Process(float delta)
    {
        // This function is called every frame.
        base._Process(delta);
    }

    public override void _PhysicsProcess(float delta)
    {
        // This is called every physics frame.
        base._PhysicsProcess(delta);
    }


As mentioned before, it's best to use these functions.

Creating nodes
--------------

To create a node from code, call the .new() method, just like for any 
other class based datatype. Example:


.. tabs::
 .. code-tab:: gdscript GDScript

    var s
    func _ready():
        s = Sprite.new() # create a new sprite!
        add_child(s) # add it as a child of this node

 .. code-tab:: csharp

    private Sprite _sprite;

    public override void _Ready()
    {
        base._Ready();
    
        _sprite = new Sprite(); // create a new sprite!
        AddChild(_sprite); // add it as a child of this node
    }

To delete a node, be it inside or outside the scene, "free()" must be
used:

.. tabs::
 .. code-tab:: gdscript GDScript

    func _someaction():
        s.free() # immediately removes the node from the scene and frees it

 .. code-tab:: csharp

    public void _SomeAction()
    {
        _sprite.Free();
    }

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

.. tabs::
 .. code-tab:: gdscript GDScript

    func _someaction():
        s.queue_free() # immediately removes the node from the scene and frees it

 .. code-tab:: csharp

    public void _SomeAction()
    {
        _sprite.QueueFree(); // immediately removes the node from the scene and frees it
    }

Instancing scenes
-----------------

Instancing a scene from code is pretty easy and done in two steps. The
first one is to load the scene from disk.

.. tabs::
 .. code-tab:: gdscript GDScript

    var scene = load("res://myscene.tscn") # will load when the script is instanced

 .. code-tab:: csharp
    
    var scene = (PackedScene)ResourceLoader.Load("res://myscene.tscn"); // will load when the script is instanced


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

.. tabs::
 .. code-tab:: gdscript GDScript

    var node = scene.instance()
    add_child(node)

 .. code-tab:: csharp
    
    var node = scene.Instance();
    AddChild(node);

The advantage of this two-step process is that a packed scene may be
kept loaded and ready to use, so it can be used to create as many
instances as desired. This is especially useful to quickly instance
several enemies, bullets, etc., in the active scene.
