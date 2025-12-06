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

+--------+--------------------------+
| Type   | Value                    |
+========+==========================+
| 0      | null                     |
+--------+--------------------------+
| 1      | bool                     |
+--------+--------------------------+
| 2      | int                      |
+--------+--------------------------+
| 3      | float                    |
+--------+--------------------------+
| 4      | String                   |
+--------+--------------------------+
| 5      | Vector2                  |
+--------+--------------------------+
| 6      | Vector2i                 |
+--------+--------------------------+
| 7      | Rect2                    |
+--------+--------------------------+
| 8      | Rect2i                   |
+--------+--------------------------+
| 9      | Vector3                  |
+--------+--------------------------+
| 10     | Vector3i                 |
+--------+--------------------------+
| 11     | Vector4                  |
+--------+--------------------------+
| 12     | Vector4i                 |
+--------+--------------------------+
| 13     | Transform2D              |
+--------+--------------------------+
| 14     | Plane                    |
+--------+--------------------------+
| 15     | Quaternion               |
+--------+--------------------------+
| 16     | AABB                     |
+--------+--------------------------+
| 17     | Basis                    |
+--------+--------------------------+
| 18     | Transform3D              |
+--------+--------------------------+
| 19     | Projection               |
+--------+--------------------------+
| 20     | Color                    |
+--------+--------------------------+
| 21     | StringName               |
+--------+--------------------------+
| 22     | NodePath                 |
+--------+--------------------------+
| 23     | RID                      |
+--------+--------------------------+
| 24     | Object                   |
+--------+--------------------------+
| 25     | Callable                 |
+--------+--------------------------+
| 26     | Signal                   |
+--------+--------------------------+
| 27     | Dictionary               |
+--------+--------------------------+
| 28     | Array                    |
+--------+--------------------------+
| 29     | PackedByteArray          |
+--------+--------------------------+
| 30     | PackedInt32Array         |
+--------+--------------------------+
| 31     | PackedInt64Array         |
+--------+--------------------------+
| 32     | PackedFloat32Array       |
+--------+--------------------------+
| 33     | PackedFloat64Array       |
+--------+--------------------------+
| 34     | PackedStringArray        |
+--------+--------------------------+
| 35     | PackedVector2Array       |
+--------+--------------------------+
| 36     | PackedVector3Array       |
+--------+--------------------------+
| 37     | PackedColorArray         |
+--------+--------------------------+
| 38     | PackedVector4Array       |
+--------+--------------------------+

Header Flags
~~~~~~~~~~~~

The header's upper 16 bits contain type-specific flags:

+------------------------------------------+-------------------------------------------+
| Flag                                     | Description                               |
+==========================================+===========================================+
| ``ENCODE_FLAG_64 = (1 << 16)``           | Used for int, float, and math types to    |
|                                          | indicate 64-bit (double) precision        |
+------------------------------------------+-------------------------------------------+
| ``ENCODE_FLAG_OBJECT_AS_ID = (1 << 16)`` | Used for Object to indicate serialization |
|                                          | as instance ID only                       |
+------------------------------------------+-------------------------------------------+

For typed containers (Array and Dictionary), additional flags indicate the
container's type information:

**Array (bits 16-17):**

+-------+--------------------------------------+
| Value | Meaning                              |
+=======+======================================+
| 0b00  | Untyped                              |
+-------+--------------------------------------+
| 0b01  | Typed with builtin type              |
+-------+--------------------------------------+
| 0b10  | Typed with class name                |
+-------+--------------------------------------+
| 0b11  | Typed with script path               |
+-------+--------------------------------------+

**Dictionary key type (bits 16-17) and value type (bits 18-19):**

Same values as Array.

Following this is the actual packet contents, which varies for each type of
packet. Note that this assumes Godot is compiled with single-precision floats,
which is the default. If Godot was compiled with double-precision floats, the
length of "Float" fields within data structures should be 8, and the offset
should be ``(offset - 4) * 2 + 4``. The "float" type itself always uses double
precision.

0: null
~~~~~~~

1: :ref:`bool<class_bool>`
~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+-------+-----------+---------------------------+
| Offset   | Len   | Type      | Description               |
+==========+=======+===========+===========================+
| 4        | 4     | Integer   | 0 for False, 1 for True   |
+----------+-------+-----------+---------------------------+

2: :ref:`int<class_int>`
~~~~~~~~~~~~~~~~~~~~~~~~

If no flags are set (flags == 0), the integer is sent as a 32 bit integer:

+----------+-------+-----------+--------------------------+
| Offset   | Len   | Type      | Description              |
+==========+=======+===========+==========================+
| 4        | 4     | Integer   | 32-bit signed integer    |
+----------+-------+-----------+--------------------------+

If flag ``ENCODE_FLAG_64`` is set (``flags & 1 == 1``), the integer is sent as
a 64-bit integer:

+----------+-------+-----------+--------------------------+
| Offset   | Len   | Type      | Description              |
+==========+=======+===========+==========================+
| 4        | 8     | Integer   | 64-bit signed integer    |
+----------+-------+-----------+--------------------------+

3: :ref:`float<class_float>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If no flags are set (flags == 0), the float is sent as a 32 bit single precision:

+----------+-------+---------+-----------------------------------+
| Offset   | Len   | Type    | Description                       |
+==========+=======+=========+===================================+
| 4        | 4     | Float   | IEEE 754 single-precision float   |
+----------+-------+---------+-----------------------------------+

If flag ``ENCODE_FLAG_64`` is set (``flags & 1 == 1``), the float is sent as
a 64-bit double precision number:

+----------+-------+---------+-----------------------------------+
| Offset   | Len   | Type    | Description                       |
+==========+=======+=========+===================================+
| 4        | 8     | Float   | IEEE 754 double-precision float   |
+----------+-------+---------+-----------------------------------+

4: :ref:`String<class_string>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+-------+-----------+------------------------------+
| Offset   | Len   | Type      | Description                  |
+==========+=======+===========+==============================+
| 4        | 4     | Integer   | String length (in byte, N)   |
+----------+-------+-----------+------------------------------+
| 8        | N     | Bytes     | UTF-8 encoded string         |
+----------+-------+-----------+------------------------------+

This field is padded to 4 bytes.

5: :ref:`Vector2<class_vector2>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If no flags are set (flags == 0), the floats are sent as 32 bit single precision:

+----------+-------+---------+----------------+
| Offset   | Len   | Type    | Description    |
+==========+=======+=========+================+
| 4        | 4     | Float   | X coordinate   |
+----------+-------+---------+----------------+
| 8        | 4     | Float   | Y coordinate   |
+----------+-------+---------+----------------+

If flag ``ENCODE_FLAG_64`` is set (flags & 1 == 1), the floats are sent as 64 bit double precision:

+----------+-------+---------+----------------+
| Offset   | Len   | Type    | Description    |
+==========+=======+=========+================+
| 4        | 8     | Double  | X coordinate   |
+----------+-------+---------+----------------+
| 12       | 8     | Double  | Y coordinate   |
+----------+-------+---------+----------------+

6: :ref:`Vector2i<class_vector2i>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+-------+-----------+----------------+
| Offset   | Len   | Type      | Description    |
+==========+=======+===========+================+
| 4        | 4     | Integer   | X coordinate   |
+----------+-------+-----------+----------------+
| 8        | 4     | Integer   | Y coordinate   |
+----------+-------+-----------+----------------+

7: :ref:`Rect2<class_rect2>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If no flags are set (flags == 0), the floats are sent as 32 bit single precision:

+----------+-------+---------+----------------+
| Offset   | Len   | Type    | Description    |
+==========+=======+=========+================+
| 4        | 4     | Float   | X position     |
+----------+-------+---------+----------------+
| 8        | 4     | Float   | Y position     |
+----------+-------+---------+----------------+
| 12       | 4     | Float   | X size         |
+----------+-------+---------+----------------+
| 16       | 4     | Float   | Y size         |
+----------+-------+---------+----------------+

If flag ``ENCODE_FLAG_64`` is set (flags & 1 == 1), the floats are sent as 64 bit double precision:

+----------+-------+---------+----------------+
| Offset   | Len   | Type    | Description    |
+==========+=======+=========+================+
| 4        | 8     | Double  | X position     |
+----------+-------+---------+----------------+
| 12       | 8     | Double  | Y position     |
+----------+-------+---------+----------------+
| 20       | 8     | Double  | X size         |
+----------+-------+---------+----------------+
| 28       | 8     | Double  | Y size         |
+----------+-------+---------+----------------+

8: :ref:`Rect2i<class_rect2i>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+-------+-----------+----------------+
| Offset   | Len   | Type      | Description    |
+==========+=======+===========+================+
| 4        | 4     | Integer   | X position     |
+----------+-------+-----------+----------------+
| 8        | 4     | Integer   | Y position     |
+----------+-------+-----------+----------------+
| 12       | 4     | Integer   | X size         |
+----------+-------+-----------+----------------+
| 16       | 4     | Integer   | Y size         |
+----------+-------+-----------+----------------+

9: :ref:`Vector3<class_vector3>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If no flags are set (flags == 0), the floats are sent as 32 bit single precision:

+----------+-------+---------+----------------+
| Offset   | Len   | Type    | Description    |
+==========+=======+=========+================+
| 4        | 4     | Float   | X coordinate   |
+----------+-------+---------+----------------+
| 8        | 4     | Float   | Y coordinate   |
+----------+-------+---------+----------------+
| 12       | 4     | Float   | Z coordinate   |
+----------+-------+---------+----------------+

If flag ``ENCODE_FLAG_64`` is set (flags & 1 == 1), the floats are sent as 64 bit double precision:

+----------+-------+---------+----------------+
| Offset   | Len   | Type    | Description    |
+==========+=======+=========+================+
| 4        | 8     | Double  | X coordinate   |
+----------+-------+---------+----------------+
| 12       | 8     | Double  | Y coordinate   |
+----------+-------+---------+----------------+
| 20       | 8     | Double  | Z coordinate   |
+----------+-------+---------+----------------+

10: :ref:`Vector3i<class_vector3i>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+-------+-----------+----------------+
| Offset   | Len   | Type      | Description    |
+==========+=======+===========+================+
| 4        | 4     | Integer   | X coordinate   |
+----------+-------+-----------+----------------+
| 8        | 4     | Integer   | Y coordinate   |
+----------+-------+-----------+----------------+
| 12       | 4     | Integer   | Z coordinate   |
+----------+-------+-----------+----------------+

11: :ref:`Vector4<class_vector4>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If no flags are set (flags == 0), the floats are sent as 32 bit single precision:

+----------+-------+---------+----------------+
| Offset   | Len   | Type    | Description    |
+==========+=======+=========+================+
| 4        | 4     | Float   | X coordinate   |
+----------+-------+---------+----------------+
| 8        | 4     | Float   | Y coordinate   |
+----------+-------+---------+----------------+
| 12       | 4     | Float   | Z coordinate   |
+----------+-------+---------+----------------+
| 16       | 4     | Float   | W coordinate   |
+----------+-------+---------+----------------+

If flag ``ENCODE_FLAG_64`` is set (flags & 1 == 1), the floats are sent as 64 bit double precision:

+----------+-------+---------+----------------+
| Offset   | Len   | Type    | Description    |
+==========+=======+=========+================+
| 4        | 8     | Double  | X coordinate   |
+----------+-------+---------+----------------+
| 12       | 8     | Double  | Y coordinate   |
+----------+-------+---------+----------------+
| 20       | 8     | Double  | Z coordinate   |
+----------+-------+---------+----------------+
| 28       | 8     | Double  | W coordinate   |
+----------+-------+---------+----------------+

12: :ref:`Vector4i<class_vector4i>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+-------+-----------+----------------+
| Offset   | Len   | Type      | Description    |
+==========+=======+===========+================+
| 4        | 4     | Integer   | X coordinate   |
+----------+-------+-----------+----------------+
| 8        | 4     | Integer   | Y coordinate   |
+----------+-------+-----------+----------------+
| 12       | 4     | Integer   | Z coordinate   |
+----------+-------+-----------+----------------+
| 16       | 4     | Integer   | W coordinate   |
+----------+-------+-----------+----------------+

13: :ref:`Transform2D<class_transform2d>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If no flags are set (flags == 0), the floats are sent as 32 bit single precision:

+----------+-------+---------+---------------------------------------------------------------+
| Offset   | Len   | Type    | Description                                                   |
+==========+=======+=========+===============================================================+
| 4        | 4     | Float   | The X component of the X column vector, accessed via [0][0]   |
+----------+-------+---------+---------------------------------------------------------------+
| 8        | 4     | Float   | The Y component of the X column vector, accessed via [0][1]   |
+----------+-------+---------+---------------------------------------------------------------+
| 12       | 4     | Float   | The X component of the Y column vector, accessed via [1][0]   |
+----------+-------+---------+---------------------------------------------------------------+
| 16       | 4     | Float   | The Y component of the Y column vector, accessed via [1][1]   |
+----------+-------+---------+---------------------------------------------------------------+
| 20       | 4     | Float   | The X component of the origin vector, accessed via [2][0]     |
+----------+-------+---------+---------------------------------------------------------------+
| 24       | 4     | Float   | The Y component of the origin vector, accessed via [2][1]     |
+----------+-------+---------+---------------------------------------------------------------+

If flag ``ENCODE_FLAG_64`` is set (flags & 1 == 1), the floats are sent as 64 bit double precision:

14: :ref:`Plane<class_plane>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If no flags are set (flags == 0), the floats are sent as 32 bit single precision:

+----------+-------+---------+---------------+
| Offset   | Len   | Type    | Description   |
+==========+=======+=========+===============+
| 4        | 4     | Float   | Normal X      |
+----------+-------+---------+---------------+
| 8        | 4     | Float   | Normal Y      |
+----------+-------+---------+---------------+
| 12       | 4     | Float   | Normal Z      |
+----------+-------+---------+---------------+
| 16       | 4     | Float   | Distance D    |
+----------+-------+---------+---------------+

If flag ``ENCODE_FLAG_64`` is set (flags & 1 == 1), the floats are sent as 64 bit double precision:

15: :ref:`Quaternion<class_quaternion>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If no flags are set (flags == 0), the floats are sent as 32 bit single precision:

+----------+-------+---------+---------------+
| Offset   | Len   | Type    | Description   |
+==========+=======+=========+===============+
| 4        | 4     | Float   | Imaginary X   |
+----------+-------+---------+---------------+
| 8        | 4     | Float   | Imaginary Y   |
+----------+-------+---------+---------------+
| 12       | 4     | Float   | Imaginary Z   |
+----------+-------+---------+---------------+
| 16       | 4     | Float   | Real W        |
+----------+-------+---------+---------------+

If flag ``ENCODE_FLAG_64`` is set (flags & 1 == 1), the floats are sent as 64 bit double precision.

16: :ref:`AABB<class_aabb>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If no flags are set (flags == 0), the floats are sent as 32 bit single precision:

+----------+-------+---------+----------------+
| Offset   | Len   | Type    | Description    |
+==========+=======+=========+================+
| 4        | 4     | Float   | X position     |
+----------+-------+---------+----------------+
| 8        | 4     | Float   | Y position     |
+----------+-------+---------+----------------+
| 12       | 4     | Float   | Z position     |
+----------+-------+---------+----------------+
| 16       | 4     | Float   | X size         |
+----------+-------+---------+----------------+
| 20       | 4     | Float   | Y size         |
+----------+-------+---------+----------------+
| 24       | 4     | Float   | Z size         |
+----------+-------+---------+----------------+

If flag ``ENCODE_FLAG_64`` is set (flags & 1 == 1), the floats are sent as 64 bit double precision.

17: :ref:`Basis<class_basis>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If no flags are set (flags == 0), the floats are sent as 32 bit single precision:

+----------+-------+---------+---------------------------------------------------------------+
| Offset   | Len   | Type    | Description                                                   |
+==========+=======+=========+===============================================================+
| 4        | 4     | Float   | The X component of the X column vector, accessed via [0][0]  |
+----------+-------+---------+---------------------------------------------------------------+
| 8        | 4     | Float   | The Y component of the X column vector, accessed via [0][1]  |
+----------+-------+---------+---------------------------------------------------------------+
| 12       | 4     | Float   | The Z component of the X column vector, accessed via [0][2]  |
+----------+-------+---------+---------------------------------------------------------------+
| 16       | 4     | Float   | The X component of the Y column vector, accessed via [1][0]  |
+----------+-------+---------+---------------------------------------------------------------+
| 20       | 4     | Float   | The Y component of the Y column vector, accessed via [1][1]  |
+----------+-------+---------+---------------------------------------------------------------+
| 24       | 4     | Float   | The Z component of the Y column vector, accessed via [1][2]  |
+----------+-------+---------+---------------------------------------------------------------+
| 28       | 4     | Float   | The X component of the Z column vector, accessed via [2][0]  |
+----------+-------+---------+---------------------------------------------------------------+
| 32       | 4     | Float   | The Y component of the Z column vector, accessed via [2][1]  |
+----------+-------+---------+---------------------------------------------------------------+
| 36       | 4     | Float   | The Z component of the Z column vector, accessed via [2][2]  |
+----------+-------+---------+---------------------------------------------------------------+

If flag ``ENCODE_FLAG_64`` is set (flags & 1 == 1), the floats are sent as 64 bit double precision.

18: :ref:`Transform3D<class_transform3d>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If no flags are set (flags == 0), the floats are sent as 32 bit single precision:

+----------+-------+---------+---------------------------------------------------------------+
| Offset   | Len   | Type    | Description                                                   |
+==========+=======+=========+===============================================================+
| 4        | 4     | Float   | The X component of the X column vector, accessed via [0][0]   |
+----------+-------+---------+---------------------------------------------------------------+
| 8        | 4     | Float   | The Y component of the X column vector, accessed via [0][1]   |
+----------+-------+---------+---------------------------------------------------------------+
| 12       | 4     | Float   | The Z component of the X column vector, accessed via [0][2]   |
+----------+-------+---------+---------------------------------------------------------------+
| 16       | 4     | Float   | The X component of the Y column vector, accessed via [1][0]   |
+----------+-------+---------+---------------------------------------------------------------+
| 20       | 4     | Float   | The Y component of the Y column vector, accessed via [1][1]   |
+----------+-------+---------+---------------------------------------------------------------+
| 24       | 4     | Float   | The Z component of the Y column vector, accessed via [1][2]   |
+----------+-------+---------+---------------------------------------------------------------+
| 28       | 4     | Float   | The X component of the Z column vector, accessed via [2][0]   |
+----------+-------+---------+---------------------------------------------------------------+
| 32       | 4     | Float   | The Y component of the Z column vector, accessed via [2][1]   |
+----------+-------+---------+---------------------------------------------------------------+
| 36       | 4     | Float   | The Z component of the Z column vector, accessed via [2][2]   |
+----------+-------+---------+---------------------------------------------------------------+
| 40       | 4     | Float   | The X component of the origin vector, accessed via [3][0]     |
+----------+-------+---------+---------------------------------------------------------------+
| 44       | 4     | Float   | The Y component of the origin vector, accessed via [3][1]     |
+----------+-------+---------+---------------------------------------------------------------+
| 48       | 4     | Float   | The Z component of the origin vector, accessed via [3][2]     |
+----------+-------+---------+---------------------------------------------------------------+

If flag ``ENCODE_FLAG_64`` is set (flags & 1 == 1), the floats are sent as 64 bit double precision.

19: :ref:`Projection<class_projection>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If no flags are set (flags == 0), the floats are sent as 32 bit single precision:

+----------+-------+---------+------------------------------+
| Offset   | Len   | Type    | Description                  |
+==========+=======+=========+==============================+
| 4        | 4     | Float   | x.x (Column 0, Row 0)        |
+----------+-------+---------+------------------------------+
| 8        | 4     | Float   | x.y (Column 0, Row 1)        |
+----------+-------+---------+------------------------------+
| 12       | 4     | Float   | x.z (Column 0, Row 2)        |
+----------+-------+---------+------------------------------+
| 16       | 4     | Float   | x.w (Column 0, Row 3)        |
+----------+-------+---------+------------------------------+
| 20       | 4     | Float   | y.x (Column 1, Row 0)        |
+----------+-------+---------+------------------------------+
| 24       | 4     | Float   | y.y (Column 1, Row 1)        |
+----------+-------+---------+------------------------------+
| 28       | 4     | Float   | y.z (Column 1, Row 2)        |
+----------+-------+---------+------------------------------+
| 32       | 4     | Float   | y.w (Column 1, Row 3)        |
+----------+-------+---------+------------------------------+
| 36       | 4     | Float   | z.x (Column 2, Row 0)        |
+----------+-------+---------+------------------------------+
| 40       | 4     | Float   | z.y (Column 2, Row 1)        |
+----------+-------+---------+------------------------------+
| 44       | 4     | Float   | z.z (Column 2, Row 2)        |
+----------+-------+---------+------------------------------+
| 48       | 4     | Float   | z.w (Column 2, Row 3)        |
+----------+-------+---------+------------------------------+
| 52       | 4     | Float   | w.x (Column 3, Row 0)        |
+----------+-------+---------+------------------------------+
| 56       | 4     | Float   | w.y (Column 3, Row 1)        |
+----------+-------+---------+------------------------------+
| 60       | 4     | Float   | w.z (Column 3, Row 2)        |
+----------+-------+---------+------------------------------+
| 64       | 4     | Float   | w.w (Column 3, Row 3)        |
+----------+-------+---------+------------------------------+

Total of 16 floats (64 bytes for single precision, 128 bytes for double).
If flag ``ENCODE_FLAG_64`` is set (flags & 1 == 1), the floats are sent as 64 bit double precision.

20: :ref:`Color<class_color>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+-------+---------+--------------------------------------------------------------+
| Offset   | Len   | Type    | Description                                                  |
+==========+=======+=========+==============================================================+
| 4        | 4     | Float   | Red (typically 0..1, can be above 1 for overbright colors)   |
+----------+-------+---------+--------------------------------------------------------------+
| 8        | 4     | Float   | Green (typically 0..1, can be above 1 for overbright colors) |
+----------+-------+---------+--------------------------------------------------------------+
| 12       | 4     | Float   | Blue (typically 0..1, can be above 1 for overbright colors)  |
+----------+-------+---------+--------------------------------------------------------------+
| 16       | 4     | Float   | Alpha (0..1)                                                 |
+----------+-------+---------+--------------------------------------------------------------+

21: :ref:`StringName<class_stringname>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Encoded identically to String (see type 4).

22: :ref:`NodePath<class_nodepath>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+-------+-----------+-----------------------------------------------------------------------------------------+
| Offset   | Len   | Type      | Description                                                                             |
+==========+=======+===========+=========================================================================================+
| 4        | 4     | Integer   | Name count with new format flag (val & 0x80000000 != 0, NameCount = val & 0x7FFFFFFF)   |
+----------+-------+-----------+-----------------------------------------------------------------------------------------+

The old format is no longer supported and will return an error.

For new format:
~~~~~~~~~~~~~~~

+----------+-------+-----------+--------------------------------------------+
| Offset   | Len   | Type      | Description                                |
+==========+=======+===========+============================================+
| 8        | 4     | Integer   | Sub-name count                             |
+----------+-------+-----------+--------------------------------------------+
| 12       | 4     | Integer   | Flags (bit 0: absolute, bit 1: property)   |
+----------+-------+-----------+--------------------------------------------+

.. note::

   If bit 1 (property flag) is set, the sub-name count is incremented by 1
   internally. This is an obsolete format for backwards compatibility.

For each Name and Sub-Name (offsets are relative to the start of each string entry):

+----------+-------+-----------+-----------------------------+
| Offset   | Len   | Type      | Description                 |
+==========+=======+===========+=============================+
| 0      | 4     | Integer   | String length (in bytes, N)   |
+----------+-------+-----------+-----------------------------+
| 4      | N     | Bytes     | UTF-8 encoded string          |
+----------+-------+-----------+-----------------------------+

Every name string is padded to 4 bytes.

23: :ref:`RID<class_rid>`
~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+-------+-----------+-----------------+
| Offset   | Len   | Type      | Description     |
+==========+=======+===========+=================+
| 4        | 8     | Integer   | 64-bit RID ID   |
+----------+-------+-----------+-----------------+

24: :ref:`Object<class_object>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An Object can be serialized in two ways, determined by the
``ENCODE_FLAG_OBJECT_AS_ID`` header flag (``flags & 1 == 1``).

With ``ENCODE_FLAG_OBJECT_AS_ID`` set (instance ID only)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+----------+-------+------------+-----------------------------------+
| Offset   | Len   | Type       | Description                       |
+==========+=======+============+===================================+
| 4        | 8     | Integer    | The Object instance ID (64-bit)   |
+----------+-------+------------+-----------------------------------+

If the instance ID is 0, it represents a null object.

Without ``ENCODE_FLAG_OBJECT_AS_ID`` (full object)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This mode requires ``full_objects = true`` when decoding, otherwise an error
is returned.

**Null object:**

+----------+-------+-----------+--------------------------------------------+
| Offset   | Len   | Type      | Description                                |
+==========+=======+===========+============================================+
| 4        | 4     | Integer   | 0 (empty string length, indicating null)   |
+----------+-------+-----------+--------------------------------------------+

**Non-null object:**

+----------+-------+----------------+--------------------------------------------------------+
| Offset   | Len   | Type           | Description                                            |
+==========+=======+================+========================================================+
| 4        | 4     | Integer        | Class name (String length, N)                          |
+----------+-------+----------------+--------------------------------------------------------+
| 8        | N     | Bytes          | Class name (UTF-8 encoded string, padded to 4 bytes)   |
+----------+-------+----------------+--------------------------------------------------------+
| 8+N      | 4     | Integer        | The number of properties that are serialized           |
+----------+-------+----------------+--------------------------------------------------------+

For each property (offsets relative to the start of each property):

+----------+-------+----------------+-----------------------------------------------------------+
| Offset   | Len   | Type           | Description                                               |
+==========+=======+================+===========================================================+
| 0        | 4     | Integer        | Property name (String length, N)                          |
+----------+-------+----------------+-----------------------------------------------------------+
| 4        | N     | Bytes          | Property name (UTF-8 encoded string, padded to 4 bytes)   |
+----------+-------+----------------+-----------------------------------------------------------+
| 4+N+Z    | W     | <variable>     | Property value, using this same format                    |
+----------+-------+----------------+-----------------------------------------------------------+

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

+----------+-------+-----------+-------------------------------+
| Offset   | Len   | Type      | Description                   |
+==========+=======+===========+===============================+
| 4        | 4     | Integer   | Signal name string length (N) |
+----------+-------+-----------+-------------------------------+
| 8        | N     | Bytes     | Signal name (UTF-8, padded)   |
+----------+-------+-----------+-------------------------------+
| 8+N      | 8     | Integer   | Object instance ID (64-bit)   |
+----------+-------+-----------+-------------------------------+

27: :ref:`Dictionary<class_dictionary>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For typed dictionaries, the header flags indicate the type kind for both keys
and values (see Header Flags section). Depending on these flags, type
information is encoded before the element count.

**Container Type Encoding (for each of key type and value type, if not NONE):**

If type kind is ``BUILTIN`` (0b01):

+----------+-------+-----------+----------------------------+
| Offset   | Len   | Type      | Description                |
+==========+=======+===========+============================+
| 4        | 4     | Integer   | Variant type ID            |
+----------+-------+-----------+----------------------------+

If type kind is ``CLASS_NAME`` (0b10) or ``SCRIPT`` (0b11):

+----------+-------+-----------+-----------------------------------------------+
| Offset   | Len   | Type      | Description                                   |
+==========+=======+===========+===============================================+
| 4        | 4     | Integer   | Class name or script path string length (N)   |
+----------+-------+-----------+-----------------------------------------------+
| 8        | N     | Bytes     | Class name or script path (UTF-8, padded)     |
+----------+-------+-----------+-----------------------------------------------+

Value type encoding, if applicable, immediately follows key type encoding.

**Element count (immediately following all type information):**

+----------+-------+-----------+----------------------------------------------------------------------+
| Offset   | Len   | Type      | Description                                                          |
+==========+=======+===========+======================================================================+
| 0        | 4     | Integer   | val & 0x7FFFFFFF = element count, val & 0x80000000 = shared (bool)   |
+----------+-------+-----------+----------------------------------------------------------------------+

Then what follows is, for each element, a key-value pair encoded one after
the other using this same format.

28: :ref:`Array<class_array>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For typed arrays, the header flags indicate the element type kind (see Header
Flags section). The container type is encoded the same way as Dictionary.

**Element count (immediately following type information, if any):**

+----------+-------+-----------+----------------------------------------------------------------------+
| Offset   | Len   | Type      | Description                                                          |
+==========+=======+===========+======================================================================+
| 0        | 4     | Integer   | val & 0x7FFFFFFF = element count, val & 0x80000000 = shared (bool)   |
+----------+-------+-----------+----------------------------------------------------------------------+

Then what follows is, for each element, a value encoded using this same format.

29: :ref:`PackedByteArray<class_PackedByteArray>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------+-------+-----------+------------------------+
| Offset        | Len   | Type      | Description            |
+===============+=======+===========+========================+
| 4             | 4     | Integer   | Array length (Bytes)   |
+---------------+-------+-----------+------------------------+
| 8..8+length   | 1     | Byte      | Byte (0..255)          |
+---------------+-------+-----------+------------------------+

The array data is padded to 4 bytes.

30: :ref:`PackedInt32Array<class_PackedInt32Array>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------+-------+-----------+---------------------------+
| Offset           | Len   | Type      | Description               |
+==================+=======+===========+===========================+
| 4                | 4     | Integer   | Array length (Integers)   |
+------------------+-------+-----------+---------------------------+
| 8..8+length\*4   | 4     | Integer   | 32-bit signed integer     |
+------------------+-------+-----------+---------------------------+

31: :ref:`PackedInt64Array<class_PackedInt64Array>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------+-------+-----------+---------------------------+
| Offset           | Len   | Type      | Description               |
+==================+=======+===========+===========================+
| 4                | 4     | Integer   | Array length (Integers)   |
+------------------+-------+-----------+---------------------------+
| 8..8+length\*8   | 8     | Integer   | 64-bit signed integer     |
+------------------+-------+-----------+---------------------------+

32: :ref:`PackedFloat32Array<class_PackedFloat32Array>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------+-------+-----------+-----------------------------------+
| Offset           | Len   | Type      | Description                       |
+==================+=======+===========+===================================+
| 4                | 4     | Integer   | Array length (Floats)             |
+------------------+-------+-----------+-----------------------------------+
| 8..8+length\*4   | 4     | Float     | IEEE 754 single-precision float   |
+------------------+-------+-----------+-----------------------------------+

33: :ref:`PackedFloat64Array<class_PackedFloat64Array>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------+-------+-----------+-----------------------------------+
| Offset           | Len   | Type      | Description                       |
+==================+=======+===========+===================================+
| 4                | 4     | Integer   | Array length (Floats)             |
+------------------+-------+-----------+-----------------------------------+
| 8..8+length\*8   | 8     | Float     | IEEE 754 double-precision float   |
+------------------+-------+-----------+-----------------------------------+

34: :ref:`PackedStringArray<class_PackedStringArray>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+-------+-----------+--------------------------+
| Offset   | Len   | Type      | Description              |
+==========+=======+===========+==========================+
| 4        | 4     | Integer   | Array length (Strings)   |
+----------+-------+-----------+--------------------------+

For each String (offsets relative to start of each string entry):

+----------+-------+-----------+----------------------------------------+
| Offset   | Len   | Type      | Description                            |
+==========+=======+===========+========================================+
| 0        | 4     | Integer   | String length (N, including null term) |
+----------+-------+-----------+----------------------------------------+
| 4        | N     | Bytes     | UTF-8 encoded string with null         |
+----------+-------+-----------+----------------------------------------+

Every string is padded to 4 bytes.

.. note::

   Unlike regular String encoding, PackedStringArray encodes strings with a
   null terminator included in the length.

35: :ref:`PackedVector2Array<class_PackedVector2Array>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If no flags are set (flags == 0), the floats are sent as 32 bit single precision:

+-------------------+-------+-----------+----------------+
| Offset            | Len   | Type      | Description    |
+===================+=======+===========+================+
| 4                 | 4     | Integer   | Array length   |
+-------------------+-------+-----------+----------------+
| 8+i\*8            | 4     | Float     | X coordinate   |
+-------------------+-------+-----------+----------------+
| 12+i\*8           | 4     | Float     | Y coordinate   |
+-------------------+-------+-----------+----------------+

If flag ``ENCODE_FLAG_64`` is set (flags & 1 == 1), the floats are sent as 64 bit double precision.

+-------------------+-------+-----------+----------------+
| Offset            | Len   | Type      | Description    |
+===================+=======+===========+================+
| 4                 | 4     | Integer   | Array length   |
+-------------------+-------+-----------+----------------+
| 8+i\*16           | 8     | Double    | X coordinate   |
+-------------------+-------+-----------+----------------+
| 16+i\*16          | 8     | Double    | Y coordinate   |
+-------------------+-------+-----------+----------------+

36: :ref:`PackedVector3Array<class_PackedVector3Array>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If no flags are set (flags == 0), the floats are sent as 32 bit single precision:

+--------------------+-------+-----------+----------------+
| Offset             | Len   | Type      | Description    |
+====================+=======+===========+================+
| 4                  | 4     | Integer   | Array length   |
+--------------------+-------+-----------+----------------+
| 8+i\*12            | 4     | Float     | X coordinate   |
+--------------------+-------+-----------+----------------+
| 12+i\*12           | 4     | Float     | Y coordinate   |
+--------------------+-------+-----------+----------------+
| 16+i\*12           | 4     | Float     | Z coordinate   |
+--------------------+-------+-----------+----------------+

If flag ``ENCODE_FLAG_64`` is set (flags & 1 == 1), the floats are sent as 64 bit double precision.

+--------------------+-------+-----------+----------------+
| Offset             | Len   | Type      | Description    |
+====================+=======+===========+================+
| 4                  | 4     | Integer   | Array length   |
+--------------------+-------+-----------+----------------+
| 8+i\*24            | 8     | Double    | X coordinate   |
+--------------------+-------+-----------+----------------+
| 16+i\*24           | 8     | Double    | Y coordinate   |
+--------------------+-------+-----------+----------------+
| 24+i\*24           | 8     | Double    | Z coordinate   |
+--------------------+-------+-----------+----------------+

37: :ref:`PackedColorArray<class_PackedColorArray>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------+-------+-----------+--------------------------------------------------------------+
| Offset             | Len   | Type      | Description                                                  |
+====================+=======+===========+==============================================================+
| 4                  | 4     | Integer   | Array length                                                 |
+--------------------+-------+-----------+--------------------------------------------------------------+
| 8+i\*16            | 4     | Float     | Red (typically 0..1, can be above 1 for overbright colors)   |
+--------------------+-------+-----------+--------------------------------------------------------------+
| 12+i\*16           | 4     | Float     | Green (typically 0..1, can be above 1 for overbright colors) |
+--------------------+-------+-----------+--------------------------------------------------------------+
| 16+i\*16           | 4     | Float     | Blue (typically 0..1, can be above 1 for overbright colors)  |
+--------------------+-------+-----------+--------------------------------------------------------------+
| 20+i\*16           | 4     | Float     | Alpha (0..1)                                                 |
+--------------------+-------+-----------+--------------------------------------------------------------+

.. note::

   Colors are always encoded in single precision.

38: :ref:`PackedVector4Array<class_PackedVector4Array>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If no flags are set (flags == 0), the floats are sent as 32 bit single precision:

+--------------------+-------+-----------+----------------+
| Offset             | Len   | Type      | Description    |
+====================+=======+===========+================+
| 4                  | 4     | Integer   | Array length   |
+--------------------+-------+-----------+----------------+
| 8+i\*16            | 4     | Float     | X coordinate   |
+--------------------+-------+-----------+----------------+
| 12+i\*16           | 4     | Float     | Y coordinate   |
+--------------------+-------+-----------+----------------+
| 16+i\*16           | 4     | Float     | Z coordinate   |
+--------------------+-------+-----------+----------------+
| 20+i\*16           | 4     | Float     | W coordinate   |
+--------------------+-------+-----------+----------------+

If flag ``ENCODE_FLAG_64`` is set (flags & 1 == 1), the floats are sent as 64 bit double precision.

+--------------------+-------+-----------+----------------+
| Offset             | Len   | Type      | Description    |
+====================+=======+===========+================+
| 4                  | 4     | Integer   | Array length   |
+--------------------+-------+-----------+----------------+
| 8+i\*32            | 8     | Double    | X coordinate   |
+--------------------+-------+-----------+----------------+
| 16+i\*32           | 8     | Double    | Y coordinate   |
+--------------------+-------+-----------+----------------+
| 24+i\*32           | 8     | Double    | Z coordinate   |
+--------------------+-------+-----------+----------------+
| 32+i\*32           | 8     | Double    | W coordinate   |
+--------------------+-------+-----------+----------------+
