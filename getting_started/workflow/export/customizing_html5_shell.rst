.. _doc_customizing_html5_shell:

Customizing the Web export HTML page
====================================

Rather than the default HTML page that comes with the export templates, it is
also possible to use a custom HTML page. This allows drastic customization of
the final web presentation and behavior. The path to the custom HTML page is
specified in the export options as ``Html/Custom Html Shell``.

The default HTML page is available in the Godot Engine repository at
`/mist/dist/html/default.html <https://github.com/godotengine/godot/blob/master/misc/dist/html/default.html>`_.
Some simple use-cases where customizing the default page is useful include:

 - Loading files from a different directory
 - Loading a ``.zip`` file instead of a ``.pck`` file as main pack
 - Loading engine files from a different directory than the main pack file
 - Loading some extra files before the engine starts, so they are available in
   the file system later
 - Passing custom "command line" arguments, e.g. ``-s`` to start a MainLoop script

Placeholder substitution
------------------------

When exporting the game, several placeholders in the HTML page are substituted
by values dependening on the export:

+------------------------------+-----------------------------------------------+
| Placeholder                  | substituted by                                |
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

``$GODOT_HEAD_INCLUDE`` is substituted with the string specified by the export
option ``Html/Head Include``.

.. _doc_javascript_engine_object:

The ``Engine`` object
---------------------

The JavaScript global object ``Engine`` is defined by ``$GODOT_BASENAME.js``
and serves as an interface to the engine start-up process.

The object itself has only two methods, ``load()`` and ``unload()``.

``Engine.load(basePath)``
~~~~~~~~~~~~~~~~~~~~~~~~~

Loads the engine from the passed base path.

Returns a promise that resolves once the engine is loaded.

``Engine.unload()``
~~~~~~~~~~~~~~~~~~~

Unloads the module to free memory. This is called automatically once the
module is instantiated unless explicitly disabled.

``Engine.isWebGLAvailable(majorVersion = 1)``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Returns ``true`` if the given major version of WebGL is available,
``false`` otherwise. Defaults to ``1`` for WebGL 1.0.

Starting an ``Engine`` instance
-------------------------------

The more interesting interface is accessed by instantiating ``Engine`` using
the ``new`` operator:

.. code-block:: js

    var engine = new Engine();

This ``Engine`` instance, referred to as ``engine`` with a lower-case ``e``
from here, is a startable instance of the engine, usually a game. To start such
an instance, the global ``Engine`` object must be loaded, then the ``engine``
instance must be initialized and started.

``engine.init(basePath)``
~~~~~~~~~~~~~~~~~~~~~~~~~

Initializes the instance. If the engine wasn't loaded yet, a base path
must be passed from which the engine will be loaded.

Returns a promise that resolves once the engine is loaded and initialized.
It can then be started with ``engine.startGame()``

``engine.preloadFile(file, path)``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This loads a file so it is available in the file system once the instance
is started. This must be called **before** starting the instance.

If ``file`` is a string, the file will be loaded from that URL. If ``file`` is
an ``ArrayBuffer`` or a view on one, the buffer will used as content of the
file.

If ``path`` is a string, it specifies the path by which the file will be
available. This is mandatory if ``file`` is not a string.
Otherwise, the path is derived from the URL of the loaded file.

Returns a promise that resolves once the file is preloaded.

``engine.start(arg1, arg2, …)``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Starts the instance of the engine, handing the passed strings as arguments
to the ``main()`` function. This allows great control over how the engine
is used, but usually the other methods whose names start with ``engine.start``
are simpler to use.

Returns a promise that resolves once the engine started.

``engine.startGame(mainPack)``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Starts the game with the main pack loaded from the passed URL string and
starts the engine with it.

If the engine isn't loaded yet, the base path of the passed URL will be
used to load the engine.

Returns a promise that resolves once the game started.

Configuring start-up behaviour
------------------------------

Beside starting the engine, other methods of the engine instance allow
configuring the behavior:

``engine.setUnloadAfterInit(enabled)``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sets whether the Engine will be unloaded automatically after the instance
is initialized. This frees browser memory by unloading files that are no
longer needed once the instance is initialized. However, if more instances of
the engine will be started, the Engine will have to be loaded again.

Defaults to ``true``.

``engine.setCanvas(canvasElem)``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By default, the first canvas element on the page is used for rendering.
By calling this method, another canvas can be specified.

``engine.setCanvasResizedOnStart(enabled)``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sets whether the canvas will be resized to the width and height specified
in the project settings on start. Defaults to ``true``.

``engine.setLocale(locale)``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By default, the engine will try to guess the locale to use from the
JavaScript environment. It is usually preferable to use a server-side
user-specified locale, or at least use the locale requested in the HTTP
``Accept-Language`` header. This method allows specifying such a custom locale
string.

``engine.setExecutableName(execName)``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By default, the base name of the loaded engine files is used for the
executable name. This method allows specifying another name.

Customizing the presentation
----------------------------

The following methods are used to implement the presentation:

``engine.setProgressFunc(func)``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This method is used to display download progress. The passed callback
function is called with two number arguments, the first argument specifies
bytes loaded so far, the second argument specifies the total number of bytes
to load.

.. code-block:: js

    function printProgress(current, total) {
        console.log("Loaded " + current + " of " + total + " bytes");
    }
    engine.setProgressFunc(printProgress);

If the total is 0, it couldn't be calculated. Possible reasons
include:

 -  Files are delivered with server-side chunked compression
 -  Files are delivered with server-side compression on Chromium
 -  Not all file downloads have started yet (usually on servers without multi-threading)

``engine.setStdoutFunc(func)``, ``engine.setStderrFunc(func)``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These methods allow implementing custom behavior for the ``stdout`` and
``stderr`` streams. The functions passed in will be called with one string
argument specifying the string to print.

.. code-block:: js

    function printStderr(text) {
        console.warn("Error: " + text);
    }
    engine.setStderrFunc(printStderr);

These methods should usually only be used in debug pages. The
``$GODOT_DEBUG_ENABLED`` placeholder can be used to check for this.

By default, ``console.log()`` and ``console.warn()`` are used respectively.

Accessing the Emscripten ``Module``
-----------------------------------

If you know what you're doing, you can access the runtime environment
(Emscripten's ``Module``) as ``engine.rtenv``. Check the official Emscripten
documentation for information on how to use it:
https://kripken.github.io/emscripten-site/docs/api_reference/module.html
