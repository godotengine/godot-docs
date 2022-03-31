.. _doc_mobile_rendering_limitations:

Mobile rendering limitations
============================

.. seealso::

    The general :ref:`doc_3d_rendering_limitations` also apply to mobile platforms.

To improve out-of-the-box performance on mobile devices, Godot automatically uses
low-end-friendly settings by default on both Android and iOS. These are configured
by project settings with a ``.mobile`` :ref:`feature tag <doc_feature_tags>` suffix.

One of the most notable changes on mobile that will affect 3D projects is that
lighting is done per-vertex instead of per-pixel. This improves performance a
lot, but can break rendering in some scenes, especially if your meshes aren't
sufficiently subdivided for per-vertex lighting to look good. This can be
disabled in the Project Settings at a performance cost (see below).

When using GLES2, some custom shaders may break when exporting to Android. This
is caused by a lower shader precision being used by default to improve
performance. You can force high precision on all shader computations by enabling
``rendering/gles2/compatibility/enable_high_float.Android`` project setting, but
this has a significant performance cost and won't work on all devices.

The following project settings have mobile-specific overrides:

+---------------------------------------------------------------------------+-----------------+--------------------+
| Setting                                                                   | Desktop default | Mobile default     |
+---------------------------------------------------------------------------+-----------------+--------------------+
| ``rendering/quality/directional_shadow/size``                             | 4096            | 2048               |
+---------------------------------------------------------------------------+-----------------+--------------------+
| ``rendering/quality/intended_usage/framebuffer_allocation``               | 3D              | 3D Without Effects |
+---------------------------------------------------------------------------+-----------------+--------------------+
| ``rendering/quality/lightmapping/use_bicubic_sampling``                   | ``true``        | ``false``          |
+---------------------------------------------------------------------------+-----------------+--------------------+
| ``rendering/quality/reflections/high_quality_ggx``                        | ``true``        | ``false``          |
+---------------------------------------------------------------------------+-----------------+--------------------+
| ``rendering/quality/shading/force_blinn_over_ggx``                        | ``false``       | ``true``           |
+---------------------------------------------------------------------------+-----------------+--------------------+
| ``rendering/quality/shading/force_lambert_over_burley``                   | ``false``       | ``true``           |
+---------------------------------------------------------------------------+-----------------+--------------------+
| ``rendering/quality/shading/force_vertex_shading``                        | ``false``       | ``true``           |
+---------------------------------------------------------------------------+-----------------+--------------------+
| ``rendering/quality/shadow_atlas/size``                                   | 4096            | 2048               |
+---------------------------------------------------------------------------+-----------------+--------------------+
| ``rendering/quality/shadows/filter_mode``                                 | PCF5            | Disabled           |
+---------------------------------------------------------------------------+-----------------+--------------------+
| *GLES3 only:* ``rendering/gles3/shaders/max_simultaneous_compiles``       | 2               | 1                  |
+---------------------------------------------------------------------------+-----------------+--------------------+
| *GLES3 only:* ``rendering/gles3/shaders/shader_cache_size_mb``            | 512             | 128                |
+---------------------------------------------------------------------------+-----------------+--------------------+
| *GLES3 only:* ``rendering/quality/depth/hdr``                             | ``true``        | ``false``          |
+---------------------------------------------------------------------------+-----------------+--------------------+
| *GLES3 only:* ``rendering/quality/reflections/texture_array_reflections`` | ``true``        | ``false``          |
+---------------------------------------------------------------------------+-----------------+--------------------+

See the :ref:`ProjectSettings class documentation <class_ProjectSettings>`
for more information on those setting overrides.

If you're only targeting mobile platforms in your project, consider changing the
project settings' values to match the mobile overrides. This way, you'll get a
preview that is closer to the mobile appearance when running the project on a
desktop platform (as well as within the editor).

.. warning::

    Due to driver bugs, GLES3 support on Android and iOS can be poor, especially
    on old or low-end devices. Therefore, it is recommended to use the GLES2
    renderer when targeting mobile platforms (especially Android).

    You can change the rendering backend in the Project Settings
    (**Rendering > Quality > Driver > Driver Name**).
