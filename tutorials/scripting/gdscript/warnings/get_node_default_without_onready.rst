GET_NODE_DEFAULT_WITHOUT_ONREADY
================================

This warning appears when a node's property is initialized to a location in the scene tree without using the ``@onready`` annotation.

Depending on how you attempt to access the scene tree, the warning message will be one of the following:

.. code-block:: none

    The default value uses "get_node()" which won't return nodes in the scene tree before "_ready()" is called. Use the "@onready" annotation to solve this.

    The default value uses "$" which won't return nodes in the scene tree before "_ready()" is called. Use the "@onready" annotation to solve this.

    The default value uses "%" which won't return nodes in the scene tree before "_ready()" is called. Use the "@onready" annotation to solve this.

The default warning level for this warning is **Error**.
To modify it, set :ref:`Project Settings > Debug > GDScript > Warnings > Get Node Default Without Onready<class_ProjectSettings_property_debug/gdscript/warnings/get_node_default_without_onready>`.

When this warning occurs
------------------------

This warning may appear when attempting to assign the default value of a property to a node in the scene tree, like so:

.. code-block:: gdscript

    extends Area2D

    # Will give warning GET_NODE_DEFAULT_WITHOUT_ONREADY.
    var my_collision_shape = $CollisionShape2D

If you want a property to refer to another node in the scene tree, you may be inclined to reference it using :ref:`get_node() <class_Node_method_get_node>` (or the ``$`` and ``%`` shorthand versions) when setting its default value.

However, properties' default values are evaluated and assigned *before* the scene tree is set up. This means that when Godot tries to assign that value, the node you're referring to may not be in the scene tree yet, and the property will be set to ``null`` instead.

How to fix this warning
-----------------------

Add the ``@onready`` annotation before your property declaration:

.. code-block:: gdscript

    extends Area2D

    @onready var my_collision_shape = $CollisionShape2D

Now, the default value of the property will not be assigned until the scene tree has been initialized, at which time the node will be present.
