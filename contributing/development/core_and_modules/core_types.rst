.. _doc_core_types:

Core types
==========

Godot has a rich set of classes and templates that compose its core,
and everything is built upon them.

This reference will try to list them in order for their better
understanding.

Definitions
-----------

Godot uses the standard C99 datatypes, such as ``uint8_t``,
``uint32_t``, ``int64_t``, etc. which are nowadays supported by every
compiler. Reinventing the wheel for those is not fun, as it makes code
more difficult to read.

In general, care is not taken to use the most efficient datatype for a
given task unless using large structures or arrays. ``int`` is used
through most of the code unless necessary. This is done because nowadays
every device has at least a 32 bits bus and can do such operations in
one cycle. It makes code more readable too.

For files or memory sizes, ``size_t`` is used, which is warranted to be
64 bits.

For Unicode characters, CharType instead of wchar_t is used, because
many architectures have 4 bytes long wchar_t, where 2 bytes might be
desired. However, by default, this has not been forced and CharType maps
directly to wchar_t.

References:
~~~~~~~~~~~

-  `core/typedefs.h <https://github.com/godotengine/godot/blob/master/core/typedefs.h>`__

Memory model
------------

PC is a wonderful architecture. Computers often have gigabytes of RAM,
terabytes of storage and gigahertz of CPU, and when an application needs
more resources the OS will swap out the inactive ones. Other
architectures (like mobile or consoles) are in general more limited.

The most common memory model is the heap, where an application will
request a region of memory, and the underlying OS will try to fit it
somewhere and return it. This often works best and is flexible,
but over time and with abuse, this can lead to segmentation.

Segmentation slowly creates holes that are too small for most common
allocations, so that memory is wasted. There is a lot of literature
about heap and segmentation, so this topic will not be developed
further here. Modern operating systems use paged memory, which helps
mitigate the problem of segmentation but doesn't solve it.

However, in many studies and tests, it is shown that given enough
memory, if the maximum allocation size is below a given threshold in
proportion to the maximum heap size and proportion of memory intended to
be unused, segmentation will not be a problem over time as it will
remain constant. In other words, leave 10-20% of your memory free
and perform all small allocations and you are fine.

Godot ensures that all objects that can be allocated dynamically are
small (less than a few kb at most). But what happens if an allocation is
too large (like an image or mesh geometry or large array)? In this case
Godot has the option to use a dynamic memory pool. This memory needs to
be locked to be accessed, and if an allocation runs out of memory, the
pool will be rearranged and compacted on demand. Depending on the need
of the game, the programmer can configure the dynamic memory pool size.

Allocating memory
-----------------

Godot has many tools for tracking memory usage in a game, especially
during debug. Because of this, the regular C and C++ library calls
should not be used. Instead, a few other ones are provided.

For C-style allocation, Godot provides a few macros:

.. code-block:: none

    memalloc()
    memrealloc()
    memfree()

These are equivalent to the usual malloc, realloc, free of the standard C
library.

For C++-style allocation, special macros are provided:

.. code-block:: none

    memnew( Class / Class(args) )
    memdelete( instance )

    memnew_arr( Class , amount )
    memdelete_arr( pointer to array )

which are equivalent to new, delete, new[] and delete[].

memnew/memdelete also use a little C++ magic and notify Objects right
after they are created, and right before they are deleted.

For dynamic memory, use one of Godot's sequence types such as ``Vector<>``
or ``LocalVector<>``. ``Vector<>`` behaves much like an STL ``std::vector<>``,
but is simpler and uses Copy-On-Write (CoW) semantics. CoW copies of
``Vector<>`` can safely access the same data from different threads, but
several threads cannot access the same ``Vector<>`` instance safely.
It can be safely passed via public API if it has a ``Packed`` alias.

The ``Packed*Array`` :ref:`types <doc_gdscript_packed_arrays>` are aliases
for specific ``Vector<*>`` types (e.g., ``PackedByteArray``,
``PackedInt32Array``) that are accessible via GDScript. Outside of core,
prefer using the ``Packed*Array`` aliases for functions exposed to scripts,
and ``Vector<>`` for other occasions.

``LocalVector<>`` is much more like ``std::vector`` than ``Vector<>``.
It is non-CoW, with less overhead. It is intended for internal use where
the benefits of CoW are not needed. Note that neither ``LocalVector<>``
nor ``Vector<>`` are drop-in replacements for each other. They are two
unrelated types with similar interfaces, both using a buffer as their
storage strategy.

``List<>`` is another Godot sequence type, using a doubly-linked list as
its storage strategy. Prefer ``Vector<>`` (or ``LocalVector<>``) over
``List<>`` unless you're sure you need it, as cache locality and memory
fragmentation tend to be more important with small collections.

References:
~~~~~~~~~~~

-  `core/os/memory.h <https://github.com/godotengine/godot/blob/master/core/os/memory.h>`__

Containers
----------

Godot provides also a set of common containers:

-  Vector
-  List
-  Set
-  Map

They aim to be as minimal as possible, as templates
in C++ are often inlined and make the binary size much fatter, both in
debug symbols and code. List, Set and Map can be iterated using
pointers, like this:

.. code-block:: cpp

    for(List<int>::Element *E=somelist.front();E;E=E->next()) {
        print_line(E->get()); // print the element
    }

The Vector<> class also has a few nice features:

-  It does copy on write, so making copies of it is cheap as long as
   they are not modified.
-  It supports multi-threading, by using atomic operations on the
   reference counter.

References:
~~~~~~~~~~~

-  `core/templates/vector.h <https://github.com/godotengine/godot/blob/master/core/templates/vector.h>`__
-  `core/templates/list.h <https://github.com/godotengine/godot/blob/master/core/templates/list.h>`__
-  `core/templates/set.h <https://github.com/godotengine/godot/blob/master/core/templates/hash_set.h>`__
-  `core/templates/map.h <https://github.com/godotengine/godot/blob/master/core/templates/hash_map.h>`__

String
------

Godot also provides a String class. This class has a huge amount of
features, full Unicode support in all the functions (like case
operations) and utf8 parsing/extracting, as well as helpers for
conversion and visualization.

References:
~~~~~~~~~~~

-  `core/string/ustring.h <https://github.com/godotengine/godot/blob/master/core/string/ustring.h>`__

StringName
----------

StringNames are like a String, but they are unique. Creating a
StringName from a string results in a unique internal pointer for all
equal strings. StringNames are useful for using strings as
identifier, as comparing them is basically comparing a pointer.

Creation of a StringName (especially a new one) is slow, but comparison
is fast.

References:
~~~~~~~~~~~

-  `core/string/string_name.h <https://github.com/godotengine/godot/blob/master/core/string/string_name.h>`__

Math types
----------

There are several linear math types available in the core/math
directory.

References:
~~~~~~~~~~~

-  `core/math <https://github.com/godotengine/godot/tree/master/core/math>`__

NodePath
--------

This is a special datatype used for storing paths in a scene tree and
referencing them fast.

References:
~~~~~~~~~~~

-  `core/string/node_path.h <https://github.com/godotengine/godot/blob/master/core/string/node_path.h>`__

RID
---

RIDs are resource IDs. Servers use these to reference data stored in
them. RIDs are opaque, meaning that the data they reference can't be
accessed directly. RIDs are unique, even for different types of
referenced data.

References:
~~~~~~~~~~~

-  `core/templates/rid.h <https://github.com/godotengine/godot/blob/master/core/templates/rid.h>`__
