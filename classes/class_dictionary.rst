Dictionary
==========

**Category:** Built-In Types
----------------------------

Brief Description
-----------------

Dictionary type.

Member Functions
----------------

-  void **`clear <#clear>`__** **(** **)**
-  `bool <class_bool>`__ **`empty <#empty>`__** **(** **)**
-  void **`erase <#erase>`__** **(** var value **)**
-  `bool <class_bool>`__ **`has <#has>`__** **(** var value **)**
-  `int <class_int>`__ **`hash <#hash>`__** **(** **)**
-  `Array <class_array>`__ **`keys <#keys>`__** **(** **)**
-  `int <class_int>`__ **`parse\_json <#parse_json>`__** **(**
   `String <class_string>`__ json **)**
-  `int <class_int>`__ **`size <#size>`__** **(** **)**
-  `String <class_string>`__ **`to\_json <#to_json>`__** **(** **)**

Description
-----------

Dictionary type. Associative container which contains values referenced
by unique keys. Dictionaries are always passed by reference.

Member Function Description
---------------------------

clear
~~~~~

-  void **clear** **(** **)**

Clear the dictionary, removing all key/value pairs.

empty
~~~~~

-  `bool <class_bool>`__ **empty** **(** **)**

Return true if the dictionary is empty.

erase
~~~~~

-  void **erase** **(** var value **)**

Erase a dictionary key/value pair by key.

has
~~~

-  `bool <class_bool>`__ **has** **(** var value **)**

Return true if the dictionary has a given key.

hash
~~~~

-  `int <class_int>`__ **hash** **(** **)**

Return a hashed integer value representing the dictionary contents.

keys
~~~~

-  `Array <class_array>`__ **keys** **(** **)**

Return the list of keys in the dictionary.

size
~~~~

-  `int <class_int>`__ **size** **(** **)**

Return the size of the dictionary (in pairs).