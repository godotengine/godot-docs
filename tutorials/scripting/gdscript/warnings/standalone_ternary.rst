STANDALONE_TERNARY
======================

The warning message is:

.. code-block:: none

    Standalone ternary operator (the return value is being discarded).

The default warning level for this warning is **Warn**.
To modify it, set :ref:`Project Settings > Debug > GDScript > Warnings > Standalone Ternary<class_ProjectSettings_property_debug/gdscript/warnings/standalone_ternary>`.

When this warning occurs
------------------------

This warning may appear when writing a ternary expression that is not being assigned to anything or passed into a function:

.. code-block::

    # Will give warning STANDALONE_TERNARY.
    3 if visible else 0

This ternary expression will return either ``3`` or ``0``, but that value won't carry over to anything or have any effect on the program.

The warning may also appear when using a ternary operator to call different functions based on a condition:

.. code-block::

    # Will give warning STANDALONE_TERNARY.
    chase_player() if can_see_player() else be_idle()



How to fix this warning
-----------------------

If the possible return values from the ternary expression are important, assign them to a variable so they aren't lost:

.. code-block::

    var number = 3 if visible else 0

For calling different functions as seen in the second example, consider splitting it into an if-else statement. While it takes a few more lines, they will be shorter and easier to read.

.. code-block::

    if can_see_player():
        chase_player()
    else:
        be_idle()



