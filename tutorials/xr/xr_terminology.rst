.. _doc_xr_terminology:

XR Terminology
==============

This page defines how terms such as *XR*, *VR*, *AR*, and *MR* are used within Godot.

These terms are not always used consistently across the industry. In Godot, we use clear
and practical definitions to avoid ambiguity and to better reflect how these technologies
are actually implemented.

XR (Extended Reality)
---------------------

**XR** is an umbrella term that covers all immersive technologies supported by Godot.

In practice, XR refers to the complete system exposed through the
:ref:`XRServer <class_xrserver>` and related APIs. This system abstracts away platform
differences and provides a unified way to build immersive applications.

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

**Virtual Reality (VR)** refers to fully immersive experiences where the user is placed
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

AR (Augmented Reality)
----------------------

.. raw:: html

    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube-nocookie.com/embed/8B8RnFokAFc" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
    </div>

**Augmented Reality (AR)** refers to experiences where virtual content is overlaid onto
the real world.

In these applications, the user continues to see their physical surroundings, while
virtual objects are rendered in a way that makes them appear part of that environment.

In Godot, AR is used in two different contexts.

Passthrough AR (XR devices)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

This refers to Augmented Reality experiences on XR headsets that use built-in cameras
to capture the real world and display it inside the headset.

The application renders virtual content on top of this camera feed, allowing users to
interact with virtual objects while still being aware of their surroundings.

- Uses XR interfaces
- Relies on camera passthrough provided by the device
- Runs on head-mounted devices

From Godot's perspective, this is part of the XR system and uses the same APIs as VR.
See :ref:`AR passthrough <doc_openxr_passthrough>` for more details.

Handheld AR (mobile devices)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This refers to Augmented Reality experiences on handheld devices, such as phones and tablets.

These applications use the device camera to display the real world on screen, while
sensor data (such as motion tracking and environment detection) is used to position
virtual objects in a stable and believable way.

This allows virtual content to appear anchored in the real world when viewed through
the device.

Implementation is done through platform-specific plugins:

- `ARKit plugin (iOS) <https://docs.godotengine.org/de/4.x/tutorials/platform/ios/plugins_for_ios.html>`_
- `ARCore plugin (Android) <https://github.com/godotvr/godot_arcore>`_

These integrations are separate from the XR interface system and must be set up
individually.

MR (Mixed Reality)
------------------

**Mixed Reality (MR)** is a term that is used inconsistently across the industry.

It is often used to describe a range of experiences between VR and AR, or to refer to
passthrough-based systems on XR headsets.

In practice, MR does not represent a clearly defined technical category and is often
used interchangeably with AR.

.. note::

    In Godot documentation, MR is not used as a separate classification.

    Experiences commonly referred to as "MR" are treated as **AR**, specifically
    passthrough AR on XR devices.

    This keeps terminology consistent and avoids ambiguity.