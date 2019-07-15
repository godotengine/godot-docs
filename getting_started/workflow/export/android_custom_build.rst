.. _doc_android_custom_build:

Custom builds for Android
=========================

Godot provides the option to use custom build Android templates. Instead of using the already pre-built template that ships
with Godot, an actual Android Java project gets installed into your project folder. Godot will then build it and use it as
an export template every time you export the project.

There are some reasons why you may want to do this:

* Modify the project before it's built
* Add external SDKs that build with your project

Configuring custom build is a more or less straightforward process, but it may take a while to get used to how the Android SDK works.

Instructions will be provided as detailed as possible to do this process.

Set up the Custom Build environment
-----------------------------------

Go to the Project menu, and install the *Custom Build* template:

.. image:: img/custom_build_install_template.png

Make sure export templates are downloaded. If not, this menu will aid you to do it.

This will create an Gradle-based Android project in *"res://android/build"*, and place a .gdignore file in *"res://android"* so Godot filesystem ignores this folder. Editing these files is not needed unless you want to :ref:`create your own add-ons<doc_android_plugin>`, or you really need to modify the project.

Install the Android SDK (Command Line Version)
----------------------------------------------

These are the steps for installing the Android SDK using command line. The advantage of this approach is the simplicity and small download/install size. It can be a bit more challenging, though. The Android Studio approach is easier but it requires downloading and installing Android Studio (which may require more than 1gb of storage).

Install Java
^^^^^^^^^^^^^

Android SDK does not come with Java, so it needs to be installed manually. Instal Java SDK (**not** runtime or JRE). OpenSDK 8 is recommended, otherwise Oracle's Java SDK for version 8 will work. Later versions may not work for Android development.

Download the command line tools
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Go to Google's website for downloading the Android SDK. A search will take you to the *Android Studio* download page.
You don't want it, so don't download (if you do want it, read further down for instructions for doing the same using Android Studio).

Look in that page for the *Command Line Tools*. Currently, they are listed under *Download Options*. Scroll down a bit until you see them.

.. image:: img/custom_build_command_line.png

Download the zip file for your platform, inside there will be a single *tools* folder:

.. image:: img/custom_build_zip.png

This may appear a little confusing, but be sure to follow these instructions carefully:

* Create a new folder anywhere you want named *android-sdk* (it **must** be an empty directory). On Windows,

::

  C:\users\<yourusername>\Documents\android-sdk

is often good enough. Unzip the *sdk zip file* you just downloaded there. The only thing in the directory you created in the previous step should be the *tools* folder with its contents inside, like this:

::

  android-sdk/
  android-sdk/tools/
  android-sdk/tools/allthefiles


Accepting the Licenses
^^^^^^^^^^^^^^^^^^^^^^

Everything would be more or less rosy up to here, but in order to even do anything, Google requires you to accept its licenses.

To do this, the *sdkmanager* must be executed from command line with a special argument. Navigate to the *tools/bin* directory inside the sdk folder (instructions provided for Windows users, as Unix users are expected to understand how command line navigation works):

.. image:: img/custom_build_bin_folder.png

Then open a command line window:

.. image:: img/custom_build_open_shell.png

In there, manually run sdkmanager with the "--licenses" argument:

.. image:: img/custom_build_sdkmanager.png

This will ask you to accept several licenses, just write *"y"* and press *enter* on every of them until it's done.

Afterwards, install the platform tools (this is needed to install *adb*):

.. image:: img/custom_build_platform_tools.png


Generating the Keystore
^^^^^^^^^^^^^^^^^^^^^^^

Once *platform tools* are installed, the last step is to generate a debug keystore (this is needed to build). Go up two folders by
writing:

::

    cd ..\..

(or open a new shell on the *android-sdk* folder).

And you need to input the following line (on Unixes this should work out of the box, for Windows there are further instructions below):

::

    keytool -keyalg RSA -genkeypair -alias androiddebugkey -keypass android -keystore debug.keystore -storepass android -dname "CN=Android Debug,O=Android,C=US" -validity 9999

On Windows, the full path to Java should be provided (and & needs to be added at the beginning on the line if you use PowerShell, it's not needed for regular console). 

To make it clearer, here is an capture of a line that works on PowerShell (by adding & and the full Java Path to keytool.exe). Again, keep in mind that you need Java installed:

.. image:: img/custom_build_command_line.png

(right-click, then open the image in a new tab if this appears too small)


Setting up Godot
^^^^^^^^^^^^^^^^

Go to the *Editor Settings* and set up a few fields in *Export -> Android*. Make sure they look like the following:

.. image:: img/custom_build_editor_settings.png

(again, right-click, then open the image in a new tab if this appears too small)


As it can be seen, most paths are inside either *android-sdk* you originally created, or inside the Java install. For Unix users, *jarsigner* is often in "/usr/bin".

With this, you should be all set.


Install the Android SDK (Android Studio)
----------------------------------------

If you just finished installing the SDK via command line tools, feel free to skip this section entirely. The Android Studio path is easier, but it takes up more disk space. It's also useful if you plan to develop Godot for Android (modify the Java source code) or if you plan to develop Add-Ons.

Download and Install Android Studio
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Download the latest version of Android Studio. When installing, pay attention to where the *android-sdk* directory is created.

.. image:: img/custom_build_install_android_studio1.png

.. note:: This is funny, the path it proposes by default contains whitespace (and complains about it). It must be changed.

In any case, it's better to select a different path inside your user folders. The recommended one is usually:

::

  C:\Users\<yourusername>\Documents\android-sdk

Replace *yourusername* by your actual user name. Once it's correct, select from the list above in the same screen:

* Android SDK
* Android SDK Platform

The rest are not needed, because the build system will fetch them itself. After selecting them, go on with the installation.


Generating the Keystore
^^^^^^^^^^^^^^^^^^^^^^^

You thought that by going the Android Studio way you could escape the Keystore generation, but no. It's back to haunt you.

Go to the folder where you installed android-sdk in the previous step, use File Explorer and open a command line tool there:

.. image:: img/custom_build_open_shell.png

The actual command line to type is the following. On Unixes it should work out of the box, but on Windows it needs additional details (keep reading afterwards).

::

    keytool -keyalg RSA -genkeypair -alias androiddebugkey -keypass android -keystore debug.keystore -storepass android -dname "CN=Android Debug,O=Android,C=US" -validity 9999

On Windows, the full path to Java should be provided (and & needs to be added at the beginning on the line if you use PowerShell, it's not needed for regular commandline). Don't worry, at least by using Android Studio on Windows, Java comes bundled with it.

To make it clearer, here is a screen capture of a line that works on PowerShell (by adding & and the full Java Path to keytool.exe, remove & if you use regular console). It uses a path to the Java version that comes with Android Studio:

.. image:: img/custom_build_command_line2.png

(right-click, then open the image in a new tab if this appears too small)


Setting up Godot
^^^^^^^^^^^^^^^^

Go to the *Editor Settings* and set up a few fields in *Export -> Android*. Make sure they look like the following:

.. image:: img/custom_build_editor_settings2.png

(again, right-click, then open the image in a new tab if this appears too small)


As it can be seen, most paths are inside either *android-sdk* you originally created, or inside the Java install. For Unix users, *jarsigner* is often in "/usr/bin".

With this, you should be all set.


Enabling Custom Build and Exporting
-----------------------------------

When setting up the Android project in the *Project -> Export* dialog, *custom build* needs to be enabled:

.. image:: img/custom_build_enable.png

From now on, attempting to export the project or one-click deploy will call the *Gradle* build system to generate fresh templates (this window will appear every time):

.. image:: img/custom_build_gradle.png

The templates built will be used automatically afterwards, so no further 
configuration is needed.
