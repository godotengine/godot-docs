.. _doc_upgrading_to_godot_4:

Upgrading to Godot 4
====================

TODO: https://github.com/godotengine/godot-proposals/issues/387#issuecomment-1251909261

Should I upgrade to Godot 4?
----------------------------

Before beginning the upgrade process, it's worth thinking about the advantages
and disadvantages that upgrading would bring to your project.

Advantages of upgrading
^^^^^^^^^^^^^^^^^^^^^^^

Along with the new features present in 4.0, upgrading gives the following advantages:

- Many bugs are fixed in 4.0, but cannot be resolved in 3.x for various reasons
  (such as graphics API differences or backwards compatibility).
- 4.x will enjoy a longer :ref:`support period <doc_release_policy>`. Godot 3.x
  will continue to be supported for some time after 4.0 is released, but it will
  eventually stop receiving support.

Disadvantages of upgrading
^^^^^^^^^^^^^^^^^^^^^^^^^^

If you don't *need* any features present in Godot 4.0, you may want to stay on
Godot 3.x for the following reasons:

- Godot 4's baseline hardware requirements (such as memory usage) are slightly
  higher, both for the editor and exported projects. This was required for the
  implementation of some core optimizations.
- Godot 4 does not and will not have support for GLES2 rendering.
  (There is still support for GLES3 rendering using the new OpenGL backend,
  which means that devices without Vulkan support can still run Godot 4.)

  - If you are targeting **very** old hardware such as Intel Sandy Bridge (2nd
    generation) integrated graphics, this will prevent the project from running
    on such hardware after upgrading.
    `Software OpenGL implementations <https://github.com/pal1000/mesa-dist-win>`__
    can be used to bypass this limitation, but they're too slow for gaming.

Running the project upgrade tool
--------------------------------

.. warning::

    **Make a full backup of your project** before upgrading! The project upgrade
    tool will *not* perform any backups of the project that is being upgraded.

    You can backup a project by using version control, or by copying the project
    folder to another location.

To use the project upgrade tool:

1. Open the Godot 4 project manager.
2. Import the Godot 3.x project using the **Import** button, or use the **Scan**
   button to find the project within a folder.
3. Double-click the imported project (or select the project then choose **Edit**).
4. You will see a dialog appearing with two options: **Convert project.godot
   Only** and **Convert Full Project**. After ensuring your project is backed up
   (see the above warning), choose **Convert Full Project**. **Convert
   project.godot Only** is intended to be used for advanced use cases *only*, in
   case the conversion tool fails.
5. Wait until the project conversion process finishes. This can take up to a few
   minutes for large projects with lots of scenes.
6. When the project manager interface becomes available again, double-click the
   project (or select the project then choose **Edit**) to open it in the
   editor.

.. note::

    Only Godot 3.0 and later projects can be upgraded using the project
    conversion tool found in the Godot 4 editor.

    Projects made using Godot versions older than 3.0 must follow a 2-step
    process:

    1. Upgrade the project to Godot 3 using the **Tools > Export to Godot 3.0**
       option in the Godot 2.1.6 editor. Open the upgraded project in the Godot
       3.x editor, then manually fix the project to make sure it looks and
       runs correctly.
    2. Only *after* performing step 1, you may upgrade the project to Godot 4.

Fixing the project after running the project upgrade tool
---------------------------------------------------------

After upgrading the project, you may notice that certain things don't look as
they should. Scripts will likely contain various errors as well (possibly
hundreds in large projects). This is because the project upgrade tool cannot
cater to all situations. Therefore, a large part of the upgrade process remains
manual.

Automatically renamed nodes and resources
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The list below refers to the nodes' new names in Godot 4.0. In the transition
between Godot 3.x and 4.0, dozens of nodes were renamed. 3D nodes had a ``3D``
prefix added to them for consistency with their 2D counterparts. This conversion
is automatic.

For ease of searching, this table lists all nodes and resources that were
renamed in a way that does not involve only adding a ``3D`` suffix to the old name:

+-----------------------------------------+-------------------------------------------+
| Old name (Godot 3.x)                    | New name (Godot 4)                        |
+=========================================+===========================================+
| AnimatedSprite                          | AnimatedSprite2D                          |
+-----------------------------------------+-------------------------------------------+
| ARVRCamera                              | XRCamera3D                                |
+-----------------------------------------+-------------------------------------------+
| ARVRController                          | XRController3D                            |
+-----------------------------------------+-------------------------------------------+
| ARVRAnchor                              | XRAnchor3D                                |
+-----------------------------------------+-------------------------------------------+
| ARVRInterface                           | XRInterface                               |
+-----------------------------------------+-------------------------------------------+
| ARVROrigin                              | XROrigin3D                                |
+-----------------------------------------+-------------------------------------------+
| ARVRPositionalTracker                   | XRPositionalTracker                       |
+-----------------------------------------+-------------------------------------------+
| ARVRServer                              | XRServer                                  |
+-----------------------------------------+-------------------------------------------+
| CubeMesh                                | BoxMesh                                   |
+-----------------------------------------+-------------------------------------------+
| EditorSpatialGizmo                      | EditorNode3DGizmo                         |
+-----------------------------------------+-------------------------------------------+
| EditorSpatialGizmoPlugin                | EditorNode3DGizmoPlugin                   |
+-----------------------------------------+-------------------------------------------+
| GIProbe                                 | VoxelGI                                   |
+-----------------------------------------+-------------------------------------------+
| GIProbeData                             | VoxelGIData                               |
+-----------------------------------------+-------------------------------------------+
| GradientTexture                         | GradientTexture1D                         |
+-----------------------------------------+-------------------------------------------+
| KinematicBody                           | CharacterBody3D                           |
+-----------------------------------------+-------------------------------------------+
| KinematicBody2D                         | CharacterBody2D                           |
+-----------------------------------------+-------------------------------------------+
| Light2D                                 | PointLight2D                              |
+-----------------------------------------+-------------------------------------------+
| LineShape2D                             | WorldBoundaryShape2D                      |
+-----------------------------------------+-------------------------------------------+
| Listener                                | AudioListener3D                           |
+-----------------------------------------+-------------------------------------------+
| NavigationMeshInstance                  | NavigationRegion3D                        |
+-----------------------------------------+-------------------------------------------+
| NavigationPolygonInstance               | NavigationRegion2D                        |
+-----------------------------------------+-------------------------------------------+
| Navigation2DServer                      | NavigationServer2D                        |
+-----------------------------------------+-------------------------------------------+
| PanoramaSky                             | Sky                                       |
+-----------------------------------------+-------------------------------------------+
| Particles                               | GPUParticles3D                            |
+-----------------------------------------+-------------------------------------------+
| Particles2D                             | GPUParticles2D                            |
+-----------------------------------------+-------------------------------------------+
| ParticlesMaterial                       | ParticleProcessMaterial                   |
+-----------------------------------------+-------------------------------------------+
| Physics2DDirectBodyState                | PhysicsDirectBodyState2D                  |
+-----------------------------------------+-------------------------------------------+
| Physics2DDirectSpaceState               | PhysicsDirectSpaceState2D                 |
+-----------------------------------------+-------------------------------------------+
| Physics2DServer                         | PhysicsServer2D                           |
+-----------------------------------------+-------------------------------------------+
| Physics2DShapeQueryParameters           | PhysicsShapeQueryParameters2D             |
+-----------------------------------------+-------------------------------------------+
| Physics2DTestMotionResult               | PhysicsTestMotionResult2D                 |
+-----------------------------------------+-------------------------------------------+
| PhysicsDirectBodyState                  | PhysicsDirectBodyState3D                  |
+-----------------------------------------+-------------------------------------------+
| PhysicsDirectSpaceState                 | PhysicsDirectSpaceState3D                 |
+-----------------------------------------+-------------------------------------------+
| PlaneShape                              | WorldBoundaryShape3D                      |
+-----------------------------------------+-------------------------------------------+
| Position2D                              | Marker2D                                  |
+-----------------------------------------+-------------------------------------------+
| Position3D                              | Marker3D                                  |
+-----------------------------------------+-------------------------------------------+
| ProceduralSky                           | Sky                                       |
+-----------------------------------------+-------------------------------------------+
| RayShape                                | SeparationRayShape3D                      |
+-----------------------------------------+-------------------------------------------+
| RayShape2D                              | SeparationRayShape2D                      |
+-----------------------------------------+-------------------------------------------+
| ShortCut                                | Shortcut                                  |
+-----------------------------------------+-------------------------------------------+
| Spatial                                 | Node3D                                    |
+-----------------------------------------+-------------------------------------------+
| SpatialGizmo                            | Node3DGizmo                               |
+-----------------------------------------+-------------------------------------------+
| SpatialMaterial                         | StandardMaterial3D                        |
+-----------------------------------------+-------------------------------------------+
| Sprite                                  | Sprite2D                                  |
+-----------------------------------------+-------------------------------------------+
| StreamTexture                           | CompressedTexture2D                       |
+-----------------------------------------+-------------------------------------------+
| TextureProgress                         | TextureProgressBar                        |
+-----------------------------------------+-------------------------------------------+
| VideoPlayer                             | VideoStreamPlayer                         |
+-----------------------------------------+-------------------------------------------+
| ViewportContainer                       | SubViewportContainer                      |
+-----------------------------------------+-------------------------------------------+
| Viewport                                | SubViewport                               |
+-----------------------------------------+-------------------------------------------+
| VisibilityEnabler                       | VisibleOnScreenEnabler3D                  |
+-----------------------------------------+-------------------------------------------+
| VisibilityNotifier                      | VisibleOnScreenNotifier3D                 |
+-----------------------------------------+-------------------------------------------+
| VisibilityNotifier2D                    | VisibleOnScreenNotifier2D                 |
+-----------------------------------------+-------------------------------------------+
| VisibilityNotifier3D                    | VisibleOnScreenNotifier3D                 |
+-----------------------------------------+-------------------------------------------+
| VisualServer                            | RenderingServer                           |
+-----------------------------------------+-------------------------------------------+
| VisualShaderNodeScalarConstant          | VisualShaderNodeFloatConstant             |
+-----------------------------------------+-------------------------------------------+
| VisualShaderNodeScalarFunc              | VisualShaderNodeFloatFunc                 |
+-----------------------------------------+-------------------------------------------+
| VisualShaderNodeScalarOp                | VisualShaderNodeFloatOp                   |
+-----------------------------------------+-------------------------------------------+
| VisualShaderNodeScalarClamp             | VisualShaderNodeClamp                     |
+-----------------------------------------+-------------------------------------------+
| VisualShaderNodeVectorClamp             | VisualShaderNodeClamp                     |
+-----------------------------------------+-------------------------------------------+
| VisualShaderNodeScalarInterp            | VisualShaderNodeMix                       |
+-----------------------------------------+-------------------------------------------+
| VisualShaderNodeVectorInterp            | VisualShaderNodeMix                       |
+-----------------------------------------+-------------------------------------------+
| VisualShaderNodeVectorScalarMix         | VisualShaderNodeMix                       |
+-----------------------------------------+-------------------------------------------+
| VisualShaderNodeScalarSmoothStep        | VisualShaderNodeSmoothStep                |
+-----------------------------------------+-------------------------------------------+
| VisualShaderNodeVectorSmoothStep        | VisualShaderNodeSmoothStep                |
+-----------------------------------------+-------------------------------------------+
| VisualShaderNodeVectorScalarSmoothStep  | VisualShaderNodeSmoothStep                |
+-----------------------------------------+-------------------------------------------+
| VisualShaderNodeVectorScalarStep        | VisualShaderNodeStep                      |
+-----------------------------------------+-------------------------------------------+
| VisualShaderNodeScalarSwitch            | VisualShaderNodeSwitch                    |
+-----------------------------------------+-------------------------------------------+
| VisualShaderNodeScalarTransformMult     | VisualShaderNodeTransformOp               |
+-----------------------------------------+-------------------------------------------+
| VisualShaderNodeScalarDerivativeFunc    | VisualShaderNodeDerivativeFunc            |
+-----------------------------------------+-------------------------------------------+
| VisualShaderNodeVectorDerivativeFunc    | VisualShaderNodeDerivativeFunc            |
+-----------------------------------------+-------------------------------------------+
| VisualShaderNodeBooleanUniform          | VisualShaderNodeBooleanParameter          |
+-----------------------------------------+-------------------------------------------+
| VisualShaderNodeColorUniform            | VisualShaderNodeColorParameter            |
+-----------------------------------------+-------------------------------------------+
| VisualShaderNodeScalarUniform           | VisualShaderNodeFloatParameter            |
+-----------------------------------------+-------------------------------------------+
| VisualShaderNodeCubeMapUniform          | VisualShaderNodeCubeMapParameter          |
+-----------------------------------------+-------------------------------------------+
| VisualShaderNodeTextureUniform          | VisualShaderNodeTexture2DParameter        |
+-----------------------------------------+-------------------------------------------+
| VisualShaderNodeTextureUniformTriplanar | VisualShaderNodeTextureParameterTriplanar |
+-----------------------------------------+-------------------------------------------+
| VisualShaderNodeTransformUniform        | VisualShaderNodeTransformParameter        |
+-----------------------------------------+-------------------------------------------+
| VisualShaderNodeVec3Uniform             | VisualShaderNodeVec3Parameter             |
+-----------------------------------------+-------------------------------------------+
| VisualShaderNodeUniform                 | VisualShaderNodeParameter                 |
+-----------------------------------------+-------------------------------------------+
| VisualShaderNodeUniformRef              | VisualShaderNodeParameterRef              |
+-----------------------------------------+-------------------------------------------+

If you cannot find a node or resource in the list below, refer to the above
table to find its new name.

.. _doc_upgrading_to_godot_4_manual_rename:

Manually renaming methods, properties, signals and constants
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Due to how the project upgrade tool works, not all
:abbr:`API (Application Programming Interface)` renames can be performed automatically.


.. tip::

    You can use the **Replace in Files** dialog to speed up replacement by pressing
    :kbd:`Ctrl + Shift + R` while the script editor is open. However, be careful
    as the Replace in Files dialog doesn't offer any way to undo a replacement.
    Use version control to commit your upgrade work regularly.
    Command line tools such as `sd <https://github.com/chmln/sd>`__ can also be used
    if you need something more flexible than the editor's Replace in Files dialog.

    If using C#, remember to search for outdated API usage with PascalCase
    notation in the project (and perform the replacement with PascalCase
    notation).

**Methods**

- File and Directory classes were replaced by :ref:`class_FileAccess` and
  :ref:`class_DirAccess`, which have an entirely different API. Several methods
  are now static, which means you can call them directly on FileAccess or
  DirAccess without having to create an instance of that class.
- Screen and window-related methods from the :ref:`class_OS` singleton (such as
  ``OS.get_screen_size()``) were moved to the :ref:`class_DisplayServer` singleton.
  Method naming was also changed to use the
  ``DisplayServer.<object>_<get/set>_property()`` form instead. For example,
  ``OS.get_screen_size()`` becomes ``DisplayServer.screen_get_size()``.
- Time and date methods from the :ref:`class_OS` singleton were moved to the
  :ref:`class_Time` singleton.
  (The Time singleton is also available in Godot 3.5 and later.)
- You may have to replace some ``instance()`` calls with ``instantiate()``. The
  converter *should* handle this automatically, but this relies on custom code that
  may not work in 100% of situations.
- AcceptDialog's ``set_autowrap()`` is now ``set_autowrap_mode()``.
- AnimationNode's ``process()`` is now ``_process()``
  (note the leading underscore, which denotes a virtual method).
- AStar2D and AStar3D's ``get_points()`` is now ``get_points_id()``.
- BaseButton's ``set_event()`` is now ``set_shortcut()``.
- Camera2D's ``get_v_offset()`` is now ``get_drag_vertical_offset()``.
- Camera2D's ``set_v_offset()`` is now ``set_drag_vertical_offset()``.
- Camera2D's ``make_current()`` is now ``set_current()``.
- Control's ``set_tooltip()`` is now ``set_tooltip_text()``.
- EditorNode3DGizmoPlugin's ``create_gizmo()`` is now ``_create_gizmo()``
  (note the leading underscore, which denotes a virtual method).
- ENetMultiplayerPeer's ``get_peer_port()`` is now ``get_peer()``.
- FileDialog's ``get_mode()`` is now ``get_file_mode()``.
- FileDialog's ``set_mode()`` is now ``set_file_mode()``.
- GraphNode's ``get_offset()`` is now ``get_position_offset()``.
- ItemList's ``get_v_scroll()`` is now ``get_v_scroll_bar()``.
- MultiPlayerAPI's ``get_network_connected_peers()`` is now ``get_peers()``.
- MultiPlayerAPI's ``get_network_peer()`` is now ``get_peer()``.
- MultiPlayerAPI's ``get_network_unique_id()`` is now ``get_unique_id()``.
- MultiPlayerAPI's ``has_network_peer()`` is now ``has_multiplayer_peer()``.
- PacketPeerUDP's ``is_listening()`` is now ``is_bound()``.
- PacketPeerUDP's ``listen()`` is now ``bound()``.
- ParticleProcessMaterial's ``set_flag()`` is now ``set_particle_flag()``.
- ResourceFormatLoader's ``get_dependencies()`` is now ``_get_dependencies()``
  (note the leading underscore, which denotes a virtual method).
- Shortcut's ``is_valid()`` is now ``has_valid_event()``.

**Properties**

.. note::

    If a property is listed here, its associated getter and setter methods must
    also be renamed manually if used in the project. For example, PathFollow2D
    and PathFollow3D's ``set_offset()`` and ``get_offset()`` must be renamed to
    ``set_progress()`` and ``get_progress()`` respectively.

- Control's ``margin`` is now ``offset``.
- MultiPlayerAPI's ``refuse_new_network_connections`` is now ``refuse_new_connections``.
- PathFollow2D and PathFollow3D's ``offset`` is now ``progress``.
- The ``extents`` property on CSG nodes and VoxelGI will have to be replaced
  with ``size``, with the set value halved (as they're no longer half-extents).
  This also affects its setter/getter methods ``set_extents()`` and
  ``get_extents()``.
- The ``Engine.editor_hint`` property was removed in favor of the
  ``Engine.is_editor_hint()`` *method*. This is because it's read-only, and
  properties in Godot are not used for read-only values.

**Enums**

- CPUParticles2D's ``FLAG_MAX`` is now ``PARTICLE_FLAG_MAX``.

**Signals**

- FileSystemDock's ``instantiate`` is now ``instance``.
- CanvasItem's ``hide`` is now ``hidden``. This rename does **not** apply to the
  ``hide()`` method, only the signal.
- Tween's ``tween_all_completed`` is now ``loop_finished``.
- EditorSettings' ``changed`` is now ``settings_changed``.

**Constants**

- Color names are now uppercase and use underscores between words.
  For example, ``Color.palegreen`` is now ``Color.PALE_GREEN``.
- MainLoop's ``NOTIFICATION_`` constants were moved to global scope, which means
  you can remove the ``MainLoop.`` prefix when referencing them.
- MainLoop's ``NOTIFICATION_WM_QUIT_REQUEST`` is now ``NOTIFICATION_WM_CLOSE_REQUEST``.

Checking project settings
^^^^^^^^^^^^^^^^^^^^^^^^^

Several project settings were renamed, and some of them had their enums changed
in incompatible ways (such as shadow filter quality). This means you may need to
set some project settings' values again. Make sure the **Advanced** toggle is
enabled in the project settings dialog so you can see all project settings.

Checking Environment settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Graphics quality settings were moved from Environment properties to project
settings. This was done to make run-time quality adjustments easier, without
having to access the currently active Environment resource then modify its
properties.

As a result, you will have to configure Environment quality settings in the
project settings as old Environment quality settings aren't converted
automatically to project settings.

If you have a graphics settings menu that changed environment properties in
Godot 3.x, you will have to change its code to call :ref:`class_RenderingServer`
methods that affect environment effects' quality. Only the "base" toggle of each
environment effect and its visual knobs remain within the Environment resource.

Updating scripts to take backwards-incompatible changes into account
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Some changes performed between Godot 3.x and 4 are not renames, but they still
break backwards compatibility due to different default behavior.

The most notable examples of this are:

- Built-in scripts that are :ref:`tool scripts <doc_running_code_in_the_editor>`
  do not get the the ``tool`` keyword converted to the ``@tool`` annotation.
- ``randomize()`` is now automatically called on project load, so deterministic
  randomness with the global RandomNumberGenerate instance requires manually
  setting a seed in a script's ``_ready()`` function.
- ``OS.get_system_time_secs()`` should be converted to ``Time.get_time_dict_from_system()["second"]``.
- A :ref:`class_StreamPeerTCP` must have ``poll()`` called on it to update its
  state, instead of relying on ``get_status()`` automatically polling:
  `GH-59582 <https://github.com/godotengine/godot/pull/59582>`__
- ``is_connected_to_host()`` was removed from StreamPeerTCP and PacketPeerUDP as
  per `GH-59582 <https://github.com/godotengine/godot/pull/59582>`__.
  ``get_status()`` can be used in StreamPeerTCP instead.
  ``is_socket_connected()`` can be used in PacketPeerUDP instead.

**Removed or replaced nodes/resources**

This lists all nodes that were replaced by another node requiring different
configuration. The setup must be done from scratch again, as the project
converter doesn't support updating existing setups:

+---------------------+-----------------------+----------------------------------------------------------------------+
| Removed node        | Closest approximation | Comment                                                              |
+=====================+=======================+======================================================================+
| AnimationTreePlayer | AnimationTree         | AnimationTreePlayer was deprecated since Godot 3.1.                  |
+---------------------+-----------------------+----------------------------------------------------------------------+
| BakedLightmap       | LightmapGI            | See :ref:`doc_baked_lightmaps`.                                      |
+---------------------+-----------------------+                                                                      |
| BakedLightmapData   | LightmapGIData        |                                                                      |
+---------------------+-----------------------+----------------------------------------------------------------------+
| BitmapFont          | FontFile              | See :ref:`doc_gui_using_fonts`.                                      |
+---------------------+-----------------------+                                                                      |
| DynamicFont         | FontFile              |                                                                      |
+---------------------+-----------------------+                                                                      |
| DynamicFontData     | FontFile              |                                                                      |
+---------------------+-----------------------+----------------------------------------------------------------------+
| Navigation3D        | Node3D                | Replaced by other Navigation nodes.                                  |
+---------------------+-----------------------+----------------------------------------------------------------------+
| Navigation2D        | Node2D                | Replaced by other Navigation nodes.                                  |
+---------------------+-----------------------+----------------------------------------------------------------------+
| OpenSimplexNoise    | FastNoiseLite         | Has different parameters and more noise types such as cellular. No   |
|                     |                       | support for 4D noise as it's absent from the FastNoiseLite library.  |
+---------------------+-----------------------+----------------------------------------------------------------------+
| ToolButton          | Button                | ToolButton was Button with the **Flat** property enabled by default. |
+---------------------+-----------------------+----------------------------------------------------------------------+
| YSort               | Node2D                | Node2D has a new **Y Sort** property in 4.0.                         |
+---------------------+-----------------------+----------------------------------------------------------------------+
| ProximityGroup      | Node3D                | :ref:`class_VisibleOnScreenNotifier3D` can act as a replacement.     |
+---------------------+-----------------------+----------------------------------------------------------------------+
| Portal              | Node3D                | Portal and room occlusion culling was replaced by raster             |
|                     |                       | :ref:`occlusion culling <doc_occlusion_culling>`                     |
|                     |                       | (OccluderInstance3D node), which requires a different setup process. |
+---------------------+-----------------------+                                                                      |
| Room                | Node3D                |                                                                      |
+---------------------+-----------------------+                                                                      |
| RoomManager         | Node3D                |                                                                      |
+---------------------+-----------------------+                                                                      |
| RoomGroup           | Node3D                |                                                                      |
+---------------------+-----------------------+----------------------------------------------------------------------+
| Occluder            | Node3D                | Geometry occlusion culling was replaced by raster                    |
|                     |                       | :ref:`occlusion culling <doc_occlusion_culling>`                     |
|                     |                       | (OccluderInstance3D node), which requires a different setup process. |
+---------------------+-----------------------+                                                                      |
| OccluderShapeSphere | Resource              |                                                                      |
+---------------------+-----------------------+----------------------------------------------------------------------+

If loading an old project, the node will be replaced with its
*Closest approximation* automatically (even if not using the project upgrade tool).

**Threading changes**

:ref:`Threading <doc_using_multiple_threads>` APIs have changed in 4.0. For
example, the following code snippet in Godot 3.x must be modified to work in 4.0:

::

    # 3.x
    var start_success = new_thread.start(self, "__threaded_background_loader",
        [resource_path, thread_num]
    )

    # 4.0
    var start_success = new_thread.start(__threaded_background_loader.bind(resource_path, thread_num))

``Thread.is_active()`` is no longer used and should be converted to ``Thread.is_alive()``.

.. seealso::

    See the `changelog <https://github.com/godotengine/godot/blob/master/CHANGELOG.md>`__
    for a full list of changes between Godot 3.x and 4.

List of automatically renamed methods, properties, signals and constants
------------------------------------------------------------------------

The `editor/project_converter_3_to_4.cpp <https://github.com/godotengine/godot/blob/master/editor/project_converter_3_to_4.cpp>`__
source file lists all automatic renames performed by the project upgrade tool.
Lines that are commented out refer to API renames that :ref:`cannot be performed automatically <doc_upgrading_to_godot_4_manual_rename>`.

Porting editor settings
-----------------------

Godot 3.x and 4.0 use different editor settings files. This means their settings
can be changed independently from each other.

If you wish to port over your Godot 3.x settings to Godot 4, open the
:ref:`editor settings folder <doc_data_paths_editor_data_paths>` and copy
``editor_settings-3.tres`` to ``editor_settings-4.tres`` while the Godot 4
editor is closed.

.. note::

    Many settings' names and categories have changed since Godot 3.x. Editor settings
    whose name or category has changed won't carry over to Godot 4.0; you will
    have to set their values again.
