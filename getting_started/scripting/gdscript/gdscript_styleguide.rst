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

One statement per line
~~~~~~~~~~~~~~~~~~~~~~

Never combine multiple statements on a single line. No, C programmers,
not with a single line conditional statement (except with the ternary
operator)!

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

Comment spacing
~~~~~~~~~~~~~~~

Normal comments should start with a space, but comments which are disabled
code should not. This helps differentiate text comments from disabled code.

**Good**:

::

    # This is a comment.
    #print("This is disabled code")

**Bad**:

::

    #This is a comment.
    # print("This is disabled code")

Whitespace
~~~~~~~~~~

Always use one space around operators and after commas. Avoid extra
spaces in dictionary references and function calls, or to create "columns."

**Good**:

::

    position.x = 5
    position.y = mpos.y + 10
    dict["key"] = 5
    myarray = [4, 5, 6]
    print("foo")

**Bad**:

::

    position.x=5
    position.y = mpos.y+10
    dict ['key'] = 5
    myarray = [4,5,6]
    print ('foo')

**NEVER**:

::

    x        = 100
    y        = 100
    velocity = 500

Naming conventions
------------------

These naming conventions follow the Godot Engine style. Breaking these
will make your code clash with the built-in naming conventions, which is
ugly.

Classes and nodes
~~~~~~~~~~~~~~~~~

Use PascalCase: ``extends KinematicBody``

Also when loading a class into a constant or variable:

::

    const MyCoolNode = preload("res://my_cool_node.gd")

Functions and variables
~~~~~~~~~~~~~~~~~~~~~~~

Use snake\_case: ``get_node()``

Prepend a single underscore (\_) to virtual methods (functions the user
must override), private functions, and private variables:
``func _ready()``

Signals
~~~~~~~

Use past tense:

::

    signal door_opened
    signal score_changed

Constants
~~~~~~~~~

Use CONSTANT\_CASE, all caps, with an underscore (\_) to separate words:
``const MAX_SPEED = 200``

Static typing
-------------

Since Godot 3.1, GDScript supports :ref:`optional static typing<doc_gdscript_static_typing>`.

Type hints
~~~~~~~~~~

Place the colon right after the variable's name, without a space, and let the GDScript compiler infer the variable's type when possible.


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
