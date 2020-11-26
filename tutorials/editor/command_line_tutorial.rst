.. _doc_command_line_tutorial:

Command line tutorial
=====================

.. highlight:: shell

Some developers like using the command line extensively. Godot is
designed to be friendly to them, so here are the steps for working
entirely from the command line. Given the engine relies on almost no
external libraries, initialization times are pretty fast, making it
suitable for this workflow.

Command line reference
----------------------

**General options**

+----------------------------+----------------------------------------------------------------------+
| Command                    | Description                                                          |
+----------------------------+----------------------------------------------------------------------+
| ``-h``, ``--help``, ``/?`` | Display the list of command line options.                            |
+----------------------------+----------------------------------------------------------------------+
| ``--version``              | Display the version string.                                          |
+----------------------------+----------------------------------------------------------------------+
| ``-v``, ``--verbose``      | Use verbose stdout mode.                                             |
+----------------------------+----------------------------------------------------------------------+
| ``--quiet``                | Quiet mode, silences stdout messages. Errors are still displayed.    |
+----------------------------+----------------------------------------------------------------------+

**Run options**

+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Command                                  | Description                                                                                                                                                  |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``-e``, ``--editor``                     | Start the editor instead of running the scene (:ref:`tools <doc_introduction_to_the_buildsystem_tools>` must be enabled).                                    |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``-p``, ``--project-manager``            | Start the project manager, even if a project is auto-detected (:ref:`tools <doc_introduction_to_the_buildsystem_tools>` must be enabled).                    |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``-q``, ``--quit``                       | Quit after the first iteration.                                                                                                                              |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``-l <locale>``, ``--language <locale>`` | Use a specific locale (<locale> being a two-letter code). See :ref:`doc_locales` for more details.                                                           |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--path <directory>``                   | Path to a project (<directory> must contain a 'project.godot' file).                                                                                         |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``-u``, ``--upwards``                    | Scan folders upwards for 'project.godot' file.                                                                                                               |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--main-pack <file>``                   | Path to a pack (.pck) file to load.                                                                                                                          |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--render-thread <mode>``               | Render thread mode ('unsafe', 'safe', 'separate'). See :ref:`Thread Model <class_ProjectSettings_property_rendering/threads/thread_model>` for more details. |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--remote-fs <address>``                | Remote filesystem (``<host/IP>[:<port>]`` address).                                                                                                          |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--remote-fs-password <password>``      | Password for remote filesystem.                                                                                                                              |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--audio-driver <driver>``              | Audio driver. Use ``--help`` first to display the list of available drivers.                                                                                 |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--display-driver <driver>``            | Display driver (and rendering driver). Use ``--help`` first to display the list of available drivers.                                                        |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--rendering-driver <driver>``          | Rendering driver (depends on display driver). Use ``--help`` first to display the list of available drivers.                                                 |
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
| ``--low-dpi``                      | Force low-DPI mode (macOS and Windows only).                               |
+------------------------------------+----------------------------------------------------------------------------+
| ``--no-window``                    | Disable window creation (Windows only). Useful together with ``--script``. |
+------------------------------------+----------------------------------------------------------------------------+
| ``--enable-vsync-via-compositor``  | When vsync is enabled, vsync via the OS' window compositor (Windows only). |
+------------------------------------+----------------------------------------------------------------------------+
| ``--disable-vsync-via-compositor`` | Disable vsync via the OS' window compositor (Windows only).                |
+------------------------------------+----------------------------------------------------------------------------+
| ``--single-window``                | Use a single window (no separate subwindows).                              |
+------------------------------------+----------------------------------------------------------------------------+
| ``--tablet-driver``                | Tablet input driver (Windows only).                                        |
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
| ``--gpu-abort``              | Abort on GPU errors (usually validation layer errors), may help see the problem if your system freezes. |
+------------------------------+---------------------------------------------------------------------------------------------------------+
| ``--remote-debug <address>`` | Remote debug (<protocol>://<host/IP>[:<port>], e.g. tcp://127.0.0.1:6007).                              |
+------------------------------+---------------------------------------------------------------------------------------------------------+
| ``--debug-collisions``       | Show collision shapes when running the scene.                                                           |
+------------------------------+---------------------------------------------------------------------------------------------------------+
| ``--debug-navigation``       | Show navigation polygons when running the scene.                                                        |
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

+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| Command                                | Description                                                                                                                                     |
+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| ``-s <script>``, ``--script <script>`` | Run a script.                                                                                                                                   |
+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--check-only``                       | Only parse for errors and quit (use with ``--script``).                                                                                         |
+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--export <preset> <path>``           | Export the project using the given export target. Export only main pack if path ends with .pck or .zip                                          |
|                                        | (:ref:`tools <doc_introduction_to_the_buildsystem_tools>` must be enabled).                                                                     |
+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--export-debug <preset> <path>``     | Like ``--export``, but use debug template (:ref:`tools <doc_introduction_to_the_buildsystem_tools>` must be enabled).                           |
+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--export-pack <preset> <path>``      | Like ``--export``, but only export the game pack for the given preset. The <path> extension determines whether it will be in PCK or ZIP format. |
|                                        | (:ref:`tools <doc_introduction_to_the_buildsystem_tools>` must be enabled).                                                                     |
+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--doctool <path>``                   | Dump the engine API reference to the given <path> in XML format, merging if existing files are found                                            |
|                                        | (:ref:`tools <doc_introduction_to_the_buildsystem_tools>` must be enabled).                                                                     |
+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--no-docbase``                       | Disallow dumping the base types (used with ``--doctool``, :ref:`tools <doc_introduction_to_the_buildsystem_tools>` must be enabled).            |
+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--build-solutions``                  | Build the scripting solutions (e.g. for C# projects, :ref:`tools <doc_introduction_to_the_buildsystem_tools>` must be enabled).                 |
+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--gdnative-generate-json-api``       | Generate JSON dump of the Godot API for GDNative bindings (:ref:`tools <doc_introduction_to_the_buildsystem_tools>` must be enabled).           |
+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| ``--test <test>``                      | Run a unit test. Use ``--help`` first to display the list of tests. (:ref:`tools <doc_introduction_to_the_buildsystem_tools>` must be enabled). |
+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+

Path
----

It is recommended that your Godot editor binary be in your ``PATH`` environment
variable, so it can be executed easily from any place by typing ``godot``.
You can do so on Linux by placing the Godot binary in ``/usr/local/bin`` and
making sure it is called ``godot``.

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
otherwise the command is ignored and the project manager appears.

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
just fly by. For this, a command line debugger is provided by adding
``-d``. It works for running either the game or a simple scene.

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

The platform names recognized by the ``--export`` switch are the same as
displayed in the export wizard of the editor. To get a list of supported
platforms from the command line, try exporting to a non-recognized
platform and the full listing of platforms your configuration supports
will be shown.

To export a debug version of the game, use the ``--export-debug`` switch
instead of ``--export``. Their parameters and usage are the same.

To export only a PCK file, use the ``--export-pack`` option followed by the
preset name and output path, with the file extension, instead of ``--export``.
The output path extension determines the package's format, either PCK or ZIP.

Running a script
----------------

It is possible to run a simple ``.gd`` script from the command line.
This feature is especially useful in large projects, e.g. for batch
conversion of assets or custom import/export.

The script must inherit from ``SceneTree`` or ``MainLoop``.

Here is a simple ``sayhello.gd`` example of how it works:

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

.. questions-answers:: command-line
