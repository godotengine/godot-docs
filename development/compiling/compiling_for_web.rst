.. _doc_compiling_for_web:

Compiling for the Web
=====================

.. highlight:: shell

Requirements
------------

To compile export templates for the Web, the following is required:

-  `Emscripten <http://emscripten.org/>`__: The easiest way to install it, if it's not up to date in your Linux package manager, is to use the `Emscripten SDK <http://emscripten.org/>`__ (Install in a path without spaces, i.e. not in "Program Files")
-  `Python 2.7+ or Python 3.5+ <https://www.python.org/>`__
-  `SCons <http://www.scons.org>`__ build system

Building export templates
-------------------------

Start a terminal and set the environment variable ``EMSCRIPTEN_ROOT`` to the
installation directory of Emscripten:

-  If you installed Emscripten via the Emscripten SDK, you will declare the variable with a path to your downloaded folder::

    export EMSCRIPTEN_ROOT=~/emsdk/emscripten/master

-  If you installed Emscripten via your package manager, you can know the path with the ``em-config`` command::

    em-config EMSCRIPTEN_ROOT

   So you will declare the variable as for example::

    export EMSCRIPTEN_ROOT=/usr/lib/emscripten

The Emscripten variables are defined in the ``~/.emscripten`` file, so this is an alternative way to check. Erase this file if you want to reinstall Emscripten with a fresh new method.

If you are on Windows and used Emscripten SDK, start a regular prompt or the Emscripten Command Prompt.
Do **not** use the Developer Command Prompt nor any of the ones that come with
Visual Studio. You can set the environment variable in the system settings or
in the prompt itself::

    set EMSCRIPTEN_ROOT=C:\emsdk\emscripten\master

Now go to the root directory of the engine source code and instruct SCons to
compile for JavaScript. Specify ``target`` as either ``release`` for a release
build or ``release_debug`` for a debug build::

    scons platform=javascript tools=no target=release
    scons platform=javascript tools=no target=release_debug

The engine will now be compiled to JavaScript by Emscripten. If all goes well,
the resulting file will be placed in the ``bin`` subdirectory. Its name is
``godot.javascript.opt.zip`` for release or ``godot.javascript.opt.debug.zip``
for debug.

If it's not, check if you have properly installed everything, and if EMSCRIPTEN_ROOT path is correctly defined, including in the ``~/.emscripten`` file.

Finally, rename the zip archive to ``javascript_release.zip`` for the
release template::

    mv bin/godot.javascript.opt.zip bin/javascript_release.zip

And ``javascript_debug.zip`` for the debug template::

    mv bin/godot.javascript.opt.debug.zip bin/javascript_debug.zip

Compiling to WebAssembly
-------------------------

The current default for exporting to the web is to compile to *asm.js*, a
highly optimizable subset of JavaScript.

It is also possible to compile to the *WebAssembly* format, which offers better
performance and loading times. Running a game in this format requires a browser
with WebAssembly support.

Compiling to WebAssembly requires using the latest version of Emscripten.
If your OS does not offer up-to-date packages for Emscripten, the easiest way
is usually to install using Emscripten's `emsdk <http://kripken.github.io/emscripten-site/docs/getting_started/downloads.html>`_.

WebAssembly can be compiled in two ways: The default way is to first
compile to asm.js similarly to the default method, then translate to
WebAssembly using a tool called ``asm2wasm``. Emscripten automatically takes
care of both processes, we simply run SCons.

The other method uses LLVM's WebAssembly backend. This backend is not yet
available in release versions of LLVM, only in development builds.
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

With ``LLVM_ROOT`` set up correctly, compiling to WebAssembly is as easy as
adding ``wasm=yes`` to the SCons arguments::

    scons platform=javascript target=release wasm=yes
    scons platform=javascript target=release_debug wasm=yes

These commands will build WebAssembly export templates in either release or
debug mode. The generated files' names contain ``.webassembly`` as an
additional file suffix before the extension.

If it's not compiling, check if you have properly installed everything, and if ``LLVM_ROOT`` and ``BINARYEN_ROOT`` variables are defined in the ``~/.emscripten`` file. You can define the ``BINARYEN_ROOT`` path manually in this file if you already installed Binaryen an other way and want to avoid SCons to compile it from ports during template compilation. Emscripten SDK comes with its own fork of LLVM called fastcomp, which has the JSBackend needed for asm.js and asm2wasm, so the ``LLVM_ROOT`` path must lead to an ``/emscripten-fastcomp`` directory.

Finally, the WebAssembly templates are renamed to ``webassembly_release.zip``
and ``webassembly_debug.zip``::

    mv bin/godot.javascript.opt.webassembly.zip       bin/webassembly_release.zip
    mv bin/godot.javascript.opt.debug.webassembly.zip bin/webassembly_debug.zip

Customizing the HTML page
-------------------------

Rather than the default HTML file generated when compiling, it is
also possible to use a custom HTML page. This allows drastic customization of
the final web presentation.

This can be done in two ways. The first is to replace the
``platform/javascript/godot_shell.html`` file. In this case, the HTML file is
used at build time, allowing Emscripten to substitute the ``{{{ SCRIPT }}}``
placeholder by a ``<script>`` element containing the loader code. This makes
the HTML file usable for both asm.js and WebAssembly templates, since they use
different loading code.

The other method is to simply replace the ``godot.html`` file within the
complete export templates. This method does not require building the engine.
However, in this case, no ``{{{ SCRIPT }}}`` placeholder should be used in the
HTML file, since it would never be replaced — the loader code for either asm.js
or WebAssembly must already be included in the file.

In the HTML page, the JavaScript object ``Module`` is the page's interface to
Emscripten. Check the official documentation for information on how to use it:
https://kripken.github.io/emscripten-site/docs/api_reference/module.html

The default HTML page offers an example to start off with, separating the
Emscripten interface logic in the JavaScript ``Module`` object from the page
logic in the ``Presentation`` object. Emscripten's default ``shell.html`` file
is another example, but does not use Godot's placeholders, listed below.

When exporting a game, several placeholders in the ``godot.html`` file are
substituted by values dependent on the export:

+------------------------------+-----------------------------------------------+
| Placeholder                  | substituted by                                |
+==============================+===============================================+
| ``$GODOT_BASE``              | Basename of files referenced within the page, |
|                              | without suffixes                              |
+------------------------------+-----------------------------------------------+
| ``$GODOT_DEBUG_ENABLED``     | ``true`` if debugging, ``false`` otherwise    |
+------------------------------+-----------------------------------------------+
| ``$GODOT_HEAD_INCLUDE``      | Custom string to include just before the end  |
|                              | of the HTML ``<head>`` element                |
+------------------------------+-----------------------------------------------+
| ``{{{ SCRIPT }}}``           | ``<script>`` that loads the engine,           |
|                              | substituted only when building, not on export |
+------------------------------+-----------------------------------------------+

The first three of the placeholders listed should always be implemented in the
HTML page, since they are important for the correct presentation of the game.
The last placeholder is important when rewriting the ``godot_shell.html`` file
and is substituted during build time rather than export.
