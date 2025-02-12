ASSERT_ALWAYS_FALSE
=======================

The warning message is:

.. code-block:: none

    Assert statement will raise an error because the expression is always false.

When this warning occurs
------------------------

The :ref:`assert() <class_@GDScript_method_assert>` keyword can be used to ensure that a given condition is met before allowing code execution to continue. If the first argument passed to it evaluates to ``true``, the rest of the function will run as expected; if it is ``false``, then the project will stop.

If ``assert()`` is passed an expression that is guaranteed to be ``false``, then the ``assert()`` call will always stop the project.

.. code-block::

    # The boolean false will always be false, so this assert will always stop
    # the program.
    assert(false, "False is false")

    # Likewise, 5 will never be 6, so this assert will always stop the program.
    assert(5 == 6, "5 isn't equal to 6")

    # This line of code won't be executed in debug builds because the editor
    # will have stopped at the assert calls above.
    print("Hello, world!")

How to fix this warning
-----------------------

Assuming you want code following the ``assert()`` to run, remove it from your code. If you do want code execution to stop at that point, :ref:`consider using breakpoints instead <doc_debugger_tools_and_options>`.



