.. _doc_configuring_an_ide_xcode:

Xcode
=====

Xcode is a free macOS-only IDE. You can download it from the Mac App Store.

Project setup
-------------

- Create an Xcode external build project anywhere.

.. image:: img/xcode_1_create_external_build_project.png

Go to the build target's **Info** tab, then:

- Set **Build Tool** to the full path to SCons.
- Set **Arguments** to something like
  ``platform=osx tools=yes bits=64 target=debug``.
- Set **Directory** to the path to Godot's source folder.
- You may uncheck **Pass build settings in environment**.

.. image:: img/xcode_2_configure_scons.png

Add a Command Line Tool target which will be used for indexing the project:

- In Xcode's menu, choose **File > New > Target...** and add a new Xcode
  command line tool target.

.. image:: img/xcode_3_add_new_target.png

.. image:: img/xcode_4_select_command_line_target.png

- Name it something so you know not to compile with this target (e.g. ``GodotXcodeIndex``).
- Goto the newly created target's **Build Settings** tab and look for **Header Search Paths**.
- Set **Header Search Paths** to the absolute path to Godot's source folder.
- Make it recursive by adding two asterisks (``**``) to the end of the path,
  e.g. ``/Users/me/repos/godot-source/**``.

Add the Godot source to the project:

- Drag and drop Godot source into the project file browser.
- Uncheck **Create external build system project**.

.. image:: img/xcode_5_after_add_godot_source_to_project.png

- Click **Next**.
- Select **Create groups**.

.. image:: img/xcode_6_after_add_godot_source_to_project_2.png

- Check *only* your command line indexing target in the
  **Add to targets** section.
- Click finish. Xcode will now index the files. This may take a few minutes.
- Once Xcode is done indexing, you should have jump-to-definition,
  autocompletion, and full syntax highlighting.

Scheme setup
------------

To enable debugging support, edit the external build target's build scheme:

- Open the scheme editor of the external build target.
- Expand the **Build** menu.
- Goto **Post Actions**.
- Add a new script run action, select your project in **Provide build settings from**
  as this allows you to use the``${PROJECT_DIR}`` variable.

.. image:: img/xcode_7_setup_build_post_action.png

- Write a script that gives the binary a name that Xcode will recognize, such as:
  ``ln -f ${PROJECT_DIR}/godot/bin/godot.osx.tools.64 ${PROJECT_DIR}/godot/bin/godot``
- Build the external build target.

Edit the external build target's Run scheme:

- Open the scheme editor again.
- Click **Run**.

.. image:: img/xcode_8_setup_run_scheme.png

- Set the **Executable** to the file you linked in your post-build action script.
- Check **Debug executable** if it isn't checked already.
- You can go to **Arguments** tab and specify the full path to a
  ``project.godot`` file to debug the editor instead of the project manager.
  Alternatively, use ``--path`` to point to a project *folder* which will be
  run directly (instead of opening the editor).

Test the Run scheme:

- Set a breakpoint in ``platform/osx/godot_main_osx.mm``.
- If all goes well, it should break at the specified breakpoint.

If you run into any issues, ask for help in one of
`Godot's community channels <https://godotengine.org/community>`__.
