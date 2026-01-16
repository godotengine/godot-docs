UNUSED_VARIABLE
===============

The warning message is:

.. code-block:: none

    The local variable "counter" is declared but never used in the block. If this is intended, prefix it with an underscore: "_counter".

The default warning level for this warning is **Warn**.
To modify it, set :ref:`Project Settings > Debug > GDScript > Warnings > Unused Variable<class_ProjectSettings_property_debug/gdscript/warnings/unused_variable>`.

When this warning occurs
------------------------

This warning may appear when a variable is declared, but never used before its function or scope ends:

.. code-block::

    extends CharacterBody2D

    func _process(delta):
        var player_speed = 5.0  # Will give warning UNUSED_VARIABLE.
        velocity = Input.get_vector("ui_left", "ui_right", "ui_up", "ui_down")
        move_and_slide()

In this example, the variable ``player_speed`` is presumably meant to control how fast the player moves. However, ``velocity`` never actually takes into account this speed variable; it only uses the result of ``Input.get_vector()``. It's likely that the programmer meant to include ``player_speed`` here somehow but forgot to write it.

How to fix this warning
-----------------------

If a variable is being marked as unused, you probably meant to use it somewhere but forgot to include it in the relevant statement. Following the example above, the likely solution would be to incorporate it into the calculation of ``velocity``:

.. code-block::

    velocity = player_speed * Input.get_vector("ui_left", "ui_right", "ui_up", "ui_down")

If you're certain you don't need the variable for anything right now, but might need its value later on, prefix its name with an underscore (``_``) as the warning text suggests. Once you start referencing it elsewhere in the code, you can remove the underscore.

.. code-block::

    var _player_speed = 5.0  # Will not give warning UNUSED_VARIABLE.

If you know you won't ever need the variable, then simply delete it.

