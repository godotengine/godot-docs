.. _class_Navigation2D:

Navigation2D
============

**Inherits:** :ref:`Node2D<class_node2d>`

**Category:** Core



Member Functions
----------------

+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`                    | :ref:`navpoly_create<class_Navigation2D_navpoly_create>`  **(** :ref:`NavigationPolygon<class_navigationpolygon>` mesh, :ref:`Matrix32<class_matrix32>` xform, :ref:`Object<class_object>` owner=NULL  **)** |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                     | :ref:`navpoly_set_transform<class_Navigation2D_navpoly_set_transform>`  **(** :ref:`int<class_int>` id, :ref:`Matrix32<class_matrix32>` xform  **)**                                                         |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                     | :ref:`navpoly_remove<class_Navigation2D_navpoly_remove>`  **(** :ref:`int<class_int>` id  **)**                                                                                                              |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector2Array<class_vector2array>`  | :ref:`get_simple_path<class_Navigation2D_get_simple_path>`  **(** :ref:`Vector2<class_vector2>` start, :ref:`Vector2<class_vector2>` end, :ref:`bool<class_bool>` optimize=true  **)**                       |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector2<class_vector2>`            | :ref:`get_closest_point<class_Navigation2D_get_closest_point>`  **(** :ref:`Vector2<class_vector2>` to_point  **)**                                                                                          |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Object<class_object>`              | :ref:`get_closest_point_owner<class_Navigation2D_get_closest_point_owner>`  **(** :ref:`Vector2<class_vector2>` to_point  **)**                                                                              |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Member Function Description
---------------------------

.. _class_Navigation2D_navpoly_create:

- :ref:`int<class_int>`  **navpoly_create**  **(** :ref:`NavigationPolygon<class_navigationpolygon>` mesh, :ref:`Matrix32<class_matrix32>` xform, :ref:`Object<class_object>` owner=NULL  **)**

.. _class_Navigation2D_navpoly_set_transform:

- void  **navpoly_set_transform**  **(** :ref:`int<class_int>` id, :ref:`Matrix32<class_matrix32>` xform  **)**

.. _class_Navigation2D_navpoly_remove:

- void  **navpoly_remove**  **(** :ref:`int<class_int>` id  **)**

.. _class_Navigation2D_get_simple_path:

- :ref:`Vector2Array<class_vector2array>`  **get_simple_path**  **(** :ref:`Vector2<class_vector2>` start, :ref:`Vector2<class_vector2>` end, :ref:`bool<class_bool>` optimize=true  **)**

.. _class_Navigation2D_get_closest_point:

- :ref:`Vector2<class_vector2>`  **get_closest_point**  **(** :ref:`Vector2<class_vector2>` to_point  **)**

.. _class_Navigation2D_get_closest_point_owner:

- :ref:`Object<class_object>`  **get_closest_point_owner**  **(** :ref:`Vector2<class_vector2>` to_point  **)**


