.. _class_Input:

Input
=====

**Inherits:** :ref:`Object<class_object>`

**Category:** Core



Member Functions
----------------

+--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`        | :ref:`is_key_pressed<class_Input_is_key_pressed>`  **(** :ref:`int<class_int>` scancode  **)**                                                                            |
+--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`        | :ref:`is_mouse_button_pressed<class_Input_is_mouse_button_pressed>`  **(** :ref:`int<class_int>` button  **)**                                                            |
+--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`        | :ref:`is_joy_button_pressed<class_Input_is_joy_button_pressed>`  **(** :ref:`int<class_int>` device, :ref:`int<class_int>` button  **)**                                  |
+--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`        | :ref:`is_action_pressed<class_Input_is_action_pressed>`  **(** :ref:`String<class_string>` action  **)**                                                                  |
+--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`add_joy_mapping<class_Input_add_joy_mapping>`  **(** :ref:`String<class_string>` mapping, :ref:`bool<class_bool>` update_existing=false  **)**                      |
+--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`remove_joy_mapping<class_Input_remove_joy_mapping>`  **(** :ref:`String<class_string>` guid  **)**                                                                  |
+--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`        | :ref:`is_joy_known<class_Input_is_joy_known>`  **(** :ref:`int<class_int>` device  **)**                                                                                  |
+--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`      | :ref:`get_joy_axis<class_Input_get_joy_axis>`  **(** :ref:`int<class_int>` device, :ref:`int<class_int>` axis  **)**                                                      |
+--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`String<class_string>`    | :ref:`get_joy_name<class_Input_get_joy_name>`  **(** :ref:`int<class_int>` device  **)**                                                                                  |
+--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`String<class_string>`    | :ref:`get_joy_guid<class_Input_get_joy_guid>`  **(** :ref:`int<class_int>` device  **)** const                                                                            |
+--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector3<class_vector3>`  | :ref:`get_accelerometer<class_Input_get_accelerometer>`  **(** **)**                                                                                                      |
+--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector2<class_vector2>`  | :ref:`get_mouse_speed<class_Input_get_mouse_speed>`  **(** **)** const                                                                                                    |
+--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`          | :ref:`get_mouse_button_mask<class_Input_get_mouse_button_mask>`  **(** **)** const                                                                                        |
+--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_mouse_mode<class_Input_set_mouse_mode>`  **(** :ref:`int<class_int>` mode  **)**                                                                                |
+--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`          | :ref:`get_mouse_mode<class_Input_get_mouse_mode>`  **(** **)** const                                                                                                      |
+--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`warp_mouse_pos<class_Input_warp_mouse_pos>`  **(** :ref:`Vector2<class_vector2>` to  **)**                                                                          |
+--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`action_press<class_Input_action_press>`  **(** :ref:`String<class_string>` action  **)**                                                                            |
+--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`action_release<class_Input_action_release>`  **(** :ref:`String<class_string>` action  **)**                                                                        |
+--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_custom_mouse_cursor<class_Input_set_custom_mouse_cursor>`  **(** :ref:`Texture<class_texture>` image, :ref:`Vector2<class_vector2>` hotspot=Vector2(0,0)  **)** |
+--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Signals
-------

-  **joy_connection_changed**  **(** :ref:`int<class_int>` index, :ref:`bool<class_bool>` connected  **)**

Numeric Constants
-----------------

- **MOUSE_MODE_VISIBLE** = **0**
- **MOUSE_MODE_HIDDEN** = **1**
- **MOUSE_MODE_CAPTURED** = **2**

Member Function Description
---------------------------

.. _class_Input_is_key_pressed:

- :ref:`bool<class_bool>`  **is_key_pressed**  **(** :ref:`int<class_int>` scancode  **)**

.. _class_Input_is_mouse_button_pressed:

- :ref:`bool<class_bool>`  **is_mouse_button_pressed**  **(** :ref:`int<class_int>` button  **)**

.. _class_Input_is_joy_button_pressed:

- :ref:`bool<class_bool>`  **is_joy_button_pressed**  **(** :ref:`int<class_int>` device, :ref:`int<class_int>` button  **)**

Returns if the joystick button at the given index is currently pressed. (see JOY\_\* constans in :ref:`@Global Scope<class_@global scope>`)

.. _class_Input_is_action_pressed:

- :ref:`bool<class_bool>`  **is_action_pressed**  **(** :ref:`String<class_string>` action  **)**

.. _class_Input_add_joy_mapping:

- void  **add_joy_mapping**  **(** :ref:`String<class_string>` mapping, :ref:`bool<class_bool>` update_existing=false  **)**

Add a new mapping entry (in SDL2 format) to the mapping database. Optionally update already connected devices.

.. _class_Input_remove_joy_mapping:

- void  **remove_joy_mapping**  **(** :ref:`String<class_string>` guid  **)**

Removes all mappings from the internal db that match the given uid.

.. _class_Input_is_joy_known:

- :ref:`bool<class_bool>`  **is_joy_known**  **(** :ref:`int<class_int>` device  **)**

Returns if the specified device is known by the system. This means that it sets all button and axis indices exactly as defined in the JOY\_\* constants (see :ref:`@Global Scope<class_@global scope>`). Unknown joysticks are not expected to match these constants, but you can still retrieve events from them.

.. _class_Input_get_joy_axis:

- :ref:`float<class_float>`  **get_joy_axis**  **(** :ref:`int<class_int>` device, :ref:`int<class_int>` axis  **)**

Returns the current value of the joystick axis at given index (see JOY\_\* constants in :ref:`@Global Scope<class_@global scope>`)

.. _class_Input_get_joy_name:

- :ref:`String<class_string>`  **get_joy_name**  **(** :ref:`int<class_int>` device  **)**

Returns the name of the joystick at the specified device index

.. _class_Input_get_joy_guid:

- :ref:`String<class_string>`  **get_joy_guid**  **(** :ref:`int<class_int>` device  **)** const

Returns a SDL2 compatible device guid on platforms that use gamepad remapping. Returns "Default Gamepad" otherwise.

.. _class_Input_get_accelerometer:

- :ref:`Vector3<class_vector3>`  **get_accelerometer**  **(** **)**

.. _class_Input_get_mouse_speed:

- :ref:`Vector2<class_vector2>`  **get_mouse_speed**  **(** **)** const

.. _class_Input_get_mouse_button_mask:

- :ref:`int<class_int>`  **get_mouse_button_mask**  **(** **)** const

.. _class_Input_set_mouse_mode:

- void  **set_mouse_mode**  **(** :ref:`int<class_int>` mode  **)**

.. _class_Input_get_mouse_mode:

- :ref:`int<class_int>`  **get_mouse_mode**  **(** **)** const

.. _class_Input_warp_mouse_pos:

- void  **warp_mouse_pos**  **(** :ref:`Vector2<class_vector2>` to  **)**

.. _class_Input_action_press:

- void  **action_press**  **(** :ref:`String<class_string>` action  **)**

.. _class_Input_action_release:

- void  **action_release**  **(** :ref:`String<class_string>` action  **)**

.. _class_Input_set_custom_mouse_cursor:

- void  **set_custom_mouse_cursor**  **(** :ref:`Texture<class_texture>` image, :ref:`Vector2<class_vector2>` hotspot=Vector2(0,0)  **)**


