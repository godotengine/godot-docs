INT_AS_ENUM_WITHOUT_CAST
============================

The warning message is:

.. code-block:: none

    Integer used when an enum value is expected. If this is intended, cast the integer to the enum type using the "as" keyword.

The default warning level for this warning is **Warn**.
To modify it, set :ref:`Project Settings > Debug > GDScript > Warnings > Int as Enum Without Cast<class_ProjectSettings_property_debug/gdscript/warnings/int_as_enum_without_cast>`.

When this warning occurs
------------------------

This warning may appear when attempting to use an integer value in place of an enum value:

.. code-block::

    var my_var: MyEnum
    my_var = 1  # Will give warning INT_AS_ENUM_WITHOUT_CAST.

How to fix this warning
-----------------------

Cast the integer value to the enum type.

.. code-block::
    
    var my_var: MyEnum
    my_var = 1 as MyEnum
