.. _doc_introduction_to_godot_development:

Introduction to Godot development
=================================

This page is meant to introduce the global organization of Godot Engine's
source code, and give useful tips for extending/fixing the engine on the
C++ side.

Architecture diagram
--------------------

The following diagram describes the architecture used by Godot, from the
core components down to the abstracted drivers, via the scene
structure and the servers.

.. image:: /img/architecture_diagram.jpg

Debugging the editor with gdb
-----------------------------

If you are writing or correcting bugs affecting Godot Engine's editor,
remember that the binary will by default run the project manager first,
and then only run the editor in another process once you've selected a
project. To launch a project directly, you need to run the editor by
passing the ``-e`` argument to Godot Engine's binary from within your
project's folder. Typically:

.. code:: bash

    $ cd ~/myproject
    $ gdb godot
    > run -e

Or:

.. code:: bash

    $ gdb godot
    > run -e ~/myproject/project.godot

(With the path pointing to the project.godot or pointing to a specific scene to open the editor at.)

Windows example:

.. code:: bash

    $ gdb godot.windows.tools.64.exe
    > run -e C:/path/to/project/project.godot

(Backslashes work as well.)

Running tests
-----------------------------

Example:
Running the ``string`` tests defined in ``/main/tests/test_string.cpp``:

.. code:: bash

    > godot --test string

Note that Godot has to be built with tools enabled for this (``tools=yes``, which is the default).

Also see the output of ``godot --help``.
