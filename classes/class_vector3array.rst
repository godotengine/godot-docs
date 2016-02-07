.. _class_Vector3Array:

Vector3Array
============

Category: Built-In Types
------------------------

Brief Description
-----------------

An Array of Vector3.

Member Functions
----------------

+------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| void                                     | :ref:`push_back<class_Vector3Array_push_back>`  **(** :ref:`Vector3<class_vector3>` vector3  **)**                |
+------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| void                                     | :ref:`resize<class_Vector3Array_resize>`  **(** :ref:`int<class_int>` idx  **)**                                  |
+------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| void                                     | :ref:`set<class_Vector3Array_set>`  **(** :ref:`int<class_int>` idx, :ref:`Vector3<class_vector3>` vector3  **)** |
+------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`                    | :ref:`size<class_Vector3Array_size>`  **(** **)**                                                                 |
+------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector3Array<class_vector3array>`  | :ref:`Vector3Array<class_Vector3Array_Vector3Array>`  **(** :ref:`Array<class_array>` from  **)**                 |
+------------------------------------------+-------------------------------------------------------------------------------------------------------------------+

Description
-----------

An Array specifically designed to hold Vector3.

Member Function Description
---------------------------

.. _class_Vector3Array_push_back:

- void  **push_back**  **(** :ref:`Vector3<class_vector3>` vector3  **)**

Inserts a Vector3 at the end.

.. _class_Vector3Array_resize:

- void  **resize**  **(** :ref:`int<class_int>` idx  **)**

Sets the size of the Vector3Array. If larger than the current size it will reserve some space beforehand, and if it is smaller it will cut off the array.

.. _class_Vector3Array_set:

- void  **set**  **(** :ref:`int<class_int>` idx, :ref:`Vector3<class_vector3>` vector3  **)**

Changes the Vector3 at the given index.

.. _class_Vector3Array_size:

- :ref:`int<class_int>`  **size**  **(** **)**

Returns the size of the array.

.. _class_Vector3Array_Vector3Array:

- :ref:`Vector3Array<class_vector3array>`  **Vector3Array**  **(** :ref:`Array<class_array>` from  **)**

Constructs a new Vector3Array. Optionally, you can pass in an Array that will be converted.


