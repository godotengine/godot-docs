.. _doc_compiling_for_web:

Compiling for the Web
=====================

.. seealso::

    This page describes how to compile HTML5 editor and export template binaries from source.
    If you're looking to export your project to HTML5 instead, read :ref:`doc_exporting_for_web`.

.. highlight:: shell

Requirements
------------

To compile export templates for the Web, the following is required:

-  `Emscripten 1.39.9+ <https://emscripten.org>`__.
-  `Python 3.5+ <https://www.python.org/>`__.
-  `SCons 3.0+ <https://www.scons.org>`__ build system.

.. seealso:: To get the Godot source code for compiling, see
             :ref:`doc_getting_source`.

             For a general overview of SCons usage for Godot, see
             :ref:`doc_introduction_to_the_buildsystem`.

Building export templates
-------------------------

Before starting, confirm that ``emcc`` is available in your PATH. This is
usually configured by the Emscripten SDK, e.g. when invoking ``emsdk activate``
and ``source ./emsdk_env.sh``/``emsdk_env.bat``.

Open a terminal and navigate to the root directory of the engine source code.
Then instruct SCons to build the Web platform. Specify ``target`` as
either ``release`` for a release build or ``release_debug`` for a debug build::

    scons platform=web tools=no target=release
    scons platform=web tools=no target=release_debug

By default, the :ref:`JavaScript singleton <doc_javascript_eval>` will be built
into the engine. Official export templates also have the JavaScript singleton
enabled. Since ``eval()`` calls can be a security concern, the
``javascript_eval`` option can be used to build without the singleton::

    scons platform=web tools=no target=release javascript_eval=no
    scons platform=web tools=no target=release_debug javascript_eval=no

The engine will now be compiled to WebAssembly by Emscripten. Once finished,
the resulting file will be placed in the ``bin`` subdirectory. Its name is
``godot.web.opt.wasm32.zip`` for release or ``godot.web.opt.debug.wasm32.zip``
for debug.

Finally, rename the zip archive to ``web_release.zip`` for the
release template::

    mv bin/godot.web.opt.wasm32.zip bin/web_release.zip

And ``web_debug.zip`` for the debug template::

    mv bin/godot.web.opt.debug.wasm32.zip bin/web_debug.zip

GDExtension
-----------

The default export templates do not include GDExtension support for
performance and compatibility reasons. See the
:ref:`export page <doc_javascript_export_options>` for more info.

You can build the export templates using the option ``dlink_enabled=yes``
to enable GDExtension support::

    scons platform=web tools=no dlink_enabled=yes target=release
    scons platform=web tools=no dlink_enabled=yes target=release_debug

Once finished, the resulting file will be placed in the ``bin`` subdirectory.
Its name will have ``_dlink`` added.

Finally, rename the zip archives to ``web_dlink_release.zip`` and
``web_dlink_release.zip`` for the release template::

    mv bin/godot.web.opt.wasm32.dlink.zip bin/web_dlink_release.zip
    mv bin/godot.web.opt.debug.wasm32.dlink.zip bin/web_dlink_debug.zip

Building the editor
-------------------

It is also possible to build a version of the Godot editor that can run in the
browser. The editor version is not recommended
over the native build. You can build the editor with::

    scons platform=web tools=yes target=release_debug

Once finished, the resulting file will be placed in the ``bin`` subdirectory.
Its name will be ``godot.web.opt.tools.wasm32.zip``. You can upload the
zip content to your web server and visit it with your browser to use the editor.

Refer to the :ref:`export page <doc_javascript_export_options>` for the web
server requirements.
