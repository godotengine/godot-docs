INTEGER_DIVISION
================

The warning message is:

.. code-block:: none

    Integer division. Decimal part will be discarded.

The default warning level for this warning is **Warn**.
To modify it, set :ref:`Project Settings > Debug > GDScript > Warnings > Integer Division<class_ProjectSettings_property_debug/gdscript/warnings/integer_division>`.

When this warning occurs
------------------------

This warning may appear when attempting to divide two integers:

.. code-block::

    var result = 5 / 3  # Will give warning INTEGER_DIVISION.

Because both operands are integers, the result will be an integer as well. Integers can't store fractional parts of numbers, so the result must be a whole number. Godot discards anything after the decimal point in the mathematical result to obtain the integer result. **Note that the number is not rounded to the nearest whole number.**


How to fix this warning
-----------------------

Use a floating-point number (``float``) for at least one operand of the division operation:

.. code-block::

    var result = 5.0 / 3

If the integers being divided are variables, cast them to ``float``:

.. code-block::

    var a: int = 5
    var b: int = 3
    var result = float(a) / float(b)

