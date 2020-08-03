.. _doc_inspector_plugins:

Inspector plugins
=================

The inspector dock supports custom plugins to create your own widgets for
editing properties. This can be beneficial when working with custom datatypes
and resources, but may be used to change the default behavior for built-in
types as well. It is possible to introduce custom controls for specific properties,
entire objects, and even detached controls associated with particular datatypes.

This tutorial explains how to use the :ref:`class_EditorInspectorPlugin` 
and :ref:`class_EditorProperty` classes to create a custom control for each
property of the integer type, replacing the default behavior with a button 
that generates random values between numbers 0 and 99.

.. figure:: img/inspector_plugin_example.png
   :align: center

   The default behavior on the left, and the end result on the right.


Setup
-----

Follow the :ref:`doc_making_plugins` guide to setup the framework for your 
new plugin. Lets assume you've called your plugin folder ``my_inspector_plugin``.
If so, you should end up with a new ``addons/my_inspector_plugin`` folder 
that contains two files: ``plugin.cfg`` and ``plugin.gd``.

As before, ``plugin.gd`` is a script extending :ref:`class_EditorPlugin` and you
need to introduce new code for its ``_enter_tree`` and ``_exit_tree`` methods. To
setup your inspector plugin you must load its script and then create and add
the instance using ``add_inspector_plugin``. If the plugin is disabled you should 
remove the instance you have added using ``remove_inspector_plugin``.

.. note:: Take note, that here you are loading a script and not a packed scene.
          Therefore you should use ``new()`` instead of ``instance()``.

.. tabs::
  .. code-tab:: gdscript GDScript
    # plugin.gd
    tool
    extends EditorPlugin

    var plugin


    func _enter_tree():
        plugin = preload("res://addons/my_inspector_plugin/MyInspectorPlugin.gd").new()
        add_inspector_plugin(plugin)


    func _exit_tree():
        remove_inspector_plugin(plugin)


EditorInspectorPlugin
---------------------

To be able to interact with the inspector dock, your ``MyInspectorPlugin.gd`` script
must extend the :ref:`class_EditorInspectorPlugin` class. This class provides 
several virtual methods that can be implemented to affect the way the inspector 
is handling properties.

To have any effect at all the script must implement the ``can_handle()`` method. This
function is called for each edited :ref:`class_Object` and must return ``true`` if 
this plugin should handle the object or its properties (including any :ref:`class_Resource`
that is embedded!).

There are 4 other methods that can be implemented to add controls to the inspector at
specific positions. The ``parse_begin()`` and ``parse_end()`` functions are called only once
at the beginning and the end of parsing for each object, respectively. They can be used to
add controls at the very top or very bottom of the inspector layout with ``add_custom_control``.

As the object is parsed the ``parse_category()`` and ``parse_property()`` functions are 
called. In addition to ``add_custom_control`` both ``add_property_editor`` and 
``add_property_editor_for_multiple_properties`` can be utilized. These methods are used
specifically to add :ref:`class_EditorProperty`-based controls.

.. tabs::
 .. code-tab:: gdscript GDScript

    # MyInspectorPlugin.gd
    extends EditorInspectorPlugin

    var RandomIntEditor = preload("res://addons/my_inspector_plugin/RandomIntEditor.gd")


    func can_handle(object):
        # We will support all objects in this example.
        return true


    func parse_property(object, type, path, hint, hint_text, usage):
        # We will handle properties of type integer.
        if type == TYPE_INT:
            # Create an instance of the custom property editor and register
            # it to a specific property path.
            add_property_editor(path, RandomIntEditor.new())
            # Inform the editor to remove the default property editor for 
            # this property type.
            return true
        else:
            return false


EditorProperty
--------------

The :ref:`class_EditorProperty` class is a special type of :ref:`class_Control` that
can interact with edited objects inside of the inspector dock. By itself it doesn't
display anything, but can house any other control nodes, including complex
scenes.

There are three essential parts to the script extending :ref:`class_EditorProperty`:

1. There must be the ``_init`` method that sets up the node structure of the control.

2. The ``update_property()`` method should be implemented to handle changes to the 
   data from the outside.

3. A signal must be emitted at some point to inform the inspector that the control has
   changed the property using ``emit_changed``.

You can display your custom widget in two ways. Use the default ``add_child`` method
to display it to the right of the property name, and ``set_bottom_editor`` to position
it below the name.

.. tabs::
 .. code-tab:: gdscript GDScript

    # RandomIntEditor.gd
    extends EditorProperty


    # The main control for editing the property.
    var property_control = Button.new()
    # An internal value of the property.
    var current_value = 0
    # A guard against internal changes when the property is updated.
    var updating = false


    func _init():
        # Add the control as a direct child of EditorProperty node.
        add_child(property_control)
        # Make sure the control is able to retain the focus.
        add_focusable(property_control)
        # Setup the initial state and connect to the signal to track changes.
        property_control.text = "Value: " + str(current_value)
        property_control.connect("pressed", self, "_on_button_pressed")


    func _on_button_pressed():
        # Ignore the signal if the property is currently being updated.
        if (updating):
            return
        
        # Generate a new random integer between 0 and 99.
        current_value = randi() % 100
        property_control.text = "Value: " + str(current_value)
        emit_changed(get_edited_property(), current_value)


    func update_property():
        # Read the current value from the property.
        var new_value = get_edited_object()[get_edited_property()]
        if (new_value == current_value):
            return
        
        # Update the control with the new value.
        updating = true
        current_value = new_value
        property_control.text = "Value: " + str(current_value)
        updating = false


Using the example code above you should be able to make a custom widget
that replaces the default :ref:`class_SpinBox` control for integers with
a :ref:`class_Button` that generates random values.
