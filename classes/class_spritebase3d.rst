.. _class_SpriteBase3D:

SpriteBase3D
============

Inherits: :ref:`GeometryInstance<class_geometryinstance>`
---------------------------------------------------------

Category: Core
--------------

Brief Description
-----------------



Member Functions
----------------

+--------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_centered<class_SpriteBase3D_set_centered>`  **(** :ref:`bool<class_bool>` centered  **)**                              |
+--------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`        | :ref:`is_centered<class_SpriteBase3D_is_centered>`  **(** **)** const                                                            |
+--------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_offset<class_SpriteBase3D_set_offset>`  **(** :ref:`Vector2<class_vector2>` offset  **)**                              |
+--------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector2<class_vector2>`  | :ref:`get_offset<class_SpriteBase3D_get_offset>`  **(** **)** const                                                              |
+--------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_flip_h<class_SpriteBase3D_set_flip_h>`  **(** :ref:`bool<class_bool>` flip_h  **)**                                    |
+--------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`        | :ref:`is_flipped_h<class_SpriteBase3D_is_flipped_h>`  **(** **)** const                                                          |
+--------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_flip_v<class_SpriteBase3D_set_flip_v>`  **(** :ref:`bool<class_bool>` flip_v  **)**                                    |
+--------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`        | :ref:`is_flipped_v<class_SpriteBase3D_is_flipped_v>`  **(** **)** const                                                          |
+--------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_modulate<class_SpriteBase3D_set_modulate>`  **(** :ref:`Color<class_color>` modulate  **)**                            |
+--------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Color<class_color>`      | :ref:`get_modulate<class_SpriteBase3D_get_modulate>`  **(** **)** const                                                          |
+--------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_opacity<class_SpriteBase3D_set_opacity>`  **(** :ref:`float<class_float>` opacity  **)**                               |
+--------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`      | :ref:`get_opacity<class_SpriteBase3D_get_opacity>`  **(** **)** const                                                            |
+--------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_pixel_size<class_SpriteBase3D_set_pixel_size>`  **(** :ref:`float<class_float>` pixel_size  **)**                      |
+--------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`      | :ref:`get_pixel_size<class_SpriteBase3D_get_pixel_size>`  **(** **)** const                                                      |
+--------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_axis<class_SpriteBase3D_set_axis>`  **(** :ref:`int<class_int>` axis  **)**                                            |
+--------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`          | :ref:`get_axis<class_SpriteBase3D_get_axis>`  **(** **)** const                                                                  |
+--------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_draw_flag<class_SpriteBase3D_set_draw_flag>`  **(** :ref:`int<class_int>` flag, :ref:`bool<class_bool>` enabled  **)** |
+--------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`        | :ref:`get_draw_flag<class_SpriteBase3D_get_draw_flag>`  **(** :ref:`int<class_int>` flag  **)** const                            |
+--------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_alpha_cut_mode<class_SpriteBase3D_set_alpha_cut_mode>`  **(** :ref:`int<class_int>` mode  **)**                        |
+--------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`          | :ref:`get_alpha_cut_mode<class_SpriteBase3D_get_alpha_cut_mode>`  **(** **)** const                                              |
+--------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Rect2<class_rect2>`      | :ref:`get_item_rect<class_SpriteBase3D_get_item_rect>`  **(** **)** const                                                        |
+--------------------------------+----------------------------------------------------------------------------------------------------------------------------------+

Numeric Constants
-----------------

- **FLAG_TRANSPARENT** = **0**
- **FLAG_SHADED** = **1**
- **FLAG_MAX** = **2**
- **ALPHA_CUT_DISABLED** = **0**
- **ALPHA_CUT_DISCARD** = **1**
- **ALPHA_CUT_OPAQUE_PREPASS** = **2**

Member Function Description
---------------------------

.. _class_SpriteBase3D_set_centered:

- void  **set_centered**  **(** :ref:`bool<class_bool>` centered  **)**

.. _class_SpriteBase3D_is_centered:

- :ref:`bool<class_bool>`  **is_centered**  **(** **)** const

.. _class_SpriteBase3D_set_offset:

- void  **set_offset**  **(** :ref:`Vector2<class_vector2>` offset  **)**

.. _class_SpriteBase3D_get_offset:

- :ref:`Vector2<class_vector2>`  **get_offset**  **(** **)** const

.. _class_SpriteBase3D_set_flip_h:

- void  **set_flip_h**  **(** :ref:`bool<class_bool>` flip_h  **)**

.. _class_SpriteBase3D_is_flipped_h:

- :ref:`bool<class_bool>`  **is_flipped_h**  **(** **)** const

.. _class_SpriteBase3D_set_flip_v:

- void  **set_flip_v**  **(** :ref:`bool<class_bool>` flip_v  **)**

.. _class_SpriteBase3D_is_flipped_v:

- :ref:`bool<class_bool>`  **is_flipped_v**  **(** **)** const

.. _class_SpriteBase3D_set_modulate:

- void  **set_modulate**  **(** :ref:`Color<class_color>` modulate  **)**

.. _class_SpriteBase3D_get_modulate:

- :ref:`Color<class_color>`  **get_modulate**  **(** **)** const

.. _class_SpriteBase3D_set_opacity:

- void  **set_opacity**  **(** :ref:`float<class_float>` opacity  **)**

.. _class_SpriteBase3D_get_opacity:

- :ref:`float<class_float>`  **get_opacity**  **(** **)** const

.. _class_SpriteBase3D_set_pixel_size:

- void  **set_pixel_size**  **(** :ref:`float<class_float>` pixel_size  **)**

.. _class_SpriteBase3D_get_pixel_size:

- :ref:`float<class_float>`  **get_pixel_size**  **(** **)** const

.. _class_SpriteBase3D_set_axis:

- void  **set_axis**  **(** :ref:`int<class_int>` axis  **)**

.. _class_SpriteBase3D_get_axis:

- :ref:`int<class_int>`  **get_axis**  **(** **)** const

.. _class_SpriteBase3D_set_draw_flag:

- void  **set_draw_flag**  **(** :ref:`int<class_int>` flag, :ref:`bool<class_bool>` enabled  **)**

.. _class_SpriteBase3D_get_draw_flag:

- :ref:`bool<class_bool>`  **get_draw_flag**  **(** :ref:`int<class_int>` flag  **)** const

.. _class_SpriteBase3D_set_alpha_cut_mode:

- void  **set_alpha_cut_mode**  **(** :ref:`int<class_int>` mode  **)**

.. _class_SpriteBase3D_get_alpha_cut_mode:

- :ref:`int<class_int>`  **get_alpha_cut_mode**  **(** **)** const

.. _class_SpriteBase3D_get_item_rect:

- :ref:`Rect2<class_rect2>`  **get_item_rect**  **(** **)** const


