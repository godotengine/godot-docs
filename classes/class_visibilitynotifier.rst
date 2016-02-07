.. _class_VisibilityNotifier:

VisibilityNotifier
==================

Inherits: :ref:`Spatial<class_spatial>`
---------------------------------------

Category: Core
--------------

Brief Description
-----------------



Member Functions
----------------

+--------------------------+-----------------------------------------------------------------------------------------------+
| void                     | :ref:`set_aabb<class_VisibilityNotifier_set_aabb>`  **(** :ref:`AABB<class_aabb>` rect  **)** |
+--------------------------+-----------------------------------------------------------------------------------------------+
| :ref:`AABB<class_aabb>`  | :ref:`get_aabb<class_VisibilityNotifier_get_aabb>`  **(** **)** const                         |
+--------------------------+-----------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`  | :ref:`is_on_screen<class_VisibilityNotifier_is_on_screen>`  **(** **)** const                 |
+--------------------------+-----------------------------------------------------------------------------------------------+

Signals
-------

-  **enter_screen**  **(** **)**
-  **enter_camera**  **(** :ref:`Object<class_object>` camera  **)**
-  **exit_screen**  **(** **)**
-  **exit_camera**  **(** :ref:`Object<class_object>` camera  **)**

Member Function Description
---------------------------

.. _class_VisibilityNotifier_set_aabb:

- void  **set_aabb**  **(** :ref:`AABB<class_aabb>` rect  **)**

.. _class_VisibilityNotifier_get_aabb:

- :ref:`AABB<class_aabb>`  **get_aabb**  **(** **)** const

.. _class_VisibilityNotifier_is_on_screen:

- :ref:`bool<class_bool>`  **is_on_screen**  **(** **)** const


