.. _class_WindowDialog:

WindowDialog
============

Inherits: :ref:`Popup<class_popup>`
-----------------------------------

Category: Core
--------------

Brief Description
-----------------

Base class for window dialogs.

Member Functions
----------------

+--------------------------------------------+------------------------------------------------------------------------------------------------+
| void                                       | :ref:`set_title<class_WindowDialog_set_title>`  **(** :ref:`String<class_string>` title  **)** |
+--------------------------------------------+------------------------------------------------------------------------------------------------+
| :ref:`String<class_string>`                | :ref:`get_title<class_WindowDialog_get_title>`  **(** **)** const                              |
+--------------------------------------------+------------------------------------------------------------------------------------------------+
| :ref:`TextureButton<class_texturebutton>`  | :ref:`get_close_button<class_WindowDialog_get_close_button>`  **(** **)**                      |
+--------------------------------------------+------------------------------------------------------------------------------------------------+

Description
-----------

Windowdialog is the base class for all window-based dialogs. It's a by-default toplevel :ref:`Control<class_control>` that draws a window decoration and allows motion and resizing.

Member Function Description
---------------------------

.. _class_WindowDialog_set_title:

- void  **set_title**  **(** :ref:`String<class_string>` title  **)**

Set the title of the window.

.. _class_WindowDialog_get_title:

- :ref:`String<class_string>`  **get_title**  **(** **)** const

Return the title of the window.

.. _class_WindowDialog_get_close_button:

- :ref:`TextureButton<class_texturebutton>`  **get_close_button**  **(** **)**

Return the close :ref:`TextureButton<class_texturebutton>`.


