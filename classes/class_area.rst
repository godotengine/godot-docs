.. _class_Area:

Area
====

**Inherits:** :ref:`CollisionObject<class_collisionobject>`

**Category:** Core



Member Functions
----------------

+----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| void                                   | :ref:`set_space_override_mode<class_Area_set_space_override_mode>`  **(** :ref:`int<class_int>` enable  **)**                   |
+----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`                  | :ref:`get_space_override_mode<class_Area_get_space_override_mode>`  **(** **)** const                                           |
+----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| void                                   | :ref:`set_gravity_is_point<class_Area_set_gravity_is_point>`  **(** :ref:`bool<class_bool>` enable  **)**                       |
+----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`                | :ref:`is_gravity_a_point<class_Area_is_gravity_a_point>`  **(** **)** const                                                     |
+----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| void                                   | :ref:`set_gravity_distance_scale<class_Area_set_gravity_distance_scale>`  **(** :ref:`float<class_float>` distance_scale  **)** |
+----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`              | :ref:`get_gravity_distance_scale<class_Area_get_gravity_distance_scale>`  **(** **)** const                                     |
+----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| void                                   | :ref:`set_gravity_vector<class_Area_set_gravity_vector>`  **(** :ref:`Vector3<class_vector3>` vector  **)**                     |
+----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector3<class_vector3>`          | :ref:`get_gravity_vector<class_Area_get_gravity_vector>`  **(** **)** const                                                     |
+----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| void                                   | :ref:`set_gravity<class_Area_set_gravity>`  **(** :ref:`float<class_float>` gravity  **)**                                      |
+----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`              | :ref:`get_gravity<class_Area_get_gravity>`  **(** **)** const                                                                   |
+----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| void                                   | :ref:`set_angular_damp<class_Area_set_angular_damp>`  **(** :ref:`float<class_float>` angular_damp  **)**                       |
+----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`              | :ref:`get_angular_damp<class_Area_get_angular_damp>`  **(** **)** const                                                         |
+----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| void                                   | :ref:`set_linear_damp<class_Area_set_linear_damp>`  **(** :ref:`float<class_float>` linear_damp  **)**                          |
+----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`              | :ref:`get_linear_damp<class_Area_get_linear_damp>`  **(** **)** const                                                           |
+----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| void                                   | :ref:`set_priority<class_Area_set_priority>`  **(** :ref:`float<class_float>` priority  **)**                                   |
+----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`              | :ref:`get_priority<class_Area_get_priority>`  **(** **)** const                                                                 |
+----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| void                                   | :ref:`set_monitorable<class_Area_set_monitorable>`  **(** :ref:`bool<class_bool>` enable  **)**                                 |
+----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`                | :ref:`is_monitorable<class_Area_is_monitorable>`  **(** **)** const                                                             |
+----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| void                                   | :ref:`set_enable_monitoring<class_Area_set_enable_monitoring>`  **(** :ref:`bool<class_bool>` enable  **)**                     |
+----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`                | :ref:`is_monitoring_enabled<class_Area_is_monitoring_enabled>`  **(** **)** const                                               |
+----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Array<class_array>`              | :ref:`get_overlapping_bodies<class_Area_get_overlapping_bodies>`  **(** **)** const                                             |
+----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Array<class_array>`              | :ref:`get_overlapping_areas<class_Area_get_overlapping_areas>`  **(** **)** const                                               |
+----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| :ref:`PhysicsBody<class_physicsbody>`  | :ref:`overlaps_body<class_Area_overlaps_body>`  **(** :ref:`Object<class_object>` body  **)** const                             |
+----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Area<class_area>`                | :ref:`overlaps_area<class_Area_overlaps_area>`  **(** :ref:`Object<class_object>` area  **)** const                             |
+----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+

Signals
-------

-  **body_enter**  **(** :ref:`Object<class_object>` body  **)**
-  **body_enter_shape**  **(** :ref:`int<class_int>` body_id, :ref:`Object<class_object>` body, :ref:`int<class_int>` body_shape, :ref:`int<class_int>` area_shape  **)**
-  **area_enter**  **(** :ref:`Object<class_object>` area  **)**
-  **area_enter_shape**  **(** :ref:`int<class_int>` area_id, :ref:`Object<class_object>` area, :ref:`int<class_int>` area_shape, :ref:`int<class_int>` area_shape  **)**
-  **body_exit**  **(** :ref:`Object<class_object>` body  **)**
-  **body_exit_shape**  **(** :ref:`int<class_int>` body_id, :ref:`Object<class_object>` body, :ref:`int<class_int>` body_shape, :ref:`int<class_int>` area_shape  **)**
-  **area_exit**  **(** :ref:`Object<class_object>` area  **)**
-  **area_exit_shape**  **(** :ref:`int<class_int>` area_id, :ref:`Object<class_object>` area, :ref:`int<class_int>` area_shape, :ref:`int<class_int>` area_shape  **)**

Member Function Description
---------------------------

.. _class_Area_set_space_override_mode:

- void  **set_space_override_mode**  **(** :ref:`int<class_int>` enable  **)**

Set the space override mode. This mode controls how an area affects gravity and damp.

AREA_SPACE_OVERRIDE_DISABLED: This area does not affect gravity/damp. These are generally areas that exist only to detect collisions, and objects entering or exiting them.

AREA_SPACE_OVERRIDE_COMBINE: This area adds its gravity/damp values to whatever has been calculated so far. This way, many overlapping areas can combine their physics to make interesting effects.

AREA_SPACE_OVERRIDE_COMBINE_REPLACE: This area adds its gravity/damp values to whatever has been calculated so far. Then stops taking into account the rest of the areas, even the default one.

AREA_SPACE_OVERRIDE_REPLACE: This area replaces any gravity/damp, even the default one, and stops taking into account the rest of the areas.

AREA_SPACE_OVERRIDE_REPLACE_COMBINE: This area replaces any gravity/damp calculated so far, but keeps calculating the rest of the areas, down to the default one.

.. _class_Area_get_space_override_mode:

- :ref:`int<class_int>`  **get_space_override_mode**  **(** **)** const

.. _class_Area_set_gravity_is_point:

- void  **set_gravity_is_point**  **(** :ref:`bool<class_bool>` enable  **)**

.. _class_Area_is_gravity_a_point:

- :ref:`bool<class_bool>`  **is_gravity_a_point**  **(** **)** const

.. _class_Area_set_gravity_distance_scale:

- void  **set_gravity_distance_scale**  **(** :ref:`float<class_float>` distance_scale  **)**

.. _class_Area_get_gravity_distance_scale:

- :ref:`float<class_float>`  **get_gravity_distance_scale**  **(** **)** const

.. _class_Area_set_gravity_vector:

- void  **set_gravity_vector**  **(** :ref:`Vector3<class_vector3>` vector  **)**

.. _class_Area_get_gravity_vector:

- :ref:`Vector3<class_vector3>`  **get_gravity_vector**  **(** **)** const

.. _class_Area_set_gravity:

- void  **set_gravity**  **(** :ref:`float<class_float>` gravity  **)**

.. _class_Area_get_gravity:

- :ref:`float<class_float>`  **get_gravity**  **(** **)** const

.. _class_Area_set_angular_damp:

- void  **set_angular_damp**  **(** :ref:`float<class_float>` angular_damp  **)**

.. _class_Area_get_angular_damp:

- :ref:`float<class_float>`  **get_angular_damp**  **(** **)** const

.. _class_Area_set_linear_damp:

- void  **set_linear_damp**  **(** :ref:`float<class_float>` linear_damp  **)**

.. _class_Area_get_linear_damp:

- :ref:`float<class_float>`  **get_linear_damp**  **(** **)** const

.. _class_Area_set_priority:

- void  **set_priority**  **(** :ref:`float<class_float>` priority  **)**

.. _class_Area_get_priority:

- :ref:`float<class_float>`  **get_priority**  **(** **)** const

.. _class_Area_set_monitorable:

- void  **set_monitorable**  **(** :ref:`bool<class_bool>` enable  **)**

.. _class_Area_is_monitorable:

- :ref:`bool<class_bool>`  **is_monitorable**  **(** **)** const

.. _class_Area_set_enable_monitoring:

- void  **set_enable_monitoring**  **(** :ref:`bool<class_bool>` enable  **)**

.. _class_Area_is_monitoring_enabled:

- :ref:`bool<class_bool>`  **is_monitoring_enabled**  **(** **)** const

.. _class_Area_get_overlapping_bodies:

- :ref:`Array<class_array>`  **get_overlapping_bodies**  **(** **)** const

.. _class_Area_get_overlapping_areas:

- :ref:`Array<class_array>`  **get_overlapping_areas**  **(** **)** const

.. _class_Area_overlaps_body:

- :ref:`PhysicsBody<class_physicsbody>`  **overlaps_body**  **(** :ref:`Object<class_object>` body  **)** const

.. _class_Area_overlaps_area:

- :ref:`Area<class_area>`  **overlaps_area**  **(** :ref:`Object<class_object>` area  **)** const


