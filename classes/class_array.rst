.. _class_Array:

Array
=====

**Category:** Built-In Types

Brief Description
-----------------

Generic array datatype.

Member Functions
----------------

+----------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| void                       | :ref:`append<class_Array_append>`  **(** var value  **)**                                                                   |
+----------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| void                       | :ref:`clear<class_Array_clear>`  **(** **)**                                                                                |
+----------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`    | :ref:`empty<class_Array_empty>`  **(** **)**                                                                                |
+----------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| void                       | :ref:`erase<class_Array_erase>`  **(** var value  **)**                                                                     |
+----------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`      | :ref:`find<class_Array_find>`  **(** var value  **)**                                                                       |
+----------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`      | :ref:`hash<class_Array_hash>`  **(** **)**                                                                                  |
+----------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| void                       | :ref:`insert<class_Array_insert>`  **(** :ref:`int<class_int>` pos, var value  **)**                                        |
+----------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| void                       | :ref:`invert<class_Array_invert>`  **(** **)**                                                                              |
+----------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`    | :ref:`is_shared<class_Array_is_shared>`  **(** **)**                                                                        |
+----------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| void                       | :ref:`pop_back<class_Array_pop_back>`  **(** **)**                                                                          |
+----------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| void                       | :ref:`pop_front<class_Array_pop_front>`  **(** **)**                                                                        |
+----------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| void                       | :ref:`push_back<class_Array_push_back>`  **(** var value  **)**                                                             |
+----------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| void                       | :ref:`push_front<class_Array_push_front>`  **(** var value  **)**                                                           |
+----------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| void                       | :ref:`remove<class_Array_remove>`  **(** :ref:`int<class_int>` pos  **)**                                                   |
+----------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| void                       | :ref:`resize<class_Array_resize>`  **(** :ref:`int<class_int>` pos  **)**                                                   |
+----------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`      | :ref:`size<class_Array_size>`  **(** **)**                                                                                  |
+----------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| void                       | :ref:`sort<class_Array_sort>`  **(** **)**                                                                                  |
+----------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| void                       | :ref:`sort_custom<class_Array_sort_custom>`  **(** :ref:`Object<class_object>` obj, :ref:`String<class_string>` func  **)** |
+----------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| :ref:`Array<class_array>`  | :ref:`Array<class_Array_Array>`  **(** :ref:`RawArray<class_rawarray>` from  **)**                                          |
+----------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| :ref:`Array<class_array>`  | :ref:`Array<class_Array_Array>`  **(** :ref:`IntArray<class_intarray>` from  **)**                                          |
+----------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| :ref:`Array<class_array>`  | :ref:`Array<class_Array_Array>`  **(** :ref:`RealArray<class_realarray>` from  **)**                                        |
+----------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| :ref:`Array<class_array>`  | :ref:`Array<class_Array_Array>`  **(** :ref:`StringArray<class_stringarray>` from  **)**                                    |
+----------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| :ref:`Array<class_array>`  | :ref:`Array<class_Array_Array>`  **(** :ref:`Vector2Array<class_vector2array>` from  **)**                                  |
+----------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| :ref:`Array<class_array>`  | :ref:`Array<class_Array_Array>`  **(** :ref:`Vector3Array<class_vector3array>` from  **)**                                  |
+----------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| :ref:`Array<class_array>`  | :ref:`Array<class_Array_Array>`  **(** :ref:`ColorArray<class_colorarray>` from  **)**                                      |
+----------------------------+-----------------------------------------------------------------------------------------------------------------------------+

Description
-----------

Generic array, contains several elements of any type, accessible by numerical index starting at 0. Arrays are always passed by reference.

Member Function Description
---------------------------

.. _class_Array_append:

- void  **append**  **(** var value  **)**

Append an element at the end of the array (alias of :ref:`push_back<class_Array_push_back>`).

.. _class_Array_clear:

- void  **clear**  **(** **)**

Clear the array (resize to 0).

.. _class_Array_empty:

- :ref:`bool<class_bool>`  **empty**  **(** **)**

Return true if the array is empty (size==0).

.. _class_Array_erase:

- void  **erase**  **(** var value  **)**

Remove the first occurrence of a value from the array.

.. _class_Array_find:

- :ref:`int<class_int>`  **find**  **(** var value  **)**

Searches the array for a value and returns its index or -1 if not found.

.. _class_Array_hash:

- :ref:`int<class_int>`  **hash**  **(** **)**

Return a hashed integer value representing the array contents.

.. _class_Array_insert:

- void  **insert**  **(** :ref:`int<class_int>` pos, var value  **)**

Insert a new element at a given position in the array. The position must be valid, or at the end of the array (pos==size()).

.. _class_Array_invert:

- void  **invert**  **(** **)**

Reverse the order of the elements in the array (so first element will now be the last).

.. _class_Array_is_shared:

- :ref:`bool<class_bool>`  **is_shared**  **(** **)**

Get whether this is a shared array instance.

.. _class_Array_pop_back:

- void  **pop_back**  **(** **)**

.. _class_Array_pop_front:

- void  **pop_front**  **(** **)**

.. _class_Array_push_back:

- void  **push_back**  **(** var value  **)**

Append an element at the end of the array.

.. _class_Array_push_front:

- void  **push_front**  **(** var value  **)**

.. _class_Array_remove:

- void  **remove**  **(** :ref:`int<class_int>` pos  **)**

Remove an element from the array by index.

.. _class_Array_resize:

- void  **resize**  **(** :ref:`int<class_int>` pos  **)**

Resize the array to contain a different number of elements. If the array size is smaller, elements are cleared, if bigger, new elements are Null.

.. _class_Array_size:

- :ref:`int<class_int>`  **size**  **(** **)**

Return the amount of elements in the array.

.. _class_Array_sort:

- void  **sort**  **(** **)**

Sort the array using natural order.

.. _class_Array_sort_custom:

- void  **sort_custom**  **(** :ref:`Object<class_object>` obj, :ref:`String<class_string>` func  **)**

Sort the array using a custom method. The arguments are an object that holds the method and the name of such method. The custom method receives two arguments (a pair of elements from the array) and must return true if the first argument is less than the second, and return false otherwise.

.. _class_Array_Array:

- :ref:`Array<class_array>`  **Array**  **(** :ref:`RawArray<class_rawarray>` from  **)**

Construct an array from a :ref:`RawArray<class_rawarray>`.

.. _class_Array_Array:

- :ref:`Array<class_array>`  **Array**  **(** :ref:`IntArray<class_intarray>` from  **)**

Construct an array from a :ref:`RawArray<class_rawarray>`.

.. _class_Array_Array:

- :ref:`Array<class_array>`  **Array**  **(** :ref:`RealArray<class_realarray>` from  **)**

Construct an array from a :ref:`RawArray<class_rawarray>`.

.. _class_Array_Array:

- :ref:`Array<class_array>`  **Array**  **(** :ref:`StringArray<class_stringarray>` from  **)**

Construct an array from a :ref:`RawArray<class_rawarray>`.

.. _class_Array_Array:

- :ref:`Array<class_array>`  **Array**  **(** :ref:`Vector2Array<class_vector2array>` from  **)**

Construct an array from a :ref:`RawArray<class_rawarray>`.

.. _class_Array_Array:

- :ref:`Array<class_array>`  **Array**  **(** :ref:`Vector3Array<class_vector3array>` from  **)**

Construct an array from a :ref:`RawArray<class_rawarray>`.

.. _class_Array_Array:

- :ref:`Array<class_array>`  **Array**  **(** :ref:`ColorArray<class_colorarray>` from  **)**

Construct an array from a :ref:`RawArray<class_rawarray>`.


