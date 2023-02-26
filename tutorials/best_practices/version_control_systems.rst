:article_outdated: True

.. _doc_version_control_systems:

Version Control Systems
=======================

Introduction
------------

Godot aims to be VCS friendly and generate mostly readable and mergeable files.
Godot also supports the use of version control systems in the editor itself.
However, VCS in the editor requires a plugin for the specific VCS you are using.
VCS can be setup or shut down in the editor under **Project > Version Control**.

.. image:: img/version_control_menu.png

Official Git plugin
-------------------

Using Git from inside the editor is supported with an official plugin.
You can find the latest releases
`here <https://github.com/godotengine/godot-git-plugin/releases>`__. Documentation on how to use the Git
plugin can be found
`here <https://github.com/godotengine/godot-git-plugin/wiki>`__.

Files to exclude from VCS
-------------------------

There are some files and folders Godot automatically creates. You should add them to your VCS ignore:

- ``.godot/``: This folder stores various project cache data. ``.godot/imported/`` stores
  all the files the engine imports automatically based on your source assets and their
  import flags. ``.godot/editor/`` holds data regarding the editor state, such as currently
  opened script files, and recently used nodes.
- ``*.translation``: These files are binary imported translations generated from CSV files.
- ``export_presets.cfg``: This file contains all the export presets for the
  project, including sensitive information such as Android keystore credentials.
- ``.mono/``: This folder stores automatically-generated Mono files. It only exists
  in projects that use the Mono version of Godot.

.. tip::

    Save `this .gitignore file <https://raw.githubusercontent.com/github/gitignore/master/Godot.gitignore>`__
    in your project's root folder to set up file exclusions automatically.

Working with Git on Windows
---------------------------

Most Git for Windows clients are configured with the ``core.autocrlf`` set to ``true``.
This can lead to files unnecessarily being marked as modified by Git due to their line endings being converted automatically.
It is better to set this option as::

    git config --global core.autocrlf input

Known issues
------------

**Always close the editor** before running ``git pull``! Otherwise, you may
`lose data if you synchronize files while the editor is open <https://github.com/godotengine/godot/issues/20250>`__.
