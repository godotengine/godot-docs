.. _class_InputEventJoystickMotion:

InputEventJoystickMotion
========================

**Category:** Built-In Types

Brief Description
-----------------



Member Functions
----------------

+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`  | :ref:`is_action<class_InputEventJoystickMotion_is_action>`  **(** :ref:`String<class_string>` action  **)**                                          |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`  | :ref:`is_action_pressed<class_InputEventJoystickMotion_is_action_pressed>`  **(** :ref:`String<class_string>` is_action_pressed  **)**               |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`  | :ref:`is_action_released<class_InputEventJoystickMotion_is_action_released>`  **(** :ref:`String<class_string>` is_action_released  **)**            |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`  | :ref:`is_echo<class_InputEventJoystickMotion_is_echo>`  **(** **)**                                                                                  |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`  | :ref:`is_pressed<class_InputEventJoystickMotion_is_pressed>`  **(** **)**                                                                            |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                     | :ref:`set_as_action<class_InputEventJoystickMotion_set_as_action>`  **(** :ref:`String<class_string>` action, :ref:`bool<class_bool>` pressed  **)** |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+

Member Variables
----------------

- :ref:`int<class_int>` **type**
- :ref:`int<class_int>` **device**
- :ref:`int<class_int>` **ID**
- :ref:`int<class_int>` **axis**
- :ref:`float<class_float>` **value**

Numeric Constants
-----------------

- **NONE** = **0**
- **KEY** = **1**
- **MOUSE_MOTION** = **2**
- **MOUSE_BUTTON** = **3**
- **JOYSTICK_MOTION** = **4**
- **JOYSTICK_BUTTON** = **5**
- **SCREEN_TOUCH** = **6**
- **SCREEN_DRAG** = **7**
- **ACTION** = **8**

Member Function Description
---------------------------

.. _class_InputEventJoystickMotion_is_action:

- :ref:`bool<class_bool>`  **is_action**  **(** :ref:`String<class_string>` action  **)**

.. _class_InputEventJoystickMotion_is_action_pressed:

- :ref:`bool<class_bool>`  **is_action_pressed**  **(** :ref:`String<class_string>` is_action_pressed  **)**

.. _class_InputEventJoystickMotion_is_action_released:

- :ref:`bool<class_bool>`  **is_action_released**  **(** :ref:`String<class_string>` is_action_released  **)**

.. _class_InputEventJoystickMotion_is_echo:

- :ref:`bool<class_bool>`  **is_echo**  **(** **)**

.. _class_InputEventJoystickMotion_is_pressed:

- :ref:`bool<class_bool>`  **is_pressed**  **(** **)**

.. _class_InputEventJoystickMotion_set_as_action:

- void  **set_as_action**  **(** :ref:`String<class_string>` action, :ref:`bool<class_bool>` pressed  **)**


