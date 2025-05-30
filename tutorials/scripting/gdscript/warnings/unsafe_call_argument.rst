UNSAFE_CALL_ARGUMENT
========================

The warning message is:

.. code-block:: none

    The argument 1 of the function "set_health()" requires the subtype "int" but the supertype "Variant" was provided.

The default warning level for this warning is **Ignore**.
To modify it, see :ref:`ProjectSettings.debug/gdscript/warnings/unsafe_call_argument<class_ProjectSettings_property_debug/gdscript/warnings/unsafe_call_argument>`.

When this warning occurs
------------------------

This warning may appear when passing a value of a certain type to a function that is expecting a subtype instead.

.. code-block::

    var original_health = 10

    func _ready():
        set_health(original_health)  # Will give warning UNSAFE_CALL_ARGUMENT.

    func set_health(new_health: int):
        current_health = new_health

Because the type of ``original_health`` was not explicitly stated, it is inferred to be a ``Variant``. The ``Variant`` type is broader than the ``int`` type expected by the ``set_health()`` function, so it is possible that the variable ``original_health`` could hold a kind of value incompatible with it.

This warning may also appear when other supertypes are passed in to functions:

.. code-block::

    @export var my_node: Node2D

    func _ready():
        make_node_invisible(my_node)  # Will give warning UNSAFE_CALL_ARGUMENT.

    func make_node_invisible(node: Sprite2D):
        node.visible = false

Here, the ``make_node_invisible()`` function expects a ``Sprite2D`` to be passed to it, but in ``_ready()`` it is receiving a ``Node2D`` (a supertype/parent type) instead.

How to fix this warning
-----------------------

When passing a value to a function, ensure that the data type of the value is the same as or a subtype of the type the function expects. Often, this may involve explicitly stating the type of a variable to ensure it isn't implicitly a ``Variant``.

.. code-block::

    var original_health: int = 10

    func _ready():
        set_health(original_health)

    func set_health(new_health: int):
        current_health = new_health

