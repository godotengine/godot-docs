:article_outdated: True

.. _doc_3d_gizmo_plugins:

3D gizmo plugins
================

Introduction
------------

3D gizmo plugins are used by the editor and custom plugins to define the
gizmos attached to any kind of Node3D node.

This tutorial shows the two main approaches to defining your own custom
gizmos. The first option works well for simple gizmos and creates less clutter in
your plugin structure, and the second one will let you store some per-gizmo data.

.. note:: This tutorial assumes you already know how to make generic plugins. If
          in doubt, refer to the :ref:`doc_making_plugins` page.

The EditorNode3DGizmoPlugin
---------------------------

Regardless of the approach we choose, we will need to create a new
:ref:`EditorNode3DGizmoPlugin <class_EditorNode3DGizmoPlugin>`. This will allow
us to set a name for the new gizmo type and define other behaviors such as whether
the gizmo can be hidden or not.

This would be a basic setup:

::

    # my_custom_gizmo_plugin.gd
    extends EditorNode3DGizmoPlugin


    func get_name():
        return "CustomNode"


::

    # MyCustomEditorPlugin.gd
    @tool
    extends EditorPlugin


    const MyCustomGizmoPlugin = preload("res://addons/my-addon/my_custom_gizmo_plugin.gd")

    var gizmo_plugin = MyCustomGizmoPlugin.new()


    func _enter_tree():
        add_node_3d_gizmo_plugin(gizmo_plugin)


    func _exit_tree():
        remove_node_3d_gizmo_plugin(gizmo_plugin)


For simple gizmos, inheriting :ref:`EditorNode3DGizmoPlugin <class_EditorNode3DGizmoPlugin>`
is enough. If you want to store some per-gizmo data or you are porting a Godot 3.0 gizmo
to 3.1+, you should go with the second approach.


Simple approach
---------------

The first step is to, in our custom gizmo plugin, override the :ref:`_has_gizmo()<class_EditorNode3DGizmoPlugin_private_method__has_gizmo>`
method so that it returns ``true`` when the node parameter is of our target type.

::

    # ...


    func _has_gizmo(node):
        return node is MyCustomNode3D


    # ...

Then we can override methods like :ref:`_redraw()<class_EditorNode3DGizmoPlugin_private_method__redraw>`
or all the handle related ones.

::

    # ...


    func _init():
        create_material("main", Color(1, 0, 0))
        create_handle_material("handles")


    func _redraw(gizmo):
        gizmo.clear()

        var node3d = gizmo.get_node_3d()

        var lines = PackedVector3Array()

        lines.push_back(Vector3(0, 1, 0))
        lines.push_back(Vector3(0, node3d.my_custom_value, 0))

        var handles = PackedVector3Array()

        handles.push_back(Vector3(0, 1, 0))
        handles.push_back(Vector3(0, node3d.my_custom_value, 0))

        gizmo.add_lines(lines, get_material("main", gizmo), false)
        gizmo.add_handles(handles, get_material("handles", gizmo), [])


    # ...

Note that we created a material in the `_init` method, and retrieved it in the `_redraw`
method using :ref:`get_material()<class_EditorNode3DGizmoPlugin_method_get_material>`. This
method retrieves one of the material's variants depending on the state of the gizmo
(selected and/or editable).

So the final plugin would look somewhat like this:

::

    extends EditorNode3DGizmoPlugin


    const MyCustomNode3D = preload("res://addons/my-addon/my_custom_node_3d.gd")


    func _init():
        create_material("main", Color(1,0,0))
        create_handle_material("handles")


    func _has_gizmo(node):
        return node is MyCustomNode3D


    func _redraw(gizmo):
        gizmo.clear()

        var node3d = gizmo.get_node_3d()

        var lines = PackedVector3Array()

        lines.push_back(Vector3(0, 1, 0))
        lines.push_back(Vector3(0, node3d.my_custom_value, 0))

        var handles = PackedVector3Array()

        handles.push_back(Vector3(0, 1, 0))
        handles.push_back(Vector3(0, node3d.my_custom_value, 0))

        gizmo.add_lines(lines, get_material("main", gizmo), false)
        gizmo.add_handles(handles, get_material("handles", gizmo), [])


    # You should implement the rest of handle-related callbacks
    # (_get_handle_name(), _get_handle_value(), _commit_handle(), ...).

Note that we just added some handles in the `_redraw` method, but we still need to implement
the rest of handle-related callbacks in :ref:`EditorNode3DGizmoPlugin <class_EditorNode3DGizmoPlugin>`
to get properly working handles.

Alternative approach
--------------------

In some cases we want to provide our own implementation of :ref:`EditorNode3DGizmo<class_EditorNode3DGizmo>`,
maybe because we want to have some state stored in each gizmo or because we are porting
an old gizmo plugin and we don't want to go through the rewriting process.

In these cases all we need to do is, in our new gizmo plugin, override
:ref:`_create_gizmo()<class_EditorNode3DGizmoPlugin_private_method__create_gizmo>`, so it returns our custom gizmo implementation
for the Node3D nodes we want to target.

::

    # my_custom_gizmo_plugin.gd
    extends EditorNode3DGizmoPlugin


    const MyCustomNode3D = preload("res://addons/my-addon/my_custom_node_3d.gd")
    const MyCustomGizmo = preload("res://addons/my-addon/my_custom_gizmo.gd")


    func _init():
        create_material("main", Color(1, 0, 0))
        create_handle_material("handles")


    func _create_gizmo(node):
        if node is MyCustomNode3D:
            return MyCustomGizmo.new()
        else:
            return null

This way all the gizmo logic and drawing methods can be implemented in a new class extending
:ref:`EditorNode3DGizmo<class_EditorNode3DGizmo>`, like so:

::

    # my_custom_gizmo.gd
    extends EditorNode3DGizmo


    # You can store data in the gizmo itself (more useful when working with handles).
    var gizmo_size = 3.0


    func _redraw():
        clear()

        var node3d = get_node_3d()

        var lines = PackedVector3Array()

        lines.push_back(Vector3(0, 1, 0))
        lines.push_back(Vector3(gizmo_size, node3d.my_custom_value, 0))

        var handles = PackedVector3Array()

        handles.push_back(Vector3(0, 1, 0))
        handles.push_back(Vector3(gizmo_size, node3d.my_custom_value, 0))

        var material = get_plugin().get_material("main", self)
        add_lines(lines, material, false)

        var handles_material = get_plugin().get_material("handles", self)
        add_handles(handles, handles_material, [])


    # You should implement the rest of handle-related callbacks
    # (_get_handle_name(), _get_handle_value(), _commit_handle(), ...).

Note that we just added some handles in the `_redraw` method, but we still need to implement
the rest of handle-related callbacks in :ref:`EditorNode3DGizmo<class_EditorNode3DGizmo>`
to get properly working handles.
