.. _doc_mobilevr_intro:

Mobile VR
=========

Godot has a mobile VR implementation that is meant to be used with phones placed inside of a VR holder.
It is implemented through the :ref:`MobileVRInterface <class_mobilevrinterface>`.
This is a bare bones implementation that outputs a side by side stereoscopic image.
It supports basic 3DOF tracking on phones that provide gyroscope and accelerometer data.

.. warning::

    This implementation is not actively maintained. As it allows maintainers and reviewers the ability
    to test stereoscopic rendering without the need for expensive XR hardware,
    this XR interface is mostly used for diagnostic purposes.


.. tabs::
  .. code-tab:: gdscript GDScript

    extends Node3D

    var xr_interface: XRInterface

    func _ready() -> void:
        xr_interface = XRServer.find_interface("Native mobile")
        if xr_interface and xr_interface.initialize():
            print("Mobile VR initialized successfully")

            # Change our main viewport to output to the HMD.
            get_viewport().use_xr = true
        else:
            print("Mobile VR not initialized, please check if your headset is connected")

  .. code-tab:: csharp

    using Godot;

    public partial class MyNode3D : Node3D
    {
        private XRInterface _xrInterface;

        public override void _Ready()
        {
            _xrInterface = XRServer.FindInterface("Native mobile");
            if(_xrInterface != null && _xrInterface.Initialize())
            {
                GD.Print("Mobile VR initialized successfully");

                // Change our main viewport to output to the HMD.
                GetViewport().UseXR = true;
            }
            else
            {
                GD.Print("Mobile VR not initialized, please check if your headset is connected");
            }
        }
    }

The mobile VR interface has various settings that control the output provided to screen.
The most important two are the ``k1`` and ``k2`` constants that affect the amount of barrel distortion
that is applied to counter the lens distortion of the VR phone holder used.
Many have a QR code you can scan that provides this information.

It is also important to provide the correct dimensions of the device and the phone's display, these metrics are stored in centimeters.
