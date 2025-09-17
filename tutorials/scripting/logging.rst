.. _doc_logging:

Logging
=======

Godot comes with several ways to organize and collect log messages.

Printing messages
-----------------

.. seealso::

    See :ref:`doc_output_panel_printing_messages` for instructions on printing
    messages. The printed output is generally identical to the logged output.

    When running a project from the editor, the editor will display logged text
    in the :ref:`doc_output_panel`.

Project settings
----------------

There are several project settings to control logging behavior in Godot:

- **Application > Run > Disable stdout:** Disables logging to standard output entirely.
  This also affects what custom loggers receive. This can be controlled at runtime
  by setting :ref:`Engine.print_to_stdout <class_Engine_property_print_to_stdout>`.
- **Application > Run > Disable stderr:** Disables logging to standard error entirely.
  This also affects what custom loggers receive. This can be controlled at runtime
  by setting :ref:`Engine.print_error_messages <class_Engine_property_print_error_messages>`.
- **Debug > Settings > stdout > Verbose stdout:** Enables verbose logging to standard output.
  Prints from :ref:`print_verbose() <class_@GlobalScope_method_print_verbose>` are only
  visible if verbose mode is enabled.
- **Debug > Settings > stdout > Print FPS:** Prints the frames per second every second,
  as well as the V-Sync status on startup (as it can effectively cap the maximum framerate).
- **Debug > Settings > stdout > Print GPU Profile:** Prints a report of GPU utilization
  every second, using the same data source as the :ref:`doc_debugger_panel_visual_profiler`.

Some of these project settings can also be overridden using
:ref:`command line arguments <doc_command_line_tutorial>` such as ``--quiet``,
``--verbose``, and ``--print-fps``.

The engine's own file logging is also configurable, as described in the section below.

Built-in file logging
---------------------

By default, Godot writes log files in ``user://logs/godot.log`` on desktop
platforms. You can change this location by modifying the
``debug/file_logging/log_path`` project setting. Logs are rotated to keep older
files available for inspection. Each session creates a new log file, with the
old file renamed to contain the date at which it was rotated. Up to 5 log files
are kept by default, which can be adjusted using the
``debug/file_logging/max_log_files`` project setting.

File logging can also be disabled completely using the
``debug/file_logging/enable_file_logging`` project setting.

When the project crashes, crash logs are written to the same file as the log
file. The crash log will only contain a usable backtrace if the binary that was
run contains debugging symbols, or if it can find a debug symbols file that
matches the binary. Official binaries don't provide debugging symbols, so this
requires a custom build to work. See
:ref:`Debugging symbols <doc_introduction_to_the_buildsystem_debugging_symbols>`
for guidance on compiling binaries with debugging symbols enabled.

.. note::

    Log files for :ref:`print() <class_@GlobalScope_method_print>`
    statements are updated when standard output is *flushed* by the engine.
    Standard output is flushed on every print in debug builds only. In projects that
    are exported in release mode, standard output is only flushed when the project exits
    or crashes to improve performance, especially if the project is often printing
    text to standard output.

    On the other hand, the standard error stream
    (used by :ref:`printerr() <class_@GlobalScope_method_printerr>`,
    :ref:`push_error() <class_@GlobalScope_method_push_error>`, and
    :ref:`push_warning() <class_@GlobalScope_method_push_warning>`) is always
    flushed on every print, even in projects exported in release mode.

    For some use cases like dedicated servers, it can be preferred to have release
    builds always flush stdout on print, so that logging services like journald can
    collect logs while the process is running. This can be done by enabling
    ``application/run/flush_stdout_on_print`` in the Project Settings.

Script backtraces
-----------------

Since Godot 4.5, when GDScript code encounters an error, it will log a backtrace that points
to the origin of the error, while also containing the call stack leading to it. This behavior
is always enabled when running in the editor, or when the project is exported in debug mode.

In projects exported in release mode, backtraces are disabled by default for performance reasons.
You can enable them by checking **Debug > Settings > GDScript > Always Track Call Stacks** in
the Project Settings. If you use a custom logging system that reports exceptions to a remote
service, it's recommended to enable this to make reported errors more actionable.

Crash backtraces
----------------

.. warning::

    Crash backtraces are only useful if they were recorded in a build that
    contains :ref:`debugging symbols <doc_introduction_to_the_buildsystem_debugging_symbols>`.
    Official Godot binaries do not contain debugging symbols, so you must compile a
    custom editor or export template binary to get useful crash backtraces.

When the project crashes, a crash backtrace is printed to the standard error stream. This is what
it can look like in a build with debug symbols:

.. code-block:: none

    ================================================================
    handle_crash: Program crashed with signal 4
    Engine version: Godot Engine v4.5.beta.custom_build (6c9aa4c7d3b9b91cd50714c40eeb234874df7075)
    Dumping the backtrace. Please include this when reporting the bug to the project developer.
    [1] /lib64/libc.so.6(+0x1a070) [0x7f6e5e277070] (??:0)
    [2] godot() [0x4da3358] (/path/to/godot/core/core_bind.cpp:336 (discriminator 2))
    [3] godot() [0xdf5f2f] (/path/to/godot/modules/gdscript/gdscript.h:591)
    [4] godot() [0xbffd46] (/path/to/godot/modules/gdscript/gdscript.cpp:2065 (discriminator 1))
    [5] godot() [0x30f2ea4] (/path/to/godot/core/variant/variant.h:870)
    [6] godot() [0x550d4e1] (/path/to/godot/core/object/object.cpp:933)
    [7] godot() [0x30d996a] (/path/to/godot/scene/main/node.cpp:318 (discriminator 1))
    [8] godot() [0x3131a7f] (/path/to/godot/core/templates/hash_map.h:465)
    [9] godot() [0x424589] (/path/to/godot/platform/linuxbsd/os_linuxbsd.cpp:970)
    [10] /lib64/libc.so.6(+0x3575) [0x7f6e5e260575] (??:0)
    [11] /lib64/libc.so.6(__libc_start_main+0x88) [0x7f6e5e260628] (??:0)
    [12] godot() [0x464df5] (??:?)
    -- END OF C++ BACKTRACE --
    ================================================================
    GDScript backtrace (most recent call first):
        [0] _ready (res://test.gd:5)
    -- END OF GDSCRIPT BACKTRACE --
    ================================================================

On the other hand, without debug symbols, it will look like this instead:

.. code-block:: none

    ================================================================
    handle_crash: Program crashed with signal 4
    Engine version: Godot Engine v4.5.beta.custom_build (6c9aa4c7d3b9b91cd50714c40eeb234874df7075)
    Dumping the backtrace. Please include this when reporting the bug to the project developer.
    [1] /lib64/libc.so.6(+0x1a070) [0x7fdfaf666070] (??:0)
    [2] godot() [0x4da3358] (??:0)
    [3] godot() [0xdf5f2f] (??:0)
    [4] godot() [0xbffd46] (??:0)
    [5] godot() [0x30f2ea4] (??:0)
    [6] godot() [0x550d4e1] (??:0)
    [7] godot() [0x30d996a] (??:0)
    [8] godot() [0x3131a7f] (??:0)
    [9] godot() [0x424589] (??:0)
    [10] /lib64/libc.so.6(+0x3575) [0x7fdfaf64f575] (??:0)
    [11] /lib64/libc.so.6(__libc_start_main+0x88) [0x7fdfaf64f628] (??:0)
    [12] godot() [0x464df5] (??:0)
    -- END OF C++ BACKTRACE --
    ================================================================
    GDScript backtrace (most recent call first):
        [0] _ready (res://test.gd:5)
    -- END OF GDSCRIPT BACKTRACE --
    ================================================================

This backtrace is also logged to the file for the current session, but it is **not**
visible in the editor Output panel. Since the engine's scripting system is not running
anymore when the engine is crashing, it is not possible to access it from scripting in
the same session. However, you can still read the crash backtrace on the next session
by loading log files and searching for the crash backtrace string
(``Program crashed with signal``) using :ref:`class_FileAccess`. This allows you to access
the backtrace information even after a crash, as long as the user restarts the project
and file logging is enabled:

.. code-block:: gdscript

    # This script can be made an autoload, so that it runs when the project starts.
    extends Node

    func _ready() -> void:
      var log_dir: String = String(ProjectSettings.get_setting("debug/file_logging/log_path")).get_base_dir()
      # Get the last log file by alphabetical order.
      # Since the timestamp is featured in the file name, it should always be the most recent
      # log file that was rotated. The non-timestamped log file is for the current session,
      # so we don't want to read that one.
      var last_log_file: String = log_dir.path_join(DirAccess.get_files_at(log_dir)[-1])
      var last_long_contents: String = FileAccess.get_file_as_string(last_log_file)

      var crash_begin_idx: int = last_long_contents.find("Program crashed with signal")
      if crash_begin_idx != -1:
          print("The previous session has crashed with the following backtrace:\n")
          print(last_long_contents.substr(crash_begin_idx))

You can customize the message that appears at the top of the backtrace using the
**Debug > Settings > Crash Handler > Message** project setting. This can be used
to point to a URL or email address that users can report issues to.

Creating custom loggers
-----------------------

Since Godot 4.5, it is possible to create custom loggers. This custom logging can
be used for many purposes:

- Show an in-game console with the same messages as printed by the engine,
  without requiring other scripts to be modified.
- Report printed errors from the player's machine to a remote server.
  This can make it easier for developers to fix bugs when the game is already released,
  or during playtesting.
- Integrate a dedicated server export with monitoring platforms.

A custom logger can be registered by creating a class that inherits from :ref:`class_logger`,
then passing an instance of this class to :ref:`OS.add_logger <class_OS_method_add_logger>`,
in a script's :ref:`_init() <class_Object_private_method__init>` method. A good place to do this
is an :ref:`autoload <doc_singletons_autoload>`.

The class must define two methods: :ref:`_log_message() <class_Logger_private_method__log_message>`
and :ref:`_log_error() <class_Logger_private_method__log_error>`.

Here is a minimal working example of a custom logger, with the script added as an autoload:

.. code-block:: gdscript

    extends Node

    class CustomLogger extends Logger:
        # Note that this method is not called for messages that use
        # `push_error()` and `push_warning()`, even though these are printed to stderr.
        func _log_message(message: String, error: bool) -> void:
            # Do something with `message`.
            # `error` is `true` for messages printed to the standard error stream (stderr) with `print_error()`.
            # Note that this method will be called from threads other than the main thread, possibly at the same
            # time, so you will need to have some kind of thread-safety as part of it, like a Mutex.
            pass

        func _log_error(
                function: String,
                file: String,
                line: int,
                code: String,
                rationale: String,
                editor_notify: bool,
                error_type: int,
                script_backtraces: Array[ScriptBacktrace]
        ) -> void:
            # Do something with the error. The error text is in `rationale`.
            # See the Logger class reference for details on other parameters.
            # Note that this method will be called from threads other than the main thread, possibly at the same
            # time, so you will need to have some kind of thread-safety as part of it, like a Mutex.
            pass

    # Use `_init()` to initialize the logger as early as possible, which ensures that messages
    # printed early are taken into account. However, even when using `_init()`, the engine's own
    # initialization messages are not accessible.
    func _init() -> void:
        OS.add_logger(CustomLogger.new())

Note that to avoid infinite recursion, you cannot effectively use
:ref:`print() <class_@GlobalScope_method_print>` and its related methods in
``_log_message()``. You also can't effectively use
:ref:`push_error() <class_@GlobalScope_method_push_error>`
or :ref:`push_warning() <class_@GlobalScope_method_push_warning>` in
``_log_error()``. Attempting to do so will print a message to the same stream
as the original message. This message is not available in the custom logger,
which is what prevents infinite recursion from occurring:

.. code-block:: none

    While attempting to print a message, another message was printed:
    ...

    While attempting to print an error, another error was printed:
    ...

.. seealso::

    You can find an example of an in-game console built with a custom logger in the
    `Custom Logging demo project <https://github.com/godotengine/godot-demo-projects/tree/master/misc/custom_logging>`__.
