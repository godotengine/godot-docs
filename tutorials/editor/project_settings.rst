:article_outdated: True

.. _doc_project_settings:

Project Settings
================

This page explains how to use the Project Settings window. If you would like to access and modify project settings via code, see :ref:`ProjectSettings <class_ProjectSettings>`.

Godot stores the project settings in a project.godot file, a plain text file in INI format. There are dozens of settings you can change to control a project's execution. To simplify this process, Godot provides a project settings dialog, which acts as a front-end to editing a project.godot file.

To access that dialog, select Project -> Project Settings.

Once the window opens, let's select a main scene. Locate the `Application/Run/Main Scene` property and click on it to select 'hello.tscn'.

The project settings dialog provides a lot of options that can be saved to a project.godot file and shows their default values. If you change a value, a tick appears to the left of its name. This means that the property will be saved in the project.godot file and remembered.
