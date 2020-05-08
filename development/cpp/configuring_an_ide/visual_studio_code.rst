.. _doc_configuring_an_ide_vscode:

Visual Studio Code
==================

Visual Studio Code is a free cross-platform IDE (not to be confused with
:ref:`doc_configuring_an_ide_vs`). You can get it
`from Microsoft <https://code.visualstudio.com/>`__.


- Make sure the C/C++ extension is installed. You can find instructions in
  the `documentation <https://code.visualstudio.com/docs/languages/cpp>`_.
- Open the cloned Godot folder in Visual Studio Code with
  **File > Open Folder...**.

In order to build the project, you need two configuration files:
``launch.json`` and ``tasks.json``. To create them:

- Open the **Debug** view by pressing :kbd:`Ctrl + Shift + D` and select the
  cogwheel with an orange dot:

.. image:: img/vscode_1_create_launch.json.png

- Select **C++ (GDB/LLDB)** (it might be named differently on macOS or Windows).

- Update ``launch.json`` to match:

.. image:: img/vscode_2_launch.json.png

If you're following this guide on macOS or Windows, you will have to adjust
``godot.linuxbsd.tools.64`` accordingly.

- Create a ``tasks.json`` file by starting the Debug process with :kbd:`F5`.
  Visual Studio Code will show a dialog with a **Configure Task** button.
  Choose it and select **Create tasks.json file from template**, then select **Others**.

- Update ``tasks.json`` to match:

.. image:: img/vscode_3_tasks.json.png

If you're following this guide on macOS or Windows, you will have to adjust
``platform=linuxbsd`` accordingly.

- You can now start the Debug process again to test that everything works.
- If the build phase fails, check the console for hints. On Linux, it's most
  likely due to missing dependencies. Check :ref:`doc_compiling_for_linuxbsd`.

If you run into any issues, ask for help in one of
`Godot's community channels <https://godotengine.org/community>`__.
