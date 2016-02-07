.. _class_Sprite:

Sprite
======

**Inherits:** :ref:`Node2D<class_node2d>`

**Category:** Core

General purpose Sprite node.

Member Functions
----------------

+--------------------------------+---------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_texture<class_Sprite_set_texture>`  **(** :ref:`Texture<class_texture>` texture  **)**  |
+--------------------------------+---------------------------------------------------------------------------------------------------+
| :ref:`Texture<class_texture>`  | :ref:`get_texture<class_Sprite_get_texture>`  **(** **)** const                                   |
+--------------------------------+---------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_centered<class_Sprite_set_centered>`  **(** :ref:`bool<class_bool>` centered  **)**     |
+--------------------------------+---------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`        | :ref:`is_centered<class_Sprite_is_centered>`  **(** **)** const                                   |
+--------------------------------+---------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_offset<class_Sprite_set_offset>`  **(** :ref:`Vector2<class_vector2>` offset  **)**     |
+--------------------------------+---------------------------------------------------------------------------------------------------+
| :ref:`Vector2<class_vector2>`  | :ref:`get_offset<class_Sprite_get_offset>`  **(** **)** const                                     |
+--------------------------------+---------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_flip_h<class_Sprite_set_flip_h>`  **(** :ref:`bool<class_bool>` flip_h  **)**           |
+--------------------------------+---------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`        | :ref:`is_flipped_h<class_Sprite_is_flipped_h>`  **(** **)** const                                 |
+--------------------------------+---------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_flip_v<class_Sprite_set_flip_v>`  **(** :ref:`bool<class_bool>` flip_v  **)**           |
+--------------------------------+---------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`        | :ref:`is_flipped_v<class_Sprite_is_flipped_v>`  **(** **)** const                                 |
+--------------------------------+---------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_region<class_Sprite_set_region>`  **(** :ref:`bool<class_bool>` enabled  **)**          |
+--------------------------------+---------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`        | :ref:`is_region<class_Sprite_is_region>`  **(** **)** const                                       |
+--------------------------------+---------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_region_rect<class_Sprite_set_region_rect>`  **(** :ref:`Rect2<class_rect2>` rect  **)** |
+--------------------------------+---------------------------------------------------------------------------------------------------+
| :ref:`Rect2<class_rect2>`      | :ref:`get_region_rect<class_Sprite_get_region_rect>`  **(** **)** const                           |
+--------------------------------+---------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_frame<class_Sprite_set_frame>`  **(** :ref:`int<class_int>` frame  **)**                |
+--------------------------------+---------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`          | :ref:`get_frame<class_Sprite_get_frame>`  **(** **)** const                                       |
+--------------------------------+---------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_vframes<class_Sprite_set_vframes>`  **(** :ref:`int<class_int>` vframes  **)**          |
+--------------------------------+---------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`          | :ref:`get_vframes<class_Sprite_get_vframes>`  **(** **)** const                                   |
+--------------------------------+---------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_hframes<class_Sprite_set_hframes>`  **(** :ref:`int<class_int>` hframes  **)**          |
+--------------------------------+---------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`          | :ref:`get_hframes<class_Sprite_get_hframes>`  **(** **)** const                                   |
+--------------------------------+---------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_modulate<class_Sprite_set_modulate>`  **(** :ref:`Color<class_color>` modulate  **)**   |
+--------------------------------+---------------------------------------------------------------------------------------------------+
| :ref:`Color<class_color>`      | :ref:`get_modulate<class_Sprite_get_modulate>`  **(** **)** const                                 |
+--------------------------------+---------------------------------------------------------------------------------------------------+

Signals
-------

-  **frame_changed**  **(** **)**

Description
-----------

General purpose Sprite node. This Sprite node can show any texture as a sprite. The texture can be used as a spritesheet for animation, or only a region from a bigger texture can referenced, like an atlas.

Member Function Description
---------------------------

.. _class_Sprite_set_texture:

- void  **set_texture**  **(** :ref:`Texture<class_texture>` texture  **)**

Set the base texture for the sprite.

.. _class_Sprite_get_texture:

- :ref:`Texture<class_texture>`  **get_texture**  **(** **)** const

Return the base texture for the sprite.

.. _class_Sprite_set_centered:

- void  **set_centered**  **(** :ref:`bool<class_bool>` centered  **)**

Set whether the sprite should be centered on the origin.

.. _class_Sprite_is_centered:

- :ref:`bool<class_bool>`  **is_centered**  **(** **)** const

Return if the sprite is centered at the local origin.

.. _class_Sprite_set_offset:

- void  **set_offset**  **(** :ref:`Vector2<class_vector2>` offset  **)**

Set the sprite draw offset, useful for setting rotation pivots.

.. _class_Sprite_get_offset:

- :ref:`Vector2<class_vector2>`  **get_offset**  **(** **)** const

Return sprite draw offst.

.. _class_Sprite_set_flip_h:

- void  **set_flip_h**  **(** :ref:`bool<class_bool>` flip_h  **)**

Set true to flip the sprite horizontaly.

.. _class_Sprite_is_flipped_h:

- :ref:`bool<class_bool>`  **is_flipped_h**  **(** **)** const

Return true if the sprite is flipped horizontally.

.. _class_Sprite_set_flip_v:

- void  **set_flip_v**  **(** :ref:`bool<class_bool>` flip_v  **)**

Set true to flip the sprite vertically.

.. _class_Sprite_is_flipped_v:

- :ref:`bool<class_bool>`  **is_flipped_v**  **(** **)** const

Return true if the sprite is flipped vertically.

.. _class_Sprite_set_region:

- void  **set_region**  **(** :ref:`bool<class_bool>` enabled  **)**

Set the sprite as a sub-region of a bigger texture. Useful for texture-atlases.

.. _class_Sprite_is_region:

- :ref:`bool<class_bool>`  **is_region**  **(** **)** const

Return if the sprite reads from a region.

.. _class_Sprite_set_region_rect:

- void  **set_region_rect**  **(** :ref:`Rect2<class_rect2>` rect  **)**

Set the region rect to read from.

.. _class_Sprite_get_region_rect:

- :ref:`Rect2<class_rect2>`  **get_region_rect**  **(** **)** const

Return the region rect to read from.

.. _class_Sprite_set_frame:

- void  **set_frame**  **(** :ref:`int<class_int>` frame  **)**

Set the texture frame for a sprite-sheet, works when vframes or hframes are greater than 1.

.. _class_Sprite_get_frame:

- :ref:`int<class_int>`  **get_frame**  **(** **)** const

Return the texture frame for a sprite-sheet, works when vframes or hframes are greater than 1.

.. _class_Sprite_set_vframes:

- void  **set_vframes**  **(** :ref:`int<class_int>` vframes  **)**

Set the amount of vertical frames and converts the sprite into a sprite-sheet. This is useful for animation.

.. _class_Sprite_get_vframes:

- :ref:`int<class_int>`  **get_vframes**  **(** **)** const

Return the amount of vertical frames. See :ref:`set_vframes<class_set_vframes>`.

.. _class_Sprite_set_hframes:

- void  **set_hframes**  **(** :ref:`int<class_int>` hframes  **)**

Set the amount of horizontal frames and converts the sprite into a sprite-sheet. This is useful for animation.

.. _class_Sprite_get_hframes:

- :ref:`int<class_int>`  **get_hframes**  **(** **)** const

Return the amount of horizontal frames. See :ref:`set_hframes<class_set_hframes>`.

.. _class_Sprite_set_modulate:

- void  **set_modulate**  **(** :ref:`Color<class_color>` modulate  **)**

Set color modulation for the sprite. All sprite pixels are multiplied by this color.  Color may contain rgb values above 1 to achieve a highlight effect.

.. _class_Sprite_get_modulate:

- :ref:`Color<class_color>`  **get_modulate**  **(** **)** const

Return color modulation for the sprite. All sprite pixels are multiplied by this color.


