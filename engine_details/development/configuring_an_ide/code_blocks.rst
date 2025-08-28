.. _doc_configuring_an_ide_code_blocks:

Code::Blocks
============

`Code::Blocks <https://codeblocks.org/>`_ is a free, open-source, cross-platform IDE.

Creating a new project
----------------------

From Code::Blocks' main screen, click **Create a new project** or select **File > New > Project...**.

.. figure:: img/code_blocks_file_new_project.png
   :figclass: figure-w480
   :align: center

In the **New from template** window, from **Projects**, select **Empty project**, and click **Go**.

.. figure:: img/code_blocks_new_empty_project.png
   :figclass: figure-w480
   :align: center

Click Next, to pass the welcome to the new empty project wizard.

.. figure:: img/code_blocks_wizard_welcome.png
   :figclass: figure-w480
   :align: center

The project file should be created in the root of the cloned project folder. To achieve this, first, ensure that the **Project title** is the same as the folder name that Godot was cloned into. Unless you cloned the project into a folder with a different name, this will be ``godot``.

Second, ensure that the **Folder to create project in** is the folder you ran the Git clone command from, not the ``godot`` project folder. Confirm that the **Resulting filename** field will create the project file in the root of the cloned project folder.

.. figure:: img/code_blocks_project_title_and_location.png
   :figclass: figure-w480
   :align: center

The compiler and configuration settings are managed through **SCons** and will be configured later. However, it's worth deselecting the **Create "Release" configuration** option; so only a single build target is created before clicking **Finish**.

.. figure:: img/code_blocks_compiler_and_configuration.png
   :figclass: figure-w480
   :align: center

Configuring the build
---------------------

The first step is to change the project properties. Right-click on the new project and select **Properties...**.

.. figure:: img/code_blocks_open_properties.png
   :figclass: figure-w480
   :align: center

Check the **This is a custom Makefile** property. Click OK to save the changes.

.. figure:: img/code_blocks_project_properties.png
   :figclass: figure-w480
   :align: center

The next step is to change the build options. Right-click on the new project and select **Build Options...**.

.. figure:: img/code_blocks_open_build_options.png
   :figclass: figure-w480
   :align: center

Select the **"Make" commands** tab and remove all the existing commands for all the build targets. For each build target enter the **SCons** command for creating the desired build in the **Build project/target** field. The minimum is ``scons``. For details on the **SCons** build options, see :ref:`doc_introduction_to_the_buildsystem`. It's also useful to add the ``scons --clean`` command in the **Clean project/target** field to the project's default commands.

If you're using Windows, all the commands need to be preceded with ``cmd /c`` to initialize the command interpreter.

.. figure:: img/code_blocks_scons_minimum.png
   :figclass: figure-w480
   :align: center

.. figure:: img/code_blocks_scons_clean.png
   :figclass: figure-w480
   :align: center

Windows example:

.. figure:: img/code_blocks_scons_windows.png
   :figclass: figure-w480
   :align: center

Code::Blocks should now be configured to build Godot; so either select **Build > Build**, click the gear button, or press :kbd:`Ctrl + F9`.

Configuring the run
-------------------

Once **SCons** has successfully built the desired target, reopen the project **Properties...** and select the **Build targets** tab. In the **Output filename** field, browse to the ``bin`` folder and select the compiled file.

Deselect the **Auto-generate filename prefix** and **Auto-generate filename extension** options.

.. figure:: img/code_blocks_build_targets.png
   :figclass: figure-w480
   :align: center

Code::Blocks should now be configured to run your compiled Godot executable; so either select **Build > Run**, click the green arrow button, or press :kbd:`Ctrl + F10`.

There are two additional points worth noting. First, if required, the **Execution working dir** field can be used to test specific projects, by setting it to the folder containing the ``project.godot`` file. Second, the **Build targets** tab can be used to add and remove build targets for working with and creating different builds.

Adding files to the project
---------------------------

To add all the Godot code files to the project, right-click on the new project and select **Add files recursively...**.

.. figure:: img/code_blocks_add_files_recursively.png
   :figclass: figure-w480
   :align: center

It should automatically select the project folder; so simply click **Open**. By default, all code files are included, so simply click **OK**.

.. figure:: img/code_blocks_select_files.png
   :figclass: figure-w480
   :align: center

Code style configuration
------------------------

Before editing any files, remember that all code needs to comply with the `code style guidelines <https://contributing.godotengine.org/en/latest/engine/guidelines/code_style.html>`__. One important difference with Godot is the use of tabs for indents. Therefore, the key default editor setting that needs to be changed in Code::Blocks is to enable tabs for indents. This setting can be found by selecting **Settings > Editor**.

.. figure:: img/code_blocks_update_editor_settings.png
   :figclass: figure-w480
   :align: center

Under **General Settings**, on the **Editor Settings** tab, under **Tab Options** check **Use TAB character**.

.. figure:: img/code_block_use_tab_character.png
   :figclass: figure-w480
   :align: center

That's it. You're ready to start contributing to Godot using the Code::Blocks IDE. Remember to save the project file and the **Workspace**. If you run into any issues, ask for help in one of `Godot's community channels <https://godotengine.org/community>`__.
