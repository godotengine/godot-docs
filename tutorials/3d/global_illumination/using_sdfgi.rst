.. _doc_using_sdfgi:

Signed distance field global illumination (SDFGI)
=================================================

Signed distance field global illumination (SDFGI) is a novel technique available
in Godot 4.0. It provides semi-real-time global illumination that scales to any
world size and works with procedurally generated levels.

SDFGI supports dynamic lights, but *not* dynamic occluders or dynamic emissive surfaces.
Therefore, SDFGI provides better real-time ability than
:ref:`baked lightmaps <doc_using_lightmap_gi>`, but worse real-time ability than
:ref:`VoxelGI <doc_using_voxel_gi>`.

From a performance standpoint, SDFGI is one of the most demanding global illumination
techniques in Godot. Like with VoxelGI, there are still many settings available to tweak
its performance requirements at the cost of quality.

.. important::

    SDFGI is only supported when using the Forward Plus rendering backend,
    not the Forward Mobile or Compatibility backends.

.. seealso::

    Not sure if SDFGI is suited to your needs?
    See :ref:`doc_introduction_to_global_illumination_comparison`
    for a comparison of GI techniques available in Godot 4.

Visual comparison
-----------------

.. figure:: img/gi_none.webp
   :alt: SDFGI disabled.

   SDFGI disabled.

.. figure:: img/gi_sdfgi.webp
   :alt: SDFGI enabled.

   SDFGI enabled.

Setting up SDFGI
----------------

In Godot, SDFGI is the global illumination technique with the fewest required
steps to enable:

1. Make sure your MeshInstance nodes have their **Global Illumination > Mode**
   property set to **Static** in the inspector.

  - For imported 3D scenes, the bake mode can be configured in the Import dock
    after selecting the 3D scene file in the FileSystem dock.

2. Add a WorldEnvironment node and create an Environment resource for it.
3. Edit the Environment resource, scroll down to the **SDFGI** section and unfold it.
4. Enable **SDFGI > Enabled**. SDFGI will automatically follow the camera when it
   moves, so you do not need to configure extents (unlike VoxelGI).

Environment SDFGI properties
----------------------------

In the Environment resource, there are several properties available to adjust
SDFGI appearance and quality:

- **Use Occlusion:** If enabled, SDFGI will throw additional rays to find and
  reduce light leaks. This has a performance cost, so only enable this property
  if you actually need it.
- **Read Sky Light:** If enabled, the environment lighting is represented in the
  global illumination. This should be enabled in outdoor scenes and disabled in
  fully indoor scenes.
- **Bounce Feedback:** By default, indirect lighting only bounces once when
  using SDFGI. Setting this value above ``0.0`` will cause SDFGI to bounce more
  than once, which provides more realistic indirect lighting at a small
  performance cost. Sensible values are usually between ``0.3`` and ``1.0``
  depending on the scene. Note that in some scenes, values above ``0.5`` can
  cause infinite feedback loops to happen, causing the scene to become extremely
  bright in a few seconds' time.
  If your indirect lighting looks "splotchy", consider increasing this value above
  ``0.0`` to get more uniform-looking lighting. If your lighting ends up looking
  too bright as a result, decrease **Energy** to compensate.
- **Cascades:** Higher values result in more detailed GI information
  (and/or greater maximum distance), but are significantly more expensive on the
  CPU and GPU. The performance cost of having more cascades especially increases
  when the camera moves fast, so consider decreasing this to ``4`` or lower
  if your camera moves fast.
- **Min Cell Size:** The minimum SDFGI cell size to use for the nearest, most detailed
  cascade. Lower values result in more accurate indirect lighting and reflection
  at the cost of lower performance.
  Adjusting this setting also affects **Cascade 0 Distance** and **Max Distance** automatically.
- **Cascade 0 Distance:** The distance at which the nearest, most detailed
  cascade ends. Greater values make the nearest cascade transition less noticeable,
  at the cost of reducing the level of detail in the nearest cascade.
  Adjusting this setting also affects **Min Cell Size** and **Max Distance** automatically.
- **Max Distance:** Controls how far away the signed distance field will be computed
  (for the least detailed cascade). SDFGI will not have any effect past this distance.
  This value should always be set below the Camera's Far value, as there is no benefit
  in computing SDFGI past the viewing distance.
  Adjusting this setting also affects **Min Cell Size** and **Cascade 0 Distance** automatically.
- **Y Scale:** Controls how far apart SDFGI probes are spread *vertically*.
  By default, vertical spread is the same as horizontal. However, since most
  game scenes aren't highly vertical, setting the Y Scale to
  ``75%`` or even ``50%`` can provide better quality and reduce light leaks
  without impacting performance.
- **Energy:** The brightness multiplier for SDFGI's indirect lighting.
- **Normal Bias:** The normal bias to use for SDFGI's probe ray bounces.
  Unlike **Probe Bias**, this only increases the value in relation to the
  mesh's normals. This makes the bias adjustment more nuanced and avoids
  increasing the bias too much for no reason. Increase this
  value if you notice striping artifacts in indirect lighting or reflections.
- **Probe Bias:** The bias to use for SDFGI's probe ray bounces. Increase this
  value if you notice striping artifacts in indirect lighting or reflections.

SDFGI interaction with lights and objects
-----------------------------------------

The amount of indirect energy emitted by a light is governed by its color,
energy *and* indirect energy properties. To make a specific light emit more
or less indirect energy without affecting the amount of direct light emitted
by the light, adjust the **Indirect Energy** property in the Light3D inspector.

To ensure correct visuals when using SDFGI, you must configure your meshes
and lights' global illumination properties according to their *purpose* in the
scene (static or dynamic).

There are 3 global illumination modes available for meshes:

- **Disabled:** The mesh won't be taken into account in SDFGI generation.
  The mesh will receive indirect lighting from the scene, but it will not
  contribute indirect lighting to the scene.
- **Static (default):** The mesh will be taken into account in SDFGI generation.
  The mesh will both receive *and* contribute indirect lighting to the scene. If
  the mesh is changed in any way after SDFGI is generated, the camera must move
  away from the object then move back close to it for SDFGI to regenerate.
  Alternatively, SDFGI can be toggled off and back on. If neither is done,
  indirect lighting will look incorrect.
- **Dynamic (not supported with SDFGI):** The mesh won't be taken into account in SDFGI generation.
  The mesh will receive indirect lighting from the scene, but it will not
  contribute indirect lighting to the scene.
  *This acts identical to the **Disabled** bake mode when using SDFGI.*

Additionally, there are 3 bake modes available for lights
(DirectionalLight3D, OmniLight3D and SpotLight3D):

- **Disabled:** The light won't be taken into account for SDFGI baking.
  The light won't contribute indirect lighting to the scene.
- **Static:** The light will be taken into account for SDFGI baking. The light
  will contribute indirect lighting to the scene. If the light is changed in any
  way after baking, indirect lighting will look incorrect until the camera moves
  away from the light and back (which causes SDFGI to be baked again). will look
  incorrect. If in doubt, use this mode for level lighting.
- **Dynamic (default):** The light won't be taken into account for SDFGI baking,
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

Adjusting SDFGI performance and quality
---------------------------------------

Since SDFGI is relatively demanding, it will perform best on systems with recent
dedicated GPUs. On older dedicated GPUs and integrated graphics,
tweaking the settings is necessary to achieve reasonable performance.

In the Project Settings' **Rendering > Global Illumination** section,
SDFGI quality can also be adjusted in several ways:

- **Sdfgi > Probe Ray Count:** Higher values result in better quality,
  at the cost of higher GPU usage. If this value is set too low,
  this can cause surfaces to have visible "splotches" of indirect lighting on
  them due to the number of rays thrown being very low.
- **Sdfgi > Frames To Converge:** Higher values result in better quality, but GI will take
  more time to fully converge. The effect of this setting is especially noticeable when first
  loading a scene, or when lights with a bake mode other than **Disabled** are moving fast.
  If this value is set too low, this can cause surfaces to have visible "splotches"
  of indirect lighting on them due to the number of rays thrown being very low.
  If your scene's lighting doesn't have fast-moving lights that contribute to GI,
  consider setting this to ``30`` to improve quality without impacting performance.
- **Sdfgi > Frames To Update Light:** Lower values result in moving lights being
  reflected faster, at the cost of higher GPU usage. If your scene's lighting
  doesn't have fast-moving lights that contribute to GI, consider setting this
  to ``16`` to improve performance.
- **Gi > Use Half Resolution:** If enabled, both SDFGI and VoxelGI will have
  their GI buffer rendering at halved resolution. For instance, when rendering
  in 3840×2160, the GI buffer will be computed at a 1920×1080 resolution.
  Enabling this option saves a lot of GPU time, but it can introduce visible
  aliasing around thin details.

SDFGI rendering performance also depends on the number of cascades and
the cell size chosen in the Environment resource (see above).

SDFGI caveats
-------------

SDFGI has some downsides due to its cascaded nature. When the camera moves,
cascade shifts may be visible in indirect lighting. This can be alleviated
by adjusting the cascade size, but also by adding fog (which will make distant
cascade shifts less noticeable).

Additionally, performance will suffer if the camera moves too fast.
This can be fixed in two ways:

- Ensuring the camera doesn't move too fast in any given situation.
- Temporarily disabling SDFGI in the Environment resource if the camera needs
  to be moved at a high speed, then enabling SDFGI once the camera speed slows down.

When SDFGI is enabled, it will also take some time for global illumination
to be fully converged (25 frames by default). This can create a noticeable transition
effect while GI is still converging. To hide this, you can use a ColorRect node
that spans the whole viewport and fade it out when switching scenes using an
AnimationPlayer node.

The signed distance field is only updated when the camera moves in and out of a
cascade. This means that if geometry is modified in the distance, the global
illumination appearance will be correct once the camera gets closer. However, if
a nearby object with a bake mode set to **Static** or **Dynamic** is moved (such
as a door), the global illumination will appear incorrect until the camera moves
away from the object.

SDFGI's sharp reflections are only visible on opaque materials. Transparent
materials will only use rough reflections, even if the material's roughness is
lower than 0.2.
