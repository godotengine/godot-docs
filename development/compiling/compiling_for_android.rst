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

Requirements
------------

For compiling under Windows, Linux or macOS, the following is required:

-  Python 2.7+ or Python 3.5+
-  SCons build system
-  [Windows only] PyWin32 (optional, for parallel compilation)
-  Android SDK version 23.0.3 [Note: Please install all tools and extras of the SDK Manager]
-  Android build tools version 19.1
-  Android NDK r13 or later
-  Gradle (will be downloaded and installed automatically if missing)
-  JDK 6 or later (either OpenJDK or Oracle JDK) - JDK 9 & 10 do not work with current Gradle.

Setting up the buildsystem
--------------------------

Set the environment variable ANDROID_HOME to point to the Android
SDK.

Set the environment variable ANDROID_NDK_ROOT to point to the
Android NDK.

To set those environment variables on Windows, press Windows+R, type
"control system", then click on **Advanced system settings** in the left
pane, then click on **Environment variables** on the window that
appears.

To set those environment variables on Unix (e.g. Linux, macOS), use
``export ANDROID_HOME=/path/to/android-sdk`` and
``export ANDROID_NDK_ROOT=/path/to/android-ndk``.
Where /path/to/android-sdk and /path/to/android-ndk is the path where Android SDK
and Android NDK are placed on your PC.

Toolchain
~~~~~~~~~

We usually try to keep the Godot Android build code up to date, but
Google changes their toolchain versions often, so if compilation
fails due to wrong toolchain version, go to your NDK directory and check
the current number, then set the following environment variable:

::

    NDK_TARGET (by default set to "arm-linux-androideabi-4.9")

Building the export templates
-----------------------------

Godot needs two export templates for Android: the optimized "release"
template (`android_release.apk`) and the debug version (`android_debug.apk`).
Compiling the standard export templates is done by calling scons with
the following arguments:

-  Release template (used when exporting with "Debugging Enabled" OFF)

::

    C:\godot> scons platform=android target=release
    C:\godot> cd platform/android/java
    C:\godot\platform\android\java> gradlew build

(on Linux or macOS, execute the `gradlew` script with `./gradlew build`)

The resulting APK is in:

::

    bin\android_release.apk

-  Debug template (used when exporting with "Debugging Enabled" ON)

::

    C:\godot> scons platform=android target=release_debug
    C:\godot> cd platform/android/java
    C:\godot\platform\android\java> gradlew build

The resulting APK is in:

::

    bin\android_debug.apk

Faster compilation
~~~~~~~~~~~~~~~~~~

If you are on Unix or installed PyWin32 on Windows and have multiple CPU
cores available, you can speed up the compilation by adding the ``-jX``
argument to the SCons command, where ``X`` is the number of cores that you
want to allocate to the compilation, e.g. ``scons -j4``.


Adding support for x86 devices
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you also want to include support for x86 devices, run the scons command
a second time with the ``android_arch=x86`` argument before building the APK
with Gradle. For example for the release template:

::

    C:\godot> scons platform=android target=release
    C:\godot> scons platform=android target=release android_arch=x86
    C:\godot> cd platform/android/java
    C:\godot\platform\android\java> gradlew build


This will create a fat binary that works in both platforms, but will add
about 6 megabytes to the APK.

Troubleshooting
~~~~~~~~~~~~~~~

It might be necessary to clean the build cache between two APK compilations,
as some users have reported issues when building the two export templates
one after the other.

Using the export templates
--------------------------

As export templates for Android, Godot needs release and debug APKs that
were compiled against the same version/commit as the editor. If you are
using official binaries for the editor, make sure to install the matching
export templates, or to build your own from the same version.

When exporting your game, Godot opens the APK, changes a few things inside and
adds your files.

Installing the templates
~~~~~~~~~~~~~~~~~~~~~~~~

The newly-compiled templates (android_debug.apk and android_release.apk)
must be copied to Godot's templates folder with their respective names.
The templates folder can be located in:

-  Windows: ``C:\Users\[username]\AppData\Roaming\Godot\templates\[version]\``
-  Linux: ``/home/[username]/.local/share/godot/templates/[version]/``
-  macOS: ``/Users/[username]/Library/Application Support/Godot/templates/[version]/``

``[version]`` is of the form ``major.minor[.patch].status`` using values from
``version.py`` in your Godot source repository (e.g. ``3.0.5.stable`` or `3.1.dev``).
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

Troubleshooting
---------------

Application not installed
~~~~~~~~~~~~~~~~~~~~~~~~~

Android might complain the application is not correctly installed. If
so, check the following:

-  Check that the debug keystore is properly generated.
-  Check that jarsigner is from JDK 6, 7 or 8.

If it still fails, open a command line and run logcat:

::

    C:\android-sdk\platform-tools> adb logcat

And check the output while the application is installed. Reason for
failure should be presented there.

Seek assistance if you can't figure it out.

Application exits immediately
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If the application runs but exits immediately, there might be one of the
following reasons:

-  Make sure to use export templates that match your editor version; if
   you use a new Godot version, you *have* to update the templates too.
-  libgodot_android.so is not in ``lib/armeabi-v7a`` or ``lib/armeabi``
-  Device does not support armv7 (try compiling yourself for armv6)
-  Device is Intel, and apk is compiled for ARM.

In any case, ``adb logcat`` should also show the cause of the error.

Compilation fails
~~~~~~~~~~~~~~~~~

On Linux systems with Kernel version 4.3 or newer, compilation may fail
with the error "pthread_create failed: Resource temporarily unavailable."

This is because of a change in the way Linux limits thread creation. But
you can change those limits through the command line. Please read this
section thoroughly before beginning.

First open a terminal, then begin compilation as usual (it may be a good
idea to run a --clean first). While compiling enter the following in
your terminal:

::

    user@host:~/$ top -b -n 1 | grep scons

The output should list a scons process, with its PID as the first number
in the output. For example the PID 1077 in the output shown below:

::

    user@host:~/$ top -b -n 1 | grep scons
    1077 user     20   0   10544   1628   1508 S 0.000 0.027   0:00.00 grep

Now you can use another command to increase the number of processes that
scons is allowed to spawn. You can check its current limits with:

::

    user@host:~/$ prlimit --pid=1077 --nproc

You can increase those limits with the command:

::

    user@host:~/$ prlimit --pid=1077 --nproc=60000:60500

Obviously you should substitute the scons PID output by top and a limits
that you think suitable. These are in the form --nproc=soft:hard where
soft must be lesser than or equal to hard. See the man page for more
information.

If all went well, and you entered the prlimit command while scons was
running, then your compilation should continue without the error.
