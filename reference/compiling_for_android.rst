.. _doc_compiling_for_android:

Compiling for Android
=====================

.. highlight:: shell

Note
----

For most cases, using the built-in deployer and export templates is good
enough. Compiling the Android APK manually is mostly useful for custom
builds or custom packages for the deployer.

Also, you still need to do all the steps mentioned in the
:ref:`doc_exporting_for_android` tutorial before attempting your custom
export template.

A. Requirements
---------------

For compiling under Windows, Linux or OSX, the following is required:

-  Python 2.7+ [3.0 is untested as of now]
-  pywin32 [Optional, Windows only. Applied when -j(number of cores) specified]
-  SCons build system
-  Android SDK version 19 [Note: Please install all Tools and Extras of sdk manager]
-  Android build tools version 19.1
-  Android NDK r10e or later
-  Gradle [will be downloaded and installed when compiling for android if it doesn't exist]
-  JDK 6+ (Oracle's releases) or OpenJDK 6+

B. Setting up Build System
--------------------------------------------------------

1) Scons : please, refer to their respective docs

2) Gradle : will be automatically setup upon packing APK if 
we do not have gradle installed previously (may require working internet connection)

3) Android :

Set the environment variable ANDROID_HOME to point to the Android
SDK.

Set the environment variable ANDROID_NDK_ROOT to point to the
Android NDK.

- on Windows :
press Windows+R, type "control system", then click on **Advanced system settings**
in the left pane, then click on **Environment variables** on the window that appears.

- on Unix (eg. Linux and Mac OS):
Open up Terminal and then execute commands below :
``export ANDROID_HOME=/path/to/android-sdk`` and
``export ANDROID_NDK_ROOT=/path/to/android-ndk``

C. Compiling
------------

C1. Compiling the Engine
------------------------

Go to the root dir of the engine source code and type:

::

    C:\godot> scons platform=android

This should result in a regular .so file (built for ARM platform) in ``\bin`` folder, as if it was
compiled with flags: ``tools=no target=debug``. The resulting file will
be huge because it will contain all debug symbols.

::

    C:\godot> bin\libgodot.android.debug.armv7.neon.so

If you also want to include support for x86 Android, add the following
compile flag: ``android_arch=x86``.

::

    C:\godot> scons platform=android android_arch=x86

::

    C:\godot> bin\libgodot.android.debug.x86.neon.so

This will create a fat binary that works in both platforms, but will add
about more than 6 megabytes to the APK.

Note on Toolchain
-----------------

We usually try to keep the Godot Android build code up to date, but
Google changes their toolchain versions very often, so if compilation
fails due to wrong toolchain version, go to your NDK directory and check
the current number, then set the following environment variable:

::

    NDK_TARGET (by default set to "arm-linux-androideabi-4.9")

So, we have done compiling the engine, right? Very Good. Now, let's compile the Android Export Template.


C2. Compiling Android Export Templates
--------------------------------------

Godot needs the freshly compiled APK as export templates. It opens the
APK, changes a few things inside, adds your file and spits it back. It's
really handy! (and required some reverse engineering of the format).

Two export template files that required by Godot when exporting to Android are:
(1) android_debug.apk
(2) android_release.apk

- (1) android_debug.apk (debug Mode)

Picked by Editor when exporting with "Debugging Enabled" = ON

::

    C:\godot> scons -j4 platform=android target=release_debug
    C:\godot> cd platform\android\java
    C:\godot> gradlew assembleDebug

Resulting APK is in:

::

    C:\godot\bin\android_debug.apk

- (2) android_release.apk (release Mode)

Picked by Editor when exporting with "Debugging Enabled" = OFF

::

    C:\godot> scons -j4 platform=android target=release
    C:\godot> cd platform\android\java
    C:\godot> gradlew assembleRelease

Resulting APK is in:

::

    C:\godot\bin\android_release.apk

Note:
-----
It's optional but always be a good practice to clean build cache first before
executing next build command, as sometimes gradle could mess up when it can't
detect a new change we have made.

Now, both files (android_debug.apk and android_release.apk) are created.
It's the time to copied them to Editor "templates" folder.

- Windows :
C:\Users\[your_username]\AppData\Roaming\Godot\templates

- Linux :
/home/.godot/templates

- Mac OS :
/users/[your_username]/.godot/templates

However, if you are writing your custom modules or custom C++ code, you
might instead want to configure your APKs as custom export templates
here:

.. image:: /img/andtemplates.png

You don't even need to copy them, you can just reference the resulting
file in the ``bin\`` directory of your Godot source folder, so the next
time you build you automatically have the custom templates referenced.

D.) Troubleshooting
---------------

1.) Application not installed
~~~~~~~~~~~~~~~~~~~~~~~~~

Android might complain the application is not correctly installed. If
so, check the following:

-  Check that the debug keystore is properly generated.
-  Check that jarsigner is from JDK6.

If it still fails, open a command line and run logcat:

::

    C:\android-sdk\platform-tools> adb logcat

And check the output while the application is installed. Reason for
failure should be presented there.

Seek assistance if you can't figure it out.

2.) Application exits immediately
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If the application runs but exits immediately, there might be one of the
following reasons:

-  libgodot_android.so is not in ``lib/armeabi-v7a``
-  Device does not support armv7 (try compiling yourself for armv6)
-  Device is ARM, and apk is compiled for intel.

In any case, ``adb logcat`` should also show the cause of the error.
