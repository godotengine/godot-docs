Introduction to Godot development
=================================

This page introduces the global organization of Godot Engine's source
code.

Debugging the editor with gdb
-----------------------------

If you are writing or correcting bugs affecting Godot Engine editor,
remember that the binary runs the launcher first, which runs the editor
in another process. Thus, you need to run the editor directly by passing
the ``-e`` argument to Godot Engine editor's binary.
