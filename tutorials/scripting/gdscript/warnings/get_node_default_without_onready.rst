GET_NODE_DEFAULT_WITHOUT_ONREADY
====================================

This warning appears when the default value of a node's property is set to a location in the scene tree without using the ``@onready`` annotation.

Depending on how you attempt to access the scene tree, the warning message will be one of the following:

.. code-block:: none

    The default value is using "$" which won't return nodes in the scene tree before "_ready()" is called. Use the "@onready" annotation to solve this.

    The default value is using "%" which won't return nodes in the scene tree before "_ready()" is called. Use the "@onready" annotation to solve this.

    The default value is using "get_node()" which won't return nodes in the scene tree before "_ready()" is called. Use the "@onready" annotation to solve this.

The default warning level for this warning is **Error**.
To modify it, see :ref:`ProjectSettings.debug/gdscript/warnings/get_node_default_without_onready<class_ProjectSettings_property_debug/gdscript/warnings/get_node_default_without_onready>`.

When this warning occurs
------------------------

Instance properties can be set by declaring them outside of a method. Additionally, they can be given a default value using ``=``::

.. code-block::

    extends Area2D

    var my_num = 3

The property ``my_num`` will always start out with a value of ``3`` in each instance of this class.
GDScript also has methods to retrieve specific nodes from the scene tree: namely the :ref:`get_node() <class_Node_method_get_node>` method, and its shorthand versions ``$`` (and ``%`` for unique nodes). Thus, if you want to have a property's default value be a particular child node, it may be tempting to write something like the following::

.. code-block::

    extends Area2D

    var my_collision_shape = $CollisionShape2D

However, properties' default values are evaluated and assigned before the scene tree is set up. This means that at the time of assigning the default value, the node may not be in the scene tree, and the variable will be set to ``null`` instead.

How to fix this warning
-----------------------

The most straightforward solution is to add the ``@onready`` annotation before your property declaration::

.. code-block::

    extends Area2D

    @onready var my_collision_shape = $CollisionShape2D

Now, the default value of the property will not be assigned until the scene tree has been initialized, and the node will be present.

Alternatively, you can set the value of the property at the beginning of your ``_ready()`` method::

.. code-block::
    
    extends Area2D
    
    var my_collision_shape

    func _ready():
        my_collision_shape = $CollisionShape2D