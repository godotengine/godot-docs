.. _doc_vulkan_validation_layers:

Validation layers
=================

Validation layers enable developers to verify their application's correct use
of the Vulkan API.

.. _doc_vulkan_validation_layers-android:

Android
-------

After enabling validation layers on Android, a developer can see errors and
warning messages in the ``adb logcat`` output.

Enabling validation layers
~~~~~~~~~~~~~~~~~~~~~~~~~~

Build validation layers from official sources
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To build Android libraries, follow the instructions on
`Khronos' repository  <https://github.com/KhronosGroup/Vulkan-ValidationLayers/blob/master/BUILD.md#building-on-android>`__.
After a successful build, the libraries will be located in ``Vulkan-ValidationLayers/build-android/libs``.

Copy libraries
^^^^^^^^^^^^^^

Copy libraries from ``Vulkan-ValidationLayers/build-android/libs`` to
``godot/platform/android/java/app/libs/debug/vulkan_validation_layers``.

Your Godot source directory tree should look like on the example below::

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

Compile and run the Android app
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Linked validation layers are automatically loaded and enabled in Android debug builds.
You can use Godot's :ref:`doc_one-click_deploy` feature to quickly test your project with the validation layers enabled.
