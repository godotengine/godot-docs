.. _doc_configuring_an_ide_clion:

CLion
=====

`CLion <https://www.jetbrains.com/clion/>`_ is a commercial IDE for C++.
It requires a ``CMakeLists.txt`` file as a project file, which is problematic
for Godot which uses the SCons buildsystem instead of CMake.
However, there is a ``CMakeLists.txt`` configuration for
:ref:`Android Studio <doc_configuring_an_ide_android_studio>` which can also
be used by CLion.

- If you've already opened another project, choose **File > Open** at the top of
  the CLion window. Otherwise, choose the option to import an existing project
  in the Welcome window.
- Navigate to your Godot Git clone then select the folder
  ``platform/android/java/lib`` - the ``CMakeLists.txt`` file is located there.
  Select the folder (*not* the ``CMakeLists.txt file``), then click **OK**.

.. image:: img/clion_1_open.png

- If this popup window appears, select **This Window** to open the project:

.. image:: img/clion_2_this_window.png

- Choose **Tools > CMake >Change Project Root** and select the root Godot folder.

.. image:: img/clion_3_change_project_root.png

- You should be now be able to see all the project files. Autocomplete should
  work once the project has finished indexing.

If you run into any issues, ask for help in one of
`Godot's community channels <https://godotengine.org/community>`__.
