.. _doc_c_sharp_collections:

C# collections
==============

The .NET base class library contains multiple collection types that can be
used to store and manipulate data. Godot also provide some collection types
that are tightly integrated with the rest of the engine.

Choose a collection
-------------------

The main difference between the `.NET collections <https://learn.microsoft.com/en-us/dotnet/standard/collections/>`_
and the Godot collections is that the .NET collections are implemented in C# while
the Godot collections are implemented in C++ and the Godot C# API is a wrapper over it,
this is an important distinction since it means every operation on a Godot collection
requires marshaling which can be expensive especially inside a loop.

Due to the performance implications, using Godot collections is only recommended
when absolutely necessary (such as interacting with the Godot API). Godot only
understands its own collection types, so it's required to use them when talking
to the engine.

If you have a collection of elements that don't need to be passed to a Godot API,
using a .NET collection would be more performant.

.. tip::

    It's also possible to convert between .NET collections and Godot collections.
    The Godot collections contain constructors from generic .NET collection interfaces
    that copy their elements, and the Godot collections can be used with the
    `LINQ <https://learn.microsoft.com/en-us/dotnet/standard/linq>`_
    ``ToList``, ``ToArray`` and ``ToDictionary`` methods. But keep in mind this conversion
    requires marshaling every element in the collection and copies it to a new collection
    so it can be expensive.

Despite this, the Godot collections are optimized to try and avoid unnecessary
marshaling, so methods like ``Sort`` or ``Reverse`` are implemented with a single
interop call and don't need to marshal every element. Keep an eye out for generic APIs
that take collection interfaces like `LINQ <https://learn.microsoft.com/en-us/dotnet/standard/linq>`_
because every method requires iterating the collection and, therefore, marshaling
every element. Prefer using the instance methods of the Godot collections when possible.

To choose which collection type to use for each situation, consider the following questions:

* Does your collection need to interact with the Godot engine?
  (e.g.: the type of an exported property, calling a Godot method).

   * If yes, since Godot only supports :ref:`c_sharp_variant_compatible_types`,
     use a Godot collection.
   * If not, consider `choosing an appropriate .NET collection <https://learn.microsoft.com/en-us/dotnet/standard/collections/selecting-a-collection-class>`_.

* Do you need a Godot collection that represents a list or sequential set of data?

   * Godot :ref:`arrays <doc_c_sharp_collections_array>` are similar to the C# collection ``List<T>``.
   * Godot :ref:`packed arrays <doc_c_sharp_collections_packedarray>` are more memory-efficient arrays,
     in C# use one of the supported ``System.Array`` types.

* Do you need a Godot collection that maps a set of keys to a set of values?

   * Godot :ref:`dictionaries <doc_c_sharp_collections_dictionary>` store pairs of keys and values
     and allow easy access to the values by their associated key.

Godot collections
-----------------

.. _doc_c_sharp_collections_packedarray:

PackedArray
^^^^^^^^^^^

Godot packed arrays are implemented as an array of a specific type, allowing it to be
more tightly packed as each element has the size of the specific type, not ``Variant``.

In C#, packed arrays are replaced by ``System.Array``:

======================  ==============================================================
GDScript                C#
======================  ==============================================================
``PackedByteArray``     ``byte[]``
``PackedInt32Array``    ``int[]``
``PackedInt64Array``    ``long[]``
``PackedFloat32Array``  ``float[]``
``PackedFloat64Array``  ``double[]``
``PackedStringArray``   ``string[]``
``PackedVector2Array``  ``Vector2[]``
``PackedVector3Array``  ``Vector3[]``
``PackedColorArray``    ``Color[]``
======================  ==============================================================

Other C# arrays are not supported by the Godot C# API since a packed array equivalent
does not exist. See the list of :ref:`c_sharp_variant_compatible_types`.

.. _doc_c_sharp_collections_array:

Array
^^^^^

Godot arrays are implemented as an array of ``Variant`` and can contain several elements
of any type. In C#, the equivalent type is ``Godot.Collections.Array``.

The generic ``Godot.Collections.Array<T>`` type allows restricting the element type to
a :ref:`Variant-compatible type <c_sharp_variant_compatible_types>`.

An untyped ``Godot.Collections.Array`` can be converted to a typed array using the
``Godot.Collections.Array<T>(Godot.Collections.Array)`` constructor.

.. note::

    Despite the name, Godot arrays are more similar to the C# collection
    ``List<T>`` than ``System.Array``. Their size is not fixed and can grow
    or shrink as elements are added/removed from the collection.

List of Godot's Array methods and their equivalent in C#:

=======================  ==============================================================
GDScript                 C#
=======================  ==============================================================
all                      `System.Linq.Enumerable.All`_
any                      `System.Linq.Enumerable.Any`_
append                   Add
append_array             AddRange
assign                   Clear and AddRange
back                     ``Array[^1]`` or `System.Linq.Enumerable.Last`_ or `System.Linq.Enumerable.LastOrDefault`_
bsearch                  BinarySearch
bsearch_custom           N/A
clear                    Clear
count                    `System.Linq.Enumerable.Count`_
duplicate                Duplicate
erase                    Remove
fill                     Fill
filter                   Use `System.Linq.Enumerable.Where`_
find                     IndexOf
front                    ``Array[0]`` or `System.Linq.Enumerable.First`_ or `System.Linq.Enumerable.FirstOrDefault`_
get_typed_builtin        N/A
get_typed_class_name     N/A
get_typed_script         N/A
has                      Contains
hash                     GD.Hash
insert                   Insert
is_empty                 Use ``Count == 0``
is_read_only             IsReadOnly
is_same_typed            N/A
is_typed                 N/A
make_read_only           MakeReadOnly
map                      `System.Linq.Enumerable.Select`_
max                      Max
min                      Min
pick_random              PickRandom (Consider using `System.Random`_)
pop_at                   ``Array[i]`` with ``RemoveAt(i)``
pop_back                 ``Array[^1]`` with ``RemoveAt(Count - 1)``
pop_front                ``Array[0]`` with ``RemoveAt(0)``
push_back                ``Insert(Count, item)``
push_front               ``Insert(0, item)``
reduce                   `System.Linq.Enumerable.Aggregate`_
remove_at                RemoveAt
resize                   Resize
reverse                  Reverse
rfind                    LastIndexOf
shuffle                  Shuffle
size                     Count
slice                    Slice
sort                     Sort
sort_custom              `System.Linq.Enumerable.OrderBy`_
operator !=              !RecursiveEqual
operator +               operator +
operator <               N/A
operator <=              N/A
operator ==              RecursiveEqual
operator >               N/A
operator >=              N/A
operator []              Array[int] indexer
=======================  ==============================================================

.. _System.Random: https://learn.microsoft.com/en-us/dotnet/api/system.random
.. _System.Linq.Enumerable.Aggregate: https://learn.microsoft.com/en-us/dotnet/api/system.linq.enumerable.aggregate
.. _System.Linq.Enumerable.All: https://learn.microsoft.com/en-us/dotnet/api/system.linq.enumerable.all
.. _System.Linq.Enumerable.Any: https://learn.microsoft.com/en-us/dotnet/api/system.linq.enumerable.any
.. _System.Linq.Enumerable.Count: https://learn.microsoft.com/en-us/dotnet/api/system.linq.enumerable.count
.. _System.Linq.Enumerable.First: https://learn.microsoft.com/en-us/dotnet/api/system.linq.enumerable.first
.. _System.Linq.Enumerable.FirstOrDefault: https://learn.microsoft.com/en-us/dotnet/api/system.linq.enumerable.firstordefault
.. _System.Linq.Enumerable.Last: https://learn.microsoft.com/en-us/dotnet/api/system.linq.enumerable.last
.. _System.Linq.Enumerable.LastOrDefault: https://learn.microsoft.com/en-us/dotnet/api/system.linq.enumerable.lastordefault
.. _System.Linq.Enumerable.OrderBy: https://learn.microsoft.com/en-us/dotnet/api/system.linq.enumerable.orderby
.. _System.Linq.Enumerable.Select: https://learn.microsoft.com/en-us/dotnet/api/system.linq.enumerable.select
.. _System.Linq.Enumerable.Where: https://learn.microsoft.com/en-us/dotnet/api/system.linq.enumerable.where

.. _doc_c_sharp_collections_dictionary:

Dictionary
^^^^^^^^^^

Godot dictionaries are implemented as a dictionary with ``Variant`` keys and values.
In C#, the equivalent type is ``Godot.Collections.Dictionary``.

The generic ``Godot.Collections.Dictionary<TKey, TValue>`` type allows restricting the key
and value types to a :ref:`Variant-compatible type <c_sharp_variant_compatible_types>`.

An untyped ``Godot.Collections.Dictionary`` can be converted to a typed dictionary using the
``Godot.Collections.Dictionary<TKey, TValue>(Godot.Collections.Dictionary)`` constructor.

.. tip::

    If you need a dictionary where the key is typed but not the value, use
    ``Variant`` as the ``TValue`` generic parameter of the typed dictionary.

    .. code-block:: csharp

        // The keys must be string, but the values can be any Variant-compatible type.
        var dictionary = new Godot.Collections.Dictionary<string, Variant>();

List of Godot's Dictionary methods and their equivalent in C#:

=======================  ==============================================================
GDScript                 C#
=======================  ==============================================================
clear                    Clear
duplicate                Duplicate
erase                    Remove
find_key                 N/A
get                      Dictionary[Variant] indexer or TryGetValue
has                      ContainsKey
has_all                  N/A
hash                     GD.Hash
is_empty                 Use ``Count == 0``
is_read_only             IsReadOnly
keys                     Keys
make_read_only           MakeReadOnly
merge                    Merge
size                     Count
values                   Values
operator !=              !RecursiveEqual
operator ==              RecursiveEqual
operator []              Dictionary[Variant] indexer, Add or TryGetValue
=======================  ==============================================================
