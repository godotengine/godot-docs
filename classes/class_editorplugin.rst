.. _class_EditorPlugin:

EditorPlugin
============

**Inherits:** :ref:`Node<class_node>`

**Category:** Core



Member Functions
----------------

+----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                   | :ref:`apply_changes<class_EditorPlugin_apply_changes>`  **(** **)** virtual                                                                                                                                         |
+----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                   | :ref:`clear<class_EditorPlugin_clear>`  **(** **)** virtual                                                                                                                                                         |
+----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                   | :ref:`edit<class_EditorPlugin_edit>`  **(** :ref:`Object<class_object>` object  **)** virtual                                                                                                                       |
+----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`                | :ref:`forward_input_event<class_EditorPlugin_forward_input_event>`  **(** :ref:`InputEvent<class_inputevent>` event  **)** virtual                                                                                  |
+----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`                | :ref:`forward_spatial_input_event<class_EditorPlugin_forward_spatial_input_event>`  **(** :ref:`Camera<class_camera>` camera, :ref:`InputEvent<class_inputevent>` event  **)** virtual                              |
+----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`StringArray<class_stringarray>`  | :ref:`get_breakpoints<class_EditorPlugin_get_breakpoints>`  **(** **)** virtual                                                                                                                                     |
+----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`String<class_string>`            | :ref:`get_name<class_EditorPlugin_get_name>`  **(** **)** virtual                                                                                                                                                   |
+----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Dictionary<class_dictionary>`    | :ref:`get_state<class_EditorPlugin_get_state>`  **(** **)** virtual                                                                                                                                                 |
+----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`                | :ref:`handles<class_EditorPlugin_handles>`  **(** :ref:`Object<class_object>` object  **)** virtual                                                                                                                 |
+----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`                | :ref:`has_main_screen<class_EditorPlugin_has_main_screen>`  **(** **)** virtual                                                                                                                                     |
+----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                   | :ref:`make_visible<class_EditorPlugin_make_visible>`  **(** :ref:`bool<class_bool>` visible  **)** virtual                                                                                                          |
+----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                   | :ref:`set_state<class_EditorPlugin_set_state>`  **(** :ref:`Dictionary<class_dictionary>` state  **)** virtual                                                                                                      |
+----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Object<class_object>`            | :ref:`get_undo_redo<class_EditorPlugin_get_undo_redo>`  **(** **)**                                                                                                                                                 |
+----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                   | :ref:`add_custom_control<class_EditorPlugin_add_custom_control>`  **(** :ref:`int<class_int>` container, :ref:`Object<class_object>` control  **)**                                                                 |
+----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                   | :ref:`add_custom_type<class_EditorPlugin_add_custom_type>`  **(** :ref:`String<class_string>` type, :ref:`String<class_string>` base, :ref:`Script<class_script>` script, :ref:`Texture<class_texture>` icon  **)** |
+----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                   | :ref:`remove_custom_type<class_EditorPlugin_remove_custom_type>`  **(** :ref:`String<class_string>` type  **)**                                                                                                     |
+----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Numeric Constants
-----------------

- **CONTAINER_TOOLBAR** = **0**
- **CONTAINER_SPATIAL_EDITOR_MENU** = **1**
- **CONTAINER_SPATIAL_EDITOR_SIDE** = **2**
- **CONTAINER_SPATIAL_EDITOR_BOTTOM** = **3**
- **CONTAINER_CANVAS_EDITOR_MENU** = **4**
- **CONTAINER_CANVAS_EDITOR_SIDE** = **5**

Member Function Description
---------------------------

.. _class_EditorPlugin_apply_changes:

- void  **apply_changes**  **(** **)** virtual

.. _class_EditorPlugin_clear:

- void  **clear**  **(** **)** virtual

.. _class_EditorPlugin_edit:

- void  **edit**  **(** :ref:`Object<class_object>` object  **)** virtual

.. _class_EditorPlugin_forward_input_event:

- :ref:`bool<class_bool>`  **forward_input_event**  **(** :ref:`InputEvent<class_inputevent>` event  **)** virtual

.. _class_EditorPlugin_forward_spatial_input_event:

- :ref:`bool<class_bool>`  **forward_spatial_input_event**  **(** :ref:`Camera<class_camera>` camera, :ref:`InputEvent<class_inputevent>` event  **)** virtual

.. _class_EditorPlugin_get_breakpoints:

- :ref:`StringArray<class_stringarray>`  **get_breakpoints**  **(** **)** virtual

.. _class_EditorPlugin_get_name:

- :ref:`String<class_string>`  **get_name**  **(** **)** virtual

.. _class_EditorPlugin_get_state:

- :ref:`Dictionary<class_dictionary>`  **get_state**  **(** **)** virtual

.. _class_EditorPlugin_handles:

- :ref:`bool<class_bool>`  **handles**  **(** :ref:`Object<class_object>` object  **)** virtual

.. _class_EditorPlugin_has_main_screen:

- :ref:`bool<class_bool>`  **has_main_screen**  **(** **)** virtual

.. _class_EditorPlugin_make_visible:

- void  **make_visible**  **(** :ref:`bool<class_bool>` visible  **)** virtual

.. _class_EditorPlugin_set_state:

- void  **set_state**  **(** :ref:`Dictionary<class_dictionary>` state  **)** virtual

.. _class_EditorPlugin_get_undo_redo:

- :ref:`Object<class_object>`  **get_undo_redo**  **(** **)**

.. _class_EditorPlugin_add_custom_control:

- void  **add_custom_control**  **(** :ref:`int<class_int>` container, :ref:`Object<class_object>` control  **)**

.. _class_EditorPlugin_add_custom_type:

- void  **add_custom_type**  **(** :ref:`String<class_string>` type, :ref:`String<class_string>` base, :ref:`Script<class_script>` script, :ref:`Texture<class_texture>` icon  **)**

.. _class_EditorPlugin_remove_custom_type:

- void  **remove_custom_type**  **(** :ref:`String<class_string>` type  **)**


