.. _class_Resource:

Resource
========

Inherits: :ref:`Reference<class_reference>`
-------------------------------------------

Category: Core
--------------

Brief Description
-----------------

Base class for all resources.

Member Functions
----------------

+------------------------------+-------------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`set_path<class_Resource_set_path>`  **(** :ref:`String<class_string>` path  **)**                           |
+------------------------------+-------------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`take_over_path<class_Resource_take_over_path>`  **(** :ref:`String<class_string>` path  **)**               |
+------------------------------+-------------------------------------------------------------------------------------------------------------------+
| :ref:`String<class_string>`  | :ref:`get_path<class_Resource_get_path>`  **(** **)** const                                                       |
+------------------------------+-------------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`set_name<class_Resource_set_name>`  **(** :ref:`String<class_string>` name  **)**                           |
+------------------------------+-------------------------------------------------------------------------------------------------------------------+
| :ref:`String<class_string>`  | :ref:`get_name<class_Resource_get_name>`  **(** **)** const                                                       |
+------------------------------+-------------------------------------------------------------------------------------------------------------------+
| :ref:`RID<class_rid>`        | :ref:`get_rid<class_Resource_get_rid>`  **(** **)** const                                                         |
+------------------------------+-------------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`set_import_metadata<class_Resource_set_import_metadata>`  **(** :ref:`Object<class_object>` metadata  **)** |
+------------------------------+-------------------------------------------------------------------------------------------------------------------+
| :ref:`Object<class_object>`  | :ref:`get_import_metadata<class_Resource_get_import_metadata>`  **(** **)** const                                 |
+------------------------------+-------------------------------------------------------------------------------------------------------------------+
| :ref:`Object<class_object>`  | :ref:`duplicate<class_Resource_duplicate>`  **(** :ref:`bool<class_bool>` subresources=false  **)**               |
+------------------------------+-------------------------------------------------------------------------------------------------------------------+

Signals
-------

-  **changed**  **(** **)**

Description
-----------

Resource is the base class for all resource types. Resources are primarily data containers. They are reference counted and freed when no longer in use. They are also loaded only once from disk, and further attempts to load the resource will return the same reference (all this in contrast to a :ref:`Node<class_node>`, which is not reference counted and can be instanced from disk as many times as desred). Resources can be saved externally on disk or bundled into another object, such as a :ref:`Node<class_node>` or another resource.

Member Function Description
---------------------------

.. _class_Resource_set_path:

- void  **set_path**  **(** :ref:`String<class_string>` path  **)**

Set the path of the resource. This is useful mainly for editors when saving/loading, and shouldn't be changed by anything else.

.. _class_Resource_take_over_path:

- void  **take_over_path**  **(** :ref:`String<class_string>` path  **)**

.. _class_Resource_get_path:

- :ref:`String<class_string>`  **get_path**  **(** **)** const

Return the path of the resource. This is useful mainly for editors when saving/loading, and shouldn't be changed by anything else.

.. _class_Resource_set_name:

- void  **set_name**  **(** :ref:`String<class_string>` name  **)**

Set the name of the resources, any name is valid (it doesn't have to be unique). Name is for descriptive purposes only.

.. _class_Resource_get_name:

- :ref:`String<class_string>`  **get_name**  **(** **)** const

Return the name of the resources, any name is valid (it doesn't have to be unique). Name is for descriptive purposes only.

.. _class_Resource_get_rid:

- :ref:`RID<class_rid>`  **get_rid**  **(** **)** const

Return the RID of the resource (or an empty RID). Many resources (such as :ref:`Texture<class_texture>`, :ref:`Mesh<class_mesh>`, etc) are high level abstractions of resources stored in a server, so this function will return the original RID.

.. _class_Resource_set_import_metadata:

- void  **set_import_metadata**  **(** :ref:`Object<class_object>` metadata  **)**

.. _class_Resource_get_import_metadata:

- :ref:`Object<class_object>`  **get_import_metadata**  **(** **)** const

.. _class_Resource_duplicate:

- :ref:`Object<class_object>`  **duplicate**  **(** :ref:`bool<class_bool>` subresources=false  **)**


