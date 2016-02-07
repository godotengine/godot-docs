.. _class_PhysicsBody:

PhysicsBody
===========

**Inherits:** :ref:`CollisionObject<class_collisionobject>`

**Category:** Core

Base class for different types of Physics bodies.

Member Functions
----------------

+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| void                   | :ref:`set_layer_mask<class_PhysicsBody_set_layer_mask>`  **(** :ref:`int<class_int>` mask  **)**                                                   |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`  | :ref:`get_layer_mask<class_PhysicsBody_get_layer_mask>`  **(** **)** const                                                                         |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| void                   | :ref:`add_collision_exception_with<class_PhysicsBody_add_collision_exception_with>`  **(** :ref:`PhysicsBody<class_physicsbody>` body  **)**       |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| void                   | :ref:`remove_collision_exception_with<class_PhysicsBody_remove_collision_exception_with>`  **(** :ref:`PhysicsBody<class_physicsbody>` body  **)** |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+

Description
-----------

PhysicsBody is an abstract base class for implementing a physics body. All PhysicsBody types inherit from it.

Member Function Description
---------------------------

.. _class_PhysicsBody_set_layer_mask:

- void  **set_layer_mask**  **(** :ref:`int<class_int>` mask  **)**

.. _class_PhysicsBody_get_layer_mask:

- :ref:`int<class_int>`  **get_layer_mask**  **(** **)** const

.. _class_PhysicsBody_add_collision_exception_with:

- void  **add_collision_exception_with**  **(** :ref:`PhysicsBody<class_physicsbody>` body  **)**

.. _class_PhysicsBody_remove_collision_exception_with:

- void  **remove_collision_exception_with**  **(** :ref:`PhysicsBody<class_physicsbody>` body  **)**


