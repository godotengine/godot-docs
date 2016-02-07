.. _class_Button:

Button
======

**Inherits:** :ref:`BaseButton<class_basebutton>`

**Category:** Core

Standard themed Button.

Member Functions
----------------

+--------------------------------+----------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_text<class_Button_set_text>`  **(** :ref:`String<class_string>` text  **)**                    |
+--------------------------------+----------------------------------------------------------------------------------------------------------+
| :ref:`String<class_string>`    | :ref:`get_text<class_Button_get_text>`  **(** **)** const                                                |
+--------------------------------+----------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_button_icon<class_Button_set_button_icon>`  **(** :ref:`Texture<class_texture>` texture  **)** |
+--------------------------------+----------------------------------------------------------------------------------------------------------+
| :ref:`Texture<class_texture>`  | :ref:`get_button_icon<class_Button_get_button_icon>`  **(** **)** const                                  |
+--------------------------------+----------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_flat<class_Button_set_flat>`  **(** :ref:`bool<class_bool>` enabled  **)**                     |
+--------------------------------+----------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_clip_text<class_Button_set_clip_text>`  **(** :ref:`bool<class_bool>` enabled  **)**           |
+--------------------------------+----------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`        | :ref:`get_clip_text<class_Button_get_clip_text>`  **(** **)** const                                      |
+--------------------------------+----------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_text_align<class_Button_set_text_align>`  **(** :ref:`int<class_int>` align  **)**             |
+--------------------------------+----------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`          | :ref:`get_text_align<class_Button_get_text_align>`  **(** **)** const                                    |
+--------------------------------+----------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`        | :ref:`is_flat<class_Button_is_flat>`  **(** **)** const                                                  |
+--------------------------------+----------------------------------------------------------------------------------------------------------+

Description
-----------

Button is just the standard themed button: :ref:`image src="images/button_example.png"/<class_image src="images/button_example.png"/>` It can contain text and an icon, and will display them according to the current :ref:`Theme<class_theme>`.

Member Function Description
---------------------------

.. _class_Button_set_text:

- void  **set_text**  **(** :ref:`String<class_string>` text  **)**

Set the button text, which will be displayed inside the button area.

.. _class_Button_get_text:

- :ref:`String<class_string>`  **get_text**  **(** **)** const

Return the button text.

.. _class_Button_set_button_icon:

- void  **set_button_icon**  **(** :ref:`Texture<class_texture>` texture  **)**

.. _class_Button_get_button_icon:

- :ref:`Texture<class_texture>`  **get_button_icon**  **(** **)** const

.. _class_Button_set_flat:

- void  **set_flat**  **(** :ref:`bool<class_bool>` enabled  **)**

Set the *flat* property of a Button. Flat buttons don't display decoration unless hoevered or pressed.

.. _class_Button_set_clip_text:

- void  **set_clip_text**  **(** :ref:`bool<class_bool>` enabled  **)**

Set the *clip_text* property of a Button. When this property is enabled, text that is too large to fit the button is clipped, when disabled (default) the Button will always be wide enough to hold the text.

.. _class_Button_get_clip_text:

- :ref:`bool<class_bool>`  **get_clip_text**  **(** **)** const

Return the state of the *clip_text* property (see :ref:`set_clip_text<Button_set_clip_text>`)

.. _class_Button_set_text_align:

- void  **set_text_align**  **(** :ref:`int<class_int>` align  **)**

.. _class_Button_get_text_align:

- :ref:`int<class_int>`  **get_text_align**  **(** **)** const

.. _class_Button_is_flat:

- :ref:`bool<class_bool>`  **is_flat**  **(** **)** const

Return the state of the *flat* property (see :ref:`set_flat<Button_set_flat>`)


