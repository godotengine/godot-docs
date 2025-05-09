INT_AS_ENUM_WITHOUT_MATCH
=============================

The warning message is:

.. code-block:: none

    Cannot cast 3 as Enum "MyClass.MyEnum": no enum member has matching value.

The default warning level for this warning is **Warn**.
To modify it, see :ref:`ProjectSettings.debug/gdscript/warnings/int_as_enum_without_match<class_ProjectSettings_property_debug/gdscript/warnings/int_as_enum_without_match>`.

When this warning occurs
------------------------

This warning may appear when attempting to cast an integer value to an enum type, but the enum type doesn't have a member with a corresponding value.

.. code-block::

    enum MyEnum { ZERO, ONE, TWO }
    
    func _ready():
        var my_var = 3 as MyEnum  # Will give warning INT_AS_ENUM_WITHOUT_MATCH.

The purpose of the enum is to keep track of a pre-determined number of possible values. In most cases, there is no reason to assign a value outside of those pre-determined ones, so it is considered to be likely a mistake.

How to fix this warning
-----------------------

Provide a value for the enum that corresponds to the intended integer value.

.. code-block::
    
    enum MyEnum { ZERO, ONE, TWO, THREE }

    func _ready():
        var my_var = 3 as MyEnum  # Will now correspond to MyEnum.THREE.

Remember that while Godot will assign integer values to enum members by default, you can also explicitly define their corresponding values:

.. code-block::

    enum MyEnum { ZERO, ONE, TWO, TEN_THOUSAND = 10000 }
    
    func _ready():
        var my_var = 10000 as MyEnum  # Will correspond to MyEnum.TEN_THOUSAND.

Alternatively, you may just need to change the integer number you're attempting to cast as an enum value to be within the range of valid values.

.. code-block::

    enum MyEnum { ZERO, ONE, TWO }

    func _ready():
        var my_var = 2 as MyEnum  # Will correspond to MyEnum.TWO
