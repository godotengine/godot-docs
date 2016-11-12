.. _doc_compiling_for_web:

Compiling for the Web
========================

.. highlight:: shell

Requirements
------------

To compile export templates for the Web, the following is required:

-  `Emscripten SDK <http://emscripten.org/>`__ (Install in a path without
   spaces, i.e. not on "Program Files")
-  `Python 2.7+ <https://www.python.org/>`__ (3.0 is
   untested as of now)
-  `SCons <http://www.scons.org>`__ build system

Compiling
---------

Start a terminal and set the environment variable ``EMSCRIPTEN_ROOT`` to the
installation directory of Emscripten::

    export EMSCRIPTEN_ROOT=~/emsdk/emscripten/master

If you are on Windows, start a regular prompt or the Emscripten Command Prompt.
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
``godot.javascript.opt.js`` for release or ``godot.javascript.opt.debug.js``
for debug. Additionally, a file of the same name but with the extension
``.html.mem`` will be generated.

Building export templates
-------------------------

After compiling, further steps are required to build the template.
The actual web export template has the form of a zip file containing at least
these 4 files:

1. ``godot.js`` — This is the file that was just compiled, but under a different
   name.

   For the release template::

       cp bin/godot.javascript.opt.js godot.js

   For the debug template::

       cp bin/godot.javascript.opt.debug.js godot.js

2. ``godot.mem`` — Also created during compilation, this file initially has the
   same name as the JavaScript file, except ``.js`` is replaced by
   ``.html.mem``.

   For the release template::

       cp bin/godot.javascript.opt.html.mem godot.mem

   For the debug template::

       cp bin/godot.javascript.opt.debug.html.mem godot.mem

3. ``godot.html`` — Another file created during compilation. This file has a
   ``.html`` extension.

   For the release template::

       cp bin/godot.javascript.opt.html godot.html

   For the debug template::

       cp bin/godot.javascript.opt.debug.html godot.html

4. ``godotfs.js`` — This file is located within the Godot Engine repository,
   under ``/tools/dist/html_fs/``.

::

    cp tools/dist/html_fs/godotfs.js .

Once these 4 files are assembled, zip them up and your export template is ready
to go. The correct name for the template file is ``javascript_release.zip`` for
the release template::

    zip javascript_release.zip godot.js godot.mem godotfs.js godot.html

And ``javascript_debug.zip`` for the debug template::

    zip javascript_debug.zip godot.js godot.mem godotfs.js godot.html

The resulting files must be placed in the ``templates`` directory in your Godot
user directory::

    mv javascript_release.zip ~/.godot/templates
    mv javascript_debug.zip ~/.godot/templates

If you are writing custom modules or using custom C++ code, you may want to
configure your zip files as custom export templates. This can be done in the
export GUI, using the "Custom Package" option.
There's no need to copy the templates in this case — you can simply reference
the resulting files in your Godot source folder, so the next time you build,
the custom templates will already be referenced.

Compiling to WebAssembly
-------------------------

The current default for exporting to the web is to compile to *asm.js*, a
highly optimizable subset of JavaScript.

It is also possible to compile to the experimental *WebAssembly* format, which
should eventually offer better performance and loading times. Its specification
is still in flux and compile tools may sporadically fail to build Godot.
Running a game per WebAssembly requires nightly browser builds with special
flags set. As such, WebAssembly builds are currently not suitable for
publishing.

Compiling to WebAssembly requires using the `incoming branch of Emscripten <http://kripken.github.io/emscripten-site/docs/building_from_source/building_emscripten_from_source_using_the_sdk.html#building-emscripten-from-the-main-repositories>`_.

WebAssembly can be compiled in two ways: The default way is to first
compile to asm.js similarly to the default method, then translate to
WebAssembly using a tool called ``asm2wasm``. Emscripten automatically takes
care of both processes, we simply run SCons.

The other method uses LLVM's WebAssembly backend, which should eventually
produce more performant binaries. To build LLVM with this backend, set the
CMake variable ``LLVM_EXPERIMENTAL_TARGETS_TO_BUILD`` to ``WebAssembly`` when
building LLVM.

Compiling with this backend outputs files in LLVM's ``.s`` format, which is
translated to actual WebAssembly using a tool called ``s2wasm``. Emscripten
manages these processes as well, so we just invoke SCons.

In order to choose one of the two methods, the ``LLVM_ROOT`` variable in the
Emscripten configuration file ``~/.emscripten`` is set. If it points to a
directory containing binaries of Emscripten's *fastcomp* fork of clang,
``asm2wasm`` is used. This is the default in a normal Emscripten installation.
Otherwise, LLVM binaries built with the WebAssembly backend will be expected
and ``s2wasm`` is used.

With ``LLVM_ROOT`` set up correctly, compiling to WebAssembly is as easy as
adding ``wasm=yes`` to the SCons arguments::

    scons platform=javascript target=release wasm=yes
    scons platform=javascript target=release_debug wasm=yes

These commands will build WebAssembly binaries in either release or debug mode.
The generated files' names contain ``.webassembly`` as an additional file
suffix before the extension.

In order to build the actual WebAssembly export templates, the WebAssembly
binary file with the ``.wasm`` extension must be added alongside the usual
files to the archive as ``godot.wasm``.

For the release template::

   cp bin/godot.javascript.opt.webassembly.wasm godot.wasm

For the debug template::

   cp bin/godot.javascript.opt.debug.webassembly.wasm godot.wasm

WebAssembly builds do not use a memory initializer file, so do not add a
``godot.mem`` file to the archive — there is none.

The WebAssembly export templates simply replace the previous asm.js-based web
export templates with the names ``javascript_release.zip`` and
``javascript_debug.zip``

Customizing the HTML page
-------------------------

Rather than the default ``godot.html`` file generated when compiling, it is
also possible to use a custom HTML page. This allows drastic customization of
the final web presentation.

The JavaScript object ``Module`` is the page's interface to Emscripten. Check
the official documentation for information on how to use it: https://kripken.github.io/emscripten-site/docs/api_reference/module.html

The default HTML page offers a good example to start off with, separating the
Emscripten interface logic in the JavaScript ``Module`` object from the page
logic in the ``Presentation`` object.

When exporting a game, several placeholders in the ``godot.html`` file are
substituted by values dependent on the export:

+------------------------------+-----------------------------------------------+
| Placeholder                  | substituted by                                |
+==============================+===============================================+
| ``{{{ SCRIPT }}}``           | ``<script>`` element responsible for loading  |
|                              | the engine, generated by Emscripten           |
+------------------------------+-----------------------------------------------+
| ``$GODOT_BASE``              | Basename of files referenced within the page, |
|                              | without file extension or other suffixes      |
+------------------------------+-----------------------------------------------+
| ``$GODOT_CANVAS_WIDTH``      | Integer specifying the initial display width  |
|                              | of the game                                   |
+------------------------------+-----------------------------------------------+
| ``$GODOT_CANVAS_HEIGHT``     | Integer specifying the initial display height |
|                              | of the game                                   |
+------------------------------+-----------------------------------------------+
| ``$GODOT_DEBUG_ENABLED``     | String ``true`` if debugging, ``false``       |
|                              | otherwise                                     |
+------------------------------+-----------------------------------------------+
| ``$GODOT_CONTROLS_ENABLED``  | String ``true`` if ``html/controls_enabled``  |
|                              | is enabled, ``false`` otherwise               |
+------------------------------+-----------------------------------------------+
| ``$GODOT_HEAD_TITLE``        | Title of the page, normally used as content   |
|                              | of the HTML ``<title>`` element               |
+------------------------------+-----------------------------------------------+
| ``$GODOT_HEAD_INCLUDE``      | Custom string to include just before the end  |
|                              | of the HTML ``<head>`` element                |
+------------------------------+-----------------------------------------------+
| ``$GODOT_STYLE_FONT_FAMILY`` | CSS format ``font-family`` to use, without    |
|                              | terminating semicolon                         |
+------------------------------+-----------------------------------------------+
| ``$GODOT_STYLE_INCLUDE``     | Custom string to include just before the end  |
|                              | of the page's CSS style sheet                 |
+------------------------------+-----------------------------------------------+

The first four of the placeholders listed should always be implemented in the
HTML page, since they are important for the correct presentation of the game.
The other placeholders are optional.

Finally, the custom HTML page is installed by replacing the existing
``godot.html`` file in the export template with the new one, retaining the name
of the original.
