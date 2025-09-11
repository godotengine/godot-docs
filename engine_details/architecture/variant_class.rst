.. _doc_variant_class:

Variant class
=============

About
-----

Variant is the most important datatype in Godot. A Variant takes up only 24
bytes on 64-bit platforms (20 bytes on 32-bit platforms) and can store almost
any engine datatype inside of it. Variants are rarely used to hold information
for long periods of time, instead they are used mainly for communication,
editing, serialization and generally moving data around.

A Variant can:

-  Store almost any datatype.
-  Perform operations between many variants (GDScript uses Variant as
   its atomic/native datatype).
-  Be hashed, so it can be compared quickly to other variants.
-  Be used to convert safely between datatypes.
-  Be used to abstract calling methods and their arguments (Godot
   exports all its functions through variants).
-  Be used to defer calls or move data between threads.
-  Be serialized as binary and stored to disk, or transferred via
   network.
-  Be serialized to text and use it for printing values and editable
   settings.
-  Work as an exported property, so the editor can edit it universally.
-  Be used for dictionaries, arrays, parsers, etc.

Basically, thanks to the Variant class, writing Godot itself was a much,
much easier task, as it allows for highly dynamic constructs not common
of C++ with little effort. Become a friend of Variant today.

.. note::

    All types within Variant except Nil and Object **cannot** be ``null`` and
    must always store a valid value. These types within Variant are therefore
    called *non-nullable* types.

    One of the Variant types is *Nil* which can only store the value ``null``.
    Therefore, it is possible for a Variant to contain the value ``null``, even
    though all Variant types excluding Nil and Object are non-nullable.

References
~~~~~~~~~~

-  `core/variant/variant.h <https://github.com/godotengine/godot/blob/master/core/variant/variant.h>`__

List of variant types
---------------------

These types are available in Variant:

+---------------------------------+---------------------------+
| Type                            | Notes                     |
+=================================+===========================+
| Nil (can only store ``null``)   | Nullable type             |
+---------------------------------+---------------------------+
| :ref:`class_bool`               |                           |
+---------------------------------+---------------------------+
| :ref:`class_int`                |                           |
+---------------------------------+---------------------------+
| :ref:`class_float`              |                           |
+---------------------------------+---------------------------+
| :ref:`class_string`             |                           |
+---------------------------------+---------------------------+
| :ref:`class_vector2`            |                           |
+---------------------------------+---------------------------+
| :ref:`class_vector2i`           |                           |
+---------------------------------+---------------------------+
| :ref:`class_rect2`              | 2D counterpart of AABB    |
+---------------------------------+---------------------------+
| :ref:`class_rect2i`             |                           |
+---------------------------------+---------------------------+
| :ref:`class_vector3`            |                           |
+---------------------------------+---------------------------+
| :ref:`class_vector3i`           |                           |
+---------------------------------+---------------------------+
| :ref:`class_transform2d`        |                           |
+---------------------------------+---------------------------+
| :ref:`class_vector4`            |                           |
+---------------------------------+---------------------------+
| :ref:`class_vector4i`           |                           |
+---------------------------------+---------------------------+
| :ref:`class_plane`              |                           |
+---------------------------------+---------------------------+
| :ref:`class_quaternion`         |                           |
+---------------------------------+---------------------------+
| :ref:`class_aabb`               | 3D counterpart of Rect2   |
+---------------------------------+---------------------------+
| :ref:`class_basis`              |                           |
+---------------------------------+---------------------------+
| :ref:`class_transform3d`        |                           |
+---------------------------------+---------------------------+
| :ref:`class_projection`         |                           |
+---------------------------------+---------------------------+
| :ref:`class_color`              |                           |
+---------------------------------+---------------------------+
| :ref:`class_stringname`         |                           |
+---------------------------------+---------------------------+
| :ref:`class_nodepath`           |                           |
+---------------------------------+---------------------------+
| :ref:`class_rid`                |                           |
+---------------------------------+---------------------------+
| :ref:`class_object`             | Nullable type             |
+---------------------------------+---------------------------+
| :ref:`class_callable`           |                           |
+---------------------------------+---------------------------+
| :ref:`class_signal`             |                           |
+---------------------------------+---------------------------+
| :ref:`class_dictionary`         |                           |
+---------------------------------+---------------------------+
| :ref:`class_array`              |                           |
+---------------------------------+---------------------------+
| :ref:`class_packedbytearray`    |                           |
+---------------------------------+---------------------------+
| :ref:`class_packedint32array`   |                           |
+---------------------------------+---------------------------+
| :ref:`class_packedint64array`   |                           |
+---------------------------------+---------------------------+
| :ref:`class_packedfloat32array` |                           |
+---------------------------------+---------------------------+
| :ref:`class_packedfloat64array` |                           |
+---------------------------------+---------------------------+
| :ref:`class_packedstringarray`  |                           |
+---------------------------------+---------------------------+
| :ref:`class_packedvector2array` |                           |
+---------------------------------+---------------------------+
| :ref:`class_packedvector3array` |                           |
+---------------------------------+---------------------------+
| :ref:`class_packedcolorarray`   |                           |
+---------------------------------+---------------------------+
| :ref:`class_packedvector4array` |                           |
+---------------------------------+---------------------------+

Containers: Array and Dictionary
--------------------------------

Both :ref:`class_array` and :ref:`class_dictionary` are implemented using
variants. A Dictionary can match any datatype used as key to any other datatype.
An Array just holds an array of Variants. Of course, a Variant can also hold a
Dictionary or an Array inside, making it even more flexible.

Modifications to a container will modify all references to
it. A Mutex should be created to lock it if
:ref:`multi-threaded access <doc_using_multiple_threads>` is desired.

References
~~~~~~~~~~

-  `core/variant/dictionary.h <https://github.com/godotengine/godot/blob/master/core/variant/dictionary.h>`__
-  `core/variant/array.h <https://github.com/godotengine/godot/blob/master/core/variant/array.h>`__
