.. _doc_gdscript:

GDScript reference
==================

:ref:`GDScript<doc_gdscript>` is a high-level, `object-oriented
<https://en.wikipedia.org/wiki/Object-oriented_programming>`_, `imperative
<https://en.wikipedia.org/wiki/Imperative_programming>`_, and `gradually typed
<https://en.wikipedia.org/wiki/Gradual_typing>`_ programming language built for Godot.

*GDScript* is a high-level, dynamically typed programming language used to
create content. It uses an indentation-based syntax similar to languages like
`Python <https://en.wikipedia.org/wiki/Python_%28programming_language%29>`_.
Its goal is to be optimized for and tightly integrated with Godot Engine,
allowing great flexibility for content creation and integration.

GDScript is entirely independent from Python and is not based on it.

History
-------

.. note::

    Documentation about GDScript's history has been moved to the
    :ref:`Frequently Asked Questions <doc_faq_what_is_gdscript>`.

Example of GDScript
-------------------

Some people can learn better by taking a look at the syntax, so
here's an example of how GDScript looks.

::

    # Everything after "#" is a comment.
    # A file is a class!

    # (optional) class definition:
    class_name MyClass

    # Inheritance:
    extends BaseClass

    # (optional) icon to show in the editor dialogs:
    @icon("res://path/to/optional/icon.svg")


    # Member variables.
    var a = 5
    var s = "Hello"
    var arr = [1, 2, 3]
    var dict = {"key": "value", 2: 3}
    var other_dict = {key = "value", other_key = 2}
    var typed_var: int
    var inferred_type := "String"

    # Constants.
    const ANSWER = 42
    const THE_NAME = "Charly"

    # Enums.
    enum {UNIT_NEUTRAL, UNIT_ENEMY, UNIT_ALLY}
    enum Named {THING_1, THING_2, ANOTHER_THING = -1}

    # Built-in vector types.
    var v2 = Vector2(1, 2)
    var v3 = Vector3(1, 2, 3)


    # Functions.
    func some_function(param1, param2, param3):
        const local_const = 5

        if param1 < local_const:
            print(param1)
        elif param2 > 5:
            print(param2)
        else:
            print("Fail!")

        for i in range(20):
            print(i)

        while param2 != 0:
            param2 -= 1

        match param3:
            3:
                print("param3 is 3!")
            _:
                print("param3 is not 3!")

        var local_var = param1 + 3
        return local_var


    # Functions override functions with the same name on the base/super class.
    # If you still want to call them, use "super":
    func something(p1, p2):
        super(p1, p2)


    # It's also possible to call another function in the super class:
    func other_something(p1, p2):
        super.something(p1, p2)


    # Inner class
    class Something:
        var a = 10


    # Constructor
    func _init():
        print("Constructed!")
        var lv = Something.new()
        print(lv.a)

If you have previous experience with statically typed languages such as
C, C++, or C# but never used a dynamically typed one before, it is advised you
read this tutorial: :ref:`doc_gdscript_more_efficiently`.

Language
--------

In the following, an overview is given to GDScript. Details, such as which
methods are available to arrays or other objects, should be looked up in
the linked class descriptions.

Identifiers
~~~~~~~~~~~

Any string that restricts itself to alphabetic characters (``a`` to
``z`` and ``A`` to ``Z``), digits (``0`` to ``9``) and ``_`` qualifies
as an identifier. Additionally, identifiers must not begin with a digit.
Identifiers are case-sensitive (``foo`` is different from ``FOO``).

Keywords
~~~~~~~~

The following is the list of keywords supported by the language. Since
keywords are reserved words (tokens), they can't be used as identifiers.
Operators (like ``in``, ``not``, ``and`` or ``or``) and names of built-in types
as listed in the following sections are also reserved.

Keywords are defined in the `GDScript tokenizer <https://github.com/godotengine/godot/blob/master/modules/gdscript/gdscript_tokenizer.cpp>`_
in case you want to take a look under the hood.

+------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
|  Keyword   | Description                                                                                                                                       |
+============+===================================================================================================================================================+
| if         | See `if/else/elif`_.                                                                                                                              |
+------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| elif       | See `if/else/elif`_.                                                                                                                              |
+------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| else       | See `if/else/elif`_.                                                                                                                              |
+------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| for        | See for_.                                                                                                                                         |
+------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| while      | See while_.                                                                                                                                       |
+------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| match      | See match_.                                                                                                                                       |
+------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| break      | Exits the execution of the current ``for`` or ``while`` loop.                                                                                     |
+------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| continue   | Immediately skips to the next iteration of the ``for`` or ``while`` loop. Stops execution in ``match`` and looks for a match in patterns below it |
+------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| pass       | Used where a statement is required syntactically but execution of code is undesired, e.g. in empty functions.                                     |
+------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| return     | Returns a value from a function.                                                                                                                  |
+------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| class      | Defines a class.                                                                                                                                  |
+------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| class_name | Defines the script as a globally accessible class with the specified name.                                                                        |
+------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| extends    | Defines what class to extend with the current class.                                                                                              |
+------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| is         | Tests whether a variable extends a given class, or is of a given built-in type.                                                                   |
+------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| in         | Tests whether a value is within a string, list, range, dictionary, or node. When used with ``for``, it iterates through them instead of testing.  |
+------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| as         | Cast the value to a given type if possible.                                                                                                       |
+------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| self       | Refers to current class instance.                                                                                                                 |
+------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| signal     | Defines a signal.                                                                                                                                 |
+------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| func       | Defines a function.                                                                                                                               |
+------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| static     | Defines a static function. Static member variables are not allowed.                                                                               |
+------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| const      | Defines a constant.                                                                                                                               |
+------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| enum       | Defines an enum.                                                                                                                                  |
+------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| var        | Defines a variable.                                                                                                                               |
+------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| breakpoint | Editor helper for debugger breakpoints.                                                                                                           |
+------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| preload    | Preloads a class or variable. See `Classes as resources`_.                                                                                        |
+------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| await      | Waits for a signal or a coroutine to finish. See `Awaiting for signals`_.                                                                         |
+------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| yield      | Previously used for coroutines. Kept as keyword for transition.                                                                                   |
+------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| assert     | Asserts a condition, logs error on failure. Ignored in non-debug builds. See `Assert keyword`_.                                                   |
+------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| void       | Used to represent that a function does not return any value.                                                                                      |
+------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| PI         | PI constant.                                                                                                                                      |
+------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| TAU        | TAU constant.                                                                                                                                     |
+------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| INF        | Infinity constant. Used for comparisons and as result of calculations.                                                                            |
+------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| NAN        | NAN (not a number) constant. Used as impossible result from calculations.                                                                         |
+------------+---------------------------------------------------------------------------------------------------------------------------------------------------+

Operators
~~~~~~~~~

The following is the list of supported operators and their precedence.

+--------------------------------------------------------------------------------+-------------------------------------------+
| **Operator**                                                                   | **Description**                           |
+================================================================================+===========================================+
| ``x[index]``                                                                   | Subscription (highest priority)           |
+--------------------------------------------------------------------------------+-------------------------------------------+
| ``x.attribute``                                                                | Attribute reference                       |
+--------------------------------------------------------------------------------+-------------------------------------------+
| ``foo()``                                                                      | Function call                             |
+--------------------------------------------------------------------------------+-------------------------------------------+
| ``is``                                                                         | Instance type checker                     |
+--------------------------------------------------------------------------------+-------------------------------------------+
| ``**``                                                                         | Power operator                            |
|                                                                                |                                           |
|                                                                                | Multiplies value by itself ``x`` times,   |
|                                                                                | similar to calling ``pow`` built-in       |
|                                                                                | function                                  |
+--------------------------------------------------------------------------------+-------------------------------------------+
| ``~``                                                                          | Bitwise NOT                               |
+--------------------------------------------------------------------------------+-------------------------------------------+
| ``-x``                                                                         | Negative / Unary negation                 |
+--------------------------------------------------------------------------------+-------------------------------------------+
| ``*`` ``/`` ``%``                                                              | Multiplication / Division / Remainder     |
|                                                                                |                                           |
|                                                                                | These operators have the same behavior    |
|                                                                                | as C++. Integer division is truncated     |
|                                                                                | rather than returning a fractional        |
|                                                                                | number, and the % operator is only        |
|                                                                                | available for ints (``fmod`` for floats), |
|                                                                                | and is additionally used for Format       |
|                                                                                | Strings                                   |
+--------------------------------------------------------------------------------+-------------------------------------------+
| ``+``                                                                          | Addition / Concatenation of arrays        |
+--------------------------------------------------------------------------------+-------------------------------------------+
| ``-``                                                                          | Subtraction                               |
+--------------------------------------------------------------------------------+-------------------------------------------+
| ``<<`` ``>>``                                                                  | Bit shifting                              |
+--------------------------------------------------------------------------------+-------------------------------------------+
| ``&``                                                                          | Bitwise AND                               |
+--------------------------------------------------------------------------------+-------------------------------------------+
| ``^``                                                                          | Bitwise XOR                               |
+--------------------------------------------------------------------------------+-------------------------------------------+
| ``|``                                                                          | Bitwise OR                                |
+--------------------------------------------------------------------------------+-------------------------------------------+
| ``<`` ``>`` ``==`` ``!=`` ``>=`` ``<=``                                        | Comparisons                               |
+--------------------------------------------------------------------------------+-------------------------------------------+
| ``in``                                                                         | Inclusion checker (when used with         |
|                                                                                | control flow keywords or in a             |
|                                                                                | standalone expression).                   |
|                                                                                |                                           |
|                                                                                | Content iterator (when used with the      |
|                                                                                | for_ keyword).                            |
+--------------------------------------------------------------------------------+-------------------------------------------+
| ``not``                                                                        | Boolean NOT                               |
+--------------------------------------------------------------------------------+-------------------------------------------+
| ``and``                                                                        | Boolean AND                               |
+--------------------------------------------------------------------------------+-------------------------------------------+
| ``or``                                                                         | Boolean OR                                |
+--------------------------------------------------------------------------------+-------------------------------------------+
| ``if x else``                                                                  | Ternary if/else                           |
+--------------------------------------------------------------------------------+-------------------------------------------+
| ``as``                                                                         | Type casting                              |
+--------------------------------------------------------------------------------+-------------------------------------------+
| ``=`` ``+=`` ``-=`` ``*=`` ``/=`` ``%=`` ``**=`` ``&=`` ``|=`` ``<<=`` ``>>=`` | Assignment (lowest priority)              |
+--------------------------------------------------------------------------------+-------------------------------------------+

Literals
~~~~~~~~

+--------------------------+----------------------------------------+
| **Literal**              | **Type**                               |
+--------------------------+----------------------------------------+
| ``45``                   | Base 10 integer                        |
+--------------------------+----------------------------------------+
| ``0x8f51``               | Base 16 (hexadecimal) integer          |
+--------------------------+----------------------------------------+
| ``0b101010``             | Base 2 (binary) integer                |
+--------------------------+----------------------------------------+
| ``3.14``, ``58.1e-10``   | Floating-point number (real)           |
+--------------------------+----------------------------------------+
| ``"Hello"``, ``"Hi"``    | Strings                                |
+--------------------------+----------------------------------------+
| ``"""Hello"""``          | Multiline string                       |
+--------------------------+----------------------------------------+
| ``&"name"``              | :ref:`StringName <class_StringName>`   |
+--------------------------+----------------------------------------+
| ``^"Node/Label"``        | :ref:`NodePath <class_NodePath>`       |
+--------------------------+----------------------------------------+
| ``$NodePath``            | Shorthand for ``get_node("NodePath")`` |
+--------------------------+----------------------------------------+

Integers and floats can have their numbers separated with ``_`` to make them more readable.
The following ways to write numbers are all valid::

    12_345_678  # Equal to 12345678.
    3.141_592_7  # Equal to 3.1415927.
    0x8080_0000_ffff  # Equal to 0x80800000ffff.
    0b11_00_11_00  # Equal to 0b11001100.

Annotations
~~~~~~~~~~~

There are some special tokens in GDScript that act like keywords but are not,
they are *annotations* instead. Every annotation start with the ``@`` character
and is specified by a name. A detailed description and example for each annotation
can be found inside the :ref:`GDScript class reference <class_@GDScript>`.

Annotations affect how the script is treated by external tools and usually don't
change the behavior.

For instance, you can use it to export a value to the editor::

    @export_range(1, 100, 1, "or_greater")
    var ranged_var: int = 50

For more information about exporting properties, read the :ref:`GDScript exports <doc_gdscript_exports>`
article.

Annotations can be specified one per line or all in the same line. They affect
the next statement that isn't an annotation. Annotations can have arguments sent
between parentheses and separated by commas.

Both of these are the same::

    @onready
    @export_node_path(TextEdit, LineEdit)
    var input_field

    @onready @export_node_path(TextEdit, LineEdit) var input_field

.. _doc_gdscript_onready_annotation:

`@onready` annotation
~~~~~~~~~~~~~~~~~~~~~

When using nodes, it's common to desire to keep references to parts
of the scene in a variable. As scenes are only warranted to be
configured when entering the active scene tree, the sub-nodes can only
be obtained when a call to ``Node._ready()`` is made.

::

    var my_label


    func _ready():
        my_label = get_node("MyLabel")

This can get a little cumbersome, especially when nodes and external
references pile up. For this, GDScript has the ``@onready`` annotation, that
defers initialization of a member variable until ``_ready()`` is called. It
can replace the above code with a single line::

    @onready var my_label = get_node("MyLabel")

Comments
~~~~~~~~

Anything from a ``#`` to the end of the line is ignored and is
considered a comment.

::

    # This is a comment.

.. _doc_gdscript_builtin_types:

Line continuation
~~~~~~~~~~~~~~~~~

A line of code in GDScript can be continued on the next line by using a backslash
(``\``). Add one at the end of a line and the code on the next line will act like
it's where the backslash is. Here is an example:

::

    var a = 1 + \
    2

A line can be continued multiple times like this:

::

    var a = 1 + \
    4 + \
    10 + \
    4

Built-in types
--------------

Built-in types are stack-allocated. They are passed as values. This means a copy
is created on each assignment or when passing them as arguments to functions.
The only exceptions are ``Array``\ s and ``Dictionaries``, which are passed by
reference so they are shared. (Packed arrays such as ``PackedByteArray`` are still
passed as values.)

Basic built-in types
~~~~~~~~~~~~~~~~~~~~

A variable in GDScript can be assigned to several built-in types.

null
^^^^

``null`` is an empty data type that contains no information and can not
be assigned any other value.

:ref:`bool <class_bool>`
^^^^^^^^^^^^^^^^^^^^^^^^

Short for "boolean", it can only contain ``true`` or ``false``.

:ref:`int <class_int>`
^^^^^^^^^^^^^^^^^^^^^^

Short for "integer", it stores whole numbers (positive and negative).
It is stored as a 64-bit value, equivalent to "int64_t" in C++.

:ref:`float <class_float>`
^^^^^^^^^^^^^^^^^^^^^^^^^^

Stores real numbers, including decimals, using floating-point values.
It is stored as a 64-bit value, equivalent to "double" in C++.
Note: Currently, data structures such as Vector2, Vector3, and
PackedFloat32Array store 32-bit single-precision "float" values.

:ref:`String <class_String>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A sequence of characters in `Unicode format <https://en.wikipedia.org/wiki/Unicode>`_.
Strings can contain the following escape sequences:

+---------------------+---------------------------------+
| **Escape sequence** | **Expands to**                  |
+---------------------+---------------------------------+
| ``\n``              | Newline (line feed)             |
+---------------------+---------------------------------+
| ``\t``              | Horizontal tab character        |
+---------------------+---------------------------------+
| ``\r``              | Carriage return                 |
+---------------------+---------------------------------+
| ``\a``              | Alert (beep/bell)               |
+---------------------+---------------------------------+
| ``\b``              | Backspace                       |
+---------------------+---------------------------------+
| ``\f``              | Formfeed page break             |
+---------------------+---------------------------------+
| ``\v``              | Vertical tab character          |
+---------------------+---------------------------------+
| ``\"``              | Double quote                    |
+---------------------+---------------------------------+
| ``\'``              | Single quote                    |
+---------------------+---------------------------------+
| ``\\``              | Backslash                       |
+---------------------+---------------------------------+
| ``\uXXXX``          | Unicode codepoint ``XXXX``      |
|                     | (hexadecimal, case-insensitive) |
+---------------------+---------------------------------+

Also, using ``\`` followed by a newline inside a string will allow you to continue it in the next line, without
inserting a newline character in the string itself.

GDScript also supports :ref:`doc_gdscript_printf`.

:ref:`StringName <class_StringName>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An immutable string that allows only one instance of each name. They are slower to
create and may result in waiting for locks when multithreading. In exchange, they're
very fast to compare, which makes them good candidates for dictionary keys.

:ref:`NodePath <class_NodePath>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A pre-parsed path to a node or a node property. They are useful to interact with
the tree to get a node, or affecting properties like with :ref:`Tweens <class_Tween>`.

Vector built-in types
~~~~~~~~~~~~~~~~~~~~~

:ref:`Vector2 <class_Vector2>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

2D vector type containing ``x`` and ``y`` fields. Can also be
accessed as an array.

:ref:`Vector2i <class_Vector2i>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Same as a Vector2 but the components are integers. Useful for representing
items in a 2D grid.

:ref:`Rect2 <class_Rect2>`
^^^^^^^^^^^^^^^^^^^^^^^^^^

2D Rectangle type containing two vectors fields: ``position`` and ``size``.
Also contains an ``end`` field which is ``position + size``.

:ref:`Vector3 <class_Vector3>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

3D vector type containing ``x``, ``y`` and ``z`` fields. This can also
be accessed as an array.

:ref:`Vector3i <class_Vector3i>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Same as Vector3 but the components are integers. Can be use for indexing items
in a 3D grid.

:ref:`Transform2D <class_Transform2D>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

3×2 matrix used for 2D transforms.

:ref:`Plane <class_Plane>`
^^^^^^^^^^^^^^^^^^^^^^^^^^

3D Plane type in normalized form that contains a ``normal`` vector field
and a ``d`` scalar distance.

:ref:`Quaternion <class_Quaternion>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Quaternion is a datatype used for representing a 3D rotation. It's
useful for interpolating rotations.

:ref:`AABB <class_AABB>`
^^^^^^^^^^^^^^^^^^^^^^^^

Axis-aligned bounding box (or 3D box) contains 2 vectors fields: ``position``
and ``size``. Also contains an ``end`` field which is
``position + size``.

:ref:`Basis <class_Basis>`
^^^^^^^^^^^^^^^^^^^^^^^^^^

3x3 matrix used for 3D rotation and scale. It contains 3 vector fields
(``x``, ``y`` and ``z``) and can also be accessed as an array of 3D
vectors.

:ref:`Transform3D <class_Transform3D>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

3D Transform contains a Basis field ``basis`` and a Vector3 field
``origin``.

Engine built-in types
~~~~~~~~~~~~~~~~~~~~~

:ref:`Color <class_Color>`
^^^^^^^^^^^^^^^^^^^^^^^^^^

Color data type contains ``r``, ``g``, ``b``, and ``a`` fields. It can
also be accessed as ``h``, ``s``, and ``v`` for hue/saturation/value.

:ref:`NodePath <class_NodePath>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Compiled path to a node used mainly in the scene system. It can be
easily assigned to, and from, a String.

:ref:`RID <class_RID>`
^^^^^^^^^^^^^^^^^^^^^^

Resource ID (RID). Servers use generic RIDs to reference opaque data.

:ref:`Object <class_Object>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Base class for anything that is not a built-in type.

Container built-in types
~~~~~~~~~~~~~~~~~~~~~~~~

:ref:`Array <class_Array>`
^^^^^^^^^^^^^^^^^^^^^^^^^^

Generic sequence of arbitrary object types, including other arrays or dictionaries (see below).
The array can resize dynamically. Arrays are indexed starting from index ``0``.
Negative indices count from the end.

::

    var arr = []
    arr = [1, 2, 3]
    var b = arr[1] # This is 2.
    var c = arr[arr.size() - 1] # This is 3.
    var d = arr[-1] # Same as the previous line, but shorter.
    arr[0] = "Hi!" # Replacing value 1 with "Hi!".
    arr.append(4) # Array is now ["Hi!", 2, 3, 4].

GDScript arrays are allocated linearly in memory for speed.
Large arrays (more than tens of thousands of elements) may however cause
memory fragmentation. If this is a concern, special types of
arrays are available. These only accept a single data type. They avoid memory
fragmentation and use less memory, but are atomic and tend to run slower than generic
arrays. They are therefore only recommended to use for large data sets:

- :ref:`PackedByteArray <class_PackedByteArray>`: An array of bytes (integers from 0 to 255).
- :ref:`PackedInt32Array <class_PackedInt32Array>`: An array of 32-bit integers.
- :ref:`PackedInt64Array <class_PackedInt64Array>`: An array of 64-bit integers.
- :ref:`PackedFloat32Array <class_PackedFloat32Array>`: An array of 32-bit floats.
- :ref:`PackedFloat64Array <class_PackedFloat64Array>`: An array of 64-bit floats.
- :ref:`PackedStringArray <class_PackedStringArray>`: An array of strings.
- :ref:`PackedVector2Array <class_PackedVector2Array>`: An array of :ref:`Vector2 <class_Vector2>` objects.
- :ref:`PackedVector3Array <class_PackedVector3Array>`: An array of :ref:`Vector3 <class_Vector3>` objects.
- :ref:`PackedColorArray <class_PackedColorArray>`: An array of :ref:`Color <class_Color>` objects.

:ref:`Dictionary <class_Dictionary>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Associative container which contains values referenced by unique keys.

::

    var d = {4: 5, "A key": "A value", 28: [1, 2, 3]}
    d["Hi!"] = 0
    d = {
        22: "value",
        "some_key": 2,
        "other_key": [2, 3, 4],
        "more_key": "Hello"
    }

Lua-style table syntax is also supported. Lua-style uses ``=`` instead of ``:``
and doesn't use quotes to mark string keys (making for slightly less to write).
However, keys written in this form can't start with a digit (like any GDScript
identifier).

::

    var d = {
        test22 = "value",
        some_key = 2,
        other_key = [2, 3, 4],
        more_key = "Hello"
    }

To add a key to an existing dictionary, access it like an existing key and
assign to it::

    var d = {} # Create an empty Dictionary.
    d.waiting = 14 # Add String "waiting" as a key and assign the value 14 to it.
    d[4] = "hello" # Add integer 4 as a key and assign the String "hello" as its value.
    d["Godot"] = 3.01 # Add String "Godot" as a key and assign the value 3.01 to it.

    var test = 4
    # Prints "hello" by indexing the dictionary with a dynamic key.
    # This is not the same as `d.test`. The bracket syntax equivalent to
    # `d.test` is `d["test"]`.
    print(d[test])

.. note::

    The bracket syntax can be used to access properties of any
    :ref:`class_Object`, not just Dictionaries. Keep in mind it will cause a
    script error when attempting to index a non-existing property. To avoid
    this, use the :ref:`Object.get() <class_Object_method_get>` and
    :ref:`Object.set() <class_Object_method_set>` methods instead.

:ref:`Signal <class_Signal>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A signal is a message that can be emitted by an object to those who want to
listen to it. The Signal type can be used for passing the emitter around.

Signals are better used by getting them from actual objects, e.g. ``$Button.button_up``.

:ref:`Callable <class_Callable>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Contains an object and a function, which is useful for passing functions as
values (e.g. when connecting to signals).

Getting a method as a member returns a callable. ``var x = $Sprite2D.rotate``
will set the value of ``x`` to a callable with ``$Sprite2D`` as the object and
``rotate`` as the method.

You can call it using the ``call`` method: ``x.call(PI)``.

Data
----

Variables
~~~~~~~~~

Variables can exist as class members or local to functions. They are
created with the ``var`` keyword and may, optionally, be assigned a
value upon initialization.

::

    var a # Data type is 'null' by default.
    var b = 5
    var c = 3.8
    var d = b + c # Variables are always initialized in order.

Variables can optionally have a type specification. When a type is specified,
the variable will be forced to have always that same type, and trying to assign
an incompatible value will raise an error.

Types are specified in the variable declaration using a ``:`` (colon) symbol
after the variable name, followed by the type.

::

    var my_vector2: Vector2
    var my_node: Node = Sprite2D.new()

If the variable is initialized within the declaration, the type can be inferred, so
it's possible to omit the type name::

    var my_vector2 := Vector2() # 'my_vector2' is of type 'Vector2'.
    var my_node := Sprite2D.new() # 'my_node' is of type 'Sprite2D'.

Type inference is only possible if the assigned value has a defined type, otherwise
it will raise an error.

Valid types are:

- Built-in types (Array, Vector2, int, String, etc.).
- Engine classes (Node, Resource, Reference, etc.).
- Constant names if they contain a script resource (``MyScript`` if you declared ``const MyScript = preload("res://my_script.gd")``).
- Other classes in the same script, respecting scope (``InnerClass.NestedClass`` if you declared ``class NestedClass`` inside the ``class InnerClass`` in the same scope).
- Script classes declared with the ``class_name`` keyword.
- Autoloads registered as singletons.

Casting
^^^^^^^

Values assigned to typed variables must have a compatible type. If it's needed to
coerce a value to be of a certain type, in particular for object types, you can
use the casting operator ``as``.

Casting between object types results in the same object if the value is of the
same type or a subtype of the cast type.

::

    var my_node2D: Node2D
    my_node2D = $Sprite2D as Node2D # Works since Sprite2D is a subtype of Node2D.

If the value is not a subtype, the casting operation will result in a ``null`` value.

::

    var my_node2D: Node2D
    my_node2D = $Button as Node2D # Results in 'null' since a Button is not a subtype of Node2D.

For built-in types, they will be forcibly converted if possible, otherwise the
engine will raise an error.

::

    var my_int: int
    my_int = "123" as int # The string can be converted to int.
    my_int = Vector2() as int # A Vector2 can't be converted to int, this will cause an error.

Casting is also useful to have better type-safe variables when interacting with
the scene tree::

    # Will infer the variable to be of type Sprite2D.
    var my_sprite := $Character as Sprite2D

    # Will fail if $AnimPlayer is not an AnimationPlayer, even if it has the method 'play()'.
    ($AnimPlayer as AnimationPlayer).play("walk")

Constants
~~~~~~~~~

Constants are values you cannot change when the game is running.
Their value must be known at compile-time. Using the
``const`` keyword allows you to give a constant value a name. Trying to assign a
value to a constant after it's declared will give you an error.

We recommend using constants whenever a value is not meant to change.

::

    const A = 5
    const B = Vector2(20, 20)
    const C = 10 + 20 # Constant expression.
    const D = Vector2(20, 30).x # Constant expression: 20.
    const E = [1, 2, 3, 4][0] # Constant expression: 1.
    const F = sin(20) # 'sin()' can be used in constant expressions.
    const G = x + 20 # Invalid; this is not a constant expression!
    const H = A + 20 # Constant expression: 25 (`A` is a constant).

Although the type of constants is inferred from the assigned value, it's also
possible to add explicit type specification::

    const A: int = 5
    const B: Vector2 = Vector2()

Assigning a value of an incompatible type will raise an error.

You can also create constants inside a function, which is useful to name local
magic values.

.. note::

    Since objects, arrays and dictionaries are passed by reference, constants are "flat".
    This means that if you declare a constant array or dictionary, it can still
    be modified afterwards. They can't be reassigned with another value though.

Enums
^^^^^

Enums are basically a shorthand for constants, and are pretty useful if you
want to assign consecutive integers to some constant.

If you pass a name to the enum, it will put all the keys inside a constant
dictionary of that name.

.. important:: In Godot 3.1 and later, keys in a named enum are not registered
               as global constants. They should be accessed prefixed by the
               enum's name (``Name.KEY``); see an example below.

::

    enum {TILE_BRICK, TILE_FLOOR, TILE_SPIKE, TILE_TELEPORT}
    # Is the same as:
    const TILE_BRICK = 0
    const TILE_FLOOR = 1
    const TILE_SPIKE = 2
    const TILE_TELEPORT = 3

    enum State {STATE_IDLE, STATE_JUMP = 5, STATE_SHOOT}
    # Is the same as:
    const State = {STATE_IDLE = 0, STATE_JUMP = 5, STATE_SHOOT = 6}
    # Access values with State.STATE_IDLE, etc.


Functions
~~~~~~~~~

Functions always belong to a `class <Classes_>`_. The scope priority for
variable look-up is: local → class member → global. The ``self`` variable is
always available and is provided as an option for accessing class members, but
is not always required (and should *not* be sent as the function's first
argument, unlike Python).

::

    func my_function(a, b):
        print(a)
        print(b)
        return a + b  # Return is optional; without it 'null' is returned.

A function can ``return`` at any point. The default return value is ``null``.

If a function contains only one line of code, it can be written on one line::

    func square(a): return a * a

    func hello_world(): print("Hello World")

    func empty_function(): pass

Functions can also have type specification for the arguments and for the return
value. Types for arguments can be added in a similar way to variables::

    func my_function(a: int, b: String):
        pass

If a function argument has a default value, it's possible to infer the type::

    func my_function(int_arg := 42, String_arg := "string"):
        pass

The return type of the function can be specified after the arguments list using
the arrow token (``->``)::

    func my_int_function() -> int:
        return 0

Functions that have a return type **must** return a proper value. Setting the
type as ``void`` means the function doesn't return anything. Void functions can
return early with the ``return`` keyword, but they can't return any value.

::

    func void_function() -> void:
        return # Can't return a value.

.. note:: Non-void functions must **always** return a value, so if your code has
          branching statements (such as an ``if``/``else`` construct), all the
          possible paths must have a return. E.g., if you have a ``return``
          inside an ``if`` block but not after it, the editor will raise an
          error because if the block is not executed, the function won't have a
          valid value to return.

Referencing functions
^^^^^^^^^^^^^^^^^^^^^

Functions are first-class items in terms of the :ref:`Callable <class_Callable>` object. Referencing a
function by name without calling it will automatically generate the proper
callable. This can be used to pass functions as arguments.

::

    func map(arr: Array, function: Callable) -> Array:
        var result = []
        for item in arr:
            result.push_back(function.call(item))
        return result

    func add1(value: int) -> int:
        return value + 1;

    func _ready() -> void:
        var my_array = [1, 2, 3]
        var plus_one = map(my_array, add1)
        print(plus_one) # Prints [2, 3, 4].

.. note:: Callables **must** be called with the ``call`` method. You cannot use
          the ``()`` operator directly. This behavior is implemented to avoid
          performance issues on direct function calls.

Lambda functions
^^^^^^^^^^^^^^^^

Lambda functions allow you to declare functions that do not belong to a class. Instead a :ref:`Callable <class_Callable>` object is created and assigned to a variable directly.
This can be useful to create Callables to pass around without polluting the class scope.

::

    var lambda = func(x): print(x)
    lambda.call(42) # Prints "42"

Lambda functions can be named for debugging purposes::

    var lambda = func my_lambda(x):
        print(x)

Lambda functions capture the local environment. Local variables are passed by value, so they won't be updated in the lambda if changed in the local function::

    var x = 42
    var my_lambda = func(): print(x)
    my_lambda.call() # Prints "42"
    x = "Hello"
    my_lambda.call() # Prints "42"

.. note:: The values of the outer scope behave like constants. Therefore, if you declare an array or dictionary, it can still be modified afterwards.

Static functions
^^^^^^^^^^^^^^^^

A function can be declared static. When a function is static, it has no
access to the instance member variables or ``self``. This is mainly
useful to make libraries of helper functions::

    static func sum2(a, b):
        return a + b

Lambdas cannot be declared static.


Statements and control flow
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Statements are standard and can be assignments, function calls, control
flow structures, etc (see below). ``;`` as a statement separator is
entirely optional.

Expressions
^^^^^^^^^^^

Expressions are sequences of operators and their operands in orderly fashion. An expression by itself can be a
statement too, though only calls are reasonable to use as statements since other expressions don't have side effects.

Expressions return values that can be assigned to valid targets. Operands to some operator can be another
expression. An assignment is not an expression and thus does not return any value.

Here are some examples of expressions::

    2 + 2 # Binary operation.
    -5 # Unary operation.
    "okay" if x > 4 else "not okay" # Ternary operation.
    x # Identifier representing variable or constant.
    x.a # Attribute access.
    x[4] # Subscript access.
    x > 2 or x < 5 # Comparisons and logic operators.
    x == y + 2 # Equality test.
    do_something() # Function call.
    [1, 2, 3] # Array definition.
    {A = 1, B = 2} # Dictionary definition.
    preload("res://icon.png") # Preload builtin function.
    self # Reference to current instance.

Identifiers, attributes, and subscripts are valid assignment targets. Other expressions cannot be on the left side of
an assignment.

if/else/elif
^^^^^^^^^^^^

Simple conditions are created by using the ``if``/``else``/``elif`` syntax.
Parenthesis around conditions are allowed, but not required. Given the
nature of the tab-based indentation, ``elif`` can be used instead of
``else``/``if`` to maintain a level of indentation.

::

    if (expression):
        statement(s)
    elif (expression):
        statement(s)
    else:
        statement(s)

Short statements can be written on the same line as the condition::

    if 1 + 1 == 2: return 2 + 2
    else:
        var x = 3 + 3
        return x

Sometimes, you might want to assign a different initial value based on a
boolean expression. In this case, ternary-if expressions come in handy::

    var x = (value) if (expression) else (value)
    y += 3 if y < 10 else -1

Ternary-if expressions can be nested to handle more than 2 cases. When nesting
ternary-if expressions, it is recommended to wrap the complete expression over
multiple lines to preserve readability::

    var count = 0

    var fruit = (
            "apple" if count == 2
            else "pear" if count == 1
            else "banana" if count == 0
            else "orange"
    )
    print(fruit)  # banana

    # Alternative syntax with backslashes instead of parentheses (for multi-line expressions).
    # Less lines required, but harder to refactor.
    var fruit_alt = \
            "apple" if count == 2 \
            else "pear" if count == 1 \
            else "banana" if count == 0 \
            else "orange"
    print(fruit_alt)  # banana

You may also wish to check if a value is contained within something. You can
use an ``if`` statement combined with the ``in`` operator to accomplish this::

    # Check if a letter is in a string.
    var text = "abc"
    if 'b' in text: print("The string contains b")

    # Check if a variable is contained within a node.
    if "varName" in get_parent(): print("varName is defined in parent!")

while
^^^^^

Simple loops are created by using ``while`` syntax. Loops can be broken
using ``break`` or continued using ``continue``:

::

    while (expression):
        statement(s)

for
^^^

To iterate through a range, such as an array or table, a *for* loop is
used. When iterating over an array, the current array element is stored in
the loop variable. When iterating over a dictionary, the *key* is stored
in the loop variable.

::

    for x in [5, 7, 11]:
        statement # Loop iterates 3 times with 'x' as 5, then 7 and finally 11.

    var dict = {"a": 0, "b": 1, "c": 2}
    for i in dict:
        print(dict[i]) # Prints 0, then 1, then 2.

    for i in range(3):
        statement # Similar to [0, 1, 2] but does not allocate an array.

    for i in range(1, 3):
        statement # Similar to [1, 2] but does not allocate an array.

    for i in range(2, 8, 2):
        statement # Similar to [2, 4, 6] but does not allocate an array.

    for c in "Hello":
        print(c) # Iterate through all characters in a String, print every letter on new line.

    for i in 3:
        statement # Similar to range(3).

    for i in 2.2:
        statement # Similar to range(ceil(2.2)).

If you want to assign values on an array as it is being iterated through, it
is best to use ``for i in array.size()``.

::
    for i in array.size():
	    array[i] = "Hello World"


The loop variable is local to the for-loop and assigning to it will not change
the value on the array. Objects passed by reference (such as nodes) can still
be manipulated by calling methods on the loop variable.

::
    for string in string_array:
        string = "Hello World" # This has no effect

    for node in node_array:
        node.add_to_group("Cool_Group") # This has an effect

match
^^^^^

A ``match`` statement is used to branch execution of a program.
It's the equivalent of the ``switch`` statement found in many other languages, but offers some additional features.

Basic syntax::

    match (expression):
        [pattern](s):
            [block]
        [pattern](s):
            [block]
        [pattern](s):
            [block]


**Crash-course for people who are familiar with switch statements**:

1. Replace ``switch`` with ``match``.
2. Remove ``case``.
3. Remove any ``break``\ s.
4. Change ``default`` to a single underscore.

**Control flow**:

The patterns are matched from top to bottom.
If a pattern matches, the first corresponding block will be executed. After that, the execution continues below the ``match`` statement.
You can use ``continue`` to stop execution in the current block and check for an additional match in the patterns below it.

There are 6 pattern types:

- Constant pattern
    Constant primitives, like numbers and strings::

        match x:
            1:
                print("We are number one!")
            2:
                print("Two are better than one!")
            "test":
                print("Oh snap! It's a string!")


- Variable pattern
    Matches the contents of a variable/enum::

        match typeof(x):
            TYPE_FLOAT:
                print("float")
            TYPE_STRING:
                print("text")
            TYPE_ARRAY:
                print("array")


- Wildcard pattern
    This pattern matches everything. It's written as a single underscore.

    It can be used as the equivalent of the ``default`` in a ``switch`` statement in other languages::

        match x:
            1:
                print("It's one!")
            2:
                print("It's one times two!")
            _:
                print("It's not 1 or 2. I don't care to be honest.")


- Binding pattern
    A binding pattern introduces a new variable. Like the wildcard pattern, it matches everything - and also gives that value a name.
    It's especially useful in array and dictionary patterns::

        match x:
            1:
                print("It's one!")
            2:
                print("It's one times two!")
            var new_var:
                print("It's not 1 or 2, it's ", new_var)


- Array pattern
    Matches an array. Every single element of the array pattern is a pattern itself, so you can nest them.

    The length of the array is tested first, it has to be the same size as the pattern, otherwise the pattern doesn't match.

    **Open-ended array**: An array can be bigger than the pattern by making the last subpattern ``..``.

    Every subpattern has to be comma-separated.

    ::

        match x:
            []:
                print("Empty array")
            [1, 3, "test", null]:
                print("Very specific array")
            [var start, _, "test"]:
                print("First element is ", start, ", and the last is \"test\"")
            [42, ..]:
                print("Open ended array")

- Dictionary pattern
    Works in the same way as the array pattern. Every key has to be a constant pattern.

    The size of the dictionary is tested first, it has to be the same size as the pattern, otherwise the pattern doesn't match.

    **Open-ended dictionary**: A dictionary can be bigger than the pattern by making the last subpattern ``..``.

    Every subpattern has to be comma separated.

    If you don't specify a value, then only the existence of the key is checked.

    A value pattern is separated from the key pattern with a ``:``.

    ::

        match x:
            {}:
                print("Empty dict")
            {"name": "Dennis"}:
                print("The name is Dennis")
            {"name": "Dennis", "age": var age}:
                print("Dennis is ", age, " years old.")
            {"name", "age"}:
                print("Has a name and an age, but it's not Dennis :(")
            {"key": "godotisawesome", ..}:
                print("I only checked for one entry and ignored the rest")

- Multiple patterns
    You can also specify multiple patterns separated by a comma. These patterns aren't allowed to have any bindings in them.

    ::

        match x:
            1, 2, 3:
                print("It's 1 - 3")
            "Sword", "Splash potion", "Fist":
                print("Yep, you've taken damage")

Classes
~~~~~~~

By default, all script files are unnamed classes. In this case, you can only
reference them using the file's path, using either a relative or an absolute
path. For example, if you name a script file ``character.gd``::

   # Inherit from 'Character.gd'.

   extends "res://path/to/character.gd"

   # Load character.gd and create a new node instance from it.

   var Character = load("res://path/to/character.gd")
   var character_node = Character.new()

.. _doc_gdscript_basics_class_name:

Registering named classes
~~~~~~~~~~~~~~~~~~~~~~~~~

You can give your class a name to register it as a new type in Godot's
editor. For that, you use the ``class_name`` keyword. You can optionally use
the ``@icon`` annotation with a path to an image, to use it as an icon. Your
class will then appear with its new icon in the editor::

   # Item.gd

   extends Node
   class_name Item
   @icon("res://interface/icons/item.png")

.. image:: img/class_name_editor_register_example.png

Here's a class file example:

::

    # Saved as a file named 'character.gd'.

    class_name Character


    var health = 5


    func print_health():
        print(health)


    func print_this_script_three_times():
        print(get_script())
        print(ResourceLoader.load("res://character.gd"))
        print(Character)

If you want to use ``extends`` too, you can keep both on the same line::

    class_name MyNode extends Node

.. note:: Godot's class syntax is compact: it can only contain member variables or
          functions. You can use static functions, but not static member variables. In the
          same way, the engine initializes variables every time you create an instance,
          and this includes arrays and dictionaries. This is in the spirit of thread
          safety, since scripts can be initialized in separate threads without the user
          knowing.


Inheritance
^^^^^^^^^^^

A class (stored as a file) can inherit from:

- A global class.
- Another class file.
- An inner class inside another class file.

Multiple inheritance is not allowed.

Inheritance uses the ``extends`` keyword::

    # Inherit/extend a globally available class.
    extends SomeClass

    # Inherit/extend a named class file.
    extends "somefile.gd"

    # Inherit/extend an inner class in another file.
    extends "somefile.gd".SomeInnerClass

.. note::

    If inheritance is not explicitly defined, the class will default to inheriting
    :ref:`class_RefCounted`.

To check if a given instance inherits from a given class,
the ``is`` keyword can be used::

    # Cache the enemy class.
    const Enemy = preload("enemy.gd")

    # [...]

    # Use 'is' to check inheritance.
    if entity is Enemy:
        entity.apply_damage()

To call a function in a *super class* (i.e. one ``extend``-ed in your current
class), use the ``super`` keyword::

    super(args)

This is especially useful because functions in extending classes replace
functions with the same name in their super classes. If you still want to
call them, you can use ``super``::

    func some_func(x):
        super(x) # Calls the same function on the super class.

If you need to call a different function from the super class, you can specify
the function name with the attribute operator::

    func overriding():
        return 0 # This overrides the method in the base class.

    func dont_override():
        return super.overriding() # This calls the method as defined in the base class.


Class constructor
^^^^^^^^^^^^^^^^^

The class constructor, called on class instantiation, is named ``_init``. If you
want to call the base class constructor, you can also use the ``super`` syntax.
Note that every class has an implicit constructor that it's always called
(defining the default values of class variables). ``super`` is used to call the
explicit constructor::

    func _init(arg):
       super("some_default", arg) # Call the custom base constructor.

This is better explained through examples. Consider this scenario::

    # State.gd (inherited class).
    var entity = null
    var message = null


    func _init(e=null):
        entity = e


    func enter(m):
        message = m


    # Idle.gd (inheriting class).
    extends "State.gd"


    func _init(e=null, m=null):
        super(e)
        # Do something with 'e'.
        message = m

There are a few things to keep in mind here:

1. If the inherited class (``State.gd``) defines a ``_init`` constructor that takes
   arguments (``e`` in this case), then the inheriting class (``Idle.gd``) *must*
   define ``_init`` as well and pass appropriate parameters to ``_init`` from ``State.gd``.
2. ``Idle.gd`` can have a different number of arguments than the base class ``State.gd``.
3. In the example above, ``e`` passed to the ``State.gd`` constructor is the same ``e`` passed
   in to ``Idle.gd``.
4. If ``Idle.gd``'s ``_init`` constructor takes 0 arguments, it still needs to pass some value
   to the ``State.gd`` base class, even if it does nothing. This brings us to the fact that you
   can pass expressions to the base constructor as well, not just variables, e.g.::

    # Idle.gd

    func _init():
        super(5)

Inner classes
^^^^^^^^^^^^^

A class file can contain inner classes. Inner classes are defined using the
``class`` keyword. They are instanced using the ``ClassName.new()``
function.

::

    # Inside a class file.

    # An inner class in this class file.
    class SomeInnerClass:
        var a = 5


        func print_value_of_a():
            print(a)


    # This is the constructor of the class file's main class.
    func _init():
        var c = SomeInnerClass.new()
        c.print_value_of_a()

.. _doc_gdscript_classes_as_resources:

Classes as resources
^^^^^^^^^^^^^^^^^^^^

Classes stored as files are treated as :ref:`resources <class_GDScript>`. They
must be loaded from disk to access them in other classes. This is done using
either the ``load`` or ``preload`` functions (see below). Instancing of a loaded
class resource is done by calling the ``new`` function on the class object::

    # Load the class resource when calling load().
    var MyClass = load("myclass.gd")

    # Preload the class only once at compile time.
    const MyClass = preload("myclass.gd")


    func _init():
        var a = MyClass.new()
        a.some_function()

Exports
~~~~~~~

.. note::

    Documentation about exports has been moved to :ref:`doc_gdscript_exports`.


.. _doc_gdscript_basics_setters_getters:

Properties (setters and getters)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sometimes, you want a class' member variable to do more than just hold data and actually perform
some validation or computation whenever its value change. It may also be desired to
encapsulate its access in some way.

For this, GDScript provides a special syntax to define properties using the ``set`` and ``get``
keywords after a variable declaration. Then you can define a code block that will be executed
when the variable is accessed or assigned.

Example::

    var milliseconds: int = 0
    var seconds: int:
        get:
            return milliseconds / 1000
        set(value):
            milliseconds = value * 1000

Using the variable name inside its own setter or getter will directly access the underlying member, so it
won't generate infinite recursion and saves you from explicitly declaring another variable::

    signal changed(new_value)
    var warns_when_changed = "some value":
        get:
            return warns_when_changed
        set(value):
            changed.emit(value)
            warns_when_changed = value

This backing member variable is not created if you don't use it.

.. note::
    Unlike ``setget`` in previous Godot versions, ``set`` and ``get`` methods are **always** called,
    even when accessed inside the same class (with or without prefixing with ``self.``). This makes the behavior
    consistent. If you need direct access to the value, use another variable for direct access and make the property
    code use that name.

In case you want to split the code from the variable declaration or you need to share the code across multiple properties,
you can use a different notation to use existing class functions::

    var my_prop:
        get = get_my_prop, set = set_my_prop

This can also be done in the same line.

.. _doc_gdscript_tool_mode:

Tool mode
~~~~~~~~~

By default, scripts don't run inside the editor and only the exported
properties can be changed. In some cases, it is desired that they do run
inside the editor (as long as they don't execute game code or manually
avoid doing so). For this, the ``@tool`` annotation exists and must be
placed at the top of the file::

    @tool
    extends Button

    func _ready():
        print("Hello")


See :ref:`doc_running_code_in_the_editor` for more information.

.. warning:: Be cautious when freeing nodes with ``queue_free()`` or ``free()``
             in a tool script (especially the script's owner itself). As tool
             scripts run their code in the editor, misusing them may lead to
             crashing the editor.

.. _doc_gdscript_basics_memory_management:

Memory management
~~~~~~~~~~~~~~~~~

Godot implements reference counting to free certain instances that are no longer
used, instead of a garbage collector, or requiring purely manual management.
Any instance of the :ref:`class_RefCounted` class (or any class that inherits
it, such as :ref:`class_Resource`) will be freed automatically when no longer
in use. For an instance of any class that is not a :ref:`class_RefCounted`
(such as :ref:`class_Node` or the base :ref:`class_Object` type), it will
remain in memory until it is deleted with ``free()`` (or ``queue_free()``
for Nodes).

.. note::

    If a :ref:`class_Node` is deleted via ``free()`` or ``queue_free()``,
    all of its children will also recursively be deleted.

To avoid reference cycles that can't be freed, a :ref:`class_WeakRef`
function is provided for creating weak references, which allow access
to the object without preventing a :ref:`class_RefCounted` from freeing.
Here is an example:


::

    extends Node

    var my_file_ref

    func _ready():
        var f = File.new()
        my_file_ref = weakref(f)
        # the File class inherits RefCounted, so it will be freed when not in use

        # the WeakRef will not prevent f from being freed when other_node is finished
        other_node.use_file(f)

    func _this_is_called_later():
        var my_file = my_file_ref.get_ref()
        if my_file:
            my_file.close()

Alternatively, when not using references, the
``is_instance_valid(instance)`` can be used to check if an object has been
freed.

.. _doc_gdscript_signals:

Signals
~~~~~~~

Signals are a tool to emit messages from an object that other objects can react
to. To create custom signals for a class, use the ``signal`` keyword.

::

   extends Node


   # A signal named health_depleted.
   signal health_depleted

.. note::

   Signals are a `Callback
   <https://en.wikipedia.org/wiki/Callback_(computer_programming)>`_
   mechanism. They also fill the role of Observers, a common programming
   pattern. For more information, read the `Observer tutorial
   <https://gameprogrammingpatterns.com/observer.html>`_ in the
   Game Programming Patterns ebook.

You can connect these signals to methods the same way you connect built-in
signals of nodes like :ref:`class_Button` or :ref:`class_RigidBody3D`.

In the example below, we connect the ``health_depleted`` signal from a
``Character`` node to a ``Game`` node. When the ``Character`` node emits the
signal, the game node's ``_on_Character_health_depleted`` is called::

    # Game.gd

    func _ready():
        var character_node = get_node('Character')
        character_node.health_depleted.connect(_on_Character_health_depleted)


    func _on_Character_health_depleted():
        get_tree().reload_current_scene()

You can emit as many arguments as you want along with a signal.

Here is an example where this is useful. Let's say we want a life bar on screen
to react to health changes with an animation, but we want to keep the user
interface separate from the player in our scene tree.

In our ``Character.gd`` script, we define a ``health_changed`` signal and emit
it with :ref:`Signal.emit() <class_Signal_method_emit>`, and from
a ``Game`` node higher up our scene tree, we connect it to the ``Lifebar`` using
the :ref:`Signal.connect() <class_Signal_method_connect>` method::

    # Character.gd

    ...
    signal health_changed


    func take_damage(amount):
        var old_health = health
        health -= amount

        # We emit the health_changed signal every time the
        # character takes damage.
        health_changed.emit(old_health, health)
    ...

::

    # Lifebar.gd

    # Here, we define a function to use as a callback when the
    # character's health_changed signal is emitted.

    ...
    func _on_Character_health_changed(old_value, new_value):
        if old_value > new_value:
            progress_bar.modulate = Color.red
        else:
            progress_bar.modulate = Color.green

        # Imagine that `animate` is a user-defined function that animates the
        # bar filling up or emptying itself.
        progress_bar.animate(old_value, new_value)
    ...

In the ``Game`` node, we get both the ``Character`` and ``Lifebar`` nodes, then
connect the character, that emits the signal, to the receiver, the ``Lifebar``
node in this case.

::

    # Game.gd

    func _ready():
        var character_node = get_node('Character')
        var lifebar_node = get_node('UserInterface/Lifebar')

        character_node.health_changed.connect(lifebar_node._on_Character_health_changed)

This allows the ``Lifebar`` to react to health changes without coupling it to
the ``Character`` node.

You can write optional argument names in parentheses after the signal's
definition::

    # Defining a signal that forwards two arguments.
    signal health_changed(old_value, new_value)

These arguments show up in the editor's node dock, and Godot can use them to
generate callback functions for you. However, you can still emit any number of
arguments when you emit signals; it's up to you to emit the correct values.

.. image:: img/gdscript_basics_signals_node_tab_1.png

GDScript can bind an array of values to connections between a signal
and a method. When the signal is emitted, the callback method receives
the bound values. These bound arguments are unique to each connection,
and the values will stay the same.

You can use this array of values to add extra constant information to the
connection if the emitted signal itself doesn't give you access to all the data
that you need.

Building on the example above, let's say we want to display a log of the damage
taken by each character on the screen, like ``Player1 took 22 damage.``. The
``health_changed`` signal doesn't give us the name of the character that took
damage. So when we connect the signal to the in-game console, we can add the
character's name in the binds array argument::

    # Game.gd

    func _ready():
        var character_node = get_node('Character')
        var battle_log_node = get_node('UserInterface/BattleLog')

        character_node.health_changed.connect(battle_log_node._on_Character_health_changed, [character_node.name])

Our ``BattleLog`` node receives each element in the binds array as an extra argument::

    # BattleLog.gd

    func _on_Character_health_changed(old_value, new_value, character_name):
        if not new_value <= old_value:
            return

        var damage = old_value - new_value
        label.text += character_name + " took " + str(damage) + " damage."


Awaiting for signals
~~~~~~~~~~~~~~~~~~~~

The ``await`` keyword can be used to create `coroutines <https://en.wikipedia.org/wiki/Coroutine>`_
which waits until a signal is emitted before continuing execution. Using the ``await`` keyword with a signal or a
call to a function that is also a coroutine will immediately return the control to the caller. When the signal is
emitted (or the called coroutine finishes), it will resume execution from the point on where it stopped.

For example, to stop execution until the user presses a button, you can do something like this::

    func wait_confirmation():
        print("Prompting user")
        await $Button.button_up # Waits for the button_up signal from Button node.
        print("User confirmed")
        return true

In this case, the ``wait_confirmation`` becomes a coroutine, which means that the caller also needs to await for it::

    func request_confirmation():
        print("Will ask the user")
        var confirmed = await wait_confirmation()
        if confirmed:
            print("User confirmed")
        else:
            print("User cancelled")

Note that requesting a coroutine's return value without ``await`` will trigger an error::

    func wrong():
        var confirmed = wait_confirmation() # Will give an error.

However, if you don't depend on the result, you can just call it asynchronously, which won't stop execution and won't
make the current function a coroutine::

    func okay():
        wait_confirmation()
        print("This will be printed immediately, before the user press the button.")

If you use await with an expression that isn't a signal nor a coroutine, the value will be returned immediately and the
function won't give the control back to the caller::

    func no_wait():
        var x = await get_five()
        print("This doesn't make this function a coroutine.")

    func get_five():
        return 5

This also means that returning a signal from a function that isn't a coroutine will make the caller await on that signal::

    func get_signal():
        return $Button.button_up

    func wait_button():
        await get_signal()
        print("Button was pressed")

.. note:: Unlike ``yield`` in previous Godot versions, you cannot obtain the function state object.
          This is done to ensure type safety.
          With this type safety in place, a function cannot say that it returns an ``int`` while it actually returns a function state object
          during runtime.

Assert keyword
~~~~~~~~~~~~~~

The ``assert`` keyword can be used to check conditions in debug builds. These
assertions are ignored in non-debug builds. This means that the expression
passed as argument won't be evaluated in a project exported in release mode.
Due to this, assertions must **not** contain expressions that have
side effects. Otherwise, the behavior of the script would vary
depending on whether the project is run in a debug build.

::

    # Check that 'i' is 0. If 'i' is not 0, an assertion error will occur.
    assert(i == 0)

When running a project from the editor, the project will be paused if an
assertion error occurs.

You can optionally pass a custom error message to be shown if the assertion
fails::

    assert(enemy_power < 256, "Enemy is too powerful!")
