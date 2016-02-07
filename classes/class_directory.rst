.. _class_Directory:

Directory
=========

**Inherits:** :ref:`Reference<class_reference>` **<** :ref:`Object<class_object>`

**Category:** Core

Brief Description
-----------------



Member Functions
----------------

+------------------------------+----------------------------------------------------------------------------------------------------------------------+
| Error                        | :ref:`open<class_Directory_open>`  **(** :ref:`String<class_string>` path  **)**                                     |
+------------------------------+----------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`      | :ref:`list_dir_begin<class_Directory_list_dir_begin>`  **(** **)**                                                   |
+------------------------------+----------------------------------------------------------------------------------------------------------------------+
| :ref:`String<class_string>`  | :ref:`get_next<class_Directory_get_next>`  **(** **)**                                                               |
+------------------------------+----------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`      | :ref:`current_is_dir<class_Directory_current_is_dir>`  **(** **)** const                                             |
+------------------------------+----------------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`list_dir_end<class_Directory_list_dir_end>`  **(** **)**                                                       |
+------------------------------+----------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`        | :ref:`get_drive_count<class_Directory_get_drive_count>`  **(** **)**                                                 |
+------------------------------+----------------------------------------------------------------------------------------------------------------------+
| :ref:`String<class_string>`  | :ref:`get_drive<class_Directory_get_drive>`  **(** :ref:`int<class_int>` idx  **)**                                  |
+------------------------------+----------------------------------------------------------------------------------------------------------------------+
| Error                        | :ref:`change_dir<class_Directory_change_dir>`  **(** :ref:`String<class_string>` todir  **)**                        |
+------------------------------+----------------------------------------------------------------------------------------------------------------------+
| :ref:`String<class_string>`  | :ref:`get_current_dir<class_Directory_get_current_dir>`  **(** **)**                                                 |
+------------------------------+----------------------------------------------------------------------------------------------------------------------+
| Error                        | :ref:`make_dir<class_Directory_make_dir>`  **(** :ref:`String<class_string>` name  **)**                             |
+------------------------------+----------------------------------------------------------------------------------------------------------------------+
| Error                        | :ref:`make_dir_recursive<class_Directory_make_dir_recursive>`  **(** :ref:`String<class_string>` name  **)**         |
+------------------------------+----------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`      | :ref:`file_exists<class_Directory_file_exists>`  **(** :ref:`String<class_string>` name  **)**                       |
+------------------------------+----------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`      | :ref:`dir_exists<class_Directory_dir_exists>`  **(** :ref:`String<class_string>` name  **)**                         |
+------------------------------+----------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`        | :ref:`get_space_left<class_Directory_get_space_left>`  **(** **)**                                                   |
+------------------------------+----------------------------------------------------------------------------------------------------------------------+
| Error                        | :ref:`copy<class_Directory_copy>`  **(** :ref:`String<class_string>` from, :ref:`String<class_string>` to  **)**     |
+------------------------------+----------------------------------------------------------------------------------------------------------------------+
| Error                        | :ref:`rename<class_Directory_rename>`  **(** :ref:`String<class_string>` from, :ref:`String<class_string>` to  **)** |
+------------------------------+----------------------------------------------------------------------------------------------------------------------+
| Error                        | :ref:`remove<class_Directory_remove>`  **(** :ref:`String<class_string>` file  **)**                                 |
+------------------------------+----------------------------------------------------------------------------------------------------------------------+

Member Function Description
---------------------------

.. _class_Directory_open:

- Error  **open**  **(** :ref:`String<class_string>` path  **)**

.. _class_Directory_list_dir_begin:

- :ref:`bool<class_bool>`  **list_dir_begin**  **(** **)**

.. _class_Directory_get_next:

- :ref:`String<class_string>`  **get_next**  **(** **)**

.. _class_Directory_current_is_dir:

- :ref:`bool<class_bool>`  **current_is_dir**  **(** **)** const

.. _class_Directory_list_dir_end:

- void  **list_dir_end**  **(** **)**

.. _class_Directory_get_drive_count:

- :ref:`int<class_int>`  **get_drive_count**  **(** **)**

.. _class_Directory_get_drive:

- :ref:`String<class_string>`  **get_drive**  **(** :ref:`int<class_int>` idx  **)**

.. _class_Directory_change_dir:

- Error  **change_dir**  **(** :ref:`String<class_string>` todir  **)**

.. _class_Directory_get_current_dir:

- :ref:`String<class_string>`  **get_current_dir**  **(** **)**

.. _class_Directory_make_dir:

- Error  **make_dir**  **(** :ref:`String<class_string>` name  **)**

.. _class_Directory_make_dir_recursive:

- Error  **make_dir_recursive**  **(** :ref:`String<class_string>` name  **)**

.. _class_Directory_file_exists:

- :ref:`bool<class_bool>`  **file_exists**  **(** :ref:`String<class_string>` name  **)**

.. _class_Directory_dir_exists:

- :ref:`bool<class_bool>`  **dir_exists**  **(** :ref:`String<class_string>` name  **)**

.. _class_Directory_get_space_left:

- :ref:`int<class_int>`  **get_space_left**  **(** **)**

.. _class_Directory_copy:

- Error  **copy**  **(** :ref:`String<class_string>` from, :ref:`String<class_string>` to  **)**

.. _class_Directory_rename:

- Error  **rename**  **(** :ref:`String<class_string>` from, :ref:`String<class_string>` to  **)**

.. _class_Directory_remove:

- Error  **remove**  **(** :ref:`String<class_string>` file  **)**


