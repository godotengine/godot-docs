.. _class_RigidBody:

RigidBody
=========

**Inherits:** :ref:`PhysicsBody<class_physicsbody>`

**Category:** Core



Member Functions
----------------

+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`_integrate_forces<class_RigidBody__integrate_forces>`  **(** :ref:`PhysicsDirectBodyState<class_physicsdirectbodystate>` state  **)** virtual |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_mode<class_RigidBody_set_mode>`  **(** :ref:`int<class_int>` mode  **)**                                                                  |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`          | :ref:`get_mode<class_RigidBody_get_mode>`  **(** **)** const                                                                                        |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_mass<class_RigidBody_set_mass>`  **(** :ref:`float<class_float>` mass  **)**                                                              |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`      | :ref:`get_mass<class_RigidBody_get_mass>`  **(** **)** const                                                                                        |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_weight<class_RigidBody_set_weight>`  **(** :ref:`float<class_float>` weight  **)**                                                        |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`      | :ref:`get_weight<class_RigidBody_get_weight>`  **(** **)** const                                                                                    |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_friction<class_RigidBody_set_friction>`  **(** :ref:`float<class_float>` friction  **)**                                                  |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`      | :ref:`get_friction<class_RigidBody_get_friction>`  **(** **)** const                                                                                |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_bounce<class_RigidBody_set_bounce>`  **(** :ref:`float<class_float>` bounce  **)**                                                        |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`      | :ref:`get_bounce<class_RigidBody_get_bounce>`  **(** **)** const                                                                                    |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_linear_velocity<class_RigidBody_set_linear_velocity>`  **(** :ref:`Vector3<class_vector3>` linear_velocity  **)**                         |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector3<class_vector3>`  | :ref:`get_linear_velocity<class_RigidBody_get_linear_velocity>`  **(** **)** const                                                                  |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_angular_velocity<class_RigidBody_set_angular_velocity>`  **(** :ref:`Vector3<class_vector3>` angular_velocity  **)**                      |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector3<class_vector3>`  | :ref:`get_angular_velocity<class_RigidBody_get_angular_velocity>`  **(** **)** const                                                                |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_gravity_scale<class_RigidBody_set_gravity_scale>`  **(** :ref:`float<class_float>` gravity_scale  **)**                                   |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`      | :ref:`get_gravity_scale<class_RigidBody_get_gravity_scale>`  **(** **)** const                                                                      |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_linear_damp<class_RigidBody_set_linear_damp>`  **(** :ref:`float<class_float>` linear_damp  **)**                                         |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`      | :ref:`get_linear_damp<class_RigidBody_get_linear_damp>`  **(** **)** const                                                                          |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_angular_damp<class_RigidBody_set_angular_damp>`  **(** :ref:`float<class_float>` angular_damp  **)**                                      |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`      | :ref:`get_angular_damp<class_RigidBody_get_angular_damp>`  **(** **)** const                                                                        |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_max_contacts_reported<class_RigidBody_set_max_contacts_reported>`  **(** :ref:`int<class_int>` amount  **)**                              |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`          | :ref:`get_max_contacts_reported<class_RigidBody_get_max_contacts_reported>`  **(** **)** const                                                      |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_use_custom_integrator<class_RigidBody_set_use_custom_integrator>`  **(** :ref:`bool<class_bool>` enable  **)**                            |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`        | :ref:`is_using_custom_integrator<class_RigidBody_is_using_custom_integrator>`  **(** **)**                                                          |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_contact_monitor<class_RigidBody_set_contact_monitor>`  **(** :ref:`bool<class_bool>` enabled  **)**                                       |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`        | :ref:`is_contact_monitor_enabled<class_RigidBody_is_contact_monitor_enabled>`  **(** **)** const                                                    |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_use_continuous_collision_detection<class_RigidBody_set_use_continuous_collision_detection>`  **(** :ref:`bool<class_bool>` enable  **)**  |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`        | :ref:`is_using_continuous_collision_detection<class_RigidBody_is_using_continuous_collision_detection>`  **(** **)** const                          |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_axis_velocity<class_RigidBody_set_axis_velocity>`  **(** :ref:`Vector3<class_vector3>` axis_velocity  **)**                               |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`apply_impulse<class_RigidBody_apply_impulse>`  **(** :ref:`Vector3<class_vector3>` pos, :ref:`Vector3<class_vector3>` impulse  **)**          |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_sleeping<class_RigidBody_set_sleeping>`  **(** :ref:`bool<class_bool>` sleeping  **)**                                                    |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`        | :ref:`is_sleeping<class_RigidBody_is_sleeping>`  **(** **)** const                                                                                  |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_can_sleep<class_RigidBody_set_can_sleep>`  **(** :ref:`bool<class_bool>` able_to_sleep  **)**                                             |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`        | :ref:`is_able_to_sleep<class_RigidBody_is_able_to_sleep>`  **(** **)** const                                                                        |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_axis_lock<class_RigidBody_set_axis_lock>`  **(** :ref:`int<class_int>` axis_lock  **)**                                                   |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`          | :ref:`get_axis_lock<class_RigidBody_get_axis_lock>`  **(** **)** const                                                                              |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Array<class_array>`      | :ref:`get_colliding_bodies<class_RigidBody_get_colliding_bodies>`  **(** **)** const                                                                |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+

Signals
-------

-  **body_enter**  **(** :ref:`Object<class_object>` body  **)**
-  **body_enter_shape**  **(** :ref:`int<class_int>` body_id, :ref:`Object<class_object>` body, :ref:`int<class_int>` body_shape, :ref:`int<class_int>` local_shape  **)**
-  **body_exit**  **(** :ref:`Object<class_object>` body  **)**
-  **body_exit_shape**  **(** :ref:`int<class_int>` body_id, :ref:`Object<class_object>` body, :ref:`int<class_int>` body_shape, :ref:`int<class_int>` local_shape  **)**

Numeric Constants
-----------------

- **MODE_STATIC** = **1**
- **MODE_KINEMATIC** = **3**
- **MODE_RIGID** = **0**
- **MODE_CHARACTER** = **2**

Member Function Description
---------------------------

.. _class_RigidBody__integrate_forces:

- void  **_integrate_forces**  **(** :ref:`PhysicsDirectBodyState<class_physicsdirectbodystate>` state  **)** virtual

.. _class_RigidBody_set_mode:

- void  **set_mode**  **(** :ref:`int<class_int>` mode  **)**

.. _class_RigidBody_get_mode:

- :ref:`int<class_int>`  **get_mode**  **(** **)** const

.. _class_RigidBody_set_mass:

- void  **set_mass**  **(** :ref:`float<class_float>` mass  **)**

.. _class_RigidBody_get_mass:

- :ref:`float<class_float>`  **get_mass**  **(** **)** const

.. _class_RigidBody_set_weight:

- void  **set_weight**  **(** :ref:`float<class_float>` weight  **)**

.. _class_RigidBody_get_weight:

- :ref:`float<class_float>`  **get_weight**  **(** **)** const

.. _class_RigidBody_set_friction:

- void  **set_friction**  **(** :ref:`float<class_float>` friction  **)**

.. _class_RigidBody_get_friction:

- :ref:`float<class_float>`  **get_friction**  **(** **)** const

.. _class_RigidBody_set_bounce:

- void  **set_bounce**  **(** :ref:`float<class_float>` bounce  **)**

.. _class_RigidBody_get_bounce:

- :ref:`float<class_float>`  **get_bounce**  **(** **)** const

.. _class_RigidBody_set_linear_velocity:

- void  **set_linear_velocity**  **(** :ref:`Vector3<class_vector3>` linear_velocity  **)**

.. _class_RigidBody_get_linear_velocity:

- :ref:`Vector3<class_vector3>`  **get_linear_velocity**  **(** **)** const

.. _class_RigidBody_set_angular_velocity:

- void  **set_angular_velocity**  **(** :ref:`Vector3<class_vector3>` angular_velocity  **)**

.. _class_RigidBody_get_angular_velocity:

- :ref:`Vector3<class_vector3>`  **get_angular_velocity**  **(** **)** const

.. _class_RigidBody_set_gravity_scale:

- void  **set_gravity_scale**  **(** :ref:`float<class_float>` gravity_scale  **)**

.. _class_RigidBody_get_gravity_scale:

- :ref:`float<class_float>`  **get_gravity_scale**  **(** **)** const

.. _class_RigidBody_set_linear_damp:

- void  **set_linear_damp**  **(** :ref:`float<class_float>` linear_damp  **)**

.. _class_RigidBody_get_linear_damp:

- :ref:`float<class_float>`  **get_linear_damp**  **(** **)** const

.. _class_RigidBody_set_angular_damp:

- void  **set_angular_damp**  **(** :ref:`float<class_float>` angular_damp  **)**

.. _class_RigidBody_get_angular_damp:

- :ref:`float<class_float>`  **get_angular_damp**  **(** **)** const

.. _class_RigidBody_set_max_contacts_reported:

- void  **set_max_contacts_reported**  **(** :ref:`int<class_int>` amount  **)**

.. _class_RigidBody_get_max_contacts_reported:

- :ref:`int<class_int>`  **get_max_contacts_reported**  **(** **)** const

.. _class_RigidBody_set_use_custom_integrator:

- void  **set_use_custom_integrator**  **(** :ref:`bool<class_bool>` enable  **)**

.. _class_RigidBody_is_using_custom_integrator:

- :ref:`bool<class_bool>`  **is_using_custom_integrator**  **(** **)**

.. _class_RigidBody_set_contact_monitor:

- void  **set_contact_monitor**  **(** :ref:`bool<class_bool>` enabled  **)**

.. _class_RigidBody_is_contact_monitor_enabled:

- :ref:`bool<class_bool>`  **is_contact_monitor_enabled**  **(** **)** const

.. _class_RigidBody_set_use_continuous_collision_detection:

- void  **set_use_continuous_collision_detection**  **(** :ref:`bool<class_bool>` enable  **)**

.. _class_RigidBody_is_using_continuous_collision_detection:

- :ref:`bool<class_bool>`  **is_using_continuous_collision_detection**  **(** **)** const

.. _class_RigidBody_set_axis_velocity:

- void  **set_axis_velocity**  **(** :ref:`Vector3<class_vector3>` axis_velocity  **)**

.. _class_RigidBody_apply_impulse:

- void  **apply_impulse**  **(** :ref:`Vector3<class_vector3>` pos, :ref:`Vector3<class_vector3>` impulse  **)**

.. _class_RigidBody_set_sleeping:

- void  **set_sleeping**  **(** :ref:`bool<class_bool>` sleeping  **)**

.. _class_RigidBody_is_sleeping:

- :ref:`bool<class_bool>`  **is_sleeping**  **(** **)** const

.. _class_RigidBody_set_can_sleep:

- void  **set_can_sleep**  **(** :ref:`bool<class_bool>` able_to_sleep  **)**

.. _class_RigidBody_is_able_to_sleep:

- :ref:`bool<class_bool>`  **is_able_to_sleep**  **(** **)** const

.. _class_RigidBody_set_axis_lock:

- void  **set_axis_lock**  **(** :ref:`int<class_int>` axis_lock  **)**

.. _class_RigidBody_get_axis_lock:

- :ref:`int<class_int>`  **get_axis_lock**  **(** **)** const

.. _class_RigidBody_get_colliding_bodies:

- :ref:`Array<class_array>`  **get_colliding_bodies**  **(** **)** const


