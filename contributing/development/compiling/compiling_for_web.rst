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

- `Emscripten 3.1.39+ <https://emscripten.org>`__.
- `Python 3.6+ <https://www.python.org/>`__.
- `SCons 3.0+ <https://scons.org/pages/download.html>`__ build system.

.. seealso:: To get the Godot source code for compiling, see
             :ref:`doc_getting_source`.

             For a general overview of SCons usage for Godot, see
             :ref:`doc_introduction_to_the_buildsystem`.

.. note:: Emscripten 3.1.39+ is recommended, but older 3.x versions are known to work.

          Please note that the minimum requirement for GDExtension support is 3.1.14.

Building export templates
-------------------------

Before starting, confirm that ``emcc`` is available in your PATH. This is
usually configured by the Emscripten SDK, e.g. when invoking ``emsdk activate``
and ``source ./emsdk_env.sh``/``emsdk_env.bat``.

Open a terminal and navigate to the root directory of the engine source code.
Then instruct SCons to build the Web platform. Specify ``target`` as
either ``template_release`` for a release build or ``template_debug`` for a debug build::

    scons platform=web target=template_release
    scons platform=web target=template_debug

By default, the :ref:`JavaScriptBridge singleton <doc_web_javascript_bridge>` will be built
into the engine. Official export templates also have the JavaScript singleton
enabled. Since ``eval()`` calls can be a security concern, the
``javascript_eval`` option can be used to build without the singleton::

    scons platform=web target=template_release javascript_eval=no
    scons platform=web target=template_debug javascript_eval=no

The engine will now be compiled to WebAssembly by Emscripten. Once finished,
the resulting file will be placed in the ``bin`` subdirectory. Its name is
``godot.web.template_release.wasm32.zip`` for release or ``godot.web.template_debug.wasm32.zip``
for debug.

Finally, rename the zip archive to ``web_release.zip`` for the
release template::

    mv bin/godot.web.template_release.wasm32.zip bin/web_release.zip

And ``web_debug.zip`` for the debug template::

    mv bin/godot.web.template_debug.wasm32.zip bin/web_debug.zip

GDExtension
-----------

The default export templates do not include GDExtension support for
performance and compatibility reasons. See the
:ref:`export page <doc_javascript_export_options>` for more info.

You can build the export templates using the option ``dlink_enabled=yes``
to enable GDExtension support::

    scons platform=web dlink_enabled=yes target=template_release
    scons platform=web dlink_enabled=yes target=template_debug

Once finished, the resulting file will be placed in the ``bin`` subdirectory.
Its name will have ``_dlink`` added.

Finally, rename the zip archives to ``web_dlink_release.zip`` and
``web_dlink_release.zip`` for the release template::

    mv bin/godot.web.template_release.wasm32.dlink.zip bin/web_dlink_release.zip
    mv bin/godot.web.template_debug.wasm32.dlink.zip bin/web_dlink_debug.zip

Building the editor
-------------------

It is also possible to build a version of the Godot editor that can run in the
browser. The editor version is not recommended
over the native build. You can build the editor with::

    scons platform=web target=editor

Once finished, the resulting file will be placed in the ``bin`` subdirectory.
Its name will be ``godot.web.editor.wasm32.zip``. You can upload the
zip content to your web server and visit it with your browser to use the editor.

Refer to the :ref:`export page <doc_javascript_export_options>` for the web
server requirements.

.. tip::

    The Godot repository includes a
    `Python script to host a local web server <https://raw.githubusercontent.com/godotengine/godot/master/platform/web/serve.py>`__.
    This can be used to test the web editor locally.

    After compiling the editor, extract the ZIP archive that was created in the
    ``bin/`` folder, then run the following command in the Godot repository
    root:

    ::

        # You may need to replace `python` with `python3` on some platforms.
        python platform/web/serve.py

    This will serve the contents of the ``bin/`` folder and open the default web
    browser automatically. In the page that opens, access ``godot.tools.html``
    and you should be able to test the web editor this way.

    Note that for production use cases, this Python-based web server should not
    be used. Instead, you should use an established web server such as Apache or
    nginx.
