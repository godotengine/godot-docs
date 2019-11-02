.. _doc_exporting_for_android:

Exporting for Android
=====================

Exporting for Android has fewer requirements than compiling Godot for it. The
following steps detail what is needed to setup the SDK and the engine.

Download the Android SDK
------------------------

Download and install the Android SDK from
https://developer.android.com/studio/

Install OpenJDK or Oracle JDK
-----------------------------

Download and install  `OpenJDK <https://github.com/ojdkbuild/ojdkbuild>`__ or `Oracle JDK <http://www.oracle.com/technetwork/java/javase/downloads/index.html>`__. Versions below JDK 8 may not work; some users have reported issues with the jarsigner (used to sign the APKs) in JDK 7.

Create a debug.keystore
-----------------------

Android needs a debug keystore file to install to devices and distribute
non-release APKs. If you have used the SDK before and have built
projects, ant or eclipse probably generated one for you (on Linux and
macOS, you can find it in the ``~/.android`` directory).

If you can't find it or need to generate one, the keytool command from
the JDK can be used for this purpose:

::

    keytool -keyalg RSA -genkeypair -alias androiddebugkey -keypass android -keystore debug.keystore -storepass android -dname "CN=Android Debug,O=Android,C=US" -validity 9999

Make sure you have adb
----------------------

Android Debug Bridge (adb) is the command line tool used to communicate with
Android devices. It's installed with the SDK, but you may need to install one
(any) of the Android API levels for it to be installed in the SDK directory.

Setting it up in Godot
----------------------

Enter the Editor Settings screen. This screen contains the editor
settings for the user account in the computer (it's independent from the
project).

.. image:: img/editorsettings.png

Scroll down to the section where the Android settings are located:

.. image:: img/androidsdk.png

In that screen, the path to 3 files needs to be set:

-  The *adb* executable (adb.exe on Windows)
-  The *jarsigner* executable (from JDK 6 or 8)
-  The debug *keystore*

Once that is configured, everything is ready to export to Android!

Exporting for Google Play Store
-------------------------------

Uploading an APK to Google's Play Store requires you to sign using a non-debug
keystore file; such file can be generated like this:

::

    keytool -v -genkey -v -keystore mygame.keystore -alias mygame -keyalg RSA -validity 10000

This keystore and key are used to verify your developer identity, remember the password and keep it in a safe place!
Use Google's Android Developer guides to learn more about `APK signing <https://developer.android.com/studio/publish/app-signing>`__.

Now fill in the following forms in your Android Export Presets:

.. image:: img/editor-export-presets-android.png

- **Release:** Enter the path to the keystore file you just generated.
- **Release User:** Replace with the key alias.
- **Release Password:** Key password. Note that the keystore password and the key password currently have to be the same.

**Your export_presets.cfg file now contains sensitive information.** If you use
a version control system, you should remove it from public repositories and add
it to your ``.gitignore`` file or equivalent.

Don't forget to uncheck the **Export With Debug** checkbox while choosing the APK's name.

.. image:: img/export-with-debug-button.png

Optimizing the APK size
-----------------------

By default, the APK will contain native libraries for both ARMv7 and ARMv8
architectures. This increases its size significantly. To create a smaller APK,
uncheck either **Armeabi-v 7a** or **Arm 64 -v 8a** in your project's Android
export preset. This will create an APK that only contains a library for
a single architecture. Note that applications targeting ARMv7 can also run on
ARMv8 devices, but the opposite is not true.

Since August 2019, Google Play requires all applications to be available in
64-bit form. This means you cannot upload an APK that contains *just* an ARMv7
library. To solve this, you can upload several APKs to Google Play using its
`Multiple APK support <https://developer.android.com/google/play/publishing/multiple-apks>`__.
Each APK should target a single architecture; creating an APK for ARMv7
and ARMv8 is usually sufficient to cover most devices in use today.

You can optimize the size further by compiling an Android export template with
only the features you need. See :ref:`doc_optimizing_for_size` for more
information.
