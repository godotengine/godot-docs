.. _doc_compiling_for_web:

Compiling for the Web
=====================

.. highlight:: shell

Requirements
------------

To compile export templates for the Web, the following is required:

-  `Emscripten 1.39.0+ <https://emscripten.org>`__.
-  `Python 3.5+ <https://www.python.org/>`__.
-  `SCons 3.0+ <https://www.scons.org>`__ build system.

.. seealso:: For a general overview of SCons usage for Godot, see
             :ref:`doc_introduction_to_the_buildsystem`.

Building export templates
-------------------------

Before starting, confirm that the Emscripten configuration file exists and
specifies all settings correctly. This file is available as ``~/.emscripten``
on UNIX-like systems and ``%USERPROFILE%\.emscripten`` on Windows. It's usually
written by the Emscripten SDK, e.g. when invoking ``emsdk activate latest``,
or by your package manager. It's also created when starting Emscripten's
``emcc`` program if the file doesn't exist.

.. attention:: On Windows, make sure to escape backslashes of paths within the Emscripten
               configuration file as double backslashes ``\\`` or use Unix-style paths with a
               single forward slash ``/``.

Open a terminal and navigate to the root directory of the engine source code.
Then instruct SCons to build the JavaScript platform. Specify ``target`` as
either ``release`` for a release build or ``release_debug`` for a debug build::

    scons platform=javascript tools=no target=release
    scons platform=javascript tools=no target=release_debug

By default, the :ref:`JavaScript singleton <doc_javascript_eval>` will be built
into the engine. Since ``eval()`` calls can be a security concern, the
``javascript_eval`` option can be used to build without the singleton::

    scons platform=javascript tools=no target=release javascript_eval=no
    scons platform=javascript tools=no target=release_debug javascript_eval=no

The engine will now be compiled to WebAssembly by Emscripten. Once finished,
the resulting file will be placed in the ``bin`` subdirectory. Its name is
``godot.javascript.opt.zip`` for release or ``godot.javascript.opt.debug.zip``
for debug.

Finally, rename the zip archive to ``webassembly_release.zip`` for the
release template::

    mv bin/godot.javascript.opt.zip bin/webassembly_release.zip

And ``webassembly_debug.zip`` for the debug template::

    mv bin/godot.javascript.opt.debug.zip bin/webassembly_debug.zip

Building per asm.js translation or LLVM backend
-----------------------------------------------

WebAssembly can be compiled in two ways: The default is to first compile to
asm.js, a highly optimizable subset of JavaScript, using Emscripten's
*fastcomp* fork of LLVM. This code is then translated to WebAssembly using a
tool called ``asm2wasm``. Emscripten automatically takes care of both
processes, we simply run SCons.

The other method uses LLVM's WebAssembly backend. This backend is available
starting with LLVM 8 or in development builds.
Emscripten manages this process as well, so we just invoke SCons.

In order to choose one of the two methods, the ``LLVM_ROOT`` variable in the
Emscripten configuration file is used. If it points to a directory containing
binaries of Emscripten's *fastcomp* fork of clang, ``asm2wasm`` is used.
This is the default in a normal Emscripten installation. Otherwise,
LLVM binaries built with the WebAssembly backend will be expected and
the LLVM's WebAssembly backend is used.
