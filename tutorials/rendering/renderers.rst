.. _doc_renderers:

Renderers
=========

.. seealso::

    This page gives an overview of Godot's renderers, focusing on the differences
    between their rendering features. For more technical details on the renderers,
    see :ref:`doc_internal_rendering_architecture`.

Introduction
------------

Godot 4 includes three renderers, or *rendering methods*, which use different
*rendering drivers*:

- **Forward+**, sometimes called **Clustered Forward**. This renderer uses
  **Vulkan**, **Direct3D 12**, or **Metal** as the rendering driver. The most advanced
  graphics backend, suited for desktop platforms only. Used by default on 
  desktop platforms.
- **Forward Mobile**, sometimes called **Mobile**. This renderer uses
  **Vulkan**, **Direct3D 12**, or **Metal** as the rendering driver. Less features, 
  but renders simple scenes faster. Suited for mobile and desktop platforms.
  Used by default on mobile platforms.
- **Compatibility**, sometimes called **GL Compatibility**.  This renderer uses
  **OpenGL 3.3**, **OpenGL ES 3.0**, or **WebGL 2.0** as the rendering driver. The least
  advanced graphics backend, suited for low-end desktop and mobile platforms.
  Used by default on the web platform.

Choosing a renderer
-------------------

Choosing a renderer is a complex question, and depends on your hardware and the
which platforms you are developing for. As a starting point:

Choose **Forward+** if:

    - You are developing for desktop.
    - You have relatively new hardware which supports Vulkan.
    - You are developing a 3D game.
    - You want to use the most advanced rendering features.

Choose **Mobile** if:

    - You are developing for newer mobile devices, XR, or desktop.
    - You have relatively new hardware which supports Vulkan.
    - You are developing a 3D game.
    - You want to use advanced rendering features, subject to the limitations
      of mobile hardware.

Choose **Compatibility** if:

    - You are developing for older mobile devices, or older desktop devices. The
      Compatibility renderer supports the widest range of hardware.
    - You have older hardware which does not support Vulkan. In this case,
      Compatibility is the only choice.
    - You are developing a 2D game, or a 3D game which does not need advanced
      rendering features.

Keep in mind every game is unique, and this is only a starting point. For example,
you might choose to use the Compatibility renderer even though you have the latest
GPU, so you can support the widest range of hardware. Or you might want to use the
Forward+ renderer for a 2D game, so you can advanced features like compute shaders.

Switching between renderers
~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the editor, you can always switch between renderers by clicking on the renderer
name in the upper-right corner of the editor.

Switching between renderers may require some manual tweaks to your scene, lighting,
and environment, since each renderer is different. In general, switching between
the Forward+ or Mobile renderers and the Compatibility renderer will require more
adjustments than switching between the Mobile and Forward+ renderers.

Switching between different renderers at runtime is not yet supported.

Feature comparison
------------------

This is not a complete list of the features of each renderer. If a feature is
not listed here, it is available in all renderers, though it may be much faster
on some renderers. For a list of *all* features in Godot, see :ref:`doc_list_of_features`. 

Overall comparison
~~~~~~~~~~~~~~~~~~

+---------------------+--------------------------+--------------------------+--------------------------+
| Feature             | Compatibility            | Mobile                   | Forward+                 |
+=====================+==========================+==========================+==========================+
| **Required**        | Older or low-end.        | Newer or high-end.       | Newer or high-end.       |
| **hardware**        |                          | Requires Vulkan support. | Requires Vulkan support. |
+---------------------+--------------------------+--------------------------+--------------------------+
| Runs on new hardware| ✔️ Yes.                  | ✔️ Yes.                  | ✔️ Yes.                  |
+---------------------+--------------------------+--------------------------+--------------------------+
| Runs on old and     | ✔️ Yes.                  | ❌ No.                   | ❌ No.                   |
| low-end hardware    |                          |                          |                          |
+---------------------+--------------------------+--------------------------+--------------------------+
| **Target platforms**| Mobile, low-end desktop, | Mobile, desktop.         | Desktop.                 |
|                     | web.                     |                          |                          |
|                     |                          |                          |                          |
+---------------------+--------------------------+--------------------------+--------------------------+
| Desktop             | ✔️ Yes.                  | ✔️ Yes.                  | ✔️ Yes.                  |
+---------------------+--------------------------+--------------------------+--------------------------+
| Mobile              | ✔️ Yes (low-end).        | ✔️ Yes (high-end).       | ❌ Supported, but poorly |
|                     |                          |                          | optimized. Use Mobile or |
|                     |                          |                          | Compatibility instead.   |
+---------------------+--------------------------+--------------------------+--------------------------+
| XR                  | ✔️ Yes.                  | ✔️ Yes.                  | ✔️ Yes.                  |
|                     |                          |                          |                          |
+---------------------+--------------------------+--------------------------+--------------------------+
| Web                 | ✔️ Yes.                  | ❌ No.                   | ❌ No.                   |
+---------------------+--------------------------+--------------------------+--------------------------+
| 2D Games            | ✔️ Yes.                  | ✔️ Yes, but              | ✔️ Yes, but              |
|                     |                          | Compatibility is usually | Compatibility is usually |
|                     |                          | good enough for 2D.      | good enough for 2D.      |
+---------------------+--------------------------+--------------------------+--------------------------+
| 3D Games            | ✔️ Yes.                  | ✔️ Yes.                  | ✔️ Yes.                  |
+---------------------+--------------------------+--------------------------+--------------------------+
| **Feature set**     | 2D and core 3D features. | Most rendering features. | All rendering features.  |
+---------------------+--------------------------+--------------------------+--------------------------+
| 2D rendering        | ✔️ Yes.                  | ✔️ Yes.                  | ✔️ Yes.                  |
| features            |                          |                          |                          |
+---------------------+--------------------------+--------------------------+--------------------------+
| Core 3D rendering   | ✔️ Yes.                  | ✔️ Yes.                  | ✔️ Yes.                  |
| features            |                          |                          |                          |
+---------------------+--------------------------+--------------------------+--------------------------+
| Advanced            | ❌ No.                   | ✔️ Yes, limited by       | ✔️ Yes. All rendering    |
| rendering features  |                          | mobile hardware.         | features are supported.  |
+---------------------+--------------------------+--------------------------+--------------------------+
| New features        | ⚠️ Some new rendering    | ✔️ Most new rendering    | ✔️ All new features are  |
|                     | features are added to    | features are added to    | added to Forward+. As the|
|                     | Compatibility. Features  | Mobile. Mobile usually   | focus of new development,|
|                     | are added after Mobile   | gets new features as     | Forward+ gets features   |
|                     | and Forward+.            | Forward+ does.           | first.                   |
+---------------------+--------------------------+--------------------------+--------------------------+
| Rendering cost      | Low base cost, but       | Medium base cost, and    | Highest base cost, and   |
|                     | high scaling cost.       | low scaling cost.        | low scaling cost.        |
+---------------------+--------------------------+--------------------------+--------------------------+
| Rendering driver    | **OpenGL** (OpenGL ES    | Vulkan, Direct3D 12,     | Vulkan, Direct3D 12,     |
|                     | 3.0, OpenGL 3.3 Core     | Metal                    | Metal                    |
|                     | Profile, WebGL 2.0)      |                          |                          |
+---------------------+--------------------------+--------------------------+--------------------------+

Lights and shadows
~~~~~~~~~~~~~~~~~~

See :ref:`doc_lights_and_shadows` for more information.

+-------------------------+--------------------------+--------------------------+--------------------------+
| Feature                 | Compatibility            | Mobile                   | Forward+                 |
+=========================+==========================+==========================+==========================+
| Lighting approach       | Forward                  | Forward                  | Clustered Forward        |
|                         |                          |                          |                          |
+-------------------------+--------------------------+--------------------------+--------------------------+
| Maximum                 | 8 per mesh. Can be       | 8 per mesh, 256 per view.| Unlimited.               |
| OmniLights              | increased.               |                          |                          |
+-------------------------+--------------------------+--------------------------+--------------------------+
| Maximum                 | 8 per mesh. Can be       | 8 per mesh, 256 per view.| Unlimited.               |
| SpotLights              | increased.               |                          |                          |
+-------------------------+--------------------------+--------------------------+--------------------------+
| Maximum                 | 8                        | 8                        | 8                        |
| DirectionalLights       |                          |                          |                          |
+-------------------------+--------------------------+--------------------------+--------------------------+
| Maximum clustered       | N/A                      | N/A                      | 512. Can be increased.   |
| elements                |                          |                          |                          |
+-------------------------+--------------------------+--------------------------+--------------------------+
| PCSS for                | ❌ Not supported.        | ✔️ Supported.            | ✔️ Supported.            |
| OmniLight and SpotLight |                          |                          |                          |
+-------------------------+--------------------------+--------------------------+--------------------------+
| PCSS for                | ❌ Not supported.        | ❌ Not supported.        | ✔️ Supported.            |
| DirectionalLight        |                          |                          |                          |
+-------------------------+--------------------------+--------------------------+--------------------------+
| Light projector         | ❌ Not supported.        | ✔️ Supported.            | ✔️ Supported.            |
| textures                |                          |                          |                          |
+-------------------------+--------------------------+--------------------------+--------------------------+

Global Illumination
~~~~~~~~~~~~~~~~~~~

See :ref:`doc_introduction_to_global_illumination` for more information.

+-------------------------+--------------------------+--------------------------+--------------------------+
| Feature                 | Compatibility            | Mobile                   | Forward+                 |
+=========================+==========================+==========================+==========================+
| ReflectionProbe         | ⚠️ Planned.              | ✔️ Supported.            | ✔️ Supported.            |
|                         |                          |                          |                          |
+-------------------------+--------------------------+--------------------------+--------------------------+
| LightmapGI              | ⚠️ Planned.              | ✔️ Supported.            | ✔️ Supported.            |
|                         |                          |                          |                          |
+-------------------------+--------------------------+--------------------------+--------------------------+
| VoxelGI                 | ❌ Not supported.        | ❌ Not supported.        | ✔️ Supported.            |
|                         |                          |                          |                          |
+-------------------------+--------------------------+--------------------------+--------------------------+
| Screen-Space            | ❌ Not supported.        | ❌ Not supported.        | ✔️ Supported.            |
| Indirect Lighting (SSIL)|                          |                          |                          |
+-------------------------+--------------------------+--------------------------+--------------------------+
| Signed Distance Field   | ❌ Not supported.        | ❌ Not supported.        | ✔️ Supported.            |
| Global Illumination     |                          |                          |                          |
| (SDFGI)                 |                          |                          |                          |
+-------------------------+--------------------------+--------------------------+--------------------------+
| Reflection probes       | ❌ Not supported.        | ✔️ Supported.            | ✔️ Supported.            |
+-------------------------+--------------------------+--------------------------+--------------------------+

Environment and post-processing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See :ref:`doc_environment_and_post_processing` for more information.

+-------------------------+--------------------------+--------------------------+--------------------------+
| Feature                 | Compatibility            | Mobile                   | Forward+                 |
+=========================+==========================+==========================+==========================+
| Fog (Depth and Height)  | ✔️ Supported.            | ✔️ Supported.            | ✔️ Supported.            |
+-------------------------+--------------------------+--------------------------+--------------------------+
| Volumetric Fog          | ❌ Not supported.        | ❌ Not supported.        | ✔️ Supported.            |
+-------------------------+--------------------------+--------------------------+--------------------------+
| Tonemapping             | ✔️ Supported.            | ✔️ Supported.            | ✔️ Supported.            |
+-------------------------+--------------------------+--------------------------+--------------------------+
| Screen-Space Reflections| ❌ Not supported.        | ❌ Not supported.        | ✔️ Supported.            |
+-------------------------+--------------------------+--------------------------+--------------------------+
| Screen-Space Ambient    | ❌ Not supported.        | ❌ Not supported.        | ✔️ Supported.            |
| Occlusion (SSAO)        |                          |                          |                          |
+-------------------------+--------------------------+--------------------------+--------------------------+
| Screen-Space            | ❌ Not supported.        | ❌ Not supported.        | ✔️ Supported.            |
| Indirect Lighting (SSIL)|                          |                          |                          |
+-------------------------+--------------------------+--------------------------+--------------------------+
| Signed Distance Field   | ❌ Not supported.        | ❌ Not supported.        | ✔️ Supported.            |
| Global Illumination     |                          |                          |                          |
| (SDFGI)                 |                          |                          |                          |
+-------------------------+--------------------------+--------------------------+--------------------------+
| Glow                    | ✔️ Supported.            | ✔️ Supported.            | ✔️ Supported.            |
+-------------------------+--------------------------+--------------------------+--------------------------+
| Adjustments             | ✔️ Supported.            | ✔️ Supported.            | ✔️ Supported.            |
+-------------------------+--------------------------+--------------------------+--------------------------+
| Custom post-processing  | ✔️ Supported.            | ✔️ Supported.            | ✔️ Supported.            |
| with fullscreen quad    |                          |                          |                          |
+-------------------------+--------------------------+--------------------------+--------------------------+
| Custom post-processing  | ❌ Not supported.        | ✔️ Supported.            | ✔️ Supported.            |
| with CompositorEffects  |                          |                          |                          |
+-------------------------+--------------------------+--------------------------+--------------------------+

Antialiasing
~~~~~~~~~~~~

See :ref:`doc_3d_antialiasing` for more information.

+-------------------+--------------------------+--------------------------+--------------------------+
| Feature           | Compatibility            | Mobile                   | Forward+                 |
+===================+==========================+==========================+==========================+
| MSAA              | ✔️ Supported.            | ✔️ Supported.            | ✔️ Supported.            |
+-------------------+--------------------------+--------------------------+--------------------------+
| TAA               | ❌ Not supported.        | ❌ Not supported.        | ✔️ Supported.            |
+-------------------+--------------------------+--------------------------+--------------------------+
| FSR2              | ❌ Not supported.        | ❌ Not supported.        | ✔️ Supported.            |
+-------------------+--------------------------+--------------------------+--------------------------+
| FXAA              | ❌ Not supported.        | ✔️ Supported.            | ✔️ Supported.            |
+-------------------+--------------------------+--------------------------+--------------------------+
| SSAA              | ❌ Not supported.        | ✔️ Supported.            | ✔️ Supported.            |
+-------------------+--------------------------+--------------------------+--------------------------+
| Screen-space      | ❌ Not supported.        | ✔️ Supported.            | ✔️ Supported.            |
| roughness limiter |                          |                          |                          |
+-------------------+--------------------------+--------------------------+--------------------------+

StandardMaterial features
~~~~~~~~~~~~~~~~~~~~~~~~~

See :ref:`doc_standard_material_3d` for more information.

+-------------------------+--------------------------+--------------------------+--------------------------+
| Feature                 | Compatibility            | Mobile                   | Forward+                 |
+=========================+==========================+==========================+==========================+
| Sub-surface scattering  | ❌ Not supported.        | ❌ Not supported.        | ✔️ Supported.            |
|                         |                          |                          |                          |
+-------------------------+--------------------------+--------------------------+--------------------------+

Shader features
~~~~~~~~~~~~~~~

See :ref:`doc_shading_reference` for more information.

+-------------------------+--------------------------+--------------------------+--------------------------+
| Feature                 | Compatibility            | Mobile                   | Forward+                 |
+=========================+==========================+==========================+==========================+
| Screen texture          | ✔️ Supported.            | ✔️ Supported.            | ✔️ Supported.            |
+-------------------------+--------------------------+--------------------------+--------------------------+
| Depth texture           | ✔️ Supported.            | ✔️ Supported.            | ✔️ Supported.            |
|                         |                          |                          |                          |
+-------------------------+--------------------------+--------------------------+--------------------------+
| Normal/Roughness texture| ❌ Not supported.        | ✔️ Supported.            | ✔️ Supported.            |
+-------------------------+--------------------------+--------------------------+--------------------------+
| Compute shaders         | ❌ Not supported.        | ⚠️ Limited.              | ✔️ Supported.            |
+-------------------------+--------------------------+--------------------------+--------------------------+

Other features
~~~~~~~~~~~~~~

+-------------------------+--------------------------+--------------------------+--------------------------+
| Feature                 | Compatibility            | Mobile                   | Forward+                 |
+=========================+==========================+==========================+==========================+
| Variable rate           | ❌ Not supported.        | ✔️ Supported.            | ✔️ Supported.            |
| shading                 |                          |                          |                          |
+-------------------------+--------------------------+--------------------------+--------------------------+
| Decals                  | ❌ Not supported.        | ✔️ Supported.            | ✔️ Supported.            |
+-------------------------+--------------------------+--------------------------+--------------------------+
| Depth of field blur     | ❌ Not supported.        | ✔️ Supported.            | ✔️ Supported.            |
+-------------------------+--------------------------+--------------------------+--------------------------+
| Adaptive and Mailbox    | ❌ Not supported.        | ✔️ Supported.            | ✔️ Supported.            |
| VSync modes             |                          |                          |                          |
+-------------------------+--------------------------+--------------------------+--------------------------+
| 2D HDR Viewport         | ❌ Not supported.        | ✔️ Supported.            | ✔️ Supported.            |
+-------------------------+--------------------------+--------------------------+--------------------------+
| RenderingDevice         | ❌ Not supported.        | ✔️ Supported.            | ✔️ Supported.            |
| access                  |                          |                          |                          |
+-------------------------+--------------------------+--------------------------+--------------------------+
