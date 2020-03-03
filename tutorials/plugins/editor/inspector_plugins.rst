.. _doc_inspector_plugins:

Inspector plugins
=================

The inspector dock supports custom plugins to create your own widgets for
editing properties. This tutorial explains how to use the
:ref:`class_EditorInspectorPlugin` and :ref:`class_EditorProperty` classes to
write such plugins with the example of creating a custom value editor.

Setup
-----

Just like :ref:`doc_making_plugins`, we start out by making a new plugin,
getting a ``plugin.cfg`` file created, and start with our
:ref:`class_EditorPlugin`.  However, instead of using
``add_custom_node`` or ``add_control_to_dock`` we'll use
``add_inspector_plugin``.

.. tabs::
  .. code-tab:: gdscript GDScript
    # MyEditorPlugin.gd

    tool extends EditorPlugin

    var plugin: EditorInspectorPlugin

    func _enter_tree():
        # EditorInspectorPlugin is a resource, so we use `new()` instead of `instance()`.
        plugin = preload("res://addons/MyPlugin/MyInspectorPlugin.gd").new()
        add_inspector_plugin(plugin)

    func _exit_tree():
        remove_inspector_plugin(plugin)

EditorInspectorPlugin
---------------------

To actually connect into the Inspector, we create a
:ref:`class_EditorInspectorPlugin` class. This script provides the "hooks" to
the inspector. Thanks to this class, the editor will call the functions within
the EditorInspectorPlugin while it goes through the process of building the UI
for the inspector. The script is used to check if we should enable ourselves for
any :ref:`class_Object` that is currently in the inspector (including any
:ref:`class_Resource` that is embedded!).

Once enabled, EditorInspectorPlugin has methods that allow for adding
:ref:`class_EditorProperty` nodes or just custom :ref:`class_Control` nodes to
the beginning and end of the inspector for that :ref:`class_Object`, or for
overriding or changing existing property editors.

.. tabs::
 .. code-tab:: gdscript GDScript

    # MyInspectorPlugin.gd

    extends EditorInspectorPlugin

    func can_handle(object):
        # Here you can specify which object types (classes) should be handled by
        # this plugin. For example if the plugin is specific to your player
        # class defined with `class_name MyPlayer`, you can do:
        # `return object is MyPlayer`
        # In this example we'll support all objects, so:
        return true

    func parse_property(object, type, path, hint, hint_text, usage):
        # We will handle properties of type integer.
        if type == TYPE_INT:
            # Register *an instance* of the custom property editor that we'll define next.
            add_property_editor(path, MyIntEditor.new())
            # We return `true` to notify the inspector that we'll be handling
            # this integer property, so it doesn't need to parse other plugins
            # (including built-in ones) for an appropriate editor.
            return true
        else:
            return false

EditorProperty
--------------

Next, we define the actual :ref:`class_EditorProperty` custom value editor that
we want instantiated to edit integers. This is a custom :ref:`class_Control` and
we can add any kinds of additional nodes to make advanced widgets to embed in
the inspector.

.. tabs::
 .. code-tab:: gdscript GDScript

    # MyIntEditor.gd
    extends EditorProperty
    class_name MyIntEditor

    var updating = false
    var spin = EditorSpinSlider.new()

    func _init():
       # We'll add an EditorSpinSlider control, which is the same that the
       # inspector already uses for integer and float edition.
       # If you want to put the editor below the property name, use:
       # `set_bottom_editor(spin)`
       # Otherwise to put it inline with the property name use:
       add_child(spin)
       # To remember focus when selected back:
       add_focusable(spin)
       # Setup the EditorSpinSlider
       spin.set_min(0)
       spin.set_max(1000)
       spin.connect("value_changed", self, "_spin_changed")

    func _spin_changed(value):
        if (updating):
            return
        emit_changed(get_edited_property(), value)

    func update_property():
        var new_value = get_edited_object()[get_edited_property()]
        updating = true
        spin.set_value(new_value)
        updating = false
