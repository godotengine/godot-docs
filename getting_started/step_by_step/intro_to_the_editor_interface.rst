.. _doc_intro_to_the_editor_interface:

Introduction to Godot's editor
==============================

This tutorial will run you through Godot's interface. We're going to
look at the **Project Manager, docks, workspaces** and everything you
need to know to get started with the engine.

You can `download Godot Engine here <https://godotengine.org/download/>`_.

Your first look at Godot's editor
---------------------------------

Welcome to Godot! With your project open, you should see the editor's interface
with menus along the top of the interface and docks along the far extremes of
the interface on either side of the viewport.

.. image:: img/editor_ui_intro_editor_interface_overview.png

At the top, from left to right, you can see the **main menus**, the
**workspaces**, and the **playtest buttons**.

The **FileSystem dock** is where you'll manage your project files and assets.

.. image:: img/editor_ui_intro_dock_filesystem.png

The **Scene dock** lists the active scene's content and the **Inspector**
allows for the management of the properties of a scene's content.

.. image:: img/editor_ui_intro_dock_inspector.png

In the center, you have the **Toolbar** at the top, where you'll find
tools to move, scale or lock your scene's objects. It changes as you
jump to different workspaces.

.. image:: img/editor_ui_intro_editor_02_toolbar.png

The **Bottom Panel** is the host for the debug console, the animation
editor, the audio mixer… They are wide and can take precious space.
That's why they're folded by default.

.. image:: img/editor_ui_intro_editor_03_animation_player.png

The workspaces
--------------

You can see four workspace buttons at the top: 2D, 3D, Script and
AssetLib.

You'll use the **2D workspace** for all types of games. In addition to 2D games,
the 2D workspace is where you'll build your interfaces. Press :kbd:`F1`
(or :kbd:`Alt + 1` on macOS) to access it.

.. image:: img/editor_ui_intro_editor_04_2d_workspace.png

In the **3D workspace**, you can work with meshes, lights, and design
levels for 3D games. Press :kbd:`F2` (or :kbd:`Alt + 2` on macOS) to access it.

.. image:: img/editor_ui_intro_editor_05_3d_workspace.png

Notice the perspective button under the toolbar, it opens a list of options
related to the 3D viewport.

.. image:: img/editor_ui_intro_editor_06_3d_workspace.png

.. note:: Read :ref:`doc_introduction_to_3d` for more detail about **3D workspace**.

The **Script** workspace is a complete code editor with a debugger, rich
auto-completion, and built-in code reference. Press :kbd:`F3` (or :kbd:`Alt + 3` on macOS)
to access it, and :kbd:`Shift + F1` to search the reference.

.. image:: img/editor_ui_intro_editor_06_script_workspace_expanded.png

To search for information about a class, method, property, constant, or signal
in the engine while you are writing a script, press the "Search Help" button at
the top right of the Script workspace.

.. image:: img/editor_ui_intro_script_search_documentation.png

A new window will pop up. Search for the item that you want to find information
about.

.. image:: img/editor_ui_intro_script_search_help_window.png

Click on the item you are looking for and press open. The documentation for the
item will be displayed in the script workspace.

.. image:: img/editor_ui_intro_script_class_documentation.png

Finally, the **AssetLib** is a library of free and open source add-ons, scripts
and assets to use in your projects.

Modify the interface
--------------------

Godot's interface lives in a single window. You cannot split it across
multiple screens although you can work with an external code editor like
Atom or Visual Studio Code for instance.

Move and resize docks
~~~~~~~~~~~~~~~~~~~~~

Click and drag on the edge of any dock or panel to resize it
horizontally or vertically.

.. image:: img/editor_ui_intro_editor_07.png

Click the three-dotted icon at the top of any dock to change its
location.

.. image:: img/editor_ui_intro_editor_08.png

Go to the ``Editor`` menu and ``Editor Settings`` to fine-tune the look
and feel of the editor.
