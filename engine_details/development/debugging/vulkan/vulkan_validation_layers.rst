.. _doc_vulkan_validation_layers:

Validation layers
=================

Validation layers enable developers to verify their application's correct use of
the Vulkan API. Validation layers can be enabled in both debug and release
builds, including in exported projects.

.. note::

    Enabling validation layers has a performance impact, so only enable them
    when you actually need the output to debug the application.

Windows
-------

Install the Vulkan SDK `<https://vulkan.lunarg.com/sdk/home>`__, which contains
validation layers as part of its default installation. No need to enable any
optional features in the installer; installing the core Vulkan SDK suffices. You
don't need to reboot after installing the SDK, but you may need to close and
reopen your current terminal.

After installing the Vulkan SDK, run Godot with the ``--gpu-validation``
:ref:`command line argument <doc_command_line_tutorial>`. You can also specify
``--gpu-abort`` which will make Godot quit as soon as a validation error happens.
This can prevent your system from freezing if a validation error occurs.

macOS
-----

.. warning::

    Official Godot macOS builds do **not** support validation layers, as these
    are statically linked against the Vulkan SDK. Dynamic linking must be used
    instead.

    In practice, this means that using validation layers on macOS **requires**
    you to use a Godot build compiled with the ``use_volk=yes`` SCons option.
    :ref:`doc_compiling_for_macos`. If testing validation layers on an exported
    project, you must recompile the export template and specify it as a custom
    export template in your project's macOS export preset.

Install the Vulkan SDK `<https://vulkan.lunarg.com/sdk/home>`__, which contains
validation layers as part of its default installation. No need to enable any
optional features in the installer; installing the core Vulkan SDK suffices. You
don't need to reboot after installing the SDK, but you may need to close and
reopen your current terminal.

After installing the Vulkan SDK, run a Godot binary that was compiled with
``use_volk=yes`` SCons option. Specify the ``--gpu-validation``
:ref:`command line argument <doc_command_line_tutorial>`.
You can also specify ``--gpu-abort`` which will make Godot quit as soon
as a validation error happens. This can prevent your system from freezing
if a validation error occurs.

Linux, \*BSD
------------

Install Vulkan validation layers from your distribution's repositories:

.. tabs::

    .. tab:: Alpine Linux

        ::

            vulkan-validation-layers

    .. tab:: Arch Linux

        ::

            pacman -S vulkan-validation-layers

    .. tab:: Debian/Ubuntu

        ::

            apt install vulkan-validationlayers

    .. tab:: Fedora

        ::

            dnf install vulkan-validation-layers

    .. tab:: FreeBSD

        ::

            pkg install graphics/vulkan-validation-layers

    .. tab:: Gentoo

        ::

            emerge -an media-libs/vulkan-layers

    .. tab:: Mageia

        ::

            urpmi vulkan-validation-layers

    .. tab:: OpenBSD

        ::

            pkg_add graphics/vulkan-validation-layers

    .. tab:: openSUSE

        ::

            zypper install vulkan-validationlayers

    .. tab:: Solus

        ::

            eopkg install -c vulkan-validation-layers

You don't need to reboot after installing the validation layers, but you may
need to close and reopen your current terminal.

After installing the package, run Godot with the ``--gpu-validation``
:ref:`command line argument <doc_command_line_tutorial>`. You can also specify
``--gpu-abort`` which will make Godot quit as soon as a validation error happens.
This can prevent your system from freezing if a validation error occurs.

.. _doc_vulkan_validation_layers_android:

Android
-------

After enabling validation layers on Android, a developer can see errors and
warning messages in the ``adb logcat`` output.

iOS
---

Validation layers are currently **not** supported on iOS.

Web
---

Validation layers are **not** supported on the web platform, as there is no support
for Vulkan there.

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

Your Godot source directory tree should look like on the example below:

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

Compile and run the Android app
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Linked validation layers are automatically loaded and enabled in Android debug builds.
You can use Godot's :ref:`doc_one-click_deploy` feature to quickly test your project with the validation layers enabled.
