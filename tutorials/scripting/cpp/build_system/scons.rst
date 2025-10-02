.. _doc_godot_cpp_build_system:

Main build system: Working with SCons
=====================================

.. seealso:: This page documents how to compile godot-cpp. If you're looking to compile Godot instead, see
             :ref:`doc_introduction_to_the_buildsystem`.

`godot-cpp <https://github.com/godotengine/godot-cpp>`__ uses `SCons <https://scons.org>`__ as its main build system.
It is modeled after :ref:`Godot's build system <doc_compiling_index>`, and some commands available there are also
available in godot-cpp projects.

Getting started
---------------

To build a godot-cpp project, it is generally sufficient to install `SCons <https://scons.org>`__, and simply run it
in the project directory:

    scons

You may want to learn about available options:

    scons --help

To cleanly re-build your project, add ``--clean`` to your build command:

    scons --clean

You can find more information about common SCons arguments and build patterns in the
`SCons User Guide <https://scons.org/doc/latest/HTML/scons-user/index.html>`__. Additional commands may be added by
individual godot-cpp projects, so consult their specific documentation for more information on those.

Configuring an IDE
------------------

Most IDEs can use a ``compile_commands.json`` file to understand a C++ project. You can generate it with godot-cpp using
the following command:

.. code-block:: shell

   # Generate compile_commands.json while compiling.
   scons compiledb=yes

   # Generate compile_commands.json without compiling.
   scons compiledb=yes compile_commands.json

For more information, please check out the :ref:`IDE configuration guides <doc_configuring_an_ide>`.
Although written for Godot engine contributors, they are largely applicable to godot-cpp projects as well.

Loading your GDExtension in Godot
---------------------------------

Godot loads GDExtensions by finding :ref:`.gdextension <doc_gdextension_file>` files in the project directory.
``.gdextension`` files are used to select and load a binary compatible with the current computer / operating system.

The `godot-cpp-template <https://github.com/godotengine/godot-cpp-template>`__, as well as the
:ref:`Getting Started section <doc_godot_cpp_getting_started>`, provide example ``.gdextension`` files for GDExtensions
that are widely compatible to many different systems.

Building for multiple platforms
-------------------------------

GDExtensions are expected to run on many different systems, each with separate binaries and build configurations.
If you are planning to publish your GDExtension, we recommend you provide binaries for all configurations that are
mentioned in the `godot-cpp-template <https://github.com/godotengine/godot-cpp-template>`__
`.gdextension file <https://github.com/godotengine/godot-cpp-template/blob/main/demo/bin/example.gdextension>`__.

There are two popular ways by which cross platform builds can be achieved:

- Cross-platform build tools
- Continuous Integration (CI)

`godot-cpp-template <https://github.com/godotengine/godot-cpp-template>`__ contains an
`example setup <https://github.com/godotengine/godot-cpp-template/tree/main/.github/workflows>`__
for a GitHub based CI workflow.
