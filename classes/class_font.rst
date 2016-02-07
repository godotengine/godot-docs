.. _class_Font:

Font
====

**Inherits:** :ref:`Resource<class_resource>` **<** :ref:`Reference<class_reference>` **<** :ref:`Object<class_object>`

**Category:** Core

Brief Description
-----------------

Internationalized font and text drawing support.

Member Functions
----------------

+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`          | :ref:`create_from_fnt<class_Font_create_from_fnt>`  **(** :ref:`String<class_string>` path  **)**                                                                                                                                             |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_height<class_Font_set_height>`  **(** :ref:`float<class_float>` px  **)**                                                                                                                                                           |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`      | :ref:`get_height<class_Font_get_height>`  **(** **)** const                                                                                                                                                                                   |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_ascent<class_Font_set_ascent>`  **(** :ref:`float<class_float>` px  **)**                                                                                                                                                           |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`      | :ref:`get_ascent<class_Font_get_ascent>`  **(** **)** const                                                                                                                                                                                   |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`      | :ref:`get_descent<class_Font_get_descent>`  **(** **)** const                                                                                                                                                                                 |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`add_kerning_pair<class_Font_add_kerning_pair>`  **(** :ref:`int<class_int>` char_a, :ref:`int<class_int>` char_b, :ref:`int<class_int>` kerning  **)**                                                                                  |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`          | :ref:`get_kerning_pair<class_Font_get_kerning_pair>`  **(** :ref:`int<class_int>` char_a, :ref:`int<class_int>` char_b  **)** const                                                                                                           |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`add_texture<class_Font_add_texture>`  **(** :ref:`Texture<class_texture>` texture  **)**                                                                                                                                                |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`add_char<class_Font_add_char>`  **(** :ref:`int<class_int>` character, :ref:`int<class_int>` texture, :ref:`Rect2<class_rect2>` rect, :ref:`Vector2<class_vector2>` align=Vector2(0,0), :ref:`float<class_float>` advance=-1  **)**     |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`          | :ref:`get_texture_count<class_Font_get_texture_count>`  **(** **)** const                                                                                                                                                                     |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Texture<class_texture>`  | :ref:`get_texture<class_Font_get_texture>`  **(** :ref:`int<class_int>` idx  **)** const                                                                                                                                                      |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector2<class_vector2>`  | :ref:`get_char_size<class_Font_get_char_size>`  **(** :ref:`int<class_int>` char, :ref:`int<class_int>` next=0  **)** const                                                                                                                   |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector2<class_vector2>`  | :ref:`get_string_size<class_Font_get_string_size>`  **(** :ref:`String<class_string>` string  **)** const                                                                                                                                     |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_distance_field_hint<class_Font_set_distance_field_hint>`  **(** :ref:`bool<class_bool>` enable  **)**                                                                                                                               |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`        | :ref:`is_distance_field_hint<class_Font_is_distance_field_hint>`  **(** **)** const                                                                                                                                                           |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`clear<class_Font_clear>`  **(** **)**                                                                                                                                                                                                   |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`draw<class_Font_draw>`  **(** :ref:`RID<class_rid>` canvas_item, :ref:`Vector2<class_vector2>` pos, :ref:`String<class_string>` string, :ref:`Color<class_color>` modulate=Color(1,1,1,1), :ref:`int<class_int>` clip_w=-1  **)** const |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`      | :ref:`draw_char<class_Font_draw_char>`  **(** :ref:`RID<class_rid>` canvas_item, :ref:`Vector2<class_vector2>` pos, :ref:`int<class_int>` char, :ref:`int<class_int>` next=-1, :ref:`Color<class_color>` modulate=Color(1,1,1,1)  **)** const |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_fallback<class_Font_set_fallback>`  **(** :ref:`Object<class_object>` fallback  **)**                                                                                                                                               |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Object<class_object>`    | :ref:`get_fallback<class_Font_get_fallback>`  **(** **)** const                                                                                                                                                                               |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Description
-----------

Font contains an unicode compatible character set, as well as the ability to draw it with variable width, ascent, descent and kerning. For creating fonts from TTF files (or other font formats), see the editor support for fonts. TODO check wikipedia for graph of ascent/baseline/descent/height/etc.

Member Function Description
---------------------------

.. _class_Font_create_from_fnt:

- :ref:`int<class_int>`  **create_from_fnt**  **(** :ref:`String<class_string>` path  **)**

.. _class_Font_set_height:

- void  **set_height**  **(** :ref:`float<class_float>` px  **)**

Set the total font height (ascent plus descent) in pixels.

.. _class_Font_get_height:

- :ref:`float<class_float>`  **get_height**  **(** **)** const

Return the total font height (ascent plus descent) in pixels.

.. _class_Font_set_ascent:

- void  **set_ascent**  **(** :ref:`float<class_float>` px  **)**

Set the font ascent (number of pixels above the baseline).

.. _class_Font_get_ascent:

- :ref:`float<class_float>`  **get_ascent**  **(** **)** const

Return the font ascent (number of pixels above the baseline).

.. _class_Font_get_descent:

- :ref:`float<class_float>`  **get_descent**  **(** **)** const

Return the font descent (number of pixels below the baseline).

.. _class_Font_add_kerning_pair:

- void  **add_kerning_pair**  **(** :ref:`int<class_int>` char_a, :ref:`int<class_int>` char_b, :ref:`int<class_int>` kerning  **)**

Add a kerning pair to the :ref:`Font<class_font>` as a difference. Kerning pairs are special cases where a typeface advance is determined by the next character.

.. _class_Font_get_kerning_pair:

- :ref:`int<class_int>`  **get_kerning_pair**  **(** :ref:`int<class_int>` char_a, :ref:`int<class_int>` char_b  **)** const

Return a kerning pair as a difference. Kerning pairs are special cases where a typeface advance is determined by the next character.

.. _class_Font_add_texture:

- void  **add_texture**  **(** :ref:`Texture<class_texture>` texture  **)**

Add a texture to the :ref:`Font<class_font>`.

.. _class_Font_add_char:

- void  **add_char**  **(** :ref:`int<class_int>` character, :ref:`int<class_int>` texture, :ref:`Rect2<class_rect2>` rect, :ref:`Vector2<class_vector2>` align=Vector2(0,0), :ref:`float<class_float>` advance=-1  **)**

Add a character to the font, where "character" is the unicode value, "texture" is the texture index, "rect" is the region in the texture (in pixels!), "align" is the (optional) alignment for the character and "advance" is the (optional) advance.

.. _class_Font_get_texture_count:

- :ref:`int<class_int>`  **get_texture_count**  **(** **)** const

.. _class_Font_get_texture:

- :ref:`Texture<class_texture>`  **get_texture**  **(** :ref:`int<class_int>` idx  **)** const

.. _class_Font_get_char_size:

- :ref:`Vector2<class_vector2>`  **get_char_size**  **(** :ref:`int<class_int>` char, :ref:`int<class_int>` next=0  **)** const

Return the size of a character, optionally taking kerning into account if the next character is provided.

.. _class_Font_get_string_size:

- :ref:`Vector2<class_vector2>`  **get_string_size**  **(** :ref:`String<class_string>` string  **)** const

Return the size of a string, taking kerning and advance into account.

.. _class_Font_set_distance_field_hint:

- void  **set_distance_field_hint**  **(** :ref:`bool<class_bool>` enable  **)**

.. _class_Font_is_distance_field_hint:

- :ref:`bool<class_bool>`  **is_distance_field_hint**  **(** **)** const

.. _class_Font_clear:

- void  **clear**  **(** **)**

Clear all the font data.

.. _class_Font_draw:

- void  **draw**  **(** :ref:`RID<class_rid>` canvas_item, :ref:`Vector2<class_vector2>` pos, :ref:`String<class_string>` string, :ref:`Color<class_color>` modulate=Color(1,1,1,1), :ref:`int<class_int>` clip_w=-1  **)** const

Draw "string" into a canvas item using the font at a given "pos" position, with "modulate" color, and optionally clipping the width. "pos" specifies te baseline, not the top. To draw from the top, *ascent* must be added to the Y axis.

.. _class_Font_draw_char:

- :ref:`float<class_float>`  **draw_char**  **(** :ref:`RID<class_rid>` canvas_item, :ref:`Vector2<class_vector2>` pos, :ref:`int<class_int>` char, :ref:`int<class_int>` next=-1, :ref:`Color<class_color>` modulate=Color(1,1,1,1)  **)** const

Draw character "char" into a canvas item using the font at a given "pos" position, with "modulate" color, and optionally kerning if "next" is apassed. clipping the width. "pos" specifies te baseline, not the top. To draw from the top, *ascent* must be added to the Y axis. The width used by the character is returned, making this function useful for drawing strings character by character.

.. _class_Font_set_fallback:

- void  **set_fallback**  **(** :ref:`Object<class_object>` fallback  **)**

.. _class_Font_get_fallback:

- :ref:`Object<class_object>`  **get_fallback**  **(** **)** const


