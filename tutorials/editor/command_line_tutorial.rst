.. _doc_command_line_tutorial:

Command line tutorial
=====================

.. highlight:: shell

Some developers like using the command line extensively. Godot is
designed to be friendly to them, so here are the steps for working
entirely from the command line. Given the engine relies on almost no
external libraries, initialization times are pretty fast, making it
suitable for this workflow.

.. note::

    On Windows and Linux, you can run a Godot binary in a terminal by specifying
    its relative or absolute path.

    On macOS, the process is different due to Godot being contained within an
    ``.app`` bundle (which is a *folder*, not a file). To run a Godot binary
    from a terminal on macOS, you have to ``cd`` to the folder where the Godot
    application bundle is located, then run ``Godot.app/Contents/MacOS/Godot``
    followed by any command line arguments. If you've renamed the application
    bundle from ``Godot`` to another name, make sure to edit this command line
    accordingly.

Command line reference
----------------------

.. |release| image:: img/template_release.svg
.. |debug| image:: img/template_debug.svg
.. |editor| image:: img/editor.svg

**Legend**

- |release| Available in editor builds, debug export templates and release export templates.
- |debug| Available in editor builds and debug export templates only.
- |editor| Only available in editor builds.

Note that unknown command line arguments have no effect whatsoever. The engine
will **not** warn you when using a command line argument that doesn't exist with a
given build type.

**General options**

+----------------------------+-----------------------------------------------------------------------------+
| Command                    | Description                                                                 |
+----------------------------+-----------------------------------------------------------------------------+
| ``-h``, ``--help``         | |release| Display the list of command line options.                         |
+----------------------------+-----------------------------------------------------------------------------+
| ``--version``              | |release| Display the version string.                                       |
+----------------------------+-----------------------------------------------------------------------------+
| ``-v``, ``--verbose``      | |release| Use verbose stdout mode.                                          |
+----------------------------+-----------------------------------------------------------------------------+
| ``-q``, ``--quiet``        | |release| Quiet mode, silences stdout messages. Errors are still displayed. |
+----------------------------+-----------------------------------------------------------------------------+

**Run options**

+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Command                                  | Description                                                                                                                                                  |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--``, ``++``                           | |release| Separator for user-provided arguments. Following arguments are not used by the engine, but can be read from ``OS.get_cmdline_user_args()``.        |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``-e``, ``--editor``                     | |editor| Start the editor instead of running the scene.                                                                                                      |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``-p``, ``--project-manager``            | |editor| Start the Project Manager, even if a project is auto-detected.                                                                                      |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--debug-server <uri>``                 | |editor| Start the editor debug server (``<protocol>://<host/IP>[:<port>]``, e.g. ``tcp://127.0.0.1:6007``)                                                  |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--quit``                               | |release| Quit after the first iteration.                                                                                                                    |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--quit-after``                         | |release| Quit after the given number of iterations. Set to 0 to disable.                                                                                    |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``-l``, ``--language <locale>``          | |release| Use a specific locale. ``<locale>`` follows the format ``language_Script_COUNTRY_VARIANT`` where language is a 2 or 3-letter language code in      |
|                                          | lowercase and the rest is optional. See :ref:`doc_locales` for more details.                                                                                 |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--path <directory>``                   | |release| Path to a project (``<directory>`` must contain a 'project.godot' file).                                                                           |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``-u``, ``--upwards``                    | |release| Scan folders upwards for 'project.godot' file.                                                                                                     |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--main-pack <file>``                   | |release| Path to a pack (.pck) file to load.                                                                                                                |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--render-thread <mode>``               | |release| Render thread mode ('unsafe', 'safe', 'separate'). See :ref:`Thread Model <class_ProjectSettings_property_rendering/driver/threads/thread_model>`  |
|                                          | for more details.                                                                                                                                            |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--remote-fs <address>``                | |release| Remote filesystem (``<host/IP>[:<port>]`` address).                                                                                                |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--remote-fs-password <password>``      | |release| Password for remote filesystem.                                                                                                                    |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--audio-driver <driver>``              | |release| Audio driver. Use ``--help`` first to display the list of available drivers.                                                                       |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--display-driver <driver>``            | |release| Display driver (and rendering driver). Use ``--help`` first to display the list of available drivers.                                              |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--rendering-method <renderer>``        | |release| Renderer name. Requires driver support.                                                                                                            |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--rendering-driver <driver>``          | |release| Rendering driver (depends on display driver). Use ``--help`` first to display the list of available drivers.                                       |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--gpu-index <device_index>``           | |release| Use a specific GPU (run with ``--verbose`` to get available device list).                                                                          |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--text-driver <driver>``               | |release| Text driver (Fonts, BiDi, shaping).                                                                                                                |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--tablet-driver <driver>``             | |release| Pen tablet input driver.                                                                                                                           |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--headless``                           | |release| Enable headless mode (``--display-driver headless --audio-driver Dummy``). Useful for servers and with ``--script``.                               |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--write-movie <file>``                 | |release| Run the engine in a way that a movie is written (usually with .avi or .png extension).                                                             |
|                                          | ``--fixed-fps`` is forced when enabled, but can be used to change movie FPS.                                                                                 |
|                                          | ``--disable-vsync`` can speed up movie writing but makes interaction more difficult.                                                                         |
|                                          | ``--quit-after`` can be used to specify the number of frames to write.                                                                                       |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

**Display options**

+------------------------------------+----------------------------------------------------------------------------+
| Command                            | Description                                                                |
+------------------------------------+----------------------------------------------------------------------------+
| ``-f``, ``--fullscreen``           | |release| Request fullscreen mode.                                         |
+------------------------------------+----------------------------------------------------------------------------+
| ``-m``, ``--maximized``            | |release| Request a maximized window.                                      |
+------------------------------------+----------------------------------------------------------------------------+
| ``-w``, ``--windowed``             | |release| Request windowed mode.                                           |
+------------------------------------+----------------------------------------------------------------------------+
| ``-t``, ``--always-on-top``        | |release| Request an always-on-top window.                                 |
+------------------------------------+----------------------------------------------------------------------------+
| ``--resolution <W>x<H>``           | |release| Request window resolution.                                       |
+------------------------------------+----------------------------------------------------------------------------+
| ``--position <X>,<Y>``             | |release| Request window position.                                         |
+------------------------------------+----------------------------------------------------------------------------+
| ``--screen <N>``                   | |release| Request window screen.                                           |
+------------------------------------+----------------------------------------------------------------------------+
| ``--single-window``                | |release| Use a single window (no separate subwindows).                    |
+------------------------------------+----------------------------------------------------------------------------+
| ``--xr-mode <mode>``               | |release| Select XR mode ('default', 'off', 'on').                         |
+------------------------------------+----------------------------------------------------------------------------+

**Debug options**

+--------------------------------+-----------------------------------------------------------------------------------------------------------------+
| Command                        | Description                                                                                                     |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``-d``, ``--debug``            | |release| Debug (local stdout debugger).                                                                        |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``-b``, ``--breakpoints``      | |release| Breakpoint list as source::line comma-separated pairs, no spaces (use ``%20`` instead).               |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``--profiling``                | |release| Enable profiling in the script debugger.                                                              |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``--gpu-profile``              | |release| Show a GPU profile of the tasks that took the most time during frame rendering.                       |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``--gpu-validation``           | |release| Enable graphics API :ref:`validation layers <doc_vulkan_validation_layers>` for debugging.            |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``--gpu-abort``                | |debug| Abort on GPU errors (usually validation layer errors), may help see the problem if your system freezes. |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``--remote-debug <uri>``       | |release| Remote debug (``<protocol>://<host/IP>[:<port>]``, e.g. ``tcp://127.0.0.1:6007``).                    |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``--single-threaded-scene``    | |release| Scene tree runs in single-threaded mode. Sub-thread groups are disabled and run on the main thread.   |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``--debug-collisions``         | |debug| Show collision shapes when running the scene.                                                           |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``--debug-paths``              | |debug| Show path lines when running the scene.                                                                 |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``--debug-navigation``         | |debug| Show navigation polygons when running the scene.                                                        |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``--debug-avoidance``          | |debug| Show navigation avoidance debug visuals when running the scene.                                         |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``--debug-stringnames``        | |debug| Print all StringName allocations to stdout when the engine quits.                                       |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``--frame-delay <ms>``         | |release| Simulate high CPU load (delay each frame by <ms> milliseconds).                                       |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``--time-scale <scale>``       | |release| Force time scale (higher values are faster, 1.0 is normal speed).                                     |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``--disable-vsync``            | |release| Forces disabling of vertical synchronization, even if enabled in the project settings.                |
|                                | Does not override driver-level V-Sync enforcement.                                                              |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``--disable-render-loop``      | |release| Disable render loop so rendering only occurs when called explicitly from script.                      |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``--disable-crash-handler``    | |release| Disable crash handler when supported by the platform code.                                            |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``--fixed-fps <fps>``          | |release| Force a fixed number of frames per second. This setting disables real-time synchronization.           |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``--delta-smoothing <enable>`` | |release| Enable or disable frame delta smoothing ('enable', 'disable').                                        |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``--print-fps``                | |release| Print the frames per second to the stdout.                                                            |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------+

**Standalone tools**

+------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| Command                                                          | Description                                                                                                                                             |
+------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``-s``, ``--script <script>``                                    | |release| Run a script.                                                                                                                                 |
+------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--check-only``                                                 | |release| Only parse for errors and quit (use with ``--script``).                                                                                       |
+------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--export-release <preset> <path>``                             | |editor| Export the project using the given preset and matching release template. The preset name                                                       |
|                                                                  | should match one defined in export_presets.cfg. ``<path>`` should be absolute or relative to the project directory,                                     |
|                                                                  | and include the filename for the binary (e.g. 'builds/game.exe'). The target directory should exist.                                                    |
+------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--export-debug <preset> <path>``                               | |editor| Like ``--export-release``, but use debug template.                                                                                             |
+------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--export-pack <preset> <path>``                                | |editor| Like ``--export-release``, but only export the game pack for the given preset. The ``<path>`` extension determines whether it will be in PCK   |
|                                                                  | or ZIP format.                                                                                                                                          |
+------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--convert-3to4 [<max_file_kb>] [<max_line_size>]``             | |editor| Convert project from Godot 3.x to Godot 4.x.                                                                                                   |
+------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--validate-conversion-3to4 [<max_file_kb>] [<max_line_size>]`` | |editor| Show what elements will be renamed when converting project from Godot 3.x to Godot 4.x.                                                        |
+------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--doctool [<path>]``                                           | |editor| Dump the engine API reference to the given ``<path>`` in XML format, merging if existing files are found.                                      |
+------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--no-docbase``                                                 | |editor| Disallow dumping the base types (used with ``--doctool``).                                                                                     |
+------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--gdscript-docs <path>``                                       | |editor| Rather than dumping the engine API, generate API reference from the inline documentation in the GDScript files found in <path>                 |
|                                                                  | (used with ``--doctool``).                                                                                                                              |
+------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--build-solutions``                                            | |editor| Build the scripting solutions (e.g. for C# projects). Implies ``--editor`` and requires a valid project to edit.                               |
+------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--dump-gdextension-interface``                                 | |editor| Generate GDExtension header file 'gdnative_interface.h' in the current folder. This file is the base file required to implement a GDExtension. |
+------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--dump-extension-api``                                         | |editor| Generate JSON dump of the Godot API for GDExtension bindings named 'extension_api.json' in the current folder.                                 |
+------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--validate-extension-api <path>``                              | |editor| Validate an extension API file dumped (with the option above) from a previous version of the engine to ensure API compatibility.               |
|                                                                  | If incompatibilities or errors are detected, the return code will be non-zero.                                                                          |
+------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--benchmark``                                                  | |editor| Benchmark the run time and print it to console.                                                                                                |
+------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--benchmark-file <path>``                                      | |editor| Benchmark the run time and save it to a given file in JSON format. The path should be absolute.                                                |
+------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+

Path
----

It is recommended to place your Godot editor binary in your ``PATH`` environment
variable, so it can be executed easily from any place by typing ``godot``.
You can do so on Linux by placing the Godot binary in ``/usr/local/bin`` and
making sure it is called ``godot`` (case-sensitive).

To achieve this on Windows or macOS easily, you can install Godot using
`Scoop <https://scoop.sh>`__ (on Windows) or `Homebrew <https://brew.sh>`__
(on macOS). This will automatically make the copy of Godot installed
available in the ``PATH``:

.. tabs::

 .. code-tab:: sh Windows

    # Standard editor:
    scoop install godot

    # Editor with C# support (will be available as `godot-mono` in `PATH`):
    scoop install godot-mono

 .. code-tab:: sh macOS

    # Standard editor:
    brew install godot

    # Editor with C# support (will be available as `godot-mono` in `PATH`):
    brew install godot-mono

Setting the project path
------------------------

Depending on where your Godot binary is located and what your current
working directory is, you may need to set the path to your project
for any of the following commands to work correctly.

When running the editor, this can be done by giving the path to the ``project.godot`` file
of your project as either the first argument, like this:

::

    godot path_to_your_project/project.godot [other] [commands] [and] [args]

For all commands, this can be done by using the ``--path`` argument:

::

    godot --path path_to_your_project [other] [commands] [and] [args]

For example, the full command for exporting your game (as explained below) might look like this:

::

    godot --headless --path path_to_your_project --export-release my_export_preset_name game.exe

When starting from a subdirectory of your project, use the ``--upwards`` argument for Godot to 
automatically find the ``project.godot`` file by recursively searching the parent directories.

For example, running a scene (as explained below) nested in a subdirectory might look like this 
when your working directory is in the same path:

::

    godot --upwards nested_scene.tscn 


..

Creating a project
------------------


Creating a project from the command line can be done by navigating the
shell to the desired place and making a ``project.godot`` file.


::

    mkdir newgame
    cd newgame
    touch project.godot


The project can now be opened with Godot.


Running the editor
------------------

Running the editor is done by executing Godot with the ``-e`` flag. This
must be done from within the project directory or by setting the project path as explained above,
otherwise the command is ignored and the Project Manager appears.

::

    godot -e

When passing in the full path to the ``project.godot`` file, the ``-e`` flag may be omitted.

If a scene has been created and saved, it can be edited later by running
the same code with that scene as argument.

::

    godot -e scene.tscn

Erasing a scene
---------------

Godot is friends with your filesystem and will not create extra metadata files.
Use ``rm`` to erase a scene file. Make sure nothing references that scene.
Otherwise, an error will be thrown upon opening the project.

::

    rm scene.tscn

Running the game
----------------

To run the game, execute Godot within the project directory or with the project path as explained above.  

::

    godot

Note that passing in the ``project.godot`` file will always run the editor instead of running the game.

When a specific scene needs to be tested, pass that scene to the command line.

::

    godot scene.tscn

Debugging
---------

Catching errors in the command line can be a difficult task because they
scroll quickly. For this, a command line debugger is provided by adding
``-d``. It works for running either the game or a single scene.

::

    godot -d

::

    godot -d scene.tscn

.. _doc_command_line_tutorial_exporting:

Exporting
---------

Exporting the project from the command line is also supported. This is
especially useful for continuous integration setups.

.. note::

    Using the ``--headless`` command line argument is **required** on platforms
    that do not have GPU access (such as continuous integration). On platforms
    with GPU access, ``--headless`` prevents a window from spawning while the
    project is exporting.

::

    # `godot` must be a Godot editor binary, not an export template.
    # Also, export templates must be installed for the editor
    # (or a valid custom export template must be defined in the export preset).
    godot --headless --export-release "Linux/X11" /var/builds/project
    godot --headless --export-release Android /var/builds/project.apk

The preset name must match the name of an export preset defined in the
project's ``export_presets.cfg`` file. If the preset name contains spaces or
special characters (such as "Windows Desktop"), it must be surrounded with quotes.

To export a debug version of the game, use the ``--export-debug`` switch instead
of ``--export-release``. Their parameters and usage are the same.

To export only a PCK file, use the ``--export-pack`` option followed by the
preset name and output path, with the file extension, instead of
``--export-release`` or ``--export-debug``. The output path extension determines
the package's format, either PCK or ZIP.

.. warning::

    When specifying a relative path as the path for ``--export-release``, ``--export-debug``
    or ``--export-pack``, the path will be relative to the directory containing
    the ``project.godot`` file, **not** relative to the current working directory.

Running a script
----------------

It is possible to run a ``.gd`` script from the command line.
This feature is especially useful in large projects, e.g. for batch
conversion of assets or custom import/export.

The script must inherit from ``SceneTree`` or ``MainLoop``.

Here is an example ``sayhello.gd``, showing how it works:

.. code-block:: python

    #!/usr/bin/env -S godot -s
    extends SceneTree

    func _init():
        print("Hello!")
        quit()

And how to run it:

::

    # Prints "Hello!" to standard output.
    godot -s sayhello.gd

If no ``project.godot`` exists at the path, current path is assumed to be the
current working directory (unless ``--path`` is specified).

The first line of ``sayhello.gd`` above is commonly referred to as
a *shebang*. If the Godot binary is in your ``PATH`` as ``godot``,
it allows you to run the script as follows in modern Linux
distributions, as well as macOS:

::

    # Mark script as executable.
    chmod +x sayhello.gd
    # Prints "Hello!" to standard output.
    ./sayhello.gd

If the above doesn't work in your current version of Linux or macOS, you can
always have the shebang run Godot straight from where it is located as follows:

::

    #!/usr/bin/godot -s
