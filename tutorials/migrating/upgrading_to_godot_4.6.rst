.. _doc_upgrading_to_godot_4.6:

Upgrading from Godot 4.5 to Godot 4.6
=====================================

For most games and apps made with 4.5 it should be relatively safe to migrate to 4.6.
This page intends to cover everything you need to pay attention to when migrating
your project.

Breaking changes
----------------

If you are migrating from 4.5 to 4.6, the breaking changes listed here might
affect you. Changes are grouped by areas/systems.

This article indicates whether each breaking change affects GDScript and whether
the C# breaking change is *binary compatible* or *source compatible*:

- **Binary compatible** - Existing binaries will load and execute successfully without
  recompilation, and the run-time behavior won't change.
- **Source compatible** - Source code will compile successfully without changes when
  upgrading Godot.

Core
~~~~

========================================================================================================================  ===================  ====================  ====================  ============
Change                                                                                                                    GDScript Compatible  C# Binary Compatible  C# Source Compatible  Introduced
========================================================================================================================  ===================  ====================  ====================  ============
**FileAccess**
Method ``create_temp`` changes ``mode_flags`` parameter type from ``int`` to ``FileAccess.ModeFlags``                     |✔️|                 |✔️ with compat|      |✔️ with compat|      `GH-114053`_
Method ``get_as_text`` removes ``skip_cr`` parameter                                                                      |✔️|                 |✔️ with compat|      |✔️ with compat|      `GH-110867`_
**Performance**
Method ``add_custom_monitor`` adds a new ``type`` optional parameter                                                      |✔️|                 |✔️ with compat|      |✔️ with compat|      `GH-110433`_
========================================================================================================================  ===================  ====================  ====================  ============

Animation
~~~~~~~~~

========================================================================================================================  ===================  ====================  ====================  ============
Change                                                                                                                    GDScript Compatible  C# Binary Compatible  C# Source Compatible  Introduced
========================================================================================================================  ===================  ====================  ====================  ============
**AnimationPlayer**
Property ``assigned_animation`` changes type from ``String`` to ``StringName``                                            |✔️|                 |❌|                  |❌|                  `GH-110767`_
Property ``autoplay`` changes type from ``String`` to ``StringName``                                                      |✔️|                 |❌|                  |❌|                  `GH-110767`_
Property ``current_animation`` changes type from ``String`` to ``StringName``                                             |✔️|                 |❌|                  |❌|                  `GH-110767`_
Method ``get_queue`` changes return type from ``PackedStringArray`` to ``StringName[]``                                   |✔️|                 |❌|                  |❌|                  `GH-110767`_
Signal ``current_animation_changed`` changes ``name`` parameter type from ``String`` to ``StringName``                    |✔️|                 |❌|                  |❌|                  `GH-110767`_
========================================================================================================================  ===================  ====================  ====================  ============

3D
~~

=================================================================================================================================================================  ===================  ====================  ====================  ============
Change                                                                                                                                                             GDScript Compatible  C# Binary Compatible  C# Source Compatible  Introduced
=================================================================================================================================================================  ===================  ====================  ====================  ============
**SpringBoneSimulator3D**
Method ``get_end_bone_direction`` changes return type from ``SpringBoneSimulator3D.BoneDirection`` to ``SkeletonModifier3D.BoneDirection``                         |✔️|                 |❌|                  |✔️|                  `GH-110120`_
Method ``get_joint_rotation_axis`` changes return type from ``SpringBoneSimulator3D.RotationAxis`` to ``SkeletonModifier3D.RotationAxis``                          |✔️|                 |❌|                  |✔️|                  `GH-110120`_
Method ``get_rotation_axis`` changes return type from ``SpringBoneSimulator3D.RotationAxis`` to ``SkeletonModifier3D.RotationAxis``                                |✔️|                 |❌|                  |✔️|                  `GH-110120`_
Method ``set_end_bone_direction`` changes ``bone_direction`` parameter type from ``SpringBoneSimulator3D.BoneDirection`` to ``SkeletonModifier3D.BoneDirection``   |✔️|                 |❌|                  |✔️|                  `GH-110120`_
Method ``set_joint_rotation_axis`` changes ``axis`` parameter type from ``SpringBoneSimulator3D.RotationAxis`` to ``SkeletonModifier3D.RotationAxis``              |✔️|                 |❌|                  |✔️|                  `GH-110120`_
Method ``set_rotation_axis`` changes ``axis`` parameter type from ``SpringBoneSimulator3D.RotationAxis`` to ``SkeletonModifier3D.RotationAxis``                    |✔️|                 |❌|                  |✔️|                  `GH-110120`_
=================================================================================================================================================================  ===================  ====================  ====================  ============

Rendering
~~~~~~~~~

========================================================================================================================  ===================  ====================  ====================  ============
Change                                                                                                                    GDScript Compatible  C# Binary Compatible  C# Source Compatible  Introduced
========================================================================================================================  ===================  ====================  ====================  ============
**DisplayServer**
Method ``accessibility_create_sub_text_edit_elements`` adds a new ``is_last_line`` optional parameter                     |✔️|                 |✔️ with compat|      |✔️ with compat|      `GH-113459`_
Method ``tts_speak`` changes ``utterance_id`` parameter type metadata from ``int32`` to ``int64``                         |✔️|                 |✔️ with compat|      |✔️ with compat|      `GH-112379`_
========================================================================================================================  ===================  ====================  ====================  ============

GUI nodes
~~~~~~~~~

========================================================================================================================  ===================  ====================  ====================  ============
Change                                                                                                                    GDScript Compatible  C# Binary Compatible  C# Source Compatible  Introduced
========================================================================================================================  ===================  ====================  ====================  ============
**Control**
Method ``grab_focus`` adds a new ``hide_focus`` optional parameter                                                        |✔️|                 |✔️ with compat|      |✔️ with compat|      `GH-110250`_
Method ``has_focus`` adds a new ``ignore_hidden_focus`` optional parameter                                                |✔️|                 |✔️ with compat|      |✔️ with compat|      `GH-110250`_
**FileDialog**
Method ``add_filter`` adds a new ``mime_type`` optional parameter                                                         |✔️|                 |✔️ with compat|      |✔️ with compat|      `GH-111439`_
**LineEdit**
Method ``edit`` adds a new ``hide_focus`` optional parameter                                                              |✔️|                 |✔️ with compat|      |✔️ with compat|      `GH-111117`_
**SplitContainer**
Method ``clamp_split_offset`` adds a new ``priority_index`` optional parameter                                            |✔️|                 |✔️ with compat|      |✔️ with compat|      `GH-90411`_
========================================================================================================================  ===================  ====================  ====================  ============

Networking
~~~~~~~~~~

========================================================================================================================  ===================  ====================  ====================  ============
Change                                                                                                                    GDScript Compatible  C# Binary Compatible  C# Source Compatible  Introduced
========================================================================================================================  ===================  ====================  ====================  ============
**StreamPeerTCP**
Method ``disconnect_from_host`` moved to base class ``StreamPeerSocket``                                                  |✔️|                 |✔️|                  |✔️|                  `GH-107954`_
Method ``get_status`` moved to base class ``StreamPeerSocket``                                                            |✔️|                 |❌|                  |✔️|                  `GH-107954`_
Method ``poll`` moved to base class ``StreamPeerSocket``                                                                  |✔️|                 |✔️|                  |✔️|                  `GH-107954`_
**TCPServer**
Method ``is_connection_available`` moved to base class ``SocketServer``                                                   |✔️|                 |✔️|                  |✔️|                  `GH-107954`_
Method ``is_listening`` moved to base class ``SocketServer``                                                              |✔️|                 |✔️|                  |✔️|                  `GH-107954`_
Method ``stop`` moved to base class ``SocketServer``                                                                      |✔️|                 |✔️|                  |✔️|                  `GH-107954`_
========================================================================================================================  ===================  ====================  ====================  ============

OpenXR
~~~~~~

========================================================================================================================  ===================  ====================  ====================  ============
Change                                                                                                                    GDScript Compatible  C# Binary Compatible  C# Source Compatible  Introduced
========================================================================================================================  ===================  ====================  ====================  ============
**OpenXRExtensionWrapper**
Method ``_get_requested_extensions`` adds a new ``xr_version`` parameter                                                  |❌|                 |❌|                  |❌|                  `GH-109302`_
Method ``_set_instance_create_info_and_get_next_pointer`` adds  a new ``xr_version`` parameter                            N/A                  N/A                   N/A                   `GH-109302`_
========================================================================================================================  ===================  ====================  ====================  ============

.. note::

    The ``OpenXRExtensionWrapper`` type is intended to be subclassed from GDExtensions. The method ``_set_instance_create_info_and_get_next_pointer``
    has a ``void*`` parameter so it's not exposed to scripting.

Editor
~~~~~~

========================================================================================================================  ===================  ====================  ====================  ============
Change                                                                                                                    GDScript Compatible  C# Binary Compatible  C# Source Compatible  Introduced
========================================================================================================================  ===================  ====================  ====================  ============
**EditorExportPreset**
Method ``get_script_export_mode`` changes return type from ``int`` to ``EditorExportPreset.ScriptExportMode``             |✔️|                 |❌|                  |❌|                  `GH-107167`_
**EditorFileDialog**
Method ``add_filter`` moved to base class ``FileDialog``                                                                  |✔️|                 |✔️|                  |✔️|                  `GH-111212`_
Method ``add_option`` moved to base class ``FileDialog``                                                                  |✔️|                 |✔️|                  |✔️|                  `GH-111212`_
Method ``add_side_menu`` removed                                                                                          |❌ with stub|       |❌ with stub|        |❌ with stub|        `GH-111162`_
Method ``clear_filename_filter`` moved to base class ``FileDialog``                                                       |✔️|                 |✔️|                  |✔️|                  `GH-111212`_
Method ``clear_filters`` moved to base class ``FileDialog``                                                               |✔️|                 |✔️|                  |✔️|                  `GH-111212`_
Method ``get_filename_filter`` moved to base class ``FileDialog``                                                         |✔️|                 |✔️|                  |✔️|                  `GH-111212`_
Method ``get_line_edit`` moved to base class ``FileDialog``                                                               |✔️|                 |✔️|                  |✔️|                  `GH-111212`_
Method ``get_option_default`` moved to base class ``FileDialog``                                                          |✔️|                 |✔️|                  |✔️|                  `GH-111212`_
Method ``get_option_name`` moved to base class ``FileDialog``                                                             |✔️|                 |✔️|                  |✔️|                  `GH-111212`_
Method ``get_option_values`` moved to base class ``FileDialog``                                                           |✔️|                 |✔️|                  |✔️|                  `GH-111212`_
Method ``get_selected_options`` moved to base class ``FileDialog``                                                        |✔️|                 |✔️|                  |✔️|                  `GH-111212`_
Method ``get_vbox`` moved to base class ``FileDialog``                                                                    |✔️|                 |✔️|                  |✔️|                  `GH-111212`_
Method ``invalidate`` moved to base class ``FileDialog``                                                                  |✔️|                 |✔️|                  |✔️|                  `GH-111212`_
Method ``popup_file_dialog`` moved to base class ``FileDialog``                                                           |✔️|                 |✔️|                  |✔️|                  `GH-111212`_
Method ``set_filename_filter`` moved to base class ``FileDialog``                                                         |✔️|                 |✔️|                  |✔️|                  `GH-111212`_
Method ``set_option_default`` moved to base class ``FileDialog``                                                          |✔️|                 |✔️|                  |✔️|                  `GH-111212`_
Method ``set_option_name`` moved to base class ``FileDialog``                                                             |✔️|                 |✔️|                  |✔️|                  `GH-111212`_
Method ``set_option_values`` moved to base class ``FileDialog``                                                           |✔️|                 |✔️|                  |✔️|                  `GH-111212`_
Property ``access`` moved to base class ``FileDialog``                                                                    |✔️|                 |❌|                  |✔️|                  `GH-111212`_
Property ``current_dir`` moved to base class ``FileDialog``                                                               |✔️|                 |✔️|                  |✔️|                  `GH-111212`_
Property ``current_file`` moved to base class ``FileDialog``                                                              |✔️|                 |✔️|                  |✔️|                  `GH-111212`_
Property ``current_path`` moved to base class ``FileDialog``                                                              |✔️|                 |✔️|                  |✔️|                  `GH-111212`_
Property ``display_mode`` moved to base class ``FileDialog``                                                              |✔️|                 |❌|                  |✔️|                  `GH-111212`_
Property ``file_mode`` moved to base class ``FileDialog``                                                                 |✔️|                 |❌|                  |✔️|                  `GH-111212`_
Property ``filters`` moved to base class ``FileDialog``                                                                   |✔️|                 |✔️|                  |✔️|                  `GH-111212`_
Property ``option_count`` moved to base class ``FileDialog``                                                              |✔️|                 |✔️|                  |✔️|                  `GH-111212`_
Property ``show_hidden_files`` moved to base class ``FileDialog``                                                         |✔️|                 |✔️|                  |✔️|                  `GH-111212`_
Signal ``dir_selected`` moved to base class ``FileDialog``                                                                |✔️|                 |❌|                  |✔️|                  `GH-111212`_
Signal ``filename_filter_changed`` moved to base class ``FileDialog``                                                     |✔️|                 |❌|                  |✔️|                  `GH-111212`_
Signal ``file_selected`` moved to base class ``FileDialog``                                                               |✔️|                 |❌|                  |✔️|                  `GH-111212`_
Signal ``files_selected`` moved to base class ``FileDialog``                                                              |✔️|                 |❌|                  |✔️|                  `GH-111212`_
========================================================================================================================  ===================  ====================  ====================  ============

Behavior changes
----------------

Android
~~~~~~~

.. note::

    The source sets configuration for Android export templates has been updated to match
    the default Android Studio project structure (`GH-110829`_). This affects the directory
    layout of the Android project:

    - Files previously in ``[Project root]/android/build/src/`` are now in ``[Project root]/android/build/src/main/java/``.
    -  Android manifest file and assets directory have been moved to ``src/main/`` subdirectories.

    For example, ``GodotApp.java`` moved from ``src/com/godot/game/GodotApp.java`` to
    ``src/main/java/com/godot/game/GodotApp.java``.

Rendering
~~~~~~~~~

.. note::

    Soft Light blend mode now always behaves as it did previously with ``use_hdr_2d``, regardless of
    the Viewport's ``use_hdr_2d`` setting (`GH-109971`_).

Changed defaults
----------------

The following default values have been changed. If your project relies on the previous defaults,
you may need to explicitly set them to the old values.

.. note::

    The default rendering driver on Windows for **newly created** projects is now :abbr:`D3D12 (Direct3D 12)` (`GH-113213`_).
    This can be changed in Project Settings under ``rendering/rendering_device/driver.windows``.

.. note::

    The default 3D physics engine for **newly created** projects is now Jolt Physics (`GH-105737`_).
    This can be changed in Project Settings under ``physics/3d/physics_engine``.

3D
~~

================================================================================  =========================  =========================  ============
Member                                                                            Old Value                  New Value                  Introduced
================================================================================  =========================  =========================  ============
**MeshInstance3D**
Property ``skeleton``                                                             NodePath("..")             NodePath("")               `GH-112267`_
================================================================================  =========================  =========================  ============

.. note::

    The default value of ``skeleton`` has changed. Enable ``animation/compatibility/default_parent_skeleton_in_mesh_instance_3d`` in Project Settings
    if the old behavior is needed for compatibility.

Rendering
~~~~~~~~~

================================================================================  =========================  =========================  ============
Member                                                                            Old Value                  New Value                  Introduced
================================================================================  =========================  =========================  ============
**ProjectSettings**
Property ``rendering/reflections/sky_reflections/roughness_layers``               8                          7                          `GH-107902`_
Property ``rendering/rendering_device/d3d12/agility_sdk_version``                 613                        618                        `GH-114043`_
**Environment**
Property ``glow_blend_mode``                                                      2                          1                          `GH-110671`_
Property ``glow_intensity``                                                       0.8                        0.3                        `GH-110671`_
Property ``glow_levels/2``                                                        0.0                        0.8                        `GH-110671`_
Property ``glow_levels/3``                                                        1.0                        0.4                        `GH-110671`_
Property ``glow_levels/4``                                                        0.0                        0.1                        `GH-110671`_
Property ``glow_levels/5``                                                        1.0                        0.0                        `GH-110671`_
Property ``ssr_depth_tolerance``                                                  0.2                        0.5                        `GH-111210`_
================================================================================  =========================  =========================  ============

GUI nodes
~~~~~~~~~

================================================================================  =========================  =========================  ============
Property/Parameter                                                                Old Value                  New Value                  Introduced
================================================================================  =========================  =========================  ============
**PopupMenu**
Property ``submenu_popup_delay``                                                  0.3                        0.2                        `GH-110256`_
**ResourceImporterCSVTranslation**
Property ``compress``                                                             true                       1                          `GH-112073`_
================================================================================  =========================  =========================  ============

.. |❌| replace:: :abbr:`❌ (This API breaks compatibility.)`
.. |❌ with stub| replace:: :abbr:`❌ (Stub compatibility methods were added to prevent crashes. However, this API is not functional anymore.)`
.. |✔️| replace:: :abbr:`✔️ (This API does not break compatibility.)`
.. |✔️ with compat| replace:: :abbr:`✔️ (This API does not break compatibility. A compatibility method was added.)`

.. _GH-90411: https://github.com/godotengine/godot/pull/90411
.. _GH-105737: https://github.com/godotengine/godot/pull/105737
.. _GH-107167: https://github.com/godotengine/godot/pull/107167
.. _GH-107902: https://github.com/godotengine/godot/pull/107902
.. _GH-107954: https://github.com/godotengine/godot/pull/107954
.. _GH-109302: https://github.com/godotengine/godot/pull/109302
.. _GH-109971: https://github.com/godotengine/godot/pull/109971
.. _GH-110120: https://github.com/godotengine/godot/pull/110120
.. _GH-110250: https://github.com/godotengine/godot/pull/110250
.. _GH-110256: https://github.com/godotengine/godot/pull/110256
.. _GH-110433: https://github.com/godotengine/godot/pull/110433
.. _GH-110671: https://github.com/godotengine/godot/pull/110671
.. _GH-110767: https://github.com/godotengine/godot/pull/110767
.. _GH-110829: https://github.com/godotengine/godot/pull/110829
.. _GH-110867: https://github.com/godotengine/godot/pull/110867
.. _GH-111117: https://github.com/godotengine/godot/pull/111117
.. _GH-111162: https://github.com/godotengine/godot/pull/111162
.. _GH-111210: https://github.com/godotengine/godot/pull/111210
.. _GH-111212: https://github.com/godotengine/godot/pull/111212
.. _GH-111439: https://github.com/godotengine/godot/pull/111439
.. _GH-112073: https://github.com/godotengine/godot/pull/112073
.. _GH-112267: https://github.com/godotengine/godot/pull/112267
.. _GH-112379: https://github.com/godotengine/godot/pull/112379
.. _GH-113213: https://github.com/godotengine/godot/pull/113213
.. _GH-113459: https://github.com/godotengine/godot/pull/113459
.. _GH-114043: https://github.com/godotengine/godot/pull/114043
.. _GH-114053: https://github.com/godotengine/godot/pull/114053
