.. _doc_what_are_godot_classes:

Applying object-oriented principles in Godot
============================================

The engine offers two main ways to create reusable objects: scripts and scenes. Neither of these
technically define classes under the hood.

Still, many best practices using Godot involve applying object-oriented programming principles to
the scripts and scenes that compose your game. That is why it's useful to understand how we can
think of them as classes.

This guide briefly explains how scripts and scenes work in the engine's core to help you understand
how they work under the hood.

How scripts work in the engine
------------------------------

The engine provides built-in classes like :ref:`Node <class_Node>`. You can extend those to create
derived types using a script.

These scripts are not technically classes. Instead, they are resources that tell the engine a
sequence of initializations to perform on one of the engine's built-in classes.

Godot's internal classes have methods that register a class's data with a :ref:`ClassDB
<class_ClassDB>`. This database provides runtime access to class information. ``ClassDB`` contains
information about classes like:

- Properties.
- Methods.
- Constants.
- Signals.

This ``ClassDB`` is what objects check against when performing an operation like accessing a
property or calling a method. It checks the database's records and the object's base types' records
to see if the object supports the operation.

Attaching a :ref:`Script <class_Script>` to your object extends the methods, properties, and signals
available from the ``ClassDB``.

.. note::

    Even scripts that don't use the ``extends`` keyword implicitly inherit from the engine's base
    :ref:`RefCounted <class_RefCounted>` class. As a result, you can instantiate scripts without the
    ``extends`` keyword from code. Since they extend ``RefCounted`` though, you cannot attach them to
    a :ref:`Node <class_Node>`.

Scenes
------

The behavior of scenes has many similarities to classes, so it can make sense to think of a scene as
a class. Scenes are reusable, instantiable, and inheritable groups of nodes. Creating a scene is
similar to having a script that creates nodes and adds them as children using ``add_child()``.

We often pair a scene with a scripted root node that makes use of the scene's nodes. As such,
the script extends the scene by adding behavior through imperative code.

The content of a scene helps to define:

- What nodes are available to the script.
- How they are organized.
- How they are initialized.
- What signal connections they have with each other.

Why is any of this important to scene organization? Because instances of scenes *are* objects. As a
result, many object-oriented principles that apply to written code also apply to scenes: single
responsibility, encapsulation, and others.

The scene is *always an extension of the script attached to its root node*, so you can interpret it
as part of a class.

Most of the techniques explained in this best practices series build on this point.
