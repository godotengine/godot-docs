.. _class_Translation:

Translation
===========

**Inherits:** :ref:`Resource<class_resource>`

**Category:** Core

Language Translation.

Member Functions
----------------

+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                   | :ref:`set_locale<class_Translation_set_locale>`  **(** :ref:`String<class_string>` locale  **)**                                                    |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`String<class_string>`            | :ref:`get_locale<class_Translation_get_locale>`  **(** **)** const                                                                                  |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                   | :ref:`add_message<class_Translation_add_message>`  **(** :ref:`String<class_string>` src_message, :ref:`String<class_string>` xlated_message  **)** |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`String<class_string>`            | :ref:`get_message<class_Translation_get_message>`  **(** :ref:`String<class_string>` src_message  **)** const                                       |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                   | :ref:`erase_message<class_Translation_erase_message>`  **(** :ref:`String<class_string>` src_message  **)**                                         |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`StringArray<class_stringarray>`  | :ref:`get_message_list<class_Translation_get_message_list>`  **(** **)** const                                                                      |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`                  | :ref:`get_message_count<class_Translation_get_message_count>`  **(** **)** const                                                                    |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+

Description
-----------

Translations are resources that can be loaded/unloaded on demand. They map a string to another string.

Member Function Description
---------------------------

.. _class_Translation_set_locale:

- void  **set_locale**  **(** :ref:`String<class_string>` locale  **)**

Set the locale of the translation.

.. _class_Translation_get_locale:

- :ref:`String<class_string>`  **get_locale**  **(** **)** const

Return the locale of the translation.

.. _class_Translation_add_message:

- void  **add_message**  **(** :ref:`String<class_string>` src_message, :ref:`String<class_string>` xlated_message  **)**

Add a message for translation.

.. _class_Translation_get_message:

- :ref:`String<class_string>`  **get_message**  **(** :ref:`String<class_string>` src_message  **)** const

Return a message for translation.

.. _class_Translation_erase_message:

- void  **erase_message**  **(** :ref:`String<class_string>` src_message  **)**

Erase a message.

.. _class_Translation_get_message_list:

- :ref:`StringArray<class_stringarray>`  **get_message_list**  **(** **)** const

Return all the messages (keys).

.. _class_Translation_get_message_count:

- :ref:`int<class_int>`  **get_message_count**  **(** **)** const


