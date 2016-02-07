.. _class_Tree:

Tree
====

**Inherits:** :ref:`Control<class_control>`

**Category:** Core



Member Functions
----------------

+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| void                             | :ref:`clear<class_Tree_clear>`  **(** **)**                                                                                                        |
+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`TreeItem<class_treeitem>`  | :ref:`create_item<class_Tree_create_item>`  **(** :ref:`TreeItem<class_treeitem>` parent=Object()  **)**                                           |
+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`TreeItem<class_treeitem>`  | :ref:`get_root<class_Tree_get_root>`  **(** **)**                                                                                                  |
+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| void                             | :ref:`set_column_min_width<class_Tree_set_column_min_width>`  **(** :ref:`int<class_int>` column, :ref:`int<class_int>` min_width  **)**           |
+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| void                             | :ref:`set_column_expand<class_Tree_set_column_expand>`  **(** :ref:`int<class_int>` column, :ref:`bool<class_bool>` expand  **)**                  |
+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`            | :ref:`get_column_width<class_Tree_get_column_width>`  **(** :ref:`int<class_int>` column  **)** const                                              |
+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| void                             | :ref:`set_hide_root<class_Tree_set_hide_root>`  **(** :ref:`bool<class_bool>` enable  **)**                                                        |
+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`TreeItem<class_treeitem>`  | :ref:`get_next_selected<class_Tree_get_next_selected>`  **(** :ref:`TreeItem<class_treeitem>` from  **)**                                          |
+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`TreeItem<class_treeitem>`  | :ref:`get_selected<class_Tree_get_selected>`  **(** **)** const                                                                                    |
+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`            | :ref:`get_selected_column<class_Tree_get_selected_column>`  **(** **)** const                                                                      |
+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`            | :ref:`get_pressed_button<class_Tree_get_pressed_button>`  **(** **)** const                                                                        |
+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| void                             | :ref:`set_select_mode<class_Tree_set_select_mode>`  **(** :ref:`int<class_int>` mode  **)**                                                        |
+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| void                             | :ref:`set_columns<class_Tree_set_columns>`  **(** :ref:`int<class_int>` amount  **)**                                                              |
+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`            | :ref:`get_columns<class_Tree_get_columns>`  **(** **)** const                                                                                      |
+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`TreeItem<class_treeitem>`  | :ref:`get_edited<class_Tree_get_edited>`  **(** **)** const                                                                                        |
+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`            | :ref:`get_edited_column<class_Tree_get_edited_column>`  **(** **)** const                                                                          |
+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Rect2<class_rect2>`        | :ref:`get_custom_popup_rect<class_Tree_get_custom_popup_rect>`  **(** **)** const                                                                  |
+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Rect2<class_rect2>`        | :ref:`get_item_area_rect<class_Tree_get_item_area_rect>`  **(** :ref:`TreeItem<class_treeitem>` item, :ref:`int<class_int>` column=-1  **)** const |
+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| void                             | :ref:`ensure_cursor_is_visible<class_Tree_ensure_cursor_is_visible>`  **(** **)**                                                                  |
+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| void                             | :ref:`set_column_titles_visible<class_Tree_set_column_titles_visible>`  **(** :ref:`bool<class_bool>` visible  **)**                               |
+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`          | :ref:`are_column_titles_visible<class_Tree_are_column_titles_visible>`  **(** **)** const                                                          |
+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| void                             | :ref:`set_column_title<class_Tree_set_column_title>`  **(** :ref:`int<class_int>` column, :ref:`String<class_string>` title  **)**                 |
+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`String<class_string>`      | :ref:`get_column_title<class_Tree_get_column_title>`  **(** :ref:`int<class_int>` column  **)** const                                              |
+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector2<class_vector2>`    | :ref:`get_scroll<class_Tree_get_scroll>`  **(** **)** const                                                                                        |
+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| void                             | :ref:`set_hide_folding<class_Tree_set_hide_folding>`  **(** :ref:`bool<class_bool>` hide  **)**                                                    |
+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`          | :ref:`is_folding_hidden<class_Tree_is_folding_hidden>`  **(** **)** const                                                                          |
+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+

Signals
-------

-  **item_activated**  **(** **)**
-  **multi_selected**  **(** :ref:`Object<class_object>` item, :ref:`int<class_int>` column, :ref:`bool<class_bool>` selected  **)**
-  **custom_popup_edited**  **(** :ref:`bool<class_bool>` arrow_clicked  **)**
-  **item_collapsed**  **(** :ref:`Object<class_object>` item  **)**
-  **item_edited**  **(** **)**
-  **item_selected**  **(** **)**
-  **cell_selected**  **(** **)**
-  **button_pressed**  **(** :ref:`Object<class_object>` item, :ref:`int<class_int>` column, :ref:`int<class_int>` id  **)**

Numeric Constants
-----------------

- **SELECT_SINGLE** = **0**
- **SELECT_ROW** = **1**
- **SELECT_MULTI** = **2**

Member Function Description
---------------------------

.. _class_Tree_clear:

- void  **clear**  **(** **)**

.. _class_Tree_create_item:

- :ref:`TreeItem<class_treeitem>`  **create_item**  **(** :ref:`TreeItem<class_treeitem>` parent=Object()  **)**

.. _class_Tree_get_root:

- :ref:`TreeItem<class_treeitem>`  **get_root**  **(** **)**

.. _class_Tree_set_column_min_width:

- void  **set_column_min_width**  **(** :ref:`int<class_int>` column, :ref:`int<class_int>` min_width  **)**

.. _class_Tree_set_column_expand:

- void  **set_column_expand**  **(** :ref:`int<class_int>` column, :ref:`bool<class_bool>` expand  **)**

.. _class_Tree_get_column_width:

- :ref:`int<class_int>`  **get_column_width**  **(** :ref:`int<class_int>` column  **)** const

.. _class_Tree_set_hide_root:

- void  **set_hide_root**  **(** :ref:`bool<class_bool>` enable  **)**

.. _class_Tree_get_next_selected:

- :ref:`TreeItem<class_treeitem>`  **get_next_selected**  **(** :ref:`TreeItem<class_treeitem>` from  **)**

.. _class_Tree_get_selected:

- :ref:`TreeItem<class_treeitem>`  **get_selected**  **(** **)** const

.. _class_Tree_get_selected_column:

- :ref:`int<class_int>`  **get_selected_column**  **(** **)** const

.. _class_Tree_get_pressed_button:

- :ref:`int<class_int>`  **get_pressed_button**  **(** **)** const

.. _class_Tree_set_select_mode:

- void  **set_select_mode**  **(** :ref:`int<class_int>` mode  **)**

.. _class_Tree_set_columns:

- void  **set_columns**  **(** :ref:`int<class_int>` amount  **)**

.. _class_Tree_get_columns:

- :ref:`int<class_int>`  **get_columns**  **(** **)** const

.. _class_Tree_get_edited:

- :ref:`TreeItem<class_treeitem>`  **get_edited**  **(** **)** const

.. _class_Tree_get_edited_column:

- :ref:`int<class_int>`  **get_edited_column**  **(** **)** const

.. _class_Tree_get_custom_popup_rect:

- :ref:`Rect2<class_rect2>`  **get_custom_popup_rect**  **(** **)** const

.. _class_Tree_get_item_area_rect:

- :ref:`Rect2<class_rect2>`  **get_item_area_rect**  **(** :ref:`TreeItem<class_treeitem>` item, :ref:`int<class_int>` column=-1  **)** const

.. _class_Tree_ensure_cursor_is_visible:

- void  **ensure_cursor_is_visible**  **(** **)**

.. _class_Tree_set_column_titles_visible:

- void  **set_column_titles_visible**  **(** :ref:`bool<class_bool>` visible  **)**

.. _class_Tree_are_column_titles_visible:

- :ref:`bool<class_bool>`  **are_column_titles_visible**  **(** **)** const

.. _class_Tree_set_column_title:

- void  **set_column_title**  **(** :ref:`int<class_int>` column, :ref:`String<class_string>` title  **)**

.. _class_Tree_get_column_title:

- :ref:`String<class_string>`  **get_column_title**  **(** :ref:`int<class_int>` column  **)** const

.. _class_Tree_get_scroll:

- :ref:`Vector2<class_vector2>`  **get_scroll**  **(** **)** const

.. _class_Tree_set_hide_folding:

- void  **set_hide_folding**  **(** :ref:`bool<class_bool>` hide  **)**

.. _class_Tree_is_folding_hidden:

- :ref:`bool<class_bool>`  **is_folding_hidden**  **(** **)** const


