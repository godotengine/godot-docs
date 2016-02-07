.. _class_Vector2Array:

Vector2Array
============

**Category:** Built-In Types

Brief Description
-----------------

An Array of Vector2.

Member Functions
----------------

+------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| void                                     | :ref:`push_back<class_Vector2Array_push_back>`  **(** :ref:`Vector2<class_vector2>` vector2  **)**                |
+------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| void                                     | :ref:`resize<class_Vector2Array_resize>`  **(** :ref:`int<class_int>` idx  **)**                                  |
+------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| void                                     | :ref:`set<class_Vector2Array_set>`  **(** :ref:`int<class_int>` idx, :ref:`Vector2<class_vector2>` vector2  **)** |
+------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`                    | :ref:`size<class_Vector2Array_size>`  **(** **)**                                                                 |
+------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector2Array<class_vector2array>`  | :ref:`Vector2Array<class_Vector2Array_Vector2Array>`  **(** :ref:`Array<class_array>` from  **)**                 |
+------------------------------------------+-------------------------------------------------------------------------------------------------------------------+

Description
-----------

An Array specifically designed to hold Vector2.

Member Function Description
---------------------------

.. _class_Vector2Array_push_back:

- void  **push_back**  **(** :ref:`Vector2<class_vector2>` vector2  **)**

Inserts a Vector2 at the end.

.. _class_Vector2Array_resize:

- void  **resize**  **(** :ref:`int<class_int>` idx  **)**

Sets the size of the Vector2Array. If larger than the current size it will reserve some space beforehand, and if it is smaller it will cut off the array.

.. _class_Vector2Array_set:

- void  **set**  **(** :ref:`int<class_int>` idx, :ref:`Vector2<class_vector2>` vector2  **)**

Changes the Vector2 at the given index.

.. _class_Vector2Array_size:

- :ref:`int<class_int>`  **size**  **(** **)**

Returns the size of the array.

.. _class_Vector2Array_Vector2Array:

- :ref:`Vector2Array<class_vector2array>`  **Vector2Array**  **(** :ref:`Array<class_array>` from  **)**

Constructs a new Vector2Array. Optionally, you can pass in an Array that will be converted.


