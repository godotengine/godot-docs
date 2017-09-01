.. _doc_scripting:

Scripting
=========

Introduction
------------

Much has been said about tools that allow users to create video games
without programming. This appeals to many people who would love to be able to
make a game without having to learn how to code. This need has been around for
a long time, even inside game companies, where game designers would like to
have more control of their game's flow.

Many products have been shipped promising such a no-programming environment,
but the results often fall short of expectations. The projects they produce end
up being too complex or require solutions that are too inefficient compared to
what could have been accomplished with traditional code.

As a result, we think that programming is here to stay. In fact, game engines
have been moving in this direction, adding tools that try to reduce the amount
of code that needs to be written rather than eliminating it. The engine can
provide many general solutions, while the developer can use code to accomplish
specific tasks.

Godot has embraced this goal from the beginning, and it has influenced many of
its design decisions. First and foremost is the scene system. This system has
many benefits, but fundamentally its goal is to relieve programmers from the
responsibility of having to implement an overall architecture.

When designing games using the scene system, the whole project is fragmented
into *complementary* scenes (not individual ones). Scenes complement
(i.e. help) each other, instead of being separate. There will be plenty of
examples of this later on, but it's very important to remember it.

GDScript
--------

:ref:`doc_gdscript` is a dynamically typed scripting language which was
designed with the following goals:

- Most importantly, it should feel simple, familiar, and as easy to learn as
  possible.
- It should have a syntax that's very readable. The syntax is mostly borrowed
  from Python.
- It should integrate tightly with Godot itself, for example sharing its memory
  model, taking advantage of the scene/node system, and exposing useful
  game-related classes already part of the Godot engine.

Programmers generally take a few days to learn GDScript and feel comfortable
with it within two weeks.

As with most dynamically typed languages, the higher productivity (code is
easier to learn, faster to write, no compilation, etc.) is balanced with a
performance penalty. However, keep in mind that most critical code is already
written in C++ in the engine (vector ops, physics, math, indexing, etc.), which
results in more than sufficient performance for most types of games.

In any case, if more performance is required, critical sections can be
rewritten in C++ and registered with Godot, which in turn exposes them to all
scripts. In this way, you can write a class in GDScript first but convert it to
a C++ class later, and the rest of the game will work the same as before.

Finally, note that GDScript provides the powerful
`extend <http://c2.com/cgi/wiki?EmbedVsExtend>`__ keyword. Many classes in the
Godot engine are available as base classes to be extended from.

Scripting a scene
-----------------

In the rest of this tutorial, we'll set up a simple GUI scene consisting of a
button and a label, where pressing the button will update the label. This will
demonstrate:

- how to write a basic script and attach it to a node
- how to hook up UI elements via *signals*
- how to write a script that can access other nodes in the scene

Before continuing, please make sure to read the :ref:`doc_gdscript` reference.
It's a simple language and the reference is short, so it will not take more
than a few minutes to get an overview of the concepts.

Scene setup
~~~~~~~~~~~

Use the add node dialog to create the following hierarchy, with the following
nodes:

- Panel

  * Label
  * Button

It should look like this in the scene tree:

.. image:: /img/scripting_scene_tree.png

Use the 2D editor to position and resize the button and label so that they
look like the image below. You can set the text in the Inspector pane.

.. image:: /img/label_button_example.png

Finally, save the scene, with a name such as "sayhello.tscn"

.. _doc_scripting-adding_a_script:

Adding a script
~~~~~~~~~~~~~~~

Right click on the panel node, and then select "Add Script" in the context
menu:

.. image:: /img/add_script.png

The script creation dialog will pop up. This dialog allows you to set the
language, class name, and other relevant options.

Actually, in GDScript, the file itself represents the class, so in this case,
the class name field is not editable.

The node we're attaching the script to is a panel, so the "Inherits" field
should automatically be filled in with "Panel". This is what we want as our
script's goal is to extend this panel node's functionality.

Finally, enter a path name for the script and select "Create":

.. image:: /img/script_create.png

Once this is done, the script will be created and added to the node. You can
see this both as an extra icon in the node as well as in the script property:

.. image:: /img/script_added.png

To edit the script, select either of the highlighted buttons. This will bring
you to the script editor where an existing template will be included by default:

.. image:: /img/script_template.png

There is not much in there. The "_ready()" function is called when the
node (and all its children) enter the active scene. (Note: "_ready()" is not
the a constructor; the constructor is "_init()").

The role of the script
~~~~~~~~~~~~~~~~~~~~~~

A script adds behavior to a node. It is used to control how the node functions
as well as how it interacts with other nodes (children, parent, siblings,
etc.). The local scope of the script is the node. In other words, the script
inherits the functions provided by that node.

.. image:: /img/brainslug.jpg

Handling a signal
~~~~~~~~~~~~~~~~~

Signals are "emitted" when some specific kind of action happens, and they can be
connected to any function of any script instance. Signals are used mostly in
GUI nodes (although other nodes have them too, and you can even define custom
signals in your own scripts).

In this step, we'll connect the "pressed" signal to a custom function.

The editor provides an interface for connecting signals to your scripts. You
can access this by selecting the node in the scene tree and then selecting the
"Node" tab. Next, make sure that you have "Signals" selected.

.. image:: /img/signals.png

At this point, you could use the visual interface to hook up the "pressed"
signal by double clicking on it and selecting a target node that already has a
script attached to it. But for the sake of learning, we're going to code up the
connection manually.

To accomplish this, we will introduce a function that is probably the most used
by Godot programmers, namely :ref:`Node.get_node() <class_Node_get_node>`.
This function uses paths to fetch nodes anywhere in the scene, relative to the
node that owns the script.

In our case, because the button and the label are siblings under the panel
where the script is attached, you can fetch the button as follows:

::

    get_node("Button")

Next, write a function which will be called when the button is pressed:

.. tabs::
 .. code-tab:: gdscript GDScript

    func _on_button_pressed():  
        get_node("Label").set_text("HELLO!")

 .. code-tab:: csharp

   // i dont know how this is supposed to be in C#

 .. group-tab:: VS

    .. image:: /img/signals.png

Finally, connect the button's "pressed" signal to that callback in _ready(), by
using :ref:`Object.connect() <class_Object_connect>`.

::

    func _ready():
        get_node("Button").connect("pressed",self,"_on_button_pressed")

The final script should look basically like this:

::

    extends Panel

    func _on_button_pressed():
        get_node("Label").set_text("HELLO!")

    func _ready():
        get_node("Button").connect("pressed",self,"_on_button_pressed")

Run the scene and press the button. You should get the following result:

.. image:: /img/scripting_hello.png

Why hello there! Congratulations on scripting your first scene.

**Note:** A common misunderstanding in this tutorial is how get_node(path)
works. For some given node, get_node(path) searches its immediate children.
In the above code, this means that *Button* must be a child of *Panel*. If
*Button* were instead a child of *Label*, the code to obtain it would be:

::

    # not for this case
    # but just in case
    get_node("Label/Button") 

Also, remember that nodes are referenced by name, not by type.
