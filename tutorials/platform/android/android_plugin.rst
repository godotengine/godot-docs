.. _doc_android_plugin:

Godot Android plugins
=====================

Introduction
------------

Android plugins are powerful tools to extend the capabilities of the Godot engine
by tapping into the functionality provided by Android platforms and ecosystem.

For example in Godot 4, Android plugins are used to support multiple Android-based
XR platforms without encumbering the core codebase with vendor specific code or binaries.

Android plugin
--------------

**Version 1 (v1)** of the Android plugin system was introduced in Godot 3 and compatible with Godot 4.0 and 4.1.
That version allowed developers to augment the Godot engine with Java, Kotlin and native functionality.

Starting in Godot 4.2, Android plugins built on the v1 architecture are now deprecated.
Instead, Godot 4.2 introduces a new **Version 2 (v2)** architecture for Android plugins.

v2 Architecture
~~~~~~~~~~~~~~~

.. note::

    Godot Android plugin leverages the :ref:`Gradle build system <doc_android_gradle_build>`.


Building on the previous v1 architecture, Android plugins continue to be derived from the
`Android archive library <https://developer.android.com/studio/projects/android-library#aar-contents>`_.

At its core, a Godot Android plugin v2 is an Android library with a dependency on the :ref:`Godot Android library <doc_android_library>`,
and a custom Android library manifest.

This architecture allows Android plugins to extend the functionality of the engine with:

- Android platform APIs
- Android libraries
- Kotlin and Java libraries
- Native libraries (via JNI)
- GDExtension libraries

Each plugin has an init class extending from the `GodotPlugin <https://github.com/godotengine/godot/blob/0a7f75ec7b465604b6496c8f5f1d638aed250d6d/platform/android/java/lib/src/org/godotengine/godot/plugin/GodotPlugin.java#L80>`_ class
which is provided by the :ref:`Godot Android library <doc_android_library>`.

The ``GodotPlugin`` class provides APIs to access the running Godot instance and hook into its lifecycle. It is loaded at runtime by the Godot engine.

v2 Packaging format
~~~~~~~~~~~~~~~~~~~

v1 Android plugins required a custom ``gdap`` configuration file that was used by the Godot Editor to detect and load them.
However this approach had several drawbacks, primary ones being that it lacked flexibility and departed from the `existing
Godot EditorExportPlugin format, delivery and installation flow <https://docs.godotengine.org/en/stable/tutorials/plugins/editor/installing_plugins.html>`_.

This has been resolved for v2 Android plugins by deprecating the ``gdap`` packaging and configuration mechanism in favor of
the existing Godot ``EditorExportPlugin`` packaging format.
The ``EditorExportPlugin`` API in turn has been extended to properly support Android plugins.


Building a v2 Android plugin
----------------------------

A github project template **is provided** at https://github.com/m4gr3d/Godot-Android-Plugin-Template as a **quickstart for building
Godot Android plugins for Godot 4.2+**.
You can follow the `template README <https://github.com/m4gr3d/Godot-Android-Plugin-Template#readme>`_
to set up your own Godot Android plugin project.

To provide further understanding, here is a break-down of the steps used to create the project template:

1. Create an Android library module using `these instructions <https://developer.android.com/studio/projects/android-library>`_

2. Add the Godot Android library as a dependency by updating the module's ``gradle`` `build file <https://github.com/m4gr3d/Godot-Android-Plugin-Template/blob/main/plugin/build.gradle.kts#L42>`_:

    .. code:: text

        dependencies {
            implementation("org.godotengine:godot:4.2.0.stable")
        }

  The Godot Android library is `hosted on MavenCentral <https://central.sonatype.com/artifact/org.godotengine/godot>`_, and updated for each release.

3. Create `GodotAndroidPlugin <https://github.com/m4gr3d/Godot-Android-Plugin-Template/blob/a01286b4cb459133bf07b11dfabdfd3980268797/plugin/src/main/java/org/godotengine/plugin/android/template/GodotAndroidPlugin.kt#L10>`_, an init class for the plugin extending `GodotPlugin <https://github.com/godotengine/godot/blob/0a7f75ec7b465604b6496c8f5f1d638aed250d6d/platform/android/java/lib/src/org/godotengine/godot/plugin/GodotPlugin.java#L80>`_.

    - If the plugin exposes Kotlin or Java methods to be called from GDScript, they must be annotated with `@UsedByGodot <https://github.com/godotengine/godot/blob/0a7f75ec7b465604b6496c8f5f1d638aed250d6d/platform/android/java/lib/src/org/godotengine/godot/plugin/UsedByGodot.java#L45>`_. The name called from GDScript **must match the method name exactly**. There is **no** coercing ``snake_case`` to ``camelCase``. For example, from GDScript:

        ::

            if Engine.has_singleton("MyPlugin"):
                var singleton = Engine.get_singleton("MyPlugin")
                print(singleton.myPluginFunction("World"))

    - If the plugin uses `signals <https://docs.godotengine.org/en/stable/getting_started/step_by_step/signals.html>`_, the init class must return the set of signals used by overriding `GodotPlugin::getPluginSignals() <https://github.com/godotengine/godot/blob/fa3428ff25bc577d2a3433090478a6d615567056/platform/android/java/lib/src/org/godotengine/godot/plugin/GodotPlugin.java#L302>`_. To emit signals, the plugin can use the `GodotPlugin::emitSignal(...) method <https://github.com/godotengine/godot/blob/0a7f75ec7b465604b6496c8f5f1d638aed250d6d/platform/android/java/lib/src/org/godotengine/godot/plugin/GodotPlugin.java#L317>`_.

4. Update the plugin ``AndroidManifest.xml`` `file <https://github.com/m4gr3d/Godot-Android-Plugin-Template/blob/main/plugin/src/main/AndroidManifest.xml>`_ with the following meta-data:

    .. code-block:: xml

        <meta-data
            android:name="org.godotengine.plugin.v2.[PluginName]"
            android:value="[plugin.init.ClassFullName]" />


  Where:

      - ``PluginName`` is the name of the plugin
      - ``plugin.init.ClassFullName`` is the full component name (package + class name) of the plugin init class (e.g: ``org.godotengine.plugin.android.template.GodotAndroidPlugin``).

5. Create the `EditorExportPlugin configuration <https://github.com/m4gr3d/Godot-Android-Plugin-Template/tree/main/plugin/export_scripts_template>`_ to package the plugin. The steps used to create the configuration can be seen in the `Packaging a v2 Android plugin`_ section.


Building a v2 Android plugin with GDExtension capabilities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Similar to GDNative support in v1 Android plugins, v2 Android plugins support the ability to integrate GDExtension capabilities.

A github project template is provided at https://github.com/m4gr3d/GDExtension-Android-Plugin-Template as a quickstart for building
GDExtension Android plugins for Godot 4.2+.
You can follow the `template's README <https://github.com/m4gr3d/GDExtension-Android-Plugin-Template#readme>`_
to set up your own Godot Android plugin project.


Migrating a v1 Android plugin to v2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the following steps if you have a v1 Android plugin you want to migrate to v2:

1. Update the plugin's manifest file:

    - Change the ``org.godotengine.plugin.v1`` prefix to ``org.godotengine.plugin.v2``

2. Update the Godot Android library build dependency:

    - You can continue using the ``godot-lib.<version>.<status>.aar`` binary from `Godot's download page <https://godotengine.org/download>`_ if that's your preference. Make sure it's updated to the latest stable version.
    - Or you can switch to the MavenCentral provided dependency:

::

    dependencies {
        implementation("org.godotengine:godot:4.2.0.stable")
    }

3. After updating the Godot Android library dependency, sync or build the plugin and resolve any compile errors:

    - The ``Godot`` instance provided by ``GodotPlugin::getGodot()`` no longer has access to an ``android.content.Context`` reference. Use ``GodotPlugin::getActivity()`` instead.

4. Delete the ``gdap`` configuration file(s) and follow the instructions in the `Packaging a v2 Android plugin`_ section to set up the plugin configuration.

Packaging a v2 Android plugin
-----------------------------

As mentioned, a v2 Android plugin is now provided to the Godot Editor as an ``EditorExportPlugin`` plugin, so it shares a lot of the `same packaging steps <https://docs.godotengine.org/en/stable/tutorials/plugins/editor/making_plugins.html#creating-a-plugin>`_.

1. Add the plugin output binaries within the plugin directory (e.g: in ``addons/<plugin_name>/``)

2. Add the `tool script <https://docs.godotengine.org/en/stable/tutorials/plugins/editor/making_plugins.html#the-script-file>`_ for the export functionality within the plugin directory (e.g: in ``addons/<plugin_name>/``)

    - The created script must be a ``@tool`` script, or else it will not work properly
    - The export tool script is used to configure the Android plugin and hook it within the Godot Editor's export process. It should look something like this:

::

    @tool
    extends EditorPlugin

    # A class member to hold the editor export plugin during its lifecycle.
    var export_plugin : AndroidExportPlugin

    func _enter_tree():
        # Initialization of the plugin goes here.
        export_plugin = AndroidExportPlugin.new()
        add_export_plugin(export_plugin)


    func _exit_tree():
        # Clean-up of the plugin goes here.
        remove_export_plugin(export_plugin)
        export_plugin = null


    class AndroidExportPlugin extends EditorExportPlugin:
        # Plugin's name.
        var _plugin_name = "<plugin_name>"

        # Specifies which platform is supported by the plugin.
        func _supports_platform(platform):
            if platform is EditorExportPlatformAndroid:
                return true
            return false

        # Return the paths of the plugin's AAR binaries relative to the 'addons' directory.
        func _get_android_libraries(platform, debug):
            if debug:
                return PackedStringArray(["<paths_to_debug_android_plugin_aar_binaries>"])
            else:
                return PackedStringArray(["<paths_to_release_android_plugin_aar_binaries>"])

        # Return the plugin's name.
        func _get_name():
            return _plugin_name


    - Here are the set of `EditorExportPlugin APIs <https://docs.godotengine.org/en/stable/classes/class_editorexportplugin.html>`_ most relevant to use in this tool script:

        - `_supports_platform <https://docs.godotengine.org/en/latest/classes/class_editorexportplugin.html#class-editorexportplugin-method-supports-platform>`_: returns ``true`` if the plugin supports the given platform. For Android plugins, this must return ``true`` when ``platform`` is `EditorExportPlatformAndroid <https://docs.godotengine.org/en/stable/classes/class_editorexportplatformandroid.html>`_
        - `_get_android_libraries <https://docs.godotengine.org/en/latest/classes/class_editorexportplugin.html#class-editorexportplugin-method-get-android-libraries>`_: retrieve the local paths of the Android libraries binaries (AAR files) provided by the plugin
        - `_get_android_dependencies <https://docs.godotengine.org/en/latest/classes/class_editorexportplugin.html#class-editorexportplugin-method-get-android-dependencies>`_: retrieve the set of Android maven dependencies (e.g: `org.godot.example:my-plugin:0.0.0`) provided by the plugin
        - `_get_android_dependencies_maven_repos <https://docs.godotengine.org/en/latest/classes/class_editorexportplugin.html#class-editorexportplugin-method-get-android-dependencies-maven-repos>`_: retrieve the urls of the maven repos for the android dependencies provided by ``_get_android_dependencies``
        - `_get_android_manifest_activity_element_contents <https://docs.godotengine.org/en/latest/classes/class_editorexportplugin.html#class-editorexportplugin-method-get-android-manifest-activity-element-contents>`_: update the contents of the `<activity>` element in the generated Android manifest
        - `_get_android_manifest_application_element_contents <https://docs.godotengine.org/en/latest/classes/class_editorexportplugin.html#class-editorexportplugin-method-get-android-manifest-application-element-contents>`_: update the contents of the `<application>` element in the generated Android manifest
        - `_get_android_manifest_element_contents <https://docs.godotengine.org/en/latest/classes/class_editorexportplugin.html#class-editorexportplugin-method-get-android-manifest-element-contents>`_: update the contents of the `<manifest>` element in the generated Android manifest

        The ``_get_android_manifest_*`` methods allow the plugin to automatically provide changes
        to the app's manifest which are preserved when the Godot Editor is updated, resolving a long standing issue with v1 Android plugins.


3. Create a ``plugin.cfg``. This is an INI file with metadata about your plugin:

::

      [plugin]

      name="<plugin_name>"
      description="<plugin_description>"
      author="<plugin_author>"
      version="<plugin_version>"
      script="<relative_path_to_the_export_tool_script>"

For reference, here is the `folder structure for the Godot Android plugin project template <https://github.com/m4gr3d/Godot-Android-Plugin-Template/tree/main/plugin/export_scripts_template>`_.
At build time, the contents of the ``export_scripts_template`` directory as well as the generated plugin binaries are copied to the ``addons/<plugin_name>`` directory:

.. code-block:: none

    export_scripts_template/
    |
    +--export_plugin.gd         # export plugin tool script
    |
    +--plugin.cfg               # plugin INI file


Packaging a v2 Android plugin with GDExtension capabilities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For GDExtension, we follow the same steps as for `Packaging a v2 Android plugin`_ and add the `GDExtension config file <https://docs.godotengine.org/en/stable/tutorials/scripting/cpp/gdextension_cpp_example.html#using-the-gdextension-module>`_ in
the same location as ``plugin.cfg``.

For reference, here is the `folder structure for the GDExtension Android plugin project template <https://github.com/m4gr3d/GDExtension-Android-Plugin-Template/tree/main/plugin/export_scripts_template>`_.
At build time, the contents of the ``export_scripts_template`` directory as well as the generated plugin binaries are copied to the ``addons/<plugin_name>`` directory:

.. code-block:: none

    export_scripts_template/
    |
    +--export_plugin.gd         # export plugin tool script
    |
    +--plugin.cfg               # plugin INI file
    |
    +--plugin.gdextension       # GDExtension config file


Here is what the ``plugin.gdextension`` config file should look like:

::

    [configuration]

    entry_symbol = "plugin_library_init"
    compatibility_minimum = "4.2"
    android_aar_plugin = true

    [libraries]

    android.debug.arm64 = "res://addons/GDExtensionAndroidPluginTemplate/bin/debug/arm64-v8a/libGDExtensionAndroidPluginTemplate.so"
    android.release.arm64 = "res://addons/GDExtensionAndroidPluginTemplate/bin/release/arm64-v8a/libGDExtensionAndroidPluginTemplate.so"
    ...


Of note is the ``android_aar_plugin`` field that specifies this GDExtension module is provided as part of a v2 Android plugin.
During the export process, this will indicate to the Godot Editor that the GDExtension native shared libraries are exported by the Android plugin AAR binaries.

For GDExtension Android plugins, the plugin init class must override `GodotPlugin::getPluginGDExtensionLibrariesPaths() <https://github.com/godotengine/godot/blob/0a7f75ec7b465604b6496c8f5f1d638aed250d6d/platform/android/java/lib/src/org/godotengine/godot/plugin/GodotPlugin.java#L277>`_,
and return the paths to the bundled GDExtension libraries config files (``*.gdextension``).

The paths must be relative to the Android library's ``assets`` directory.
At runtime, the plugin will provide these paths to the Godot engine which will use them to load and initialize the bundled GDExtension libraries.

Using a v2 Android plugin
-------------------------

.. note::

    - Godot 4.2 or higher is required

    - v2 Android plugin requires the use of the `Gradle build process <https://docs.godotengine.org/en/stable/classes/class_editorexportplatformandroid.html#class-editorexportplatformandroid-property-gradle-build-use-gradle-build>`_.

    - The provided github project templates include demo Godot projects for quick testing.


1. Copy the plugin's output directory (``addons/<plugin_name>``) to the target Godot project's directory

2. Open the project in the Godot Editor; the Editor should detect the plugin

3. Navigate to ``Project`` -> ``Project Settings...`` -> ``Plugins``, and ensure the plugin is enabled

4. Install the Godot Android build template by clicking on ``Project`` -> ``Install Android Build Template...``

5. Navigate to ``Project`` -> ``Export...``

6. In the ``Export`` window, create an ``Android export preset``

7. In the ``Android export preset``, scroll to ``Gradle Build`` and set ``Use Gradle Build`` to ``true``

8. Update the project's scripts as needed to access the plugin's functionality. For example:

::

    if Engine.has_singleton("MyPlugin"):
            var singleton = Engine.get_singleton("MyPlugin")
            print(singleton.myPluginFunction("World"))

9. Connect an Android device to your machine and run the project on it


Using a v2 Android plugin as an Android library
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Since they are also Android libraries, Godot v2 Android plugins can be stripped from their ``EditorExportPlugin`` packaging and provided as raw ``AAR`` binaries for use as libraries alongside the :ref:`Godot Android library <doc_android_library>` by Android apps.

If targeting this use-case, make sure to include additional instructions for how the ``AAR`` binaries should be included (e.g: custom additions to the Android app's manifest).

Reference implementations
-------------------------

- `Godot Android Plugins Samples <https://github.com/m4gr3d/Godot-Android-Samples/tree/master/plugins>`_
- `Godot Android Plugin Template <https://github.com/m4gr3d/Godot-Android-Plugin-Template>`_
- `GDExtension Android Plugin Template <https://github.com/m4gr3d/GDExtension-Android-Plugin-Template>`_
- `Godot OpenXR Loaders <https://github.com/GodotVR/godot_openxr_loaders>`_


Tips and Guidelines
-------------------

Simplify access to the exposed Java / Kotlin APIs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To make it easier to access the exposed Java / Kotlin APIs in the Godot Editor, it's recommended to
provide one (or multiple) gdscript wrapper class(es) for your plugin users to interface with.

For example:

::

    class_name PluginInterface extends Object

    ## Interface used to access the functionality provided by this plugin.

    var _plugin_name = "GDExtensionAndroidPluginTemplate"
    var _plugin_singleton

    func _init():
        if Engine.has_singleton(_plugin_name):
            _plugin_singleton = Engine.get_singleton(_plugin_name)
        else:
            printerr("Initialization error: unable to access the java logic")

    ## Print a 'Hello World' message to the logcat.
    func helloWorld():
        if _plugin_singleton:
            _plugin_singleton.helloWorld()
        else:
            printerr("Initialization error")

Support using the GDExtension functionality in the Godot Editor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If planning to use the GDExtension functionality in the Godot Editor, it is recommended that the
GDExtension's native binaries are compiled not just for Android, but also for the OS onto which
developers / users intend to run the Godot Editor. Not doing so may prevent developers /
users from writing code that accesses the plugin from within the Godot Editor.

This may involve creating dummy plugins for the host OS just so the API is published to the
editor. You can use the `godot-cpp-template <https://github.com/godotengine/godot-cpp-template>`__
github template for reference on how to do so.

Godot crashes upon load
~~~~~~~~~~~~~~~~~~~~~~~

.. UPDATE: Not supported yet. When more complex datatypes are supported,
.. update this section.

Check ``adb logcat`` for possible problems, then:

- Check that the methods exposed by the plugin used the following Java types: ``void``, ``boolean``, ``int``, ``float``, ``java.lang.String``, ``org.godotengine.godot.Dictionary``, ``int[]``, ``byte[]``, ``float[]``, ``java.lang.String[]``.
- More complex datatypes are not supported for now.
