.. _class_PopupMenu:

PopupMenu
=========

**Inherits:** :ref:`Popup<class_popup>` **<** :ref:`Control<class_control>` **<** :ref:`CanvasItem<class_canvasitem>` **<** :ref:`Node<class_node>` **<** :ref:`Object<class_object>`

**Category:** Core

Brief Description
-----------------

PopupMenu displays a list of options.

Member Functions
----------------

+------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`add_icon_item<class_PopupMenu_add_icon_item>`  **(** :ref:`Object<class_object>` texture, :ref:`String<class_string>` label, :ref:`int<class_int>` id=-1, :ref:`int<class_int>` accel=0  **)**             |
+------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`add_item<class_PopupMenu_add_item>`  **(** :ref:`String<class_string>` label, :ref:`int<class_int>` id=-1, :ref:`int<class_int>` accel=0  **)**                                                            |
+------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`add_icon_check_item<class_PopupMenu_add_icon_check_item>`  **(** :ref:`Object<class_object>` texture, :ref:`String<class_string>` label, :ref:`int<class_int>` id=-1, :ref:`int<class_int>` accel=0  **)** |
+------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`add_check_item<class_PopupMenu_add_check_item>`  **(** :ref:`String<class_string>` label, :ref:`int<class_int>` id=-1, :ref:`int<class_int>` accel=0  **)**                                                |
+------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`add_submenu_item<class_PopupMenu_add_submenu_item>`  **(** :ref:`String<class_string>` label, :ref:`String<class_string>` submenu, :ref:`int<class_int>` id=-1  **)**                                      |
+------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`set_item_text<class_PopupMenu_set_item_text>`  **(** :ref:`int<class_int>` idx, :ref:`String<class_string>` text  **)**                                                                                    |
+------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`set_item_icon<class_PopupMenu_set_item_icon>`  **(** :ref:`int<class_int>` idx, :ref:`Object<class_object>` icon  **)**                                                                                    |
+------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`set_item_accelerator<class_PopupMenu_set_item_accelerator>`  **(** :ref:`int<class_int>` idx, :ref:`int<class_int>` accel  **)**                                                                           |
+------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`set_item_metadata<class_PopupMenu_set_item_metadata>`  **(** :ref:`int<class_int>` idx, var metadata  **)**                                                                                                |
+------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`set_item_checked<class_PopupMenu_set_item_checked>`  **(** :ref:`int<class_int>` idx, :ref:`bool<class_bool>` checked  **)**                                                                               |
+------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`set_item_disabled<class_PopupMenu_set_item_disabled>`  **(** :ref:`int<class_int>` idx, :ref:`bool<class_bool>` disabled  **)**                                                                            |
+------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`set_item_submenu<class_PopupMenu_set_item_submenu>`  **(** :ref:`int<class_int>` idx, :ref:`String<class_string>` submenu  **)**                                                                           |
+------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`set_item_as_separator<class_PopupMenu_set_item_as_separator>`  **(** :ref:`int<class_int>` idx, :ref:`bool<class_bool>` enable  **)**                                                                      |
+------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`set_item_as_checkable<class_PopupMenu_set_item_as_checkable>`  **(** :ref:`int<class_int>` idx, :ref:`bool<class_bool>` enable  **)**                                                                      |
+------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`set_item_ID<class_PopupMenu_set_item_ID>`  **(** :ref:`int<class_int>` idx, :ref:`int<class_int>` id  **)**                                                                                                |
+------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`String<class_string>`  | :ref:`get_item_text<class_PopupMenu_get_item_text>`  **(** :ref:`int<class_int>` idx  **)** const                                                                                                                |
+------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Object<class_object>`  | :ref:`get_item_icon<class_PopupMenu_get_item_icon>`  **(** :ref:`int<class_int>` idx  **)** const                                                                                                                |
+------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`get_item_metadata<class_PopupMenu_get_item_metadata>`  **(** :ref:`int<class_int>` idx  **)** const                                                                                                        |
+------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`        | :ref:`get_item_accelerator<class_PopupMenu_get_item_accelerator>`  **(** :ref:`int<class_int>` idx  **)** const                                                                                                  |
+------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`String<class_string>`  | :ref:`get_item_submenu<class_PopupMenu_get_item_submenu>`  **(** :ref:`int<class_int>` idx  **)** const                                                                                                          |
+------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`      | :ref:`is_item_separator<class_PopupMenu_is_item_separator>`  **(** :ref:`int<class_int>` idx  **)** const                                                                                                        |
+------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`      | :ref:`is_item_checkable<class_PopupMenu_is_item_checkable>`  **(** :ref:`int<class_int>` idx  **)** const                                                                                                        |
+------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`      | :ref:`is_item_checked<class_PopupMenu_is_item_checked>`  **(** :ref:`int<class_int>` idx  **)** const                                                                                                            |
+------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`      | :ref:`is_item_disabled<class_PopupMenu_is_item_disabled>`  **(** :ref:`int<class_int>` idx  **)** const                                                                                                          |
+------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`        | :ref:`get_item_ID<class_PopupMenu_get_item_ID>`  **(** :ref:`int<class_int>` idx  **)** const                                                                                                                    |
+------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`        | :ref:`get_item_index<class_PopupMenu_get_item_index>`  **(** :ref:`int<class_int>` id  **)** const                                                                                                               |
+------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`        | :ref:`get_item_count<class_PopupMenu_get_item_count>`  **(** **)** const                                                                                                                                         |
+------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`add_separator<class_PopupMenu_add_separator>`  **(** **)**                                                                                                                                                 |
+------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`remove_item<class_PopupMenu_remove_item>`  **(** :ref:`int<class_int>` idx  **)**                                                                                                                          |
+------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`clear<class_PopupMenu_clear>`  **(** **)**                                                                                                                                                                 |
+------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Signals
-------

-  **item_pressed**  **(** :ref:`int<class_int>` ID  **)**

Description
-----------

PopupMenu is the typical Control that displays a list of options. They are popular in toolbars or context menus.

Member Function Description
---------------------------

.. _class_PopupMenu_add_icon_item:

- void  **add_icon_item**  **(** :ref:`Object<class_object>` texture, :ref:`String<class_string>` label, :ref:`int<class_int>` id=-1, :ref:`int<class_int>` accel=0  **)**

Add a new item with text "label" and icon "texture". An id can optionally be provided, as well as an accelerator. If no id is provided, one will be created from the index.

.. _class_PopupMenu_add_item:

- void  **add_item**  **(** :ref:`String<class_string>` label, :ref:`int<class_int>` id=-1, :ref:`int<class_int>` accel=0  **)**

Add a new item with text "label". An id can optionally be provided, as well as an accelerator. If no id is provided, one will be created from the index.

.. _class_PopupMenu_add_icon_check_item:

- void  **add_icon_check_item**  **(** :ref:`Object<class_object>` texture, :ref:`String<class_string>` label, :ref:`int<class_int>` id=-1, :ref:`int<class_int>` accel=0  **)**

Add a new check able item with text "label" and icon "texture". An id can optionally be provided, as well as an accelerator. If no id is provided, one will be created from the index. Note that checkable items just display a checkmark, but don't have any built-in checking behavior and must be checked/unchecked manually.

.. _class_PopupMenu_add_check_item:

- void  **add_check_item**  **(** :ref:`String<class_string>` label, :ref:`int<class_int>` id=-1, :ref:`int<class_int>` accel=0  **)**

Add a new checkable item with text "label". An id can optionally be provided, as well as an accelerator. If no id is provided, one will be created from the index. Note that checkable items just display a checkmark, but don't have any built-in checking behavior and must be checked/unchecked manually.

.. _class_PopupMenu_add_submenu_item:

- void  **add_submenu_item**  **(** :ref:`String<class_string>` label, :ref:`String<class_string>` submenu, :ref:`int<class_int>` id=-1  **)**

.. _class_PopupMenu_set_item_text:

- void  **set_item_text**  **(** :ref:`int<class_int>` idx, :ref:`String<class_string>` text  **)**

Set the text of the item at index "idx".

.. _class_PopupMenu_set_item_icon:

- void  **set_item_icon**  **(** :ref:`int<class_int>` idx, :ref:`Object<class_object>` icon  **)**

Set the icon of the item at index "idx".

.. _class_PopupMenu_set_item_accelerator:

- void  **set_item_accelerator**  **(** :ref:`int<class_int>` idx, :ref:`int<class_int>` accel  **)**

Set the accelerator of the item at index "idx". Accelerators are special combinations of keys that activate the item, no matter which control is focused.

.. _class_PopupMenu_set_item_metadata:

- void  **set_item_metadata**  **(** :ref:`int<class_int>` idx, var metadata  **)**

.. _class_PopupMenu_set_item_checked:

- void  **set_item_checked**  **(** :ref:`int<class_int>` idx, :ref:`bool<class_bool>` checked  **)**

Set the checkstate status of the item at index "idx".

.. _class_PopupMenu_set_item_disabled:

- void  **set_item_disabled**  **(** :ref:`int<class_int>` idx, :ref:`bool<class_bool>` disabled  **)**

.. _class_PopupMenu_set_item_submenu:

- void  **set_item_submenu**  **(** :ref:`int<class_int>` idx, :ref:`String<class_string>` submenu  **)**

.. _class_PopupMenu_set_item_as_separator:

- void  **set_item_as_separator**  **(** :ref:`int<class_int>` idx, :ref:`bool<class_bool>` enable  **)**

.. _class_PopupMenu_set_item_as_checkable:

- void  **set_item_as_checkable**  **(** :ref:`int<class_int>` idx, :ref:`bool<class_bool>` enable  **)**

.. _class_PopupMenu_set_item_ID:

- void  **set_item_ID**  **(** :ref:`int<class_int>` idx, :ref:`int<class_int>` id  **)**

Set the id of the item at index "idx".

.. _class_PopupMenu_get_item_text:

- :ref:`String<class_string>`  **get_item_text**  **(** :ref:`int<class_int>` idx  **)** const

Return the text of the item at index "idx".

.. _class_PopupMenu_get_item_icon:

- :ref:`Object<class_object>`  **get_item_icon**  **(** :ref:`int<class_int>` idx  **)** const

Return the icon of the item at index "idx".

.. _class_PopupMenu_get_item_metadata:

- void  **get_item_metadata**  **(** :ref:`int<class_int>` idx  **)** const

.. _class_PopupMenu_get_item_accelerator:

- :ref:`int<class_int>`  **get_item_accelerator**  **(** :ref:`int<class_int>` idx  **)** const

Return the accelerator of the item at index "idx". Accelerators are special combinations of keys that activate the item, no matter which control is focused.

.. _class_PopupMenu_get_item_submenu:

- :ref:`String<class_string>`  **get_item_submenu**  **(** :ref:`int<class_int>` idx  **)** const

.. _class_PopupMenu_is_item_separator:

- :ref:`bool<class_bool>`  **is_item_separator**  **(** :ref:`int<class_int>` idx  **)** const

.. _class_PopupMenu_is_item_checkable:

- :ref:`bool<class_bool>`  **is_item_checkable**  **(** :ref:`int<class_int>` idx  **)** const

.. _class_PopupMenu_is_item_checked:

- :ref:`bool<class_bool>`  **is_item_checked**  **(** :ref:`int<class_int>` idx  **)** const

Return the checkstate status of the item at index "idx".

.. _class_PopupMenu_is_item_disabled:

- :ref:`bool<class_bool>`  **is_item_disabled**  **(** :ref:`int<class_int>` idx  **)** const

.. _class_PopupMenu_get_item_ID:

- :ref:`int<class_int>`  **get_item_ID**  **(** :ref:`int<class_int>` idx  **)** const

Return the id of the item at index "idx".

.. _class_PopupMenu_get_item_index:

- :ref:`int<class_int>`  **get_item_index**  **(** :ref:`int<class_int>` id  **)** const

Find and return the index of the item containing a given id.

.. _class_PopupMenu_get_item_count:

- :ref:`int<class_int>`  **get_item_count**  **(** **)** const

Return the amount of items.

.. _class_PopupMenu_add_separator:

- void  **add_separator**  **(** **)**

Add a separator between items. Separators also occupy an index.

.. _class_PopupMenu_remove_item:

- void  **remove_item**  **(** :ref:`int<class_int>` idx  **)**

.. _class_PopupMenu_clear:

- void  **clear**  **(** **)**

Clear the popup menu.


