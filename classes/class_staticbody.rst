.. _class_StaticBody:

StaticBody
==========

Inherits: :ref:`PhysicsBody<class_physicsbody>`
-----------------------------------------------

Category: Core
--------------

Brief Description
-----------------

PhysicsBody for static collision objects.

Member Functions
----------------

+--------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_constant_linear_velocity<class_StaticBody_set_constant_linear_velocity>`  **(** :ref:`Vector3<class_vector3>` vel  **)**   |
+--------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_constant_angular_velocity<class_StaticBody_set_constant_angular_velocity>`  **(** :ref:`Vector3<class_vector3>` vel  **)** |
+--------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector3<class_vector3>`  | :ref:`get_constant_linear_velocity<class_StaticBody_get_constant_linear_velocity>`  **(** **)** const                                |
+--------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector3<class_vector3>`  | :ref:`get_constant_angular_velocity<class_StaticBody_get_constant_angular_velocity>`  **(** **)** const                              |
+--------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_friction<class_StaticBody_set_friction>`  **(** :ref:`float<class_float>` friction  **)**                                  |
+--------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`      | :ref:`get_friction<class_StaticBody_get_friction>`  **(** **)** const                                                                |
+--------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_bounce<class_StaticBody_set_bounce>`  **(** :ref:`float<class_float>` bounce  **)**                                        |
+--------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`      | :ref:`get_bounce<class_StaticBody_get_bounce>`  **(** **)** const                                                                    |
+--------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+

Description
-----------

StaticBody implements a static collision :ref:`Node<class_node>`, by utilizing a rigid body in the :ref:`PhysicsServer<class_physicsserver>`. Static bodies are used for static collision. For more information on physics body nodes, see :ref:`PhysicsBody<class_physicsbody>`.

Member Function Description
---------------------------

.. _class_StaticBody_set_constant_linear_velocity:

- void  **set_constant_linear_velocity**  **(** :ref:`Vector3<class_vector3>` vel  **)**

.. _class_StaticBody_set_constant_angular_velocity:

- void  **set_constant_angular_velocity**  **(** :ref:`Vector3<class_vector3>` vel  **)**

.. _class_StaticBody_get_constant_linear_velocity:

- :ref:`Vector3<class_vector3>`  **get_constant_linear_velocity**  **(** **)** const

.. _class_StaticBody_get_constant_angular_velocity:

- :ref:`Vector3<class_vector3>`  **get_constant_angular_velocity**  **(** **)** const

.. _class_StaticBody_set_friction:

- void  **set_friction**  **(** :ref:`float<class_float>` friction  **)**

.. _class_StaticBody_get_friction:

- :ref:`float<class_float>`  **get_friction**  **(** **)** const

.. _class_StaticBody_set_bounce:

- void  **set_bounce**  **(** :ref:`float<class_float>` bounce  **)**

.. _class_StaticBody_get_bounce:

- :ref:`float<class_float>`  **get_bounce**  **(** **)** const


