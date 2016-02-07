.. _class_ResourceSaver:

ResourceSaver
=============

**Inherits:** :ref:`Object<class_object>`

**Category:** Core

Brief Description
-----------------

Resource Saving Interface.

Member Functions
----------------

+----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`                  | :ref:`save<class_ResourceSaver_save>`  **(** :ref:`String<class_string>` path, :ref:`Resource<class_resource>` resource, :ref:`int<class_int>` flags=0  **)** |
+----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`StringArray<class_stringarray>`  | :ref:`get_recognized_extensions<class_ResourceSaver_get_recognized_extensions>`  **(** :ref:`Object<class_object>` type  **)**                                |
+----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

Numeric Constants
-----------------

- **FLAG_RELATIVE_PATHS** = **1**
- **FLAG_BUNDLE_RESOURCES** = **2**
- **FLAG_CHANGE_PATH** = **4**
- **FLAG_OMIT_EDITOR_PROPERTIES** = **8**
- **FLAG_SAVE_BIG_ENDIAN** = **16**
- **FLAG_COMPRESS** = **32**

Description
-----------

Resource Saving Interface. This interface is used for saving resources to disk.

Member Function Description
---------------------------

.. _class_ResourceSaver_save:

- :ref:`int<class_int>`  **save**  **(** :ref:`String<class_string>` path, :ref:`Resource<class_resource>` resource, :ref:`int<class_int>` flags=0  **)**

Save a resource to disk, to a given path.

.. _class_ResourceSaver_get_recognized_extensions:

- :ref:`StringArray<class_stringarray>`  **get_recognized_extensions**  **(** :ref:`Object<class_object>` type  **)**

Return the list of extensions available for saving a resource of a given type.


