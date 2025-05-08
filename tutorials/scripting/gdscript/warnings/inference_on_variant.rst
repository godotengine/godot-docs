INFERENCE_ON_VARIANT
========================

The warning message is:

.. code-block:: none

    The variable type is being inferred from a Variant value, so it will be typed as Variant.

The default warning level for this warning is **Error**.
To modify it, see :ref:`ProjectSettings.debug/gdscript/warnings/inference_on_variant<class_ProjectSettings_property_debug/gdscript/warnings/inference_on_variant>`.

When this warning occurs
------------------------

This warning may appear when using the ``:=`` operator to declare a variable with an inferred type, when the inferred type is Variant.

.. code-block::

    func _ready():
        var my_var := get_value()  # Will give warning INFERENCE_ON_VARIANT.

    func get_value():
        return 3

Because the return type of ``get_value()`` isn't explicitly stated to be ``int``, Godot won't assume that it only returns an ``int``, and thus will consider its return type to be ``Variant``. The ``:=`` operator will then only be able to set the type of ``my_var`` to ``Variant``, which is effectively the same as not setting a type for ``my_var`` at all.

How to fix this warning
-----------------------

If initializing a variable based on the return value of a function (like in the example above), give the function an explicit return type:

.. code-block::
    func get_value() -> int:
        return 3

