.. _doc_gdscript_custom_classes:

Custom Classes
==============

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
class), user the ``super`` keyword::

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

Properties
~~~~~~~~~~

Sometimes you want a class' member variable to do more than just hold data and actually perform
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

    Unlike ``setget`` in previous Godot versions, the properties setter and getter are **always** called,
    even when accessed inside the same class (with or without prefixing with ``self.``). This makes the behavior
    consistent. If you need direct access to the value, use another variable for direct access and make the property
    code use that name.

In case you want to split the code from the variable declaration or you need to share the code across multiple properties,
you can use a different notation to use existing class functions::

    var my_prop:
        get = get_my_prop, set = set_my_prop

This can also be done in the same line.
