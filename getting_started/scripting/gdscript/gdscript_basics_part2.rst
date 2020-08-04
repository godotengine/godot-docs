.. _doc_gdscript_basics2:

GDScript basics - part 2
========================

.. _doc_gdscript_classes:

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

Instead, you can give your class a name to register it as a new type in Godot's
editor. For that, you use the ``class_name`` keyword. You can add an
optional comma followed by a path to an image, to use it as an icon. Your class
will then appear with its new icon in the editor::

   # Item.gd

   extends Node
   class_name Item, "res://interface/icons/item.png"

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


To check if a given instance inherits from a given class,
the ``is`` keyword can be used::

    # Cache the enemy class.
    const Enemy = preload("enemy.gd")

    # [...]

    # Use 'is' to check inheritance.
    if entity is Enemy:
        entity.apply_damage()

To call a function in a *parent class* (i.e. one ``extend``-ed in your current
class), prepend ``.`` to the function name::

    .base_func(args)

This is especially useful because functions in extending classes replace
functions with the same name in their parent classes. If you still want to
call them, you can prefix them with ``.`` (like the ``super`` keyword
in other languages)::

    func some_func(x):
        .some_func(x) # Calls the same function on the parent class.

.. note:: Default functions like  ``_init``, and most notifications such as
          ``_enter_tree``, ``_exit_tree``, ``_process``, ``_physics_process``,
          etc. are called in all parent classes automatically.
          There is no need to call them explicitly when overloading them.


Class Constructor
^^^^^^^^^^^^^^^^^

The class constructor, called on class instantiation, is named ``_init``. As
mentioned earlier, the constructors of parent classes are called automatically
when inheriting a class. So, there is usually no need to call ``._init()``
explicitly.

Unlike the call of a regular function, like in the above example with
``.some_func``, if the constructor from the inherited class takes arguments,
they are passed like this::

    func _init(args).(parent_args):
       pass

This is better explained through examples. Consider this scenario::

    # State.gd (inherited class)
    var entity = null
    var message = null


    func _init(e=null):
        entity = e


    func enter(m):
        message = m


    # Idle.gd (inheriting class)
    extends "State.gd"


    func _init(e=null, m=null).(e):
        # Do something with 'e'.
        message = m

There are a few things to keep in mind here:

1. If the inherited class (``State.gd``) defines a ``_init`` constructor that takes
   arguments (``e`` in this case), then the inheriting class (``Idle.gd``) *must*
   define ``_init`` as well and pass appropriate parameters to ``_init`` from ``State.gd``.
2. ``Idle.gd`` can have a different number of arguments than the parent class ``State.gd``.
3. In the example above, ``e`` passed to the ``State.gd`` constructor is the same ``e`` passed
   in to ``Idle.gd``.
4. If ``Idle.gd``'s ``_init`` constructor takes 0 arguments, it still needs to pass some value
   to the ``State.gd`` parent class, even if it does nothing. This brings us to the fact that you
   can pass literals in the base constructor as well, not just variables. eg.::

    # Idle.gd

    func _init().(5):
        pass

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
    var my_class = load("myclass.gd")

    # Preload the class only once at compile time.
    const MyClass = preload("myclass.gd")


    func _init():
        var a = MyClass.new()
        a.some_function()

.. _doc_gdscript_setters_getters:

Setters/getters
~~~~~~~~~~~~~~~

It is often useful to know when a class' member variable changes for
whatever reason. It may also be desired to encapsulate its access in some way.

For this, GDScript provides a *setter/getter* syntax using the ``setget`` keyword.
It is used directly after a variable definition:

::

    var variable = value setget setterfunc, getterfunc

Whenever the value of ``variable`` is modified by an *external* source
(i.e. not from local usage in the class), the *setter* function (``setterfunc`` above)
will be called. This happens *before* the value is changed. The *setter* must decide what to do
with the new value. Vice versa, when ``variable`` is accessed, the *getter* function
(``getterfunc`` above) must ``return`` the desired value. Below is an example::

    var my_var setget my_var_set, my_var_get


    func my_var_set(new_value):
        my_var = new_value


    func my_var_get():
        return my_var # Getter must return a value.

Either of the *setter* or *getter* functions can be omitted::

    # Only a setter.
    var my_var = 5 setget my_var_set
    # Only a getter (note the comma).
    var my_var = 5 setget ,my_var_get

Setters and getters are useful when :ref:`exporting variables <doc_gdscript_exports>`
to the editor in tool scripts or plugins, for validating input.

As said, *local* access will *not* trigger the setter and getter. Here is an
illustration of this:

::

    func _init():
        # Does not trigger setter/getter.
        my_integer = 5
        print(my_integer)

        # Does trigger setter/getter.
        self.my_integer = 5
        print(self.my_integer)

.. _doc_gdscript_tool_mode:

Tool mode
~~~~~~~~~

By default, scripts don't run inside the editor and only the exported
properties can be changed. In some cases, it is desired that they do run
inside the editor (as long as they don't execute game code or manually
avoid doing so). For this, the ``tool`` keyword exists and must be
placed at the top of the file::

    tool
    extends Button


    func _ready():
        print("Hello")


See :ref:`doc_running_code_in_the_editor` for more information.

.. warning:: Be cautious when freeing nodes with ``queue_free()`` or ``free()``
             in a tool script (especially the script's owner itself). As tool
             scripts run their code in the editor, misusing them may lead to
             crashing the editor.

Memory management
~~~~~~~~~~~~~~~~~

If a class inherits from :ref:`class_Reference`, then instances will be
freed when no longer in use. No garbage collector exists, just
reference counting. By default, all classes that don't define
inheritance extend **Reference**. If this is not desired, then a class
must inherit :ref:`class_Object` manually and must call instance.free(). To
avoid reference cycles that can't be freed, a ``weakref`` function is
provided for creating weak references.

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
signals of nodes like :ref:`class_Button` or :ref:`class_RigidBody`.

In the example below, we connect the ``health_depleted`` signal from a
``Character`` node to a ``Game`` node. When the ``Character`` node emits the
signal, the game node's ``_on_Character_health_depleted`` is called::

    # Game.gd

    func _ready():
        var character_node = get_node('Character')
        character_node.connect("health_depleted", self, "_on_Character_health_depleted")


    func _on_Character_health_depleted():
        get_tree().reload_current_scene()

You can emit as many arguments as you want along with a signal.

Here is an example where this is useful. Let's say we want a life bar on screen
to react to health changes with an animation, but we want to keep the user
interface separate from the player in our scene tree.

In our ``Character.gd`` script, we define a ``health_changed`` signal and emit
it with :ref:`Object.emit_signal() <class_Object_method_emit_signal>`, and from
a ``Game`` node higher up our scene tree, we connect it to the ``Lifebar`` using
the :ref:`Object.connect() <class_Object_method_connect>` method::

    # Character.gd

    ...
    signal health_changed


    func take_damage(amount):
        var old_health = health
        health -= amount

        # We emit the health_changed signal every time the
        # character takes damage.
        emit_signal("health_changed", old_health, health)
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

.. note::

    To use signals, your class has to extend the ``Object`` class or any
    type extending it like ``Node``, ``KinematicBody``, ``Control``...

In the ``Game`` node, we get both the ``Character`` and ``Lifebar`` nodes, then
connect the character, that emits the signal, to the receiver, the ``Lifebar``
node in this case.

::

    # Game.gd

    func _ready():
        var character_node = get_node('Character')
        var lifebar_node = get_node('UserInterface/Lifebar')

        character_node.connect("health_changed", lifebar_node, "_on_Character_health_changed")

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

        character_node.connect("health_changed", battle_log_node, "_on_Character_health_changed", [character_node.name])

Our ``BattleLog`` node receives each element in the binds array as an extra argument::

    # BattleLog.gd

    func _on_Character_health_changed(old_value, new_value, character_name):
        if not new_value <= old_value:
            return

        var damage = old_value - new_value
        label.text += character_name + " took " + str(damage) + " damage."

.. _doc_gdscript_yield:

Coroutines with yield
~~~~~~~~~~~~~~~~~~~~~

GDScript offers support for `coroutines <https://en.wikipedia.org/wiki/Coroutine>`_
via the :ref:`yield<class_@GDScript_method_yield>` built-in function. Calling ``yield()`` will
immediately return from the current function, with the current frozen
state of the same function as the return value. Calling ``resume()`` on
this resulting object will continue execution and return whatever the
function returns. Once resumed, the state object becomes invalid. Here is
an example::

    func my_func():
        print("Hello")
        yield()
        print("world")


    func _ready():
        var y = my_func()
        # Function state saved in 'y'.
        print("my dear")
        y.resume()
        # 'y' resumed and is now an invalid state.

Will print::

    Hello
    my dear
    world

It is also possible to pass values between ``yield()`` and ``resume()``,
for example::

    func my_func():
        print("Hello")
        print(yield())
        return "cheers!"


    func _ready():
        var y = my_func()
        # Function state saved in 'y'.
        print(y.resume("world"))
        # 'y' resumed and is now an invalid state.

Will print::

    Hello
    world
    cheers!

Remember to save the new function state, when using multiple ``yield``\s::

    func co_func():
        for i in range(1, 5):
            print("Turn %d" % i)
            yield();


    func _ready():
        var co = co_func();
        while co is GDScriptFunctionState && co.is_valid():
            co = co.resume();

.. _doc_gdscript_coroutines_and_signals:

Coroutines & signals
^^^^^^^^^^^^^^^^^^^^

The real strength of using ``yield`` is when combined with signals.
``yield`` can accept two arguments, an object and a signal. When the
signal is received, execution will recommence. Here are some examples::

    # Resume execution the next frame.
    yield(get_tree(), "idle_frame")

    # Resume execution when animation is done playing.
    yield(get_node("AnimationPlayer"), "animation_finished")

    # Wait 5 seconds, then resume execution.
    yield(get_tree().create_timer(5.0), "timeout")

Coroutines themselves use the ``completed`` signal when they transition
into an invalid state, for example::

    func my_func():
        yield(button_func(), "completed")
        print("All buttons were pressed, hurray!")


    func button_func():
        yield($Button0, "pressed")
        yield($Button1, "pressed")

``my_func`` will only continue execution once both buttons have been pressed.

You can also get the signal's argument once it's emitted by an object:

::

    # Wait for when any node is added to the scene tree.
    var node = yield(get_tree(), "node_added")

If you're unsure whether a function may yield or not, or whether it may yield
multiple times, you can yield to the ``completed`` signal conditionally:

::

    func generate():
        var result = rand_range(-1.0, 1.0)

        if result < 0.0:
            yield(get_tree(), "idle_frame")

        return result


    func make():
        var result = generate()

        if result is GDScriptFunctionState: # Still working.
            result = yield(result, "completed")

        return result

This ensures that the function returns whatever it was supposed to return
regardless of whether coroutines were used internally. Note that using
``while`` would be redundant here as the ``completed`` signal is only emitted
when the function didn't yield anymore.

.. _doc_gdscript_onready:

Onready keyword
~~~~~~~~~~~~~~~

When using nodes, it's common to desire to keep references to parts
of the scene in a variable. As scenes are only warranted to be
configured when entering the active scene tree, the sub-nodes can only
be obtained when a call to ``Node._ready()`` is made.

::

    var my_label


    func _ready():
        my_label = get_node("MyLabel")

This can get a little cumbersome, especially when nodes and external
references pile up. For this, GDScript has the ``onready`` keyword, that
defers initialization of a member variable until ``_ready()`` is called. It
can replace the above code with a single line::

    onready var my_label = get_node("MyLabel")

.. _doc_gdscript_assert:

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
