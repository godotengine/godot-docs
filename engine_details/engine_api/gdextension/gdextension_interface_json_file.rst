.. _doc_gdextension_interface_json_file:

The C interface JSON file
=========================

The ``gdextension_interface.json`` file is the "source of truth" for the C API that
Godot uses to communicate with GDExtensions.

You can use the Godot executable to dump the file by using the following command:

.. code-block:: shell

    godot --headless --dump-gdextension-interface-json

This file is intended to be used by GDExtension language bindings to generate code for
using this API in whatever form makes the most sense for that language.

.. note::

    This is not to be confused with the ``extension_api.json``, which is also used by
    GDExtension language bindings, and contains information about the classes and
    methods that are exposed by Godot. The ``gdextension_interface.json`` is more
    low-level, and is used to interact with those higher-level classes and methods.

For languages that can be extended via C, or provide tools for interacting with C code,
it's also possible to use the Godot executable to dump a generated C header file:

.. code-block:: shell

    godot --headless --dump-gdextension-interface

.. note::

    The header file is compatible with earlier versions of the header file that were included
    with Godot 4.5 and earlier, which means it preserves some typos in names in order to
    ensure compatibility.

The goal of this page is to explain the JSON format for the GDExtension language bindings that
would like to do their own code generation from the JSON.

Overall structure
-----------------

The JSON file is broken up into 3 sections:

- The header, which includes some miscellaneous information at the top-level of the JSON file.
- The ``types`` key, which defines all the types used in the GDExtension interface.
- The ``interface`` key, which defines all the function pointers that can be loaded via the
  ``GDExtensionInterfaceGetProcAddress`` function pointer, which is passed to all GDExtensions
  when they are loaded.

There is a complete `JSON schema <https://github.com/godotengine/godot/blob/master/core/extension/gdextension_interface.schema.json>`__
included in Godot's source code.

Even though we may add new types and interface functions with each minor release of Godot, we
strive to **never** change them in a backwards incompatible way, or remove them. Every
interface function is labeled with the version of Godot it was introduced in (the ``since``
key), so you can always use the latest version of the file, and simply refrain from using
anything in versions of Godot that are newer than the version you are targeting.

Header
------

The "header" is made up of 3 miscellaneous keys at the top-level of the file:

- ``_copyright``: The standard copyright and license text that Godot includes in all source
  code files.
- ``$schema``: Points to the JSON schema relative to this file. It can be useful to place
  the schema in the same directory, if you're viewing it with a code editor that understands
  JSON schema.
- ``format_version``: An integer for the version of the file format (meaning the schema).
  Right now, there is only one format version (``1``). If we ever change the file format in
  an incompatible way, we will increment this number. This *doesn't* reflect the version
  of the data in the file (so it won't change between Godot versions), only its format.
  Hopefully, we'll never have to use it, but it allows code generators to error early if they
  encounter an unexpected value here.

Types
-----

The ``types`` section is an array of types that will be used by other types, and the interface
functions that will be in the last section.

The types should be evaluated in order. Later types may refer to earlier types, but earlier
types will not refer to later types.

There is a small set of built-in types which aren't explicitly listed in the JSON:

- ``void``
- ``int8_t``
- ``uint8_t``
- ``int16_t``
- ``uint16_t``
- ``int32_t``
- ``uint32_t``
- ``int64_t``
- ``uint64_t``
- ``size_t`` (``uint32_t`` on 32-bit architectures, and ``uint64_t`` on 64-bit architectures)
- ``char``
- ``char16_t``
- ``char32_t``
- ``wchar_t``
- ``float``
- ``double``

These correspond to their equivalent C types.

Additionally, types can include modifiers such as:

- ``*`` (e.g. ``int8_t*``) to indicate a pointer to the type
- ``const`` (e.g. ``const int8_t*``) to indicate a const type

Each type defined in the JSON file falls into one of 5 "kinds":

- ``enum``
- ``handle``
- ``alias``
- ``struct``
- ``function``

Regardless of the "kind", all types can have the following keys:

- ``kind`` (required): The type's "kind".
- ``name`` (required): The name of the type, which could be used as a valid C identifier.
- ``description``: An array of strings documenting the type, where each string is a line of
  documentation (this format for ``description`` is used throughout the JSON file).
- ``deprecated``: An object with its own keys for the Godot version the type was deprecated in
  (``since``), a message explaining the deprecation (``message``), and optionally a replacement
  to use instead (``replacement``).

Enums
~~~~~

Enums are 32-bit integers with a fixed set of possible values. In C, they could be represented
as an ``enum``.

They have the following keys:

- ``is_bitfield``: If true, this enum is a bitfield, where the enum values can be bitwise OR'd together.
  It is false by default.
- ``values``: The array of fixed values for this enum, each with a ``name``, ``value``, and ``description``.

An enum should be represented as an ``int32_t``, unless ``is_bitfield`` is true, in which case a ``uint32_t``
should be used.

Example
+++++++

.. code-block:: json

    {
        "name": "GDExtensionInitializationLevel",
        "kind": "enum",
        "values": [
            {
                "name": "GDEXTENSION_INITIALIZATION_CORE",
                "value": 0
            },
            {
                "name": "GDEXTENSION_INITIALIZATION_SERVERS",
                "value": 1
            },
            {
                "name": "GDEXTENSION_INITIALIZATION_SCENE",
                "value": 2
            },
            {
                "name": "GDEXTENSION_INITIALIZATION_EDITOR",
                "value": 3
            },
            {
                "name": "GDEXTENSION_MAX_INITIALIZATION_LEVEL",
                "value": 4
            }
        ]
    }

Handles
~~~~~~~

Handles are pointers to opaque structs. In C, they could be represented as ``void *`` or ``struct{} *``.

They have the following keys:

- ``is_const``: If true, this handle type is to be treated as a "const pointer", meaning its internal
  data will not be changed. It is false by default.
- ``is_uninitialized``: If true, this handle type is to be treated as pointing to uninitialized memory
  (which may be initialized using interface functions). It is false by default.
- ``parent``: The optional name of another handle type, if this handle type is the const or uninitialized
  version of the parent type. This only makes sense if either ``is_const`` or ``is_uninitialized`` is true.

Handles are the size of pointers on the given architecture (so, 64-bit on x86_64 and 32-bit on x86_32,
for example).

Example
+++++++

.. code-block:: json

    {
        "name": "GDExtensionStringNamePtr",
        "kind": "handle"
    }

Aliases
~~~~~~~

Aliases are alternative names for a type. In C, they could be represented as a ``typedef``.

They have only one additional key:

- ``type``: The type the alias is an alternative name for. It may include modifiers as described above.

These should be represented using the same C type as the type they refer to.

Example
+++++++

.. code-block:: json

    {
        "name": "GDExtensionInt",
        "kind": "alias",
        "type": "int64_t"
    }

Structs
~~~~~~~

Structs represent C ``struct``\ s (aka a block of memory made up of the given members in order), and should
follow all the same layout and alignment rules as C structs.

They have only one additional key:

- ``members``: An array of objects which have a ``name``, ``type`` (which may include modifiers), and
  ``description``.

Example
+++++++

.. code-block:: json

    {
        "name": "GDExtensionCallError",
        "kind": "struct",
        "members": [
            {
                "name": "error",
                "type": "GDExtensionCallErrorType"
            },
            {
                "name": "argument",
                "type": "int32_t"
            },
            {
                "name": "expected",
                "type": "int32_t"
            }
        ]
    }

Functions
~~~~~~~~~

Functions represent C function pointer types, with a list of arguments and a return type, and should
follow the same size and alignment requirements as C function pointers.

They have the following members:

- ``return_value``: An object which has a ``type`` (which may include modifiers) and ``description``.
  If the function has no return value, this will be omitted.
- ``arguments`` (required): An array of function arguments which each has a ``type`` (which may include modifiers),
  ``name``, and ``description``.


Example
+++++++

.. code-block:: json

    {
        "name": "GDExtensionPtrConstructor",
        "kind": "function",
        "arguments": [
            {
                "name": "p_base",
                "type": "GDExtensionUninitializedTypePtr"
            },
            {
                "name": "p_args",
                "type": "const GDExtensionConstTypePtr*"
            }
        ]
    }

Interface
---------

The ``interface`` section of the JSON file is the list of interface functions, which can be loaded
by ``name`` using the ``GDExtensionInterfaceGetProcAddress`` function pointer, which is
passed to all GDExtensions when they are loaded.

Interface functions have some of the same keys as types, including ``name`` (required),
``deprecated``, and ``description``.

And they also have ``return_value`` and ``arguments`` (required) that have the same format
as the equivalent keys on function types (as described in the previous section).

There are only a handful of unique keys:

- ``since`` (required): The Godot version that introduced this interface function.
- ``see``: An array of strings describing external references with more information, for example,
  names of classes or functions in the Godot source code, or URLs pointing to documentation.
- ``legacy_type_name``: The legacy name used for the function pointer type in the header generated
  by Godot, when the legacy name doesn't match the pattern used for these type names. This field
  only exists so that we can generate the header in a way that is backwards compatible with the
  header from Godot 4.5 or earlier, and it shouldn't be used unless you also need to maintain
  compatibility with the old header.

Example
~~~~~~~

.. code-block:: json

    {
        "name": "get_godot_version",
        "arguments": [
            {
                "name": "r_godot_version",
                "type": "GDExtensionGodotVersion*",
                "description": [
                    "A pointer to the structure to write the version information into."
                ]
            }
        ],
        "description": [
            "Gets the Godot version that the GDExtension was loaded into."
        ],
        "since": "4.1",
        "deprecated": {
            "since": "4.5",
            "replace_with": "get_godot_version2"
        }
    }
