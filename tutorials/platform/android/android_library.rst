.. _doc_android_library:

Godot Android library
=====================

On Android platforms, the Godot Engine is designed as an `Android library <https://developer.android.com/studio/projects/android-library>`_,
enabling several key features:

- Allows Godot Android projects to leverage components, libraries, and tools from the Android, Java, and Kotlin ecosystems via :ref:`doc_android_gradle_build`

- Provides the ability to make the engine portable and embeddable:

  - Helps accelerate development and improve the capabilities of the :ref:`Godot Android Editor <doc_using_the_android_editor>`
  - Allows the integration and reuse of the engine's capabilities within existing codebases

The Godot Android library is packaged as an AAR archive file and hosted on `MavenCentral <https://central.sonatype.com/artifact/org.godotengine/godot>`_ along
with `its documentation <https://javadoc.io/doc/org.godotengine/godot/latest/index.html>`_.

It provides access to Godot APIs and capabilities for the following use-cases.

Godot Android plugins
---------------------

Android plugins are tools to extend the capabilities of the Godot Engine
by tapping into the functionality provided by Android platforms and ecosystem.

An Android plugin is an Android library with a dependency on the Godot Android library.
The Godot Android library is used by the plugin to hook into the engine's lifecycle and
access the engine's APIs, granting it capabilities used to update and customize the engine behavior as needed.

For more information, see :ref:`Godot Android plugins <doc_android_plugin>`.

Embedding Godot in existing Android projects
--------------------------------------------

The Godot Android library can be used to embed the Godot Engine within Android applications or libraries,
allowing developers to augment their projects with the full capabilities of the engine.

For more information, see :ref:`Embedding Godot in Android projects <doc_embedding_in_android_projects>`.
