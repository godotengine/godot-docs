NATIVE_METHOD_OVERRIDE
==========================

The warning message is:

.. code-block:: none

    The method "get_class()" overrides a method from native class "Object". This won't be called by the engine and may not work as expected.

The default warning level for this warning is **Error**.
To modify it, see :ref:`ProjectSettings.debug/gdscript/warnings/native_method_override<class_ProjectSettings_property_debug/gdscript/warnings/native_method_override>`.

When this warning occurs
------------------------

This warning may appear if you try to define a method in a script that has the same name as a native class's method:

.. code-block::

    extends Node

    func get_class():  # Will give warning NATIVE_METHOD_OVERRIDE.
        return "MyCoolClass"

Here, ``get_class()`` is a method on ``Object``. When Godot tries to call this class's ``get_class()`` method internally, it will use its own internal method, not the one the user has defined here.

How to fix this warning
-----------------------

Name the function something else:

.. code-block::

    func get_class_name():  # Will not give a warning.
        return "MyCoolClass"

(Note that doing this still won't override the behavior of a native method.)
