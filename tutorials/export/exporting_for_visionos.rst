.. _doc_exporting_for_visionos:

Exporting for visionOS
======================

.. seealso::

    This page describes how to export a Godot project to visionOS.
    If you're looking to compile export template binaries from source instead,
    follow the :ref:`doc_compiling_for_ios` instructions with ``platform=visionos``
    (visionOS reuses the iOS/Apple-embedded toolchain).

Exporting instructions for visionOS are currently identical to
:ref:`doc_compiling_for_ios`, except you should add a **visionOS**
export preset instead of **iOS**. See the linked page for details.

Godot supports two kinds of visionOS apps:

- **Windowed** -- your Godot project runs inside a flat window placed in the
  user's space, like an iPad app on visionOS. This is the default.
- **Immersive** -- your Godot project renders stereoscopically through
  CompositorServices and ARKit, either fully immersive (replacing the
  surroundings) or in mixed immersion (composited over passthrough).

.. note::

    Immersive visionOS support is provided by the **visionOS XR** module.
    Windowed export works without any XR setup.

Immersive experiences
---------------------

To run immersively, enable the visionOS XR interface from a script that runs at
startup, and set the project up to request an immersive app role.

Project setup
~~~~~~~~~~~~~

In the **visionOS** export preset:

- Set **Application > App Role** to **Immersive**.
- Set **Application > Immersion Style** to **Full** or **Mixed** depending on
  whether you want to replace the user's surroundings or composite over
  passthrough.

Startup script
~~~~~~~~~~~~~~

Initialize the XR interface in ``_ready()`` (not ``_process()`` -- calling the
visionOS APIs mid-frame causes problems), and turn on the XR viewport:

.. code-block:: gdscript

    func _ready() -> void:
        var xr_interface := XRServer.find_interface("visionOS")
        if xr_interface and xr_interface.initialize():
            var viewport := get_viewport()
            viewport.use_xr = true
            viewport.vrs_mode = Viewport.VRS_XR
            viewport.use_hdr_2d = true
        else:
            OS.alert("Unable to start visionOS XR interface")

.. warning::

    ``Viewport.VRS_XR`` is **required** on this platform -- it carries the
    mandatory CompositorServices foveation (rasterization rate) map. Setting
    ``vrs_mode`` to ``VRS_DISABLED`` breaks the compositor hand-off and the app
    renders nothing.

Common pitfalls
---------------

Several visionOS-specific requirements fail *silently* -- the app launches and
holds a locked 90 FPS while rendering nothing or showing artifacts. Check these
first.

The XR origin must be current
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Set ``current = true`` on your :ref:`class_XROrigin3D` node (in the Inspector or
from code). If no origin is current, the headset has no tracking origin to
render from: you get a locked 90 FPS and a black/empty view, with no error.
This is the single most common silent failure.

Use the Mobile rendering method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

visionOS immersive rendering requires the **Mobile** rendering method
(``rendering/renderer/rendering_method.mobile`` / set **Rendering Method** to
**Mobile** in Project Settings). The **Forward+** method renders nothing on this
path, again with no error -- an easy trap when porting an existing desktop
project.

Camera near plane must be at least 0.1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Apple Vision Pro enforces a minimum near-plane distance. Set your
:ref:`class_XRCamera3D`'s ``near`` to **0.1** or greater (the engine default of
``0.05`` is below the minimum). If ``near`` divided by the
:ref:`class_XROrigin3D`'s world scale is below the platform minimum, nothing
renders. The interface logs the reason to **Console.app**:

.. code-block:: none

    Your XRCamera3D Near value is lower than the minimum value supported by the
    visionOS platform. Make sure that Near divided by XROrigin's World Scale is
    higher than or equal to the value returned by
    LayerRender.Capabilities.supportedMinimumNearPlaneDistance. This value is 0.1
    for Apple Vision Pro.

Mixed immersion: depth and transparency
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In mixed immersion, CompositorServices composites your content over passthrough
using the rendered frame's alpha channel, with one rule: **wherever depth is 0
(nothing drawn), alpha must also be 0.** Pixels that write a non-zero alpha but
no depth -- a :ref:`class_WorldEnvironment` background with non-zero alpha, or
transparent / additive geometry that does not write depth (glow, halos, sky
dissolves) -- produce blocky grey artifacts around your content.

Two fixes:

1. Make sure your :ref:`class_WorldEnvironment` background's color **alpha is 0**,
   and force any offending transparent objects to write depth (or make them
   opaque).
2. Add a full-screen quad post-process pass that writes a tiny depth to every
   pixel, so depth is never exactly 0. This is the most general fix and works
   even with a clear-color background (see the
   :ref:`full-screen quad tutorial <doc_advanced_postprocessing>`):

   .. code-block:: glsl

       shader_type spatial;
       render_mode unshaded, fog_disabled, depth_draw_always, blend_mix;

       #define DEPTH_BIAS 0.00000001

       void vertex() {
           POSITION = vec4(VERTEX.xy, DEPTH_BIAS, 1.0);
       }

       void fragment() {
           ALBEDO = vec3(0.0);
           ALPHA = 0.0;
       }

Hand and controller tracking
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Head-pose tracking works out of the box in immersive mode, and the user's
upper limbs are composited automatically with correct depth -- no code needed.
Pinch input, hand tracking, and PSVR2 controller tracking are planned as
follow-up additions and may not be available in your build yet.
