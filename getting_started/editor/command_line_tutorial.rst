.. _doc_command_line_tutorial:

Command line tutorial
=====================

.. highlight:: shell

Some developers like using the command line extensively. Godot is
designed to be friendly to them, so here are the steps for working
entirely from the command line. Given the engine relies on little to no
external libraries, initialization times are pretty fast, making it
suitable for this workflow.

Path
----

It is recommended that your Godot binary is in your PATH environment
variable, so it can be executed easily from any place by typing
``godot``. You can do so on Linux by placing the Godot binary in
``/usr/local/bin`` and making sure it is called ``godot``.

Setting the project path
------------------------

Depending on where your Godot binary is located and what your current
working directory is, you may need to set the path to your project
for any of the following commands to work correctly.

This can be done by giving the path to the ``project.godot`` file
of your project as either the first argument, like this:

::

    user@host:~$ godot path_to_your_project/project.godot [other] [commands] [and] [args]

Or by using the ``--path`` argument:

::

    user@host:~$ godot --path path_to_your_project [other] [commands] [and] [args]

For example, the full command for exporting your game (as explained below) might look like this:

::

    user@host:~$ godot --path path_to_your_project --export my_export_preset_name game.exe

Creating a project
------------------


Creating a project from the command line can be done by navigating the
shell to the desired place and making a project.godot file.


::

    user@host:~$ mkdir newgame
    user@host:~$ cd newgame
    user@host:~/newgame$ touch project.godot


The project can now be opened with Godot.


Running the editor
------------------

Running the editor is done by executing godot with the ``-e`` flag. This
must be done from within the project directory or a subdirectory,
otherwise the command is ignored and the project manager appears.

::

    user@host:~/newgame$ godot -e

If a scene has been created and saved, it can be edited later by running
the same code with that scene as argument.

::

    user@host:~/newgame$ godot -e scene.tscn

Erasing a scene
---------------

Godot is friends with your filesystem and will not create extra
metadata files. Use ``rm`` to erase a scene file. Make sure nothing
references that scene or else an error will be thrown upon opening.

::

    user@host:~/newgame$ rm scene.tscn

Running the game
----------------

To run the game, simply execute Godot within the project directory or
subdirectory.

::

    user@host:~/newgame$ godot

When a specific scene needs to be tested, pass that scene to the command
line.

::

    user@host:~/newgame$ godot scene.tscn

Debugging
---------

Catching errors in the command line can be a difficult task because they
just fly by. For this, a command line debugger is provided by adding
``-d``. It works for both running the game or a simple scene.

::

    user@host:~/newgame$ godot -d

::

    user@host:~/newgame$ godot -d scene.tscn

Exporting
---------

Exporting the project from the command line is also supported. This is
especially useful for continuous integration setups. The version of Godot
that is headless (server build, no video) is ideal for this.

::

    user@host:~/newgame$ godot --export "Linux X11" /var/builds/project
    user@host:~/newgame$ godot --export Android /var/builds/project.apk

The platform names recognized by the ``--export`` switch are the same as
displayed in the export wizard of the editor. To get a list of supported
platforms from the command line, try exporting to a non-recognized
platform and the full listing of platforms your configuration supports
will be shown.

To export a debug version of the game, use the ``--export-debug`` switch
instead of ``--export``. Their parameters and usage are the same.

Running a script
----------------

It is possible to run a simple .gd script from the command line. This
feature is especially useful in large projects, for batch
conversion of assets or custom import/export.

The script must inherit from SceneTree or MainLoop.

Here is a simple example of how it works:

.. code:: python

    #sayhello.gd
    extends SceneTree

    func _init():
        print("Hello!")
        quit()

And how to run it:

::

    user@host:~/newgame$ godot -s sayhello.gd
    Hello!

If no project.godot exists at the path, current path is assumed to be the
current working directory (unless ``-path`` is specified).
