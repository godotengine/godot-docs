.. _doc_what_are_godot_classes:

Godot scenes and scripts are classes
====================================

In Godot, scripts and scenes can both be the equivalent of classes in an
Object-Oriented programming language. The main difference is that scenes are
`declarative code <https://en.wikipedia.org/wiki/Declarative_programming>`_,
while scripts can contain `imperative code
<https://en.wikipedia.org/wiki/Imperative_programming>`_.

As a result, many best practices in Godot boil down to applying Object-Oriented
design principles to the scenes, nodes, or script that make up your game.

This guide explains how scripts and scenes work in the engine's core, to help
you get a sense of how Godot works under the hood, and to help you better
understand where some of this series' best practices come from.

Making sense of classes in Godot
--------------------------------

Godot Engine provides built-in classes like :ref:`Node <class_Node>`.
User-created types are not technically classes. Instead, they are resources that
tell the engine a sequence of initializations to perform on one of the engine's
built-in classes.

Godot's internal classes have methods that register a class's data with a
:ref:`ClassDB <class_ClassDB>`. This database provides runtime access to class
information. ``ClassDB`` contains information about classes like:

- properties
- methods
- constants
- signals

This ``ClassDB`` is what Objects check against when performing an operation like
accessing a property or calling a method. ``ClassDB`` checks the database's
records and the records of the Object's base types to see if the Object supports
the operation.

On the engine's side, every class defines a static ``_bind_methods()`` function
that describes what C++ content it registers to the database and how. When you
use the engine, you can extend the methods, properties, and signals available from
the ``ClassDB`` by attaching a :ref:`Script <class_Script>` to your node.

Objects check their attached script before the database. This is why scripts can
override built-in methods. If a script defines a ``_get_property_list()`` method,
Godot appends that data to the list of properties the Object fetches from the
ClassDB. The same is true for other declarative code.

Even scripts that don't inherit from a built-in type, i.e. scripts that don't
start with the ``extends`` keyword, implicitly inherit from the engine's base
:ref:`Reference <class_Reference>` class. This allows the Object to defer
to the script's content where the engine logic deems appropriate.

.. note::

   As a result, you can instance scripts without the ``extends`` keyword
   from code, but you cannot attach them to a :ref:`Node <class_Node>`


Scripting performances and PackedScene
--------------------------------------

As the size of Objects increases, the scripts' necessary size to create them
grows much, much larger. Creating node hierarchies demonstrates this. Each
individual Node's logic could be several hundred lines of code in length.

Let's see a simple example of creating a single ``Node`` as a child. The code
below creates a new ``Node``, changes its name, assigns a script to it, sets its
future parent as its owner so it gets saved to disk along with it, and finally
adds it as a child of the ``Main`` node:

.. tabs::
  .. code-tab:: gdscript GDScript

    # Main.gd
    extends Node

    func _init():
        var child = Node.new()
        child.name = "Child"
        child.script = preload("Child.gd")
        child.owner = self
        add_child(child)

  .. code-tab:: csharp

    using System;
    using Godot;

    namespace ExampleProject
    {
        public class Main : Resource
        {
            public Node Child { get; set; }

            public Main()
            {
                Child = new Node();
                Child.Name = "Child";
                Child.Script = (Script)ResourceLoader.Load("child.gd");
                Child.Owner = this;
                AddChild(Child);
            }
        }
    }

Script code like this is much slower than engine-side C++ code. Each change
makes a separate call to the scripting API which leads to many "look-ups" on the
back-end to find the logic to execute.

Scenes help to avoid this performance issue. :ref:`PackedScene
<class_PackedScene>`, the base type that scenes inherit from, are resources that
use serialized data to create objects. The engine can process scenes in batches
on the back-end and provide much better performance than scripts.

Scenes and scripts are objects
------------------------------

Why is any of this important to scene organization? Because scenes *are*
objects. One often pairs a scene with a scripted root node that makes use of the
sub-nodes. This means that the scene is often an extension of the script's
declarative code.

The content of a scene helps to define:

- What nodes are available to the script
- How they are organized
- How are they initialized
- What signal connections they have with each other

Many Object-Oriented principles which apply to written code *also* apply to
scenes.

The scene is *always an extension of the script attached to its root node*. You
can see all the nodes it contains as part of a single class.

Most of the tips and techniques explained in this series will build on this.
