.. _class_ColorArray:

ColorArray
==========

Category: Built-In Types
------------------------

Brief Description
-----------------

Array of Colors

Member Functions
----------------

+--------------------------------------+-----------------------------------------------------------------------------------------------------------+
| void                                 | :ref:`push_back<class_ColorArray_push_back>`  **(** :ref:`Color<class_color>` color  **)**                |
+--------------------------------------+-----------------------------------------------------------------------------------------------------------+
| void                                 | :ref:`resize<class_ColorArray_resize>`  **(** :ref:`int<class_int>` idx  **)**                            |
+--------------------------------------+-----------------------------------------------------------------------------------------------------------+
| void                                 | :ref:`set<class_ColorArray_set>`  **(** :ref:`int<class_int>` idx, :ref:`Color<class_color>` color  **)** |
+--------------------------------------+-----------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`                | :ref:`size<class_ColorArray_size>`  **(** **)**                                                           |
+--------------------------------------+-----------------------------------------------------------------------------------------------------------+
| :ref:`ColorArray<class_colorarray>`  | :ref:`ColorArray<class_ColorArray_ColorArray>`  **(** :ref:`Array<class_array>` from  **)**               |
+--------------------------------------+-----------------------------------------------------------------------------------------------------------+

Description
-----------

Array of Color, can only contains colors. Optimized for memory usage, can't fragment the memory.

Member Function Description
---------------------------

.. _class_ColorArray_push_back:

- void  **push_back**  **(** :ref:`Color<class_color>` color  **)**

Append a value to the array.

.. _class_ColorArray_resize:

- void  **resize**  **(** :ref:`int<class_int>` idx  **)**

Resize the array.

.. _class_ColorArray_set:

- void  **set**  **(** :ref:`int<class_int>` idx, :ref:`Color<class_color>` color  **)**

Set an index in the array.

.. _class_ColorArray_size:

- :ref:`int<class_int>`  **size**  **(** **)**

Return the array size.

.. _class_ColorArray_ColorArray:

- :ref:`ColorArray<class_colorarray>`  **ColorArray**  **(** :ref:`Array<class_array>` from  **)**

Create from a generic array.


