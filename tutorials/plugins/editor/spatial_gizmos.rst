.. _doc_spatial_gizmo_plugins:

Spatial gizmo plugins
=====================

Introduction
------------

Spatial gizmo plugins are used by the editor and custom plugins to define the
gizmos attached to any kind of Spatial node.

This tutorial will show you the two main approaches to defining your own custom
gizmos. The first option works well for simple gizmos and creates less clutter in
your plugin structure, while the second one will let you store some per-gizmo data.

.. note:: This tutorial assumes you already know how to make generic plugins. If
          in doubt, refer to the :ref:`doc_making_plugins` page.

The EditorSpatialGizmoPlugin
----------------------------

Regardless of the approach we choose, we will need to create a new
:ref:`EditorSpatialGizmoPlugin <class_EditorSpatialGizmoPlugin>`. This will allow
us to set a name for the new gizmo type and define other behaviors such as whether
the gizmo can be hidden or not.

This would be a basic setup:

::

    # MyCustomGizmoPlugin.gd

    extends EditorSpatialGizmoPlugin

    func get_name():
        return "CustomNode"


::

    # MyCustomEditorPlugin.gd

    tool
    extends EditorPlugin

    const MyCustomGizmoPlugin = preload("res://addons/my-addon/MyCustomGizmoPlugin.gd")

    var gizmo_plugin = MyCustomGizmoPlugin.new()

    func _enter_tree():
        add_spatial_gizmo_plugin(gizmo_plugin)

    func _exit_tree():
        remove_spatial_gizmo_plugin(gizmo_plugin)


For simple gizmos, just inheriting :ref:`EditorSpatialGizmoPlugin <class_EditorSpatialGizmoPlugin>`
is enough. If you want to store some per-gizmo data or you are porting a Godot 3.0 gizmo
to 3.1+, you should go with the second approach.


Simple approach
---------------

The first step is to, in our custom gizmo plugin, override the :ref:`has_gizmo()<class_EditorSpatialGizmoPlugin_method_has_gizmo>`
method so that it returns ``true`` when the spatial parameter is of our target type.

::

    # ...

    func has_gizmo(spatial):
        return spatial is MyCustomSpatial
    # ...

Then we can override methods like :ref:`redraw()<class_EditorSpatialGizmoPlugin_method_redraw>`
or all the handle related ones.

::

    # ...

    func _init():
        create_material("main", Color(1, 0, 0))
        create_handle_material("handles")

    func redraw(gizmo):
        gizmo.clear()

        var spatial = gizmo.get_spatial_node()

        var lines = PoolVector3Array()

        lines.push_back(Vector3(0, 1, 0))
        lines.push_back(Vector3(0, spatial.my_custom_value, 0))

        var handles = PoolVector3Array()

        handles.push_back(Vector3(0, 1, 0))
        handles.push_back(Vector3(0, spatial.my_custom_value, 0))

        gizmo.add_lines(lines, get_material("main", gizmo), false)
        gizmo.add_handles(handles, get_material("handles", gizmo))

    # ...

Note that we created a material in the `_init` method, and retrieved it in the `redraw`
method using :ref:`get_material()<class_EditorSpatialGizmoPlugin_method_get_material>`. This
method retrieves one of the material's variants depending on the state of the gizmo
(selected and/or editable).

So the final plugin would look somewhat like this:

::

    extends EditorSpatialGizmoPlugin

    const MyCustomSpatial = preload("res://addons/my-addon/MyCustomSpatial.gd")

    func _init():
        create_material("main", Color(1,0,0))
        create_handle_material("handles")

    func has_gizmo(spatial):
        return spatial is MyCustomSpatial

    func redraw(gizmo):
        gizmo.clear()

        var spatial = gizmo.get_spatial_node()

        var lines = PoolVector3Array()

        lines.push_back(Vector3(0, 1, 0))
        lines.push_back(Vector3(0, spatial.my_custom_value, 0))

        var handles = PoolVector3Array()

        handles.push_back(Vector3(0, 1, 0))
        handles.push_back(Vector3(0, spatial.my_custom_value, 0))

        gizmo.add_lines(lines, get_material("main", gizmo), false)
        gizmo.add_handles(handles, get_material("handles", gizmo))

    # you should implement the rest of handle-related callbacks
    # (get_handle_name(), get_handle_value(), commit_handle()...)

Note that we just added some handles in the redraw method, but we still need to implement
the rest of handle-related callbacks in :ref:`EditorSpatialGizmoPlugin <class_EditorSpatialGizmoPlugin>`
to get properly working handles.

Alternative approach
--------------------

In some cases we want to provide our own implementation of :ref:`EditorSpatialGizmo<class_EditorSpatialGizmo>`,
maybe because we want to have some state stored in each gizmo or because we are porting
an old gizmo plugin and we don't want to go through the rewriting process.

In these cases all we need to do is, in our new gizmo plugin, override
:ref:`create_gizmo()<class_EditorSpatialGizmoPlugin_method_create_gizmo>`, so it returns our custom gizmo implementation
for the Spatial nodes we want to target.

::

    # MyCustomGizmoPlugin.gd
    extends EditorSpatialGizmoPlugin

    const MyCustomSpatial = preload("res://addons/my-addon/MyCustomSpatial.gd")
    const MyCustomGizmo = preload("res://addons/my-addon/MyCustomGizmo.gd")

    func _init():
        create_material("main", Color(1, 0, 0))
        create_handle_material("handles")

    func create_gizmo(spatial):
        if spatial is MyCustomSpatial:
            return MyCustomGizmo.new()
        else:
            return null

This way all the gizmo logic and drawing methods can be implemented in a new class extending
:ref:`EditorSpatialGizmo<class_EditorSpatialGizmo>`, like so:

::

    # MyCustomGizmo.gd

    extends EditorSpatialGizmo

    # You can store data in the gizmo itself (more useful when working with handles)
    var gizmo_size = 3.0

    func redraw():
        clear()

        var spatial = get_spatial_node()

        var lines = PoolVector3Array()

        lines.push_back(Vector3(0, 1, 0))
        lines.push_back(Vector3(gizmo_size, spatial.my_custom_value, 0))

        var handles = PoolVector3Array()

        handles.push_back(Vector3(0, 1, 0))
        handles.push_back(Vector3(gizmo_size, spatial.my_custom_value, 0))

        var material = get_plugin().get_material("main", self)
        add_lines(lines, material, false)

        var handles_material = get_plugin().get_material("handles", self)
        add_handles(handles, handles_material)

    # you should implement the rest of handle-related callbacks
    # (get_handle_name(), get_handle_value(), commit_handle()...)

Note that we just added some handles in the redraw method, but we still need to implement
the rest of handle-related callbacks in :ref:`EditorSpatialGizmo<class_EditorSpatialGizmo>`
to get properly working handles.
