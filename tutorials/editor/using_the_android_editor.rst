.. _doc_using_the_android_editor:

Using the Android editor
========================

In 2023, `we added <https://godotengine.org/article/android_godot_editor_play_store_beta_release/>`__
a `Android port of the editor <https://godotengine.org/download/android/>`__
that can be used to work on new or existing projects on Android devices.

.. note::

    The Android editor is in beta testing stage, while we continue to refine the experience,
    and bring it up to parity with the Desktop version of the editor. See :ref:`doc_using_the_android_editor_limitations` below.

Android devices support
-----------------------

The Android editor requires devices running Android 5 Lollipop or higher, with at least OpenGL 3 support. This includes (not exhaustive):

- Android tablets, foldables and large phones
- Android-powered netbooks
- Chromebooks supporting Android apps

.. _doc_using_the_android_editor_limitations:

Required Permissions
--------------------

The Android editor requires the `All files access permission <https://developer.android.com/training/data-storage/manage-all-files#all-files-access>`__.
The permission allows the editor to create / import / read project files from any file locations on the device.
Without the permission, the editor is still functional, but has limited access to the device's files and directories.

Limitations & known issues
--------------------------

Here are the known limitations and issues of the Android editor:

- No C#/Mono support
- No support for external script editors
- While available, the *Vulkan Forward+* renderer is not recommended due to severe performance issues
- No support for building and exporting an Android APK binary.
  As a workaround, you can generate and export a `Godot PCK or ZIP file <https://docs.godotengine.org/en/stable/tutorials/export/exporting_projects.html#pck-versus-zip-pack-file-formats>`__
- No support for building and exporting binaries for other platforms
- Performance and stability issues when using the *Vulkan Mobile* renderer for a project
- UX not optimized for Android phones form-factor
- `Android Go devices <https://developer.android.com/guide/topics/androidgo>`__ lacks
  the *All files access* permission required for device read/write access.
  As a workaround, when using a Android Go device, it's recommended to create new projects only in the Android *Documents* or *Downloads* directories.
- The editor doesn't properly resume when *Don't keep activities* is enabled in the *Developer Options*

.. seealso::

    See the
    `list of open issues on GitHub related to the Android editor <https://github.com/godotengine/godot/issues?q=is%3Aopen+is%3Aissue+label%3Aplatform%3Aandroid+label%3Atopic%3Aeditor>`__ for a list of known bugs.
