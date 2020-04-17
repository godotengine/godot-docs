.. _doc_data_paths:

Data paths
==========

Path separators
---------------

For the sake of supporting as many platforms as possible, Godot only
accepts UNIX-style path separators (``/``). These work on all
platforms, including Windows.

A path like ``C:\Projects`` will become ``C:/Projects``.

Resource path
-------------

As mentioned in the :ref:`doc_command_line_tutorial`, Godot considers that
a project exists in any given folder that contains a ``project.godot``
text file, even if such file is empty.

Accessing project files can be done by opening any path with ``res://``
as a base. For example, a texture located in the root of the project
folder may be opened from the following path: ``res://some_texture.png``.

User path (persistent data)
---------------------------

While the project is running, it is a common scenario that the
resource path will be read-only, due to it being inside a package,
self-contained executable, or system-wide install location.

Storing persistent files in such scenarios should be done by using the
``user://`` prefix, for example: ``user://game_save.txt``.

On some devices (for example, mobile and consoles), this path is unique
to the project. On desktop operating systems, the engine uses the
typical ``~/.local/share/godot/app_userdata/Name`` on macOS and Linux,
and ``%APPDATA%/Name`` on Windows. ``Name`` is taken from the
application name defined in the Project Settings, but it can be
overridden on a per-platform basis using
:ref:`feature tags <doc_feature_tags>`.

Editor data paths
-----------------

The editor uses different paths for user data, user settings and cache depending
on the platform. By default, these paths are:

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
- **User settings** contains editor settings, text editor themes,
  script templates, etc.
- **Cache** contains temporary data. It can safely be removed
  when Godot is closed.

Godot complies with the `XDG Base Directory Specification
<https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html>`__
on all platforms. Environment variables can be overridden as per
the specification to change the editor (and project) data paths.

.. note:: If you use
          `Godot packaged as a Flatpak <https://flathub.org/apps/details/org.godotengine.Godot>`__,
          the editor data paths will be located in subfolders in
          ``~/.var/app/org.godotengine.Godot/``.

.. _doc_data_paths_self_contained_mode:

Self-contained mode
~~~~~~~~~~~~~~~~~~~

If you create a file called ``._sc_`` or ``_sc_`` in the same directory as the
editor binary, Godot will enable *self-contained mode*. This will make Godot
write all user data to a directory named ``editor_data/`` in the same directory
as the editor binary. This is useful to create a "portable" installation,
which can then be placed on an USB drive.

The `Steam release of Godot <https://store.steampowered.com/app/404790/>`__
uses self-contained mode by default.
