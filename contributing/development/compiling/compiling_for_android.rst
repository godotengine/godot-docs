.. _doc_compiling_for_android:

Compiling for Android
=====================

.. highlight:: shell

.. seealso::

    This page describes how to compile Android export template binaries from source.
    If you're looking to export your project to Android instead, read :ref:`doc_exporting_for_android`.

Note
----

In most cases, using the built-in deployer and export templates is good
enough. Compiling the Android APK manually is mostly useful for custom
builds or custom packages for the deployer.

Also, you still need to follow the steps mentioned in the
:ref:`doc_exporting_for_android` tutorial before attempting to build
a custom export template.

Requirements
------------

For compiling under Windows, Linux or macOS, the following is required:

- `Python 3.6+ <https://www.python.org/downloads/>`_.
- `SCons 3.0+ <https://scons.org/pages/download.html>`_ build system.
- `Android SDK <https://developer.android.com/studio/#command-tools>`_
  (command-line tools are sufficient).

   - Required SDK components will be automatically installed.
   - On Linux,
      **do not use an Android SDK provided by your distribution's repositories as it will often be outdated**.

- Gradle (will be downloaded and installed automatically if missing).
- JDK 17 (either OpenJDK or Oracle JDK).

   - You can download a build from `ojdkbuild <https://adoptium.net/temurin/releases/?variant=openjdk17>`_.

.. seealso:: To get the Godot source code for compiling, see
             :ref:`doc_getting_source`.

             For a general overview of SCons usage for Godot, see
             :ref:`doc_introduction_to_the_buildsystem`.

.. _doc_android_setting_up_the_buildsystem:

Setting up the buildsystem
--------------------------

-  Set the environment variable ``ANDROID_HOME`` to point to the Android
   SDK. If you downloaded the Android command-line tools, this would be
   the folder where you extracted the contents of the ZIP archive.

-  Install the necessary SDK components in this folder:

    -  Accept the SDK component licenses by running the following command
       where ``android_sdk_path`` is the path to the Android SDK, then answering all the prompts with ``y``:

    ::

        cmdline-tools/latest/bin/sdkmanager --sdk_root=<android_sdk_path> --licenses

    -  Complete setup by running the following command where ``android_sdk_path`` is the path to the Android SDK.

    ::

        cmdline-tools/latest/bin/sdkmanager --sdk_root=<android_sdk_path> "platform-tools" "build-tools;30.0.3" "platforms;android-29" "cmdline-tools;latest" "cmake;3.10.2.4988404"

.. seealso::   To set the environment variable on Windows, press :kbd:`Windows + R`, type
            "control system", then click on **Advanced system settings** in the left
            pane, then click on **Environment variables** on the window that appears.

.. seealso::   To set the environment variable on Linux or macOS, use
            ``export ANDROID_HOME=/path/to/android-sdk`` where ``/path/to/android-sdk`` points to
            the root of the SDK directories.

Building the export templates
-----------------------------

Godot needs two export templates for Android: the optimized "release"
template (``android_release.apk``) and the debug template (``android_debug.apk``).
As Google requires all APKs to include ARMv8 (64-bit) libraries since August 2019,
the commands below build an APK containing both ARMv7 and ARMv8 libraries.

Compiling the standard export templates is done by calling SCons from the Godot
root directory with the following arguments:

-  Release template (used when exporting with **Debugging Enabled** unchecked)

::

    scons platform=android target=template_release arch=arm32
    scons platform=android target=template_release arch=arm64 generate_apk=yes

.. note::

    If you are changing the list of architectures you're building, remember to add
    ``generate_apk=yes`` to the *last* architecture you're building, so that an APK
    file is generated after the build.

The resulting APK will be located at ``bin/android_release.apk``.

-  Debug template (used when exporting with **Debugging Enabled** checked)

::

    scons platform=android target=template_debug arch=arm32
    scons platform=android target=template_debug arch=arm64 generate_apk=yes

The resulting APK will be located at ``bin/android_debug.apk``.

.. seealso::

    If you want to enable Vulkan validation layers, see
    :ref:`Vulkan validation layers on Android <doc_vulkan_validation_layers_android>`.

Adding support for x86 devices
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you also want to include support for x86 and x86_64 devices, run the SCons
command a third and fourth time with the ``arch=x86_32``, and
``arch=x86_64`` arguments before building the APK with Gradle. For
example, for the release template:

::

    scons platform=android target=template_release arch=arm32
    scons platform=android target=template_release arch=arm64
    scons platform=android target=template_release arch=x86_32
    scons platform=android target=template_release arch=x86_64 generate_apk=yes

This will create a fat binary that works on all platforms.
The final APK size of exported projects will depend on the platforms you choose
to support when exporting; in other words, unused platforms will be removed from
the APK.

Cleaning the generated export templates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can use the following commands to remove the generated export templates:

::

    cd platform/android/java
    # On Windows
    .\gradlew clean
    # On Linux and macOS
    ./gradlew clean


Using the export templates
--------------------------

Godot needs release and debug APKs that were compiled against the same
version/commit as the editor. If you are using official binaries
for the editor, make sure to install the matching export templates,
or build your own from the same version.

When exporting your game, Godot opens the APK, changes a few things inside and
adds your files.

Installing the templates
~~~~~~~~~~~~~~~~~~~~~~~~

The newly-compiled templates (``android_debug.apk``
and ``android_release.apk``) must be copied to Godot's templates folder
with their respective names. The templates folder can be located in:

-  Windows: ``%APPDATA%\Godot\export_templates\<version>\``
-  Linux: ``$HOME/.local/share/godot/export_templates/<version>/``
-  macOS: ``$HOME/Library/Application Support/Godot/export_templates/<version>/``

``<version>`` is of the form ``major.minor[.patch].status`` using values from
``version.py`` in your Godot source repository (e.g. ``4.1.3.stable`` or ``4.2.dev``).
You also need to write this same version string to a ``version.txt`` file located
next to your export templates.

.. TODO: Move these paths to a common reference page

However, if you are writing your custom modules or custom C++ code, you
might instead want to configure your APKs as custom export templates
here:

.. image:: img/andtemplates.png

You don't even need to copy them, you can just reference the resulting
file in the ``bin\`` directory of your Godot source folder, so that the
next time you build you will automatically have the custom templates
referenced.

Building the Godot editor
-------------------------

Compiling the editor is done by calling SCons from the Godot
root directory with the following arguments:

::

   scons platform=android arch=arm32 production=yes target=editor
   scons platform=android arch=arm64 production=yes target=editor
   scons platform=android arch=x86_32 production=yes target=editor
   scons platform=android arch=x86_64 production=yes target=editor generate_apk=yes

You can skip certain architectures depending on your target device to speed up
compilation. Remember to add ``generate_apk=yes`` to the *last* architecture
you're building, so that an APK file is generated after the build.

The resulting APK will be located at ``bin/android_editor_builds/android_editor-release.apk``.

Removing the Editor templates
-----------------------------

You can use the following commands to remove the generated editor templates:

::

    cd platform/android/java
    # On Windows
   .\gradlew clean
   # On Linux and macOS
   ./gradlew clean

Installing the Godot editor
---------------------------

With an Android device with Developer Options enabled, connect the Android device to your computer via its charging cable to a USB/USB-C port.
Open up a Terminal/Command Prompt and run the following commands from the root directory with the following arguments:

::

   adb install ./bin/android_editor_builds/android_editor-release.apk

Troubleshooting
---------------

Platform doesn't appear in SCons
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Double-check that you've set the ``ANDROID_HOME``
environment variable. This is required for the platform to appear in SCons'
list of detected platforms.
See :ref:`Setting up the buildsystem <doc_android_setting_up_the_buildsystem>`
for more information.

Application not installed
~~~~~~~~~~~~~~~~~~~~~~~~~

Android might complain the application is not correctly installed.
If so:

-  Check that the debug keystore is properly generated.
-  Check that the jarsigner executable is from JDK 8.

If it still fails, open a command line and run `logcat <https://developer.android.com/studio/command-line/logcat>`_:

::

    adb logcat

Then check the output while the application is installed;
the error message should be presented there.
Seek assistance if you can't figure it out.

Application exits immediately
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If the application runs but exits immediately, this might be due to
one of the following reasons:

-  Make sure to use export templates that match your editor version; if
   you use a new Godot version, you *have* to update the templates too.
-  ``libgodot_android.so`` is not in ``libs/<arch>/``
   where ``<arch>`` is the device's architecture.
-  The device's architecture does not match the exported one(s).
   Make sure your templates were built for that device's architecture,
   and that the export settings included support for that architecture.

In any case, ``adb logcat`` should also show the cause of the error.
