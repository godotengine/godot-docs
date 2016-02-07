.. _class_ResourceLoader:

ResourceLoader
==============

Inherits: :ref:`Object<class_object>`
-------------------------------------

Category: Core
--------------

Brief Description
-----------------

Resource Loader.

Member Functions
----------------

+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`ResourceInteractiveLoader<class_resourceinteractiveloader>`  | :ref:`load_interactive<class_ResourceLoader_load_interactive>`  **(** :ref:`String<class_string>` path, :ref:`String<class_string>` type_hint=""  **)**                   |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Resource<class_resource>`                                    | :ref:`load<class_ResourceLoader_load>`  **(** :ref:`String<class_string>` path, :ref:`String<class_string>` type_hint="", :ref:`bool<class_bool>` p_no_cache=false  **)** |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`StringArray<class_stringarray>`                              | :ref:`get_recognized_extensions_for_type<class_ResourceLoader_get_recognized_extensions_for_type>`  **(** :ref:`String<class_string>` type  **)**                         |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                                               | :ref:`set_abort_on_missing_resources<class_ResourceLoader_set_abort_on_missing_resources>`  **(** :ref:`bool<class_bool>` abort  **)**                                    |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`StringArray<class_stringarray>`                              | :ref:`get_dependencies<class_ResourceLoader_get_dependencies>`  **(** :ref:`String<class_string>` path  **)**                                                             |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`                                            | :ref:`has<class_ResourceLoader_has>`  **(** :ref:`String<class_string>` path  **)**                                                                                       |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Description
-----------

Resource Loader. This is a static object accessible as :ref:`ResourceLoader<class_resourceloader>`. GDScript has a simplified load() function, though.

Member Function Description
---------------------------

.. _class_ResourceLoader_load_interactive:

- :ref:`ResourceInteractiveLoader<class_resourceinteractiveloader>`  **load_interactive**  **(** :ref:`String<class_string>` path, :ref:`String<class_string>` type_hint=""  **)**

Load a resource interactively, the returned object allows to load with high granularity.

.. _class_ResourceLoader_load:

- :ref:`Resource<class_resource>`  **load**  **(** :ref:`String<class_string>` path, :ref:`String<class_string>` type_hint="", :ref:`bool<class_bool>` p_no_cache=false  **)**

.. _class_ResourceLoader_get_recognized_extensions_for_type:

- :ref:`StringArray<class_stringarray>`  **get_recognized_extensions_for_type**  **(** :ref:`String<class_string>` type  **)**

Return the list of recognized extensions for a resource type.

.. _class_ResourceLoader_set_abort_on_missing_resources:

- void  **set_abort_on_missing_resources**  **(** :ref:`bool<class_bool>` abort  **)**

Change the behavior on missing sub-resources. Default is to abort load.

.. _class_ResourceLoader_get_dependencies:

- :ref:`StringArray<class_stringarray>`  **get_dependencies**  **(** :ref:`String<class_string>` path  **)**

.. _class_ResourceLoader_has:

- :ref:`bool<class_bool>`  **has**  **(** :ref:`String<class_string>` path  **)**


