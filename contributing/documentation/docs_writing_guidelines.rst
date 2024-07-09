.. _doc_docs_writing_guidelines:

Writing guidelines
==================

The Godot community is rich and international. Users come from all
around the world. Some of them are young, and many aren't native English
speakers. That's why we must all write using a clear and a common
language. For the class reference, the goal is to make it easy to read
for everyone and precise.

In summary, always try to:

1. Use the active voice
2. Use precise action verbs
3. Avoid verbs that end in -ing
4. Remove unnecessary adverbs and adjectives.
5. Ban these 8 words: obvious, simple, basic, easy, actual, just, clear, and however
6. Use explicit references
7. Use 's to show possession
8. Use the Oxford comma

There are 3 rules to describe classes:

1. Give an overview of the node in the brief description
2. Mention what methods return if it's useful
3. Use "if true" to describe booleans

.. note::

    A technical writer's job is to pack as much information as possible into
    the smallest and clearest sentences possible. These guidelines will help
    you work towards that goal.

.. seealso::

    See the :ref:`content guidelines <doc_content_guidelines>` for information
    on the types of documentation you can write in the official documentation.

7 rules for clear English
-------------------------

Use the active voice
~~~~~~~~~~~~~~~~~~~~

Use the active voice when possible. Take the classes, methods, and
constants you describe as the subject. It's natural to write using the
passive voice, but it's harder to read and produces longer sentences.

.. highlight:: none

Passive:

::

    The man **was bitten** by the dog.

Active:

::

    The dog bit the man.

**Don't** use the passive voice:

::

    void edit_set_pivot ( Vector2 pivot )
    [...] This method **is implemented** only in some nodes that inherit Node2D.

**Do** use the node's name as a noun:

::

    void edit_set_pivot ( Vector2 pivot )
    [...] Only some Node2Ds **implement** this method.

Use precise action verbs
~~~~~~~~~~~~~~~~~~~~~~~~

Favor precise yet common verbs over generic ones like ``make``, ``set``,
and any expression you can replace with a single word.

**Don't** repeat the method's name. It already states it sets the pivot
value to a new one:

::

    void edit_set_pivot ( Vector2 pivot )
    Set the pivot position of the 2D node to [code]pivot[/code] value. [...]

**Do** explain what's the consequence of this "set": use precise verbs
like ``place``, ``position``, ``rotate``, ``fade``, etc.

::

    void edit_set_pivot ( Vector2 pivot )
    Position the node's pivot to the [code]pivot[/code] value. [...]

Avoid verbs that end in -ing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The progressive forms describe continuous actions. E.g. "is calling",
"is moving".

**Don't** use the progressive form for instant changes.

::

    Vector2 move ( Vector2 rel_vec )
    Move the body in the given direction, **stopping** if there is an obstacle. [...]

**Do** use simple present, past, or future.

::

    Vector2 move ( Vector2 rel_vec )
    Moves the body in the vector's direction. The body **stops** if it collides with an obstacle. [...]

Exception: If the subject is not clear, replacing "ing" verbs is not an
improvement. For example, in the previous sentence, "it replaces"
would not make much sense where "replacing" currently is.

You may use the progressive tense to describe actions that are
continuous in time. Anything like animation or coroutines.

.. tip::

    Verbs can turn into adjectival nouns with -ing. This is not a
    conjugation, so you may use them: ``the remaining movement``,
    ``the missing file``, etc.

Remove unnecessary adverbs and adjectives
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Write as few adjectives and adverbs as possible. Only use them if they
add key information to the description.

**Don't** use redundant or meaningless adverbs. Words that lengthen the
documentation but don't add any information:

::

    **Basically** a big texture [...]

**Do** write short sentences in a simple, descriptive language:

::

    A big texture [...]

Ban these 8 words
~~~~~~~~~~~~~~~~~

**Don't** ever use these 8 banned words:

1. obvious
2. simple
3. basic
4. easy
5. actual
6. just
7. clear
8. however (some uses)

Game creation and programming aren't simple, and nothing's easy to
someone learning to use the API for the first time. Other words in the
list, like ``just`` or ``actual`` won't add any info to the sentence.
Don't use corresponding adverbs either: obviously, simply, basically,
easily, actually, clearly.

**Don't** example. The banned words lengthen the description and take
attention away from the most important info:

::

    **TextureRect**
    Control frame that **simply** draws an assigned texture. It can stretch or not. It's a **simple** way to **just** show an image in a UI.

**Do** remove them:

::

    **TextureRect**
    [Control] node that displays a texture. The texture can stretch to the node's bounding box or stay in the center. Useful to display sprites in your UIs.

"Simple" never helps. Remember, for other users, anything could be
complex or frustrate them. There's nothing like a good old *it's simple*
to make you cringe. Here's the old brief description, the first sentence
on the Timer node's page:

::

    **Timer**
    A **simple** Timer node.

**Do** explain what the node does instead:

::

    **Timer**
    Calls a function of your choice after a certain duration.

**Don't** use "basic", it is too vague:

::

    **Vector3**
    Vector class, which performs **basic** 3D vector math operations.

**Do** use the brief description to offer an overview of the node:

::

    **Vector3**
    Provides essential math functions to manipulate 3D vectors: cross product, normalize, rotate, etc.

Use explicit references
~~~~~~~~~~~~~~~~~~~~~~~

Favor explicit references over implicit ones.

**Don't** use words like "the former", "the latter", etc. They're not
the most common in English, and they require you to check the reference.

::

    [code]w[/code] and [code]h[/code] define right and bottom margins. The **latter** two resize the texture so it fits in the defined margin.

**Do** repeat words. They remove all ambiguity:

::

    [code]w[/code] and [code]h[/code] define right and bottom margins. **[code]w[/code] and [code]h[/code]** resize the texture so it fits the margin.

If you need to repeat the same variable name 3 or 4 times, you probably
need to rephrase your description.

Use 's to show possession
~~~~~~~~~~~~~~~~~~~~~~~~~

Avoid "The milk **of** the cow". It feels unnatural in English. Write "The cow's
milk" instead.

**Don't** write "of the X":

::

    The region **of the AtlasTexture that is** used.

**Do** use ``'s``. It lets you put the main subject at the start of the
sentence, and keep it short:

::

    The **AtlasTexture's** used region.

Use the Oxford comma to enumerate anything
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

From the Oxford dictionary:

    The 'Oxford comma' is an optional comma before the word 'and' at the end of a list:
    *We sell books, videos, and magazines.*

    [...] Not all writers and publishers use it, but it can clarify the meaning of a sentence when the items in a list are not single words:
    *These items are available in black and white, red and yellow, and blue and green.*

**Don't** leave the last element of a list without a comma:

::

    Create a CharacterBody2D node, a CollisionShape2D node and a sprite node.

**Do** add a comma before `and` or `or`, for the last
element of a list with more than two elements.

::

    Create a CharacterBody2D node, a CollisionShape2D node, and a sprite node.


How to write methods and classes
--------------------------------

Dynamic vs static typing
~~~~~~~~~~~~~~~~~~~~~~~~

The code examples in the documentation should follow a consistent style not to
confuse users. As static type hints are an optional feature of GDScript, we
chose to stick to writing dynamic code. This leads to writing GDScript that is
concise and accessible.

The exception is topics that explain static typing concepts to users.

**Don't** add a type hint with a colon or by casting:

::

    const MainAttack := preload("res://fire_attack.gd")
    var hit_points := 5
    var name: String = "Bob"
    var body_sprite := $Sprite2D as Sprite2D


**Do** write constants and variables with dynamic typing:

::

    const MainAttack = preload("res://fire_attack.gd")
    var hit_points = 5
    var name = "Bob"
    var body_sprite = $Sprite2D


**Don't** write functions with inferred arguments or return types:

::

    func choose(arguments: PackedStringArray) -> String:
        # Chooses one of the arguments from array with equal chances
        randomize()
        var size := arguments.size()
        var choice: int = randi() % size
        return arguments[choice]

**Do** write functions using dynamic typing:

::

    func choose(arguments):
        # Chooses one of the arguments from array with equal chances
        randomize()
        var size = arguments.size()
        var choice = randi() % size
        return arguments[choice]

Use real-world code examples where appropriate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Real-world examples are more accessible to beginners than abstract ``foos`` and
``bars``. You can also copy them directly from your game projects, ensuring that
any code snippet compiles without errors.

Writing ``var speed = 10`` rather than ``var my_var = 10`` allows beginners to
understand code better. It gives them a frame of reference as to where they
could use the code snippets in a live project.

**Don't** write made-up examples:

.. code-block:: gdscript

    @onready var a = preload("res://MyPath")
    @onready var my_node = $MyNode


    func foo():
        # Do stuff

**Do** write concrete examples:

.. code-block:: gdscript

    @onready var sfx_player_gun = preload("res://Assets/Sound/SFXPlayerGun.ogg")
    @onready var audio_player = $Audio/AudioStreamPlayer


    func play_shooting_sound():
        audio_player.stream = sfx_player_gun
        audio_player.play()

Of course, there are times when using real-world examples is impractical. In
those situations, you should still avoid using names such as ``my_var``,
``foo()`` or ``my_func()`` and consider more meaningful names for your examples.

Give an overview of the node in the brief description
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The brief description is the reference's most important sentence. It's
the user's first contact with a node:

1. It's the only description in the "Create New Node" dialog.
2. It's at the top of every page in the reference

The brief description should explain the node's role and its
functionality, in up to 200 characters.

**Don't** write tiny and vague summaries:

::

    **Node2D**
    Base node for 2D system.

**Do** give an overview of the node's functionality:

::

    **Node2D**
    A 2D game object, inherited by all 2D-related nodes. Has a position, rotation, scale, and Z index.

Use the node's full description to provide more information, and a code
example, if possible.

Mention what methods return if it's useful
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Some methods return important values. Describe them at the end of the
description, ideally on a new line. No need to mention the return values
for any method whose name starts with ``set`` or ``get``.

**Don't** use the passive voice:

::

    Vector2 move ( Vector2 rel_vec )
    [...] The returned vector is how much movement was remaining before being stopped.

**Do** always use "Returns".

::

    Vector2 move ( Vector2 rel_vec )
    [...] Returns the remaining movement before the body was stopped.

Notice the exception to the "direct voice" rule: with the move method,
an external collider can influence the method and the body that calls
``move``. In this case, you can use the passive voice.

Use "if true" to describe booleans
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For boolean member variables, always use ``if true`` and/or
``if false``, to stay explicit. ``Controls whether or not`` may be
ambiguous and won't work for every member variable.

Also, surround boolean values, variable names and methods with ``[code][/code]``.

**Do** start with "if true":

::

    Timer.autostart
    If [code]true[/code], the timer will automatically start when entering the scene tree.


Use ``[code]`` around arguments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the class reference, always surround arguments with ``[code][/code]``. In the
documentation and in Godot, it will display like ``this``. When you edit XML
files in the Godot repository, replace existing arguments written like 'this' or
\`this\` with ``[code]this[/code]``.


Common vocabulary to use in Godot's documentation
-------------------------------------------------

The developers chose some specific words to refer to areas of the
interface. They're used in the sources, in the documentation, and you
should always use them instead of synonyms, so the users know what
you're talking about.

.. figure:: img/editor-vocabulary-overview.png
   :alt: Overview of the interface and common vocabulary

   Overview of the interface and common vocabulary

In the top left corner of the editor lie the ``main menus``. In the
center, the buttons change the ``workspace``. And together the buttons
in the top right are the ``playtest buttons``. The area in the center,
that displays the 2D or the 3D space, is the ``viewport``. At its top,
you find a list of ``tools`` inside the ``toolbar``.

The tabs or dockable panels on either side of the viewport are
``docks``. You have the ``FileSystem dock``, the ``Scene dock`` that
contains your scene tree, the ``Import dock``, the ``Node dock``, and
the ``Inspector`` or ``Inspector dock``. With the default layout you may
call the tabbed docks ``tabs``: the ``Scene tab``, the ``Node tab``...

The Animation, Debugger, etc. at the bottom of the viewport are
``panels``. Together they make up the ``bottom panels``.

Foldable areas of the Inspector are ``sections``. The node's parent
class names, which you can't fold, are ``Classes`` e.g. the
``CharacterBody2D class``. And individual lines with key-value pairs are
``properties``. E.g. ``position`` or ``modulate color`` are both
``properties``.

Keyboard shortcut guidelines
----------------------------

Keyboard and mouse shortcuts should make use of the ``:kbd:`` tag, which allows
shortcuts to stand out from the rest of the text and inline code. Use the
compact form for modifier keys (:kbd:`Ctrl`/:kbd:`Cmd`) instead of their spelled
out form (:kbd:`Control`/:kbd:`Command`). For combinations, use the ``+`` symbol
with a space on either side of the symbol.

Make sure to mention shortcuts that differ on macOS compared to other platforms.
You can find a list of all shortcuts, including what they are on macOS, on
:ref:`this page <doc_default_key_mapping>`.

Try to integrate the shortcut into sentences the best you can. Here are some
examples with the ``:kbd:`` tag left as-is for better visibility:

- Press ``:kbd:`Ctrl + Alt + T``` to toggle the panel (``:kbd:`Opt + Cmd + T``` on macOS).
- Press ``:kbd:`Space``` and hold the left mouse button to pan in the 2D editor.
- Press ``:kbd:`Shift + Up Arrow``` to move the node upwards by 8 pixels.
