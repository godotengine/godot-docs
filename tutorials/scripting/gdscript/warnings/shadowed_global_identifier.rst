SHADOWED_GLOBAL_IDENTIFIER
==============================

The warning message is:

.. code-block:: none

    The variable "char" has the same name as a built-in function.

The default warning level for this warning is **Warn**.
To modify it, set :ref:`Project Settings > Debug > GDScript > Warnings > Shadowed Global Identifier<class_ProjectSettings_property_debug/gdscript/warnings/shadowed_global_identifier>`.

When this warning occurs
------------------------

This warning may appear when using a name for something that is already being used for a global identifier. Global identifiers include:

* built-in functions (like ``char`` or ``convert``),
* native classes (like ``Node`` or ``Area2D``),
* global classes defined in another script file,
* and built-in types (like ``int`` or ``String``).

When something is *shadowed*, its name is taken by something else, and as such, it can't be accessed anymore within that scope. For example, if you used the code:

.. code-block::

    var char = "A"  # Will give warning SHADOWED_GLOBAL_IDENTIFIER.

and later within this block of code, you wanted to convert an ``int`` ASCII/Unicode character point into a ``String`` (that's what the ``char()`` function does), you would be out of luck.


How to fix this warning
-----------------------

Change the name of the identifier to something else that isn't the same as a global identifier.

.. code-block::

    var letter = "A"

This code would not cause the warning to appear, since ``letter`` is not a global identifier.

