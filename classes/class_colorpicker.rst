.. _class_ColorPicker:

ColorPicker
===========

Inherits: :ref:`BoxContainer<class_boxcontainer>`
-------------------------------------------------

Category: Core
--------------

Brief Description
-----------------

Color picker control.

Member Functions
----------------

+----------------------------+----------------------------------------------------------------------------------------------------+
| void                       | :ref:`set_color<class_ColorPicker_set_color>`  **(** :ref:`Color<class_color>` color  **)**        |
+----------------------------+----------------------------------------------------------------------------------------------------+
| :ref:`Color<class_color>`  | :ref:`get_color<class_ColorPicker_get_color>`  **(** **)** const                                   |
+----------------------------+----------------------------------------------------------------------------------------------------+
| void                       | :ref:`set_raw_mode<class_ColorPicker_set_raw_mode>`  **(** :ref:`bool<class_bool>` mode  **)**     |
+----------------------------+----------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`    | :ref:`is_raw_mode<class_ColorPicker_is_raw_mode>`  **(** **)** const                               |
+----------------------------+----------------------------------------------------------------------------------------------------+
| void                       | :ref:`set_edit_alpha<class_ColorPicker_set_edit_alpha>`  **(** :ref:`bool<class_bool>` show  **)** |
+----------------------------+----------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`    | :ref:`is_editing_alpha<class_ColorPicker_is_editing_alpha>`  **(** **)** const                     |
+----------------------------+----------------------------------------------------------------------------------------------------+
| void                       | :ref:`add_preset<class_ColorPicker_add_preset>`  **(** :ref:`Color<class_color>` arg0  **)**       |
+----------------------------+----------------------------------------------------------------------------------------------------+

Signals
-------

-  **color_changed**  **(** :ref:`Color<class_color>` color  **)**

Description
-----------

This is a simple color picker :ref:`Control<class_control>`. It's useful for selecting a color from an RGB/RGBA colorspace.

Member Function Description
---------------------------

.. _class_ColorPicker_set_color:

- void  **set_color**  **(** :ref:`Color<class_color>` color  **)**

Select the current color.

.. _class_ColorPicker_get_color:

- :ref:`Color<class_color>`  **get_color**  **(** **)** const

Return the current (edited) color.

.. _class_ColorPicker_set_raw_mode:

- void  **set_raw_mode**  **(** :ref:`bool<class_bool>` mode  **)**

.. _class_ColorPicker_is_raw_mode:

- :ref:`bool<class_bool>`  **is_raw_mode**  **(** **)** const

.. _class_ColorPicker_set_edit_alpha:

- void  **set_edit_alpha**  **(** :ref:`bool<class_bool>` show  **)**

.. _class_ColorPicker_is_editing_alpha:

- :ref:`bool<class_bool>`  **is_editing_alpha**  **(** **)** const

.. _class_ColorPicker_add_preset:

- void  **add_preset**  **(** :ref:`Color<class_color>` arg0  **)**


