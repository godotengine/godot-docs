.. _doc_gdscript_more_efficiently:

GDScript: An introduction to dynamic languages
==============================================

About
-----

This tutorial aims to be a quick reference for how to use GDScript more
efficiently. It focuses on common cases specific to the language, but
also covers a lot of information on dynamically typed languages.

It's meant to be especially useful for programmers with little or no previous
experience with dynamically typed languages.

Dynamic nature
--------------

Pros & cons of dynamic typing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

GDScript is a Dynamically Typed language. As such, its main advantages
are that:

-  The language is easy to get started with.
-  Most code can be written and changed quickly and without hassle.
-  Less code written means less errors & mistakes to fix.
-  The code is easy to read (little clutter).
-  No compilation is required to test.
-  Runtime is tiny.
-  It has duck-typing and polymorphism by nature.

While the main disadvantages are:

-  Less performance than statically typed languages.
-  More difficult to refactor (symbols can't be traced).
-  Some errors that would typically be detected at compile time in
   statically typed languages only appear while running the code
   (because expression parsing is more strict).
-  Less flexibility for code-completion (some variable types are only
   known at run-time).

This, translated to reality, means that Godot used with GDScript is a combination
designed to create games quickly and efficiently. For games that are very
computationally intensive and can't benefit from the engine built-in
tools (such as the Vector types, Physics Engine, Math library, etc), the
possibility of using C++ is present too. This allows you to still create most of the
game in GDScript and add small bits of C++ in the areas that need
a performance boost.

Variables & assignment
~~~~~~~~~~~~~~~~~~~~~~

All variables in a dynamically typed language are "variant"-like. This
means that their type is not fixed, and is only modified through
assignment. Example:

Static:

.. code-block:: cpp

    int a; // Value uninitialized.
    a = 5; // This is valid.
    a = "Hi!"; // This is invalid.

Dynamic:

::

    var a # 'null' by default.
    a = 5 # Valid, 'a' becomes an integer.
    a = "Hi!" # Valid, 'a' changed to a string.

As function arguments:
~~~~~~~~~~~~~~~~~~~~~~

Functions are of dynamic nature too, which means they can be called with
different arguments, for example:

Static:

.. code-block:: cpp

    void print_value(int value) {

        printf("value is %i\n", value);
    }

    [..]

    print_value(55); // Valid.
    print_value("Hello"); // Invalid.

Dynamic:

::

    func print_value(value):
        print(value)

    [..]

    print_value(55) # Valid.
    print_value("Hello") # Valid.

Pointers & referencing:
~~~~~~~~~~~~~~~~~~~~~~~

In static languages, such as C or C++ (and to some extent Java and C#),
there is a distinction between a variable and a pointer/reference to a
variable. The latter allows the object to be modified by other functions
by passing a reference to the original one.

In C# or Java, everything not a built-in type (int, float, sometimes
String) is always a pointer or a reference. References are also
garbage-collected automatically, which means they are erased when no
longer used. Dynamically typed languages tend to use this memory model,
too. Some Examples:

-  C++:

.. code-block:: cpp

    void use_class(SomeClass *instance) {

        instance->use();
    }

    void do_something() {

        SomeClass *instance = new SomeClass; // Created as pointer.
        use_class(instance); // Passed as pointer.
        delete instance; // Otherwise it will leak memory.
    }

-  Java:

.. code-block:: java

    @Override
    public final void use_class(SomeClass instance) {

        instance.use();
    }

    public final void do_something() {

        SomeClass instance = new SomeClass(); // Created as reference.
        use_class(instance); // Passed as reference.
        // Garbage collector will get rid of it when not in
        // use and freeze your game randomly for a second.
    }

-  GDScript:

::

    func use_class(instance): # Does not care about class type
        instance.use() # Will work with any class that has a ".use()" method.

    func do_something():
        var instance = SomeClass.new() # Created as reference.
        use_class(instance) # Passed as reference.
        # Will be unreferenced and deleted.

In GDScript, only base types (int, float, string and the vector types)
are passed by value to functions (value is copied). Everything else
(instances, arrays, dictionaries, etc) is passed as reference. Classes
that inherit :ref:`class_RefCounted` (the default if nothing is specified)
will be freed when not used, but manual memory management is allowed too
if inheriting manually from :ref:`class_Object`.

Arrays
------

Arrays in dynamically typed languages can contain many different mixed
datatypes inside and are always dynamic (can be resized at any time).
Compare for example arrays in statically typed languages:

.. code-block:: cpp

    int *array = new int[4]; // Create array.
    array[0] = 10; // Initialize manually.
    array[1] = 20; // Can't mix types.
    array[2] = 40;
    array[3] = 60;
    // Can't resize.
    use_array(array); // Passed as pointer.
    delete[] array; // Must be freed.

    // or

    std::vector<int> array;
    array.resize(4);
    array[0] = 10; // Initialize manually.
    array[1] = 20; // Can't mix types.
    array[2] = 40;
    array[3] = 60;
    array.resize(3); // Can be resized.
    use_array(array); // Passed reference or value.
    // Freed when stack ends.

And in GDScript:

::

    var array = [10, "hello", 40, 60] # You can mix types.
    array.resize(3) # Can be resized.
    use_array(array) # Passed as reference.
    # Freed when no longer in use.

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

Dictionaries are a powerful tool in dynamically typed languages.
Most programmers that come from statically typed languages (such as C++
or C#) ignore their existence and make their life unnecessarily more
difficult. This datatype is generally not present in such languages (or
only in limited form).

Dictionaries can map any value to any other value with complete
disregard for the datatype used as either key or value. Contrary to
popular belief, they are efficient because they can be implemented
with hash tables. They are, in fact, so efficient that some languages
will go as far as implementing arrays as dictionaries.

Example of Dictionary:

::

    var d = {"name": "John", "age": 22}
    print("Name: ", d["name"], " Age: ", d["age"])

Dictionaries are also dynamic, keys can be added or removed at any point
at little cost:

::

    d["mother"] = "Rebecca" # Addition.
    d["age"] = 11 # Modification.
    d.erase("name") # Removal.

In most cases, two-dimensional arrays can often be implemented more
easily with dictionaries. Here's a battleship game example:

::

    # Battleship Game

    const SHIP = 0
    const SHIP_HIT = 1
    const WATER_HIT = 2

    var board = {}

    func initialize():
        board[Vector2(1, 1)] = SHIP
        board[Vector2(1, 2)] = SHIP
        board[Vector2(1, 3)] = SHIP

    func missile(pos):
        if pos in board: # Something at that position.
            if board[pos] == SHIP: # There was a ship! hit it.
                board[pos] = SHIP_HIT
            else:
                print("Already hit here!") # Hey dude you already hit here.
        else: # Nothing, mark as water.
            board[pos] = WATER_HIT

    func game():
        initialize()
        missile(Vector2(1, 1))
        missile(Vector2(5, 8))
        missile(Vector2(2, 3))

Dictionaries can also be used as data markup or quick structures. While
GDScript's dictionaries resemble python dictionaries, it also supports Lua
style syntax and indexing, which makes it useful for writing initial
states and quick structs:

::

    # Same example, lua-style support.
    # This syntax is a lot more readable and usable.
    # Like any GDScript identifier, keys written in this form cannot start
    # with a digit.

    var d = {
        name = "John",
        age = 22
    }

    print("Name: ", d.name, " Age: ", d.age) # Used "." based indexing.

    # Indexing

    d["mother"] = "Rebecca"
    d.mother = "Caroline" # This would work too to create a new key.

For & while
-----------

Iterating using the C-style for loop in C-derived languages can be quite complex:

.. code-block:: cpp

    const char** strings = new const char*[50];

    [..]

    for (int i = 0; i < 50; i++) {
		printf("Value: %c Index: %d\n", strings[i], i);
	}

    // Even in STL:
    std::list<std::string> strings;
    
    [..]

	for (std::string::const_iterator it = strings.begin(); it != strings.end(); it++) {
		std::cout << *it << std::endl;
	}

Because of this, GDScript makes the opinionated decision to have a for-in loop over iterables instead:

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

    range(n) # Will count from 0 to n in steps of 1. The parameter n is exclusive.
    range(b, n) # Will count from b to n in steps of 1. The parameters b is inclusive. The parameter n is exclusive.
    range(b, n, s) # Will count from b to n, in steps of s. The parameters b is inclusive. The parameter n is exclusive.

Some examples involving C-style for loops:

.. code-block:: cpp

    for (int i = 0; i < 10; i++) {}

    for (int i = 5; i < 10; i++) {}

    for (int i = 5; i < 10; i += 2) {}

Translate to:

::

    for i in range(10):
        pass

    for i in range(5, 10):
        pass

    for i in range(5, 10, 2):
        pass

And backwards looping done through a negative counter:

::

    for (int i = 10; i > 0; i--) {}

Becomes:

::

    for i in range(10, 0, -1):
        pass

While
-----

while() loops are the same everywhere:

::

    var i = 0

    while i < strings.size():
        print(strings[i])
        i += 1

Custom iterators
----------------
You can create custom iterators in case the default ones don't quite meet your
needs by overriding the Variant class's ``_iter_init``, ``_iter_next``, and ``_iter_get``
functions in your script. An example implementation of a forward iterator follows:

::

    class ForwardIterator:
        var start
        var current
        var end
        var increment

        func _init(start, stop, increment):
            self.start = start
            self.current = start
            self.end = stop
            self.increment = increment

        func should_continue():
            return (current < end)

        func _iter_init(arg):
            current = start
            return should_continue()

        func _iter_next(arg):
            current += increment
            return should_continue()

        func _iter_get(arg):
            return current

And it can be used like any other iterator:

::

    var itr = ForwardIterator.new(0, 6, 2)
    for i in itr:
        print(i) # Will print 0, 2, and 4.

Make sure to reset the state of the iterator in ``_iter_init``, otherwise nested
for-loops that use custom iterators will not work as expected.

Duck typing
-----------

One of the most difficult concepts to grasp when moving from a
statically typed language to a dynamic one is duck typing. Duck typing
makes overall code design much simpler and straightforward to write, but
it's not obvious how it works.

As an example, imagine a situation where a big rock is falling down a
tunnel, smashing everything on its way. The code for the rock, in a
statically typed language would be something like:

.. code-block:: cpp

    void BigRollingRock::on_object_hit(Smashable *entity) {

        entity->smash();
    }

This way, everything that can be smashed by a rock would have to
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

Yes, we should call it Hulk typing instead.

It's possible that the object being hit doesn't have a smash() function.
Some dynamically typed languages simply ignore a method call when it
doesn't exist, but GDScript is stricter, so checking if the function
exists is desirable:

::

    func _on_object_hit(object):
        if object.has_method("smash"):
            object.smash()

Then, simply define that method and anything the rock touches can be
smashed.
