:article_outdated: True

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

**General options**

+----------------------------+----------------------------------------------------------------------+
| Command                    | Description                                                          |
+----------------------------+----------------------------------------------------------------------+
| ``-h``, ``--help``         | Display the list of command line options.                            |
+----------------------------+----------------------------------------------------------------------+
| ``--version``              | Display the version string.                                          |
+----------------------------+----------------------------------------------------------------------+
| ``-v``, ``--verbose``      | Use verbose stdout mode.                                             |
+----------------------------+----------------------------------------------------------------------+
| ``-q, --quiet``            | Quiet mode, silences stdout messages. Errors are still displayed.    |
+----------------------------+----------------------------------------------------------------------+

**Run options**

+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Command                                  | Description                                                                                                                                                  |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--``                                   | Separator for user-provided arguments. Following arguments are not used by the engine, but can be read from ``OS.get_cmdline_user_args()``.                  |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``-e``, ``--editor``                     | Start the editor instead of running the scene (:ref:`target=editor <doc_introduction_to_the_buildsystem_target>` must be used).                              |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``-p``, ``--project-manager``            | Start the Project Manager, even if a project is auto-detected (:ref:`target=editor <doc_introduction_to_the_buildsystem_target>` must be used).              |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--debug-server <uri>``                 | Start the editor debug server (``<protocol>://<host/IP>[:<port>]``, e.g. ``tcp://127.0.0.1:6007``)                                                           |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--quit``                               | Quit after the first iteration.                                                                                                                              |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``-l``, ``--language <locale>``          | Use a specific locale. ``<locale>`` follows the format ``language_Script_COUNTRY_VARIANT`` where language is a 2 or 3-letter language code in lower case     |
|                                          | and the rest is optional. See :ref:`doc_locales` for more details.                                                                                           |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--path <directory>``                   | Path to a project (``<directory>`` must contain a 'project.godot' file).                                                                                     |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``-u``, ``--upwards``                    | Scan folders upwards for 'project.godot' file.                                                                                                               |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--main-pack <file>``                   | Path to a pack (.pck) file to load.                                                                                                                          |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--render-thread <mode>``               | Render thread mode ('unsafe', 'safe', 'separate'). See :ref:`Thread Model <class_ProjectSettings_property_rendering/driver/threads/thread_model>`            |
|                                          | for more details.                                                                                                                                            |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--remote-fs <address>``                | Remote filesystem (``<host/IP>[:<port>]`` address).                                                                                                          |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--remote-fs-password <password>``      | Password for remote filesystem.                                                                                                                              |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--audio-driver <driver>``              | Audio driver. Use ``--help`` first to display the list of available drivers.                                                                                 |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--display-driver <driver>``            | Display driver (and rendering driver). Use ``--help`` first to display the list of available drivers.                                                        |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--rendering-method <renderer>``        | Renderer name. Requires driver support.                                                                                                                      |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--rendering-driver <driver>``          | Rendering driver (depends on display driver). Use ``--help`` first to display the list of available drivers.                                                 |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--gpu-index <device_index>``           | Use a specific GPU (run with ``--verbose`` to get available device list).                                                                                    |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--text-driver <driver>``               | Text driver ('Fonts', 'BiDi', 'shaping')                                                                                                                     |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--tablet-driver <driver>``             | Pen tablet input driver.                                                                                                                                     |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--headless``                           | Enable headless mode (``--display-driver headless --audio-driver Dummy``). Useful for servers and with ``--script``.                                         |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--write-movie <file>``                 | Run the engine in a way that a movie is written (by default .avi MJPEG). Fixed FPS is forced when enabled, but can be used to change movie FPS.              |
|                                          | Disabling vsync can speed up movie writing but makes interaction more difficult.                                                                             |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--disable-vsync``                      | Force disabling of vsync. Run the engine in a way that a movie is written (by default .avi MJPEG).                                                           |
|                                          | Fixed FPS is forced when enabled, but can be used to change movie FPS.                                                                                       |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

**Display options**

+------------------------------------+----------------------------------------------------------------------------+
| Command                            | Description                                                                |
+------------------------------------+----------------------------------------------------------------------------+
| ``-f``, ``--fullscreen``           | Request fullscreen mode.                                                   |
+------------------------------------+----------------------------------------------------------------------------+
| ``-m``, ``--maximized``            | Request a maximized window.                                                |
+------------------------------------+----------------------------------------------------------------------------+
| ``-w``, ``--windowed``             | Request windowed mode.                                                     |
+------------------------------------+----------------------------------------------------------------------------+
| ``-t``, ``--always-on-top``        | Request an always-on-top window.                                           |
+------------------------------------+----------------------------------------------------------------------------+
| ``--resolution <W>x<H>``           | Request window resolution.                                                 |
+------------------------------------+----------------------------------------------------------------------------+
| ``--position <X>,<Y>``             | Request window position.                                                   |
+------------------------------------+----------------------------------------------------------------------------+
| ``--single-window``                | Use a single window (no separate subwindows).                              |
+------------------------------------+----------------------------------------------------------------------------+
| ``--xr-mode <mode>``               | Select XR mode (default/off/on).                                           |
+------------------------------------+----------------------------------------------------------------------------+

**Debug options**

.. note::

    Debug options are only available in the editor and debug export templates
    (they require ``debug`` or ``release_debug`` build targets, see
    :ref:`doc_introduction_to_the_buildsystem_target` for more details).

+------------------------------+---------------------------------------------------------------------------------------------------------+
| Command                      | Description                                                                                             |
+------------------------------+---------------------------------------------------------------------------------------------------------+
| ``-d``, ``--debug``          | Debug (local stdout debugger).                                                                          |
+------------------------------+---------------------------------------------------------------------------------------------------------+
| ``-b``, ``--breakpoints``    | Breakpoint list as source::line comma-separated pairs, no spaces (use %20 instead).                     |
+------------------------------+---------------------------------------------------------------------------------------------------------+
| ``--profiling``              | Enable profiling in the script debugger.                                                                |
+------------------------------+---------------------------------------------------------------------------------------------------------+
| ``--gpu-profile``            | Show a GPU profile of the tasks that took the most time during frame rendering.                         |
+------------------------------+---------------------------------------------------------------------------------------------------------+
| ``--gpu-validation``         | Enable graphics API validation layers for debugging.                                                    |
+------------------------------+---------------------------------------------------------------------------------------------------------+
| ``--gpu-abort``              | Abort on GPU errors (usually validation layer errors), may help see the problem if your system freezes. |
+------------------------------+---------------------------------------------------------------------------------------------------------+
| ``--remote-debug <uri>``     | Remote debug (``<protocol>://<host/IP>[:<port>]``, e.g. ``tcp://127.0.0.1:6007``).                      |
+------------------------------+---------------------------------------------------------------------------------------------------------+
| ``--debug-collisions``       | Show collision shapes when running the scene.                                                           |
+------------------------------+---------------------------------------------------------------------------------------------------------+
| ``--debug-paths``            | Show path lines when running the scene.                                                                 |
+------------------------------+---------------------------------------------------------------------------------------------------------+
| ``--debug-navigation``       | Show navigation polygons when running the scene.                                                        |
+------------------------------+---------------------------------------------------------------------------------------------------------+
| ``--debug-stringnames``      | Print all StringName allocations to stdout when the engine quits.                                       |
+------------------------------+---------------------------------------------------------------------------------------------------------+
| ``--frame-delay <ms>``       | Simulate high CPU load (delay each frame by <ms> milliseconds).                                         |
+------------------------------+---------------------------------------------------------------------------------------------------------+
| ``--time-scale <scale>``     | Force time scale (higher values are faster, 1.0 is normal speed).                                       |
+------------------------------+---------------------------------------------------------------------------------------------------------+
| ``--disable-render-loop``    | Disable render loop so rendering only occurs when called explicitly from script.                        |
+------------------------------+---------------------------------------------------------------------------------------------------------+
| ``--disable-crash-handler``  | Disable crash handler when supported by the platform code.                                              |
+------------------------------+---------------------------------------------------------------------------------------------------------+
| ``--fixed-fps <fps>``        | Force a fixed number of frames per second. This setting disables real-time synchronization.             |
+------------------------------+---------------------------------------------------------------------------------------------------------+
| ``--print-fps``              | Print the frames per second to the stdout.                                                              |
+------------------------------+---------------------------------------------------------------------------------------------------------+

**Standalone tools**

+------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| Command                                                          | Description                                                                                                                                     |
+------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| ``-s``, ``--script <script>``                                    | Run a script.                                                                                                                                   |
+------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--check-only``                                                 | Only parse for errors and quit (use with ``--script``).                                                                                         |
+------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--export-release <preset> <path>``                             | Export the project using the given preset and matching release template (:ref:`target=editor <doc_introduction_to_the_buildsystem_target>` must |
|                                                                  | be used). The preset name should match one defined in export_presets.cfg. ``<path>`` should be absolute or relative to the project directory,   |
|                                                                  | and include the filename for the binary (e.g. 'builds/game.exe'). The target directory should exist.                                            |
+------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--export-debug <preset> <path>``                               | Like ``--export-release``, but use debug template (:ref:`target=editor <doc_introduction_to_the_buildsystem_target>` must be used).             |
+------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--export-pack <preset> <path>``                                | Like ``--export-release``, but only export the game pack for the given preset. The ``<path>`` extension determines whether it will be in PCK    |
|                                                                  | or ZIP format (:ref:`target=editor <doc_introduction_to_the_buildsystem_target>` must be used).                                                 |
+------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--convert-3to4 [<max_file_kb>] [<max_line_size>]``             | Convert project from Godot 3.x to Godot 4.x.                                                                                                    |
+------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--validate-conversion-3to4 [<max_file_kb>] [<max_line_size>]`` | Show what elements will be renamed when converting project from Godot 3.x to Godot 4.x.                                                         |
+------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--doctool <path>``                                             | Dump the engine API reference to the given ``<path>`` in XML format, merging if existing files are found                                        |
|                                                                  | (:ref:`target=editor <doc_introduction_to_the_buildsystem_target>` must be used).                                                               |
+------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--no-docbase``                                                 | Disallow dumping the base types (used with ``--doctool``, :ref:`target=editor <doc_introduction_to_the_buildsystem_target>` must be used).      |
+------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--build-solutions``                                            | Build the scripting solutions (e.g. for C# projects, :ref:`target=editor <doc_introduction_to_the_buildsystem_target>` must be used).           |
|                                                                  | Implies ``--editor`` and requires a valid project to edit.                                                                                      |
+------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
|  ``--dump-gdextension-interface``                                | Generate GDExtension header file 'gdnative_interface.h' in the current folder. This file is the base file required to implement a GDExtension.  |
+------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--dump-extension-api``                                         | Generate JSON dump of the Godot API for GDExtension bindings named 'extension_api.json' in the current folder                                   |
|                                                                  | (:ref:`target=editor <doc_introduction_to_the_buildsystem_target>` must be used).                                                               |
+------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--startup-benchmark``                                          | Benchmark the startup time and print it to console.                                                                                             |
+------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--startup-benchmark-file <path>``                              | Benchmark the startup time and save it to a given file in JSON format.                                                                          |
+------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+

Path
----

It is recommended that your Godot editor binary be in your ``PATH`` environment
variable, so it can be executed easily from any place by typing ``godot``.
You can do so on Linux by placing the Godot binary in ``/usr/local/bin`` and
making sure it is called ``godot`` (case-sensitive).

Setting the project path
------------------------

Depending on where your Godot binary is located and what your current
working directory is, you may need to set the path to your project
for any of the following commands to work correctly.

This can be done by giving the path to the ``project.godot`` file
of your project as either the first argument, like this:

::

    godot path_to_your_project/project.godot [other] [commands] [and] [args]

Or by using the ``--path`` argument:

::

    godot --path path_to_your_project [other] [commands] [and] [args]

For example, the full command for exporting your game (as explained below) might look like this:

::

    godot --path path_to_your_project --export my_export_preset_name game.exe

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
must be done from within the project directory or a subdirectory,
otherwise the command is ignored and the Project Manager appears.

::

    godot -e

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

To run the game, simply execute Godot within the project directory or
subdirectory.

::

    godot

When a specific scene needs to be tested, pass that scene to the command
line.

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
especially useful for continuous integration setups. The version of Godot
that is headless (server build, no video) is ideal for this.

::

    # `godot` must be a Godot editor binary, not an export template.
    # Also, export templates must be installed for the editor
    # (or a valid custom export template must be defined in the export preset).
    godot --export "Linux/X11" /var/builds/project
    godot --export Android /var/builds/project.apk

The preset name must match the name of an export preset defined in the
project's ``export_presets.cfg`` file. If the preset name contains spaces or
special characters (such as "Windows Desktop"), it must be surrounded with quotes.

To export a debug version of the game, use the ``--export-debug`` switch
instead of ``--export``. Their parameters and usage are the same.

To export only a PCK file, use the ``--export-pack`` option followed by the
preset name and output path, with the file extension, instead of ``--export``.
The output path extension determines the package's format, either PCK or ZIP.

.. warning::

    When specifying a relative path as the path for `--export`, `--export-debug`
    or `--export-pack`, the path will be relative to the directory containing
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
