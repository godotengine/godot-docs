.. _doc_using_voxel_gi:

Using Voxel global illumination
===============================

VoxelGI is a form of fully real-time global illumination, intended to be used
for small/medium-scale 3D scenes. VoxelGI is fairly demanding on the GPU, so
it's best used when targeting dedicated graphics cards.

.. important::

    VoxelGI is only supported when using the Forward Plus rendering backend,
    not the Forward Mobile or Compatibility backends.

.. seealso::

    Not sure if VoxelGI is suited to your needs?
    See :ref:`doc_introduction_to_global_illumination_comparison`
    for a comparison of GI techniques available in Godot 4.

Visual comparison
-----------------

.. figure:: img/gi_none.webp
   :alt: VoxelGI disabled.

   VoxelGI disabled.

.. figure:: img/gi_voxel_gi.webp
   :alt: VoxelGI enabled.

   VoxelGI enabled.

Setting up VoxelGI
------------------

1. Make sure your static level geometry is imported with the Light Baking option
   set to **Static** or **Static Lightmaps** in the Import dock.
   For manually added MeshInstance3D nodes, make sure the **Global Illumination > Mode**
   property is set to **Static** in the inspector.
2. Create a VoxelGI node in the Scene tree dock.
3. Move the VoxelGI node to the center of the area you want it to cover by
   dragging the manipulation gizmo in the 3D viewport. Then adjust the VoxelGI's
   extents by dragging the red points in the 3D viewport (or enter values in the
   inspector). Make sure the VoxelGI's extents aren't unnecessarily large, or
   quality will suffer.
4. Select the VoxelGI node and click **Bake** at the top of the 3D editor viewport.
   This will take at least a few seconds to complete (depending on the number of VoxelGI
   subdivisions and scene complexity).

If at least one mesh contained within the VoxelGI's extents has its global
illumination mode set to **Static**, you should see indirect lighting appear
within the scene.

.. note::

    To avoid bloating text-based scene files with large amounts of binary data,
    make sure the VoxelGIData resource is *always* saved to an external binary file.
    This file must be saved with a ``.res`` (binary resource) extension instead of
    ``.tres`` (text-based resource).
    Using an external binary resource for VoxelGIData will keep your text-based
    scene small while ensuring it loads and saves quickly.

VoxelGI node properties
-----------------------

The following properties can be adjusted in the VoxelGI node inspector before
baking:

- **Subdiv:** Higher values result in more precise indirect lighting, at the cost
  of lower performance, longer bake times and increased storage requirements.
- **Extents:** Represents the size of the box in which indirect lighting should
  be baked. Extents are centered around the VoxelGI node's origin.

The following properties can be adjusted in the VoxelGIData *resource* that is
contained within a VoxelGI node after it has been baked:

- **Dynamic Range:** The maximum brightness that can be represented in indirect lighting.
  Higher values make it possible to represent brighter indirect light,
  at the cost of lower precision (which can result in visible banding).
  If in doubt, leave this unchanged.
- **Energy:** The indirect lighting's overall energy. This also effects the energy
  of direct lighting emitted by meshes with emissive materials.
- **Bias:** Optional bias added to lookups into the voxel buffer at run time.
  This helps avoid self-occlusion artifacts.
- **Normal Bias:** Similar to **Bias**, but offsets the lookup into the voxel buffer
  by the surface normal. This also helps avoid self-occlusion artifacts. Higher
  values reduce self-reflections visible in non-rough materials, at the cost of
  more visible light leaking and flatter-looking indirect lighting. To
  prioritize hiding self-reflections over lighting quality, set **Bias** to
  ``0.0`` and **Normal Bias** to a value between ``1.0`` and ``2.0``.
- **Propagation:** The energy factor to use for bounced indirect lighting.
  Higher values will result in brighter, more diffuse lighting
  (which may end up looking too flat). When **Use Two Bounces** is enabled,
  you may want to decrease **Propagation** to compensate for the overall brighter
  indirect lighting.
- **Use Two Bounces:** If enabled, lighting will bounce twice instead of just once.
  This results in more realistic-looking indirect lighting, and makes indirect lighting
  visible in reflections as well. Enabling this generally has no noticeable performance cost.
- **Interior:** If enabled, environment sky lighting will not be taken into account by VoxelGI.
  This should be enabled in indoor scenes to avoid light leaking from the environment.

VoxelGI interaction with lights and objects
-------------------------------------------

To ensure correct visuals when using VoxelGI, you must configure your meshes
and lights' global illumination properties according to their *purpose* in the
scene (static or dynamic).

There are 3 global illumination modes available for meshes:

- **Disabled:** The mesh won't be taken into account for VoxelGI baking.
  The mesh will *receive* indirect lighting from the scene, but it will not
  *contribute* indirect lighting to the scene.
- **Static (default):** The mesh will be taken into account for VoxelGI baking. The mesh will
  both receive *and* contribute indirect lighting to the scene. If the mesh
  is changed in any way after baking, the VoxelGI node must be baked again.
  Otherwise, indirect lighting will look incorrect.
- **Dynamic:** The mesh won't be taken into account for VoxelGI baking, but it will
  still receive *and* contribute indirect lighting to the scene in real-time.
  This option is much slower compared to **Static**. Only use the **Dynamic**
  global illumination mode on large meshes that will change significantly during gameplay.

Additionally, there are 3 bake modes available for lights
(DirectionalLight3D, OmniLight3D and SpotLight3D):

- **Disabled:** The light won't be taken into account for VoxelGI baking.
  The light won't contribute indirect lighting to the scene.
- **Static:** The light will be taken into account for VoxelGI baking.
  The light will contribute indirect lighting to the scene. If the light
  is changed in any way after baking, the VoxelGI node must be baked again or
  indirect lighting will look incorrect. If in doubt, use this mode for level lighting.
- **Dynamic (default):** The light won't be taken into account for VoxelGI baking,
  but it will still contribute indirect lighting to the scene in real-time.
  This option is slower compared to **Static**. Only use the **Dynamic** global
  illumination mode on lights that will change significantly during gameplay.

.. note::

    The amount of indirect energy emitted by a light depends on its color,
    energy *and* indirect energy properties. To make a specific light emit more
    or less indirect energy without affecting the amount of direct light emitted
    by the light, adjust the **Indirect Energy** property in the Light3D inspector.

.. seealso::

    See :ref:`doc_introduction_to_global_illumination_gi_mode_recommendations`
    for general usage recommendations.

Adjusting VoxelGI performance and quality
-----------------------------------------

Since VoxelGI is relatively demanding, it will perform best on systems with recent
dedicated GPUs. On older dedicated GPUs and integrated graphics,
tweaking the settings is necessary to achieve reasonable performance.

In the Project Settings' **Rendering > Global Illumination** section,
VoxelGI quality can also be adjusted in two ways:

- **Voxel Gi > Quality:** If set to **Low**
  instead of **High**, voxel cone tracing will only use 4 taps instead of 6.
  This speeds up rendering at the cost of less pronounced ambient occlusion.
- **Gi > Use Half Resolution:** If enabled, both VoxelGI and SDFGI will have
  their GI buffer rendering at halved resolution. For instance, when rendering
  in 3840×2160, the GI buffer will be computed at a 1920×1080 resolution.
  Enabling this option saves a lot of GPU time, but it can introduce visible
  aliasing around thin details.

Note that the **Advanced** toggle must be enabled in the project settings dialog
for the above settings to be visible.

Additionally, VoxelGI can be disabled entirely by hiding the VoxelGI node.
This can be used for comparison purposes or to improve performance on low-end systems.

Reducing VoxelGI light leaks and artifacts
------------------------------------------

After baking VoxelGI, you may notice indirect light is leaking at some spots
in your level geometry. This can be remedied in several ways:

- For both light leaking and artifacts, try moving or rotating the VoxelGI node
  then bake it again.
- To combat light leaking in general, ensure your level geometry is fully sealed.
  This is best done in the 3D modeling software used to design the level,
  but primitive MeshInstance3D nodes with their global illumination mode set to
  **Static** can also be used.
- To combat light leaking with thin geometry, it's recommended to make the geometry
  in question thicker. If this is not possible, then add a primitive MeshInstance3D
  node with its global illumination mode set to **Static**. Bake VoxelGI again,
  then hide the primitive MeshInstance3D node (it will still be taken into account by VoxelGI).
  For optimal results, the MeshInstance3D should have a material whose color
  matches the original thin geometry.
- To combat artifacts that can appear on reflective surfaces, try increasing
  **Bias** and/or **Normal Bias** in the VoxelGIData resource as described above.
  Do not increase these values too high, or light leaking will become more pronounced.

If you notice VoxelGI nodes popping in and out of existence as the camera moves,
this is most likely because the engine is rendering too many VoxelGI instances
at once. Godot is limited to rendering 8 VoxelGI nodes at once, which means up
to 8 instances can be in the camera view before some of them will start
flickering.

Additionally, for performance reasons, Godot can only blend between 2 VoxelGI
nodes at a given pixel on the screen. If you have more than 2 VoxelGI nodes
overlapping, global illumination may appear to flicker as the camera moves or
rotates.
