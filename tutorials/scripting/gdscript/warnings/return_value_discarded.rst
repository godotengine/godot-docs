RETURN_VALUE_DISCARDED
======================

The warning message is:

.. code-block:: none

    The function "get_number()" returns a value that will be discarded if not used.

The default warning level for this warning is **Ignore**.
To modify it, set :ref:`Project Settings > Debug > GDScript > Warnings > Return Value Discarded<class_ProjectSettings_property_debug/gdscript/warnings/return_value_discarded>`.

When this warning occurs
------------------------

This warning may appear if a method returns a value, but that value is not used in an expression or assigned to a variable:

.. code-block::

    func _ready():
        print("About to get a number...")
        get_number()  # Will give warning RETURN_VALUE_DISCARDED.
        print("Got a number!")

    func get_number() -> int:
        return 5

How to fix this warning
-----------------------

Assign the returned value to a variable for use later.

.. code-block::
    
    func _ready():
        print("About to get a number...")
        var num = get_number()
        print("Got a number! It's %s" % num)

However, some methods in Godot's APIs return values that are not necessary to store. As such, depending on the situation, it may make more sense to ignore this warning.

