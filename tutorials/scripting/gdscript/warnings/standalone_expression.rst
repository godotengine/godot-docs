STANDALONE_EXPRESSION
=========================

The warning message is:

.. code-block:: none

    Standalone expression (the line may have no effect).

The default warning level for this warning is **Warn**.
To modify it, see :ref:`ProjectSettings.debug/gdscript/warnings/standalone_expression<class_ProjectSettings_property_debug/gdscript/warnings/standalone_expression>`.

When this warning occurs
------------------------

This warning may appear when writing an expression that is not assigned to anything or passed to a function:

.. code-block::

    # Will give warning STANDALONE_EXPRESSION.
    (5 * 3) + 2

This expression evaluates to the integer value ``17``, but after that, nothing happens to or with it.

Note that the warning states the expression *may* have no effect, not that it *won't* have an effect. If the expression includes a function call that ends up doing more than just returning a value, the line itself ultimately will have an effect.

.. code-block::

    extends Node

    var counter = 0

    func _ready():
        # Will give warning STANDALONE_EXPRESSION.
        (5 * 3) + 2 * add_to_val(3)

    func add_to_val(val) -> int:
        counter += 1
        return val + 2

Here, the line in ``_ready()`` receives the ``STANDALONE_EXPRESSION`` warning, even though the call to ``add_to_val()`` changes the ``counter`` property. The other math calculations won't have any effect.

How to fix this warning
-----------------------

If you've written an expression in your code, it's likely because you intended to use it for something. Make sure you're assigning it to a variable or passing it to a function.

If you're certain that you don't need the expression for anything, remove it. Make sure to keep function calls that may have side effects (such as the ``add_to_val()`` call in the example above).



