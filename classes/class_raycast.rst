.. _class_RayCast:

RayCast
=======

**Inherits:** :ref:`Spatial<class_spatial>`

**Category:** Core



Member Functions
----------------

+--------------------------------+---------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_enabled<class_RayCast_set_enabled>`  **(** :ref:`bool<class_bool>` enabled  **)**             |
+--------------------------------+---------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`        | :ref:`is_enabled<class_RayCast_is_enabled>`  **(** **)** const                                          |
+--------------------------------+---------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_cast_to<class_RayCast_set_cast_to>`  **(** :ref:`Vector3<class_vector3>` local_point  **)**   |
+--------------------------------+---------------------------------------------------------------------------------------------------------+
| :ref:`Vector3<class_vector3>`  | :ref:`get_cast_to<class_RayCast_get_cast_to>`  **(** **)** const                                        |
+--------------------------------+---------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`        | :ref:`is_colliding<class_RayCast_is_colliding>`  **(** **)** const                                      |
+--------------------------------+---------------------------------------------------------------------------------------------------------+
| :ref:`Object<class_object>`    | :ref:`get_collider<class_RayCast_get_collider>`  **(** **)** const                                      |
+--------------------------------+---------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`          | :ref:`get_collider_shape<class_RayCast_get_collider_shape>`  **(** **)** const                          |
+--------------------------------+---------------------------------------------------------------------------------------------------------+
| :ref:`Vector3<class_vector3>`  | :ref:`get_collision_point<class_RayCast_get_collision_point>`  **(** **)** const                        |
+--------------------------------+---------------------------------------------------------------------------------------------------------+
| :ref:`Vector3<class_vector3>`  | :ref:`get_collision_normal<class_RayCast_get_collision_normal>`  **(** **)** const                      |
+--------------------------------+---------------------------------------------------------------------------------------------------------+
| void                           | :ref:`add_exception_rid<class_RayCast_add_exception_rid>`  **(** :ref:`RID<class_rid>` rid  **)**       |
+--------------------------------+---------------------------------------------------------------------------------------------------------+
| void                           | :ref:`add_exception<class_RayCast_add_exception>`  **(** :ref:`Object<class_object>` node  **)**        |
+--------------------------------+---------------------------------------------------------------------------------------------------------+
| void                           | :ref:`remove_exception_rid<class_RayCast_remove_exception_rid>`  **(** :ref:`RID<class_rid>` rid  **)** |
+--------------------------------+---------------------------------------------------------------------------------------------------------+
| void                           | :ref:`remove_exception<class_RayCast_remove_exception>`  **(** :ref:`Object<class_object>` node  **)**  |
+--------------------------------+---------------------------------------------------------------------------------------------------------+
| void                           | :ref:`clear_exceptions<class_RayCast_clear_exceptions>`  **(** **)**                                    |
+--------------------------------+---------------------------------------------------------------------------------------------------------+

Member Function Description
---------------------------

.. _class_RayCast_set_enabled:

- void  **set_enabled**  **(** :ref:`bool<class_bool>` enabled  **)**

.. _class_RayCast_is_enabled:

- :ref:`bool<class_bool>`  **is_enabled**  **(** **)** const

.. _class_RayCast_set_cast_to:

- void  **set_cast_to**  **(** :ref:`Vector3<class_vector3>` local_point  **)**

.. _class_RayCast_get_cast_to:

- :ref:`Vector3<class_vector3>`  **get_cast_to**  **(** **)** const

.. _class_RayCast_is_colliding:

- :ref:`bool<class_bool>`  **is_colliding**  **(** **)** const

.. _class_RayCast_get_collider:

- :ref:`Object<class_object>`  **get_collider**  **(** **)** const

.. _class_RayCast_get_collider_shape:

- :ref:`int<class_int>`  **get_collider_shape**  **(** **)** const

.. _class_RayCast_get_collision_point:

- :ref:`Vector3<class_vector3>`  **get_collision_point**  **(** **)** const

.. _class_RayCast_get_collision_normal:

- :ref:`Vector3<class_vector3>`  **get_collision_normal**  **(** **)** const

.. _class_RayCast_add_exception_rid:

- void  **add_exception_rid**  **(** :ref:`RID<class_rid>` rid  **)**

.. _class_RayCast_add_exception:

- void  **add_exception**  **(** :ref:`Object<class_object>` node  **)**

.. _class_RayCast_remove_exception_rid:

- void  **remove_exception_rid**  **(** :ref:`RID<class_rid>` rid  **)**

.. _class_RayCast_remove_exception:

- void  **remove_exception**  **(** :ref:`Object<class_object>` node  **)**

.. _class_RayCast_clear_exceptions:

- void  **clear_exceptions**  **(** **)**


