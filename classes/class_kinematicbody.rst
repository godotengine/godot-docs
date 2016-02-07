.. _class_KinematicBody:

KinematicBody
=============

Inherits: :ref:`PhysicsBody<class_physicsbody>`
-----------------------------------------------

Category: Core
--------------

Brief Description
-----------------



Member Functions
----------------

+--------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector3<class_vector3>`  | :ref:`move<class_KinematicBody_move>`  **(** :ref:`Vector3<class_vector3>` rel_vec  **)**                                                    |
+--------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector3<class_vector3>`  | :ref:`move_to<class_KinematicBody_move_to>`  **(** :ref:`Vector3<class_vector3>` position  **)**                                             |
+--------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`        | :ref:`can_teleport_to<class_KinematicBody_can_teleport_to>`  **(** :ref:`Vector3<class_vector3>` position  **)**                             |
+--------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`        | :ref:`is_colliding<class_KinematicBody_is_colliding>`  **(** **)** const                                                                     |
+--------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector3<class_vector3>`  | :ref:`get_collision_pos<class_KinematicBody_get_collision_pos>`  **(** **)** const                                                           |
+--------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector3<class_vector3>`  | :ref:`get_collision_normal<class_KinematicBody_get_collision_normal>`  **(** **)** const                                                     |
+--------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector3<class_vector3>`  | :ref:`get_collider_velocity<class_KinematicBody_get_collider_velocity>`  **(** **)** const                                                   |
+--------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Object<class_object>`    | :ref:`get_collider<class_KinematicBody_get_collider>`  **(** **)** const                                                                     |
+--------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`          | :ref:`get_collider_shape<class_KinematicBody_get_collider_shape>`  **(** **)** const                                                         |
+--------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_collide_with_static_bodies<class_KinematicBody_set_collide_with_static_bodies>`  **(** :ref:`bool<class_bool>` enable  **)**       |
+--------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`        | :ref:`can_collide_with_static_bodies<class_KinematicBody_can_collide_with_static_bodies>`  **(** **)** const                                 |
+--------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_collide_with_kinematic_bodies<class_KinematicBody_set_collide_with_kinematic_bodies>`  **(** :ref:`bool<class_bool>` enable  **)** |
+--------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`        | :ref:`can_collide_with_kinematic_bodies<class_KinematicBody_can_collide_with_kinematic_bodies>`  **(** **)** const                           |
+--------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_collide_with_rigid_bodies<class_KinematicBody_set_collide_with_rigid_bodies>`  **(** :ref:`bool<class_bool>` enable  **)**         |
+--------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`        | :ref:`can_collide_with_rigid_bodies<class_KinematicBody_can_collide_with_rigid_bodies>`  **(** **)** const                                   |
+--------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_collide_with_character_bodies<class_KinematicBody_set_collide_with_character_bodies>`  **(** :ref:`bool<class_bool>` enable  **)** |
+--------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`        | :ref:`can_collide_with_character_bodies<class_KinematicBody_can_collide_with_character_bodies>`  **(** **)** const                           |
+--------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_collision_margin<class_KinematicBody_set_collision_margin>`  **(** :ref:`float<class_float>` pixels  **)**                         |
+--------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`      | :ref:`get_collision_margin<class_KinematicBody_get_collision_margin>`  **(** **)** const                                                     |
+--------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+

Member Function Description
---------------------------

.. _class_KinematicBody_move:

- :ref:`Vector3<class_vector3>`  **move**  **(** :ref:`Vector3<class_vector3>` rel_vec  **)**

.. _class_KinematicBody_move_to:

- :ref:`Vector3<class_vector3>`  **move_to**  **(** :ref:`Vector3<class_vector3>` position  **)**

.. _class_KinematicBody_can_teleport_to:

- :ref:`bool<class_bool>`  **can_teleport_to**  **(** :ref:`Vector3<class_vector3>` position  **)**

Returns whether the KinematicBody can be teleported to the destination given as an argument, checking all collision shapes of the body against potential colliders at the destination.

.. _class_KinematicBody_is_colliding:

- :ref:`bool<class_bool>`  **is_colliding**  **(** **)** const

.. _class_KinematicBody_get_collision_pos:

- :ref:`Vector3<class_vector3>`  **get_collision_pos**  **(** **)** const

.. _class_KinematicBody_get_collision_normal:

- :ref:`Vector3<class_vector3>`  **get_collision_normal**  **(** **)** const

.. _class_KinematicBody_get_collider_velocity:

- :ref:`Vector3<class_vector3>`  **get_collider_velocity**  **(** **)** const

.. _class_KinematicBody_get_collider:

- :ref:`Object<class_object>`  **get_collider**  **(** **)** const

.. _class_KinematicBody_get_collider_shape:

- :ref:`int<class_int>`  **get_collider_shape**  **(** **)** const

.. _class_KinematicBody_set_collide_with_static_bodies:

- void  **set_collide_with_static_bodies**  **(** :ref:`bool<class_bool>` enable  **)**

.. _class_KinematicBody_can_collide_with_static_bodies:

- :ref:`bool<class_bool>`  **can_collide_with_static_bodies**  **(** **)** const

.. _class_KinematicBody_set_collide_with_kinematic_bodies:

- void  **set_collide_with_kinematic_bodies**  **(** :ref:`bool<class_bool>` enable  **)**

.. _class_KinematicBody_can_collide_with_kinematic_bodies:

- :ref:`bool<class_bool>`  **can_collide_with_kinematic_bodies**  **(** **)** const

.. _class_KinematicBody_set_collide_with_rigid_bodies:

- void  **set_collide_with_rigid_bodies**  **(** :ref:`bool<class_bool>` enable  **)**

.. _class_KinematicBody_can_collide_with_rigid_bodies:

- :ref:`bool<class_bool>`  **can_collide_with_rigid_bodies**  **(** **)** const

.. _class_KinematicBody_set_collide_with_character_bodies:

- void  **set_collide_with_character_bodies**  **(** :ref:`bool<class_bool>` enable  **)**

.. _class_KinematicBody_can_collide_with_character_bodies:

- :ref:`bool<class_bool>`  **can_collide_with_character_bodies**  **(** **)** const

.. _class_KinematicBody_set_collision_margin:

- void  **set_collision_margin**  **(** :ref:`float<class_float>` pixels  **)**

.. _class_KinematicBody_get_collision_margin:

- :ref:`float<class_float>`  **get_collision_margin**  **(** **)** const


