CONFUSABLE_IDENTIFIER
=========================

The warning message is:

.. code-block:: none

    The identifier "my_vаr" has misleading characters and might be confused with something else.

The default warning level for this warning is **Warn**.
To modify it, set :ref:`Project Settings > Debug > GDScript > Warnings > Confusable Identifier<class_ProjectSettings_property_debug/gdscript/warnings/confusable_identifier>`.

When this warning occurs
------------------------

Some alphabets such as Cyrillic have characters that look like Latin (such as English, Spanish, etc.) characters, but are actually different.

.. code-block::

    var engine_nаme = "Godot"
    print(engine_name)

In this code snippet, the ``print`` statement would fail, because ``engine_name`` is actually not defined. The identifier in the ``print`` statement uses the Latin character "a" (U+0061), while the identifier in the variable declaration above uses the Cyrillic character "а" (U+0430).

How to fix this warning
-----------------------

Avoid using Cyrillic or other alphabets' characters that are visually similar to Latin ones. A good rule of thumb is to prefer the Latin alphabet for program identifiers.



