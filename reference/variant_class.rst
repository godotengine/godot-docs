.. _doc_variant_class:

Variant class
=============

About
-----

Variant is the most important datatype of Godot, it's the most important
class in the engine. A Variant takes up only 20 bytes and can store
almost any engine datatype inside of it. Variants are rarely used to
hold information for long periods of time, instead they are used mainly
for communication, editing, serialization and generally moving data
around.

A Variant can:

-  Store almost any datatype
-  Perform operations between many variants (GDScript uses Variant as
   it's atomic/native datatype).
-  Be hashed, so it can be compared quickly to over variants
-  Be used to convert safely between datatypes
-  Be used to abstract calling methods and their arguments (Godot
   exports all it's functions through variants)
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

References:
~~~~~~~~~~~

-  `core/variant.h <https://github.com/godotengine/godot/blob/master/core/variant.h>`__

Dictionary and Array
--------------------

Both are implemented using variants. A Dictionary can match any datatype
used as key to any other datatype. An Array just holds an array of
Variants. Of course, a Variant can also hold a Dictionary and an Array
inside, making it even more flexible.

Both have a shared mode and a COW mode. Scripts often use them in shared
mode (meaning modifications to a container will modify all references to
it), or COW mode (modifications will always alter the local copy, making
a copy of the internal data if necessary, but will not affect the other
copies). In COW mode, Both Dictionary and Array are thread-safe,
otherwise a Mutex should be created to lock if multi thread access is
desired.

References:
~~~~~~~~~~~

-  `core/dictionary.h <https://github.com/godotengine/godot/blob/master/core/dictionary.h>`__
-  `core/array.h <https://github.com/godotengine/godot/blob/master/core/array.h>`__
