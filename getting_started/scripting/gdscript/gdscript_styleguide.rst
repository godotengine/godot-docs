.. _doc_gdscript_styleguide:

GDScript Style Guide
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

Code Structure
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

    effect.interpolate_property(sprite, 'transform/scale',
                sprite.get_scale(), Vector2(2.0, 2.0), 0.3,
                Tween.TRANS_QUAD, Tween.EASE_OUT)

**Bad**:

::

    effect.interpolate_property(sprite, 'transform/scale',
        sprite.get_scale(), Vector2(2.0, 2.0), 0.3,
        Tween.TRANS_QUAD, Tween.EASE_OUT)

Blank lines
~~~~~~~~~~~

Surround functions and class definitions by a blank line.

Use one blank line inside functions to separate logical sections.

One Statement per Line
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

Avoid Unnecessary Parentheses
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

Whitespace
~~~~~~~~~~

Always use one space around operators and after commas. Avoid extra
spaces in dictionary references and function calls, or to create "columns."

**Good**:

::

    position.x = 5
    position.y = mpos.y + 10
    dict['key'] = 5
    myarray = [4, 5, 6]
    print('foo')

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

Naming Conventions
------------------

These naming conventions follow the Godot Engine style. Breaking these
will make your code clash with the built-in naming conventions, which is
ugly.

Classes and Nodes
~~~~~~~~~~~~~~~~~

Use PascalCase: ``extends KinematicBody``

Also when loading a class into a constant or variable:

::

    const MyCoolNode = preload('res://my_cool_node.gd')

Functions and Variables
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
