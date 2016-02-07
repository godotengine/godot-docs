.. _class_InputEventMouseMotion:

InputEventMouseMotion
=====================

**Category:** Built-In Types



Member Functions
----------------

+--------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`  | :ref:`is_action<class_InputEventMouseMotion_is_action>`  **(** :ref:`String<class_string>` action  **)**                                          |
+--------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`  | :ref:`is_action_pressed<class_InputEventMouseMotion_is_action_pressed>`  **(** :ref:`String<class_string>` is_action_pressed  **)**               |
+--------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`  | :ref:`is_action_released<class_InputEventMouseMotion_is_action_released>`  **(** :ref:`String<class_string>` is_action_released  **)**            |
+--------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`  | :ref:`is_echo<class_InputEventMouseMotion_is_echo>`  **(** **)**                                                                                  |
+--------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`  | :ref:`is_pressed<class_InputEventMouseMotion_is_pressed>`  **(** **)**                                                                            |
+--------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| void                     | :ref:`set_as_action<class_InputEventMouseMotion_set_as_action>`  **(** :ref:`String<class_string>` action, :ref:`bool<class_bool>` pressed  **)** |
+--------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+

Member Variables
----------------

- :ref:`int<class_int>` **type**
- :ref:`int<class_int>` **device**
- :ref:`int<class_int>` **ID**
- :ref:`bool<class_bool>` **shift**
- :ref:`bool<class_bool>` **alt**
- :ref:`bool<class_bool>` **control**
- :ref:`bool<class_bool>` **meta**
- :ref:`int<class_int>` **button_mask**
- :ref:`int<class_int>` **x**
- :ref:`int<class_int>` **y**
- :ref:`Vector2<class_vector2>` **pos**
- :ref:`int<class_int>` **global_x**
- :ref:`int<class_int>` **global_y**
- :ref:`Vector2<class_vector2>` **global_pos**
- :ref:`int<class_int>` **relative_x**
- :ref:`int<class_int>` **relative_y**
- :ref:`Vector2<class_vector2>` **relative_pos**
- :ref:`float<class_float>` **speed_x**
- :ref:`float<class_float>` **speed_y**
- :ref:`Vector2<class_vector2>` **speed**

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

.. _class_InputEventMouseMotion_is_action:

- :ref:`bool<class_bool>`  **is_action**  **(** :ref:`String<class_string>` action  **)**

.. _class_InputEventMouseMotion_is_action_pressed:

- :ref:`bool<class_bool>`  **is_action_pressed**  **(** :ref:`String<class_string>` is_action_pressed  **)**

.. _class_InputEventMouseMotion_is_action_released:

- :ref:`bool<class_bool>`  **is_action_released**  **(** :ref:`String<class_string>` is_action_released  **)**

.. _class_InputEventMouseMotion_is_echo:

- :ref:`bool<class_bool>`  **is_echo**  **(** **)**

.. _class_InputEventMouseMotion_is_pressed:

- :ref:`bool<class_bool>`  **is_pressed**  **(** **)**

.. _class_InputEventMouseMotion_set_as_action:

- void  **set_as_action**  **(** :ref:`String<class_string>` action, :ref:`bool<class_bool>` pressed  **)**


