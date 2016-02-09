.. _doc_gdscript:

GDScript
========

Introduction
------------

GDScript is a high level, dynamically typed programming language used to
create content. It uses a syntax that is very similar to the Python
language (blocks are indent-based) and its goal is to be very optimal
and tightly integrated with the engine, allowing great flexibility for
content creation and integration.

History
-------

Initially, Godot was designed to support multiple scripting languages
(this ability still exists today). However, only GDScript is in use
right now. There is a little history behind this.

In the early days, the engine used the `Lua <http://www.lua.org>`__
scripting language. Lua is fast, but creating bindings to an object
oriented system (by using fallbacks) was complex and slow and took an
enormous amount of code. After some experiments with
`Python <http://www.python.org>`__, it also proved difficult to embed.

The last third party scripting language that was used for shipped games
was `Squirrel <http://squirrel-lang.org>`__, but it was dropped as well.
At that point, it became evident that Godot would work more optimally by
using a built-in scripting language, as the following barriers were met:

-  Godot embeds scripts in nodes, most languages are not designed with
   this in mind.
-  Godot uses several built-in data types for 2D and 3D math, script
   languages do not provide this, and binding them is inefficient.
-  Godot uses threads heavily for lifting and initializing data from the
   net or disk, script interpreters for common languages are not
   friendly to this.
-  Godot already has a memory management model for resources, most
   script languages provide their own, which resulted in duplicate
   effort and bugs.
-  Binding code is always messy and results in several failure points,
   unexpected bugs and generally low maintainability.

Finally, GDScript was written as a custom solution. The language and
interpreter for it ended up being smaller than the binding code itself
for Lua and Squirrel, and equally as functional. With time, having a
built-in language has proven to be a huge advantage.

Example
-------

Some people can learn better by just taking a look at the syntax, so
here's a simple example of how it looks.

::

    # a file is a class!

    # inheritance

    extends BaseClass

    # member variables

    var a = 5 
    var s = "Hello"
    var arr = [1, 2, 3]
    var dict = {"key":"value", 2:3}

    # constants

    const answer = 42
    const thename = "Charly"

    # built-in vector types

    var v2 = Vector2(1, 2)
    var v3 = Vector3(1, 2, 3)

    # function

    func some_function(param1, param2):
        var local_var = 5

        if param1 < local_var:
            print(param1)
        elif param2 > 5:
            print(param2)
        else:
            print("fail!")

        for i in range(20):
            print(i)

        while(param2 != 0):
            param2 -= 1

        var local_var2 = param1+3
        return local_var2


    # subclass

    class Something:
        var a = 10

    # constructor

    func _init():
        print("constructed!")
        var lv = Something.new()
        print(lv.a)

If you have previous experience with statically typed languages such as
C, C++, or C# but never used a dynamically typed one, it is advised you
read this tutorial: :ref:`doc_gdscript_more_efficiently`.

Language
--------

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

Operators
~~~~~~~~~

The following is the list of supported operators and their precedence
(TODO, change since this was made to reflect python operators)

+---------------------------------------------------------------+-----------------------------------------+
| **Operator**                                                  | **Description**                         |
+---------------------------------------------------------------+-----------------------------------------+
| ``x[index]``                                                  | Subscription, Highest Priority          |
+---------------------------------------------------------------+-----------------------------------------+
| ``x.attribute``                                               | Attribute Reference                     |
+---------------------------------------------------------------+-----------------------------------------+
| ``extends``                                                   | Instance Type Checker                   |
+---------------------------------------------------------------+-----------------------------------------+
| ``~``                                                         | Bitwise NOT                             |
+---------------------------------------------------------------+-----------------------------------------+
| ``-x``                                                        | Negative                                |
+---------------------------------------------------------------+-----------------------------------------+
| ``*`` ``/`` ``%``                                             | Multiplication / Division / Remainder   |
+---------------------------------------------------------------+-----------------------------------------+
| ``+`` ``-``                                                   | Addition / Subtraction                  |
+---------------------------------------------------------------+-----------------------------------------+
| ``<<`` ``>>``                                                 | Bit Shifting                            |
+---------------------------------------------------------------+-----------------------------------------+
| ``&``                                                         | Bitwise AND                             |
+---------------------------------------------------------------+-----------------------------------------+
| ``^``                                                         | Bitwise XOR                             |
+---------------------------------------------------------------+-----------------------------------------+
| ``&#124;``                                                    | Bitwise OR                              |
+---------------------------------------------------------------+-----------------------------------------+
| ``<`` ``>`` ``==`` ``!=`` ``>=`` ``<=``                       | Comparisons                             |
+---------------------------------------------------------------+-----------------------------------------+
| ``in``                                                        | Content Test                            |
+---------------------------------------------------------------+-----------------------------------------+
| ``!`` ``not``                                                 | Boolean NOT                             |
+---------------------------------------------------------------+-----------------------------------------+
| ``and`` ``&&``                                                | Boolean AND                             |
+---------------------------------------------------------------+-----------------------------------------+
| ``or`` ``&#124;&#124;``                                       | Boolean OR                              |
+---------------------------------------------------------------+-----------------------------------------+
| ``=`` ``+=`` ``-=`` ``*=`` ``/=`` ``%=`` ``&=`` ``&#124;=``   | Assignment, Lowest Priority             |
+---------------------------------------------------------------+-----------------------------------------+

Literals
~~~~~~~~

+--------------------------+--------------------------------+
| **Literal**              | **Type**                       |
+--------------------------+--------------------------------+
| ``45``                   | Base 10 integer                |
+--------------------------+--------------------------------+
| ``0x8F51``               | Base 16 (hex) integer          |
+--------------------------+--------------------------------+
| ``3.14``, ``58.1e-10``   | Floating point number (real)   |
+--------------------------+--------------------------------+
| ``"Hello"``, ``"Hi"``    | Strings                        |
+--------------------------+--------------------------------+
| ``"""Hello, Dude"""``    | Multiline string               |
+--------------------------+--------------------------------+
| ``&#64;"Node/Label"``    | NodePath or StringName         |
+--------------------------+--------------------------------+

Comments
~~~~~~~~

Anything from a ``#`` to the end of the line is ignored and is
considered a comment.

::

    # This is a comment

Multi-line comments can be created using """ (three quotes in a row) at
the beginning and end of a block of text.

::

    """ Everything on these 
    lines is considered
    a comment """

Built-In Types
--------------

Basic Built-In Types
~~~~~~~~~~~~~~~~~~~~

A variable in GDScript can be assigned to several built-in types.

null
^^^^

null is a data type that contains no information, nothing assigned, and
it's just empty. It can only be set to one value: ``null``.

bool
^^^^

The Boolean data type can only contain ``true`` or ``false``.

int
^^^

The integer data type can only contain integer numbers, (both negative
and positive).

float
^^^^^

Used to contain a floating point value (real numbers).

:ref:`String <class_String>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A sequence of characters in Unicode format. Strings can contain the
standard C escape sequences.

Vector Built-In Types
~~~~~~~~~~~~~~~~~~~~~

:ref:`Vector2 <class_Vector2>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

2D vector type containing ``x`` and ``y`` fields. Can alternatively
access fields as ``width`` and ``height`` for readability. Can also be
accessed as array.

:ref:`Rect2 <class_Rect2>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

2D Rectangle type containing two vectors fields: ``pos`` and ``size``.
Alternatively contains an ``end`` field which is ``pos+size``.

:ref:`Vector3 <class_Vector3>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

3D vector type containing ``x``, ``y`` and ``z`` fields. This can also
be accessed as an array.

:ref:`Matrix32 <class_Matrix32>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

3x2 matrix used for 2D transforms.

:ref:`Plane <class_Plane>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

3D Plane type in normalized form that contains a ``normal`` vector field
and a ``d`` scalar distance.

:ref:`Quat <class_Quat>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Quaternion is a datatype used for representing a 3D rotation. It's
useful for interpolating rotations.

:ref:`AABB <class_AABB>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Axis Aligned bounding box (or 3D box) contains 2 vectors fields: ``pos``
and ``size``. Alternatively contains an ``end`` field which is
``pos+size``. As an alias of this type, ``Rect3`` can be used
interchangeably.

:ref:`Matrix3 <class_Matrix3>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

3x3 matrix used for 3D rotation and scale. It contains 3 vector fields
(``x``, ``y`` and ``z``) and can also be accessed as an array of 3D
vectors.

:ref:`Transform <class_Transform>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

3D Transform contains a Matrix3 field ``basis`` and a Vector3 field
``origin``.

Engine Built-In Types
~~~~~~~~~~~~~~~~~~~~~

:ref:`Color <class_Color>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Color data type contains ``r``, ``g``, ``b``, and ``a`` fields. It can
also be accessed as ``h``, ``s``, and ``v`` for hue/saturation/value.

:ref:`Image <class_Image>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Contains a custom format 2D image and allows direct access to the
pixels.

:ref:`NodePath <class_NodePath>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Compiled path to a node used mainly in the scene system. It can be
easily assigned to, and from, a String.

:ref:`RID <class_RID>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Resource ID (RID). Servers use generic RIDs to reference opaque data.

:ref:`Object <class_Object>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Base class for anything that is not a built-in type.

:ref:`InputEvent <class_InputEvent>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Events from input devices are contained in very compact form in
InputEvent objects. Due to the fact that they can be received in high
amounts from frame to frame they are optimized as their own data type.

Container Built-In Types
~~~~~~~~~~~~~~~~~~~~~~~~

:ref:`Array <class_Array>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Generic sequence of objects. Its size can be changed to anything and
starts from index 0.

::

    var arr=[]
    arr=[1, 2, 3]
    arr[0] = "Hi!"

Arrays are allocated linearly in memory, so they are fast, but very
large arrays (more than tens of thousands of elements) may cause
fragmentation.

There are specialized arrays (listed below) for some built-in data types
which do not suffer from this and use less memory, but they are atomic
and generally run a little slower, so they are only justified for very
large amount of data.

:ref:`Dictionary <class_Dictionary>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Associative container which contains values referenced by unique keys.

::

    var d={4:5, "a key":"a value", 28:[1,2,3]}
    d["Hi!"] = 0

Lua-style table syntax is also supported, given that it's easier to
write and read:

::


    var d = {
        somekey = 2,
        otherkey = [2,3,4],
        morekey = "Hello"
    }

:ref:`ByteArray <class_ByteArray>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An array of bytes can only contain bytes (integers from 0 to 255).

This, and all of the following specialized array types, are optimized
for memory usage and can't fragment the memory.

:ref:`IntArray <class_IntArray>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Array of integers can only contain integers.

:ref:`FloatArray <class_FloatArray>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Array of floats can only contain floats.

:ref:`StringArray <class_StringArray>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Array of strings can only contain strings.

:ref:`Vector2Array <class_Vector2Array>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Array of Vector2 can only contain 2D Vectors.

:ref:`Vector3Array <class_Vector3Array>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Array of Vector3 can only contain 3D Vectors.

:ref:`ColorArray <class_ColorArray>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Array of Color can only contains colors.

Data
----

Variables
~~~~~~~~~

Variables can exist as class members or local to functions. They are
created with the ``var`` keyword and may, optionally, be assigned a
value upon initialization.

::

    var a  # data type is null by default
    var b = 5
    var c = 3.8
    var d = b + c  # variables are always initialized in order

Constants
~~~~~~~~~

Constants are similar to variables, but must be constants or constant
expressions and must be assigned on initialization.

::

    const a = 5
    const b = Vector2(20, 20)
    const c = 10 + 20 # constant expression
    const d = Vector2(20, 30).x  # constant expression: 20
    const e = [1, 2, 3, 4][0]  # constant expression: 1
    const f = sin(20)  # sin() can be used in constant expressions
    const g = x + 20  # invalid; this is not a constant expression!

Functions
~~~~~~~~~

Functions always belong to a class. The scope priority for variable
look-up is: local→class member→global. ``self`` is provided as an option
for accessing class members, but is not always required (and must *not*
be defined as the first parameter, like in Python). For performance
reasons, functions are not considered class members, so they can't be
referenced directly. A function can return at any point. The default
return value is null.

::

    func myfunction(a, b):
        print(a)
        print(b)
        return a + b  # return is optional; without it null is returned

Statements and Control Flow
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Statements are standard and can be assignments, function calls, control
flow structures, etc (see below). ``;`` as a statement separator is
entirely optional.

if/else/elif
^^^^^^^^^^^^

Simple conditions are created by using the *if/else/elif* syntax.
Parenthesis around statements is allowed, but not required. Given the
nature of the tab-based indentation, elif can be used instead of
else:/if: to maintain a level of indentation.

::

    if [expression]:
        statement(s)
    elif [expression]:
        statement(s)
    else:
        statement(s)

while
^^^^^

Simple loops are created by using *while* syntax. Loops can be broken
using *break* or continued using *continue*:

::

    while [expression]:
        statement(s)

for
^^^

To iterate through a range, such as an array or table, a *for* loop is
used. For loops store the index in the loop variable on each iteration.

::

    for i in [0, 1, 2]:
        statement  # loop iterates 3 times with i as 0, then 1 and finally 2

    var dict = {"a":0, "b":1, "c":2}
    for i in dict:
        print(dict[i])  # loop iterates the keys; with i being "a","b" and "c" it prints 0, 1 and 2.

    for i in range(3):
        statement  # similar to [0, 1, 2] but does not allocate an array

    for i in range(1,3):
        statement  # similar to [1, 2] but does not allocate an array

    for i in range(2,8,2):
        statement  # similar to [2, 4, 6] but does not allocate an array

Function Call on Base Class
^^^^^^^^^^^^^^^^^^^^^^^^^^^

To call a function on a base class (that was overridden in the current
one), prepend ``.`` to the function name:

::

    .basefunc()

However, remember that functions such as ``_init``, and most
notifications such as ``_enter_tree``, ``_exit_tree``, ``_process``,
``_fixed_process``, etc. are called in all base classes automatically,
so this should be only for calling functions you write yourself.

Classes
^^^^^^^

By default, the body of a script file is an unnamed class and it can
only be referenced externally as a resource or file. Class syntax is
meant to be very compact and can only contain member variables or
functions. Static functions are allowed, but not static members (this is
in the spirit of thread safety since scripts can be initialized in
separate threads without the user knowing). In the same way, member
variables (including arrays and dictionaries) are initialized every time
an instance is created.

Class File Example
~~~~~~~~~~~~~~~~~~

Imagine the following being stored in a file like myclass.gd.

::

    var a = 5

    func print_value_of_a():
        print(a)

Inheritance
~~~~~~~~~~~

A class file can inherit from a global class, another file or a subclass
inside another file. Multiple inheritance is not allowed. The
``extends`` syntax is used. Follows is 3 methods of using extends:

::

    # extend from some class (global)
    extends SomeClass 

::

    # optionally, extend from another file
    extends "somefile.gd" 

::

    # extend from a subclass in another file
    extends "somefile.gd".Subclass

Inheritance Testing
~~~~~~~~~~~~~~~~~~~

It's possible to check if an instance inherits from a given class. For
this the ``extends`` keyword can be used as an operator instead:

::

    const enemy_class = preload("enemy.gd")  # cache the enemy class

    # [...]

    if (entity extends enemy_class):
        entity.apply_damage()

Constructor
~~~~~~~~~~~

A class can have an optional constructor; a function named ``_init``
that is called when the class is instanced.

Arguments to Parent Constructor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When inheriting, parent constructors are called automatically (no need
to call ``._init()``). If a parent constructor takes arguments, they are
passed like this:

::

    func _init(args).(parentargs):
       pass

Sub Classes
~~~~~~~~~~~

A class file can have subclasses. This syntax should be straightforward:

::

    class SomeSubClass:
        var a = 5
        func print_value_of_a():
            print(a)

    func _init():
        var sc = SomeSubClass.new()  #instance by calling built-in new
        sc.print_value_of_a()

Classes as Objects
~~~~~~~~~~~~~~~~~~

It may be desired at some point to load a class from a file and then
instance it. Since the global scope does not exist, classes must be
loaded as a resource. Instancing is done by calling the ``new`` function
in a class object:

::

    # load the class (loaded every time the script is instanced)
    var MyClass = load("myclass.gd")

    # alternatively, using the preload() function preloads the class at compile time
    var MyClass2 = preload("myclass.gd")

    func _init():
        var a = MyClass.new()
        a.somefunction()

Exports
~~~~~~~

Class members can be exported. This means their value gets saved along
with a scene. If class members have initializers to constant
expressions, they will be available for editing in the property editor.
Exporting is done by using the export keyword:

::

    extends Button

    export var data  # value will be saved
    export var number = 5  # also available to the property editor

One of the fundamental benefits of exporting member variables is to have
them visible in the property editor. This way artists and game designers
can modify values that later influence how the program runs. For this, a
special export syntax is provided for more detail in the exported
variables:

::

    # if the exported value assigns a constant or constant expression, the type will be inferred and used in the editor

    export var number = 5

    # export can take a basic data type as an argument which will be used in the editor

    export(int) var number

    # export can also take a resource type to use as a hint

    export(Texture) var character_face

    # integers and strings hint enumerated values

    export(int, "Warrior", "Magician", "Thief") var character_class  # (editor will set them as 0, 1 and 2) 
    export(String, "Rebecca", "Mary", "Leah") var character_name 

    # strings as paths

    export(String, FILE) var f  # string is a path to a file
    export(String, DIR) var f  # string is a path to a directory
    export(String, FILE, "*.txt") var f  # string is a path to a file, custom filter provided as hint

    # using paths in the global filesystem is also possible, but only in tool scripts (see further below)

    export(String, FILE, GLOBAL, "*.png") var tool_image # string is a path to a PNG file in the global filesystem
    export(String, DIR, GLOBAL) var tool_dir # string is a path to a directory in the global filesystem

    # multiline strings

    export(String, MULTILINE) var text # display a large window to edit strings with multiple lines

    # integers and floats hint ranges

    export(int, 20) var i  # 0 to 20 allowed
    export(int, -10, 20) var j  # -10 to 20 allowed
    export(float, -10, 20, 0.2) var k  # -10 to 20 allowed, with stepping of 0.2
    export(float, EXP, 100, 1000, 20) var l  # exponential range, editing this property using the slider will set the value exponentially

    # floats with easing hint

    export(float, EASE) var transition_speed # display a visual representation of the ease() function when editing

    # color can hint availability of alpha

    export(Color, RGB) var col  # Color is RGB
    export(Color, RGBA) var col  # Color is RGBA

It must be noted that even if the script is not being run while at the
editor, the exported properties are still editable (see below for
"tool").

Exporting bit flags
^^^^^^^^^^^^^^^^^^^

Integers used as bit flags can store multiple true/false (boolean)
values in one property. By using the export hint ``int, FLAGS``, they
can be set from the editor:

::

    export(int, FLAGS) var spell_elements = ELEMENT_WIND | ELEMENT_WATER # individually edit the bits of an integer

Restricting the flags to a certain number of named flags is also
possible. The syntax is very similar to the enumeration syntax:

::

    export(int, FLAGS, "Fire", "Water", "Earth", "Wind") var spell_elements = 0 # set any of the given flags from the editor

In this example, ``Fire`` has value 1, ``Water`` has value 2, ``Earth``
has value 4 and ``Wind`` corresponds to value 8. Usually, constants
should be defined accordingly (e.g. ``const ELEMENT_WIND = 8`` and so
on).

Using bit flags requires some understanding of bitwise operations. If in
doubt, boolean variables should be exported instead.

Exporting Arrays
^^^^^^^^^^^^^^^^

Exporting arrays works too but there is a restriction. While regular
arrays are created local to every instance, exported arrays are shared
between all instances. This means that editing them in one instance will
cause them to change in all other instances. Exported arrays can have
initializers, but they must be constant expressions.

::

    # Exported array, shared between all instances.
    # Default value must be a constant expression.

    export var a=[1,2,3]

    # Typed arrays also work, only initialized empty:

    export var vector3s = Vector3Array()
    export var strings = StringArray()

    # Regular array, created local for every instance.
    # Default value can include run-time values, but can't
    # be exported.

    var b = [a,2,3]

Static Functions
~~~~~~~~~~~~~~~~

A function can be declared static. When a function is static it has no
access to the instance member variables or ``self``. This is mainly
useful to make libraries of helper functions:

::

    static func sum2(a, b):
        return a + b

Setters/Getters
~~~~~~~~~~~~~~~

| It is often useful to know when an member variable changed. It may
  also be desired to encapsulate its access. For this, GDScript provides
  a *setter\_/\_getter* helper using the ``setget`` keyword.
| Just add it at the end of the variable definition line like this:

::

    var myinteger = 5 setget myinteger_changed

If the value of ``myinteger`` is modified *externally* (not from local
usage in the class), the *setter* function will be called beforehand.
The *setter* must, then, decide what to do with the new value. The
*setter function* looks like this:

::

    func myinteger_changed(newvalue):
        myinteger=newvalue

A *setter* and a *getter* can be used together too, just define both of
them:

::

    var myvar setget myvar_set,myvar_get

    func myvar_set(newvalue):
        myvar=newvalue

    func myvar_get():
        return myvar # getter must return a value

Using simply a *getter* is possible too, just skip the setter:

::

    var myvar setget ,myvar_get

This is especially useful when exporting variables to editor in tool
scripts or plugins, for validating input.

Note: As mentioned before, local access will not trigger the setter and
getter. For example:

::

    func _init():
    #does not trigger setter/getter
        myinteger=5
        print(myinteger)
    #triggers setter/getter
        self.myinteger=5
        print(self.myinteger)

Tool Mode
~~~~~~~~~

Scripts, by default, don't run inside the editor and only the exported
properties can be changed. In some cases it is desired that they do run
inside the editor (as long as they don't execute game code or manually
avoid doing so). For this, the ``tool`` keyword exists and must be
placed at the top of the file:

::

    tool
    extends Button

    func _ready():
        print("Hello")

Memory Management
~~~~~~~~~~~~~~~~~

If a class inherits from :ref:`class_Reference`, then instances will be
freed when no longer in use. No garbage collector exists, just simple
reference counting. By default, all classes that don't define
inheritance extend **Reference**. If this is not desired, then a class
must inherit :ref:`class_Object` manually and must call instance.free(). To
avoid reference cycles that can't be freed, a ``weakref`` function is
provided for creating weak references.

Function References
~~~~~~~~~~~~~~~~~~~

Functions can't be referenced because they are not treated as class
members. There are two alternatives to this, though. The ``call``
function or the ``funcref`` helper.

::

    instance.call("funcname", args)  # call a function by name

    var fr = funcref(instance, "funcname")  # create a function ref
    fr.call_func(args)

Signals
~~~~~~~

It is often desired to send a notification that something happened in an
instance. GDScript supports creation of built-in Godot signals.
Declaring a signal in GDScript is easy, in the body of the class, just
write:

::

    # no arguments
    signal your_signal_name
    # with arguments
    signal your_signal_name_with_args(a,b)

These signals, just like regular signals, can be connected in the editor
or from code. Just take the instance of a class where the signal was
declared and connect it to the method of another instance:

::

    func _callback_no_args():
        print("Got callback!")

    func _callback_args(a,b):
        print("Got callback with args! a: ",a," and b: ",b)

    func _at_some_func():
        instance.connect("your_signal_name",self,"callback_no_args")
        instance.connect("your_signal_name_with_args",self,"callback_args")

It is also possible to bind arguments to a signal that lacks them with
your custom values:

::

    func _at_some_func():
        instance.connect("your_signal_name_with_args",self,"callback_no_args",[22,"hello"])

This is very useful when a signal from many objects is connected to a
single callback and the sender must be identified:

::

    func _button_pressed(which):
        print("Button was pressed: ",which.get_name())

    func _ready():
        for b in get_node("buttons").get_children():
            b.connect("pressed",self,"_button_pressed",[b])

Finally, emitting a custom signal is done by using the
Object.emit\_signal method:

::

    func _at_some_func():
        emit_signal("your_signal_name")
        emit_signal("your_signal_name_with_args",55,128)
        someinstance.emit_signal("somesignal")

Coroutines
~~~~~~~~~~

GDScript has some support for coroutines via the ``yield`` built-in
function. The way it works is very simple: Calling ``yield()`` will
immediately return from the current function, with the current frozen
state of the same function as the return value. Calling ``resume`` on
this resulting object will continue execution and return whatever the
function returns. Once resumed the state object becomes invalid. Here is
an example:

::

    func myfunc():

       print("hello")
       yield()
       print("world")

    func _ready():

        var y = myfunc()
        #function state saved in 'y'
        print("my dear")
        y.resume()
        # 'y' resumed and is now an invalid state

Will print:

::

    hello
    my dear
    world

It is also possible to pass values between yield() and resume(), for
example:

::

    func myfunc():

       print("hello")
       print( yield() )
       return "cheers!"

    func _ready():

        var y = myfunc()
        #function state saved in 'y'
        print( y.resume("world") )
        # 'y' resumed and is now an invalid state

Will print:

::

    hello
    world
    cheers!

Coroutines & Signals
~~~~~~~~~~~~~~~~~~~~

The real strength of using ``yield`` is when combined with signals.
``yield`` can accept two parameters, an object and a signal. When the
signal is activated, execution will return. Here are some examples:

::

    #resume execution the next frame
    yield( get_tree(), "idle_frame" )

    #resume execution when animation is done playing:
    yield( get_node("AnimationPlayer"), "finished" )
