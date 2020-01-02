.. _doc_gdscript_styleguide:

GDScript style guide
====================

Description
-----------

This styleguide lists conventions to write elegant GDScript. The goal is
to encourage writing clean, readable code and promote consistency across
projects, discussions, and tutorials. Hopefully, this will also
encourage development of auto-formatting tools.

Since GDScript is close to Python, this guide is inspired by Python's
`PEP 8 <https://www.python.org/dev/peps/pep-0008/>`__ programming
styleguide.

.. note:: Godot's built-in script editor uses a lot of these conventions
          by default. Let it help you.

Code structure
--------------

Indentation
~~~~~~~~~~~

Indent type: Tabs *(editor default)*

Indent size: 4 *(editor default)*

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

Try to keep lines under 80 characters. This ensures greater readability on small
displays and splitted editors (such as side-by-side diffs). It's OK to go over
by a few characters, but a line should never exceed 100 characters.

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
   <kbd>Ctrl</kbd> <kbd>K</kbd>. This feature adds a single # sign at the start
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

Naming conventions
------------------

These naming conventions follow the Godot Engine style. Breaking these
will make your code clash with the built-in naming conventions, which is
ugly.

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

   var health := 0 # The compiler will use the int type

**Bad**:

::

   # The compiler can't infer the exact type and will use Node
   # instead of ProgressBar
   onready var health_bar := get_node("UI/LifeBar")

When you let the compiler infer the type hint, write the colon and equal signs together: ``:=``.

::

   var health := 0 # The compiler will use the int type

Add a space on either sides of the return type arrow when defining functions.

::

   func heal(amount: int) -> void:
