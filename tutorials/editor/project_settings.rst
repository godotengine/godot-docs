:article_outdated: True

.. _doc_project_settings:

Project Settings
================

.. warning:: This page is a work-in-progress.

This page explains how to use the Project Settings window. If you would like to access and modify 
project settings via code, see :ref:`ProjectSettings <class_ProjectSettings>`.

Godot stores the project settings in a ``project.godot`` file, a plain text file in INI format. There 
are dozens of settings you can change to control a project's execution. To simplify this process, Godot 
provides a project settings dialog, which acts as a front-end to editing a ``project.godot`` file.

To access that dialog, select Project > Project Settings.

Once the window opens, let's select a main scene. Locate the `Application > Run > Main Scene` property 
and click on the selector to select a scene from your project folder.

The project settings dialog provides a lot of options that can be saved to a ``project.godot`` file.
Initially, properties show their default values. If you change a value, a revert button appears to the 
left of its name. This means that the property is not using its default value. Clicking on it will revert 
the property to its default value.
