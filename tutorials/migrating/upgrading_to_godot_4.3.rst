.. _doc_upgrading_to_godot_4.3:

Upgrading from Godot 4.2 to Godot 4.3
=====================================

For most games and apps made with 4.2 it should be relatively safe to migrate to 4.3.
This page intends to cover everything you need to pay attention to when migrating
your project.

Breaking changes
----------------

If you are migrating from 4.2 to 4.3, the breaking changes listed here might
affect you. Changes are grouped by areas/systems.

This article indicates whether each breaking change affects GDScript and whether
the C# breaking change is *binary compatible* or *source compatible*:

- **Binary compatible** - Existing binaries will load and execute successfully without
  recompilation, and the runtime behavior won't change.
- **Source compatible** - Source code will compile successfully without changes when
  upgrading Godot.

GDExtension
~~~~~~~~~~~

========================================================================================================================  ===================  ====================  ====================  ===========
Change                                                                                                                    GDScript Compatible  C# Binary Compatible  C# Source Compatible  Introduced
========================================================================================================================  ===================  ====================  ====================  ===========
**GDExtension**
Method ``close_library`` removed                                                                                          |❌|                 |❌|                  |❌|                  `GH-88418`_
Method ``initialize_library`` removed                                                                                     |❌|                 |❌|                  |❌|                  `GH-88418`_
Method ``open_library`` removed                                                                                           |❌|                 |❌|                  |❌|                  `GH-88418`_
========================================================================================================================  ===================  ====================  ====================  ===========

Since it was basically impossible to use these methods in any useful way, these methods have been removed. Use ``GDExtensionManager::load_extension`` and ``GDExtensionManager::unload_extension`` instead to correctly load and unload a GDExtension.

Animation
~~~~~~~~~

========================================================================================================================  ===================  ====================  ====================  ===========
Change                                                                                                                    GDScript Compatible  C# Binary Compatible  C# Source Compatible  Introduced
========================================================================================================================  ===================  ====================  ====================  ===========
**Animation**
Method ``position_track_interpolate`` adds a new ``backward`` optional parameter                                          |✔️|                 |✔️ with compat|      |✔️|                  `GH-86629`_
Method ``rotation_track_interpolate`` adds a new ``backward`` optional parameter                                          |✔️|                 |✔️ with compat|      |✔️|                  `GH-86629`_
Method ``scale_track_interpolate`` adds a new ``backward`` optional parameter                                             |✔️|                 |✔️ with compat|      |✔️|                  `GH-86629`_
Method ``blend_shape_track_interpolate`` adds a new ``backward`` optional parameter                                       |✔️|                 |✔️ with compat|      |✔️|                  `GH-86629`_
Method ``value_track_interpolate`` adds a new ``backward`` optional parameter                                             |✔️|                 |✔️ with compat|      |✔️|                  `GH-86629`_
Method ``track_find_key`` adds a new ``limit`` optional parameter                                                         |✔️|                 |✔️ with compat|      |✔️|                  `GH-86661`_
Method ``track_find_key`` adds a new ``backward`` optional parameter                                                      |✔️|                 |✔️ with compat|      |✔️|                  `GH-92861`_
**AnimationMixer**
Method ``_post_process_key_value`` changes ``object`` parameter type from ``Object`` to ``uint64``                        |✔️|                 |❌|                  |❌|                  `GH-86687`_
**Skeleton3D**
Method ``add_bone`` changes return type from ``void`` to ``int32``                                                        |✔️|                 |❌|                  |✔️|                  `GH-88791`_
Signal ``bone_pose_changed`` replaced by ``skeleton_updated``                                                             |❌|                 |❌|                  |❌|                  `GH-90575`_
**BoneAttachment3D**
Method ``on_bone_pose_update`` replaced by ``on_skeleton_update``                                                         |✔️|                 |✔️ with compat|      |✔️ with compat|      `GH-90575`_
========================================================================================================================  ===================  ====================  ====================  ===========

GUI nodes
~~~~~~~~~

========================================================================================================================  ===================  ====================  ====================  ===========
Change                                                                                                                    GDScript Compatible  C# Binary Compatible  C# Source Compatible  Introduced
========================================================================================================================  ===================  ====================  ====================  ===========
**AcceptDialog**
Method ``register_text_enter`` changes parameter ``line_edit`` type from ``Control`` to ``LineEdit``                      |✔️|                 |✔️ with compat|      |✔️ with compat|      `GH-89419`_
Method ``remove_button`` changes parameter ``button`` type from ``Control`` to ``Button``                                 |✔️|                 |✔️ with compat|      |✔️ with compat|      `GH-89419`_
========================================================================================================================  ===================  ====================  ====================  ===========

Physics
~~~~~~~

========================================================================================================================  ===================  ====================  ====================  ===========
Change                                                                                                                    GDScript Compatible  C# Binary Compatible  C# Source Compatible  Introduced
========================================================================================================================  ===================  ====================  ====================  ===========
**PhysicsShapeQueryParameters3D**
Property ``motion`` changes type from ``Vector2`` to ``Vector3``                                                          |❌|                 |❌|                  |❌|                  `GH-85393`_
========================================================================================================================  ===================  ====================  ====================  ===========

.. note::

    In C#, the enum ``PhysicsServer3D.G6DofJointAxisFlag`` breaks compatibility because of the way the bindings generator
    detects the enum prefix. New members were added in `GH-89851`_ to the enum that caused the enum members to be renamed.

Rendering
~~~~~~~~~

========================================================================================================================  ===================  ====================  ====================  ===========
Change                                                                                                                    GDScript Compatible  C# Binary Compatible  C# Source Compatible  Introduced
========================================================================================================================  ===================  ====================  ====================  ===========
**RenderingDevice**
Enum field ``FinalAction.FINAL_ACTION_CONTINUE`` changes value from ``2`` to ``0``                                        |✔️|                 |❌|                  |❌|                  `GH-84976`_
Enum field ``InitialAction.INITIAL_ACTION_CLEAR`` changes value from ``0`` to ``1``                                       |✔️|                 |❌|                  |❌|                  `GH-84976`_
Enum field ``InitialAction.INITIAL_ACTION_CLEAR_REGION_CONTINUE`` changes value from ``2`` to ``1``                       |✔️|                 |❌|                  |❌|                  `GH-84976`_
Enum field ``InitialAction.INITIAL_ACTION_CONTINUE`` changes value from ``5`` to ``0``                                    |✔️|                 |❌|                  |❌|                  `GH-84976`_
Enum field ``InitialAction.INITIAL_ACTION_DROP`` changes value from ``4`` to ``2``                                        |✔️|                 |❌|                  |❌|                  `GH-84976`_
Enum field ``InitialAction.INITIAL_ACTION_KEEP`` changes value from ``3`` to ``0``                                        |✔️|                 |❌|                  |❌|                  `GH-84976`_
Method ``buffer_clear`` removes ``post_barrier`` parameter                                                                |✔️|                 |✔️ with compat|      |✔️ with compat|      `GH-84976`_
Method ``buffer_update`` removes ``post_barrier`` parameter                                                               |✔️|                 |✔️ with compat|      |✔️ with compat|      `GH-84976`_
Method ``compute_list_begin`` removes ``allow_draw_overlap`` parameter                                                    |✔️|                 |✔️ with compat|      |✔️ with compat|      `GH-84976`_
Method ``compute_list_end`` removes ``post_barrier`` parameter                                                            |✔️|                 |✔️ with compat|      |✔️ with compat|      `GH-84976`_
Method ``draw_list_begin`` removes ``storage_textures`` parameter                                                         |✔️|                 |✔️ with compat|      |✔️ with compat|      `GH-84976`_
Method ``draw_list_end`` removes ``post_barrier`` parameter                                                               |✔️|                 |✔️ with compat|      |✔️ with compat|      `GH-84976`_
Method ``texture_clear`` removes ``post_barrier`` parameter                                                               |✔️|                 |✔️ with compat|      |✔️ with compat|      `GH-84976`_
Method ``texture_copy`` removes ``post_barrier`` parameter                                                                |✔️|                 |✔️ with compat|      |✔️ with compat|      `GH-84976`_
Method ``texture_resolve_multisample`` removes ``post_barrier`` parameter                                                 |✔️|                 |✔️ with compat|      |✔️ with compat|      `GH-84976`_
Method ``texture_update`` removes ``post_barrier`` parameter                                                              |✔️|                 |✔️ with compat|      |✔️ with compat|      `GH-84976`_
**RenderingServer**
Method ``environment_set_fog`` adds a new ``fog_mode`` optional parameter                                                 |✔️|                 |✔️ with compat|      |✔️|                  `GH-84792`_
**RenderSceneBuffersRD**
Method ``get_color_layer`` adds a new ``msaa`` optional parameter                                                         |✔️|                 |✔️ with compat|      |✔️|                  `GH-80214`_
Method ``get_depth_layer`` adds a new ``msaa`` optional parameter                                                         |✔️|                 |✔️ with compat|      |✔️|                  `GH-80214`_
Method ``get_velocity_layer`` adds a new ``msaa`` optional parameter                                                      |✔️|                 |✔️ with compat|      |✔️|                  `GH-80214`_
Method ``get_color_texture`` adds a new ``msaa`` optional parameter                                                       |✔️|                 |✔️ with compat|      |✔️|                  `GH-80214`_
Method ``get_depth_texture`` adds a new ``msaa`` optional parameter                                                       |✔️|                 |✔️ with compat|      |✔️|                  `GH-80214`_
Method ``get_velocity_texture`` adds a new ``msaa`` optional parameter                                                    |✔️|                 |✔️ with compat|      |✔️|                  `GH-80214`_
========================================================================================================================  ===================  ====================  ====================  ===========

.. note::

    While the values of the enum fields in ``RenderingDevice.InitialAction`` and ``RenderingDevice.FinalAction`` changed,
    the only method that consumed them (``draw_list_begin``) added a compatibility method which supports the old values.
    So in practice it doesn't break compatibility.

.. note::

    In C#, the enum ``RenderingDevice.DriverResource`` breaks compatibility because of the way the bindings generator
    detects the enum prefix. New members were added in `GH-83452`_ to the enum that caused the enum members to be
    renamed.

Text
~~~~

========================================================================================================================  ===================  ====================  ====================  ===========
Change                                                                                                                    GDScript Compatible  C# Binary Compatible  C# Source Compatible  Introduced
========================================================================================================================  ===================  ====================  ====================  ===========
**Font**
Method ``find_variation`` adds a new ``baseline_offset`` optional parameter                                               |✔️|                 |✔️ with compat|      |✔️|                  `GH-87668`_
**RichTextLabel**
Method ``push_meta`` adds a new ``underline_mode`` optional parameter                                                     |✔️|                 |✔️ with compat|      |✔️|                  `GH-89024`_
**TextServer**
Method ``shaped_text_get_word_breaks`` adds a new optional ``skip_grapheme_flags`` parameter                              |✔️|                 |✔️ with compat|      |✔️|                  `GH-90732`_
**TextServerExtension**
Method ``_shaped_text_get_word_breaks`` adds a new ``skip_grapheme_flags`` parameter                                      |❌|                 |❌|                  |❌|                  `GH-90732`_
========================================================================================================================  ===================  ====================  ====================  ===========

Audio
~~~~~

========================================================================================================================  ===================  ====================  ====================  ===========
Change                                                                                                                    GDScript Compatible  C# Binary Compatible  C# Source Compatible  Introduced
========================================================================================================================  ===================  ====================  ====================  ===========
**AudioStreamPlaybackPolyphonic**
Method ``play_stream`` adds new ``playback_type``, and ``bus`` optional parameters                                        |✔️|                 |✔️ with compat|      |✔️|                  `GH-91382`_
========================================================================================================================  ===================  ====================  ====================  ===========

Navigation
~~~~~~~~~~

========================================================================================================================  ===================  ====================  ====================  ===========
Change                                                                                                                    GDScript Compatible  C# Binary Compatible  C# Source Compatible  Introduced
========================================================================================================================  ===================  ====================  ====================  ===========
**AStar2D**
Method ``get_id_path`` adds new ``allow_partial_path`` optional parameter                                                 |✔️|                 |✔️ with compat|      |✔️|                  `GH-88047`_
Method ``get_point_path`` adds new ``allow_partial_path`` optional parameter                                              |✔️|                 |✔️ with compat|      |✔️|                  `GH-88047`_
**AStar3D**
Method ``get_id_path`` adds new ``allow_partial_path`` optional parameter                                                 |✔️|                 |✔️ with compat|      |✔️|                  `GH-88047`_
Method ``get_point_path`` adds new ``allow_partial_path`` optional parameter                                              |✔️|                 |✔️ with compat|      |✔️|                  `GH-88047`_
**AStarGrid2D**
Method ``get_id_path`` adds new ``allow_partial_path`` optional parameter                                                 |✔️|                 |✔️ with compat|      |✔️|                  `GH-88047`_
Method ``get_point_path`` adds new ``allow_partial_path`` optional parameter                                              |✔️|                 |✔️ with compat|      |✔️|                  `GH-88047`_
**NavigationRegion2D**
Property ``avoidance_layers`` removed                                                                                     |❌|                 |❌|                  |❌|                  `GH-90747`_
Property ``constrain_avoidance`` removed                                                                                  |❌|                 |❌|                  |❌|                  `GH-90747`_
Method ``get_avoidance_layer_value`` removed                                                                              |❌|                 |❌|                  |❌|                  `GH-90747`_
Method ``set_avoidance_layer_value`` removed                                                                              |❌|                 |❌|                  |❌|                  `GH-90747`_
========================================================================================================================  ===================  ====================  ====================  ===========

.. note::

    The constrain avoidance feature in ``NavigationRegion2D`` was experimental and has been discontinued with no
    replacement.

TileMap
~~~~~~~

========================================================================================================================  ===================  ====================  ====================  ===========
Change                                                                                                                    GDScript Compatible  C# Binary Compatible  C# Source Compatible  Introduced
========================================================================================================================  ===================  ====================  ====================  ===========
**TileData**
Method ``get_navigation_polygon`` adds new ``flip_h``, ``flip_v``, and ``transpose`` optional parameters                  |✔️|                 |✔️ with compat|      |✔️|                  `GH-84660`_
Method ``get_occluder`` adds new ``flip_h``, ``flip_v``, and ``transpose`` optional parameters                            |✔️|                 |✔️ with compat|      |✔️|                  `GH-84660`_
========================================================================================================================  ===================  ====================  ====================  ===========

XR
~~

========================================================================================================================  ===================  ====================  ====================  ===========
Change                                                                                                                    GDScript Compatible  C# Binary Compatible  C# Source Compatible  Introduced
========================================================================================================================  ===================  ====================  ====================  ===========
**WebXRInterface**
Method ``get_input_source_tracker`` changes return type from ``XRPositionalTracker`` to ``XRControllerTracker``           |✔️|                 |❌|                  |✔️|                  `GH-90645`_
**XRServer**
Method ``get_tracker`` changes return type from ``XRPositionalTracker`` to ``XRTracker``                                  |✔️|                 |❌|                  |❌|                  `GH-90645`_
========================================================================================================================  ===================  ====================  ====================  ===========

Editor plugins
~~~~~~~~~~~~~~

========================================================================================================================  ===================  ====================  ====================  ===========
Change                                                                                                                    GDScript Compatible  C# Binary Compatible  C# Source Compatible  Introduced
========================================================================================================================  ===================  ====================  ====================  ===========
**EditorInspectorPlugin**
Method ``add_property_editor`` adds a new ``label`` optional parameter                                                    |✔️|                 |✔️ with compat|      |✔️|                  `GH-92322`_
**EditorPlugin**
Method ``add_control_to_bottom_panel`` adds a new ``shortcut`` optional parameter                                         |✔️|                 |✔️ with compat|      |✔️|                  `GH-88081`_
Method ``add_control_to_dock`` adds a new ``shortcut`` optional parameter                                                 |✔️|                 |✔️ with compat|      |✔️|                  `GH-88081`_
**EditorSceneFormatImporterFBX**
Type renamed to ``EditorSceneFormatImporterFBX2GLTF``                                                                     |❌|                 |❌|                  |❌|                  `GH-81746`_
========================================================================================================================  ===================  ====================  ====================  ===========

Behavior changes
----------------

In 4.3, some behavior changes have been introduced, which might require you to adjust your project.

Core
~~~~

.. note::

    Binary serialization was modified to fix some issues with the serialization of scripted Objects and typed Arrays (`GH-78219`_).
    This breaks compat with script encoding/decoding.

.. note::

    ``PackedByteArray`` is now able to use a more compact base64 encoding for storage. But the trade-off is that it breaks
    compatibility, meaning that older versions of Godot may not be able to open resources saved by 4.3 (`GH-89186`_).

    To maximize compatibility, this new storage format will only be enabled for resources and scenes that contain large
    PackedByteArrays for now. Support for this new format will also be added in patch updates for older versions of Godot.
    Once all supported Godot versions are able to read the new format, we will gradually retire the compatibility measures
    and have all resources and scenes use the new storage format.

.. note::

    In C#, the ``Transform3D.InterpolateWith`` implementation was fixed to use the right order of operations, applying the rotation before the scale (`GH-89843`_).

.. note::

    In C#, the ``Aabb.GetSupport`` implementation was fixed to properly return the support vector (`GH-88919`_).

.. note::

    In C#, the Variant types' ``ToString`` implementation now defaults to using the ``InvariantCulture`` (`GH-89547`_)
    which means ``Vector2(1.2, 3.4)`` is formatted using ``.`` as the decimal separator independently of the language
    of the operating system that the program is running on.

Animation
~~~~~~~~~

.. note::

    ``AnimationMixer`` replaced its Capture mode with a new Capture feature that works much better than the old one,
    this replaces the existing cache (`GH-86715`_).

.. note::

    ``AnimationNode`` has a reworked process for retrieving the semantic time info. This ensures that time-related
    behavior works as expected, but changes the blending behavior. Implementors of the ``_process`` virtual method
    should also note that this method is now deprecated and will be replaced by a new one in the future (`GH-87171`_).

More information about the changes to Animation can be found in the
`Migrating Animations from Godot 4.0 to 4.3 <https://godotengine.org/article/migrating-animations-from-godot-4-0-to-4-3>`__
article.

GUI nodes
~~~~~~~~~

.. note::

    The default font outline color was changed from white to black (`GH-54641`_).

.. note::

    The ``auto_translate`` property is deprecated in favor of the ``auto_translate_mode`` property which is now in ``Node`` (`GH-87530`_).
    The default value for ``auto_translate_mode`` is ``AUTO_TRANSLATE_INHERIT``, which means nodes inherit the ``auto_translate_mode`` value
    from their parent. This means, existing nodes with the ``auto_translate`` property set to ``true`` may no longer be translated if they
    are children of a node with the ``auto_translate`` property set to ``false``.

Multiplayer
~~~~~~~~~~~

.. note::

    The ``SceneMultiplayer`` caching protocol was changed to send the received ID instead of the Node path when sending a node removal confirmation packet (`GH-90027`_).

    This is a breaking change for the high-level multiplayer protocol making it incompatible with previous Godot versions.
    Upgrade both your server and client versions to Godot 4.3 to handle this change gracefully.

    Note that high-level multiplayer facilities are only ever meant to be compatible with server and client using the same Godot version. It is recommended to implement some kind of version checking.

Rendering
~~~~~~~~~

.. note::

    Decals now convert the modulate color from an sRGB color to a linear color, like all other inputs, to ensure proper
    blending (`GH-89849`_). Existing projects that were using the decal's modulate property will notice a change in
    their visuals.

.. note::

    The reverse Z depth buffer technique is now implemented. This may break compatibility for some shaders.
    Read the `Introducing Reverse Z (AKA I'm sorry for breaking your shader) <https://godotengine.org/article/introducing-reverse-z/>`__
    article for more information and guidance on how to fix common scenarios.

TileMap
~~~~~~~

.. note::

    ``TileMap`` layers were moved to individual nodes (`GH-87379`_ and `GH-89179`_).

Android
~~~~~~~

.. note::

    Android permissions are no longer requested automatically because it goes against the recommended best practices (`GH-87080`_).
    Use the ``request_permission`` method in ``OS`` and the ``on_request_permissions_result`` signal on ``MainLoop`` to request
    permissions and wait for the user response.

.. |❌| replace:: :abbr:`❌ (This API breaks compatibility.)`
.. |✔️| replace:: :abbr:`✔️ (This API does not break compatibility.)`
.. |✔️ with compat| replace:: :abbr:`✔️ (This API does not break compatibility. A compatibility method was added.)`

.. _GH-54641: https://github.com/godotengine/godot/pull/54641
.. _GH-78219: https://github.com/godotengine/godot/pull/78219
.. _GH-80214: https://github.com/godotengine/godot/pull/80214
.. _GH-81746: https://github.com/godotengine/godot/pull/81746
.. _GH-83452: https://github.com/godotengine/godot/pull/83452
.. _GH-84660: https://github.com/godotengine/godot/pull/84660
.. _GH-84792: https://github.com/godotengine/godot/pull/84792
.. _GH-84976: https://github.com/godotengine/godot/pull/84976
.. _GH-85393: https://github.com/godotengine/godot/pull/85393
.. _GH-86629: https://github.com/godotengine/godot/pull/86629
.. _GH-86661: https://github.com/godotengine/godot/pull/86661
.. _GH-86687: https://github.com/godotengine/godot/pull/86687
.. _GH-86715: https://github.com/godotengine/godot/pull/86715
.. _GH-87080: https://github.com/godotengine/godot/pull/87080
.. _GH-87171: https://github.com/godotengine/godot/pull/87171
.. _GH-87379: https://github.com/godotengine/godot/pull/87379
.. _GH-87530: https://github.com/godotengine/godot/pull/87530
.. _GH-87668: https://github.com/godotengine/godot/pull/87668
.. _GH-87888: https://github.com/godotengine/godot/pull/87888
.. _GH-88047: https://github.com/godotengine/godot/pull/88047
.. _GH-88081: https://github.com/godotengine/godot/pull/88081
.. _GH-88418: https://github.com/godotengine/godot/pull/88418
.. _GH-88791: https://github.com/godotengine/godot/pull/88791
.. _GH-88919: https://github.com/godotengine/godot/pull/88919
.. _GH-89024: https://github.com/godotengine/godot/pull/89024
.. _GH-89179: https://github.com/godotengine/godot/pull/89179
.. _GH-89186: https://github.com/godotengine/godot/pull/89186
.. _GH-89419: https://github.com/godotengine/godot/pull/89419
.. _GH-89547: https://github.com/godotengine/godot/pull/89547
.. _GH-89843: https://github.com/godotengine/godot/pull/89843
.. _GH-89849: https://github.com/godotengine/godot/pull/89849
.. _GH-89851: https://github.com/godotengine/godot/pull/89851
.. _GH-90027: https://github.com/godotengine/godot/pull/90027
.. _GH-90575: https://github.com/godotengine/godot/pull/90575
.. _GH-90645: https://github.com/godotengine/godot/pull/90645
.. _GH-90732: https://github.com/godotengine/godot/pull/90732
.. _GH-90747: https://github.com/godotengine/godot/pull/90747
.. _GH-91382: https://github.com/godotengine/godot/pull/91382
.. _GH-92322: https://github.com/godotengine/godot/pull/92322
.. _GH-92861: https://github.com/godotengine/godot/pull/92861
