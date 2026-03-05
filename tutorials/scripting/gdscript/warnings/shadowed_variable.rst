SHADOWED_VARIABLE
=================

The warning message is:

.. code-block:: none

    The local variable "level" is shadowing an already-declared variable at line 3 in the current class.

The default warning level for this warning is **Warn**.
To modify it, set :ref:`Project Settings > Debug > GDScript > Warnings > Shadowed Variable<class_ProjectSettings_property_debug/gdscript/warnings/shadowed_variable>`.

When this warning occurs
------------------------

This warning may appear when giving something the same name as a variable previously defined in the class.

.. code-block::

    extends Node

    var level = 3

    func _ready():
        # Will give warning SHADOWED_VARIABLE.
        var level = 1
        print("Time for level %s" % level)

In this example, the script class has a property ``level`` which can be accessed from its functions. However, at the first line of ``_ready()``, a new ``level`` variable is declared for that function specifically. After this declaration, any references to ``level`` will go to that version and not the shared variable for the class. This is called *shadowing*.


How to fix this warning
-----------------------

Change the name to something that isn't being used by the class. For example, if receiving a warning about using the identifier ``level``, consider using something more descriptive like ``new_level``.



