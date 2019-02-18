.. _doc_what_are_godot_classes:

What are Godot classes really?
==============================

Godot offers two main means of creating types: scripts and scenes.
Both of these represent a "class" since Godot revolves around
Object-Oriented design. *How* they do this may not be clear to beginner
or intermediate users though.

Godot Engine provides classes out-of-the-box (like
:ref:`Node <class_Node>`), but user-created types are not actually classes.
Instead they are resources that tell the engine a sequence of initializations
to perform on an engine class.

Godot's internal classes have methods that register a class's data with
a :ref:`ClassDB <class_ClassDB>`. This database provides runtime access to
class information (also called "reflection"). Things stored in the ClassDB
include, among other things...

- properties

- methods

- constants

- signals

Furthermore, this ClassDB is what Objects actually check against when
performing any operation. Access a property? Call a method? Emit a signal?
It will check the database's records (and the records of the Object's base
types) to see if the Object supports the operation. Every C++ Object defines
a static `_bind_methods()` function that describes what C++ content it
registers to the database and how.

So, if the engine provides all of this data at startup, then how does
a user define their own data? It'd be nice if users could define a custom
set of data to be appended to an object's data. That way, users could inject
their own properties and methods into the engine's Object query requests.

*This* is what a :ref:`Script <class_Script>` is. Objects check their attached
script before the database, so scripts can even override methods.
If a script defines a `_get_property_list()` method, that data is appended to
the list of properties the Object fetches from the ClassDB. The same holds
true for other declarative code.

This can lead to some users' confusion when they see a script as being
a class unto itself. In reality, the engine just auto-instantiates the
base engine class and then adds the script to that object. This then allows
the Object to defer to the Script's content where the engine logic deems
appropriate.

A problem does present itself though. As the size of Objects increases,
the scripts' necessary size to create them grows much, much larger.
Creating node hierarchies demonstrates this. Each individual Node's logic
could be several hundred lines of code in length.

let's see a simple example of creating a single Node as a child.

.. tabs::
  .. code-tab:: gdscript GDScript

    # main.gd
    extends Node

    var child # define a variable to store a reference to the child

    func _init():
        child = Node.new() # Construct the child.
        child.name = "Child" # Change its name.
        child.script = preload("child.gd") # Give it custom features.
        child.owner = self # Serialize this node if self is saved.
        add_child(child) # Add "Child" as a child of self.

  .. code-tab:: csharp

    // Main.cs
    using System;
    using Godot;

    namespace ExampleProject
    {
        public class Main : Resource
        {
            public Node Child { get; set; }

            public Main()
            {
                Child = new Node(); // Construct the child.
                Child.Name = "Child"; // Change its name.
                Child.Script = (Script)ResourceLoader.Load("child.gd"); // Give it custom features.
                Child.Owner = this; // Serialize this node if this is saved.
                AddChild(Child); // Add "Child" as a child of this.
            }
        }
    }

Notice that only two pieces of declarative code are involved in
the creation of this child node: the variable declaration and
the constructor declaration. Everything else about the child
must be setup using imperative code. However, script code is
much slower than engine C++ code. Each change must make a separate
call to the scripting API which means a lot of C++ "lookups" within
data structures to find the corresponding logic to execute.

To help offload the work, it would be convenient if one could batch up
all operations involved in creating and setting up node hierarchies. The
engine could then handle the construction using its fast C++ code, and the
script code would be free from the perils of imperative code.

*This* is what a scene (:ref:`PackedScene <class_PackedScene>`) is: a
resource that provides an advanced "constructor" serialization which is
offloaded to the engine for batch processing.

Now, why is any of this important to scene organization? Because one must
understand that scenes *are* objects. One often pairs a scene with
a scripted root node that makes use of the sub-nodes. This means that the
scene is often an extension of the script's declarative code.

It helps to define...

- what objects are available to the script?

- how are they organized?

- how are they initialized?

- what connections to each other do they have, if any?

As such, many Object-Oriented principles which apply to "programming", i.e.
scripts, *also* apply to scenes. Some scripts are designed to only work
in one scene (which are often bundled into the scene itself). Other scripts
are meant to be re-used between scenes.

**Regardless, the scene is always an extension of the root script, and can
therefore be interpreted as a part of the class.**
Most of the points covered in this series will build on this point, so
keep it in mind.
