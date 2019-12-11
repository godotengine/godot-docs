.. _doc_android_plugin:

Creating Android plugins v2 (Godot 4.0+)
=========================================

Introduction
------------

Android plugins are powerful tools to extend the capabilities of the Godot engine 
by tapping into the functionality provided by the Android platform and ecosystem. 

Mobile gaming monetization is one such example since it requires features 
and capabilities that don't belong to the core feature set of a game engine:

-  Analytics
-  In-app purchases
-  Receipt validation
-  Install tracking
-  Ads
-  Video ads
-  Cross-promotion
-  In-game soft & hard currencies
-  Promo codes
-  A/B testing
-  Login
-  Cloud saves
-  Leaderboards and scores
-  User support & feedback
-  Posting to Facebook, Twitter, etc.
-  Push notifications

Making modifications to the Android export template is another use-case since using a plugin for that task allows the project
to remain compatible with newer Godot versions.

Android plugin v2
-----------------

**Version 2** of the Android plugin is supported starting with Godot 4.0. This is a breaking, backward-incompatible update 
which deprecates **version 1** of the Android plugin in Godot 4.0.

As a prerequisite, make sure you understand how to set up a :ref:`custom build environment<doc_android_custom_build>` for Android.

At its core, a *v2* Godot Android plugin is a `Android archive library <https://developer.android.com/studio/projects/android-library#aar-contents>`_ (*aar* archive file) 
with the following caveats:

-  The library must have a dependency on the Godot engine library (``godot-lib.x.y.aar``). A stable version is made available for each Godot release.

-  The library must include a specifically configured ``<meta-data>`` tag in its manifest file.

Building a v2 Android plugin
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Prerequisite:** `Android Studio <https://developer.android.com/studio>`_ is strongly recommended as the IDE to use to create *v2* Android plugins. 
The instructions below assumes that you're using Android Studio.

1.  Follow `these instructions <https://developer.android.com/studio/projects/android-library>`_ to create an Android library module for your plugin.

2.  Add the Godot engine library as a dependency to your plugin module:

    -  Download the Godot engine library (godot-lib.x.y.aar)

    -   Follow `these instructions <https://developer.android.com/studio/projects/android-library#AddDependency>`_ to add 
        the Godot engine library as a dependency for your plugin.

    -  In the plugin module's ``build.gradle`` file, replace ``implementation`` with ``compileOnly`` for the dependency line for the Godot engine library.

3.  Create a new class in the plugin module and make sure it extends ``org.godotengine.godot.plugin.GodotPlugin``.
    At runtime, it will be used to instantiate a singleton object that will be used by the Godot engine to load, initialize and run the plugin.

4.  Update the plugin ``AndroidManifest.xml`` file:

    -   Open the plugin ``AndroidManifest.xml`` file.

    -   Add the ``<application></application>`` tag if it's missing.

    -   In the ``<application>`` tag, add a ``<meta-data>`` tag setup as follow::
        
            <meta-data 
                android:name="org.godotengine.plugin.v2.[PluginName]" 
                android:value="[plugin.init.ClassFullName]" />

        Where ``PluginName`` is the name of the plugin, and ``plugin.init.ClassFullName`` is the full name (package + class name) of the plugin loading class.

5.  Add the remaining logic for your plugin and run the ``gradle :build`` command to generate the plugin's ``aar`` file.

**Note:** The plugin's ``aar`` filename must match the following pattern: ``[PluginName]*.aar`` 
where ``PluginName`` is the name of the plugin in camel case (e.g: ``GodotPaymentV3.release.aar``).

Loading and using a v2 Android plugin
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once you have access to the plugin ``aar`` file, move it to the Godot project ``res://android/build/libs/plugins`` 
directory.

From your script:

.. code::

    if Engine.has_singleton("MyPlugin"):
        var singleton = Engine.get_singleton("MyPlugin")
        print(singleton.myPluginFunction("World"))

**When exporting the project**, you need to add the plugin's name to the ``Custom Template`` -> ``V2 Plugins`` section.
If trying to add multiple plugins, separate their names by a comma (``,``).

Bundling gdnative resources
^^^^^^^^^^^^^^^^^^^^^^^^^^^
A v2 Android plugin can define and provide C/C++ gdnative resources, either to provide and/or access functionality from the game logic.
The gdnative resources can be bundled within the plugin ``aar`` file which simplifies the distribution and deployment process:

    -   The shared libraries (``.so``) for the defined gdnative libraries will be automatically bundled by the ``aar`` build system. 

    -   Godot ``*.gdnlib`` and ``*.gdns`` resource files must be manually defined in the plugin ``assets`` directory. 
        The recommended path for these resources relative to the ``assets`` directory should be: ``godot/plugin/v2/[PluginName]/``.

For gdnative libraries, the plugin singleton object must override the ``org.godotengine.godot.plugin.GodotPlugin::getPluginGDNativeLibrariesPaths()`` method, 
and return the paths to the bundled gdnative libraries config files (``*.gdnlib``). The paths must be relative to the ``assets`` directory.
At runtime, the plugin will provide these paths to Godot core which will use them to load and initialize the bundled gdnative libraries.

Reference implementations
^^^^^^^^^^^^^^^^^^^^^^^^^
-   `Godot Oculus Mobile plugin <https://github.com/m4gr3d/godot_oculus_mobile/tree/2.0>`_

    -   `Bundled gdnative resources <https://github.com/m4gr3d/godot_oculus_mobile/tree/2.0/plugin/src/main/assets/addons/godot_ovrmobile>`_

-   `Godot Payment V3 plugin <https://github.com/m4gr3d/godot/tree/rearch_godot_android_plugin/platform/android/java/plugins/godotpaymentv3>`_


Troubleshooting
---------------

Godot crashes upon load
^^^^^^^^^^^^^^^^^^^^^^^

Check ``adb logcat`` for possible problems, then:

-  Check that the methods used in the Java singleton only use simple
   Java datatypes, more complex ones are not supported.
