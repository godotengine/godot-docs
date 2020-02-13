.. _doc_customizing_html5_shell:

Customizing the Web export HTML page
====================================

Rather than the default HTML page that comes with the export templates, it is
also possible to use a custom HTML page. This allows drastic customization of
the final web presentation and behavior. The path to the custom HTML page is
specified in the export options as ``Html/Custom Html Shell``.

The default HTML page is available in the Godot Engine repository at
`/misc/dist/html/full-size.html <https://github.com/godotengine/godot/blob/master/misc/dist/html/full-size.html>`__.
Some simple use-cases where customizing the default page is useful include:

 - Loading files from a different directory
 - Loading a ``.zip`` file instead of a ``.pck`` file as main pack
 - Loading engine files from a different directory than the main pack file
 - Adding a click-to-play button so games can be started in full-screen mode
 - Loading some extra files before the engine starts, so they are available in
   the file system later
 - Passing custom "command line" arguments, e.g. ``-s`` to start a MainLoop script

Another sample HTML page is available at `/misc/dist/html/fixed-size.html <https://github.com/godotengine/godot/blob/master/misc/dist/html/fixed-size.html>`__.
This page uses a fixed size canvas with an output widget below. However, the
F12 browser console should be preferred as it can display additional
information, such as WebGL errors.

Placeholder substitution
------------------------

When exporting the game, several placeholders in the HTML page are replaced
with values depending on the export:

+------------------------------+-----------------------------------------------+
| Placeholder                  | Substituted by                                |
+==============================+===============================================+
| ``$GODOT_BASENAME``          | Basename of exported files without suffixes,  |
|                              | e.g. ``game`` when exporting ``game.html``    |
+------------------------------+-----------------------------------------------+
| ``$GODOT_DEBUG_ENABLED``     | ``true`` if debugging, ``false`` otherwise    |
+------------------------------+-----------------------------------------------+
| ``$GODOT_HEAD_INCLUDE``      | Custom string to include just before the end  |
|                              | of the HTML ``<head>`` element                |
+------------------------------+-----------------------------------------------+

The HTML file must evaluate the JavaScript file ``$GODOT_BASENAME.js``. This
file defines a global ``Engine`` object used to start the engine, :ref:`see
below <doc_javascript_engine_object>` for details.

The boot splash image is exported as ``$GODOT_BASENAME.png`` and can be used
e.g. in ``<img />`` elements.

``$GODOT_DEBUG_ENABLED`` can be useful to optionally display e.g. an output
console or other debug tools.

``$GODOT_HEAD_INCLUDE`` is replaced with the string specified by the export
option ``Html/Head Include``.

.. _doc_javascript_engine_object:

The ``Engine`` object
---------------------

The JavaScript global object ``Engine`` is defined by ``$GODOT_BASENAME.js``
and serves as an interface to the engine start-up process.

The API is based on and requires basic understanding of `Promises <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises>`__.

The object itself has only the following methods:

.. js:function:: Engine.load(basePath)

    Load the engine from the passed base path.

    :param string basePath: Base path of the engine to load.
    :returns: Promise which resolves once the engine is loaded.

.. js:function:: Engine.unload()

    Unload the engine to free memory.

    This is called automatically once the engine is started unless
    explicitly disabled using :js:func:`engine.setUnloadAfterInit`.

.. js:function:: Engine.isWebGLAvailable([majorVersion = 1])

    Check whether WebGL is available.

    :param number majorVersion:
        The major WebGL version to check for. Defaults to 1 for *WebGL 1.0*.

    :returns:
        ``true`` if the given major version of WebGL is available, ``false``
        otherwise.

.. js:function:: Engine.setWebAssemblyFilenameExtension(extension)

    When loading the engine, the filename extension of the WebAssembly module
    is assumed to be ``wasm``. This function allows usage of an alternate
    extension.

    .. code-block:: js

        Engine.setWebAssemblyFilenameExtension('dat');
        // Load 'mygame.dat' as WebAssembly module.
        Engine.load('mygame');

    This is useful for outdated hosts that only accept uploads of files with
    certain filename extensions.

    :param string extension:
        Filename extension without preceding dot.

    .. Note::
     Depending on the host, using an alternate filename extension can prevent
     some start-up optimizations. This occurs when the file is delivered with a
     MIME-type other than :mimetype:`application/wasm`.

Starting an ``Engine`` instance
-------------------------------

:js:class:`Engine` also acts a class:

.. js:class:: Engine

    An instance of the engine that can be started, usually a game.

Instantiate the class using the ``new`` operator:

.. code-block:: js

    var engine = new Engine();

This yields an :js:class:`Engine` instance, referred to as ``engine`` with a
lower-case ``e`` from here.

To start such an instance, the global ``Engine`` object must be loaded,
then the ``engine`` instance must be initialized and finally started.

.. js:function:: engine.init([basePath])

    Initialize the instance. The instance can then be started with one of the
    ``start`` functions, usually :js:func:`engine.startGame`.

    :param string basePath:
        The base path to the engine, same as in :js:func:`Engine.load`.
        Must be passed only if the engine hasn't been loaded yet.

    :returns: Promise that resolves once the engine is loaded and initialized.

.. js:function:: engine.preloadFile(file[, path])

    Load a file so it is available in the file system once the instance runs. Must
    be called **before** starting the instance.

    :param file:
        If type is string, the file will be loaded from that path.

        If type is ``ArrayBuffer`` or a view on one, the buffer will used as
        the content of the file.

    :param string path:
        Path by which the file will be available. Mandatory if ``file`` is not
        a string. If not passed, the path is derived from the URL of the loaded
        file.

    :returns: Promise that resolves once the file is preloaded.

.. js:function:: engine.start([arg1, arg2, …])

    Starts the instance of the engine, using the passed strings as
    command line arguments. This allows great control over how the engine is
    started, but usually the other methods starting with ``engine.start`` are
    simpler and should be used instead.

    If the instance has not yet been initialized with :js:func:`engine.init`,
    it will be.

    The engine must be loaded beforehand.

    Requires that the engine has been loaded, and that a canvas can be found on
    the page.

    :param string variadic: Command line arguments.

    :returns: Promise that resolves once the engine started.

.. js:function:: engine.startGame(execName, mainPack)

    Initializes the engine if not yet initialized, loads the executable, 
    and starts the game with the main pack loaded from the passed URL.

    If the engine isn't loaded yet, the base path of the passed executable name 
    will be used to load the engine.

    :param string execName:
        Executable's name (URL) to start. Also used as base path to load the
        engine if not loaded already. Should not contain the file's extension.

    :param string mainPack:
        Path (URL) to the main pack to start.

    :returns: Promise that resolves once the game started.

Configuring start-up behaviour
------------------------------

Beside starting the engine, other methods of the engine instance allow
configuring the behavior:

.. js:function:: engine.setUnloadAfterInit(enabled)

    Specify whether the Engine will be unloaded automatically after the
    instance is initialized.

    This frees browser memory by unloading files that are no longer needed once
    the instance is initialized. However, if more instances of the engine will
    be started, the Engine will have to be loaded again.

    Enabled by default.

    :param boolean enabled:
        ``true`` if the engine shall be unloaded after initializing,
        ``false`` otherwise.

.. js:function:: engine.setCanvas(canvasElem)

    Specify a canvas to use.

    By default, the first canvas element on the page is used for rendering.

    :param HTMLCanvasElement canvasElem: The canvas to use.

.. js:function:: engine.setCanvasResizedOnStart(enabled)

    Specifies whether the canvas will be resized to the width and height
    specified in the project settings on start.

    Enabled by default.

    :param boolean enabled:
        ``true`` if the canvas shall be resized on start, ``false`` otherwise.

.. js:function:: engine.setLocale(locale)

    By default, the engine will try to guess the locale to use from the
    JavaScript environment. It is usually preferable to use a server-side
    user-specified locale, or at least use the locale requested in the HTTP
    ``Accept-Language`` header. This method allows specifying such a custom
    locale string.

    For example, with PHP:

    .. code-block:: php

        engine.setLocale(<?php echo Locale::acceptFromHttp($_SERVER['HTTP_ACCEPT_LANGUAGE']); ?>);

    :param string locale:
        Locale.

    .. seealso:: List of :ref:`locales <doc_locales>`.

.. js:function:: engine.setExecutableName(execName)

    Specify the virtual filename of the executable.

    A real executable file doesn't exist for the HTML5 platform. However,
    a virtual filename is stored by the engine for compatibility with other
    platforms.

    By default, the base name of the loaded engine files is used.
    This method allows specifying another name.

    This affects the output of :ref:`OS.get_executable_path() <class_OS_method_get_executable_path>`
    and the automatically started main pack, :file:`{ExecutableName}.pck`.

    :param string execName: Executable name.

Customizing the presentation
----------------------------

The following methods are used to implement the presentation:

.. js:function:: engine.setProgressFunc(callback)

    Set the callback for displaying download progress.

    :param function callback:
        Callback called once per frame with two number arguments:
        bytes loaded so far, and total bytes to load.

    .. code-block:: js

        function printProgress(current, total) {
            console.log("Loaded " + current + " of " + total + " bytes");
        }
        engine.setProgressFunc(printProgress);

    If the total is 0, it couldn't be calculated. Possible reasons
    include:

     -  Files are delivered with server-side chunked compression
     -  Files are delivered with server-side compression on Chromium
     -  Not all file downloads have started yet (usually on servers without
        multi-threading)

    .. Note::
     For ease of use, the callback is only called once per frame, so that usage
     of ``requestAnimationFrame()`` is not necessary.

.. js:function:: engine.setStdoutFunc(callback)

    Specify the standard output stream callback.

    :param function callback:
        Callback function called with one argument, the string to print.

    .. code-block:: js

        function printStdout(text) {
            console.log(text);
        }
        engine.setStdoutFunc(printStdout);

    This method should usually only be used in debug pages. The
    ``$GODOT_DEBUG_ENABLED`` placeholder can be used to check for this.

    By default, ``console.log()`` is used.

.. js:function:: engine.setStderrFunc(callback)

    Specify the standard error stream callback.

    :param function callback:
        Callback function called with one argument, the string to print.

    .. code-block:: js

        function printStderr(text) {
            console.warn("Error: " + text);
        }
        engine.setStderrFunc(printStderr);

    This method should usually only be used in debug pages. The
    ``$GODOT_DEBUG_ENABLED`` placeholder can be used to check for this.

    By default, ``console.warn()`` is used.

Accessing the Emscripten ``Module``
-----------------------------------

If you know what you're doing, you can access the runtime environment
(Emscripten's ``Module``) as ``engine.rtenv``. Check the official Emscripten
documentation for information on how to use it:
https://kripken.github.io/emscripten-site/docs/api_reference/module.html
