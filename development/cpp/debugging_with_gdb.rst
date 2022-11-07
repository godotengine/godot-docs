.. _doc_debugging_with_gdb:

Debugging with gdb
==================

Debugging the Godot editor
----------------------

If you are writing or correcting bugs affecting Godot Engine's editor,
remember that the binary will by default run the project manager first,
and then only run the editor in another process once you've selected a
project. To launch a project directly, you need to run the editor by
passing the ``-e`` argument to Godot Engine's binary from within your
project's folder. Typically:

.. code-block:: none

    $ cd ~/myproject
    $ gdb godot
    > run -e

Or:

.. code-block:: none

    $ gdb godot
    > run -e --path ~/myproject
