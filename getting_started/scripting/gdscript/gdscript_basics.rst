.. _doc_gdscript:

GDScript basics
===============

Introduction
------------

*GDScript* is a high-level, dynamically typed programming language used to
create content. It uses a syntax similar to
`Python <https://en.wikipedia.org/wiki/Python_%28programming_language%29>`_
(blocks are indent-based and many keywords are similar). Its goal is
to be optimized for and tightly integrated with Godot Engine, allowing great
flexibility for content creation and integration.

History
~~~~~~~

.. note::

    Documentation about GDScript's history has been moved to the
    :ref:`Frequently Asked Questions <doc_faq_what_is_gdscript>`.

Example of GDScript
~~~~~~~~~~~~~~~~~~~

Some people can learn better by taking a look at the syntax, so
here's a simple example of how GDScript looks.

::

    # A file is a class!

    # Inheritance

    extends BaseClass

    # (optional) class definition with a custom icon

    class_name MyClass, "res://path/to/optional/icon.svg"


    # Member variables

    var a = 5
    var s = "Hello"
    var arr = [1, 2, 3]
    var dict = {"key": "value", 2: 3}
    var typed_var: int
    var inferred_type := "String"

    # Constants

    const ANSWER = 42
    const THE_NAME = "Charly"

    # Enums

    enum {UNIT_NEUTRAL, UNIT_ENEMY, UNIT_ALLY}
    enum Named {THING_1, THING_2, ANOTHER_THING = -1}

    # Built-in vector types

    var v2 = Vector2(1, 2)
    var v3 = Vector3(1, 2, 3)


    # Function

    func some_function(param1, param2):
        var local_var = 5

        if param1 < local_var:
            print(param1)
        elif param2 > 5:
            print(param2)
        else:
            print("Fail!")

        for i in range(20):
            print(i)

        while param2 != 0:
            param2 -= 1

        var local_var2 = param1 + 3
        return local_var2


    # Functions override functions with the same name on the base/parent class.
    # If you still want to call them, use '.' (like 'super' in other languages).

    func something(p1, p2):
        .something(p1, p2)


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

Below is an overview of GDScript. Details such as which
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

+------------+---------------------------------------------------------------------------------------------------------------+
|  Keyword   | Description                                                                                                   |
+============+===============================================================================================================+
| if         | See :ref:`if/else/elif <doc_gdscript_if_else_elif>`.                                                          |
+------------+---------------------------------------------------------------------------------------------------------------+
| elif       | See :ref:`if/else/elif <doc_gdscript_if_else_elif>`.                                                          |
+------------+---------------------------------------------------------------------------------------------------------------+
| else       | See :ref:`if/else/elif <doc_gdscript_if_else_elif>`.                                                          |
+------------+---------------------------------------------------------------------------------------------------------------+
| for        | See :ref:`for <doc_gdscript_for>`.                                                                            |
+------------+---------------------------------------------------------------------------------------------------------------+
| while      | See :ref:`while <doc_gdscript_while>`.                                                                        |
+------------+---------------------------------------------------------------------------------------------------------------+
| match      | See :ref:`match <doc_gdscript_match>`.                                                                        |
+------------+---------------------------------------------------------------------------------------------------------------+
| break      | Exits the execution of the current ``for`` or ``while`` loop.                                                 |
+------------+---------------------------------------------------------------------------------------------------------------+
| continue   | Immediately skips to the next iteration of the ``for`` or ``while`` loop.                                     |
+------------+---------------------------------------------------------------------------------------------------------------+
| pass       | Used where a statement is required syntactically but execution of code is undesired, e.g. in empty functions. |
|            | See :ref:`functions <doc_gdscript_functions>`.                                                                |
+------------+---------------------------------------------------------------------------------------------------------------+
| func       | Defines a function. See :ref:`functions <doc_gdscript_functions>`.                                            |
+------------+---------------------------------------------------------------------------------------------------------------+
| return     | Returns a value from a function. See :ref:`functions <doc_gdscript_functions>`.                               |
+------------+---------------------------------------------------------------------------------------------------------------+
| class      | Defines a class. A class is a template for creating objects relevant to your program. See                     |
|            | :ref:`Classes <doc_gdscript_classes>`.                                                                        |
+------------+---------------------------------------------------------------------------------------------------------------+
| extends    | Defines the class to extend with the current class. See :ref:`Classes <doc_gdscript_classes>`.                |
+------------+---------------------------------------------------------------------------------------------------------------+
| is         | Tests whether a variable extends a given class, or is of a given built-in type.                               |
+------------+---------------------------------------------------------------------------------------------------------------+
| as         | Cast the value to a given type if possible. See :ref:`Casting <doc_gdscript_casting>`.                        |
+------------+---------------------------------------------------------------------------------------------------------------+
| self       | Refers to current class instance.                                                                             |
+------------+---------------------------------------------------------------------------------------------------------------+
| tool       | Executes the script in the editor. See :ref:`Tool mode <doc_gdscript_tool_mode>`.                             |
+------------+---------------------------------------------------------------------------------------------------------------+
| signal     | Defines a signal. See :ref:`doc_gdscript_signals`.                                                            |
+------------+---------------------------------------------------------------------------------------------------------------+
| static     | Defines a static function. Static member variables are not allowed. See                                       |
|            | :ref:`Static functions <doc_gdscript_static_functions>`.                                                      |
+------------+---------------------------------------------------------------------------------------------------------------+
| const      | Defines a constant. See :ref:`functions <doc_gdscript_constants>`.                                            |
+------------+---------------------------------------------------------------------------------------------------------------+
| enum       | Defines an enum. See :ref:`enums <doc_gdscript_enums>`.                                                       |
+------------+---------------------------------------------------------------------------------------------------------------+
| var        | Defines a variable. See :ref:`variables <doc_gdscript_variables>`.                                            |
+------------+---------------------------------------------------------------------------------------------------------------+
| onready    | Initializes a variable once the Node the script is attached to and its children are part of the scene tree.   |
|            | See :ref:`Onready <doc_gdscript_onready>`.                                                                    |
+------------+---------------------------------------------------------------------------------------------------------------+
| export     | Saves a variable along with the resource it's attached to and makes it visible and modifiable in the editor.  |
|            | See :ref:`Exports <doc_gdscript_exports>`.                                                                    |
+------------+---------------------------------------------------------------------------------------------------------------+
| setget     | Defines setter and getter functions for a variable. See :ref:`Setters/getters <doc_gdscript_setters_getters>`.|
+------------+---------------------------------------------------------------------------------------------------------------+
| breakpoint | Editor helper for debugger breakpoints.                                                                       |
+------------+---------------------------------------------------------------------------------------------------------------+
| preload    | Preloads a class or variable. See :ref:`Classes as resources <doc_gdscript_classes_as_resources>`.            |
+------------+---------------------------------------------------------------------------------------------------------------+
| yield      | Coroutine support. See :ref:`Coroutines with yield <doc_gdscript_yield>`.                                     |
+------------+---------------------------------------------------------------------------------------------------------------+
| assert     | Asserts a condition, logs error on failure. Ignored in non-debug builds.                                      |
|            | See :ref:`Assert <doc_gdscript_assert>`.                                                                      |
+------------+---------------------------------------------------------------------------------------------------------------+
| remote     | Networking RPC annotation. See :ref:`high-level multiplayer docs <doc_high_level_multiplayer>`.               |
+------------+---------------------------------------------------------------------------------------------------------------+
| master     | Networking RPC annotation. See :ref:`high-level multiplayer docs <doc_high_level_multiplayer>`.               |
+------------+---------------------------------------------------------------------------------------------------------------+
| puppet     | Networking RPC annotation. See :ref:`high-level multiplayer docs <doc_high_level_multiplayer>`.               |
+------------+---------------------------------------------------------------------------------------------------------------+
| remotesync | Networking RPC annotation. See :ref:`high-level multiplayer docs <doc_high_level_multiplayer>`.               |
+------------+---------------------------------------------------------------------------------------------------------------+
| mastersync | Networking RPC annotation. See :ref:`high-level multiplayer docs <doc_high_level_multiplayer>`.               |
+------------+---------------------------------------------------------------------------------------------------------------+
| puppetsync | Networking RPC annotation. See :ref:`high-level multiplayer docs <doc_high_level_multiplayer>`.               |
+------------+---------------------------------------------------------------------------------------------------------------+
| PI         | PI constant.                                                                                                  |
+------------+---------------------------------------------------------------------------------------------------------------+
| TAU        | TAU constant.                                                                                                 |
+------------+---------------------------------------------------------------------------------------------------------------+
| INF        | Infinity constant. Used for comparisons.                                                                      |
+------------+---------------------------------------------------------------------------------------------------------------+
| NAN        | NAN (not a number) constant. Used for comparisons.                                                            |
+------------+---------------------------------------------------------------------------------------------------------------+

Operators
~~~~~~~~~

The following is the list of supported operators and their precedence.

+---------------------------------------------------------------+-----------------------------------------+
| **Operator**                                                  | **Description**                         |
+---------------------------------------------------------------+-----------------------------------------+
| ``x[index]``                                                  | Subscription (highest priority)         |
+---------------------------------------------------------------+-----------------------------------------+
| ``x.attribute``                                               | Attribute reference                     |
+---------------------------------------------------------------+-----------------------------------------+
| ``foo()``                                                     | Function call                           |
+---------------------------------------------------------------+-----------------------------------------+
| ``is``                                                        | Instance type checker                   |
+---------------------------------------------------------------+-----------------------------------------+
| ``~``                                                         | Bitwise NOT                             |
+---------------------------------------------------------------+-----------------------------------------+
| ``-x``                                                        | Negative / Unary negation               |
+---------------------------------------------------------------+-----------------------------------------+
| ``*`` ``/`` ``%``                                             | Multiplication / Division / Remainder   |
|                                                               |                                         |
|                                                               | These operators have the same behavior  |
|                                                               | as C++. Integer division is truncated   |
|                                                               | rather than returning a fractional      |
|                                                               | number, and the % operator is only      |
|                                                               | available for ints ("fmod" for floats)  |
+---------------------------------------------------------------+-----------------------------------------+
| ``+``                                                         | Addition / Concatenation of arrays      |
+---------------------------------------------------------------+-----------------------------------------+
| ``-``                                                         | Subtraction                             |
+---------------------------------------------------------------+-----------------------------------------+
| ``<<`` ``>>``                                                 | Bit shifting                            |
+---------------------------------------------------------------+-----------------------------------------+
| ``&``                                                         | Bitwise AND                             |
+---------------------------------------------------------------+-----------------------------------------+
| ``^``                                                         | Bitwise XOR                             |
+---------------------------------------------------------------+-----------------------------------------+
| ``|``                                                         | Bitwise OR                              |
+---------------------------------------------------------------+-----------------------------------------+
| ``<`` ``>`` ``==`` ``!=`` ``>=`` ``<=``                       | Comparisons                             |
+---------------------------------------------------------------+-----------------------------------------+
| ``in``                                                        | Content test                            |
+---------------------------------------------------------------+-----------------------------------------+
| ``!`` ``not``                                                 | Boolean NOT                             |
+---------------------------------------------------------------+-----------------------------------------+
| ``and`` ``&&``                                                | Boolean AND                             |
+---------------------------------------------------------------+-----------------------------------------+
| ``or`` ``||``                                                 | Boolean OR                              |
+---------------------------------------------------------------+-----------------------------------------+
| ``if x else``                                                 | Ternary if/else                         |
+---------------------------------------------------------------+-----------------------------------------+
| ``as``                                                        | Type casting                            |
+---------------------------------------------------------------+-----------------------------------------+
| ``=`` ``+=`` ``-=`` ``*=`` ``/=`` ``%=`` ``&=`` ``|=``        | Assignment (lowest priority)            |
+---------------------------------------------------------------+-----------------------------------------+

Literals
~~~~~~~~

+--------------------------+----------------------------------------+
| **Literal**              | **Type**                               |
+--------------------------+----------------------------------------+
| ``45``                   | Base 10 integer                        |
+--------------------------+----------------------------------------+
| ``0x8F51``               | Base 16 (hexadecimal) integer          |
+--------------------------+----------------------------------------+
| ``0b101010``             | Base 2 (binary) integer                |
+--------------------------+----------------------------------------+
| ``3.14``, ``58.1e-10``   | Floating-point number (real)           |
+--------------------------+----------------------------------------+
| ``"Hello"``, ``"Hi"``    | Strings                                |
+--------------------------+----------------------------------------+
| ``"""Hello"""``          | Multiline string                       |
+--------------------------+----------------------------------------+
| ``@"Node/Label"``        | :ref:`class_NodePath` or StringName    |
+--------------------------+----------------------------------------+
| ``$NodePath``            | Shorthand for ``get_node("NodePath")`` |
+--------------------------+----------------------------------------+

Comments
~~~~~~~~

Anything from a ``#`` to the end of the line is ignored and is
considered a comment.

::

    # This is a comment and will be ignored.

.. _doc_gdscript_builtin_types:

Built-in types
--------------

Data you create in Godot will be of a certain type (a whole number or a string
of characters for example). While you can create your own data types to 
describe your data, Godot has a set of built-in types as described 
below for you to useful.

Advanced note : Built-in types are stack-allocated. They are passed as values. 
This means a copy is created on each assignment or when passing them as 
arguments to functions. The only exceptions are ``Array``\ s and 
``Dictionaries``, which are passed by reference so they are shared. (Pooled 
arrays such as ``PackedByteArray`` are still passed as values.)

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

GDScript also supports :ref:`doc_gdscript_printf`.

Vector built-in types
~~~~~~~~~~~~~~~~~~~~~

:ref:`Vector2 <class_Vector2>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

2D vector type containing ``x`` and ``y`` fields. Can also be
accessed as an array.

:ref:`Rect2 <class_Rect2>`
^^^^^^^^^^^^^^^^^^^^^^^^^^

2D Rectangle type containing two vectors fields: ``position`` and ``size``.
Also contains an ``end`` field which is ``position + size``.

:ref:`Vector3 <class_Vector3>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

3D vector type containing ``x``, ``y`` and ``z`` fields. This can also
be accessed as an array.

:ref:`Transform2D <class_Transform2D>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

3×2 matrix used for 2D transforms.

:ref:`Plane <class_Plane>`
^^^^^^^^^^^^^^^^^^^^^^^^^^

3D Plane type in normalized form that contains a ``normal`` vector field
and a ``d`` scalar distance.

:ref:`Quat <class_Quat>`
^^^^^^^^^^^^^^^^^^^^^^^^

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

:ref:`Transform <class_Transform>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
    arr = [1, 2, 3] # arr now contains 3 separate values - 1, 2 and 3.
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

Data
----

.. _doc_gdscript_variables:

Variables
~~~~~~~~~

A variable is some data that is stored with an associated label. For example
you could store a variable "fruit" which contained the contents "apple".
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
    var my_node: Node = Sprite.new()

If the variable is initialized within the declaration, the type can be inferred, so
it's possible to omit the type name::

    var my_vector2 := Vector2() # 'my_vector2' is of type 'Vector2'.
    var my_node := Sprite.new() # 'my_node' is of type 'Sprite'.

Type inference is only possible if the assigned value has a defined type, otherwise
it will raise an error.

Valid types are:

- Built-in types (Array, Vector2, int, String, etc.).
- Engine classes (Node, Resource, Reference, etc.).
- Constant names if they contain a script resource (``MyScript`` if you declared ``const MyScript = preload("res://my_script.gd")``).
- Other classes in the same script, respecting scope (``InnerClass.NestedClass`` if you declared ``class NestedClass`` inside the ``class InnerClass`` in the same scope).
- Script classes declared with the ``class_name`` keyword.

.. _doc_gdscript_casting:

Casting
^^^^^^^

Values assigned to typed variables must have a compatible type. If it's needed to
coerce a value to be of a certain type, in particular for object types, you can
use the casting operator ``as``.

Casting between object types results in the same object if the value is of the
same type or a subtype of the cast type.

::

    var my_node2D: Node2D
    my_node2D = $Sprite as Node2D # Works since Sprite is a subtype of Node2D.

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

    # Will infer the variable to be of type Sprite.
    var my_sprite := $Character as Sprite

    # Will fail if $AnimPlayer is not an AnimationPlayer, even if it has the method 'play()'.
    ($AnimPlayer as AnimationPlayer).play("walk")

.. _doc_gdscript_constants:

Constants
~~~~~~~~~

Constants are similar to variables, but must be a fixed value or constant
expression, and must be assigned on initialization.

::

    const A = 5
    const B = Vector2(20, 20)
    const C = 10 + 20 # Constant expression.
    const D = Vector2(20, 30).x # Constant expression: 20.
    const E = [1, 2, 3, 4][0] # Constant expression: 1.
    const F = sin(20) # 'sin()' can be used in constant expressions.
    const G = x + 20 # Invalid; this is not a constant expression as 'x' is not defined!
    const H = A + 20 # Constant expression: 25 (`A` is a constant).

Although the type of constant is inferred from the assigned value, it's also
possible to add an explicit type specification::

    const A: int = 5
    const B: Vector2 = Vector2()

Assigning a value of an incompatible type will raise an error.

.. note::

    Since arrays and dictionaries are passed by reference, constants are "flat".
    This means that if you declare a constant array or dictionary, it can still
    be modified afterwards. They can't be reassigned with another value though.

.. _doc_gdscript_enums:

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

.. _doc_gdscript_functions:

Functions
~~~~~~~~~

A function is a block of code that performs a particular task. Separating code
into functions makes it more readable and allows for common code to be reused
rather than rewritten every time it is needed.

Functions always belong to a `class <doc_gdscript_classes>`_. The scope priority for
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

    void_function() -> void:
        return # Can't return a value

.. note:: Non-void functions must **always** return a value, so if your code has
          branching statements (such as an ``if``/``else`` construct), all the
          possible paths must have a return. E.g., if you have a ``return``
          inside an ``if`` block but not after it, the editor will raise an
          error because if the block is not executed, the function won't have a
          valid value to return.

TALK ABOUT PASS

Referencing functions
^^^^^^^^^^^^^^^^^^^^^

Contrary to Python, functions are *not* first-class objects in GDScript. This
means they cannot be stored in variables, passed as an argument to another
function, or be returned from other functions. This is for performance reasons.

To reference a function by name at run-time, (e.g. to store it in a variable, 
or pass it to another function as an argument)  the ``call`` or ``funcref`` 
helpers are required::

    # Call a function by name in one step.
    my_node.call("my_function", args)

    # Store a function reference.
    var my_func = funcref(my_node, "my_function")
    # Call stored function reference.
    my_func.call_func(args)

.. _doc_gdscript_static_functions:

Static functions
^^^^^^^^^^^^^^^^

A function can be declared static. When a function is static, it has no
access to the instance member variables or ``self``. This is mainly
useful to make libraries of helper functions::

    static func sum2(a, b):
        return a + b


Statements and control flow
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Statements are standard and can be assignments, function calls, control
flow structures, etc (see below). ``;`` as a statement separator is
entirely optional.

.. _doc_gdscript_if_else_elif:

if/else/elif
^^^^^^^^^^^^

Simple conditions are created by using the ``if``/``else``/``elif`` syntax.
Parenthesis around conditions are allowed, but not required. Given the
nature of the tab-based indentation, ``elif`` can be used instead of
``else``/``if`` to maintain a level of indentation.

::

    if [expression]:
        statement(s)
    elif [expression]:
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

    var x = [value] if [expression] else [value]
    y += 3 if y < 10 else -1

.. _doc_gdscript_while:

while
^^^^^

Simple loops are created by using ``while`` syntax. Loops can be broken
using ``break`` or continued using ``continue``:

::

    while [expression]:
        statement(s)

.. _doc_gdscript_for:

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
        statement # Similar to range(3)

    for i in 2.2:
        statement # Similar to range(ceil(2.2))

.. _doc_gdscript_match:

match
^^^^^

A ``match`` statement is used to branch execution of a program.
It's the equivalent of the ``switch`` statement found in many other languages, but offers some additional features.

Basic syntax::

    match [expression]:
        [pattern](s):
            [block]
        [pattern](s):
            [block]
        [pattern](s):
            [block]


**Crash-course for people who are familiar with switch statements**:

1. Replace ``switch`` with ``match``.
2. Remove ``case``.
3. Remove any ``break``\ s. If you don't want to ``break`` by default, you can use ``continue`` for a fallthrough.
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
            TYPE_REAL:
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

