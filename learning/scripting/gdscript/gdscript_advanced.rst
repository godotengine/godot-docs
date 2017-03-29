.. _doc_gdscript_more_efficiently:

GDScript more efficiently
=========================

About
-----

This tutorial aims to be a quick reference for how to use GDScript more
efficiently. It focuses in common cases specific to the language, but
also covers a lot related to using dynamically typed languages.

It's meant to be specially useful for programmers without previous or
little experience of dynamically typed languages.

Dynamic nature
--------------

Pros & cons of dynamic typing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

GDScript is a Dynamically Typed language. As such, it's main advantages
are that:

-  Language is very simple to learn.
-  Most code can be written and changed quickly and without hassle.
-  Less code written means less errors & mistakes to fix.
-  Easier to read the code (less clutter).
-  No compilation is required to test.
-  Runtime is tiny.
-  Duck-typing and polymorphism by nature.

While the main cons are:

-  Less performance than statically typed languages.
-  More difficult to refactor (symbols can't be traced)
-  Some errors that would typically be detected at compile time in
   statically typed languages only appear while running the code
   (because expression parsing is more strict).
-  Less flexibility for code-completion (some variable types are only
   known at run-time).

This, translated to reality, means that Godot+GDScript are a combination
designed to games very quickly and efficiently. For games that are very
computationally intensive and can't benefit from the engine built-in
tools (such as the Vector types, Physics Engine, Math library, etc), the
possibility of using C++ is present too. This allows to still create the
entire game in GDScript and add small bits of C++ in the areas that need
a boost.

Variables & assignment
~~~~~~~~~~~~~~~~~~~~~~

All variables in a dynamically typed language are "variant"-like. This
means that their type is not fixed, and is only modified through
assignment. Example:

Static:

::

    int a; // value uninitialized
    a = 5; // this is valid
    a = "Hi!"; // this is invalid

Dynamic:

::

    var a # null by default
    a = 5 # valid, 'a' becomes an integer
    a = "Hi!" # valid, 'a' changed to a string

As function arguments:
~~~~~~~~~~~~~~~~~~~~~~

Functions are of dynamic nature too, which means they can be called with
different arguments, for example:

Static:

::

    void print_value(int value) 
    {
        printf("value is %i\n",value);
    }

    [..]

    print_value(55); // valid
    print_value("Hello"); // invalid

Dynamic:

::

    func print_value(value):
        print(value)
    [..]

    print_value(55) # valid
    print_value("Hello") # valid

Pointers & referencing:
~~~~~~~~~~~~~~~~~~~~~~~

In static languages such as C or C++ (and to some extent Java and C#),
there is a distinction between a variable and a pointer/reference to a
variable. The later allows the object to be modified by other functions
by passing a reference to the original one.

In C# or Java, everything not a built-in type (int, float, sometimes
String) is always a pointer or a reference. References are also
garbage-collected automatically, which means they are erased when no
longer used. Dynamically typed languages tend to use this memory model
too. Some Examples:

-  C++:

.. code:: cpp

    void use_class(SomeClass *instance) {

        instance->use();
    }

    void do_something() {

        SomeClass *instance = new SomeClass; // created as pointer
        use_class(instance); // passed as pointer
        delete instance; // otherwise it will leak memory
    }

-  Java:

.. code:: java

    @Override
    public final void use_class(SomeClass instance) {

        instance.use();
    }

    public final void do_something() {

        SomeClass instance = new SomeClass(); // created as reference
        use_class(instance); // passed as reference
        // garbage collector will get rid of it when not in 
        // use and freeze your game randomly for a second
    }

-  GDScript:

::

    func use_class(instance); # does not care about class type
        instance.use() # will work with any class that has a ".use()" method.

    func do_something():
        var instance = SomeClass.new() # created as reference
        use_class(instance) # passed as reference
        # will be unreferenced and deleted

In GDScript, only base types (int, float, string and the vector types)
are passed by value to functions (value is copied). Everything else
(instances, arrays, dictionaries, etc) is passed as reference. Classes
that inherit :ref:`class_Reference` (the default if nothing is specified)
will be freed when not used, but manual memory management is allowed too
if inheriting manually from :ref:`class_Object`.

Arrays
------

Arrays in dynamically typed languages can contain many different mixed
datatypes inside and are always dynamic (can be resized at any time).
Compare for example arrays in statically typed languages:

::

    int *array = new int[4]; // create array
    array[0] = 10; // initialize manually
    array[1] = 20; // can't mix types
    array[2] = 40;
    array[3] = 60;
    // can't resize
    use_array(array); // passed as pointer
    delete[] array; // must be freed

    //or

    std::vector<int> array;
    array.resize(4);
    array[0] = 10; // initialize manually
    array[1] = 20; // can't mix types
    array[2] = 40;
    array[3] = 60;
    array.resize(3); // can be resized
    use_array(array); // passed reference or value
    // freed when stack ends

And in GDScript:

::

    var array = [10, "hello", 40, 60] # simple, and can mix types
    array.resize(3) # can be resized
    use_array(array) # passed as reference
    # freed when no longer in use

In dynamically typed languages, arrays can also double as other
datatypes, such as lists:

::

    var array = []
    array.append(4)
    array.append(5)
    array.pop_front()

Or unordered sets:

::

    var a = 20
    if a in [10, 20, 30]:
        print("We have a winner!")

Dictionaries
------------

Dictionaries are always a very powerful in dynamically typed languages.
Most programmers that come from statically typed languages (such as C++
or C#) ignore their existence and make their life unnecessarily more
difficult. This datatype is generally not present in such languages (or
only on limited form).

Dictionaries can map any value to any other value with complete
disregard for the datatype used as either key or value. Contrary to
popular belief, they are very efficient because they can be implemented
with hash tables. They are, in fact, so efficient that some languages
will go as far as implementing arrays as dictionaries.

Example of Dictionary:

::

    var d = { "name": "john", "age": 22 } # simple syntax
    print("Name: ", d["name"], " Age: ", d["age"])

Dictionaries are also dynamic, keys can be added or removed at any point
at little cost:

::

    d["mother"] = "Rebecca" # addition
    d["age"] = 11 # modification
    d.erase("name") # removal

In most cases, two-dimensional arrays can often be implemented more
easily with dictionaries. Here's a simple battleship game example:

::

    # battleship game

    const SHIP = 0
    const SHIP_HIT = 1
    const WATER_HIT = 2

    var board = {}

    func initialize():
        board[Vector(1,1)] = SHIP
        board[Vector(1,2)] = SHIP
        board[Vector(1,3)] = SHIP

    func missile(pos):

        if pos in board: # something at that pos
            if board[pos] == SHIP: # there was a ship! hit it
                board[pos] = SHIP_HIT
            else: 
                print("already hit here!") # hey dude you already hit here
        else: # nothing, mark as water
            board[pos] = WATER_HIT

    func game():
        initialize()
        missile(Vector2(1,1))
        missile(Vector2(5,8))
        missile(Vector2(2,3))

Dictionaries can also be used as data markup or quick structures. While
GDScript dictionaries resemble python dictionaries, it also supports Lua
style syntax an indexing, which makes it very useful for writing initial
states and quick structs:

::

    # same example, lua-style support
    # this syntax is a lot more readable and usable

    var d = {
        name = "john",
        age = 22
    }

    print("Name: ", d.name, " Age: ", d.age) # used "." based indexing

    # indexing

    d.mother = "rebecca" # this doesn't work (use syntax below to add a key:value pair)
    d["mother"] = "rebecca" # this works
    d.name = "caroline" # if key exists, assignment does work, this is why it's like a quick struct.

For & while
-----------

Iterating in some statically typed languages can be quite complex:

::

    const char* strings = new const char*[50];

    [..]

    for(int i=0; i<50; i++)
    {

        printf("value: %s\n", i, strings[i]);
    }

    // even in STL:

    for(std::list<std::string>::const_iterator it = strings.begin(); it != strings.end(); it++) {

        std::cout << *it << std::endl;
    }

This is usually greatly simplified in dynamically typed languages:

::

    for s in strings:
        print(s)

Container datatypes (arrays and dictionaries) are iterable. Dictionaries
allow iterating the keys:

::

    for key in dict:
        print(key, " -> ", dict[key])

Iterating with indices is also possible:

::

    for i in range(strings.size()):
        print(strings[i])

The range() function can take 3 arguments:

::

        range(n) (will go from 0 to n-1)
        range(b, n) (will go from b to n-1)
        range(b, n, s) (will go from b to n-1, in steps of s)

Some examples:

::

    for(int i=0; i<10; i++) {}

    for(int i=5; i<10; i++) {}

    for(int i=5; i<10; i+=2) {}

Translate to:

::

    for i in range(10):

    for i in range(5, 10):

    for i in range(5, 10, 2):

And backwards looping is done through a negative counter:

::

    for(int i=10; i>0; i--) {}

becomes

::

    for i in range(10, 0, -1):

While
-----

while() loops are the same everywhere:

::

    var i = 0

    while(i < strings.size()):
        print(strings[i])
        i += 1

Duck typing
-----------

One of the most difficult concepts to grasp when moving from a
statically typed language to a dynamic one is duck typing. Duck typing
makes overall code design much simpler and straightforward to write, but
it's not obvious how it works.

As an example, imagine a situation where a big rock is falling down a
tunnel, smashing everything on its way. The code for the rock, in a
statically typed language would be something like:

::

    void BigRollingRock::on_object_hit(Smashable *entity) 
    {
        entity->smash();
    }

This, way, everything that can be smashed by a rock would have to
inherit Smashable. If a character, enemy, piece of furniture, small rock
were all smashable, they would need to inherit from the class Smashable,
possibly requiring multiple inheritance. If multiple inheritance was
undesired, then they would have to inherit a common class like Entity.
Yet, it would not be very elegant to add a virtual method ``smash()`` to
Entity only if a few of them can be smashed.

With dynamically typed languages, this is not a problem. Duck typing
makes sure you only have to define a ``smash()`` function where required
and that's it. No need to consider inheritance, base classes, etc.

::

    func _on_object_hit(object):
        object.smash()

And that's it. If the object that hit the big rock has a smash() method,
it will be called. No need for inheritance or polymorphism. Dynamically
typed languages only care about the instance having the desired method
or member, not what it inherits or the class type. The definition of
Duck Typing should make this clearer:

*"When I see a bird that walks like a duck and swims like a duck and
quacks like a duck, I call that bird a duck"*

In this case, it translates to:

*"If the object can be smashed, don't care what it is, just smash it."*

Yes, we should call it Hulk typing instead. Anyway though, there exists
the possibility of the object being hit not having a smash() function.
Some dynamically typed languages simply ignore a method call when it
doesn't exist (like Objective C), but GDScript is more strict, so
checking if the function exists is desirable:

::

    func _on_object_hit(object):
        if (object.has_method("smash")):
            object.smash()

Then, simply define that method and anything the rock touches can be
smashed.
