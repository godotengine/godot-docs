.. _class_Reference:

Reference
=========

Inherits: :ref:`Object<class_object>`
-------------------------------------

Category: Core
--------------

Brief Description
-----------------

Base class for anything that keeps a reference count.

Member Functions
----------------

+--------------------------+--------------------------------------------------------------+
| :ref:`bool<class_bool>`  | :ref:`init_ref<class_Reference_init_ref>`  **(** **)**       |
+--------------------------+--------------------------------------------------------------+
| void                     | :ref:`reference<class_Reference_reference>`  **(** **)**     |
+--------------------------+--------------------------------------------------------------+
| :ref:`bool<class_bool>`  | :ref:`unreference<class_Reference_unreference>`  **(** **)** |
+--------------------------+--------------------------------------------------------------+

Description
-----------

Base class for anything that keeps a reference count. Resource and many other helper objects inherit this. References keep an internal reference counter so they are only released when no longer in use.

Member Function Description
---------------------------

.. _class_Reference_init_ref:

- :ref:`bool<class_bool>`  **init_ref**  **(** **)**

.. _class_Reference_reference:

- void  **reference**  **(** **)**

Increase the internal reference counter. Use this only if you really know what you are doing.

.. _class_Reference_unreference:

- :ref:`bool<class_bool>`  **unreference**  **(** **)**

Decrease the internal reference counter. Use this only if you really know what you are doing.


