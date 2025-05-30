STATIC_CALLED_ON_INSTANCE
=============================

The warning message is:

.. code-block:: none

    The function "do_static_thing()" is a static function but was called from an instance. Instead, it should be directly called from the type: "MyClass.do_static_thing()".

The default warning level for this warning is **Warn**.
To modify it, see :ref:`ProjectSettings.debug/gdscript/warnings/static_called_on_instance<class_ProjectSettings_property_debug/gdscript/warnings/static_called_on_instance>`.

When this warning occurs
------------------------

..
    It's been a problem with other pages too, but I worry this is getting a bit repetitive with the original warning message.

This warning may appear when attempting to call a static function on an instance.

.. code-block::

    class MathFuncs:
        static func subtract_two(val):
            return val - 2

    func _ready():
        var my_math_funcs = MathFuncs.new()

        # Will give warning STATIC_CALLED_ON_INSTANCE.
        var result = my_math_funcs.subtract_two(5)

When a function is *static*, it belongs to the class as a whole, not any one specific instance of the class. See :ref:`Static variables <doc_gdscript_basics_static_variables>` and :ref:`Static functions <doc_gdscript_basics_static_functions>` for more information.

There is often no need to call a static function on an instance of a class. In the example above, the function ``subtract_two()`` will always perform the same operation; one instance of the ``MathFuncs`` class would never return a different value than another instance. As such, when the user tries to call ``subtract_two()`` from an instance of ``MathFuncs``, it suggests the user may not understand what the function does.

How to fix this warning
-----------------------

Don't use an instance of the class to access the function. Instead, use the class name itself:

.. code-block::

    var result = MathFuncs.subtract_two(5)



