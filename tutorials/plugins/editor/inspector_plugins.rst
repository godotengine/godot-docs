.. _doc_inspector_plugins:

Inspector Plugins
=====================

Introduction
------------

Godot 3.1 comes with a new inspector. Adding plugins to it is now possible.

This tutorial will explain the process.


Inspector Plugin
----------------

This short tutorial will explain how to make a simple value editor.
Create an EditorInspectorPlugin first. This is needed to initialize your plugin.


.. tabs::
 .. code-tab:: gdscript GDScript
    
    # MyEditorPlugin.gd 
    
    extends EditorInspectorPlugin
    
    func can_handle(object):
        # if only editing a specific type
        # return object is TheTypeIWant
        # if everything is supported
        return true

    func parse_property(object,type,path,hint,hint_text,usage):
        if (type==TYPE_INT):
             add_custom_property_editor(path,MyEditor.new())
             return true # I want this one
        else:
             return false


Editor
------


Here is an editor for editing integers

.. tabs::
 .. code-tab:: gdscript GDScript
    
    # MyEditor.gd 
    extends EditorProperty
    class_name MyEditor

    var updating = false

    func _spin_changed(value):
        if (updating):
            return

        emit_changed( get_edited_property(), value )

    func update_property():
        var new_value = get_edited_object()[ get_edited_property() ]

        updating=true
        spin.set_value( new_value )
        updating=false

    var spin = EditorSpinSlider.new() # use the new spin slider
    func _init():
       # if you want to put the editor below the label
       #   set_bottom_editor( spin )
       # else use:
       add_child( spin )
       # to remember focus when selected back
       add_focusable( spin ) 
       spin.set_min(0)
       spin.set_max(1000)
       spin.connect("value_changed",self,"_spin_changed")
     



