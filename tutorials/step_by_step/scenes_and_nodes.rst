.. _doc_scenes_and_nodes:

Scenes and nodes
================

Introduction
------------

.. image:: /img/chef.png

Imagine for a second that you are not a game developer anymore. Instead,
You are a chef! Change your hipster outfit for a toque and a double
breasted jacket. Now, instead of making games, you create new and
delicious recipes for your guests.

So, how does a chef create a recipe? Recipes are divided in two
sections, the first is the ingredients and the second is the
instructions to prepare it. This way, anyone can follow the recipe and
savor your magnificent creation.

Making games in Godot feels pretty much the same way. Using the engine
feels like being in a kitchen. In this kitchen, *nodes* are like a
refrigerator full of fresh ingredients to cook with.

There are many types of nodes, some show images, others play sound,
other nodes display 3D models, etc. There's dozens of them.

Nodes
-----

But let's go to the basics. A node is a basic element for creating a
game, it has the following characteristics:

-  Has a name.
-  Has editable properties.
-  Can receive a callback to process every frame.
-  Can be extended (to have more functions).
-  Can be added to other nodes as children.

.. image:: /img/tree.png

The last one is very important. Nodes can have other nodes as
children. When arranged in this way, the nodes become a **tree**.

In Godot, the ability to arrange nodes in this way creates a powerful
tool for organizing the projects. Since different nodes have different
functions, combining them allows to create more complex functions.

This is probably not clear yet and it makes little sense, but everything
will click a few sections ahead. The most important fact to remember for
now is that nodes exist and can be arranged this way.

Scenes
------

.. image:: /img/scene_tree_example.png

Now that the existence of nodes has been defined, the next logical
step is to explain what a Scene is.

A scene is composed of a group of nodes organized hierarchically (in
tree fashion). It has the following properties:

-  A scene always has only one root node.
-  Scenes can be saved to disk and loaded back.
-  Scenes can be *instanced* (more on that later).
-  Running a game means running a scene.
-  There can be several scenes in a project, but for it to start, one of
   them must selected to be loaded first.

Basically, the Godot editor is a **scene editor**. It has plenty of
tools for editing 2D and 3D scenes as well as user interfaces, but all
the editor revolves around the concept of editing a scene and the nodes
that compose it.

Creating a new project
----------------------

Theory is boring, so let's change subject and go practical. Following a
long tradition in tutorials, the first project will be a hello world.
For this, the editor will be used.

When godot executable is run outside a project, the Project Manager
appears. This helps developers manage their projects.

.. image:: /img/project_manager.png

To create a new project, the "New Project" option must be used. Choose
and create a path for the project and specify the project name:

.. image:: /img/create_new_project.png

Editor
------

Once the "New Project" is created, the next step is opening it. This
will open the Godot editor. Here is how the editor looks when freshly
opened:

.. image:: /img/empty_editor.png

As mentioned before, making games in Godot feels like being in a
kitchen, so let's open the refrigerator and add some fresh nodes to the
project. We'll begin with a Hello World! To do this, the "New Node"
button must be pressed:

.. image:: /img/newnode_button.png

This will open the Create Node dialog, showing the long list of nodes
that can be created:

.. image:: /img/node_classes.png

From there, select the "Label" node first. Searching for it is probably
the quickest way:

.. image:: /img/node_search_label.png

And finally, create the Label! A lot happens when Create is pressed:

.. image:: /img/editor_with_label.png

First of all, the scene is changed to the 2D editor (because Label is
a 2D Node type), and the Label appears, selected, at the top left
corner of the viewport.

The node appears in the scene tree editor (box in the top left
corner), and the label properties appear in the Inspector (box on the
right side).

The next step will be to change the "Text" Property of the label, let's
change it to "Hello, World!":

.. image:: /img/hw.png

Ok, everything's ready to run the scene! Press the PLAY SCENE Button on
the top bar (or hit F6):

.. image:: /img/playscene.png

Aaaand... Oops.

.. image:: /img/neversaved.png

Scenes need to be saved to be run, so save the scene to something like
hello.scn in Scene -> Save:

.. image:: /img/save_scene.png

And here's when something funny happens. The file dialog is a special
file dialog, and only allows to save inside the project. The project
root is "res://" which means "resource path. This means that files can
only be saved inside the project. For the future, when doing file
operations in Godot, remember that "res://" is the resource path, and no
matter the platform or install location, it is the way to locate where
resource files are from inside the game.

After saving the scene and pressing run scene again, the "Hello, World!"
demo should finally execute:

.. image:: /img/helloworld.png

Success!

.. _doc_scenes_and_nodes-configuring_the_project:

Configuring the project
-----------------------

Ok, It's time to do some configuration to the project. Right now, the
only way to run something is to execute the current scene. Projects,
however, have several scenes so one of them must be set as the main
scene. This scene is the one that will be loaded at the time the project
is run.

These settings are all stored in the engine.cfg file, which is a
plaintext file in win.ini format, for easy editing. There are dozens of
settings that can be set in that file to alter how a project executes,
so to make matters simpler, a project setting dialog exists, which is
sort of a frontend to editing engine.cfg

To access that dialog, simply go to Scene -> Project Settings.

Once the window opens, the task will be to select a main scene. This can
be done easily by changing the application/main_scene property and
selecting 'hello.scn'.

.. image:: /img/main_scene.png

With this change, pressing the regular Play button (or F5) will run the
project, no matter which scene is being edited.

Going back to the project settings dialog. This dialog provides a lot
of options that can be added to engine.cfg and show their default
values. If the default value is ok, then there isn't any need to
change it.

When a value is changed, a tick is marked to the left of the name.
This means that the property will be saved to the engine.cfg file and
remembered.

As a side note, for future reference and a little out of context (this
is the first tutorial after all!), it is also possible to add custom
configuration options and read them in run-time using the
:ref:`Globals <class_Globals>` singleton.

To be continued...
------------------

This tutorial talks about "scenes and nodes", but so far there has been
only *one* scene and *one* node! Don't worry, the next tutorial will
deal with that...
