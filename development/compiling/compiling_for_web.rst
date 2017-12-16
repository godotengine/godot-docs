.. _doc_compiling_for_web:

Compiling for the Web
=====================

.. highlight:: shell

Requirements
------------

To compile export templates for the Web, the following is required:

-  `Emscripten 1.37.9+ <http://emscripten.org/>`__: If the version available
   per package manager is not recent enough, the best alternative is to install
   using the `Emscripten SDK <http://kripken.github.io/emscripten-site/docs/gettng_started/downloads.html>`__
   (Install in a path without spaces, i.e. not in ``Program Files``)
-  `Python 2.7+ or Python 3.5+ <https://www.python.org/>`__
-  `SCons <http://www.scons.org>`__ build system

Building export templates
-------------------------

Start a terminal and set the environment variable ``EMSCRIPTEN_ROOT`` to the
installation directory of Emscripten:

If you installed Emscripten via the Emscripten SDK, declare the variable with a
path to the downloaded folder::

    export EMSCRIPTEN_ROOT=~/emsdk/emscripten/master

If you installed Emscripten via package manager, the path can be retrieved with
the ``em-config`` command::

    export EMSCRIPTEN_ROOT=`em-config EMSCRIPTEN_ROOT`

On Windows you can set the environment variable in the system settings or in
the command prompt::

    set EMSCRIPTEN_ROOT="C:\emsdk\emscripten\master"

Now go to the root directory of the engine source code and instruct SCons to
build the JavaScript platform. Specify ``target`` as either ``release`` for a
release build or ``release_debug`` for a debug build::

    scons platform=javascript tools=no target=release
    scons platform=javascript tools=no target=release_debug

The engine will now be compiled to WebAssembly by Emscripten. If all goes well,
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

The other method uses LLVM's WebAssembly backend. This backend is not yet
available in release versions of LLVM, only in development builds built with
``LLVM_EXPERIMENTAL_TARGETS_TO_BUILD=WebAssembly``.
Compiling with this backend outputs files in LLVM's ``.s`` format, which is
translated into actual WebAssembly using a tool called ``s2wasm``.
Emscripten manages these processes as well, so we just invoke SCons.

In order to choose one of the two methods, the ``LLVM_ROOT`` variable in the
Emscripten configuration file ``~/.emscripten`` is set. If it points to a
directory containing binaries of Emscripten's *fastcomp* fork of clang,
``asm2wasm`` is used. This is the default in a normal Emscripten installation.
Otherwise, LLVM binaries built with the WebAssembly backend will be expected
and ``s2wasm`` is used. On Windows, make sure to escape backslashes of paths
within this file as double backslashes ``\\`` or use Unix-style paths with
a single forward slash ``/``.
