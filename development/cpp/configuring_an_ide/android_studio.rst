.. _doc_configuring_an_ide_android_studio:

Android Studio
==============

`Android Studio <https://developer.android.com/studio>`_ is a free
`JetBrains <https://www.jetbrains.com/>`_ IDE for Android development.
It has a feature-rich editor which supports Java and C/C++. It can be used to
work on Godot's core engine as well as the Android platform codebase.

Importing the project
---------------------

- From the Android Studio's welcome window select **Open an existing 
  Android Studio project**.

.. figure:: img/android_studio_setup_project_1.png
   :figclass: figure-w480
   :align: center
   
   Android Studio's welcome window.

- Navigate to ``<Godot root directory>/platform/android/java`` and select the ``settings.gradle`` file.
- Android Studio will import and index the project.
- To build the project, follow the :ref:`compiling instructions <toc-devel-compiling>`.

If you run into any issues, ask for help in one of
`Godot's community channels <https://godotengine.org/community>`__.
