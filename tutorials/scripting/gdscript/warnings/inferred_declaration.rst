INFERRED_DECLARATION
========================

The warning message is:

.. code-block:: none

    "for" iterator variable "i" has an implicitly inferred static type.

The default warning level for this warning is **Ignore**.
To modify it, see :ref:`ProjectSettings.debug/gdscript/warnings/inferred_declaration<class_ProjectSettings_property_debug/gdscript/warnings/inferred_declaration>`.

When this warning occurs
------------------------

This warning may appear when creating a variable for a particular scope, such as a ``for`` loop, without specifying its type explicitly:

.. code-block::

    for i in 10:  # Will give warning INFERRED_DECLARATION. 
        print(i)

In this example, the variable ``i`` did not have its type specified. It is inferred to be an ``int``, but not outright stated in the code.

How to fix this warning
-----------------------

Provide a type specifier for the variable, like so:

.. code-block::

    for i: int in 10:  # Will not give a warning.
        print(i)
