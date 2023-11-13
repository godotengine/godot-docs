.. _doc_overridable_functions:

Overridable functions
=====================

Godot's Node class provides virtual functions you can override to update nodes
every frame or on specific events, like when they enter the scene tree.

This document presents the ones you'll use most often.

.. seealso:: Under the hood, these functions rely on Godot's low-level
             notifications system. To learn more about it, see
             :ref:`doc_godot_notifications`.

Two functions allow you to initialize and get nodes besides the class's
constructor: ``_enter_tree()`` and ``_ready()``.

When the node enters the Scene Tree, it becomes active and the engine calls its
``_enter_tree()`` method. That node's children may not be part of the active scene yet. As
you can remove and re-add nodes to the scene tree, this function may be called
multiple times throughout a node's lifetime.

Most of the time, you'll use ``_ready()`` instead. This function is called only
once in a node's lifetime, after ``_enter_tree()``. ``_ready()`` ensures that all children
have entered the scene tree first, so you can safely call ``get_node()`` on them.

.. seealso:: To learn more about getting node references, read
             :ref:`doc_nodes_and_scene_instances`.

Another related callback is ``_exit_tree()``, which the engine calls every time
a node is about to exit the scene tree. This can be when you call :ref:`Node.remove_child()
<class_Node_method_remove_child>` or when you free a node.

.. tabs::
 .. code-tab:: gdscript GDScript

    # Called every time the node enters the scene tree.
    func _enter_tree():
        pass

    # Called when both the node and its children have entered the scene tree.
    func _ready():
        pass

    # Called when the node is about to leave the scene tree, after all its
    # children received the _exit_tree() callback.
    func _exit_tree():
        pass

 .. code-tab:: csharp

    // Called every time the node enters the scene tree.
    public override void _EnterTree()
    {
        base._EnterTree();
    }

    // Called when both the node and its children have entered the scene tree.
    public override void _Ready()
    {
        base._Ready();
    }

    // Called when the node is about to leave the scene tree, after all its
    // children.
    public override void _ExitTree()
    {
        base._ExitTree();
    }

The two virtual methods ``_process()`` and ``_physics_process()`` allow you to
update the node, every frame and every physics frame respectively. For more
information, read the dedicated documentation:
:ref:`doc_idle_and_physics_processing`.

.. tabs::
 .. code-tab:: gdscript GDScript

    # Called every frame.
    func _process(delta):
        pass

    # Called every physics frame.
    func _physics_process(delta):
        pass

 .. code-tab:: csharp

    public override void _Process(double delta)
    {
        // Called every frame.
        base._Process(delta);
    }

    public override void _PhysicsProcess(double delta)
    {
        // Called every physics frame.
        base._PhysicsProcess(delta);
    }

Two more essential built-in node callback functions are
:ref:`Node._unhandled_input() <class_Node_private_method__unhandled_input>` and
:ref:`Node._input() <class_Node_private_method__input>`, which you use to both receive
and process individual input events. The ``_unhandled_input()`` method receives
every key press, mouse click, etc. that have not been handled already in an
``_input()`` callback or in a user interface component. You want to use it for
gameplay input in general. The ``_input()`` callback allows you to intercept and
process input events before ``_unhandled_input()`` gets them.

To learn more about inputs in Godot, see the :ref:`Input section <toc-learn-features-inputs>`.

.. tabs::
 .. code-tab:: gdscript GDScript

    # Called once for every event.
    func _unhandled_input(event):
        pass

    # Called once for every event before _unhandled_input(), allowing you to
    # consume some events.
    func _input(event):
        pass

 .. code-tab:: csharp

    // Called once for every event.
    public override void _UnhandledInput(InputEvent @event)
    {
        base._UnhandledInput(@event);
    }

    // Called once for every event before _UnhandledInput(), allowing you to
    // consume some events.
    public override void _Input(InputEvent @event)
    {
        base._Input(@event);
    }

There are some more overridable functions like
:ref:`Node._get_configuration_warnings()
<class_Node_private_method__get_configuration_warnings>`. Specialized node types provide
more callbacks like :ref:`CanvasItem._draw() <class_CanvasItem_private_method__draw>` to
draw programmatically or :ref:`Control._gui_input()
<class_Control_private_method__gui_input>` to handle clicks and input on UI elements.
