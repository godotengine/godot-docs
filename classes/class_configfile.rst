.. _class_ConfigFile:

ConfigFile
==========

**Inherits:** :ref:`Reference<class_reference>`

**Category:** Core



Member Functions
----------------

+----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                   | :ref:`set_value<class_ConfigFile_set_value>`  **(** :ref:`String<class_string>` section, :ref:`String<class_string>` key, var value  **)**              |
+----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                   | :ref:`get_value<class_ConfigFile_get_value>`  **(** :ref:`String<class_string>` section, :ref:`String<class_string>` key, var default=NULL  **)** const |
+----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`                | :ref:`has_section<class_ConfigFile_has_section>`  **(** :ref:`String<class_string>` section  **)** const                                                |
+----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`                | :ref:`has_section_key<class_ConfigFile_has_section_key>`  **(** :ref:`String<class_string>` section, :ref:`String<class_string>` key  **)** const       |
+----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`StringArray<class_stringarray>`  | :ref:`get_sections<class_ConfigFile_get_sections>`  **(** **)** const                                                                                   |
+----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`StringArray<class_stringarray>`  | :ref:`get_section_keys<class_ConfigFile_get_section_keys>`  **(** :ref:`String<class_string>` section  **)** const                                      |
+----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| Error                                  | :ref:`load<class_ConfigFile_load>`  **(** :ref:`String<class_string>` path  **)**                                                                       |
+----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| Error                                  | :ref:`save<class_ConfigFile_save>`  **(** :ref:`String<class_string>` path  **)**                                                                       |
+----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+

Member Function Description
---------------------------

.. _class_ConfigFile_set_value:

- void  **set_value**  **(** :ref:`String<class_string>` section, :ref:`String<class_string>` key, var value  **)**

.. _class_ConfigFile_get_value:

- void  **get_value**  **(** :ref:`String<class_string>` section, :ref:`String<class_string>` key, var default=NULL  **)** const

.. _class_ConfigFile_has_section:

- :ref:`bool<class_bool>`  **has_section**  **(** :ref:`String<class_string>` section  **)** const

.. _class_ConfigFile_has_section_key:

- :ref:`bool<class_bool>`  **has_section_key**  **(** :ref:`String<class_string>` section, :ref:`String<class_string>` key  **)** const

.. _class_ConfigFile_get_sections:

- :ref:`StringArray<class_stringarray>`  **get_sections**  **(** **)** const

.. _class_ConfigFile_get_section_keys:

- :ref:`StringArray<class_stringarray>`  **get_section_keys**  **(** :ref:`String<class_string>` section  **)** const

.. _class_ConfigFile_load:

- Error  **load**  **(** :ref:`String<class_string>` path  **)**

.. _class_ConfigFile_save:

- Error  **save**  **(** :ref:`String<class_string>` path  **)**


