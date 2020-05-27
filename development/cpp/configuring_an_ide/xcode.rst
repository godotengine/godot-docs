.. _doc_configuring_an_ide_xcode:

Xcode
=====

`Xcode <https://developer.apple.com/xcode>`_ is a free macOS-only IDE. You can 
download it from the Mac App Store.

Importing the project
---------------------

- From Xcode's main screen create a new project using the **Other > External Build System** template.

.. figure:: img/xcode_1_create_external_build_project.png
   :figclass: figure-w480
   :align: center

- Open your build targets from the **Targets** section and select the **Info** tab.
- Fill out the form with the following settings:

  +------------+------------------------------------------------------------------------------+
  | Build Tool | A full path to the **scons** executable, e.g. **/usr/local/bin/scons**       |
  +------------+------------------------------------------------------------------------------+
  | Arguments  | See :ref:`doc_introduction_to_the_buildsystem` for a full list of arguments. |
  +------------+------------------------------------------------------------------------------+
  | Directory  | A full path to the Godot root folder                                         |
  +------------+------------------------------------------------------------------------------+

.. figure:: img/xcode_2_configure_scons.png
   :figclass: figure-w480
   :align: center

- Add a Command Line Tool target which will be used for indexing the project by
  choosing **File > New > Target...**.

.. figure:: img/xcode_3_add_new_target.png
   :figclass: figure-w480
   :align: center

- Select **OS X > Application > Command Line Tool**.

.. figure:: img/xcode_4_select_command_line_target.png
   :figclass: figure-w480
   :align: center

.. note:: Name it something so you know not to compile with this target (e.g. ``GodotXcodeIndex``).

- For this target open the **Build Settings** tab and look for **Header Search Paths**.
- Set **Header Search Paths** to the absolute path to the Godot root folder. You need to
  include subdirectories as well. To achieve that, add two two asterisks (``**``) to the 
  end of the path, e.g. ``/Users/me/repos/godot-source/**``.

- Add the Godot source to the project by dragging and dropping it into the project file browser.
- Uncheck **Create external build system project**.

.. figure:: img/xcode_5_after_add_godot_source_to_project.png
   :figclass: figure-w480
   :align: center

- Next select **Create groups** for the **Added folders** option and check *only* 
  your command line indexing target in the **Add to targets** section.

.. figure:: img/xcode_6_after_add_godot_source_to_project_2.png
   :figclass: figure-w480
   :align: center

- Xcode will now index the files. This may take a few minutes.
- Once Xcode is done indexing, you should have jump-to-definition,
  autocompletion, and full syntax highlighting.

Debugging the project
---------------------

To enable debugging support you need to edit the external build target's build and run schemes.

- Open the scheme editor of the external build target.
- Locate the **Build > Post Actions** section.
- Add a new script run action
- Under **Provide build settings from** select your project. This allows to reference 
  the project directory within the script.
- Create a script that will give the binary a name that Xcode can recognize, e.g.:

.. code-block:: shell

  ln -f ${PROJECT_DIR}/godot/bin/godot.osx.tools.64 ${PROJECT_DIR}/godot/bin/godot

.. figure:: img/xcode_7_setup_build_post_action.png
   :figclass: figure-w480
   :align: center

- Build the external build target.

- Open the scheme editor again and select **Run**.

.. figure:: img/xcode_8_setup_run_scheme.png
   :figclass: figure-w480
   :align: center

- Set the **Executable** to the file you linked in your post-build action script.
- Check **Debug executable**.
- You can add two arguments on the **Arguments** tab:
  the ``-e`` flag opens the editor instead of the project manager, and the ``--path`` argument
  tells the executable to open the specified project (must be provided as an *absolute* path 
  to the project root, not the ``project.godot`` file).

To check that everything is working, put a breakpoint in ``platform/osx/godot_main_osx.mm`` and
run the project.

If you run into any issues, ask for help in one of
`Godot's community channels <https://godotengine.org/community>`__.
