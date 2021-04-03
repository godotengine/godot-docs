.. _doc_validation_layers_android:

Vulkan validation layers on Android
===================================

Validation layers enable developers to verify their application's correct use
of the Vulkan API. After enabling validation layers a developer can see errors
and warning messages in the `logcat's` output.

Enabling validation layers
--------------------------

Build validation layers from official sources
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To build Android libraries, follow the instructions on `Khronos' repository 
<https://https://github.com/KhronosGroup/Vulkan-ValidationLayers/blob/master/BUILD.md#building-on-android>`__.
After a successful build, the libraries will be located in ``Vulkan-ValidationLayers/build-android/libs``.

Copy libraries
~~~~~~~~~~~~~~

Copy libraries from ``Vulkan-ValidationLayers/build-android/libs`` to
``godot/platform/android/java/app/libs/debug/vulkan_validation_layers``.

Your Godot's directory tree should look like on the example below:

::

    godot
    |-- platform
        |-- android
            |-- java
                |-- app
                    |-- libs
                        |-- debug
                            |-- vulkan_validation_layers
                                |-- arm64-v8a
                                |-- armeabi-v7a
                                |-- x86
                                |-- x86_64

If the subdirectory ``libs/debug/vulkan_validation_layers`` doesn't exist, create it.


Compile and run android app
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Linked validation layers are automatically loaded and enabled in Android debug builds.
