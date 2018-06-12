.. _doc_packaging_godot:

Packaging Godot
===============

Godot has features to make it easier to distribute and to package it for application repositories.

Default behaviour
-----------------

By default, Godot stores all settings and installed templates in a per-user directory.
First Godot checks the ``APPDATA`` environment variable. If it exists, the per-user directory
is the ``Godot`` subdirectory of ``APPDATA``.
If ``APPDATA`` doesn't exist, Godot checks the ``HOME`` environment variable. The per-user
directory is then the ".godot" subdir of ``HOME``.

This meets common operating system standards.

Global template path (Unix only)
--------------------------------

The ``unix_global_settings_path`` build variable is meant for Unix/Linux distro packagers
who want to package export templates together with godot. It allows to put the export
templates on a hardcoded path.

To use it, pass the desired path via the scons ``unix_global_settings_path`` build variable
when building the editor. The export templates then live at the "templates" subdirectory
of the path specified.

Templates installed at the per-user location still override the system wide templates.

This option is only available on unix based platforms.

Self contained mode
-------------------

The self contained mode can be used to package Godot for distribution systems where it
doesn't live at a fixed location. If the editor finds a ``._sc_`` file in the directory
the executable is located in, Godot will continue in "self contained mode".
On Windows, the file name to use is ``_sc_`` (without the preceding dot).

In self contained mode, all config files are located next to the executable in a directory
called ``editor_data``. Godot doesn't read or write to the per-user location anymore.

The contents of the ``._sc_`` file (when not empty) are read with the ConfigFile api (same
format as ``project.godot``, etc). So far it can contain a list of pre-loaded project in this
format:

:: 

  [init_projects]
  list=["demos/2d/platformer", "demos/2d/isometric"]

The paths are relative to the executable location, and will be added to the file ``editor_settings.xml``
when this is created for the first time.


