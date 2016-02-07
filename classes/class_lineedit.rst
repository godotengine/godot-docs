.. _class_LineEdit:

LineEdit
========

**Inherits:** :ref:`Control<class_control>`

**Category:** Core

Control that provides single line string editing.

Member Functions
----------------

+------------------------------+--------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`set_align<class_LineEdit_set_align>`  **(** :ref:`int<class_int>` align  **)**                         |
+------------------------------+--------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`        | :ref:`get_align<class_LineEdit_get_align>`  **(** **)** const                                                |
+------------------------------+--------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`clear<class_LineEdit_clear>`  **(** **)**                                                              |
+------------------------------+--------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`select_all<class_LineEdit_select_all>`  **(** **)**                                                    |
+------------------------------+--------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`set_text<class_LineEdit_set_text>`  **(** :ref:`String<class_string>` text  **)**                      |
+------------------------------+--------------------------------------------------------------------------------------------------------------+
| :ref:`String<class_string>`  | :ref:`get_text<class_LineEdit_get_text>`  **(** **)** const                                                  |
+------------------------------+--------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`set_cursor_pos<class_LineEdit_set_cursor_pos>`  **(** :ref:`int<class_int>` pos  **)**                 |
+------------------------------+--------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`        | :ref:`get_cursor_pos<class_LineEdit_get_cursor_pos>`  **(** **)** const                                      |
+------------------------------+--------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`set_max_length<class_LineEdit_set_max_length>`  **(** :ref:`int<class_int>` chars  **)**               |
+------------------------------+--------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`        | :ref:`get_max_length<class_LineEdit_get_max_length>`  **(** **)** const                                      |
+------------------------------+--------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`append_at_cursor<class_LineEdit_append_at_cursor>`  **(** :ref:`String<class_string>` text  **)**      |
+------------------------------+--------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`set_editable<class_LineEdit_set_editable>`  **(** :ref:`bool<class_bool>` enabled  **)**               |
+------------------------------+--------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`      | :ref:`is_editable<class_LineEdit_is_editable>`  **(** **)** const                                            |
+------------------------------+--------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`set_secret<class_LineEdit_set_secret>`  **(** :ref:`bool<class_bool>` enabled  **)**                   |
+------------------------------+--------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`      | :ref:`is_secret<class_LineEdit_is_secret>`  **(** **)** const                                                |
+------------------------------+--------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`select<class_LineEdit_select>`  **(** :ref:`int<class_int>` from=0, :ref:`int<class_int>` to=-1  **)** |
+------------------------------+--------------------------------------------------------------------------------------------------------------+

Signals
-------

-  **text_entered**  **(** :ref:`String<class_string>` text  **)**
-  **text_changed**  **(** :ref:`String<class_string>` text  **)**

Numeric Constants
-----------------

- **ALIGN_LEFT** = **0**
- **ALIGN_CENTER** = **1**
- **ALIGN_RIGHT** = **2**
- **ALIGN_FILL** = **3**

Description
-----------

LineEdit provides a single line string editor, used for text fields.

Member Function Description
---------------------------

.. _class_LineEdit_set_align:

- void  **set_align**  **(** :ref:`int<class_int>` align  **)**

.. _class_LineEdit_get_align:

- :ref:`int<class_int>`  **get_align**  **(** **)** const

.. _class_LineEdit_clear:

- void  **clear**  **(** **)**

Clear the :ref:`LineEdit<class_lineedit>` text.

.. _class_LineEdit_select_all:

- void  **select_all**  **(** **)**

Select the whole string.

.. _class_LineEdit_set_text:

- void  **set_text**  **(** :ref:`String<class_string>` text  **)**

Set the text in the :ref:`LineEdit<class_lineedit>`, clearing the existing one and the selection.

.. _class_LineEdit_get_text:

- :ref:`String<class_string>`  **get_text**  **(** **)** const

Return the text in the :ref:`LineEdit<class_lineedit>`.

.. _class_LineEdit_set_cursor_pos:

- void  **set_cursor_pos**  **(** :ref:`int<class_int>` pos  **)**

Set the cursor position inside the :ref:`LineEdit<class_lineedit>`, causing it to scroll if needed.

.. _class_LineEdit_get_cursor_pos:

- :ref:`int<class_int>`  **get_cursor_pos**  **(** **)** const

Return the cursor position inside the :ref:`LineEdit<class_lineedit>`.

.. _class_LineEdit_set_max_length:

- void  **set_max_length**  **(** :ref:`int<class_int>` chars  **)**

Set the maximum amount of characters the :ref:`LineEdit<class_lineedit>` can edit, and cropping existing text in case it exceeds that limit. Setting 0 removes the limit.

.. _class_LineEdit_get_max_length:

- :ref:`int<class_int>`  **get_max_length**  **(** **)** const

Return the maximum amount of characters the :ref:`LineEdit<class_lineedit>` can edit. If 0 is returned, no limit exists.

.. _class_LineEdit_append_at_cursor:

- void  **append_at_cursor**  **(** :ref:`String<class_string>` text  **)**

Append text at cursor, scrolling the :ref:`LineEdit<class_lineedit>` when needed.

.. _class_LineEdit_set_editable:

- void  **set_editable**  **(** :ref:`bool<class_bool>` enabled  **)**

Set the *editable* status of the :ref:`LineEdit<class_lineedit>`. When disabled, existing text can't be modified and new text can't be added.

.. _class_LineEdit_is_editable:

- :ref:`bool<class_bool>`  **is_editable**  **(** **)** const

Return the *editable* status of the :ref:`LineEdit<class_lineedit>` (see :ref:`set_editable<LineEdit_set_editable>`).

.. _class_LineEdit_set_secret:

- void  **set_secret**  **(** :ref:`bool<class_bool>` enabled  **)**

Set the *secret* status of the :ref:`LineEdit<class_lineedit>`. When enabled, every character is displayed as "\*".

.. _class_LineEdit_is_secret:

- :ref:`bool<class_bool>`  **is_secret**  **(** **)** const

Return the *secret* status of the :ref:`LineEdit<class_lineedit>` (see :ref:`set_secret<LineEdit_set_secret>`).

.. _class_LineEdit_select:

- void  **select**  **(** :ref:`int<class_int>` from=0, :ref:`int<class_int>` to=-1  **)**


