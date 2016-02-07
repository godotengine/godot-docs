.. _class_ButtonGroup:

ButtonGroup
===========

Inherits: :ref:`BoxContainer<class_boxcontainer>`
-------------------------------------------------

Category: Core
--------------

Brief Description
-----------------

Group of Buttons.

Member Functions
----------------

+--------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| :ref:`BaseButton<class_basebutton>`  | :ref:`get_pressed_button<class_ButtonGroup_get_pressed_button>`  **(** **)** const                                       |
+--------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`                | :ref:`get_pressed_button_index<class_ButtonGroup_get_pressed_button_index>`  **(** **)** const                           |
+--------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| :ref:`BaseButton<class_basebutton>`  | :ref:`get_focused_button<class_ButtonGroup_get_focused_button>`  **(** **)** const                                       |
+--------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| :ref:`Array<class_array>`            | :ref:`get_button_list<class_ButtonGroup_get_button_list>`  **(** **)** const                                             |
+--------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| void                                 | :ref:`set_pressed_button<class_ButtonGroup_set_pressed_button>`  **(** :ref:`BaseButton<class_basebutton>` button  **)** |
+--------------------------------------+--------------------------------------------------------------------------------------------------------------------------+

Description
-----------

Group of :ref:`Button<class_button>`s. All direct and indirect children buttons become radios. Only one allows being pressed.

Member Function Description
---------------------------

.. _class_ButtonGroup_get_pressed_button:

- :ref:`BaseButton<class_basebutton>`  **get_pressed_button**  **(** **)** const

Return the pressed button.

.. _class_ButtonGroup_get_pressed_button_index:

- :ref:`int<class_int>`  **get_pressed_button_index**  **(** **)** const

Return the index of the pressed button (by tree order).

.. _class_ButtonGroup_get_focused_button:

- :ref:`BaseButton<class_basebutton>`  **get_focused_button**  **(** **)** const

Return the focused button.

.. _class_ButtonGroup_get_button_list:

- :ref:`Array<class_array>`  **get_button_list**  **(** **)** const

Return the list of all the buttons in the group.

.. _class_ButtonGroup_set_pressed_button:

- void  **set_pressed_button**  **(** :ref:`BaseButton<class_basebutton>` button  **)**

Set the button to be pressed.


