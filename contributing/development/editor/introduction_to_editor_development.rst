.. _doc_introduction_to_editor_development:

Introduction to editor development
==================================

On this page, you will learn:

- The **design decisions** behind the Godot editor.
- How to work efficiently on the Godot editor's C++ code.

This guide is aimed at current or future engine contributors.
To create editor plugins in GDScript, see :ref:`doc_making_plugins` instead.

.. seealso::

    If you are new to Godot, we recommended you to read
    :ref:`doc_godot_design_philosophy` before continuing. Since the Godot editor
    is a Godot project written in C++, much of the engine's philosophy applies
    to the editor.

Technical choices
-----------------

The Godot editor is drawn using Godot's renderer and
:ref:`UI system <doc_user_interface>`. It does *not* rely on a toolkit
such as GTK or Qt. This is similar in spirit to software like Blender.
While using toolkits makes it easier to achieve a "native" appearance, they are
also quite heavy and their licensing is not compatible with Godot's.

The editor is fully written in C++. It can't contain any GDScript or C# code.

Directory structure
-------------------

The editor's code is fully self-contained in the
`editor/ <https://github.com/godotengine/godot/tree/master/editor>`__ folder
of the Godot source repository.

Some editor functionality is also implemented via
:ref:`modules <doc_custom_modules_in_cpp>`. Some of these are only enabled in
editor builds to decrease the binary size of export templates. See the
`modules/ <https://github.com/godotengine/godot/tree/master/modules>`__ folder
in the Godot source repository.

Some important files in the editor are:

- `editor/editor_node.cpp <https://github.com/godotengine/godot/blob/master/editor/editor_node.cpp>`__:
  Main editor initialization file. Effectively the "main scene" of the editor.
- `editor/project_manager.cpp <https://github.com/godotengine/godot/blob/master/editor/project_manager.cpp>`__:
  Main Project Manager initialization file. Effectively the "main scene" of the Project Manager.
- `editor/plugins/canvas_item_editor_plugin.cpp <https://github.com/godotengine/godot/blob/master/editor/plugins/canvas_item_editor_plugin.cpp>`__:
  The 2D editor viewport and related functionality (toolbar at the top, editing modes, overlaid helpers/panels, …).
- `editor/plugins/node_3d_editor_plugin.cpp <https://github.com/godotengine/godot/blob/master/editor/plugins/node_3d_editor_plugin.cpp>`__:
  The 3D editor viewport and related functionality (toolbar at the top, editing modes, overlaid panels, …).
- `editor/plugins/node_3d_editor_gizmos.cpp <https://github.com/godotengine/godot/blob/master/editor/plugins/node_3d_editor_gizmos.cpp>`__:
  Where the 3D editor gizmos are defined and drawn.
  This file doesn't have a 2D counterpart as 2D gizmos are drawn by the nodes themselves.

Editor dependencies in ``scene/`` files
---------------------------------------

When working on an editor feature, you may have to modify files in
Godot's GUI nodes, which you can find in the ``scene/`` folder.

One rule to keep in mind is that you must **not** introduce new dependencies to
``editor/`` includes in other folders such as ``scene/``. This applies even if
you use ``#ifdef TOOLS_ENABLED``.

To make the codebase easier to follow and more self-contained, the allowed
dependency order is:

- ``editor/`` -> ``scene/`` -> ``servers/`` -> ``core/``

This means that files in ``editor/`` can depend on includes from ``scene/``,
``servers/``, and ``core/``. But, for example, while ``scene/`` can depend on includes
from ``servers/`` and ``core/``, it cannot depend on includes from ``editor/``.

Currently, there are some dependencies to ``editor/`` includes in ``scene/``
files, but
`they are in the process of being removed <https://github.com/godotengine/godot/issues/53295>`__.

Development tips
----------------

To iterate quickly on the editor, we recommend to set up a test project and
:ref:`open it from the command line <doc_command_line_tutorial>` after compiling
the editor. This way, you don't have to go through the Project Manager every
time you start Godot.
