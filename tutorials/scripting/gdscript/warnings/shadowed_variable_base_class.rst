SHADOWED_VARIABLE_BASE_CLASS
================================

The warning message is:

.. code-block:: none

    The local variable "name" is shadowing an already-declared property in the base class "Node".

The default warning level for this warning is **Warn**.
To modify it, see :ref:`ProjectSettings.debug/gdscript/warnings/shadowed_variable_base_class<class_ProjectSettings_property_debug/gdscript/warnings/shadowed_variable_base_class>`.

When this warning occurs
------------------------

This warning may appear when using a name for something that the script's base class already uses for something else.

.. code-block::

    extends Node

    func _ready():
        # Will give warning SHADOWED_VARIABLE_BASE_CLASS.
        var name = "Bob"
        print("Hi, my name is %s" % name)

In this example, the ``Node`` class already defines ``name`` as the name associated with the node itself in the scene tree and editor. Before the ``var name`` declaration, writing ``name = "MyNode"`` would have set the node's name. After the declaration, though, the same line of code would not change it. In fact, after the ``var name``, the node's name can no longer be accessed within the ``_ready()`` function. This is called *shadowing*.


How to fix this warning
-----------------------

Change the name to something that isn't being used by the base class. For example, if receiving a warning about using the identifier ``name``, consider using something more descriptive like ``char_name`` or ``item_name``.



