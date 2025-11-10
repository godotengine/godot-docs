.. _doc_core_types:

Core types
==========

Godot has a rich set of classes and templates that compose its core,
and everything is built upon them.

This reference will try to list them in order for their better
understanding.

Allocating memory
-----------------

Godot has many tricks for ensuring memory safety and tracking memory
usage. Because of this, the regular C and C++ library calls
should not be used. Instead, a few replacements are provided.

For C-style allocation, Godot provides a few macros:

.. code-block:: cpp

    memalloc(size)
    memrealloc(pointer)
    memfree(pointer)

These are equivalent to the usual ``malloc()``, ``realloc()``, and ``free()``
of the C standard library.

For C++-style allocation, special macros are provided:

.. code-block:: cpp

    memnew(Class)
    memnew(Class(args))
    memdelete(instance)

    memnew_arr(Class, amount)
    memdelete_arr(pointer_to_array)

These are equivalent to ``new``, ``delete``, ``new[]``, and ``delete[]``
respectively.

``memnew``/``memdelete`` also use a little C++ magic to automatically call post-init
and pre-release functions. For example, this is used to notify Objects right after
they are created, and right before they are deleted.

-  `core/os/memory.h <https://github.com/godotengine/godot/blob/master/core/os/memory.h>`__

Containers
----------

Godot provides its own set of containers, which means STL containers like ``std::string``
and ``std::vector`` are generally not used in the codebase. See :ref:`doc_faq_why_not_stl` for more information.

A 📜 icon denotes the type is part of :ref:`Variant <doc_variant_class>`. This
means it can be used as a parameter or return value of a method exposed to the
scripting API.

+-----------------------+--------------------------+---------------------------------------------------------------------------------------+
| Godot datatype        | Closest C++ STL datatype | Comment                                                                               |
+=======================+==========================+=======================================================================================+
| |string| 📜           | ``std::string``          | **Use this as the "default" string type.** ``String`` uses UTF-32 encoding            |
|                       |                          | to simplify processing thanks to its fixed character size.                            |
+-----------------------+--------------------------+---------------------------------------------------------------------------------------+
| |vector|              | ``std::vector``          | **Use this as the "default" vector type.** Uses copy-on-write (COW) semantics.        |
|                       |                          | This means it's generally slower but can be copied around almost for free.            |
|                       |                          | Use ``LocalVector`` instead where COW isn't needed and performance matters.           |
+-----------------------+--------------------------+---------------------------------------------------------------------------------------+
| |hash_set|            | ``std::unordered_set``   | **Use this as the "default" set type.**                                               |
+-----------------------+--------------------------+---------------------------------------------------------------------------------------+
| |a_hash_map|          | ``std::unordered_map``   | **Use this as the "default" map type.** Does not preserve insertion order.            |
|                       |                          | Note that pointers into the map, as well as iterators, are not stable under mutations.|
|                       |                          | If either of these affordances are needed, use ``HashMap`` instead.                   |
+-----------------------+--------------------------+---------------------------------------------------------------------------------------+
| |string_name| 📜      | ``std::string``          | Uses string interning for fast comparisons. Use this for static strings that are      |
|                       |                          | referenced frequently and used in multiple locations in the engine.                   |
+-----------------------+--------------------------+---------------------------------------------------------------------------------------+
| |local_vector|        | ``std::vector``          | Closer to ``std::vector`` in semantics, doesn't use copy-on-write (COW) thus it's     |
|                       |                          | faster than ``Vector``. Prefer it over ``Vector`` when copying it cheaply             |
|                       |                          | is not needed.                                                                        |
+-----------------------+--------------------------+---------------------------------------------------------------------------------------+
| |array| 📜            | ``std::vector``          | Values can be of any Variant type. No static typing is imposed.                       |
|                       |                          | Uses shared reference counting, similar to ``std::shared_ptr``.                       |
|                       |                          | Uses Vector<Variant> internally.                                                      |
+-----------------------+--------------------------+---------------------------------------------------------------------------------------+
| |typed_array| 📜      | ``std::vector``          | Subclass of ``Array`` but with static typing for its elements.                        |
|                       |                          | Not to be confused with ``Packed*Array``, which is internally a ``Vector``.           |
+-----------------------+--------------------------+---------------------------------------------------------------------------------------+
| |packed_array| 📜     | ``std::vector``          | Alias of ``Vector``, e.g. ``PackedColorArray = Vector<Color>``.                       |
|                       |                          | Only a limited list of packed array types are available                               |
|                       |                          | (use ``TypedArray`` otherwise).                                                       |
+-----------------------+--------------------------+---------------------------------------------------------------------------------------+
| |list|                | ``std::list``            | Linked list type. Generally slower than other array/vector types. Prefer using        |
|                       |                          | other types in new code, unless using ``List`` avoids the need for type conversions.  |
+-----------------------+--------------------------+---------------------------------------------------------------------------------------+
| |fixed_vector|        | ``std::array``           | Vector with a fixed capacity (more similar to ``boost::container::static_vector``).   |
|                       |                          | This container type is more efficient than other vector-like types because it makes   |
|                       |                          | no heap allocations.                                                                  |
+-----------------------+--------------------------+---------------------------------------------------------------------------------------+
| |span|                | ``std::span``            | Represents read-only access to a contiguous array without needing to copy any data.   |
|                       |                          | Note that ``Span`` is designed to be a high performance API: It does not perform      |
|                       |                          | parameter correctness checks in the same way you might be used to with other Godot    |
|                       |                          | containers. Use with care.                                                            |
|                       |                          | `Span` can be constructed from most array-like containers (e.g. ``vector.span()``).   |
+-----------------------+--------------------------+---------------------------------------------------------------------------------------+
| |rb_set|              | ``std::set``             | Uses a `red-black tree <https://en.wikipedia.org/wiki/Red-black_tree>`__              |
|                       |                          | for faster access.                                                                    |
+-----------------------+--------------------------+---------------------------------------------------------------------------------------+
| |v_set|               | ``std::flat_set``        | Uses copy-on-write (COW) semantics.                                                   |
|                       |                          | This means it's generally slower but can be copied around almost for free.            |
|                       |                          | The performance benefits of ``VSet`` aren't established, so prefer using other types. |
+-----------------------+--------------------------+---------------------------------------------------------------------------------------+
| |hash_map|            | ``std::unordered_map``   | Defensive (robust but slow) map type. Preserves insertion order.                      |
|                       |                          | Pointers to keys and values, as well as iterators, are stable under mutation.         |
|                       |                          | Use this map type when either of these affordances are needed. Use ``AHashMap``       |
|                       |                          | otherwise.                                                                            |
+-----------------------+--------------------------+---------------------------------------------------------------------------------------+
| |rb_map|              | ``std::map``             | Map type that uses a                                                                  |
|                       |                          | `red-black tree <https://en.wikipedia.org/wiki/Red-black-tree>`__ to find keys.       |
|                       |                          | The performance benefits of ``RBMap`` aren't established, so prefer using other types.|
+-----------------------+--------------------------+---------------------------------------------------------------------------------------+
| |dictionary| 📜       | ``std::unordered_map``   | Keys and values can be of any Variant type. No static typing is imposed.              |
|                       |                          | Uses shared reference counting, similar to ``std::shared_ptr``.                       |
|                       |                          | Preserves insertion order. Uses ``HashMap<Variant>`` internally.                      |
+-----------------------+--------------------------+---------------------------------------------------------------------------------------+
| |typed_dictionary| 📜 | ``std::unordered_map``   | Subclass of ``Dictionary`` but with static typing for its keys and values.            |
+-----------------------+--------------------------+---------------------------------------------------------------------------------------+
| |pair|                | ``std::pair``            | Stores a single pair. See also ``KeyValue`` in the same file, which uses read-only    |
|                       |                          | keys.                                                                                 |
+-----------------------+--------------------------+---------------------------------------------------------------------------------------+

.. |string| replace:: `String <https://github.com/godotengine/godot/blob/master/core/string/ustring.h>`__
.. |vector| replace:: `Vector <https://github.com/godotengine/godot/blob/master/core/templates/vector.h>`__
.. |hash_set| replace:: `HashSet <https://github.com/godotengine/godot/blob/master/core/templates/hash_set.h>`__
.. |hash_map| replace:: `HashMap <https://github.com/godotengine/godot/blob/master/core/templates/hash_map.h>`__
.. |string_name| replace:: `StringName <https://github.com/godotengine/godot/blob/master/core/string/string_name.h>`__
.. |local_vector| replace:: `LocalVector <https://github.com/godotengine/godot/blob/master/core/templates/local_vector.h>`__
.. |array| replace:: `Array <https://github.com/godotengine/godot/blob/master/core/variant/array.h>`__
.. |typed_array| replace:: `TypedArray <https://github.com/godotengine/godot/blob/master/core/variant/typed_array.h>`__
.. |packed_array| replace:: `Packed*Array <https://github.com/godotengine/godot/blob/master/core/variant/variant.h>`__
.. |list| replace:: `List <https://github.com/godotengine/godot/blob/master/core/templates/list.h>`__
.. |fixed_vector| replace:: `FixedVector <https://github.com/godotengine/godot/blob/master/core/templates/fixed_vector.h>`__
.. |span| replace:: `Span <https://github.com/godotengine/godot/blob/master/core/templates/span.h>`__
.. |rb_set| replace:: `RBSet <https://github.com/godotengine/godot/blob/master/core/templates/rb_set.h>`__
.. |v_set| replace:: `VSet <https://github.com/godotengine/godot/blob/master/core/templates/vset.h>`__
.. |a_hash_map| replace:: `AHashMap <https://github.com/godotengine/godot/blob/master/core/templates/a_hash_map.h>`__
.. |rb_map| replace:: `RBMap <https://github.com/godotengine/godot/blob/master/core/templates/rb_map.h>`__
.. |dictionary| replace:: `Dictionary <https://github.com/godotengine/godot/blob/master/core/variant/dictionary.h>`__
.. |typed_dictionary| replace:: `TypedDictionary <https://github.com/godotengine/godot/blob/master/core/variant/typed_dictionary.h>`__
.. |pair| replace:: `Pair <https://github.com/godotengine/godot/blob/master/core/templates/pair.h>`__

.. _doc_core_concurrency_types:

Multithreading / Concurrency
----------------------------

.. seealso::

    You can find more information on multithreading strategies at :ref:`doc_using_multiple_threads`.

None of Godot's containers are thread-safe. When you expect multiple threads to access them, you must use multithread
protections.

Note that some of the types listed here are also available through the bindings, but the binding types are wrapped with
:ref:`class_RefCounted` (found in the ``CoreBind::`` namespace). Prefer the primitives listed here when possible, for
efficiency reasons.

+-----------------------+------------------------------+---------------------------------------------------------------------------------------+
| Godot datatype        | Closest C++ STL datatype     | Comment                                                                               |
+=======================+==============================+=======================================================================================+
| |mutex|               | ``std::recursive_mutex``     | Recursive mutex type. Use ``MutexLock lock(mutex)`` to lock it.                       |
+-----------------------+------------------------------+---------------------------------------------------------------------------------------+
| |binary_mutex|        | ``std::mutex``               | Non-recursive mutex type. Use ``MutexLock lock(mutex)`` to lock it.                   |
+-----------------------+------------------------------+---------------------------------------------------------------------------------------+
| |rw_lock|             | ``std::shared_timed_mutex``  | Read-write aware mutex type. Use ``RWLockRead lock(mutex)`` or                        |
|                       |                              | ``RWLockWrite lock(mutex)`` to lock it.                                               |
+-----------------------+------------------------------+---------------------------------------------------------------------------------------+
| |safe_binary_mutex|   | ``std::mutex``               | Recursive mutex type that can be used with ``ConditionVariable``.                     |
|                       |                              | Use ``MutexLock lock(mutex)`` to lock it.                                             |
+-----------------------+------------------------------+---------------------------------------------------------------------------------------+
| |condition_variable|  | ``std::condition_variable``  | Condition variable type, used with ``SafeBinaryMutex``.                               |
+-----------------------+------------------------------+---------------------------------------------------------------------------------------+
| |semaphore|           | ``std::counting_semaphore``  | Counting semaphore type.                                                              |
+-----------------------+------------------------------+---------------------------------------------------------------------------------------+
| |safe_numeric|        | ``std::atomic``              | Templated atomic type, designed for numbers.                                          |
+-----------------------+------------------------------+---------------------------------------------------------------------------------------+
| |safe_flag|           | ``std::atomic_bool``         | Bool atomic type.                                                                     |
+-----------------------+------------------------------+---------------------------------------------------------------------------------------+
| |safe_ref_count|      | ``std::atomic``              | Atomic type designed for reference counting. Will refuse to increment the             |
|                       |                              | reference count if it is 0.                                                           |
+-----------------------+------------------------------+---------------------------------------------------------------------------------------+

.. |mutex| replace:: `Mutex <https://github.com/godotengine/godot/blob/master/core/os/mutex.h>`__
.. |binary_mutex| replace:: `BinaryMutex <https://github.com/godotengine/godot/blob/master/core/os/mutex.h>`__
.. |rw_lock| replace:: `RWLock <https://github.com/godotengine/godot/blob/master/core/os/rw_lock.h>`__
.. |safe_binary_mutex| replace:: `SafeBinaryMutex <https://github.com/godotengine/godot/blob/master/core/os/safe_binary_mutex.h>`__
.. |condition_variable| replace:: `ConditionVariable <https://github.com/godotengine/godot/blob/master/core/os/condition_variable.h>`__
.. |semaphore| replace:: `Semaphore <https://github.com/godotengine/godot/blob/master/core/os/semaphore.h>`__
.. |safe_numeric| replace:: `SafeNumeric <https://github.com/godotengine/godot/blob/master/core/templates/safe_refcount.h>`__
.. |safe_flag| replace:: `SafeFlag <https://github.com/godotengine/godot/blob/master/core/templates/safe_refcount.h>`__
.. |safe_ref_count| replace:: `SafeRefCount <https://github.com/godotengine/godot/blob/master/core/templates/safe_refcount.h>`__

Math types
----------

There are several linear math types available in the ``core/math``
directory:

-  `core/math <https://github.com/godotengine/godot/tree/master/core/math>`__

NodePath
--------

This is a special datatype used for storing paths in a scene tree and
referencing them in an optimized manner:

-  `core/string/node_path.h <https://github.com/godotengine/godot/blob/master/core/string/node_path.h>`__

RID
---

RIDs are *Resource IDs*. Servers use these to reference data stored in
them. RIDs are opaque, meaning that the data they reference can't be
accessed directly. RIDs are unique, even for different types of
referenced data:

-  `core/templates/rid.h <https://github.com/godotengine/godot/blob/master/core/templates/rid.h>`__
