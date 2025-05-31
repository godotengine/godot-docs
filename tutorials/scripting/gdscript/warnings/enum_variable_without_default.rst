ENUM_VARIABLE_WITHOUT_DEFAULT
=================================

The warning message is:

.. code-block:: none

    The variable "my_var" has an enum type and does not set an explicit default value. The default will be set to "0".

The default warning level for this warning is **Warn**.
To modify it, set :ref:`Project Settings > Debug > GDScript > Warnings > Enum Variable Without Default<class_ProjectSettings_property_debug/gdscript/warnings/enum_variable_without_default>`.

When this warning occurs
------------------------

This warning may appear when declaring a variable whose type is an enum with values assigned to its members, but the variable is not assigned a value.

.. code-block::

    enum MyEnum {
        A = 1,
        B = 2,
        C = 3
    }

    func _ready():
        var my_var: MyEnum  # Will give warning ENUM_VARIABLE_WITHOUT_DEFAULT.

Godot will usually default an enum-typed variable to the integer ``0``. However, if the enum does not have a member that corresponds to ``0``, Godot will be confused on how to assign it.

How to fix this warning
-----------------------

Provide the variable with a default value, like so:

.. code-block::

    var my_var: MyEnum = MyEnum.A

Alternatively, if the enum has a member with a value of 0, Godot will use that as the default value.

.. code-block::

    enum MyEnum {
        Z = 0,  # Will be used as the default value.
        A = 1,
        B = 2,
        C = 3
    }

    func _ready():
        var my_var: MyEnum  # Will default to MyEnum.Z.



