``GET_NODE_DEFAULT_WITHOUT_ONREADY``
====================================

The warning that appears when a node's default value is set to a location in the scene tree without using the ``@onready`` annotation.
The message will say something like:

.. code-block:: none

    The default value is using "$" which won't return nodes in the scene tree before "_ready()" is called. Use the "@onready" annotation to solve this.

When this warning occurs
------------------------
In GDScript, instance variables can be set by declaring them outside of a method. Additionally, they can be given a default value using ``=``::

    extends Area2D
    var my_num = 3

This way, the variable ``my_num`` will always start out with a value of ``3`` in each instance of this class.
GDScript also has methods to retrieve specific nodes from the scene tree: namely, the ``get_node`` method, and its shorthand versions ``$`` (and ``%`` for unique nodes). Thus, if you want to have an instance variable default to a child of the node with a script, it may be tempting to write something like the following::

    extends Area2D
    var my_collision_shape = $CollisionShape2D

However, class instance variables' default values are evaluated and assigned before the scene tree is set up. This means that at the time of assigning the default value, the node may not be in the scene tree, and the variable will be set to ``null`` instead.

How to fix this warning
-----------------------
The most straightforward solution is to add the ``@onready`` annotation before your variable declaration::

    extends Area2D
    @onready var my_collision_shape = $CollisionShape2D

Now, the default value of the variable will not be assigned until the scene tree has been initialized, and the target node will be present.

Alternatively, you can set the value of the variable at the beginning of your ``_ready`` method::

    extends Area2D
    var my_collision_shape

    func _ready():
        my_collision_shape = $CollisionShape2D