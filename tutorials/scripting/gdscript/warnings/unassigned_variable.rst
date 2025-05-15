UNASSIGNED_VARIABLE
=======================

The warning message is:

.. code-block:: none

    The variable "my_var" is used before being assigned a value.

The default warning level for this warning is **Warn**.
To modify it, see :ref:`ProjectSettings.debug/gdscript/warnings/unassigned_variable<class_ProjectSettings_property_debug/gdscript/warnings/unassigned_variable>`.

When this warning occurs
------------------------

This warning may appear when attempting to use a variable that hasn't had a value assigned to it yet.

.. code-block::

    var my_var
    print(my_var)

Without having a value assigned to the variable, Godot may not know what to do with it.

How to fix this warning
-----------------------

Assign a value to the variable before including it in an expression or function call:

.. code-block::

    var my_var = 5
    print(my_var)



