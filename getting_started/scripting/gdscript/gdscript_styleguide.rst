.. _doc_gdscript_styleguide:

GDScript style guide
====================

This style guide lists conventions to write elegant GDScript. The goal is to
encourage writing clean, readable code and promote consistency across projects,
discussions, and tutorials. Hopefully, this will also support the development of
auto-formatting tools.

Since GDScript is close to Python, this guide is inspired by Python's
`PEP 8 <https://www.python.org/dev/peps/pep-0008/>`__ programming
style guide.

Style guides aren't meant as hard rulebooks. At times, you may not be able to
apply some of the guidelines below. When that happens, use your best judgment,
and ask fellow developers for insights.

In general, keeping your code consistent in your projects and within your team is
more important than following this guide to a tee.

.. note:: Godot's built-in script editor uses a lot of these conventions
          by default. Let it help you.

Here is a complete class example based on these guidelines:

::

    class_name StateMachine
    extends Node
    # Hierarchical State machine for the player.
    # Initializes states and delegates engine callbacks
    # (_physics_process, _unhandled_input) to the state.


    signal state_changed(previous, new)

    export var initial_state = NodePath()
    var is_active = true setget set_is_active

    onready var _state = get_node(initial_state) setget set_state
    onready var _state_name = _state.name


    func _init():
        add_to_group("state_machine")


    func _ready():
        connect("state_changed", self, "_on_state_changed")
        _state.enter()


    func _unhandled_input(event):
        _state.unhandled_input(event)


    func _physics_process(delta):
        _state.physics_process(delta)


    func transition_to(target_state_path, msg={}):
        if not has_node(target_state_path):
            return

        var target_state = get_node(target_state_path)
        assert(target_state.is_composite == false)

        _state.exit()
        self._state = target_state
        _state.enter(msg)
        Events.emit_signal("player_state_changed", _state.name)


    func set_is_active(value):
        is_active = value
        set_physics_process(value)
        set_process_unhandled_input(value)
        set_block_signals(not value)


    func set_state(value):
        _state = value
        _state_name = _state.name


    func _on_state_changed(previous, new):
        print("state changed")
        emit_signal("state_changed")

.. _formatting:

Formatting
----------

Encoding and special characters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Use line feed (**LF**) characters to break lines, not CRLF or CR. *(editor default)*
* Use one line feed character at the end of each file. *(editor default)*
* Use **UTF-8** encoding without a `byte order mark <https://en.wikipedia.org/wiki/Byte_order_mark>`_. *(editor default)*
* Use **Tabs** instead of spaces for indentation. *(editor default)*

Indentation
~~~~~~~~~~~

Each indent level should be one greater than the block containing it.

**Good**:

::

    for i in range(10):
        print("hello")

**Bad**:

::

    for i in range(10):
      print("hello")

    for i in range(10):
            print("hello")

Use 2 indent levels to distinguish continuation lines from
regular code blocks.

**Good**:

::

    effect.interpolate_property(sprite, "transform/scale",
                sprite.get_scale(), Vector2(2.0, 2.0), 0.3,
                Tween.TRANS_QUAD, Tween.EASE_OUT)

**Bad**:

::

    effect.interpolate_property(sprite, "transform/scale",
        sprite.get_scale(), Vector2(2.0, 2.0), 0.3,
        Tween.TRANS_QUAD, Tween.EASE_OUT)

Exceptions to this rule are arrays, dictionaries, and enums. Use a single
indentation level to distinguish continuation lines:

**Good**:

::

    var party = [
        "Godot",
        "Godette",
        "Steve",
    ]

    var character_dir = {
        "Name": "Bob",
        "Age": 27,
        "Job": "Mechanic",
    }

    enum Tiles {
        TILE_BRICK,
        TILE_FLOOR,
        TILE_SPIKE,
        TILE_TELEPORT,
    }

**Bad**:

::

    var party = [
            "Godot",
            "Godette",
            "Steve",
    ]

    var character_dir = {
            "Name": "Bob",
            "Age": 27,
            "Job": "Mechanic",
    }

    enum Tiles {
            TILE_BRICK,
            TILE_FLOOR,
            TILE_SPIKE,
            TILE_TELEPORT,
    }

Trailing comma
~~~~~~~~~~~~~~

Use a trailing comma on the last line in arrays, dictionaries, and enums. This
results in easier refactoring and better diffs in version control as the last
line doesn't need to be modified when adding new elements.

**Good**:

::

    enum Tiles {
        TILE_BRICK,
        TILE_FLOOR,
        TILE_SPIKE,
        TILE_TELEPORT,
    }

**Bad**:

::

    enum Tiles {
        TILE_BRICK,
        TILE_FLOOR,
        TILE_SPIKE,
        TILE_TELEPORT
    }

Trailing commas are unnecessary in single-line lists, so don't add them in this case.

**Good**:

::

    enum Tiles {TILE_BRICK, TILE_FLOOR, TILE_SPIKE, TILE_TELEPORT}

**Bad**:

::

    enum Tiles {TILE_BRICK, TILE_FLOOR, TILE_SPIKE, TILE_TELEPORT,}

Blank lines
~~~~~~~~~~~

Surround functions and class definitions with two blank lines:

::

    func heal(amount):
        health += amount
        health = min(health, max_health)
        emit_signal("health_changed", health)


    func take_damage(amount, effect=null):
        health -= amount
        health = max(0, health)
        emit_signal("health_changed", health)

Use one blank line inside functions to separate logical sections.

Line length
~~~~~~~~~~~

Keep individual lines of code under 100 characters.

If you can, try to keep lines under 80 characters. This helps to read the code
on small displays and with two scripts opened side-by-side in an external text
editor. For example, when looking at a differential revision.

One statement per line
~~~~~~~~~~~~~~~~~~~~~~

Never combine multiple statements on a single line. No, C programmers,
not even with a single line conditional statement.

**Good**:

::

    if position.x > width:
        position.x = 0

    if flag:
        print("flagged")

**Bad**:

::

    if position.x > width: position.x = 0

    if flag: print("flagged")

The only exception to that rule is the ternary operator:

::

   next_state = "fall" if not is_on_floor() else "idle"

Avoid unnecessary parentheses
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Avoid parentheses in expressions and conditional statements. Unless
necessary for order of operations, they only reduce readability.

**Good**:

::

    if is_colliding():
        queue_free()

**Bad**:

::

    if (is_colliding()):
        queue_free()

Boolean operators
~~~~~~~~~~~~~~~~~

Prefer the plain English versions of boolean operators, as they are the most accessible:

- Use ``and`` instead of ``&&``.
- Use ``or`` instead of ``||``.

You may also use parentheses around boolean operators to clear any ambiguity.
This can make long expressions easier to read.

**Good**:

::

    if (foo and bar) or baz:
        print("condition is true")

**Bad**:

::

    if foo && bar || baz:
        print("condition is true")

Comment spacing
~~~~~~~~~~~~~~~

Regular comments should start with a space, but not code that you comment out.
This helps differentiate text comments from disabled code.

**Good**:

::

    # This is a comment.
    #print("This is disabled code")

**Bad**:

::

    #This is a comment.
    # print("This is disabled code")

.. note::

   In the script editor, to toggle the selected code commented, press
   :kbd:`Ctrl + K`. This feature adds a single # sign at the start
   of the selected lines.

Whitespace
~~~~~~~~~~

Always use one space around operators and after commas. Also, avoid extra spaces
in dictionary references and function calls.

**Good**:

::

    position.x = 5
    position.y = target_position.y + 10
    dict["key"] = 5
    my_array = [4, 5, 6]
    print("foo")

**Bad**:

::

    position.x=5
    position.y = mpos.y+10
    dict ["key"] = 5
    myarray = [4,5,6]
    print ("foo")

Don't use spaces to align expressions vertically:

::

    x        = 100
    y        = 100
    velocity = 500

Quotes
~~~~~~

Use double quotes unless single quotes make it possible to escape fewer
characters in a given string. See the examples below:

::

    # Normal string.
    print("hello world")

    # Use double quotes as usual to avoid escapes.
    print("hello 'world'")

    # Use single quotes as an exception to the rule to avoid escapes.
    print('hello "world"')

    # Both quote styles would require 2 escapes; prefer double quotes if it's a tie.
    print("'hello' \"world\"")

.. _naming_conventions:

Naming conventions
------------------

These naming conventions follow the Godot Engine style. Breaking these will make
your code clash with the built-in naming conventions, leading to inconsistent
code.

File names
~~~~~~~~~~

Use snake_case for file names. For named classes, convert the PascalCase class
name to snake_case::

    # This file should be saved as `weapon.gd`.
    extends Node
    class_name Weapon

::

    # This file should be saved as `yaml_parser.gd`.
    extends Object
    class_name YAMLParser

This is consistent with how C++ files are named in Godot's source code. This
also avoids case sensitivity issues that can crop up when exporting a project
from Windows to other platforms.

Classes and nodes
~~~~~~~~~~~~~~~~~

Use PascalCase for class and node names:

::

   extends KinematicBody

Also use PascalCase when loading a class into a constant or a variable:

::

    const Weapon = preload("res://weapon.gd")

Functions and variables
~~~~~~~~~~~~~~~~~~~~~~~

Use snake\_case to name functions and variables:

::

   var particle_effect
   func load_level():

Prepend a single underscore (\_) to virtual methods functions the user must
override, private functions, and private variables:

::

   var _counter = 0
   func _recalculate_path():

Signals
~~~~~~~

Use the past tense to name signals:

::

    signal door_opened
    signal score_changed

Constants and enums
~~~~~~~~~~~~~~~~~~~

Write constants with CONSTANT\_CASE, that is to say in all caps with an
underscore (\_) to separate words:

::

    const MAX_SPEED = 200

Use PascalCase for enum *names* and CONSTANT\_CASE for their members, as they
are constants:

::

    enum Element {
        EARTH,
        WATER,
        AIR,
        FIRE,
    }


Code order
----------

This first section focuses on code order. For formatting, see
:ref:`formatting`. For naming conventions, see :ref:`naming_conventions`.

We suggest to organize GDScript code this way:

::

    01. tool
    02. class_name
    03. extends
    04. # docstring

    05. signals
    06. enums
    07. constants
    08. exported variables
    09. public variables
    10. private variables
    11. onready variables

    12. optional built-in virtual _init method
    13. built-in virtual _ready method
    14. remaining built-in virtual methods
    15. public methods
    16. private methods

We optimized the order to make it easy to read the code from top to bottom, to
help developers reading the code for the first time understand how it works, and
to avoid errors linked to the order of variable declarations.

This code order follows four rules of thumb:

1. Properties and signals come first, followed by methods.
2. Public comes before private.
3. Virtual callbacks come before the class's interface.
4. The object's construction and initialization functions, ``_init`` and
   ``_ready``, come before functions that modify the object at runtime.


Class declaration
~~~~~~~~~~~~~~~~~

If the code is meant to run in the editor, place the ``tool`` keyword on the
first line of the script.

Follow with the `class_name` if necessary. You can turn a GDScript file into a
global type in your project using this feature. For more information, see
:ref:`doc_gdscript`.

Then, add the `extends` keyword if the class extends a built-in type.

Following that, you should have the class's optional docstring as comments. You
can use that to explain the role of your class to your teammates, how it works,
and how other developers should use it, for example.

::

   class_name MyNode
   extends Node
   # A brief description of the class's role and functionality.
   # Longer description.

Signals and properties
~~~~~~~~~~~~~~~~~~~~~~

Write signal declarations, followed by properties, that is to say, member
variables, after the docstring.

Enums should come after signals, as you can use them as export hints for other
properties.

Then, write constants, exported variables, public, private, and onready
variables, in that order.

::

   signal spawn_player(position)

   enum Jobs {KNIGHT, WIZARD, ROGUE, HEALER, SHAMAN}

   const MAX_LIVES = 3

   export(Jobs) var job = Jobs.KNIGHT
   export var max_health = 50
   export var attack = 5

   var health = max_health setget set_health

   var _speed = 300.0

   onready var sword = get_node("Sword")
   onready var gun = get_node("Gun")


.. note::

   The GDScript compiler evaluates onready variables right before the ``_ready``
   callback. You can use that to cache node dependencies, that is to say, to get
   child nodes in the scene that your class relies on. This is what the example
   above shows.

Member variables
~~~~~~~~~~~~~~~~

Don't declare member variables if they are only used locally in a method, as it
makes the code more difficult to follow. Instead, declare them as local
variables in the method's body.

Local variables
~~~~~~~~~~~~~~~

Declare local variables as close as possible to their first use. This makes it
easier to follow the code, without having to scroll too much to find where the
variable was declared.

Methods and static functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After the class's properties come the methods.

Start with the ``_init()`` callback method, that the engine will call upon
creating the object in memory. Follow with the ``_ready()`` callback, that Godot
calls when it adds a node to the scene tree.

These function should come first because they show how the object is
initialized.

Other built-in virtual callbacks, like ``_unhandled_input()`` and
``_physics_process``, should come next. These control the object's main loop and
interactions with the game engine.

The rest of the class's interface, public and private methods, come after that,
in that order.

::

    func _init():
        add_to_group("state_machine")


    func _ready():
        connect("state_changed", self, "_on_state_changed")
        _state.enter()


    func _unhandled_input(event):
        _state.unhandled_input(event)


    func transition_to(target_state_path, msg={}):
        if not has_node(target_state_path):
            return

        var target_state = get_node(target_state_path)
        assert(target_state.is_composite == false)

        _state.exit()
        self._state = target_state
        _state.enter(msg)
        Events.emit_signal("player_state_changed", _state.name)


    func _on_state_changed(previous, new):
        print("state changed")
        emit_signal("state_changed")


Static typing
-------------

Since Godot 3.1, GDScript supports :ref:`optional static typing<doc_gdscript_static_typing>`.

Type hints
~~~~~~~~~~

Place the colon right after the variable's name, without a space, and let the
GDScript compiler infer the variable's type when possible.

**Good**:

::

   onready var health_bar: ProgressBar = get_node("UI/LifeBar")

   var health := 0 # The compiler will use the int type.

**Bad**:

::

   # The compiler can't infer the exact type and will use Node
   # instead of ProgressBar.
   onready var health_bar := get_node("UI/LifeBar")

When you let the compiler infer the type hint, write the colon and equal signs together: ``:=``.

::

   var health := 0 # The compiler will use the int type.

Add a space on either sides of the return type arrow when defining functions.

::

   func heal(amount: int) -> void:
