UNASSIGNED_VARIABLE_OP_ASSIGN
=================================

The warning message is:

.. code-block:: none

    The variable "my_counter" is modified with the compound-assignment operator "+=" but was not previously initialized.

The default warning level for this warning is **Warn**.
To modify it, set :ref:`Project Settings > Debug > GDScript > Warnings > Unassigned Variable Op Assign<class_ProjectSettings_property_debug/gdscript/warnings/unassigned_variable_op_assign>`.

When this warning occurs
------------------------

This warning may appear when attempting to use one of the compound-assignment operators, like ``+=``, ``-=``, ``*=``, or ``/=``, on a variable that hasn't had a value assigned to it yet.

.. code-block::

    var my_counter: int
    my_counter += 1

Compound-assignment operators are shorthand for performing a binary math operation and an assignment operation. The above example is equivalent to:

.. code-block::

    var my_counter: int
    my_counter = my_counter + 1

Here, the variable ``my_counter`` hasn't been given a value at the time that the code attempts to use the value from ``my_counter`` in order to calculate the new value for it.

How to fix this warning
-----------------------

Assign an initial value to the variable before attempting to use a compound-assignment operator with it:

.. code-block::

    var my_counter: int = 0
    my_counter += 1



