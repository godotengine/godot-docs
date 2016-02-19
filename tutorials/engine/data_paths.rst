.. _doc_data_paths:

Data paths
==========

Path separators
---------------

For the sake of supporting as many platforms as possible, Godot only
accepts unix style path separators (``/``). These work everywhere,
including Windows.

A path like: ``C:\Projects`` will become ``C:/Projects``.

Resource path
-------------

As mentioned before. Godot considers that a project exists at any
given folder that contains an "engine.cfg" text file, even if such
file is empty.

Accessing project files can be done by opening any path with ``res://``
as a base. For example, a texture located in the root of the project
folder may be opened from the following path: ``res://sometexture.png``.

Userdata path (persistent data)
-------------------------------

While the project is running, it is a very common scenario that the
resource path will be read-only, due to it being inside a package,
self contained executable, or system wide install location.

Storing persistent files in such scenarios should be done by using the
``user://`` prefix, for example: ``user://gamesave.txt``.

In some devices (for example, mobile ad consoles) this path is unique
for the app. Under desktop operating systems, the engine uses the
typical ~/.Name (check the project name under the settings) in OSX and
Linux, and APPDATA/Name for Windows.
