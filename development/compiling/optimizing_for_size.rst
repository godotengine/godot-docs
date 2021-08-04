.. _doc_optimizing_for_size:

Optimizing a build for size
===========================

.. highlight:: none

Rationale
---------

Sometimes, it is desired to optimize a build for size rather than speed.
This means not compiling unused functions from the engine, as well as using
specific compiler flags to aid on decreasing build size.
Common situations include creating builds for mobile and web platforms.

This tutorial aims to give an overview on different methods to create
a smaller binary. Before continuing, it is recommended to read the previous tutorials
on compiling Godot for each platform.

Disabling 3D
------------

For 2D games, having the whole 3D engine available usually makes no sense. Because of this,
there is a build flag to disable most of it. Without the 3D parts, the binary size can be
reduced by about 15%:

::

    scons p=<platform> target=release tools=no disable_3d=yes

The following classes are not available when building with ``disable_3d=yes``:

- :ref:`class_ARVRAnchor`
- :ref:`class_ARVRCamera`
- :ref:`class_ARVRController`
- :ref:`class_ARVROrigin`
- :ref:`class_AnimatedSprite3D`
- :ref:`class_Area`
- :ref:`class_AudioStreamPlayer3D`
- :ref:`class_BakedLightmap`
- :ref:`class_BakedLightmapData`
- :ref:`class_BoneAttachment`
- :ref:`class_BoxShape`
- :ref:`class_CPUParticles`
- :ref:`class_CSGBox`
- :ref:`class_CSGCombiner`
- :ref:`class_CSGCylinder`
- :ref:`class_CSGMesh`
- :ref:`class_CSGPolygon`
- :ref:`class_CSGPrimitive`
- :ref:`class_CSGShape`
- :ref:`class_CSGSphere`
- :ref:`class_CSGTorus`
- :ref:`class_Camera`
- :ref:`class_CapsuleMesh`
- :ref:`class_CapsuleShape`
- :ref:`class_ClippedCamera`
- :ref:`class_CollisionObject`
- :ref:`class_CollisionPolygon`
- :ref:`class_CollisionShape`
- :ref:`class_ConcavePolygonShape`
- :ref:`class_ConeTwistJoint`
- :ref:`class_ConvexPolygonShape`
- :ref:`class_CubeMesh`
- :ref:`class_CullInstance`
- :ref:`class_Curve3D`
- :ref:`class_CylinderMesh`
- :ref:`class_CylinderShape`
- :ref:`class_DirectionalLight`
- :ref:`class_EditorSceneImporterGLTF`
- :ref:`class_GIProbe`
- :ref:`class_GIProbeData`
- :ref:`class_GLTFAccessor`
- :ref:`class_GLTFAnimation`
- :ref:`class_GLTFBufferView`
- :ref:`class_GLTFCamera`
- :ref:`class_GLTFDocument`
- :ref:`class_GLTFLight`
- :ref:`class_GLTFMesh`
- :ref:`class_GLTFNode`
- :ref:`class_GLTFSkeleton`
- :ref:`class_GLTFSkin`
- :ref:`class_GLTFSpecGloss`
- :ref:`class_GLTFState`
- :ref:`class_GLTFTexture`
- :ref:`class_Generic6DOFJoint`
- :ref:`class_GeometryInstance`
- :ref:`class_GridMap`
- :ref:`class_HeightMapShape`
- :ref:`class_HingeJoint`
- :ref:`class_ImmediateGeometry`
- :ref:`class_InterpolatedCamera`
- :ref:`class_Joint`
- :ref:`class_KinematicBody`
- :ref:`class_KinematicCollision`
- :ref:`class_Light`
- :ref:`class_Listener`
- :ref:`class_Material`
- :ref:`class_MeshInstance`
- :ref:`class_MeshLibrary`
- :ref:`class_MultiMeshInstance`
- :ref:`class_Navigation`
- :ref:`class_NavigationMesh`
- :ref:`class_NavigationMeshInstance`
- :ref:`class_OmniLight`
- :ref:`class_PackedSceneGLTF`
- :ref:`class_Particles`
- :ref:`class_Path`
- :ref:`class_PathFollow`
- :ref:`class_PhysicalBone`
- :ref:`class_PhysicsBody`
- :ref:`class_PinJoint`
- :ref:`class_PlaneMesh`
- :ref:`class_PlaneShape`
- :ref:`class_PointMesh`
- :ref:`class_Portal`
- :ref:`class_Position3D`
- :ref:`class_PrimitiveMesh`
- :ref:`class_PrismMesh`
- :ref:`class_ProximityGroup`
- :ref:`class_QuadMesh`
- :ref:`class_RayCast`
- :ref:`class_RayShape`
- :ref:`class_ReflectionProbe`
- :ref:`class_RemoteTransform`
- :ref:`class_RigidBody`
- :ref:`class_Room`
- :ref:`class_RoomGroup`
- :ref:`class_RoomManager`
- :ref:`class_RootMotionView`
- :ref:`class_Shape`
- :ref:`class_SkeletonIK`
- :ref:`class_SliderJoint`
- :ref:`class_SoftBody`
- :ref:`class_SpatialMaterial`
- :ref:`class_SpatialVelocityTracker`
- :ref:`class_SphereMesh`
- :ref:`class_SphereShape`
- :ref:`class_SpotLight`
- :ref:`class_SpringArm`
- :ref:`class_Sprite3D`
- :ref:`class_SpriteBase3D`
- :ref:`class_StaticBody`
- :ref:`class_VehicleBody`
- :ref:`class_VehicleWheel`
- :ref:`class_VisibilityEnabler`
- :ref:`class_VisibilityNotifier`
- :ref:`class_VisualInstance`
- :ref:`class_WorldEnvironment`

.. note::

    The editor is not designed to operate without 3D support, so this flag only works
    in combination with ``tools=no``.

Disabling advanced GUI nodes
----------------------------

If your game doesn't require complex GUI controls, they can be disabled using a build flag:

::

    scons p=<platform> target=release tools=no disable_advanced_gui=yes

The following classes are not available when building with ``disable_advanced_gui=yes``:

- :ref:`class_AcceptDialog`
- :ref:`class_CharFXTransform`
- :ref:`class_ColorPicker`
- :ref:`class_ColorPickerButton`
- :ref:`class_ConfirmationDialog`
- :ref:`class_FileDialog`
- :ref:`class_GraphEdit`
- :ref:`class_GraphNode`
- :ref:`class_HSplitContainer`
- :ref:`class_MarginContainer`
- :ref:`class_OptionButton`
- :ref:`class_PopupDialog`
- :ref:`class_PopupMenu`
- :ref:`class_RichTextEffect`
- :ref:`class_RichTextLabel`
- :ref:`class_SpinBox`
- :ref:`class_SplitContainer`
- :ref:`class_TextEdit`
- :ref:`class_Tree`
- :ref:`class_TreeItem`
- :ref:`class_VSplitContainer`
- :ref:`class_ViewportContainer`
- :ref:`class_WindowDialog`

.. note::

    The editor uses many of these GUI controls, so this flag only works
    in combination with ``tools=no``.

Disabling unwanted modules
--------------------------

A lot of Godot's functions are offered as modules.
You can see a list of modules with the following command:

::

    scons --help

The list of modules that can be disabled will appear, together with all
build options. If you are working on a simple 2D game, you could disable
a lot of them:

::

    scons p=<platform> target=release tools=no \
    module_bmp_enabled=no module_bullet_enabled=no module_camera_enabled=no module_csg_enabled=no \
    module_dds_enabled=no module_enet_enabled=no module_etc_enabled=no module_gdnative_enabled=no \
    module_gridmap_enabled=no module_hdr_enabled=no module_jsonrpc_enabled=no module_mbedtls_enabled=no \
    module_mobile_vr_enabled=no module_opensimplex_enabled=no module_opus_enabled=no module_pvr_enabled=no \
    module_recast_enabled=no module_regex_enabled=no module_squish_enabled=no module_svg_enabled=no \
    module_tga_enabled=no module_theora_enabled=no module_tinyexr_enabled=no module_upnp_enabled=no \
    module_vhacd_enabled=no module_vorbis_enabled=no module_webm_enabled=no module_webrtc_enabled=no \
    module_websocket_enabled=no module_webxr_enabled=no module_xatlas_unwrap_enabled=no

If this proves not to work for your use case, you should review the list of
modules and see which ones you actually still need for your game (e.g. you
might want to keep networking-related modules, regex support, or theora/webm
to play videos).

.. important::

    While you can disable most modules, some are required for core functionally,
    especially when building with ``tools=yes``. SCons will warn you if your desired
    module configuration is impossible and abort the build process.

If you don't want to add them to the commandline every time you do a build,
you can supply a list of disabled modules by creating a ``custom.py`` file at the root
of your Godot source directory, with the contents similar to the following:

.. code-block:: python

    # custom.py

    module_arkit_enabled = "no"
    module_assimp_enabled = "no"
    module_bmp_enabled = "no"
    module_bullet_enabled = "no"
    module_camera_enabled = "no"
    module_csg_enabled = "no"
    module_dds_enabled = "no"
    module_enet_enabled = "no"
    module_etc_enabled = "no"
    module_gdnative_enabled = "no"
    module_gridmap_enabled = "no"
    module_hdr_enabled = "no"
    module_jsonrpc_enabled = "no"
    module_mbedtls_enabled = "no"
    module_mobile_vr_enabled = "no"
    module_opensimplex_enabled = "no"
    module_opus_enabled = "no"
    module_pvr_enabled = "no"
    module_recast_enabled = "no"
    module_regex_enabled = "no"
    module_squish_enabled = "no"
    module_svg_enabled = "no"
    module_tga_enabled = "no"
    module_theora_enabled = "no"
    module_tinyexr_enabled = "no"
    module_upnp_enabled = "no"
    module_vhacd_enabled = "no"
    module_vorbis_enabled = "no"
    module_webm_enabled = "no"
    module_webrtc_enabled = "no"
    module_websocket_enabled = "no"
    module_webxr_enabled = "no"
    module_xatlas_unwrap_enabled = "no"

.. seealso::

    You can use the online
    `Godot build options generator <https://godot-build-options-generator.github.io/>`__
    to generate a ``custom.py`` file containing SCons options.

.. seealso::

    :ref:`doc_overriding_build_options`.

Optimizing for size instead of speed
------------------------------------

Godot 3.1 onwards allows compiling using size optimizations (instead of speed).
To enable this, set the ``optimize`` flag to ``size``:

::

    scons p=<platform> target=release tools=no optimize=size

Some platforms such as WebAssembly already use this mode by default.

Compiling with link-time optimization
-------------------------------------

Enabling link-time optimization (LTO) produces more efficient binaries, both in
terms of performance and file size. It works by eliminating duplicate
template functions and unused code. It can currently be used with the GCC
and MSVC compilers:

::

    scons p=<platform> target=release tools=no use_lto=yes

Linking becomes much slower and more RAM is consumed with this option, so it should be used only for
release builds.

Stripping binaries
------------------

If you build from source, remember to strip debug symbols from binaries:

::

    strip godot.64
