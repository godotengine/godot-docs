.. _doc_upgrading_to_godot_4:

Upgrading from Godot 3 to Godot 4
=================================

Should I upgrade to Godot 4?
----------------------------

Before beginning the upgrade process, it's worth thinking about the advantages
and disadvantages that upgrading would bring to your project.

Advantages of upgrading
^^^^^^^^^^^^^^^^^^^^^^^

Along with the
`new features present in 4.0 <https://github.com/godotengine/godot/blob/master/CHANGELOG.md>`__,
upgrading gives the following advantages:

- Many bugs are fixed in 4.0, but cannot be resolved in 3.x for various reasons
  (such as graphics API differences or backwards compatibility).
- 4.x will enjoy a longer :ref:`support period <doc_release_policy>`. Godot 3.x
  will continue to be supported for some time after 4.0 is released, but it will
  eventually stop receiving support.

See :ref:`doc_docs_changelog` for a list of pages documenting new features in Godot 4.0.

Disadvantages of upgrading
^^^^^^^^^^^^^^^^^^^^^^^^^^

If you don't *need* any features present in Godot 4.0, you may want to stay on
Godot 3.x for the following reasons:

- `Godot 3.x is tried and true, while Godot 4 remains in its early stages. <https://godotengine.org/article/release-management-4-0-and-beyond>`__

  - Godot 4.0 is expected to contain workflow and performance issues that Godot
    3.x doesn't have. These issues will be ironed out over time in future
    Godot 4.x releases.

- Godot 4 has fewer third-party tutorials available compared to Godot 3.x.
  If you're new to game engines, you may have a better experience using Godot 3.x
  as a result.
- Godot 4's baseline hardware requirements (such as memory usage) are slightly
  higher, both for the editor and exported projects. This was required for the
  implementation of some core optimizations.
- Since Godot 4 includes more features than Godot 3, Godot 4's binary size for
  exported projects is larger. While this can be mitigated by
  :ref:`optimizing a build for size <doc_optimizing_for_size>`, a 4.0 build with
  a given set of enabled modules will remain larger compared to a 3.x build with
  the same modules. This can be an issue for
  :ref:`exporting to the Web <doc_exporting_for_web>`, as binary size directly
  influences how fast the engine can initialize (regardless of download speed).
- Godot 4 does not and will not have support for GLES2 rendering.
  (There is still support for GLES3 rendering using the new OpenGL backend,
  which means that devices without Vulkan support can still run Godot 4.)

  - If you are targeting **very** old hardware such as Intel Sandy Bridge (2nd
    generation) integrated graphics, this will prevent the project from running
    on such hardware after upgrading.
    `Software OpenGL implementations <https://github.com/pal1000/mesa-dist-win>`__
    can be used to bypass this limitation, but they're too slow for gaming.

Caveats of upgrading
^^^^^^^^^^^^^^^^^^^^

**Since Godot 4 is a complete rewrite in many aspects, some features have
unfortunately been lost in the process.** Some of these features may be restored
in future Godot releases:

- Bullet physics was removed in favor of GodotPhysics. This only affects 3D
  projects that used the default physics engine (which was Bullet) and didn't
  manually change it to GodotPhysics. There are no plans to re-add Bullet physics
  in core, but a third-party add-on could be created for it thanks to
  GDExtension.
- Rendering in 2D is no longer performed in HDR, which means "overbright"
  modulate values have no visible effect. This is planned to be restored at some
  point in the future.
- While rendering still happens in HDR in 3D when using the Forward Plus or
  Forward Mobile backends, Viewports cannot return HDR data anymore. This is
  planned to be restored at some point in the future.
- Mono was replaced by .NET 6. This means exporting C# projects to Android, iOS
  and HTML5 is no longer supported for now. Exporting C# projects to desktop
  platforms is still supported, and as of 4.2 there's experimental support for
  exporting to mobile platforms. Support for exporting C# projects to more
  platforms will be restored in future 4.x releases as upstream support
  improves.

You can find a more complete list of functional regressions by searching for
`issues labeled "regression" but not "bug" on GitHub <https://github.com/godotengine/godot/issues?q=is%3Aissue+is%3Aopen+label%3Aregression+-label%3Abug>`__.

Preparing before the upgrade (optional)
---------------------------------------

If you want to be ready to upgrade to Godot 4 in the future, consider using
:ref:`class_Tweener` and the :ref:`class_Time` singleton in your project. These
classes are both available in Godot 3.5 and later.

This way, you won't be relying on the deprecated Tween node and OS time
functions, both of which are removed in Godot 4.0.

It's also a good idea to rename external shaders so that their extension is
``.gdshader`` instead of ``.shader``. Godot 3.x supports both extensions, but
only ``.gdshader`` is supported in Godot 4.0.

Running the project upgrade tool
--------------------------------

.. warning::

    **Make a full backup of your project** before upgrading! The project upgrade
    tool will *not* perform any backups of the project that is being upgraded.

    You can backup a project by using version control, or by copying the project
    folder to another location.

Using the Project Manager
^^^^^^^^^^^^^^^^^^^^^^^^^

To use the project upgrade tool:

1. Open the Godot 4 Project Manager.
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
6. When the Project Manager interface becomes available again, double-click the
   project (or select the project then choose **Edit**) to open it in the
   editor.

If you hit conversion issues due to some project files being too large or long,
you can use the command line to upgrade the project (see below). This will allow
you to override the converter's size limits.

Using the command line
^^^^^^^^^^^^^^^^^^^^^^

To use the project upgrade tool from the :ref:`command line <doc_command_line_tutorial>`,
it's recommended to validate the project conversion by running the Godot editor binary with the following arguments:

::

    # [<max_file_kb>] [<max_line_size>] are optional arguments.
    # Remove them if you aren't changing their values.
    path/to/godot.binary --path /path/to/project/folder --validate-conversion-3to4 [<max_file_kb>] [<max_line_size>]

If the list of planned upgrades looks good to you, run the following command on
the Godot editor binary to upgrade project files:

::

    # [<max_file_kb>] [<max_line_size>] are optional arguments.
    # Remove them if you aren't changing their values.
    path/to/godot.binary --path /path/to/project/folder --convert-3to4 [<max_file_kb>] [<max_line_size>]

``[<max_file_kb>]`` and ``[<max_line_size>]`` are *optional* arguments to specify
the maximum size of files to be converted (in kilobytes and lines). The default
limits are 4 MB and 100,000 lines respectively. If a file hits either of those
limits, it will not be upgraded by the project converter. This is useful to
prevent large resources from slowing down the upgrade to a crawl.

If you still want large files to be converted by the project upgrade tool,
increase the size limits when running the project upgrade tool. For example,
running the Godot editor binary with those arguments increases both limits by a
10× factor:

::

    path/to/godot.binary --path /path/to/project/folder --convert-3to4 40000 1000000

.. note::

    Only Godot 3.0 and later projects can be upgraded using the project
    conversion tool found in the Godot 4 editor.

    It's recommended to ensure that your project is up-to-date with the latest
    3.x stable release before running the project upgrade tool.

Fixing the project after running the project upgrade tool
---------------------------------------------------------

After upgrading the project, you may notice that certain things don't look as
they should. Scripts will likely contain various errors as well (possibly
hundreds in large projects). This is because the project upgrade tool cannot
cater to all situations. Therefore, a large part of the upgrade process remains
manual.

Automatically renamed nodes and resources
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The list below refers to nodes which were simply renamed for consistency or
clarity in Godot 4.0. The project upgrade tool renames them automatically in
your scripts.

One noteworthy set of renames is 3D nodes, which all got a ``3D`` suffix added for
consistency with their 2D counterparts. For example, ``Area`` is now ``Area3D``.

For ease of searching, this table lists all nodes and resources that were renamed
and are automatically converted, excluding the ones which only involved adding
a ``3D`` suffix to the old name:

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

.. _doc_upgrading_to_godot_4_manual_rename:

Manually renaming methods, properties, signals and constants
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Due to how the project upgrade tool works, not all
:abbr:`API (Application Programming Interface)` renames can be performed automatically.
The list below contains all renames that must be performed manually using the script editor.

If you cannot find a node or resource in the list below, refer to the above
table to find its new name.

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
- CanvasItem's ``update()`` is now ``queue_redraw()``.
- Control's ``set_tooltip()`` is now ``set_tooltip_text()``.
- EditorNode3DGizmoPlugin's ``create_gizmo()`` is now ``_create_gizmo()``
  (note the leading underscore, which denotes a virtual method).
- ENetMultiplayerPeer's ``get_peer_port()`` is now ``get_peer()``.
- FileDialog's ``get_mode()`` is now ``get_file_mode()``.
- FileDialog's ``set_mode()`` is now ``set_file_mode()``.
- GraphNode's ``get_offset()`` is now ``get_position_offset()``.
- GridMap's ``world_to_map()`` is now ``local_to_map()``.
- GridMap's ``map_to_world()`` is now ``map_to_local()``.
- Image's ``get_rect()`` is now ``get_region()``.
- ItemList's ``get_v_scroll()`` is now ``get_v_scroll_bar()``.
- MultiPlayerAPI's ``get_network_connected_peers()`` is now ``get_peers()``.
- MultiPlayerAPI's ``get_network_peer()`` is now ``get_peer()``.
- MultiPlayerAPI's ``get_network_unique_id()`` is now ``get_unique_id()``.
- MultiPlayerAPI's ``has_network_peer()`` is now ``has_multiplayer_peer()``.
- PacketPeerUDP's ``is_listening()`` is now ``is_bound()``.
- PacketPeerUDP's ``listen()`` is now ``bind()``.
- ParticleProcessMaterial's ``set_flag()`` is now ``set_particle_flag()``.
- ResourceFormatLoader's ``get_dependencies()`` is now ``_get_dependencies()``
  (note the leading underscore, which denotes a virtual method).
- SceneTree's ``change_scene()`` is now ``change_scene_to_file()``.
- Shortcut's ``is_valid()`` is now ``has_valid_event()``.
- TileMap's ``world_to_map()`` is now ``local_to_map()``.
- TileMap's ``map_to_world()`` is now ``map_to_local()``.

**Properties**

.. note::

    If a property is listed here, its associated getter and setter methods must
    also be renamed manually if used in the project. For example, PathFollow2D
    and PathFollow3D's ``set_offset()`` and ``get_offset()`` must be renamed to
    ``set_progress()`` and ``get_progress()`` respectively.

- Control's ``margin`` is now ``offset``.
- Label's ``percent_visible`` is now ``visible_ratio``.
- MultiPlayerAPI's ``refuse_new_network_connections`` is now ``refuse_new_connections``.
- PathFollow2D and PathFollow3D's ``offset`` is now ``progress``.
- TextureProgressBar's ``percent_visible`` is now ``show_percentage``.
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
- MainLoop's ``NOTIFICATION_`` constants were duplicated to ``Node`` which means
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

Updating shaders
^^^^^^^^^^^^^^^^

There have been some changes to shaders that aren't covered by the upgrade tool.

The ``.shader`` file extension is no longer supported, which means you must
rename ``.shader`` files to ``.gdshader`` and update references accordingly in
scene/resource files using an external text editor.

Some notable renames you will need to perform in shaders are:

- Texture filter and repeat modes are now set on individual uniforms, rather
  than the texture files themselves.
- ``hint_albedo`` is now ``source_color``.
- ``hint_color`` is now ``source_color``.
- :ref:`Built in matrix variables were renamed. <doc_spatial_shader>`
- Particles shaders no longer use the ``vertex()`` processor function. Instead
  they use ``start()`` and ``process()``.

See :ref:`doc_shading_language` for more information.

Updating scripts to take backwards-incompatible changes into account
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Some changes performed between Godot 3.x and 4 are not renames, but they still
break backwards compatibility due to different default behavior.

The most notable examples of this are:

- Lifecycle functions such as ``_ready()`` and ``_process()`` no longer
  implicitly call parent classes' functions that have the same name. Instead,
  you must use ``super()`` at the top of a lifecycle function in the child class
  so that the parent class function is called first.
- Both :ref:`class_String` and :ref:`class_StringName` are now exposed to
  GDScript. This allows for greater optimization, as StringName is specifically
  designed to be used for "constant" strings that are created once and reused
  many times. These types are not strictly equivalent to each other, which means
  ``is_same("example", &"example")`` returns ``false``. Although in most cases
  they are interchangeable (``"example" == &"example"`` returns ``true``),
  sometimes you may have to replace ``"example"`` with ``&"example"``.
- :ref:`GDScript setter and getter syntax <doc_gdscript_basics_setters_getters>`
  was changed, but it's only partially converted by the conversion tool. In most
  cases, manual changes are required to make setters and getters working again.
- :ref:`GDScript signal connection syntax <doc_gdscript_signals>` was changed.
  The conversion tool will use the string-based syntax which is still present in
  Godot 4, but it's recommended to switch to the :ref:`class_Signal`-based syntax
  described on the linked page. This way, strings are no longer involved,
  which avoids issues with signal name errors that can only be discovered at run-time.
- Built-in scripts that are :ref:`tool scripts <doc_running_code_in_the_editor>`
  do not get the ``tool`` keyword converted to the ``@tool`` annotation.
- The Tween node was removed in favor of Tweeners, which are also available in
  Godot 3.5 and later. See the
  `original pull request <https://github.com/godotengine/godot/pull/41794>`__
  for details.
- ``randomize()`` is now automatically called on project load, so deterministic
  randomness with the global RandomNumberGenerate instance requires manually
  setting a seed in a script's ``_ready()`` function.
- ``call_group()``, ``set_group()`` and ``notify_group()`` are now immediate by
  default. If calling an expensive function, this may result in stuttering when
  used on a group containing a large number of nodes. To use deferred calls like
  before, replace ``call_group(...)`` with
  ``call_group_flags(SceneTree.GROUP_CALL_DEFERRED, ...)`` (and do the same with
  ``set_group()`` and ``notify_group()`` respectively).
- Instead of ``rotation_degrees``, the ``rotation`` property is exposed to the
  editor, which is automatically displayed as degrees in the Inspector
  dock. This may break animations, as the conversion is not handled automatically by the
  conversion tool.
- :ref:`class_AABB`'s ``has_no_surface()`` was inverted and renamed to ``has_surface()``.
- :ref:`class_AABB` and :ref:`class_Rect2`'s ``has_no_area()`` was inverted and
  renamed to ``has_area()``.
- :ref:`class_AnimatedTexture`'s ``fps`` property was replaced by ``speed_scale``,
  which works the same as AnimationPlayer's ``playback_speed`` property.
- :ref:`class_AnimatedSprite2D` and :ref:`class_AnimatedSprite3D` now allow
  negative ``speed_scale`` values. This may break animations if you relied on
  ``speed_scale`` being internally clamped to ``0.0``.
- :ref:`class_AnimatedSprite2D` and :ref:`class_AnimatedSprite3D`'s ``playing``
  property was removed. Use ``play()``/``stop()`` method instead OR configure
  ``autoplay`` animation via the SpriteFrames bottom panel (but not both at once).
- :ref:`class_Array`'s ``slice()`` second parameter (``end``) is now *exclusive*,
  instead of being inclusive. For example, this means that
  ``[1, 2, 3].slice(0, 1)`` now returns ``[1]`` instead of ``[1, 2]``.
- :ref:`class_BaseButton`'s signals are now ``button_up`` and ``button_down``.
  The ``pressed`` property is now ``button_pressed``.
- :ref:`class_Camera2D`'s ``rotating`` property was replaced by
  ``ignore_rotation``, which has inverted behavior.
- Camera2D's ``zoom`` property was inverted: higher values are now more zoomed
  in, instead of less.
- :ref:`class_Node`'s ``remove_and_skip()`` method was removed.
  If you need to reimplement it in a script, you can use the
  `old C++ implementation <https://github.com/godotengine/godot/blob/7936b3cc4c657e4b273b376068f095e1e0e4d82a/scene/main/node.cpp#L1910-L1945>`__
  as a reference.
- ``OS.get_system_time_secs()`` should be converted to
  ``Time.get_time_dict_from_system()["second"]``.
- :ref:`class_ResourceSaver`'s ``save()`` method now has its arguments swapped around
  (``resource: Resource, path: String``). This also applies to
  :ref:`class_ResourceFormatSaver`'s ``_save()`` method.
- A :ref:`class_StreamPeerTCP` must have ``poll()`` called on it to update its
  state, instead of relying on ``get_status()`` automatically polling:
  `GH-59582 <https://github.com/godotengine/godot/pull/59582>`__
- :ref:`class_String`'s ``right()`` method `has changed behavior <https://github.com/godotengine/godot/pull/36180>`__:
  it now returns a number of characters from the right of the string, rather than
  the right side of the string from a given position. If you need the old behavior,
  you can use ``substr()`` instead.
- ``is_connected_to_host()`` was removed from StreamPeerTCP and PacketPeerUDP as
  per `GH-59582 <https://github.com/godotengine/godot/pull/59582>`__.
  ``get_status()`` can be used in StreamPeerTCP instead.
  ``is_socket_connected()`` can be used in :ref:`class_PacketPeerUDP` instead.
- In ``_get_property_list()``, the ``or_lesser`` property hint string is now ``or_less``.
- In ``_get_property_list()``, the ``noslider`` property hint string is now ``no_slider``.
- VisualShaderNodeVec4Parameter now takes a :ref:`class_Vector4` as parameter
  instead of a :ref:`class_Quaternion`.

**Removed or replaced nodes/resources**

This lists all nodes that were replaced by another node requiring different
configuration. The setup must be done from scratch again, as the project
converter doesn't support updating existing setups:

+---------------------+-----------------------+----------------------------------------------------------------------------+
| Removed node        | Closest approximation | Comment                                                                    |
+=====================+=======================+============================================================================+
| AnimationTreePlayer | AnimationTree         | AnimationTreePlayer was deprecated since Godot 3.1.                        |
+---------------------+-----------------------+----------------------------------------------------------------------------+
| BakedLightmap       | LightmapGI            | See :ref:`doc_using_lightmap_gi`.                                          |
+---------------------+-----------------------+                                                                            |
| BakedLightmapData   | LightmapGIData        |                                                                            |
+---------------------+-----------------------+----------------------------------------------------------------------------+
| BitmapFont          | FontFile              | See :ref:`doc_gui_using_fonts`.                                            |
+---------------------+-----------------------+                                                                            |
| DynamicFont         | FontFile              |                                                                            |
+---------------------+-----------------------+                                                                            |
| DynamicFontData     | FontFile              |                                                                            |
+---------------------+-----------------------+----------------------------------------------------------------------------+
| Navigation2D        | Node2D                | Replaced by :ref:`other 2D Navigation nodes <doc_navigation_overview_2d>`. |
+---------------------+-----------------------+----------------------------------------------------------------------------+
| Navigation3D        | Node3D                | Replaced by :ref:`other 3D Navigation nodes <doc_navigation_overview_3d>`. |
+---------------------+-----------------------+----------------------------------------------------------------------------+
| OpenSimplexNoise    | FastNoiseLite         | Has different parameters and more noise types such as cellular. No         |
|                     |                       | support for 4D noise as it's absent from the FastNoiseLite library.        |
+---------------------+-----------------------+----------------------------------------------------------------------------+
| ToolButton          | Button                | ToolButton was Button with the **Flat** property enabled by default.       |
+---------------------+-----------------------+----------------------------------------------------------------------------+
| YSort               | Node2D or Control     | CanvasItem has a new **Y Sort Enabled** property in 4.0.                   |
+---------------------+-----------------------+----------------------------------------------------------------------------+
| ProximityGroup      | Node3D                | :ref:`class_VisibleOnScreenNotifier3D` can act as a replacement.           |
+---------------------+-----------------------+----------------------------------------------------------------------------+
| Portal              | Node3D                | Portal and room occlusion culling was replaced by raster                   |
|                     |                       | :ref:`occlusion culling <doc_occlusion_culling>`                           |
|                     |                       | (OccluderInstance3D node), which requires a different setup process.       |
+---------------------+-----------------------+                                                                            |
| Room                | Node3D                |                                                                            |
+---------------------+-----------------------+                                                                            |
| RoomManager         | Node3D                |                                                                            |
+---------------------+-----------------------+                                                                            |
| RoomGroup           | Node3D                |                                                                            |
+---------------------+-----------------------+----------------------------------------------------------------------------+
| Occluder            | Node3D                | Geometry occlusion culling was replaced by raster                          |
|                     |                       | :ref:`occlusion culling <doc_occlusion_culling>`                           |
|                     |                       | (OccluderInstance3D node), which requires a different setup process.       |
+---------------------+-----------------------+                                                                            |
| OccluderShapeSphere | Resource              |                                                                            |
+---------------------+-----------------------+----------------------------------------------------------------------------+

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

ArrayMesh resource compatibility breakage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you've saved an ArrayMesh resource to a ``.res`` or ``.tres`` file, the
format used in 4.0 is not compatible with the one used in 3.x. You will need to
go through the process of importing the source mesh file and saving it as an
ArrayMesh resource again.

List of automatically renamed methods, properties, signals and constants
------------------------------------------------------------------------

The `editor/renames_map_3_to_4.cpp <https://github.com/godotengine/godot/blob/master/editor/renames_map_3_to_4.cpp>`__
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
