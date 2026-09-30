.. _doc_upgrading_to_godot_4.8:

Upgrading from Godot 4.7 to Godot 4.8
=====================================

For most games and apps made with 4.7 it should be relatively safe to migrate to 4.8.
This page intends to cover everything you need to pay attention to when migrating
your project.

Breaking changes
----------------

If you are migrating from 4.7 to 4.8, the breaking changes listed here might
affect you. Changes are grouped by areas/systems.

This article indicates whether each breaking change affects GDScript and whether
the C# breaking change is *binary compatible* or *source compatible*:

- **Binary compatible** - Existing binaries will load and execute successfully without
  recompilation, and the runtime behavior won't change.
- **Source compatible** - Source code will compile successfully without changes when
  upgrading Godot.

GDScript
~~~~~~~~

========================================================================================================================  ===================  ====================  ====================  ============
Change                                                                                                                    GDScript Compatible  C# Binary Compatible  C# Source Compatible  Introduced
========================================================================================================================  ===================  ====================  ====================  ============
**GDScriptTextDocument**
Method ``codeLens`` removed                                                                                               |❌|                 |❌|                  |❌|                  `GH-114533`_
Method ``colorPresentation`` removed                                                                                      |❌|                 |❌|                  |❌|                  `GH-114533`_
Method ``foldingRange`` removed                                                                                           |❌|                 |❌|                  |❌|                  `GH-114533`_
========================================================================================================================  ===================  ====================  ====================  ============

.. note::

    The methods were stubs that were never implemented, so they were removed.

Rendering
~~~~~~~~~

=========================================================================================================================  ===================  ====================  ====================  ============
Change                                                                                                                     GDScript Compatible  C# Binary Compatible  C# Source Compatible  Introduced
=========================================================================================================================  ===================  ====================  ====================  ============
**DisplayServer**
Method ``get_display_cutouts`` adds new ``screen`` optional parameter                                                      |✔️|                 |✔️ with compat|      |✔️|                  `GH-119196`_
Method ``get_display_safe_area`` adds new ``screen`` optional parameter                                                    |✔️|                 |✔️ with compat|      |✔️|                  `GH-119196`_
Signal ``orientation_changed`` changes ``orientation`` parameter type from ``int`` to ``DisplayServer.SensorOrientation``  |✔️|                 |❌|                  |❌|                  `GH-121895`_
**Image**
Method ``compress`` replaces parameter ``astc_format`` with ``profile``                                                    |❌|                 |✔️ with compat|      |✔️ with compat|      `GH-115003`_
Method ``compress_from_channels`` replaces parameter ``astc_format`` with ``profile``                                      |❌|                 |✔️ with compat|      |✔️ with compat|      `GH-115003`_
Method ``generate_mipmaps`` adds new ``preserve_alpha_test_coverage`` optional parameter                                   |✔️|                 |✔️ with compat|      |✔️|                  `GH-104289`_
Method ``generate_mipmaps`` adds new ``alpha_test_threshold`` optional parameter                                           |✔️|                 |✔️ with compat|      |✔️|                  `GH-104289`_
**MovieWriter**
Method ``_write_frame`` changes ``audio_frame_block`` parameter type from ``const void*`` to ``const int32_t*``            N/A                  N/A                   N/A                   `GH-120749`_
**RenderingDevice**
Method ``texture_create_shared_from_slice`` adds new ``layers`` optional parameter                                         |✔️|                 |✔️ with compat|      |✔️|                  `GH-121937`_
=========================================================================================================================  ===================  ====================  ====================  ============

.. note::

    The method ``_write_frame`` has pointer parameters so it's not exposed to scripting.

Animation
~~~~~~~~~

========================================================================================================================  ===================  ====================  ====================  ============
Change                                                                                                                    GDScript Compatible  C# Binary Compatible  C# Source Compatible  Introduced
========================================================================================================================  ===================  ====================  ====================  ============
**AnimationNodeBlendSpace2D**
Property ``triangles`` removed                                                                                            |✔️|                 |❌|                  |❌|                  `GH-121318`_
**Skeleton3D**
Method ``reset_bone_pose`` adds a new ``reset_bone_skin_scale`` optional parameter                                        |✔️|                 |✔️ with compat|      |✔️|                  `GH-120609`_
Method ``reset_bone_poses`` adds a new ``reset_bone_skin_scale`` optional parameter                                       |✔️|                 |✔️ with compat|      |✔️|                  `GH-120609`_
========================================================================================================================  ===================  ====================  ====================  ============

Audio
~~~~~

========================================================================================================================  ===================  ====================  ====================  ============
Change                                                                                                                    GDScript Compatible  C# Binary Compatible  C# Source Compatible  Introduced
========================================================================================================================  ===================  ====================  ====================  ============
**AudioEffectInstance**
Method ``_process`` changes ``src_buffer`` parameter type from ``const void*`` to ``const AudioFrame*``                   N/A                  N/A                   N/A                   `GH-120749`_
========================================================================================================================  ===================  ====================  ====================  ============

.. note::

    The method ``_process`` has pointer parameters so it's not exposed to scripting.

XR
~~

========================================================================================================================  ===================  ====================  ====================  ============
Change                                                                                                                    GDScript Compatible  C# Binary Compatible  C# Source Compatible  Introduced
========================================================================================================================  ===================  ====================  ====================  ============
**OpenXRSpatialEntityExtension**
Method ``create_spatial_context`` adds a new ``failed_callback`` optional parameter                                       |✔️|                 |✔️ with compat|      |✔️|                  `GH-121123`_
========================================================================================================================  ===================  ====================  ====================  ============

Editor
~~~~~~

========================================================================================================================  ===================  ====================  ====================  ============
Change                                                                                                                    GDScript Compatible  C# Binary Compatible  C# Source Compatible  Introduced
========================================================================================================================  ===================  ====================  ====================  ============
**ScriptEditor**
Type ``ScriptEditor`` changes inheritance from ``PanelContainer`` to ``EditorDock``                                       |❌|                 |❌|                  |❌|                  `GH-113051`_
========================================================================================================================  ===================  ====================  ====================  ============

Behavior changes
----------------

Core
~~~~

.. note::

    The method ``ClassDB.can_instantiate`` no longer considers names of global class scripts (`GH-123379`_).
    Users that need to check for global class scripts can use ``ProjectSettings.get_global_class_list``.

3D
~~

.. note::

    The undocumented ``Node3D._enter_world`` and ``Node3D._exit_world`` callbacks have been removed (`GH-111504`_).
    Users should use ``NOTIFICATION_ENTER_WORLD`` and ``NOTIFICATION_EXIT_WORLD`` instead.

Input
~~~~~

.. note::

    There is now a built-in keyboard shortcut to toggle fullscreen in a project, set to
    :kbd:`Alt + Enter` by default (as well as :kbd:`Ctrl + Cmd + F` on macOS) (`GH-39708`_).
    This shortcut can be modified or removed in the Project Settings' :ui:`Input Map` tab
    by enabling the :button:`Show Built-in Actions`: toggle at the top-right corner and editing
    the ``ui_toggle_fullscreen`` action.

GDScript
~~~~~~~~

.. note::

    GDScripts now explicitly disallow inheriting from their own inner classes (`GH-121171`_).
    The previous behavior added complexity and resulted in confusing bugs, so now users
    get a clear error message instead. Users with a valid use case may use inheritance
    by path (``extends "res://some_other_script"``).

.NET/C#
~~~~~~~

.. note::

    The new minimum required .NET version is 10.0. This change will also require upgrading from Visual Studio 2022
    to Visual Studio 2026 (`GH-123738`_).

Editor
~~~~~~

.. note::

    Main screens are now docks (`GH-113051`_). While compatibility code exists to ensure that old main screen plugins
    still work, they will only work if the plugin implements main screen in the most standard way. There are some edge
    cases that aren't supported, e.g. when a control isn't added to the main screen in the same frame as the plugin
    enters the tree.

    The method ``EditorInterface.get_editor_main_screen`` is now deprecated and doesn't function the same way as
    before. Now, it no longer returns a real main screen.

    As a result of this change, the :button:`Make Floating` functionality of the script editor now uses the dock system,
    accessible through a right mouse button click on the Script tab.

Changed defaults
----------------

The following default values have been changed. If your project uses any of these properties
with their default value, you can achieve a similar behavior to the previous version by manually
setting the values to match the old defaults.

.. note::

    The default GUI focus strategy in **newly created** projects is set to a new option
    called **Balloon** (`GH-120631`_). This aims to improve the consistency of keyboard/controller
    navigation depending on neighboring controls' position. This can lead to different focus behavior
    in some cases. This can be changed in the Project Settings under ``gui/common/auto_focus_strategy``.

.. note::

    Gamepad input is now ignored on unfocused windows by default for **newly created** projects (`GH-120399`_).
    This aims to avoid accidental inputs that are performed when the project is unfocused, as controller input is
    normally sent to all windows by the operating system (unlike keyboard/mouse input). This can be changed in
    the Project Settings under ``input_devices/joypads/ignore_joypad_on_unfocused_application``.

.. note::

    Multi-bounce ambient occlusion is enabled by default for **newly created** projects (`GH-115426`_).
    This affects the appearance of 3D projects in Forward+ with SSAO enabled or when ambient occlusion maps are used.
    This can be changed in the Project Settings under ``rendering/lights_and_shadows/multi_bounce_occlusion/enabled``.

.. |N/A| replace:: :abbr:`N/A (This API is not available so compatibility is not applicable.)`
.. |❌| replace:: :abbr:`❌ (This API breaks compatibility.)`
.. |❌ with stub| replace:: :abbr:`❌ (Stub compatibility methods were added to prevent crashes. However, this API is not functional anymore.)`
.. |✔️| replace:: :abbr:`✔️ (This API does not break compatibility.)`
.. |✔️ with compat| replace:: :abbr:`✔️ (This API does not break compatibility. A compatibility method was added.)`

.. _GH-39708: https://github.com/godotengine/godot/pull/39708
.. _GH-104289: https://github.com/godotengine/godot/pull/104289
.. _GH-111504: https://github.com/godotengine/godot/pull/111504
.. _GH-113051: https://github.com/godotengine/godot/pull/113051
.. _GH-114533: https://github.com/godotengine/godot/pull/114533
.. _GH-115003: https://github.com/godotengine/godot/pull/115003
.. _GH-115426: https://github.com/godotengine/godot/pull/115426
.. _GH-119196: https://github.com/godotengine/godot/pull/119196
.. _GH-120399: https://github.com/godotengine/godot/pull/120399
.. _GH-120609: https://github.com/godotengine/godot/pull/120609
.. _GH-120631: https://github.com/godotengine/godot/pull/120631
.. _GH-120749: https://github.com/godotengine/godot/pull/120749
.. _GH-121123: https://github.com/godotengine/godot/pull/121123
.. _GH-121171: https://github.com/godotengine/godot/pull/121171
.. _GH-121318: https://github.com/godotengine/godot/pull/121318
.. _GH-121895: https://github.com/godotengine/godot/pull/121895
.. _GH-121937: https://github.com/godotengine/godot/pull/121937
.. _GH-123379: https://github.com/godotengine/godot/pull/123379
.. _GH-123738: https://github.com/godotengine/godot/pull/123738
