SHADOWED_GLOBAL_IDENTIFIER
==============================

The warning message is:

.. code-block:: none

    The variable "char" has the same name as a built-in function.

The default warning level for this warning is **Warn**.
To modify it, see :ref:`ProjectSettings.debug/gdscript/warnings/shadowed_global_identifier<class_ProjectSettings_property_debug/gdscript/warnings/shadowed_global_identifier>`.

When this warning occurs
------------------------

This warning may appear when using a name for something that is already being used for an existing:

* built-in function (like ``char`` or ``convert``),
* native class (like ``Node`` or ``Area2D``),
* global class defined in another script file,
* or built-in type (like ``int`` or ``String``).

When something is *shadowed*, its name is taken by something else, and as such, it can't be accessed anymore within that scope. For example, if you used the code:

.. code-block::

    var char = "A"

and later within this block of code, you wanted to convert an ``int`` ASCII/Unicode character point into a ``String`` (that's what the ``char()`` function does), you would be out of luck.


How to fix this warning
-----------------------

Change the name of the identifier to something else that isn't the same as a global identifier.



