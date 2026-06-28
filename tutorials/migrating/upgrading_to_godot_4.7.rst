.. _doc_upgrading_to_godot_4.7:

Upgrading from Godot 4.6 to Godot 4.7
=====================================

For most games and apps made with 4.6 it should be relatively safe to migrate to 4.7.
This page intends to cover everything you need to pay attention to when migrating
your project.

Breaking changes
----------------

If you are migrating from 4.6 to 4.7, the breaking changes listed here might
affect you. Changes are grouped by areas/systems.

This article indicates whether each breaking change affects GDScript and whether
the C# breaking change is *binary compatible* or *source compatible*:

- **Binary compatible** - Existing binaries will load and execute successfully without
  recompilation, and the runtime behavior won't change.
- **Source compatible** - Source code will compile successfully without changes when
  upgrading Godot.

Core
~~~~

========================================================================================================================  ===================  ====================  ====================  ============
Change                                                                                                                    GDScript Compatible  C# Binary Compatible  C# Source Compatible  Introduced
========================================================================================================================  ===================  ====================  ====================  ============
**Object**
Method ``is_class`` changes ``class`` parameter type from ``String`` to ``StringName``                                    |✔️|                 |✔️ with compat|      |✔️|                  `GH-118582`_
**ZIPPacker**
Method ``start_file`` adds new ``permissions`` and ``modified_time`` optional parameters                                  |✔️|                 |✔️ with compat|      |✔️|                  `GH-115946`_
**OptimizedTranslation**
Method ``generate`` changes return type from ``void`` to ``bool``                                                         |✔️|                 |❌|                  |✔️|                  `GH-119563`_
========================================================================================================================  ===================  ====================  ====================  ============

2D
~~

========================================================================================================================  ===================  ====================  ====================  ============
Change                                                                                                                    GDScript Compatible  C# Binary Compatible  C# Source Compatible  Introduced
========================================================================================================================  ===================  ====================  ====================  ============
**CPUParticles2D**
Method ``request_particles_process`` adds new ``process_time_residual`` optional parameter                                |✔️|                 |✔️ with compat|      |✔️|                  `GH-109142`_
**GPUParticles2D**
Method ``request_particles_process`` adds new ``process_time_residual`` optional parameter                                |✔️|                 |✔️ with compat|      |✔️|                  `GH-109142`_
========================================================================================================================  ===================  ====================  ====================  ============

3D
~~

========================================================================================================================  ===================  ====================  ====================  ============
Change                                                                                                                    GDScript Compatible  C# Binary Compatible  C# Source Compatible  Introduced
========================================================================================================================  ===================  ====================  ====================  ============
**CPUParticles3D**
Method ``request_particles_process`` adds new ``process_time_residual`` optional parameter                                |✔️|                 |✔️ with compat|      |✔️|                  `GH-109142`_
**GPUParticles3D**
Method ``request_particles_process`` adds new ``process_time_residual`` optional parameter                                |✔️|                 |✔️ with compat|      |✔️|                  `GH-109142`_
========================================================================================================================  ===================  ====================  ====================  ============

GUI nodes
~~~~~~~~~

=================================================================================================================================================  ===================  ====================  ====================  ============
Change                                                                                                                                             GDScript Compatible  C# Binary Compatible  C# Source Compatible  Introduced
=================================================================================================================================================  ===================  ====================  ====================  ============
**Control**
Property ``accessibility_live`` changes type from ``DisplayServer.AccessibilityLiveMode`` to ``AccessibilityServer.AccessibilityLiveMode``         |✔️|                 |❌|                  |❌|                  `GH-116839`_
**RichTextLabel**
Enum field ``ImageUpdateMask.UPDATE_WIDTH_IN_PERCENT`` renamed to ``ImageUpdateMask.UPDATE_WIDTH_UNIT``                                            |❌|                 |✔️|                  |❌|                  `GH-112617`_
Method ``add_image`` changes ``width`` parameter type from ``int`` to ``float``                                                                    |✔️|                 |✔️ with compat|      |✔️|                  `GH-112617`_
Method ``add_image`` changes ``height`` parameter type from ``int`` to ``float``                                                                   |✔️|                 |✔️ with compat|      |✔️|                  `GH-112617`_
Method ``add_image`` renames ``width_in_percent`` parameter to ``width_unit`` and changes type from ``bool`` to ``RichTextLabel.ImageUnit``        |✔️|                 |✔️ with compat|      |❌|                  `GH-112617`_
Method ``add_image`` renames ``height_in_percent`` parameter to ``height_unit`` and changes type from ``bool`` to ``RichTextLabel.ImageUnit``      |✔️|                 |✔️ with compat|      |❌|                  `GH-112617`_
Method ``update_image`` changes ``width`` parameter type from ``int`` to ``float``                                                                 |✔️|                 |✔️ with compat|      |✔️|                  `GH-112617`_
Method ``update_image`` changes ``height`` parameter type from ``int`` to ``float``                                                                |✔️|                 |✔️ with compat|      |✔️|                  `GH-112617`_
Method ``update_image`` renames ``width_in_percent`` parameter to ``width_unit`` and changes type from ``bool`` to ``RichTextLabel.ImageUnit``     |✔️|                 |✔️ with compat|      |❌|                  `GH-112617`_
Method ``update_image`` renames ``height_in_percent`` parameter to ``height_unit`` and changes type from ``bool`` to ``RichTextLabel.ImageUnit``   |✔️|                 |✔️ with compat|      |❌|                  `GH-112617`_
=================================================================================================================================================  ===================  ====================  ====================  ============

Text
~~~~

========================================================================================================================  ===================  ====================  ====================  ============
Change                                                                                                                    GDScript Compatible  C# Binary Compatible  C# Source Compatible  Introduced
========================================================================================================================  ===================  ====================  ====================  ============
**Font**
Method ``find_variation`` adds new ``palette_index`` and ``custom_colors`` optional parameters                            |✔️|                 |✔️ with compat|      |✔️|                  `GH-117149`_
**TreeItem**
Method ``select`` adds new ``set_as_cursor`` optional parameter                                                           |✔️|                 |✔️ with compat|      |✔️|                  `GH-119367`_
========================================================================================================================  ===================  ====================  ====================  ============

Rendering
~~~~~~~~~

==================================================================================================================================================  ===================  ====================  ====================  ============
Change                                                                                                                                              GDScript Compatible  C# Binary Compatible  C# Source Compatible  Introduced
==================================================================================================================================================  ===================  ====================  ====================  ============
**Image**
Method ``save_exr`` adds new ``color_image`` and ``max_linear_value`` optional parameters                                                           |✔️|                 |✔️ with compat|      |✔️|                  `GH-117800`_
Method ``save_exr_to_buffer`` adds new ``color_image`` and ``max_linear_value`` optional parameters                                                 |✔️|                 |✔️ with compat|      |✔️|                  `GH-117800`_
**ImageTexture**
Method ``get_format`` moved to base class ``Texture2D``                                                                                             |✔️|                 |✔️|                  |✔️|                  `GH-109004`_
**PortableCompressedTexture2D**
Method ``get_format`` moved to base class ``Texture2D``                                                                                             |✔️|                 |✔️|                  |✔️|                  `GH-109004`_
**RenderingServer**
Method ``particles_request_process_time`` renames ``time`` parameter to ``process_time`` and adds new ``process_time_residual`` optional parameter  |✔️|                 |✔️ with compat|      |❌|                  `GH-109142`_
Method ``viewport_set_size`` adds new ``view_count`` optional parameter                                                                             |✔️|                 |✔️ with compat|      |✔️|                  `GH-115799`_
==================================================================================================================================================  ===================  ====================  ====================  ============

Animation
~~~~~~~~~

========================================================================================================================  ===================  ====================  ====================  ============
Change                                                                                                                    GDScript Compatible  C# Binary Compatible  C# Source Compatible  Introduced
========================================================================================================================  ===================  ====================  ====================  ============
**Animation**
Property ``length`` changes type metadata from ``float`` to ``double``                                                    |✔️|                 |❌|                  |❌|                  `GH-116394`_
**AnimationNodeBlendSpace1D**
Method ``add_blend_point`` adds new ``name`` optional parameter                                                           |✔️|                 |✔️ with compat|      |✔️|                  `GH-110369`_
**AnimationNodeBlendSpace2D**
Method ``add_blend_point`` adds new ``name`` optional parameter                                                           |✔️|                 |✔️ with compat|      |✔️|                  `GH-110369`_
========================================================================================================================  ===================  ====================  ====================  ============

Physics
~~~~~~~

========================================================================================================================  ===================  ====================  ====================  ============
Change                                                                                                                    GDScript Compatible  C# Binary Compatible  C# Source Compatible  Introduced
========================================================================================================================  ===================  ====================  ====================  ============
**PhysicsServer2D**
Method ``body_set_shape_as_one_way_collision`` adds new ``direction`` optional parameter                                  |✔️|                 |✔️ with compat|      |✔️|                  `GH-104736`_
**PhysicsServer2DExtension**
Method ``_body_set_shape_as_one_way_collision`` adds new ``direction`` parameter                                          |❌|                 |❌|                  |❌|                  `GH-104736`_
========================================================================================================================  ===================  ====================  ====================  ============

Audio
~~~~~

========================================================================================================================  ===================  ====================  ====================  ============
Change                                                                                                                    GDScript Compatible  C# Binary Compatible  C# Source Compatible  Introduced
========================================================================================================================  ===================  ====================  ====================  ============
**AudioEffectSpectrumAnalyzer**
Property ``tap_back_pos`` removed                                                                                         |❌|                 |❌|                  |❌|                  `GH-114355`_
========================================================================================================================  ===================  ====================  ====================  ============

XR
~~

========================================================================================================================  ===================  ====================  ====================  ============
Change                                                                                                                    GDScript Compatible  C# Binary Compatible  C# Source Compatible  Introduced
========================================================================================================================  ===================  ====================  ====================  ============
**OpenXRExtensionWrapper**
Method ``_on_register_metadata`` adds new ``interaction_profile_metadata`` parameter                                      |❌|                 |❌|                  |❌|                  `GH-117399`_
**OpenXRSpatialAnchorCapability**
Method ``create_new_anchor`` adds new ``next`` optional parameter                                                         |✔️|                 |✔️ with compat|      |✔️|                  `GH-118128`_
========================================================================================================================  ===================  ====================  ====================  ============

Editor
~~~~~~

========================================================================================================================  ===================  ====================  ====================  ============
Change                                                                                                                    GDScript Compatible  C# Binary Compatible  C# Source Compatible  Introduced
========================================================================================================================  ===================  ====================  ====================  ============
**EditorSceneFormatImporter**
Constant ``IMPORT_ANIMATION`` moved to enum ``ImportFlags``                                                               |✔️|                 |✔️|                  |❌|                  `GH-115788`_
Constant ``IMPORT_DISCARD_MESHES_AND_MATERIALS`` moved to enum ``ImportFlags``                                            |✔️|                 |✔️|                  |❌|                  `GH-115788`_
Constant ``IMPORT_FAIL_ON_MISSING_DEPENDENCIES`` moved to enum ``ImportFlags``                                            |✔️|                 |✔️|                  |❌|                  `GH-115788`_
Constant ``IMPORT_FORCE_DISABLE_MESH_COMPRESSION`` moved to enum ``ImportFlags``                                          |✔️|                 |✔️|                  |❌|                  `GH-115788`_
Constant ``IMPORT_GENERATE_TANGENT_ARRAYS`` moved to enum ``ImportFlags``                                                 |✔️|                 |✔️|                  |❌|                  `GH-115788`_
Constant ``IMPORT_SCENE`` moved to enum ``ImportFlags``                                                                   |✔️|                 |✔️|                  |❌|                  `GH-115788`_
Constant ``IMPORT_USE_NAMED_SKIN_BINDS`` moved to enum ``ImportFlags``                                                    |✔️|                 |✔️|                  |❌|                  `GH-115788`_
**EditorVCSInterface**
Method ``_commit`` adds new ``amend`` parameter                                                                           |❌|                 |❌|                  |❌|                  `GH-117968`_
========================================================================================================================  ===================  ====================  ====================  ============

Behavior changes
----------------

Animation
~~~~~~~~~

.. note::

    AnimationNodeBlendSpace1D and AnimationNodeBlendSpace2D have a new SyncMode
    enum that replaces the previous boolean ``sync`` property. If you are using
    an AnimationTree and your animations aren't transitioning correctly after
    upgrading, you may need to set that value in each of your blend spaces to
    get the desired behavior back.

    The new sync modes are documented in
    :ref:`AnimationNodeBlendSpace1D.sync_mode <class_AnimationNodeBlendSpace1D_property_sync_mode>`
    and :ref:`AnimationNodeBlendSpace2D.sync_mode <class_AnimationNodeBlendSpace2D_property_sync_mode>`.

Rendering
~~~~~~~~~

.. note::

    The ``LinearToSRGB`` visual shader no longer clamps to the range ``[0.0, 1.0]``
    when using the Mobile or Forward+ renderer (`GH-113956`_).

.. note::

    ``CanvasItem`` now avoids adding the antialiasing feather when drawing lines (`GH-105122`_).
    The feather made lines appear thicker than intended, projects that relied on this behavior
    will have to be updated to draw a thicker line width.

Physics
~~~~~~~

.. note::

    The default ``area_mask`` for ``AudioStreamPlayer`` was changed from ``1`` to ``0`` (disabled) (`GH-107679`_).
    If you use the ``audio_bus_override`` feature on ``Area2D`` or ``Area3D``, **and** you
    use the ``AudioStreamPlayer`` default ``area_mask`` (just layer ``1`` ticked), you will need
    to reset the mask to layer ``1`` — otherwise, the bus overrides will stop working.
    If the mask was set to anything except layer ``1``, it will continue to work as expected.

.. note::

    When using Jolt Physics as the 3D physics engine, ``WorldBoundaryShape3D`` will now use the same
    convention as Godot when applying ``WorldBoundaryShape3D.plane.d``, resulting in the sign of the plane
    distance being interpreted in the opposite way compared to Godot 4.6 (`GH-118948`_). You will need to flip
    the sign yourself to get the same behavior as in Godot 4.6.

.. note::

    When using Jolt Physics as the 3D physics engine, ``SoftBody3D`` will no longer default its mass to ``0``,
    which resulted in an automatically calculated weight of 1 kg per point, resulting in a very high total
    mass for the body. Now instead it will default to 1 kg for the entire ``SoftBody3D``, same as Godot
    Physics (`GH-116041`_).

.. note::

    When using Jolt Physics as the 3D physics engine, ``SoftBody3D`` will now apply
    ``SoftBody3D.linear_stiffness`` in a way that better matches Godot Physics, and in a way that's more
    appropriate in general (`GH-116041`_). This will affect every ``SoftBody3D`` instance in one way or
    another, meaning you will need to re-tweak properties like ``SoftBody3D.linear_stiffness`` and
    ``SoftBody3D.damping_coefficient`` to achieve your desired behavior.

.. note::

    When using Jolt Physics as the 3D physics engine, ``Area3D`` will now report overlaps with ``SoftBody3D``
    from its various signals and methods (`GH-114198`_). To work around this breaking change, configure your
    collision layers/masks such that any undesirable interactions between ``Area3D`` and ``SoftBody3D`` are
    ignored.

Input
~~~~~

.. note::

    The device IDs for mouse and keyboard were changed from ``0`` to ``InputEvent.DEVICE_ID_MOUSE`` and
    ``InputEvent.DEVICE_ID_KEYBOARD`` because some joypads may use ``0`` as their ID (`GH-116274`_).
    Check the input event by type or compare the device ID ``InputEvent.device`` to the constants
    ``InputEvent.DEVICE_ID_MOUSE`` and ``InputEvent.DEVICE_ID_KEYBOARD`` instead.


GDScript
~~~~~~~~

.. note::

    Setting the element of packed arrays no longer calls the setter for the entire packed array property
    (`GH-113228`_).

.. note::

    Methods that inherit from a method with a typed return now inherit the return type as well,
    requiring an explicit return statement in the override (`GH-115763`_).
    Add ``return null`` to the end of the method to fix the error.

Changed defaults
----------------

The following default values have been changed. If your project uses any of these properties
with their default value, you can achieve a similar behavior to the previous version by manually
setting the values to match the old defaults.


.. note::

    The default stretch mode and stretch aspect for **newly created** projects
    is now ``canvas_items`` and ``expand`` respectively (previously ``disabled``
    and ``keep``). This can be changed in the Project Settings under
    ``display/window/stretch/mode`` and ``display/window/stretch/aspect``.

Animation
~~~~~~~~~

================================================================================  =========================  =========================
Property/Parameter                                                                Old Default                New Default
================================================================================  =========================  =========================
**LookAtModifier3D**
Property ``relative``                                                             true                       false
================================================================================  =========================  =========================

Core
~~~~

================================================================================  =========================  =========================
Property/Parameter                                                                Old Default                New Default
================================================================================  =========================  =========================
**ProjectSettings**
Property ``rendering/reflections/sky_reflections/roughness_layers``               7                          8
================================================================================  =========================  =========================

GUI nodes
~~~~~~~~~

================================================================================  =========================  =========================
Property/Parameter                                                                Old Default                New Default
================================================================================  =========================  =========================
**RichTextLabel**
Method ``add_image`` parameter ``width_in_percent``                               false                      0
Method ``add_image`` parameter ``height_in_percent``                              false                      0
Method ``update_image`` parameter ``width_in_percent``                            false                      0
Method ``update_image`` parameter ``height_in_percent``                           false                      0
================================================================================  =========================  =========================

Import
~~~~~~

================================================================================  =========================  =========================
Property/Parameter                                                                Old Default                New Default
================================================================================  =========================  =========================
**ResourceImporterDynamicFont**
Property ``hinting``                                                              1                          3
================================================================================  =========================  =========================

.. |N/A| replace:: :abbr:`N/A (This API is not available so compatibility is not applicable.)`
.. |❌| replace:: :abbr:`❌ (This API breaks compatibility.)`
.. |❌ with stub| replace:: :abbr:`❌ (Stub compatibility methods were added to prevent crashes. However, this API is not functional anymore.)`
.. |✔️| replace:: :abbr:`✔️ (This API does not break compatibility.)`
.. |✔️ with compat| replace:: :abbr:`✔️ (This API does not break compatibility. A compatibility method was added.)`

.. _GH-104736: https://github.com/godotengine/godot/pull/104736
.. _GH-105122: https://github.com/godotengine/godot/pull/105122
.. _GH-107679: https://github.com/godotengine/godot/pull/107679
.. _GH-109004: https://github.com/godotengine/godot/pull/109004
.. _GH-109142: https://github.com/godotengine/godot/pull/109142
.. _GH-110369: https://github.com/godotengine/godot/pull/110369
.. _GH-112617: https://github.com/godotengine/godot/pull/112617
.. _GH-113228: https://github.com/godotengine/godot/pull/113228
.. _GH-113956: https://github.com/godotengine/godot/pull/113956
.. _GH-114198: https://github.com/godotengine/godot/pull/114198
.. _GH-114355: https://github.com/godotengine/godot/pull/114355
.. _GH-115763: https://github.com/godotengine/godot/pull/115763
.. _GH-115788: https://github.com/godotengine/godot/pull/115788
.. _GH-115799: https://github.com/godotengine/godot/pull/115799
.. _GH-115946: https://github.com/godotengine/godot/pull/115946
.. _GH-116041: https://github.com/godotengine/godot/pull/116041
.. _GH-116274: https://github.com/godotengine/godot/pull/116274
.. _GH-116394: https://github.com/godotengine/godot/pull/116394
.. _GH-116839: https://github.com/godotengine/godot/pull/116839
.. _GH-117149: https://github.com/godotengine/godot/pull/117149
.. _GH-117399: https://github.com/godotengine/godot/pull/117399
.. _GH-117800: https://github.com/godotengine/godot/pull/117800
.. _GH-117968: https://github.com/godotengine/godot/pull/117968
.. _GH-118128: https://github.com/godotengine/godot/pull/118128
.. _GH-118582: https://github.com/godotengine/godot/pull/118582
.. _GH-118948: https://github.com/godotengine/godot/pull/118948
.. _GH-119367: https://github.com/godotengine/godot/pull/119367
.. _GH-119563: https://github.com/godotengine/godot/pull/119563
