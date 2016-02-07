.. _class_Node2D:

Node2D
======

Inherits: :ref:`CanvasItem<class_canvasitem>`
---------------------------------------------

Category: Core
--------------

Brief Description
-----------------

Base node for 2D system.

Member Functions
----------------

+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| void                             | :ref:`set_pos<class_Node2D_set_pos>`  **(** :ref:`Vector2<class_vector2>` pos  **)**                                                          |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| void                             | :ref:`set_rot<class_Node2D_set_rot>`  **(** :ref:`float<class_float>` rot  **)**                                                              |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| void                             | :ref:`set_scale<class_Node2D_set_scale>`  **(** :ref:`Vector2<class_vector2>` scale  **)**                                                    |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector2<class_vector2>`    | :ref:`get_pos<class_Node2D_get_pos>`  **(** **)** const                                                                                       |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`        | :ref:`get_rot<class_Node2D_get_rot>`  **(** **)** const                                                                                       |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector2<class_vector2>`    | :ref:`get_scale<class_Node2D_get_scale>`  **(** **)** const                                                                                   |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| void                             | :ref:`rotate<class_Node2D_rotate>`  **(** :ref:`float<class_float>` radians  **)**                                                            |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| void                             | :ref:`move_local_x<class_Node2D_move_local_x>`  **(** :ref:`float<class_float>` delta, :ref:`bool<class_bool>` scaled=false  **)**            |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| void                             | :ref:`move_local_y<class_Node2D_move_local_y>`  **(** :ref:`float<class_float>` delta, :ref:`bool<class_bool>` scaled=false  **)**            |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| void                             | :ref:`translate<class_Node2D_translate>`  **(** :ref:`Vector2<class_vector2>` offset  **)**                                                   |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| void                             | :ref:`global_translate<class_Node2D_global_translate>`  **(** :ref:`Vector2<class_vector2>` offset  **)**                                     |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| void                             | :ref:`scale<class_Node2D_scale>`  **(** :ref:`Vector2<class_vector2>` ratio  **)**                                                            |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| void                             | :ref:`set_global_pos<class_Node2D_set_global_pos>`  **(** :ref:`Vector2<class_vector2>` pos  **)**                                            |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector2<class_vector2>`    | :ref:`get_global_pos<class_Node2D_get_global_pos>`  **(** **)** const                                                                         |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| void                             | :ref:`set_transform<class_Node2D_set_transform>`  **(** :ref:`Matrix32<class_matrix32>` xform  **)**                                          |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| void                             | :ref:`set_global_transform<class_Node2D_set_global_transform>`  **(** :ref:`Matrix32<class_matrix32>` xform  **)**                            |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| void                             | :ref:`look_at<class_Node2D_look_at>`  **(** :ref:`Vector2<class_vector2>` point  **)**                                                        |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`        | :ref:`get_angle_to<class_Node2D_get_angle_to>`  **(** :ref:`Vector2<class_vector2>` point  **)** const                                        |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| void                             | :ref:`set_z<class_Node2D_set_z>`  **(** :ref:`int<class_int>` z  **)**                                                                        |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`            | :ref:`get_z<class_Node2D_get_z>`  **(** **)** const                                                                                           |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| void                             | :ref:`set_z_as_relative<class_Node2D_set_z_as_relative>`  **(** :ref:`bool<class_bool>` enable  **)**                                         |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`          | :ref:`is_z_relative<class_Node2D_is_z_relative>`  **(** **)** const                                                                           |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| void                             | :ref:`edit_set_pivot<class_Node2D_edit_set_pivot>`  **(** :ref:`Vector2<class_vector2>` pivot  **)**                                          |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Matrix32<class_matrix32>`  | :ref:`get_relative_transform_to_parent<class_Node2D_get_relative_transform_to_parent>`  **(** :ref:`Object<class_object>` parent  **)** const |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+

Description
-----------

Base node for 2D system. Node2D contains a position, rotation and scale, which is used to position and animate. It can alternatively be used with a custom 2D transform (:ref:`Matrix32<class_matrix32>`). A tree of Node2Ds allows complex hierachies for animation and positioning.

Member Function Description
---------------------------

.. _class_Node2D_set_pos:

- void  **set_pos**  **(** :ref:`Vector2<class_vector2>` pos  **)**

Set the position of the 2d node.

.. _class_Node2D_set_rot:

- void  **set_rot**  **(** :ref:`float<class_float>` rot  **)**

Set the rotation of the 2d node.

.. _class_Node2D_set_scale:

- void  **set_scale**  **(** :ref:`Vector2<class_vector2>` scale  **)**

Set the scale of the 2d node.

.. _class_Node2D_get_pos:

- :ref:`Vector2<class_vector2>`  **get_pos**  **(** **)** const

Return the position of the 2D node.

.. _class_Node2D_get_rot:

- :ref:`float<class_float>`  **get_rot**  **(** **)** const

Return the rotation of the 2D node.

.. _class_Node2D_get_scale:

- :ref:`Vector2<class_vector2>`  **get_scale**  **(** **)** const

Return the scale of the 2D node.

.. _class_Node2D_rotate:

- void  **rotate**  **(** :ref:`float<class_float>` radians  **)**

.. _class_Node2D_move_local_x:

- void  **move_local_x**  **(** :ref:`float<class_float>` delta, :ref:`bool<class_bool>` scaled=false  **)**

.. _class_Node2D_move_local_y:

- void  **move_local_y**  **(** :ref:`float<class_float>` delta, :ref:`bool<class_bool>` scaled=false  **)**

.. _class_Node2D_translate:

- void  **translate**  **(** :ref:`Vector2<class_vector2>` offset  **)**

.. _class_Node2D_global_translate:

- void  **global_translate**  **(** :ref:`Vector2<class_vector2>` offset  **)**

.. _class_Node2D_scale:

- void  **scale**  **(** :ref:`Vector2<class_vector2>` ratio  **)**

.. _class_Node2D_set_global_pos:

- void  **set_global_pos**  **(** :ref:`Vector2<class_vector2>` pos  **)**

.. _class_Node2D_get_global_pos:

- :ref:`Vector2<class_vector2>`  **get_global_pos**  **(** **)** const

Return the global position of the 2D node.

.. _class_Node2D_set_transform:

- void  **set_transform**  **(** :ref:`Matrix32<class_matrix32>` xform  **)**

.. _class_Node2D_set_global_transform:

- void  **set_global_transform**  **(** :ref:`Matrix32<class_matrix32>` xform  **)**

.. _class_Node2D_look_at:

- void  **look_at**  **(** :ref:`Vector2<class_vector2>` point  **)**

.. _class_Node2D_get_angle_to:

- :ref:`float<class_float>`  **get_angle_to**  **(** :ref:`Vector2<class_vector2>` point  **)** const

.. _class_Node2D_set_z:

- void  **set_z**  **(** :ref:`int<class_int>` z  **)**

.. _class_Node2D_get_z:

- :ref:`int<class_int>`  **get_z**  **(** **)** const

.. _class_Node2D_set_z_as_relative:

- void  **set_z_as_relative**  **(** :ref:`bool<class_bool>` enable  **)**

.. _class_Node2D_is_z_relative:

- :ref:`bool<class_bool>`  **is_z_relative**  **(** **)** const

.. _class_Node2D_edit_set_pivot:

- void  **edit_set_pivot**  **(** :ref:`Vector2<class_vector2>` pivot  **)**

.. _class_Node2D_get_relative_transform_to_parent:

- :ref:`Matrix32<class_matrix32>`  **get_relative_transform_to_parent**  **(** :ref:`Object<class_object>` parent  **)** const


