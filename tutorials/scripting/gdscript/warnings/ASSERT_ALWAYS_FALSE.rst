ASSERT_ALWAYS_FALSE
=======================

The warning message is:

.. code-block:: none

    Assert statement will raise an error because the expression is always false.

When this warning occurs
------------------------

The :ref:`assert() <class_@GDScript_method_assert>` keyword can be used to ensure that a given condition is met before allowing code execution to continue. If the first argument passed to it is truthy, the rest of the function will run as expected; if it is falsy, then the project will stop.

If ``assert()`` is passed something guaranteed to be falsy, then the ``assert()`` call will always stop the project.

.. code-block::

    # Zero always evaluates to false.
    assert(0, "Zero is falsy")

    # Likewise, an empty string always evaluates to false.
    assert("", "An empty string is falsy")

.. note::

    Godot will *not* raise this warning if a literal falsy boolean is passed:

    .. code-block::

        # Despite false being passed, this won't raise ASSERT_ALWAYS_FALSE.
        assert(false, "False is false")

        # This evaluates to a boolean which is false, so it also won't raise
        # the warning.
        assert(3 == 4, "3 isn't equal to 4")

    This is because ``assert(false)`` calls are often used in development to forcibly halt program execution and avoid strange errors later on.

    See `issue #58087 <https://github.com/godotengine/godot/issues/58087>`_ for more information.

How to fix this warning
-----------------------

Assuming you want code following the ``assert()`` to run, remove it from your code. If you do want code execution to stop at that point, replace the condition with ``false``, or :ref:`consider using breakpoints instead <doc_debugger_tools_and_options>`.



