.. _doc_html5_shell_classref:

HTML5 shell class reference
===========================

Projects exported for the Web expose the ``Engine`` class to the JavaScript environment, that allows
fine control over the engine's start-up process.

This API is built in an asynchronous manner and requires basic understanding
of `Promises <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises>`__.

Engine
------

The ``Engine`` class provides methods for loading and starting exported projects on the Web. For default export
settings, this is already part of the exported HTML page. To understand practical use of the ``Engine`` class,
see :ref:`Custom HTML page for Web export <doc_customizing_html5_shell>`.

Static Methods
^^^^^^^^^^^^^^

+---------+-------------------------------------------------------------------------------------------------------------------+
| Promise | `Engine.load <#Engine.load>`__ **(** string basePath **)**                                                        |
+---------+-------------------------------------------------------------------------------------------------------------------+
| void    | `Engine.unload <#Engine.unload>`__ **(** **)**                                                                    |
+---------+-------------------------------------------------------------------------------------------------------------------+
| boolean | `Engine.isWebGLAvailable <#Engine.isWebGLAvailable>`__ **(** *[ number majorVersion=1 ]* **)**                    |
+---------+-------------------------------------------------------------------------------------------------------------------+
| void    | `Engine.setWebAssemblyFilenameExtension <#Engine.setWebAssemblyFilenameExtension>`__ **(** string extension **)** |
+---------+-------------------------------------------------------------------------------------------------------------------+

Instance Properties
^^^^^^^^^^^^^^^^^^^

+-----------------------+----------------------------------+
| Emscripten ``Module`` | `engine.rtenv <#engine.rtenv>`__ |
+-----------------------+----------------------------------+

Instance Methods
^^^^^^^^^^^^^^^^

+---------+------------------------------------------------------------------------------------------------------+
| Engine  | `Engine <#Engine>`__ **(** **)**                                                                     |
+---------+------------------------------------------------------------------------------------------------------+
| Promise | `engine.init <#engine.init>`__ **(** *[ string basePath ]* **)**                                     |
+---------+------------------------------------------------------------------------------------------------------+
| Promise | `engine.preloadFile <#engine.preloadFile>`__ **(** string\|ArrayBuffer file *[, string path ]* **)** |
+---------+------------------------------------------------------------------------------------------------------+
| Promise | `engine.start <#engine.start>`__ **(** *[ string arg1, string arg2, … ]* **)**                       |
+---------+------------------------------------------------------------------------------------------------------+
| Promise | `engine.startGame <#engine.startGame>`__ **(** string execName, string mainPack **)**                |
+---------+------------------------------------------------------------------------------------------------------+
| void    | `engine.setUnloadAfterInit <#engine.setUnloadAfterInit>`__ **(** boolean enabled **)**               |
+---------+------------------------------------------------------------------------------------------------------+
| void    | `engine.setCanvas <#engine.setCanvas>`__ **(** HTMLCanvasElement canvasElem **)**                    |
+---------+------------------------------------------------------------------------------------------------------+
| void    | `engine.setCanvasResizedOnStart <#engine.setCanvasResizedOnStart>`__ **(** boolean enabled **)**     |
+---------+------------------------------------------------------------------------------------------------------+
| void    | `engine.setLocale <#engine.setLocale>`__ **(** string locale **)**                                   |
+---------+------------------------------------------------------------------------------------------------------+
| void    | `engine.setExecutableName <#engine.setExecutableName>`__ **(** string execName **)**                 |
+---------+------------------------------------------------------------------------------------------------------+
| void    | `engine.setProgressFunc <#engine.setProgressFunc>`__ **(** function callback **)**                   |
+---------+------------------------------------------------------------------------------------------------------+
| void    | `engine.setStdoutFunc <#engine.setStdoutFunc>`__ **(** function callback **)**                       |
+---------+------------------------------------------------------------------------------------------------------+
| void    | `engine.setStderrFunc <#engine.setStderrFunc>`__ **(** function callback **)**                       |
+---------+------------------------------------------------------------------------------------------------------+


Static Method Descriptions
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. js:method:: Engine.load(basePath)

    Load the engine from the specified base path.

    :param string basePath:
        Base path of the engine to load.
    :returns:
        Promise which resolves once the engine is loaded.

.. js:method:: Engine.unload()

    Unload the engine to free memory.

    This method is called automatically once the engine is started unless
    explicitly disabled using :js:meth:`engine.setUnloadAfterInit`.

.. js:method:: Engine.isWebGLAvailable([majorVersion = 1])

    Check whether WebGL is available. Optionally, specify a particular version of WebGL to check for.

    :param number majorVersion:
        The major WebGL version to check for. Defaults to ``1`` for *WebGL 1.0*.
    :returns:
        ``true`` if the given major version of WebGL is available, ``false``
        otherwise.

.. js:method:: Engine.setWebAssemblyFilenameExtension(extension)

    Set an alternative filename extension for the WebAssembly module. By default
    it is assumed to be ``wasm``.

    :param string extension:
        Filename extension without preceding dot.


Instance Property Descriptions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. js:attribute:: engine.rtenv

    The runtime environment provided by Emscripten's ``Module``. For more information
    refer to the `official documentation <https://emscripten.org/docs/api_reference/module.html>`__ on Emscripten.

Instance Method Descriptions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. js:class:: Engine

    Create a new instance of the ``Engine`` class.

.. js:method:: engine.init([basePath])

    Initialize the engine instance. Optionally, pass the base path to the engine to load it,
    if it hasn't been loaded yet. See :js:meth:`Engine.load`.

    :param string basePath:
        Base path of the engine to load.

    :returns:
        Promise that resolves once the engine is loaded and initialized.

.. js:method:: engine.preloadFile(file[, path])

    Load a file so it is available in the instance's file system once it runs. Must
    be called **before** starting the instance.

    :param string|ArrayBuffer file:
        If type is ``string``, the file will be loaded from that path.

        If type is ``ArrayBuffer`` or a view on one, the buffer will used as
        the content of the file.

    :param string path:
        Path by which the file will be accessible. Required, if ``file`` is not
        a string. If not passed, the path is derived from the URL of the loaded
        file.

    :returns:
        Promise that resolves once the file is loaded.

.. js:method:: engine.start([arg1, arg2, …])

    Start the instance of the engine, using the passed strings as
    command line arguments. :js:meth:`engine.startGame` can be used
    in typical cases instead.

    This will initialize the instance if it is not initialized. For manual
    initialization, see :js:meth:`engine.init`. The engine must be loaded beforehand.

    Fails if a canvas cannot be found on the page.

    :param string variadic:
        Command line argument.

    :returns:
        Promise that resolves once the engine started.

.. js:method:: engine.startGame(execName, mainPack)

    Start the game instance using the given executable URL and main pack URL.

    This will initialize the instance if it is not initialized. For manual
    initialization, see :js:meth:`engine.init`.

    This will load the engine if it is not loaded. The base path of the
    executable URL will be used as the engine base path.

    :param string execName:
        Executable name in a form of URL, omitting filename extension.

    :param string mainPack:
        URL of the main pack to start the game.

    :returns:
        Promise that resolves once the game started.

.. js:method:: engine.setUnloadAfterInit(enabled)

    Specify whether the engine will be unloaded automatically after the
    instance is initialized. Enabled by default.

    :param boolean enabled:
        ``true`` if the engine shall be unloaded after initializing,
        ``false`` otherwise.

.. js:method:: engine.setCanvas(canvasElem)

    Specify a canvas HTML element to use. By default, the first canvas element
    on the page is used for rendering.

    :param HTMLCanvasElement canvasElem:
        The canvas element to use.

.. js:method:: engine.setCanvasResizedOnStart(enabled)

    Specifies whether the canvas will be resized to the width and height
    specified in the project settings on start. Enabled by default.

    :param boolean enabled:
        ``true`` if the canvas shall be resized on start, ``false`` otherwise.

.. js:method:: engine.setLocale(locale)

    Specify a language code to select the proper localization for the game.

    .. seealso:: Complete list of :ref:`supported locales <doc_locales>`.

    :param string locale:
        Language code.

.. js:method:: engine.setExecutableName(execName)

    Specify the virtual filename of the executable. By default, the base name
    of the loaded engine files is used.

    This affects the output of :ref:`OS.get_executable_path() <class_OS_method_get_executable_path>`
    and sets the automatically started main pack to :file:`{ExecutableName}.pck`.

    :param string execName:
        Executable name.

.. js:method:: engine.setProgressFunc(callback)

    Specify a callback function for displaying download progress. The callback function is
    called once per frame, so that the usage of ``requestAnimationFrame()`` is not necessary.

    If the callback function receives a total amount of bytes as 0, this means that
    it is impossible to calculate. Possible reasons include:

     -  Files are delivered with server-side chunked compression
     -  Files are delivered with server-side compression on Chromium
     -  Not all file downloads have started yet (usually on servers without
        multi-threading)

    :param function callback:
        The callback function must accept two numeric arguments: the amount of bytes
        loaded so far, and the total number of bytes to load.

.. js:method:: engine.setStdoutFunc(callback)

    Specify a callback function for handling the standard output stream. This method
    should usually only be used in debug pages. By default, ``console.log()`` is used.

    :param function callback:
        The callback function must accept one string argument: the message to print.

.. js:method:: engine.setStderrFunc(callback)

    Specify a callback function for handling the standard error stream. This method
    should usually only be used in debug pages. By default, ``console.warn()`` is used.

    :param function callback:
        The callback function must accept one string argument: the message to print.
