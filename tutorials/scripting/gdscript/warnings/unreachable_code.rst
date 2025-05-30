UNREACHABLE_CODE
====================

The warning message is:

.. code-block:: none

    Unreachable code (statement after return) in function "_ready()".

The default warning level for this warning is **Warn**.
To modify it, see :ref:`ProjectSettings.debug/gdscript/warnings/unreachable_code<class_ProjectSettings_property_debug/gdscript/warnings/unreachable_code>`.

When this warning occurs
------------------------

This warning may appear if there is code that can never be reached because all possible code paths before it would hit a ``return`` statement and leave a function:

.. code-block::

    func calculate_num(a):
        if a > 5:
            return 10
        else:
            return 3

        print("Returning zero")
        return 0

In this function, there are only two ways the code can be run:

* If ``a`` is greater than ``5``, the function will return ``10``, and the print statement will not be reached.
* If ``a`` is equal to or less than ``5``, the function will return ``3``, and again the print statement will not be reached.

There is no way for code execution to get past the if-else block and to the print statement.

How to fix this warning
-----------------------

If you want the code marked with the warning to be run, modify your function's logic so that there is a path to that code.

.. code-block::

    func calculate_num(a):
        if a > 5:
            return 10
        elif a > 2:  # Now this condition can be false, and the print statement can be reached.
            return 3

        print("Returning zero")
        return 0

If the code with the warning isn't important, then remove it.

.. code-block::

    func calculate_num(a):
        if a > 5:
            return 10
        else:
            return 3


