UNASSIGNED_VARIABLE
===================

The warning message is:

.. code-block:: none

    The variable "my_var" is used before being assigned a value.

The default warning level for this warning is **Warn**.
To modify it, set :ref:`Project Settings > Debug > GDScript > Warnings > Unassigned Variable<class_ProjectSettings_property_debug/gdscript/warnings/unassigned_variable>`.

When this warning occurs
------------------------

This warning may appear when attempting to use a variable that hasn't had a value assigned to it yet.

.. code-block::

    var my_var
    print(my_var)

By default, the variable will be ``null``. However, Godot considers this a warning because the user did not explicitly assign the value, and as such might be unaware of it.

How to fix this warning
-----------------------

Assign a value to the variable before including it in an expression or function call:

.. code-block::

    var my_var = 5
    print(my_var)



