.. _class_IntArray:

IntArray
========

**Category:** Built-In Types

Brief Description
-----------------

Integer Array.

Member Functions
----------------

+----------------------------------+-------------------------------------------------------------------------------------------------------+
| void                             | :ref:`push_back<class_IntArray_push_back>`  **(** :ref:`int<class_int>` integer  **)**                |
+----------------------------------+-------------------------------------------------------------------------------------------------------+
| void                             | :ref:`resize<class_IntArray_resize>`  **(** :ref:`int<class_int>` idx  **)**                          |
+----------------------------------+-------------------------------------------------------------------------------------------------------+
| void                             | :ref:`set<class_IntArray_set>`  **(** :ref:`int<class_int>` idx, :ref:`int<class_int>` integer  **)** |
+----------------------------------+-------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`            | :ref:`size<class_IntArray_size>`  **(** **)**                                                         |
+----------------------------------+-------------------------------------------------------------------------------------------------------+
| :ref:`IntArray<class_intarray>`  | :ref:`IntArray<class_IntArray_IntArray>`  **(** :ref:`Array<class_array>` from  **)**                 |
+----------------------------------+-------------------------------------------------------------------------------------------------------+

Description
-----------

Integer Array. Array of integers. Can only contain integers. Optimized for memory usage, can't fragment the memory.

Member Function Description
---------------------------

.. _class_IntArray_push_back:

- void  **push_back**  **(** :ref:`int<class_int>` integer  **)**

Append a value to the array.

.. _class_IntArray_resize:

- void  **resize**  **(** :ref:`int<class_int>` idx  **)**

Resize the array.

.. _class_IntArray_set:

- void  **set**  **(** :ref:`int<class_int>` idx, :ref:`int<class_int>` integer  **)**

Set an index in the array.

.. _class_IntArray_size:

- :ref:`int<class_int>`  **size**  **(** **)**

Return the array size.

.. _class_IntArray_IntArray:

- :ref:`IntArray<class_intarray>`  **IntArray**  **(** :ref:`Array<class_array>` from  **)**

Create from a generic array.


