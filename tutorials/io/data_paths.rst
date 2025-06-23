.. _doc_data_paths:

File paths in Godot projects
============================

This page explains how file paths work inside Godot projects. You will learn how
to access paths in your projects using the ``res://`` and ``user://`` notations,
and where Godot stores project and editor files on your and your users' systems.

Path separators
---------------

To make supporting multiple platforms easier, Godot uses **UNIX-style path
separators** (forward slash ``/``). These work on all platforms, **including
Windows**.

Instead of writing paths like ``C:\Projects\Game``, in Godot, you should write
``C:/Projects/Game``.

Windows-style path separators (backward slash ``\``) are also supported in some
path-related methods, but they need to be doubled (``\\``), as ``\`` is normally
used as an escape for characters with a special meaning.

This makes it possible to work with paths returned by other Windows
applications. We still recommend using only forward slashes in your own code to
guarantee that everything will work as intended.

.. tip::

    The String class offers over a dozen methods to work with strings that represent file paths:

    - :ref:`String.filecasecmp_to() <class_String_method_filecasecmp_to>`
    - :ref:`String.filenocasecmp_to() <class_String_method_filenocasecmp_to>`
    - :ref:`String.get_base_dir() <class_String_method_get_base_dir>`
    - :ref:`String.get_basename() <class_String_method_get_basename>`
    - :ref:`String.get_extension() <class_String_method_get_extension>`
    - :ref:`String.get_file() <class_String_method_get_file>`
    - :ref:`String.is_absolute_path() <class_String_method_is_absolute_path>`
    - :ref:`String.is_relative_path() <class_String_method_is_relative_path>`
    - :ref:`String.is_valid_filename() <class_String_method_is_valid_filename>`
    - :ref:`String.path_join() <class_String_method_path_join>`
    - :ref:`String.simplify_path() <class_String_method_simplify_path>`
    - :ref:`String.validate_filename() <class_String_method_validate_filename>`

Accessing files in the project folder (``res://``)
--------------------------------------------------

Godot considers that a project exists in any folder that contains a
``project.godot`` text file, even if the file is empty. The folder that contains
this file is your project's root folder.

You can access any file relative to it by writing paths starting with
``res://``, which stands for resources. For example, you can access an image
file ``character.png`` located in the project's root folder in code with the
following path: ``res://character.png``.

Accessing persistent user data (``user://``)
--------------------------------------------

To store persistent data files, like the player's save or settings, you want to
use ``user://`` instead of ``res://`` as your path's prefix. This is because
when the game is running, the project's file system will likely be read-only.

The ``user://`` prefix points to a different directory on the user's device.
Unlike ``res://``, the directory pointed at by ``user://`` is created
automatically and *guaranteed* to be writable to, even in an exported project.

The location of the ``user://`` folder depends on what is configured in the
Project Settings:

- By default, the ``user://`` folder is created within Godot's
  :ref:`editor data path <doc_data_paths_editor_data_paths>` in the
  ``app_userdata/[project_name]`` folder. This is the default so that prototypes
  and test projects stay self-contained within Godot's data folder.
- If :ref:`application/config/use_custom_user_dir <class_ProjectSettings_property_application/config/use_custom_user_dir>`
  is enabled in the Project Settings, the ``user://`` folder is created **next
  to** Godot's editor data path, i.e. in the standard location for applications
  data.

  * By default, the folder name will be inferred from the project name, but it
    can be further customized with
    :ref:`application/config/custom_user_dir_name <class_ProjectSettings_property_application/config/custom_user_dir_name>`.
    This path can contain path separators, so you can use it e.g. to group
    projects of a given studio with a ``Studio Name/Game Name`` structure.

On desktop platforms, the actual directory paths for ``user://`` are:

+---------------------+------------------------------------------------------------------------------+
| Type                | Location                                                                     |
+=====================+==============================================================================+
| Default             | | Windows: ``%APPDATA%\Godot\app_userdata\[project_name]``                   |
|                     | | macOS: ``~/Library/Application Support/Godot/app_userdata/[project_name]`` |
|                     | | Linux: ``~/.local/share/godot/app_userdata/[project_name]``                |
+---------------------+------------------------------------------------------------------------------+
| Custom dir          | | Windows: ``%APPDATA%\[project_name]``                                      |
|                     | | macOS: ``~/Library/Application Support/[project_name]``                    |
|                     | | Linux: ``~/.local/share/[project_name]``                                   |
+---------------------+------------------------------------------------------------------------------+
| Custom dir and name | | Windows: ``%APPDATA%\[custom_user_dir_name]``                              |
|                     | | macOS: ``~/Library/Application Support/[custom_user_dir_name]``            |
|                     | | Linux: ``~/.local/share/[custom_user_dir_name]``                           |
+---------------------+------------------------------------------------------------------------------+

``[project_name]`` is based on the application name defined in the Project Settings, but
you can override it on a per-platform basis using :ref:`feature tags <doc_feature_tags>`.

On mobile platforms, this path is unique to the project and is not accessible
by other applications for security reasons.

On HTML5 exports, ``user://`` will refer to a virtual filesystem stored on the
device via IndexedDB. (Interaction with the main filesystem can still be performed
through the :ref:`JavaScriptBridge <class_JavaScriptBridge>` singleton.)

File logging
------------

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
:ref:`Debugging symbols <doc_introduction_to_the_buildsystem_debugging_symbols>`.
for guidance on compiling binaries with debugging symbols enabled.

.. note::

    Log files for :ref:`print<class_@GlobalScope_method_print>`
    statements are updated when standard output is *flushed* by the engine.
    Standard output is flushed on every print in debug builds only. In projects that
    are exported in release mode, standard output is only flushed when the project exits
    or crashes to improve performance, especially if the project is often printing
    text to standard output.

    On the other hand, the standard error stream
    (used by :ref:`printerr<class_@GlobalScope_method_printerr>`,
    :ref:`push_error<class_@GlobalScope_method_push_error>` and
    :ref:`push_warning<class_@GlobalScope_method_push_warning>`) is always
    flushed on every print, even in projects exported in release mode.

    For some use cases like dedicated servers, it can be preferred to have release
    builds always flush stdout on print, so that logging services like journald can
    collect logs while the process is running. This can be done by enabling
    ``application/run/flush_stdout_on_print`` in the Project Settings.

Converting paths to absolute paths or "local" paths
---------------------------------------------------

You can use :ref:`ProjectSettings.globalize_path() <class_ProjectSettings_method_globalize_path>`
to convert a "local" path like ``res://path/to/file.txt`` to an absolute OS path.
For example, :ref:`ProjectSettings.globalize_path() <class_ProjectSettings_method_globalize_path>`
can be used to open "local" paths in the OS file manager
using :ref:`OS.shell_open() <class_OS_method_shell_open>` since it only accepts
native OS paths.

To convert an absolute OS path to a "local" path starting with ``res://``
or ``user://``, use :ref:`ProjectSettings.localize_path() <class_ProjectSettings_method_localize_path>`.
This only works for absolute paths that point to files or folders in your
project's root or ``user://`` folders.

.. _doc_data_paths_editor_data_paths:

Editor data paths
-----------------

The editor uses different paths for editor data, editor settings, and cache,
depending on the platform. By default, these paths are:

+-----------------+---------------------------------------------------+
| Type            | Location                                          |
+=================+===================================================+
| Editor data     | | Windows: ``%APPDATA%\Godot\``                   |
|                 | | macOS: ``~/Library/Application Support/Godot/`` |
|                 | | Linux: ``~/.local/share/godot/``                |
+-----------------+---------------------------------------------------+
| Editor settings | | Windows: ``%APPDATA%\Godot\``                   |
|                 | | macOS: ``~/Library/Application Support/Godot/`` |
|                 | | Linux: ``~/.config/godot/``                     |
+-----------------+---------------------------------------------------+
| Cache           | | Windows: ``%TEMP%\Godot\``                      |
|                 | | macOS: ``~/Library/Caches/Godot/``              |
|                 | | Linux: ``~/.cache/godot/``                      |
+-----------------+---------------------------------------------------+

- **Editor data** contains export templates and project-specific data.
- **Editor settings** contains the main editor settings configuration file as
  well as various other user-specific customizations (editor layouts, feature
  profiles, script templates, etc.).
- **Cache** contains data generated by the editor, or stored temporarily.
  It can safely be removed when Godot is closed.

Godot complies with the `XDG Base Directory Specification
<https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html>`__
on Linux/\*BSD. You can override the ``XDG_DATA_HOME``, ``XDG_CONFIG_HOME`` and
``XDG_CACHE_HOME`` environment variables to change the editor and project data
paths.

.. note:: If you use `Godot packaged as a Flatpak
          <https://flathub.org/apps/details/org.godotengine.Godot>`__, the
          editor data paths will be located in subfolders in
          ``~/.var/app/org.godotengine.Godot/``.

.. _doc_data_paths_self_contained_mode:

Self-contained mode
~~~~~~~~~~~~~~~~~~~

If you create a file called ``._sc_`` or ``_sc_`` in the same directory as the
editor binary (or in `MacOS/Contents/` for a macOS editor .app bundle), Godot
will enable *self-contained mode*.
This mode makes Godot write all editor data, settings, and cache to a directory
named ``editor_data/`` in the same directory as the editor binary.
You can use it to create a portable installation of the editor.

The `Steam release of Godot <https://store.steampowered.com/app/404790/>`__ uses
self-contained mode by default.

.. UPDATE: Not supported yet. When self-contained mode is supported in exported
.. projects, remove or update this note.

.. note::

    Self-contained mode is not supported in exported projects yet.
    To read and write files relative to the executable path, use
    :ref:`OS.get_executable_path() <class_OS_method_get_executable_path>`.
    Note that writing files in the executable path only works if the executable
    is placed in a writable location (i.e. **not** Program Files or another
    directory that is read-only for regular users).
