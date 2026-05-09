.. _doc_xr_terminology:

XR Terminology
==============

This page defines how terms such as *XR*, *VR*, and *AR* are used within Godot.

These terms are not always used consistently across the industry. In Godot, we use clear
and practical definitions to avoid ambiguity and to better reflect how these technologies
are actually implemented.

XR (Extended Reality)
---------------------

**XR** is an umbrella term that covers all extended reality technologies supported by Godot.

In practice, XR refers to the complete system exposed through the
:ref:`XRServer <class_xrserver>` and related APIs. This system abstracts away platform
differences and provides a unified way to build XR applications.

XR includes:

- Virtual Reality (VR)
- Augmented Reality (AR)

From a development perspective, XR is the entry point for working with both fully
virtual experiences and those that combine virtual and real-world elements.

VR (Virtual Reality)
--------------------

.. raw:: html

    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube-nocookie.com/embed/xJKQ2ca5zVw" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
    </div>

**Virtual Reality (VR)** refers to fully **immersive** experiences where the user is placed
inside a completely virtual environment.

When using VR, the user does not see the real world. Instead, everything they see is
rendered by the application, and their movement is tracked and applied to the virtual
camera and controllers.

In Godot, VR typically involves:

- Head-mounted displays (HMDs)
- Fully virtual 3D scenes
- 6DOF (six degrees of freedom) tracking for head and controllers

This is the most common use of XR in Godot. See
:ref:`Setting up XR <doc_setting_up_xr>` for how to get started.

.. note::

    Even in VR applications, passthrough can be used if supported by the headset.

    In this case, passthrough is typically used to reveal specific real-world
    elements, such as a keyboard, mouse, or other peripherals, while the rest
    of the experience remains fully virtual.

    This is a hybrid use case and differs from Augmented Reality, as passthrough
    is not used to place virtual content into the real world, but to selectively
    expose parts of the real world within a VR experience.

AR (Augmented Reality)
----------------------

.. raw:: html

    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube-nocookie.com/embed/8B8RnFokAFc" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
    </div>

**Augmented Reality (AR)** refers to experiences where virtual content is overlaid onto
the real world.

The user continues to see their physical surroundings, while virtual objects are rendered
in a way that makes them appear part of that environment.

In Godot, AR is treated as a single concept, regardless of the type of device used.
This includes XR headsets using camera passthrough, see-through glasses with displays, and handheld devices
such as phones and tablets.

For XR devices and AR glasses that support standards such as OpenXR or WebXR, AR
functionality is available through the XR system. In these cases, applications can run
across different devices with minimal changes. Passthrough on VR headsets is one example
of this, and is simply a technical method used to enable AR capabilities on such devices.

Outside of Godot, this type of experience is sometimes referred to as "Mixed Reality (MR)".
In Godot documentation, this is treated as Augmented Reality to avoid ambiguity.
Passthrough is considered an implementation detail, not a separate category.

See :ref:`AR passthrough <doc_openxr_passthrough>` for an example of AR using the XR system.

.. note::

    Handheld platforms such as phones and tablets currently do not provide OpenXR support.

    Instead, AR functionality is exposed through proprietary APIs and requires
    platform-specific plugins:

	- `ARCore plugin (Android) <https://github.com/godotvr/godot_arcore>`_

    This results in platform-specific implementations that are not fully portable.

    OpenXR is capable of supporting handheld AR. If adopted by platform vendors, this would
    allow AR applications to run across phones, headsets, and glasses using a shared codebase.