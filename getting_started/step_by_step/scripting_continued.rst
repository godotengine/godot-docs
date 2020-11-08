.. _doc_scripting_continued:

Scripting (continued)
=====================
Notifications
-------------

Godot has a system of notifications. These are usually not needed for
scripting, as it's too low-level and virtual functions are provided for
most of them. It's just good to know they exist. For example,
you may add an
:ref:`Object._notification() <class_Object_method__notification>`
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
shows the notifications it can receive. However, in most cases GDScript
provides simpler overridable functions.

Overridable functions
---------------------

Such overridable functions, which are described as
follows, can be applied to nodes:

.. tabs::
 .. code-tab:: gdscript GDScript

    func _enter_tree():
        # When the node enters the Scene Tree, it becomes active
        # and  this function is called. Children nodes have not entered
        # the active scene yet. In general, it's better to use _ready()
        # for most cases.
        pass

    func _ready():
        # This function is called after _enter_tree, but it ensures
        # that all children nodes have also entered the Scene Tree,
        # and became active.
        pass

    func _exit_tree():
        # When the node exits the Scene Tree, this function is called.
        # Children nodes have all exited the Scene Tree at this point
        # and all became inactive.
        pass

    func _process(delta):
        # This function is called every frame.
        pass

    func _physics_process(delta):
        # This is called every physics frame.
        pass

 .. code-tab:: csharp

    public override void _EnterTree()
    {
        // When the node enters the Scene Tree, it becomes active
        // and  this function is called. Children nodes have not entered
        // the active scene yet. In general, it's better to use _ready()
        // for most cases.
        base._EnterTree();
    }

    public override void _Ready()
    {
        // This function is called after _enter_tree, but it ensures
        // that all children nodes have also entered the Scene Tree,
        // and became active.
        base._Ready();
    }

    public override void _ExitTree()
    {
        // When the node exits the Scene Tree, this function is called.
        // Children nodes have all exited the Scene Tree at this point
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

As mentioned before, it's better to use these functions instead of
the notification system.

.. _doc_scripting_continued_class_name:

Register scripts as classes
---------------------------

Godot has a "Script Class" feature to register individual scripts with the
Editor. By default, you can only access unnamed scripts by loading the file
directly.

You can name a script and register it as a type in the editor with the
``class_name`` keyword followed by the class's name. You may add a comma and an
optional path to an image to use as an icon. You will then find your new type in
the Node or Resource creation dialog.

.. tabs::
 .. code-tab:: gdscript GDScript

    extends Node

    # Declare the class name here
    class_name ScriptName, "res://path/to/optional/icon.svg"

    func _ready():
        var this = ScriptName           # reference to the script
        var cppNode = MyCppNode.new()   # new instance of a class named MyCppNode

        cppNode.queue_free()

.. image:: img/script_class_nativescript_example.png


.. warning:: In Godot 3.1:

            - Only GDScript and NativeScript, i.e., C++ and other GDNative-powered languages, can register scripts.
            - Only GDScript creates global variables for each named script.
