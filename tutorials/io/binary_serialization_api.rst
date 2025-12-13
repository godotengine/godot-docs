.. _doc_binary_serialization_api:

Binary serialization API
========================

Introduction
------------

Godot has a serialization API based on Variant. It's used for
converting data types to an array of bytes efficiently. This API is exposed
via the global :ref:`bytes_to_var() <class_@GlobalScope_method_bytes_to_var>`
and :ref:`var_to_bytes() <class_@GlobalScope_method_var_to_bytes>` functions,
but it is also used in the ``get_var`` and ``store_var`` methods of
:ref:`class_FileAccess` as well as the packet APIs for :ref:`class_PacketPeer`.
This format is *not* used for binary scenes and resources.

Full Objects vs Object instance IDs
-----------------------------------

If a variable is serialized with ``full_objects = true``, then any Objects
contained in the variable will be serialized and included in the result. This
is recursive.

If ``full_objects = false``, then only the instance IDs will be serialized for
any Objects contained in the variable.

Packet specification
--------------------

The packet is designed to be always padded to 4 bytes. All values are
little-endian-encoded. All packets have a 4-byte header representing an
integer, specifying the type of data.

The header is structured as follows:

- Byte 0 (bits 0-7): ``Variant::Type``
- Byte 1 (bits 8-15): Unused
- Bytes 2-3 (bits 16-31): Additional data (type-specific flags)

::

    type = header & 0xFF;
    flags = header >> 16;

+-------------+----------------------+
| Value       | Type Description     |
+=============+======================+
| 0  (0x00)   | null                 |
+-------------+----------------------+
| 1  (0x01)   | bool                 |
+-------------+----------------------+
| 2  (0x02)   | int                  |
+-------------+----------------------+
| 3  (0x03)   | float                |
+-------------+----------------------+
| 4  (0x04)   | String               |
+-------------+----------------------+
| 5  (0x05)   | Vector2              |
+-------------+----------------------+
| 6  (0x06)   | Vector2i             |
+-------------+----------------------+
| 7  (0x07)   | Rect2                |
+-------------+----------------------+
| 8  (0x08)   | Rect2i               |
+-------------+----------------------+
| 9  (0x09)   | Vector3              |
+-------------+----------------------+
| 10 (0x0A)   | Vector3i             |
+-------------+----------------------+
| 11 (0x0B)   | Transform2D          |
+-------------+----------------------+
| 12 (0x0C)   | Vector4              |
+-------------+----------------------+
| 13 (0x0D)   | Vector4i             |
+-------------+----------------------+
| 14 (0x0E)   | Plane                |
+-------------+----------------------+
| 15 (0x0F)   | Quaternion           |
+-------------+----------------------+
| 16 (0x10)   | AABB                 |
+-------------+----------------------+
| 17 (0x11)   | Basis                |
+-------------+----------------------+
| 18 (0x12)   | Transform3D          |
+-------------+----------------------+
| 19 (0x13)   | Projection           |
+-------------+----------------------+
| 20 (0x14)   | Color                |
+-------------+----------------------+
| 21 (0x15)   | StringName           |
+-------------+----------------------+
| 22 (0x16)   | NodePath             |
+-------------+----------------------+
| 23 (0x17)   | RID                  |
+-------------+----------------------+
| 24 (0x18)   | Object               |
+-------------+----------------------+
| 25 (0x19)   | Callable             |
+-------------+----------------------+
| 26 (0x1A)   | Signal               |
+-------------+----------------------+
| 27 (0x1B)   | Dictionary           |
+-------------+----------------------+
| 28 (0x1C)   | Array                |
+-------------+----------------------+
| 29 (0x1D)   | PackedByteArray      |
+-------------+----------------------+
| 30 (0x1E)   | PackedInt32Array     |
+-------------+----------------------+
| 31 (0x1F)   | PackedInt64Array     |
+-------------+----------------------+
| 32 (0x20)   | PackedFloat32Array   |
+-------------+----------------------+
| 33 (0x21)   | PackedFloat64Array   |
+-------------+----------------------+
| 34 (0x22)   | PackedStringArray    |
+-------------+----------------------+
| 35 (0x23)   | PackedVector2Array   |
+-------------+----------------------+
| 36 (0x24)   | PackedVector3Array   |
+-------------+----------------------+
| 37 (0x25)   | PackedColorArray     |
+-------------+----------------------+
| 38 (0x26)   | PackedVector4Array   |
+-------------+----------------------+

Header Flags
~~~~~~~~~~~~

The header's upper 16 bits contain type-specific flags:

+--------------------------------------------+---------------------------------------------+
| Flag                                       | Description                                 |
+============================================+=============================================+
| ``ENCODE_FLAG_64 = (1 << 16)``             | Used for int, float, and math types to      |
|                                            | indicate 64-bit (long/double) precision     |
+--------------------------------------------+---------------------------------------------+
| ``ENCODE_FLAG_OBJECT_AS_ID = (1 << 16)``   | Used for Object to indicate serialization   |
|                                            | as an instance ID only                      |
+--------------------------------------------+---------------------------------------------+

.. note::

    For integers and floats used in any of these data types, if the ENCODE_FLAG_64 flag is set
    then the value is serialized as a 64-bit integer or double-precision float respectively.

For typed containers (Array and Dictionary), additional flags indicate the container's type information:

**Array (bits 16-17):**

+--------+----------------------------+
| Value  | Meaning                    |
+========+============================+
| 0b00   | Untyped                    |
+--------+----------------------------+
| 0b01   | Typed with built-in type   |
+--------+----------------------------+
| 0b10   | Typed with class name      |
+--------+----------------------------+
| 0b11   | Typed with script path     |
+--------+----------------------------+

**Dictionary key type (bits 16-17) and value type (bits 18-19):**

Same values as Array.

Following this is the actual packet contents, which varies for each type of
packet. Note that this assumes Godot is compiled with single-precision floats,
which is the default. If Godot was compiled with double-precision floats, the
length of "Float" fields within data structures should be 8, and the offset
should be ``(offset - 4) * 2 + 4``. The "float" type itself always uses double
precision.

.. _nil-section:

0: NIL
~~~~~~~

null - No value is serialized after the header.

1: :ref:`bool<class_bool>`
~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+----------+-----------+---------------------------+
| Offset   | Length   | Type      | Description               |
+==========+==========+===========+===========================+
| 4        | 4        | Integer   | 0 for False, 1 for True   |
+----------+----------+-----------+---------------------------+

2: :ref:`int<class_int>`
~~~~~~~~~~~~~~~~~~~~~~~~

If no flags are set (``flags == 0``), the integer is serialized as a 32-bit integer:

+----------+----------+-----------+-------------------------+
| Offset   | Length   | Type      | Description             |
+==========+==========+===========+=========================+
| 4        | 4        | Integer   | 32-bit signed integer   |
+----------+----------+-----------+-------------------------+

If flag ``ENCODE_FLAG_64`` is set (``flags & 1 == 1``), the integer is serialized as a 64-bit integer:

+----------+----------+-----------+-------------------------+
| Offset   | Length   | Type      | Description             |
+==========+==========+===========+=========================+
| 4        | 8        | Integer   | 64-bit signed integer   |
+----------+----------+-----------+-------------------------+

3: :ref:`float<class_float>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If no flags are set (``flags == 0``), the float is serialized as a 32-bit single-precision float:

+----------+----------+---------+-----------------------------------+
| Offset   | Length   | Type    | Description                       |
+==========+==========+=========+===================================+
| 4        | 4        | Float   | IEEE 754 single-precision float   |
+----------+----------+---------+-----------------------------------+

If flag ``ENCODE_FLAG_64`` is set (``flags & 1 == 1``), the float is serialized as a 64-bit double-precision float:

+----------+----------+---------+-----------------------------------+
| Offset   | Length   | Type    | Description                       |
+==========+==========+=========+===================================+
| 4        | 8        | Float   | IEEE 754 double-precision float   |
+----------+----------+---------+-----------------------------------+

.. _string-section:

4: :ref:`String<class_string>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+----------+-----------+--------------------------------------------+
| Offset   | Length   | Type      | Description                                |
+==========+==========+===========+============================================+
| 4        | 4        | Integer   | String length (in bytes, N)                |
+----------+----------+-----------+--------------------------------------------+
| 8        | N        | Bytes     | UTF-8 encoded string (padded to 4 bytes)   |
+----------+----------+-----------+--------------------------------------------+

5: :ref:`Vector2<class_vector2>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+----------+---------+----------------+
| Offset   | Length   | Type    | Description    |
+==========+==========+=========+================+
| 4        | 4        | Float   | X coordinate   |
+----------+----------+---------+----------------+
| 8        | 4        | Float   | Y coordinate   |
+----------+----------+---------+----------------+

6: :ref:`Vector2i<class_vector2i>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+----------+-----------+----------------+
| Offset   | Length   | Type      | Description    |
+==========+==========+===========+================+
| 4        | 4        | Integer   | X coordinate   |
+----------+----------+-----------+----------------+
| 8        | 4        | Integer   | Y coordinate   |
+----------+----------+-----------+----------------+

7: :ref:`Rect2<class_rect2>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+----------+---------+---------------+
| Offset   | Length   | Type    | Description   |
+==========+==========+=========+===============+
| 4        | 4        | Float   | X position    |
+----------+----------+---------+---------------+
| 8        | 4        | Float   | Y position    |
+----------+----------+---------+---------------+
| 12       | 4        | Float   | X size        |
+----------+----------+---------+---------------+
| 16       | 4        | Float   | Y size        |
+----------+----------+---------+---------------+

8: :ref:`Rect2i<class_rect2i>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+----------+-----------+---------------+
| Offset   | Length   | Type      | Description   |
+==========+==========+===========+===============+
| 4        | 4        | Integer   | X position    |
+----------+----------+-----------+---------------+
| 8        | 4        | Integer   | Y position    |
+----------+----------+-----------+---------------+
| 12       | 4        | Integer   | X size        |
+----------+----------+-----------+---------------+
| 16       | 4        | Integer   | Y size        |
+----------+----------+-----------+---------------+

9: :ref:`Vector3<class_vector3>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+----------+---------+----------------+
| Offset   | Length   | Type    | Description    |
+==========+==========+=========+================+
| 4        | 4        | Float   | X coordinate   |
+----------+----------+---------+----------------+
| 8        | 4        | Float   | Y coordinate   |
+----------+----------+---------+----------------+
| 12       | 4        | Float   | Z coordinate   |
+----------+----------+---------+----------------+

10: :ref:`Vector3i<class_vector3i>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+----------+-----------+----------------+
| Offset   | Length   | Type      | Description    |
+==========+==========+===========+================+
| 4        | 4        | Integer   | X coordinate   |
+----------+----------+-----------+----------------+
| 8        | 4        | Integer   | Y coordinate   |
+----------+----------+-----------+----------------+
| 12       | 4        | Integer   | Z coordinate   |
+----------+----------+-----------+----------------+

11: :ref:`Transform2D<class_transform2d>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+----------+---------+-----------------------------------------+
| Offset   | Length   | Type    | Description                             |
+==========+==========+=========+=========================================+
| 4        | 4        | Float   | The X component of the X Vector2        |
+----------+----------+---------+-----------------------------------------+
| 8        | 4        | Float   | The Y component of the X Vector2        |
+----------+----------+---------+-----------------------------------------+
| 12       | 4        | Float   | The X component of the Y Vector2        |
+----------+----------+---------+-----------------------------------------+
| 16       | 4        | Float   | The Y component of the Y Vector2        |
+----------+----------+---------+-----------------------------------------+
| 20       | 4        | Float   | The X component of the Origin Vector2   |
+----------+----------+---------+-----------------------------------------+
| 24       | 4        | Float   | The Y component of the Origin Vector2   |
+----------+----------+---------+-----------------------------------------+

12: :ref:`Vector4<class_vector4>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+----------+---------+----------------+
| Offset   | Length   | Type    | Description    |
+==========+==========+=========+================+
| 4        | 4        | Float   | X coordinate   |
+----------+----------+---------+----------------+
| 8        | 4        | Float   | Y coordinate   |
+----------+----------+---------+----------------+
| 12       | 4        | Float   | Z coordinate   |
+----------+----------+---------+----------------+
| 16       | 4        | Float   | W coordinate   |
+----------+----------+---------+----------------+

13: :ref:`Vector4i<class_vector4i>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+----------+-----------+----------------+
| Offset   | Length   | Type      | Description    |
+==========+==========+===========+================+
| 4        | 4        | Integer   | X coordinate   |
+----------+----------+-----------+----------------+
| 8        | 4        | Integer   | Y coordinate   |
+----------+----------+-----------+----------------+
| 12       | 4        | Integer   | Z coordinate   |
+----------+----------+-----------+----------------+
| 16       | 4        | Integer   | W coordinate   |
+----------+----------+-----------+----------------+



14: :ref:`Plane<class_plane>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+----------+---------+---------------+
| Offset   | Length   | Type    | Description   |
+==========+==========+=========+===============+
| 4        | 4        | Float   | Normal X      |
+----------+----------+---------+---------------+
| 8        | 4        | Float   | Normal Y      |
+----------+----------+---------+---------------+
| 12       | 4        | Float   | Normal Z      |
+----------+----------+---------+---------------+
| 16       | 4        | Float   | Distance D    |
+----------+----------+---------+---------------+

15: :ref:`Quaternion<class_quaternion>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+----------+---------+---------------+
| Offset   | Length   | Type    | Description   |
+==========+==========+=========+===============+
| 4        | 4        | Float   | Imaginary X   |
+----------+----------+---------+---------------+
| 8        | 4        | Float   | Imaginary Y   |
+----------+----------+---------+---------------+
| 12       | 4        | Float   | Imaginary Z   |
+----------+----------+---------+---------------+
| 16       | 4        | Float   | Real W        |
+----------+----------+---------+---------------+

16: :ref:`AABB<class_aabb>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+----------+---------+---------------+
| Offset   | Length   | Type    | Description   |
+==========+==========+=========+===============+
| 4        | 4        | Float   | X position    |
+----------+----------+---------+---------------+
| 8        | 4        | Float   | Y position    |
+----------+----------+---------+---------------+
| 12       | 4        | Float   | Z position    |
+----------+----------+---------+---------------+
| 16       | 4        | Float   | X size        |
+----------+----------+---------+---------------+
| 20       | 4        | Float   | Y size        |
+----------+----------+---------+---------------+
| 24       | 4        | Float   | Z size        |
+----------+----------+---------+---------------+

17: :ref:`Basis<class_basis>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+----------+---------+------------------------------------------------+
| Offset   | Length   | Type    | Description                                    |
+==========+==========+=========+================================================+
| 4        | 4        | Float   | The X component of the X column vector (x.x)   |
+----------+----------+---------+------------------------------------------------+
| 8        | 4        | Float   | The Y component of the X column vector (x.y)   |
+----------+----------+---------+------------------------------------------------+
| 12       | 4        | Float   | The Z component of the X column vector (x.z)   |
+----------+----------+---------+------------------------------------------------+
| 16       | 4        | Float   | The X component of the Y column vector (y.x)   |
+----------+----------+---------+------------------------------------------------+
| 20       | 4        | Float   | The Y component of the Y column vector (y.y)   |
+----------+----------+---------+------------------------------------------------+
| 24       | 4        | Float   | The Z component of the Y column vector (y.z)   |
+----------+----------+---------+------------------------------------------------+
| 28       | 4        | Float   | The X component of the Z column vector (z.x)   |
+----------+----------+---------+------------------------------------------------+
| 32       | 4        | Float   | The Y component of the Z column vector (z.y)   |
+----------+----------+---------+------------------------------------------------+
| 36       | 4        | Float   | The Z component of the Z column vector (z.z)   |
+----------+----------+---------+------------------------------------------------+

18: :ref:`Transform3D<class_transform3d>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+----------+---------+------------------------------------------------------+
| Offset   | Length   | Type    | Description                                          |
+==========+==========+=========+======================================================+
| 4        | 4        | Float   | The X component of the X column vector (basis.x.x)   |
+----------+----------+---------+------------------------------------------------------+
| 8        | 4        | Float   | The Y component of the X column vector (basis.x.y)   |
+----------+----------+---------+------------------------------------------------------+
| 12       | 4        | Float   | The Z component of the X column vector (basis.x.z)   |
+----------+----------+---------+------------------------------------------------------+
| 16       | 4        | Float   | The X component of the Y column vector (basis.y.x)   |
+----------+----------+---------+------------------------------------------------------+
| 20       | 4        | Float   | The Y component of the Y column vector (basis.y.y)   |
+----------+----------+---------+------------------------------------------------------+
| 24       | 4        | Float   | The Z component of the Y column vector (basis.y.z)   |
+----------+----------+---------+------------------------------------------------------+
| 28       | 4        | Float   | The X component of the Z column vector (basis.z.x)   |
+----------+----------+---------+------------------------------------------------------+
| 32       | 4        | Float   | The Y component of the Z column vector (basis.z.y)   |
+----------+----------+---------+------------------------------------------------------+
| 36       | 4        | Float   | The Z component of the Z column vector (basis.z.z)   |
+----------+----------+---------+------------------------------------------------------+
| 40       | 4        | Float   | The X component of the origin vector (origin.x)      |
+----------+----------+---------+------------------------------------------------------+
| 44       | 4        | Float   | The Y component of the origin vector (origin.y)      |
+----------+----------+---------+------------------------------------------------------+
| 48       | 4        | Float   | The Z component of the origin vector (origin.z)      |
+----------+----------+---------+------------------------------------------------------+

19: :ref:`Projection<class_projection>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+----------+---------+------------------------------------------------+
| Offset   | Length   | Type    | Description                                    |
+==========+==========+=========+================================================+
| 4        | 4        | Float   | The X component of the X column vector (x.x)   |
+----------+----------+---------+------------------------------------------------+
| 8        | 4        | Float   | The Y component of the X column vector (x.y)   |
+----------+----------+---------+------------------------------------------------+
| 12       | 4        | Float   | The Z component of the X column vector (x.z)   |
+----------+----------+---------+------------------------------------------------+
| 16       | 4        | Float   | The W component of the X column vector (x.w)   |
+----------+----------+---------+------------------------------------------------+
| 20       | 4        | Float   | The X component of the Y column vector (y.x)   |
+----------+----------+---------+------------------------------------------------+
| 24       | 4        | Float   | The Y component of the Y column vector (y.y)   |
+----------+----------+---------+------------------------------------------------+
| 28       | 4        | Float   | The Z component of the Y column vector (y.z)   |
+----------+----------+---------+------------------------------------------------+
| 32       | 4        | Float   | The W component of the Y column vector (y.w)   |
+----------+----------+---------+------------------------------------------------+
| 36       | 4        | Float   | The X component of the Z column vector (z.x)   |
+----------+----------+---------+------------------------------------------------+
| 40       | 4        | Float   | The Y component of the Z column vector (z.y)   |
+----------+----------+---------+------------------------------------------------+
| 44       | 4        | Float   | The Z component of the Z column vector (z.z)   |
+----------+----------+---------+------------------------------------------------+
| 48       | 4        | Float   | The W component of the Z column vector (z.w)   |
+----------+----------+---------+------------------------------------------------+
| 52       | 4        | Float   | The X component of the W column vector (w.x)   |
+----------+----------+---------+------------------------------------------------+
| 56       | 4        | Float   | The Y component of the W column vector (w.y)   |
+----------+----------+---------+------------------------------------------------+
| 60       | 4        | Float   | The Z component of the W column vector (w.z)   |
+----------+----------+---------+------------------------------------------------+
| 64       | 4        | Float   | The W component of the W column vector (w.w)   |
+----------+----------+---------+------------------------------------------------+

20: :ref:`Color<class_color>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+----------+---------+----------------------------------------------------------------+
| Offset   | Length   | Type    | Description                                                    |
+==========+==========+=========+================================================================+
| 4        | 4        | Float   | Red (typically 0..1, can be above 1 for overbright colors)     |
+----------+----------+---------+----------------------------------------------------------------+
| 8        | 4        | Float   | Green (typically 0..1, can be above 1 for overbright colors)   |
+----------+----------+---------+----------------------------------------------------------------+
| 12       | 4        | Float   | Blue (typically 0..1, can be above 1 for overbright colors)    |
+----------+----------+---------+----------------------------------------------------------------+
| 16       | 4        | Float   | Alpha (0..1)                                                   |
+----------+----------+---------+----------------------------------------------------------------+

21: :ref:`StringName<class_stringname>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Serialized identically to :ref:`String <string-section>`.

22: :ref:`NodePath<class_nodepath>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+----------+-----------+-----------------------------------------------------------------------------------------+
| Offset   | Length   | Type      | Description                                                                             |
+==========+==========+===========+=========================================================================================+
| 4        | 4        | Integer   | Name count with new format flag (val & 0x80000000 != 0, NameCount = val & 0x7FFFFFFF)   |
+----------+----------+-----------+-----------------------------------------------------------------------------------------+

The old format is no longer supported and will return an error.

For new format:
~~~~~~~~~~~~~~~

+----------+----------+-----------+--------------------------------------------+
| Offset   | Length   | Type      | Description                                |
+==========+==========+===========+============================================+
| 8        | 4        | Integer   | Sub-name count                             |
+----------+----------+-----------+--------------------------------------------+
| 12       | 4        | Integer   | Flags (bit 0: absolute, bit 1: property)   |
+----------+----------+-----------+--------------------------------------------+

.. note::

   If bit 1 (property flag) is set, the sub-name count is incremented by 1
   internally. This is an obsolete format for backwards compatibility.

For each Name and Sub-Name (offsets are relative to the start of each string entry):

+----------+----------+-----------+-----------------------------------------------------------+
| Offset   | Length   | Type      | Description                                               |
+==========+==========+===========+===========================================================+
| 0        | 4        | Integer   | Name/Sub-Name (String length, in bytes, N)                |
+----------+----------+-----------+-----------------------------------------------------------+
| 4        | N        | Bytes     | Name/Sub-Name (UTF-8 encoded string, padded to 4 bytes)   |
+----------+----------+-----------+-----------------------------------------------------------+

23: :ref:`RID<class_rid>`
~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+----------+-----------+-----------------+
| Offset   | Length   | Type      | Description     |
+==========+==========+===========+=================+
| 4        | 8        | Integer   | 64-bit RID ID   |
+----------+----------+-----------+-----------------+

24: :ref:`Object<class_object>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An Object can be serialized in two ways, determined by the ``ENCODE_FLAG_OBJECT_AS_ID`` header flag (``flags & 1 == 1``).

With ``ENCODE_FLAG_OBJECT_AS_ID`` set (Instance ID only)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+----------+----------+-----------+-----------------------------------+
| Offset   | Length   | Type      | Description                       |
+==========+==========+===========+===================================+
| 4        | 8        | Integer   | The Object instance ID (64-bit)   |
+----------+----------+-----------+-----------------------------------+

If the instance ID is 0, it represents a null object.

Without ``ENCODE_FLAG_OBJECT_AS_ID`` (full object)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This mode requires ``full_objects = true`` when decoding, otherwise an error
is returned.

**Null object:**

+----------+----------+-----------+------------------------------+
| Offset   | Length   | Type      | Description                  |
+==========+==========+===========+==============================+
| 4        | 4        | Integer   | 0 (Representing a nullptr)   |
+----------+----------+-----------+------------------------------+

**Non-null object:**

Header:
+----------+----------+-----------+--------------------------------------------------------+
| Offset   | Length   | Type      | Description                                            |
+==========+==========+===========+========================================================+
| 4        | 4        | Integer   | Class name (String length, in bytes, N)                |
+----------+----------+-----------+--------------------------------------------------------+
| 8        | N        | Bytes     | Class name (UTF-8 encoded string, padded to 4 bytes)   |
+----------+----------+-----------+--------------------------------------------------------+
| 8 + N    | 4        | Integer   | The number of properties that are serialized (P)       |
+----------+----------+-----------+--------------------------------------------------------+

Following this header is a contiguous block of key-value property entries, defined below,
where the offset is relative to the start of each property entry:

+----------+--------------+--------------+-----------------------------------------------------------+
| Offset   | Length       | Type         | Description                                               |
+==========+==============+==============+===========================================================+
| 0        | 4            | Integer      | Property name (String length, in bytes, N)                |
+----------+--------------+--------------+-----------------------------------------------------------+
| 4        | N            | Bytes        | Property name (UTF-8 encoded string, padded to 4 bytes)   |
+----------+--------------+--------------+-----------------------------------------------------------+
| 4 + N    | <variable>   | <variable>   | Property value, using this same format                    |
+----------+--------------+--------------+-----------------------------------------------------------+

.. note::

   Not all properties are included. Only properties that are configured with the
   :ref:`PROPERTY_USAGE_STORAGE<class_@GlobalScope_constant_PROPERTY_USAGE_STORAGE>`
   flag set will be serialized. You can add a new usage flag to a property by overriding the
   :ref:`_get_property_list<class_Object_private_method__get_property_list>`
   method in your class. You can also check how property usage is configured by
   calling ``Object._get_property_list``. See
   :ref:`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>` for the
   possible usage flags.

.. note::

   If a property named ``script`` is present and its value is a String, it is
   treated specially: the string is interpreted as a resource path to a Script,
   which is loaded and assigned to the object.

25: :ref:`Callable<class_callable>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Callables cannot be meaningfully serialized. No additional data is written,
and decoding produces an empty Callable.

26: :ref:`Signal<class_signal>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+----------+-----------+---------------------------------------------------------+
| Offset   | Length   | Type      | Description                                             |
+==========+==========+===========+=========================================================+
| 4        | 4        | Integer   | Signal name (String length, in bytes, N)                |
+----------+----------+-----------+---------------------------------------------------------+
| 8        | N        | Bytes     | Signal name (UTF-8 encoded string, padded to 4 bytes)   |
+----------+----------+-----------+---------------------------------------------------------+
| 8 + N    | 8        | Integer   | Object instance ID (64-bit)                             |
+----------+----------+-----------+---------------------------------------------------------+

27: :ref:`Dictionary<class_dictionary>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For typed dictionaries, the header flags indicate the variant type for both keys
and values (see Header Flags section). Depending on these flags, type
information is encoded before the element count.

**Container Type Encoding (for each of key type and value type, if not NONE):**

If type kind is ``BUILTIN`` (0b01):

+----------+----------+-----------+-------------------+
| Offset   | Length   | Type      | Description       |
+==========+==========+===========+===================+
| 4        | 4        | Integer   | Variant type ID   |
+----------+----------+-----------+-------------------+

If type kind is ``CLASS_NAME`` (0b10) or ``SCRIPT`` (0b11):

+----------+----------+-----------+--------------------------------------------------------------------+
| Offset   | Length   | Type      | Description                                                        |
+==========+==========+===========+====================================================================+
| 4        | 4        | Integer   | Class name/Script path (String length, in bytes, N)                |
+----------+----------+-----------+--------------------------------------------------------------------+
| 8        | N        | Bytes     | Class name/Script path (UTF-8 encoded string, padded to 4 bytes)   |
+----------+----------+-----------+--------------------------------------------------------------------+

Value type encoding, if applicable, immediately follows key type encoding.

**Element count (immediately following all type information):**

+----------+----------+-----------+----------------------------------------------------------------------+
| Offset   | Length   | Type      | Description                                                          |
+==========+==========+===========+======================================================================+
| 0        | 4        | Integer   | val & 0x7FFFFFFF = element count, val & 0x80000000 = shared (bool)   |
+----------+----------+-----------+----------------------------------------------------------------------+

Following this header is a contiguous block of key-value pairs,
encoded using the same serialization format defined in this document.

28: :ref:`Array<class_array>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For typed arrays, the header flags indicate the element type (see Header
Flags section). The container type is encoded the same way as Dictionary.

**Element count (immediately following type information, if any):**

+----------+----------+-----------+----------------------------------------------------------------------+
| Offset   | Length   | Type      | Description                                                          |
+==========+==========+===========+======================================================================+
| 0        | 4        | Integer   | val & 0x7FFFFFFF = element count, val & 0x80000000 = shared (bool)   |
+----------+----------+-----------+----------------------------------------------------------------------+

Following the element count is a contiguous block of values,
encoded using the same serialization format defined in this document.

29: :ref:`PackedByteArray<class_PackedByteArray>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+----------+-----------+---------------------------------+
| Offset   | Length   | Type      | Description                     |
+==========+==========+===========+=================================+
| 4        | 4        | Integer   | Array length (L)                |
+----------+----------+-----------+---------------------------------+
| 8 + i    | 1        | Byte      | Array element #i ``(0 <= i < L)`` |
+----------+----------+-----------+---------------------------------+

The array data is padded to 4 bytes.

30: :ref:`PackedInt32Array<class_PackedInt32Array>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------+----------+-----------+---------------------------------+
| Offset       | Length   | Type      | Description                     |
+==============+==========+===========+=================================+
| 4            | 4        | Integer   | Array length (L)                |
+--------------+----------+-----------+---------------------------------+
| 8 + i \* 4   | 4        | Integer   | Array element #i ``(0 <= i < L)`` |
+--------------+----------+-----------+---------------------------------+

31: :ref:`PackedInt64Array<class_PackedInt64Array>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------+----------+-----------+---------------------------------+
| Offset       | Length   | Type      | Description                     |
+==============+==========+===========+=================================+
| 4            | 4        | Integer   | Array length (L)                |
+--------------+----------+-----------+---------------------------------+
| 8 + i \* 8   | 8        | Integer   | Array element #i ``(0 <= i < L)`` |
+--------------+----------+-----------+---------------------------------+

32: :ref:`PackedFloat32Array<class_PackedFloat32Array>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------+----------+-----------+---------------------------------+
| Offset       | Length   | Type      | Description                     |
+==============+==========+===========+=================================+
| 4            | 4        | Integer   | Array length (L)                |
+--------------+----------+-----------+---------------------------------+
| 8 + i \* 4   | 4        | Float     | Array element #i ``(0 <= i < L)`` |
+--------------+----------+-----------+---------------------------------+

33: :ref:`PackedFloat64Array<class_PackedFloat64Array>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------+----------+-----------+---------------------------------+
| Offset       | Length   | Type      | Description                     |
+==============+==========+===========+=================================+
| 4            | 4        | Integer   | Array length (L)                |
+--------------+----------+-----------+---------------------------------+
| 8 + i \* 8   | 8        | Float     | Array element #i ``(0 <= i < L)`` |
+--------------+----------+-----------+---------------------------------+

34: :ref:`PackedStringArray<class_PackedStringArray>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+----------+-----------+--------------------------+
| Offset   | Length   | Type      | Description              |
+==========+==========+===========+==========================+
| 4        | 4        | Integer   | Array length (Strings)   |
+----------+----------+-----------+--------------------------+

Following the array length is a contiguous block of strings.

For each string entry (0 <= i < length):

.. note::

   Offsets below are relative to the start of each string entry.

+----------+----------+-----------+----------------------------------------------------+
| Offset   | Length   | Type      | Description                                        |
+==========+==========+===========+====================================================+
| 0        | 4        | Integer   | String length (N, including the null terminator)   |
+----------+----------+-----------+----------------------------------------------------+
| 4        | N        | Bytes     | UTF-8 encoded string with a null terminator        |
+----------+----------+-----------+----------------------------------------------------+

Every string is padded to 4 bytes.

.. note::

   Unlike regular String encoding, PackedStringArray encodes strings with a
   null terminator included in the length.

35: :ref:`PackedVector2Array<class_PackedVector2Array>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+----------+-----------+----------------+
| Offset   | Length   | Type      | Description    |
+==========+==========+===========+================+
| 4        | 4        | Integer   | Array length   |
+----------+----------+-----------+----------------+

Following the array length is a contiguous block of Vector2s.

For each Vector2 entry (0 <= i < length):

+---------------+----------+---------+----------------+
| Offset        | Length   | Type    | Description    |
+===============+==========+=========+================+
| 8 + i \* 8    | 4        | Float   | X coordinate   |
+---------------+----------+---------+----------------+
| 12 + i \* 8   | 4        | Float   | Y coordinate   |
+---------------+----------+---------+----------------+

36: :ref:`PackedVector3Array<class_PackedVector3Array>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+----------+-----------+----------------+
| Offset   | Length   | Type      | Description    |
+==========+==========+===========+================+
| 4        | 4        | Integer   | Array length   |
+----------+----------+-----------+----------------+

Following the array length is a contiguous block of Vector3s.

For each Vector3 entry (0 <= i < length):

+----------------+----------+---------+----------------+
| Offset         | Length   | Type    | Description    |
+================+==========+=========+================+
| 8 + i \* 12    | 4        | Float   | X coordinate   |
+----------------+----------+---------+----------------+
| 12 + i \* 12   | 4        | Float   | Y coordinate   |
+----------------+----------+---------+----------------+
| 16 + i \* 12   | 4        | Float   | Z coordinate   |
+----------------+----------+---------+----------------+

37: :ref:`PackedColorArray<class_PackedColorArray>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+----------+-----------+----------------+
| Offset   | Length   | Type      | Description    |
+==========+==========+===========+================+
| 4        | 4        | Integer   | Array length   |
+----------+----------+-----------+----------------+

Following the array length is a contiguous block of Colors.

For each Color entry (0 <= i < length):

+----------------+----------+---------+----------------------------------------------------------------+
| Offset         | Length   | Type    | Description                                                    |
+================+==========+=========+================================================================+
| 8 + i \* 16    | 4        | Float   | Red (typically 0..1, can be above 1 for overbright colors)     |
+----------------+----------+---------+----------------------------------------------------------------+
| 12 + i \* 16   | 4        | Float   | Green (typically 0..1, can be above 1 for overbright colors)   |
+----------------+----------+---------+----------------------------------------------------------------+
| 16 + i \* 16   | 4        | Float   | Blue (typically 0..1, can be above 1 for overbright colors)    |
+----------------+----------+---------+----------------------------------------------------------------+
| 20 + i \* 16   | 4        | Float   | Alpha (0..1)                                                   |
+----------------+----------+---------+----------------------------------------------------------------+

.. note::

   Colors are always encoded in single precision.

38: :ref:`PackedVector4Array<class_PackedVector4Array>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+----------+-----------+----------------+
| Offset   | Length   | Type      | Description    |
+==========+==========+===========+================+
| 4        | 4        | Integer   | Array length   |
+----------+----------+-----------+----------------+

Following the array length is a contiguous block of Vector4s.

For each Vector4 entry (0 <= i < length):

+----------------+----------+---------+----------------+
| Offset         | Length   | Type    | Description    |
+================+==========+=========+================+
| 8 + i \* 16    | 4        | Float   | X coordinate   |
+----------------+----------+---------+----------------+
| 12 + i \* 16   | 4        | Float   | Y coordinate   |
+----------------+----------+---------+----------------+
| 16 + i \* 16   | 4        | Float   | Z coordinate   |
+----------------+----------+---------+----------------+
| 20 + i \* 16   | 4        | Float   | W coordinate   |
+----------------+----------+---------+----------------+
