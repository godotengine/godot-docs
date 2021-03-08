.. _doc_data_paths:

File paths in Godot projects
============================

This page explains how file paths work inside Godot projects. You will learn how
to access paths in your projects using the ``res://`` and ``user://`` notations
and where Godot stores user files on your hard-drive.

Path separators
---------------

To as many platforms as possible, Godot only accepts UNIX-style path separators
(``/``). These work on all platforms, including Windows.

Instead of writing paths like ``C:\Projects``, in Godot, you should write
``C:/Projects``.

Accessing files in the project folder
-------------------------------------

Godot considers that a project exists in any folder that contains a
``project.godot`` text file, even if the file is empty. The folder that contains
this file is your project's root folder.

You can access any file relative to it by writing paths starting with
``res://``, which stands for resources. For example, you can access an image
file ``character.png`` located in the project's root folder in code with the
following path: ``res://some_texture.png``.

Accessing persistent user data
------------------------------

To store persistent data files, like the player's save or settings, you want to
use ``user://`` instead of ``res://`` as your path's prefix. This is because
when the game is running, the project's file system will likely be read-only.

The ``user://`` prefix points to a different directory on the user's device. On
mobile and consoles, this path is unique to the project. On desktop, the engine
stores user files in ``~/.local/share/godot/app_userdata/Name`` on
Linux, ``~/Library/Application Support/Godot/app_userdata/Name`` on macOS (since Catalina) and ``%APPDATA%/Name`` on Windows. ``Name`` is based on the application
name defined in the Project Settings, but you can override it on a per-platform
basis using :ref:`feature tags <doc_feature_tags>`.

Converting paths to absolute paths or "local" paths
---------------------------------------------------

You can use :ref:`ProjectSettings.globalize_path() <class_ProjectSettings_method_globalize_path>`
to convert a "local" path like ``res://path/to/file.txt`` to an absolute OS path.
For example, :ref:`ProjectSettings.globalize_path() <class_ProjectSettings_method_globalize_path>`
can be used to open "local" paths in the OS file manager
using :ref:`OS.shell_open() <class_OS_method_shell_open>` since it only accepts
native OS paths.

To convert an absolute OS path to a "local" path starting with ``res://``, use
:ref:`ProjectSettings.localize_path() <class_ProjectSettings_method_localize_path>`.

Editor data paths
-----------------

The editor uses different paths for user data, user settings, and cache,
depending on the platform. By default, these paths are:

+---------------+---------------------------------------------------+
| Type          | Location                                          |
+===============+===================================================+
| User data     | - Windows: ``%APPDATA%\Godot\``                   |
|               | - macOS: ``~/Library/Application Support/Godot/`` |
|               | - Linux: ``~/.local/share/godot/``                |
+---------------+---------------------------------------------------+
| User settings | - Windows: ``%APPDATA%\Godot\``                   |
|               | - macOS: ``~/Library/Application Support/Godot/`` |
|               | - Linux: ``~/.config/godot/``                     |
+---------------+---------------------------------------------------+
| Cache         | - Windows: ``%TEMP%\Godot\``                      |
|               | - macOS: ``~/Library/Caches/Godot/``              |
|               | - Linux: ``~/.cache/godot/``                      |
+---------------+---------------------------------------------------+

- **User data** contains export templates and project-specific data.
- **User settings** contains editor settings, text editor themes, script
  templates, etc.
- **Cache** contains temporary data. It can safely be removed when Godot is
  closed.

Godot complies with the `XDG Base Directory Specification
<https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html>`__
on all platforms. You can override environment variables following the
specification to change the editor and project data paths.

.. note:: If you use `Godot packaged as a Flatpak
          <https://flathub.org/apps/details/org.godotengine.Godot>`__, the
          editor data paths will be located in subfolders in
          ``~/.var/app/org.godotengine.Godot/``.

.. _doc_data_paths_self_contained_mode:

Self-contained mode
~~~~~~~~~~~~~~~~~~~

If you create a file called ``._sc_`` or ``_sc_`` in the same directory as the
editor binary, Godot will enable *self-contained mode*. This mode makes Godot
write all user data to a directory named ``editor_data/`` in the same directory
as the editor binary. You can use it to create a portable installation of the
editor.

The `Steam release of Godot <https://store.steampowered.com/app/404790/>`__ uses
self-contained mode by default.
