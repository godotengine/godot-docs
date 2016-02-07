.. _class_ItemList:

ItemList
========

**Inherits:** :ref:`Control<class_control>`

**Category:** Core



Member Functions
----------------

+--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`add_item<class_ItemList_add_item>`  **(** :ref:`String<class_string>` text, :ref:`Texture<class_texture>` icon=Object(), :ref:`bool<class_bool>` selectable=true  **)** |
+--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`add_icon_item<class_ItemList_add_icon_item>`  **(** :ref:`Texture<class_texture>` icon, :ref:`bool<class_bool>` selectable=true  **)**                                  |
+--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_item_text<class_ItemList_set_item_text>`  **(** :ref:`int<class_int>` idx, :ref:`String<class_string>` text  **)**                                                  |
+--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`String<class_string>`    | :ref:`get_item_text<class_ItemList_get_item_text>`  **(** :ref:`int<class_int>` idx  **)** const                                                                              |
+--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_item_icon<class_ItemList_set_item_icon>`  **(** :ref:`int<class_int>` idx, :ref:`Texture<class_texture>` icon  **)**                                                |
+--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Texture<class_texture>`  | :ref:`get_item_icon<class_ItemList_get_item_icon>`  **(** :ref:`int<class_int>` idx  **)** const                                                                              |
+--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_item_selectable<class_ItemList_set_item_selectable>`  **(** :ref:`int<class_int>` idx, :ref:`bool<class_bool>` selectable  **)**                                    |
+--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`        | :ref:`is_item_selectable<class_ItemList_is_item_selectable>`  **(** :ref:`int<class_int>` idx  **)** const                                                                    |
+--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_item_disabled<class_ItemList_set_item_disabled>`  **(** :ref:`int<class_int>` idx, :ref:`bool<class_bool>` disabled  **)**                                          |
+--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`        | :ref:`is_item_disabled<class_ItemList_is_item_disabled>`  **(** :ref:`int<class_int>` idx  **)** const                                                                        |
+--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_item_metadata<class_ItemList_set_item_metadata>`  **(** :ref:`int<class_int>` idx, var metadata  **)**                                                              |
+--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`get_item_metadata<class_ItemList_get_item_metadata>`  **(** :ref:`int<class_int>` idx  **)** const                                                                      |
+--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_item_custom_bg_color<class_ItemList_set_item_custom_bg_color>`  **(** :ref:`int<class_int>` idx, :ref:`Color<class_color>` custom_bg_color  **)**                   |
+--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Color<class_color>`      | :ref:`get_item_custom_bg_color<class_ItemList_get_item_custom_bg_color>`  **(** :ref:`int<class_int>` idx  **)** const                                                        |
+--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_item_tooltip<class_ItemList_set_item_tooltip>`  **(** :ref:`int<class_int>` idx, :ref:`String<class_string>` tooltip  **)**                                         |
+--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`String<class_string>`    | :ref:`get_item_tooltip<class_ItemList_get_item_tooltip>`  **(** :ref:`int<class_int>` idx  **)** const                                                                        |
+--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`select<class_ItemList_select>`  **(** :ref:`int<class_int>` idx, :ref:`bool<class_bool>` single=true  **)**                                                             |
+--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`unselect<class_ItemList_unselect>`  **(** :ref:`int<class_int>` idx  **)**                                                                                              |
+--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`        | :ref:`is_selected<class_ItemList_is_selected>`  **(** :ref:`int<class_int>` idx  **)** const                                                                                  |
+--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`          | :ref:`get_item_count<class_ItemList_get_item_count>`  **(** **)** const                                                                                                       |
+--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`remove_item<class_ItemList_remove_item>`  **(** :ref:`int<class_int>` idx  **)**                                                                                        |
+--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`clear<class_ItemList_clear>`  **(** **)**                                                                                                                               |
+--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`sort_items_by_text<class_ItemList_sort_items_by_text>`  **(** **)**                                                                                                     |
+--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_fixed_column_width<class_ItemList_set_fixed_column_width>`  **(** :ref:`int<class_int>` width  **)**                                                                |
+--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`          | :ref:`get_fixed_column_width<class_ItemList_get_fixed_column_width>`  **(** **)** const                                                                                       |
+--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_max_text_lines<class_ItemList_set_max_text_lines>`  **(** :ref:`int<class_int>` lines  **)**                                                                        |
+--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`          | :ref:`get_max_text_lines<class_ItemList_get_max_text_lines>`  **(** **)** const                                                                                               |
+--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_max_columns<class_ItemList_set_max_columns>`  **(** :ref:`int<class_int>` amount  **)**                                                                             |
+--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`          | :ref:`get_max_columns<class_ItemList_get_max_columns>`  **(** **)** const                                                                                                     |
+--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_select_mode<class_ItemList_set_select_mode>`  **(** :ref:`int<class_int>` mode  **)**                                                                               |
+--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`          | :ref:`get_select_mode<class_ItemList_get_select_mode>`  **(** **)** const                                                                                                     |
+--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_icon_mode<class_ItemList_set_icon_mode>`  **(** :ref:`int<class_int>` mode  **)**                                                                                   |
+--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`          | :ref:`get_icon_mode<class_ItemList_get_icon_mode>`  **(** **)** const                                                                                                         |
+--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_min_icon_size<class_ItemList_set_min_icon_size>`  **(** :ref:`Vector2<class_vector2>` size  **)**                                                                   |
+--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector2<class_vector2>`  | :ref:`get_min_icon_size<class_ItemList_get_min_icon_size>`  **(** **)** const                                                                                                 |
+--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`ensure_current_is_visible<class_ItemList_ensure_current_is_visible>`  **(** **)**                                                                                       |
+--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Signals
-------

-  **item_activated**  **(** :ref:`int<class_int>` index  **)**
-  **multi_selected**  **(** :ref:`int<class_int>` index, :ref:`bool<class_bool>` selected  **)**
-  **item_selected**  **(** :ref:`int<class_int>` index  **)**

Numeric Constants
-----------------

- **ICON_MODE_TOP** = **0**
- **ICON_MODE_LEFT** = **1**
- **SELECT_SINGLE** = **0**
- **SELECT_MULTI** = **1**

Member Function Description
---------------------------

.. _class_ItemList_add_item:

- void  **add_item**  **(** :ref:`String<class_string>` text, :ref:`Texture<class_texture>` icon=Object(), :ref:`bool<class_bool>` selectable=true  **)**

.. _class_ItemList_add_icon_item:

- void  **add_icon_item**  **(** :ref:`Texture<class_texture>` icon, :ref:`bool<class_bool>` selectable=true  **)**

.. _class_ItemList_set_item_text:

- void  **set_item_text**  **(** :ref:`int<class_int>` idx, :ref:`String<class_string>` text  **)**

.. _class_ItemList_get_item_text:

- :ref:`String<class_string>`  **get_item_text**  **(** :ref:`int<class_int>` idx  **)** const

.. _class_ItemList_set_item_icon:

- void  **set_item_icon**  **(** :ref:`int<class_int>` idx, :ref:`Texture<class_texture>` icon  **)**

.. _class_ItemList_get_item_icon:

- :ref:`Texture<class_texture>`  **get_item_icon**  **(** :ref:`int<class_int>` idx  **)** const

.. _class_ItemList_set_item_selectable:

- void  **set_item_selectable**  **(** :ref:`int<class_int>` idx, :ref:`bool<class_bool>` selectable  **)**

.. _class_ItemList_is_item_selectable:

- :ref:`bool<class_bool>`  **is_item_selectable**  **(** :ref:`int<class_int>` idx  **)** const

.. _class_ItemList_set_item_disabled:

- void  **set_item_disabled**  **(** :ref:`int<class_int>` idx, :ref:`bool<class_bool>` disabled  **)**

.. _class_ItemList_is_item_disabled:

- :ref:`bool<class_bool>`  **is_item_disabled**  **(** :ref:`int<class_int>` idx  **)** const

.. _class_ItemList_set_item_metadata:

- void  **set_item_metadata**  **(** :ref:`int<class_int>` idx, var metadata  **)**

.. _class_ItemList_get_item_metadata:

- void  **get_item_metadata**  **(** :ref:`int<class_int>` idx  **)** const

.. _class_ItemList_set_item_custom_bg_color:

- void  **set_item_custom_bg_color**  **(** :ref:`int<class_int>` idx, :ref:`Color<class_color>` custom_bg_color  **)**

.. _class_ItemList_get_item_custom_bg_color:

- :ref:`Color<class_color>`  **get_item_custom_bg_color**  **(** :ref:`int<class_int>` idx  **)** const

.. _class_ItemList_set_item_tooltip:

- void  **set_item_tooltip**  **(** :ref:`int<class_int>` idx, :ref:`String<class_string>` tooltip  **)**

.. _class_ItemList_get_item_tooltip:

- :ref:`String<class_string>`  **get_item_tooltip**  **(** :ref:`int<class_int>` idx  **)** const

.. _class_ItemList_select:

- void  **select**  **(** :ref:`int<class_int>` idx, :ref:`bool<class_bool>` single=true  **)**

.. _class_ItemList_unselect:

- void  **unselect**  **(** :ref:`int<class_int>` idx  **)**

.. _class_ItemList_is_selected:

- :ref:`bool<class_bool>`  **is_selected**  **(** :ref:`int<class_int>` idx  **)** const

.. _class_ItemList_get_item_count:

- :ref:`int<class_int>`  **get_item_count**  **(** **)** const

.. _class_ItemList_remove_item:

- void  **remove_item**  **(** :ref:`int<class_int>` idx  **)**

.. _class_ItemList_clear:

- void  **clear**  **(** **)**

.. _class_ItemList_sort_items_by_text:

- void  **sort_items_by_text**  **(** **)**

.. _class_ItemList_set_fixed_column_width:

- void  **set_fixed_column_width**  **(** :ref:`int<class_int>` width  **)**

.. _class_ItemList_get_fixed_column_width:

- :ref:`int<class_int>`  **get_fixed_column_width**  **(** **)** const

.. _class_ItemList_set_max_text_lines:

- void  **set_max_text_lines**  **(** :ref:`int<class_int>` lines  **)**

.. _class_ItemList_get_max_text_lines:

- :ref:`int<class_int>`  **get_max_text_lines**  **(** **)** const

.. _class_ItemList_set_max_columns:

- void  **set_max_columns**  **(** :ref:`int<class_int>` amount  **)**

.. _class_ItemList_get_max_columns:

- :ref:`int<class_int>`  **get_max_columns**  **(** **)** const

.. _class_ItemList_set_select_mode:

- void  **set_select_mode**  **(** :ref:`int<class_int>` mode  **)**

.. _class_ItemList_get_select_mode:

- :ref:`int<class_int>`  **get_select_mode**  **(** **)** const

.. _class_ItemList_set_icon_mode:

- void  **set_icon_mode**  **(** :ref:`int<class_int>` mode  **)**

.. _class_ItemList_get_icon_mode:

- :ref:`int<class_int>`  **get_icon_mode**  **(** **)** const

.. _class_ItemList_set_min_icon_size:

- void  **set_min_icon_size**  **(** :ref:`Vector2<class_vector2>` size  **)**

.. _class_ItemList_get_min_icon_size:

- :ref:`Vector2<class_vector2>`  **get_min_icon_size**  **(** **)** const

.. _class_ItemList_ensure_current_is_visible:

- void  **ensure_current_is_visible**  **(** **)**


