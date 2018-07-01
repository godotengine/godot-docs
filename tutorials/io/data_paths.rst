.. _doc_data_paths:

Data paths
==========

Path separators
---------------

For the sake of supporting as many platforms as possible, Godot only
accepts UNIX-style path separators (``/``). These work on all
platforms including Windows.

A path like ``C:\Projects`` will become ``C:/Projects``.

Resource path
-------------

As mentioned before, Godot considers that a project exists in any
given folder that contains a ``project.godot`` text file, even if such
file is empty.

Accessing project files can be done by opening any path with ``res://``
as a base. For example, a texture located in the root of the project
folder may be opened from the following path: ``res://some_texture.png``.

User path (persistent data)
-------------------------------

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
