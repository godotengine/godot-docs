ASSERT_ALWAYS_TRUE
======================

The warning message is:

.. code-block:: none

    Assert statement is redundant because the expression is always true.

The default warning level for this warning is **Warn**.
To modify it, set :ref:`Project Settings > Debug > GDScript > Warnings > Assert Always True<class_ProjectSettings_property_debug/gdscript/warnings/assert_always_true>`.

When this warning occurs
------------------------

The :ref:`assert() <class_@GDScript_method_assert>` keyword can be used to ensure that a given condition is met before allowing code execution to continue. If the first argument passed to it evaluates to ``true``, the rest of the function will run as expected; if it is ``false``, then the project will stop.

If ``assert()`` is passed an expression that is guaranteed to be ``true``, then the ``assert()`` call will never stop the project, thus making it redundant.

.. code-block::

    # The boolean true will always be true, so this assert will never stop
    # the program.
    assert(true, "True is false, somehow?")

    # Likewise, 3 will never be equal to 4, so this assert will never stop
    # the program.
    assert(3 != 4, "3 is equal to 4")

How to fix this warning
-----------------------

Remove the ``assert()`` statement from your code.



