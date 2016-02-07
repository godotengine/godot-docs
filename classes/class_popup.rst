.. _class_Popup:

Popup
=====

**Inherits:** :ref:`Control<class_control>` **<** :ref:`CanvasItem<class_canvasitem>` **<** :ref:`Node<class_node>` **<** :ref:`Object<class_object>`

**Inherited By:** :ref:`PopupPanel<class_popuppanel>`, :ref:`PopupDialog<class_popupdialog>`, :ref:`PopupMenu<class_popupmenu>`, :ref:`WindowDialog<class_windowdialog>`

**Category:** Core

Brief Description
-----------------

Base container control for popups and dialogs.

Member Functions
----------------

+--------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| void                     | :ref:`popup_centered<class_Popup_popup_centered>`  **(** :ref:`Vector2<class_vector2>` size=Vector2(0,0)  **)**                    |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| void                     | :ref:`popup_centered_ratio<class_Popup_popup_centered_ratio>`  **(** :ref:`float<class_float>` ratio=0.75  **)**                   |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| void                     | :ref:`popup_centered_minsize<class_Popup_popup_centered_minsize>`  **(** :ref:`Vector2<class_vector2>` minsize=Vector2(0,0)  **)** |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| void                     | :ref:`popup<class_Popup_popup>`  **(** **)**                                                                                       |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| void                     | :ref:`set_exclusive<class_Popup_set_exclusive>`  **(** :ref:`bool<class_bool>` enable  **)**                                       |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`  | :ref:`is_exclusive<class_Popup_is_exclusive>`  **(** **)** const                                                                   |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------+

Signals
-------

-  **popup_hide**  **(** **)**
-  **about_to_show**  **(** **)**

Numeric Constants
-----------------

- **NOTIFICATION_POST_POPUP** = **80**
- **NOTIFICATION_POPUP_HIDE** = **81**

Description
-----------

Popup is a base :ref:`Control<class_control>` used to show dialogs and popups. It's a subwindow and modal by default (see :ref:`Control<class_control>`) and has helpers for custom popup behavior.

Member Function Description
---------------------------

.. _class_Popup_popup_centered:

- void  **popup_centered**  **(** :ref:`Vector2<class_vector2>` size=Vector2(0,0)  **)**

Popup (show the control in modal form) in the center of the screen, at the current size, or at a size determined by "size".

.. _class_Popup_popup_centered_ratio:

- void  **popup_centered_ratio**  **(** :ref:`float<class_float>` ratio=0.75  **)**

Popup (show the control in modal form) in the center of the screen, scalled at a ratio of size of the screen.

.. _class_Popup_popup_centered_minsize:

- void  **popup_centered_minsize**  **(** :ref:`Vector2<class_vector2>` minsize=Vector2(0,0)  **)**

.. _class_Popup_popup:

- void  **popup**  **(** **)**

Popup (show the control in modal form).

.. _class_Popup_set_exclusive:

- void  **set_exclusive**  **(** :ref:`bool<class_bool>` enable  **)**

.. _class_Popup_is_exclusive:

- :ref:`bool<class_bool>`  **is_exclusive**  **(** **)** const


