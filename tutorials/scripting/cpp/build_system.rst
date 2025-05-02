.. _doc_godot_cpp_build_system:

Build System
============

`godot-cpp <https://github.com/godotengine/godot-cpp>`__ uses `SCons <https://scons.org>`__ as its build system.
It is modeled after :ref:`Godot's build system <doc_compiling_index>`, and some commands available there are also
available in godot-cpp projects.

Getting Started
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
individual godot-cpp projects, so consult their individual documentations for more information on those.

Configuring an IDE
------------------

Most IDEs can use a ``compile_commands.json`` file to understand a C++ project. You can generate it in godot-cpp with
the following command:

.. code-block:: shell

   # Generate compile_commands.json while compiling
   scons compiledb=yes

   # Generate compile_commands.json without compiling
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

GDExtensions are expected to run on many different systems. Generally, a single computer is only capable of building
for a few different platforms. For example, Windows users will be able to build for Windows, Android and Web,
but not for macOS or Linux.

To make your GDExtension as widely compatible as possible, we recommend setting up Continuous Integration (CI) to build
your GDExtension on many different platforms. The
`godot-cpp-template <https://github.com/godotengine/godot-cpp-template>`__ contains an example setup for a GitHub based
CI workflow.

CMake
-----

godot-cpp comes with a `CMakeLists.txt <https://github.com/godotengine/godot-cpp/blob/master/CMakeLists.txt>`__ file, to
support users that prefer using `CMake <https://cmake.org>`__ over `SCons <https://scons.org>`__ for their build system.

While actively supported, it is considered secondary to the SCons build system. This means it may lack some features
that are provided for users using SCons. It is documented in godot-cpp's
`cmake.rst <https://github.com/godotengine/godot-cpp/blob/master/doc/cmake.rst>`__ file.
