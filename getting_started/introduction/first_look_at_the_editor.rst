.. This page is only here to introduce the interface to the user broadly. To
   cover individual areas in greater detail, write the corresponding pages in
   the most appropriate section, and link them. E.g. the animation editor goes
   to the animation section. General pages, for instance, about the Project
   Manager, should go in the editor manual.

.. _doc_intro_to_the_editor_interface:

First look at Godot's interface
===============================

This page will give you a brief overview of Godot's interface. We're going to
look at the different main screens and docks to help you situate yourself.

.. seealso:: For a comprehensive breakdown of the editor's interface and how to
             use it, see the :ref:`Editor manual <toc-editor-interface>`.

The Project Manager
-------------------

When you launch Godot, the first window you see is the Project Manager. In the
default tab **Projects**, you can manage existing projects, import or create new
ones, and more.

.. image:: img/editor_intro_project_manager.webp

At the top of the window, there is another tab named **Asset Library**. The first
time you go to this tab you'll see a "Go Online" button. For privacy reasons, the Godot
project manager does not access the internet by default. To change this click
the "Go Online" button. You can change this option later in the settings.

Once your network mode is set to "online", you can search for demo projects in the open
source asset library, which includes many projects developed by the community:

.. image:: img/editor_intro_project_templates.webp

The Project Manager's settings can be opened using the **Settings** menu:

.. image:: img/editor_intro_settings.webp

From here, you can change the editor's language (default is the system language), interface theme, display 
scale, network mode, and also the directory naming convention.

.. seealso:: To learn the Project Manager's ins and outs, read
             :ref:`doc_project_manager`.


First look at Godot's editor
----------------------------

When you open a new or an existing project, the editor's interface appears.
Let's look at its main areas:

.. image:: img/editor_intro_editor_empty.webp

By default, along the window's top edge, it features **main menu** on the left, **workspace** switching 
buttons in the center (active workspace is highlighted), and **playtest** buttons on the right:

.. image:: img/editor_intro_top_menus.webp

Just below the workspace buttons, the opened :ref:`scenes <doc_key_concepts_overview_scenes>`
as tabs are seen. The plus (+) button right next to the tabs will add a new scene to the project.
With the button on the far right, distraction-free mode can be toggled, which maximizes or restores 
the **viewport**'s size by hiding **docks** in the interface:

.. image:: img/editor_intro_scene_selector.webp

In the center, below the scene selector is the **viewport** with its **toolbar** at the top, where you'll
find different tools to move, scale, or lock the scene's nodes (currently the 3D workspace is active):

.. image:: img/editor_intro_3d_viewport.webp

This toolbar changes based on the context and selected node. Here is the 2D toolbar:

.. image:: img/editor_intro_toolbar_2d.webp

Below is the 3D one:

.. image:: img/editor_intro_toolbar_3d.webp

.. seealso:: To learn more on workspaces, read :ref:`doc_intro_to_the_editor_interface_four_screens`.

.. seealso:: To learn more on the 3D viewport and 3D in general, read :ref:`doc_introduction_to_3d`.

On either side of the viewport sit the :ref:`doc_docks`. And at the bottom of the
window lies the :ref:`doc_bottom_panel`.

Let's look at the docks. The **FileSystem** dock lists your project files, including
scripts, images, audio samples, and more:

.. image:: img/editor_intro_filesystem_dock.webp

The **Scene** dock lists the active scene's nodes:

.. image:: img/editor_intro_scene_dock.webp

The **Inspector** allows you to edit the properties of a selected node:

.. image:: img/editor_intro_inspector_dock.webp

.. seealso:: To read more on inspector, see :ref:`doc_editor_inspector_dock`.

.. seealso:: Docks can be customized. Read more on :ref:`doc_customizing_editor_moving_resizing_docks`.

The **bottom panel**, situated below the viewport, is the host for the debug
console, the animation editor, the audio mixer, and more. They can take precious
space, that's why they're folded by default:

.. image:: img/editor_intro_bottom_panels.webp

When you click on one, it expands vertically. Below, you can see the animation editor opened:

.. image:: img/editor_intro_bottom_panel_animation.webp

Bottom panels can also be shown or hidden using the shortcuts defined in 
**Editor Settings > Shortcuts**, under the **Bottom Panels** category.

.. _doc_intro_to_the_editor_interface_four_screens:

The four main screens
---------------------

There are four main screen buttons centered at the top of the editor:
2D, 3D, Script, and Asset Library.

You'll use the **2D screen** for all types of games. In addition to 2D games,
the 2D screen is where you'll build your interfaces.

.. image:: img/editor_intro_workspace_2d.webp

In the **3D screen**, you can work with meshes, lights, and design levels for
3D games.

.. image:: img/editor_intro_workspace_3d.webp

.. note:: Read :ref:`doc_introduction_to_3d` for more detail about the **3D
          main screen**.

The **Script screen** is a complete code editor with a debugger, rich
auto-completion, and built-in code reference.

.. image:: img/editor_intro_workspace_script.webp

Finally, the **Asset Library** is a library of free and open source add-ons, scripts,
and assets to use in your projects.

.. image:: img/editor_intro_workspace_assetlib.webp

.. seealso:: You can learn more about the asset library in
             :ref:`doc_what_is_assetlib`.

Integrated class reference
--------------------------

Godot comes with a built-in class reference.

You can search for information about a class, method, property, constant, or
signal by any one of the following methods:

* Pressing :kbd:`F1` (or :kbd:`Opt + Space` on macOS, or :kbd:`Fn + F1` for laptops 
  with a :kbd:`Fn` key) anywhere in the editor.
* Clicking the "Search Help" button in the top-right of the Script main screen.
* Clicking on the Help menu and Search Help.
* :kbd:`Ctrl + Click` (:kbd:`Cmd + Click` on macOS) on a class name, function name, 
  or built-in variable in the script editor.

.. image:: img/editor_intro_search_help_button.webp

When you do any of these, a window pops up. Type to search for any item. You can
also use it to browse available objects and methods.

.. image:: img/editor_intro_search_help.webp

Double-click on an item to open the corresponding page in the script main screen.

.. image:: img/editor_intro_help_class_animated_sprite.webp

Alternatively,

* Clicking while pressing the :kbd:`Ctrl` key on a class name, function name,
  or built-in variable in the script editor.
* Right-clicking on nodes and choosing **Open Documentation** or choosing **Lookup Symbol**
  for elements in script editor will directly open their documentation.
