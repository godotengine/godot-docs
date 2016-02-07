.. _class_TextEdit:

TextEdit
========

**Inherits:** :ref:`Control<class_control>` **<** :ref:`CanvasItem<class_canvasitem>` **<** :ref:`Node<class_node>` **<** :ref:`Object<class_object>`

**Category:** Core

Brief Description
-----------------

Multiline text editing control.

Member Functions
----------------

+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                             | :ref:`set_text<class_TextEdit_set_text>`  **(** :ref:`String<class_string>` text  **)**                                                                                                                                     |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                             | :ref:`insert_text_at_cursor<class_TextEdit_insert_text_at_cursor>`  **(** :ref:`String<class_string>` text  **)**                                                                                                           |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`            | :ref:`get_line_count<class_TextEdit_get_line_count>`  **(** **)** const                                                                                                                                                     |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`String<class_string>`      | :ref:`get_text<class_TextEdit_get_text>`  **(** **)**                                                                                                                                                                       |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`String<class_string>`      | :ref:`get_line<class_TextEdit_get_line>`  **(** :ref:`int<class_int>` line  **)** const                                                                                                                                     |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                             | :ref:`cursor_set_column<class_TextEdit_cursor_set_column>`  **(** :ref:`int<class_int>` column, :ref:`bool<class_bool>` adjust_viewport=false  **)**                                                                        |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                             | :ref:`cursor_set_line<class_TextEdit_cursor_set_line>`  **(** :ref:`int<class_int>` line, :ref:`bool<class_bool>` adjust_viewport=false  **)**                                                                              |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`            | :ref:`cursor_get_column<class_TextEdit_cursor_get_column>`  **(** **)** const                                                                                                                                               |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`            | :ref:`cursor_get_line<class_TextEdit_cursor_get_line>`  **(** **)** const                                                                                                                                                   |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                             | :ref:`set_readonly<class_TextEdit_set_readonly>`  **(** :ref:`bool<class_bool>` enable  **)**                                                                                                                               |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                             | :ref:`set_wrap<class_TextEdit_set_wrap>`  **(** :ref:`bool<class_bool>` enable  **)**                                                                                                                                       |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                             | :ref:`set_max_chars<class_TextEdit_set_max_chars>`  **(** :ref:`int<class_int>` amount  **)**                                                                                                                               |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                             | :ref:`cut<class_TextEdit_cut>`  **(** **)**                                                                                                                                                                                 |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                             | :ref:`copy<class_TextEdit_copy>`  **(** **)**                                                                                                                                                                               |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                             | :ref:`paste<class_TextEdit_paste>`  **(** **)**                                                                                                                                                                             |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                             | :ref:`select_all<class_TextEdit_select_all>`  **(** **)**                                                                                                                                                                   |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                             | :ref:`select<class_TextEdit_select>`  **(** :ref:`int<class_int>` from_line, :ref:`int<class_int>` from_column, :ref:`int<class_int>` to_line, :ref:`int<class_int>` to_column  **)**                                       |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`          | :ref:`is_selection_active<class_TextEdit_is_selection_active>`  **(** **)** const                                                                                                                                           |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`            | :ref:`get_selection_from_line<class_TextEdit_get_selection_from_line>`  **(** **)** const                                                                                                                                   |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`            | :ref:`get_selection_from_column<class_TextEdit_get_selection_from_column>`  **(** **)** const                                                                                                                               |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`            | :ref:`get_selection_to_line<class_TextEdit_get_selection_to_line>`  **(** **)** const                                                                                                                                       |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`            | :ref:`get_selection_to_column<class_TextEdit_get_selection_to_column>`  **(** **)** const                                                                                                                                   |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`String<class_string>`      | :ref:`get_selection_text<class_TextEdit_get_selection_text>`  **(** **)** const                                                                                                                                             |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`String<class_string>`      | :ref:`get_word_under_cursor<class_TextEdit_get_word_under_cursor>`  **(** **)** const                                                                                                                                       |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`IntArray<class_intarray>`  | :ref:`search<class_TextEdit_search>`  **(** :ref:`String<class_string>` flags, :ref:`int<class_int>` from_line, :ref:`int<class_int>` from_column, :ref:`int<class_int>` to_line  **)** const                               |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                             | :ref:`undo<class_TextEdit_undo>`  **(** **)**                                                                                                                                                                               |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                             | :ref:`redo<class_TextEdit_redo>`  **(** **)**                                                                                                                                                                               |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                             | :ref:`clear_undo_history<class_TextEdit_clear_undo_history>`  **(** **)**                                                                                                                                                   |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                             | :ref:`set_syntax_coloring<class_TextEdit_set_syntax_coloring>`  **(** :ref:`bool<class_bool>` enable  **)**                                                                                                                 |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`          | :ref:`is_syntax_coloring_enabled<class_TextEdit_is_syntax_coloring_enabled>`  **(** **)** const                                                                                                                             |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                             | :ref:`add_keyword_color<class_TextEdit_add_keyword_color>`  **(** :ref:`String<class_string>` keyword, :ref:`Color<class_color>` color  **)**                                                                               |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                             | :ref:`add_color_region<class_TextEdit_add_color_region>`  **(** :ref:`String<class_string>` begin_key, :ref:`String<class_string>` end_key, :ref:`Color<class_color>` color, :ref:`bool<class_bool>` line_only=false  **)** |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                             | :ref:`set_symbol_color<class_TextEdit_set_symbol_color>`  **(** :ref:`Color<class_color>` color  **)**                                                                                                                      |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                             | :ref:`set_custom_bg_color<class_TextEdit_set_custom_bg_color>`  **(** :ref:`Color<class_color>` color  **)**                                                                                                                |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                             | :ref:`clear_colors<class_TextEdit_clear_colors>`  **(** **)**                                                                                                                                                               |
+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Signals
-------

-  **text_changed**  **(** **)**
-  **cursor_changed**  **(** **)**
-  **request_completion**  **(** **)**

Numeric Constants
-----------------

- **SEARCH_MATCH_CASE** = **1** --- Match case when searching.
- **SEARCH_WHOLE_WORDS** = **2** --- Match whole words when searching.
- **SEARCH_BACKWARDS** = **4** --- Search from end to beginning.

Description
-----------

TextEdit is meant for editing large, multiline text. It also has facilities for editing code, such as syntax highlighting support and multiple levels of undo/redo.

Member Function Description
---------------------------

.. _class_TextEdit_set_text:

- void  **set_text**  **(** :ref:`String<class_string>` text  **)**

Set the entire text.

.. _class_TextEdit_insert_text_at_cursor:

- void  **insert_text_at_cursor**  **(** :ref:`String<class_string>` text  **)**

Insert a given text at the cursor position.

.. _class_TextEdit_get_line_count:

- :ref:`int<class_int>`  **get_line_count**  **(** **)** const

Return the amount of total lines in the text.

.. _class_TextEdit_get_text:

- :ref:`String<class_string>`  **get_text**  **(** **)**

Return the whole text.

.. _class_TextEdit_get_line:

- :ref:`String<class_string>`  **get_line**  **(** :ref:`int<class_int>` line  **)** const

Return the text of a specific line.

.. _class_TextEdit_cursor_set_column:

- void  **cursor_set_column**  **(** :ref:`int<class_int>` column, :ref:`bool<class_bool>` adjust_viewport=false  **)**

.. _class_TextEdit_cursor_set_line:

- void  **cursor_set_line**  **(** :ref:`int<class_int>` line, :ref:`bool<class_bool>` adjust_viewport=false  **)**

.. _class_TextEdit_cursor_get_column:

- :ref:`int<class_int>`  **cursor_get_column**  **(** **)** const

Return the column the editing cursor is at.

.. _class_TextEdit_cursor_get_line:

- :ref:`int<class_int>`  **cursor_get_line**  **(** **)** const

Return the line the editing cursor is at.

.. _class_TextEdit_set_readonly:

- void  **set_readonly**  **(** :ref:`bool<class_bool>` enable  **)**

Set the text editor as read-only. Text can be displayed but not edited.

.. _class_TextEdit_set_wrap:

- void  **set_wrap**  **(** :ref:`bool<class_bool>` enable  **)**

Enable text wrapping when it goes beyond he edge of what is visible.

.. _class_TextEdit_set_max_chars:

- void  **set_max_chars**  **(** :ref:`int<class_int>` amount  **)**

Set the maximum amount of characters editable.

.. _class_TextEdit_cut:

- void  **cut**  **(** **)**

Cut the current selection.

.. _class_TextEdit_copy:

- void  **copy**  **(** **)**

Copy the current selection.

.. _class_TextEdit_paste:

- void  **paste**  **(** **)**

Paste the current selection.

.. _class_TextEdit_select_all:

- void  **select_all**  **(** **)**

Select all the text.

.. _class_TextEdit_select:

- void  **select**  **(** :ref:`int<class_int>` from_line, :ref:`int<class_int>` from_column, :ref:`int<class_int>` to_line, :ref:`int<class_int>` to_column  **)**

Perform selection, from line/column to line/column.

.. _class_TextEdit_is_selection_active:

- :ref:`bool<class_bool>`  **is_selection_active**  **(** **)** const

Return true if the selection is active.

.. _class_TextEdit_get_selection_from_line:

- :ref:`int<class_int>`  **get_selection_from_line**  **(** **)** const

Return the selection begin line.

.. _class_TextEdit_get_selection_from_column:

- :ref:`int<class_int>`  **get_selection_from_column**  **(** **)** const

Return the selection begin column.

.. _class_TextEdit_get_selection_to_line:

- :ref:`int<class_int>`  **get_selection_to_line**  **(** **)** const

Return the selection end line.

.. _class_TextEdit_get_selection_to_column:

- :ref:`int<class_int>`  **get_selection_to_column**  **(** **)** const

Return the selection end column.

.. _class_TextEdit_get_selection_text:

- :ref:`String<class_string>`  **get_selection_text**  **(** **)** const

Return the text inside the selection.

.. _class_TextEdit_get_word_under_cursor:

- :ref:`String<class_string>`  **get_word_under_cursor**  **(** **)** const

.. _class_TextEdit_search:

- :ref:`IntArray<class_intarray>`  **search**  **(** :ref:`String<class_string>` flags, :ref:`int<class_int>` from_line, :ref:`int<class_int>` from_column, :ref:`int<class_int>` to_line  **)** const

Perform a search inside the text. Search flags can be specified in the SEARCH\_\* enum.

.. _class_TextEdit_undo:

- void  **undo**  **(** **)**

Perform undo operation.

.. _class_TextEdit_redo:

- void  **redo**  **(** **)**

Perform redo operation.

.. _class_TextEdit_clear_undo_history:

- void  **clear_undo_history**  **(** **)**

Clear the undo history.

.. _class_TextEdit_set_syntax_coloring:

- void  **set_syntax_coloring**  **(** :ref:`bool<class_bool>` enable  **)**

Set to enable the syntax coloring.

.. _class_TextEdit_is_syntax_coloring_enabled:

- :ref:`bool<class_bool>`  **is_syntax_coloring_enabled**  **(** **)** const

Return true if the syntax coloring is enabled.

.. _class_TextEdit_add_keyword_color:

- void  **add_keyword_color**  **(** :ref:`String<class_string>` keyword, :ref:`Color<class_color>` color  **)**

Add a keyword and its color.

.. _class_TextEdit_add_color_region:

- void  **add_color_region**  **(** :ref:`String<class_string>` begin_key, :ref:`String<class_string>` end_key, :ref:`Color<class_color>` color, :ref:`bool<class_bool>` line_only=false  **)**

Add color region (given the delimiters) and its colors.

.. _class_TextEdit_set_symbol_color:

- void  **set_symbol_color**  **(** :ref:`Color<class_color>` color  **)**

Set the color for symbols.

.. _class_TextEdit_set_custom_bg_color:

- void  **set_custom_bg_color**  **(** :ref:`Color<class_color>` color  **)**

Set a custom background color. A background color with alpha==0 disables this.

.. _class_TextEdit_clear_colors:

- void  **clear_colors**  **(** **)**

Clear all the syntax coloring information.


