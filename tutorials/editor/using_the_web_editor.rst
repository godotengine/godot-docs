:article_outdated: True

.. _doc_using_the_web_editor:

Using the Web editor
====================

Since Godot 3.3, there is a `Web editor <https://editor.godotengine.org/>`__
you can use to work on new or existing projects.

.. note::

    The web editor is in a preliminary stage. While its feature set may be
    sufficient for educational purposes, it is currently **not recommended for
    production work**. See :ref:`doc_using_the_web_editor_limitations` below.

Browser support
---------------

The Web editor requires support for WebAssembly's SharedArrayBuffer. This
is in turn required to support threading in the browser. The following desktop
browsers support WebAssembly threading and can therefore run the web editor:

- Chrome 68 or later
- Firefox 79 or later
- Edge 79 or later

Opera and Safari are not supported yet. Safari may work in the future once
proper threading support is added.

**Mobile browsers are currently not supported.**

The web editor only supports the Compatibility rendering method, as there is no
stable way to run Vulkan applications on the web yet.

.. note::

    If you use Linux, due to
    `poor Firefox WebGL performance <https://bugzilla.mozilla.org/show_bug.cgi?id=1010527>`__,
    it's recommended to use a Chromium-based browser instead of Firefox.

.. _doc_using_the_web_editor_limitations:

Limitations
-----------

Due to limitations on the Godot or Web platform side, the following features
are currently missing:

- No C#/Mono support.
- No GDExtension support.
- No debugging support. This means GDScript debugging/profiling, live scene
  editing, the Remote Scene tree dock and other features that rely on the debugger
  protocol will not work.
- No project exporting. As a workaround, you can download the project source
  using **Project > Tools > Download Project Source** and export it using a
  `native version of the Godot editor <https://godotengine.org/download>`__.
- The editor won't warn you when closing the tab with unsaved changes.
- No lightmap baking support. You can still use existing lightmaps if they were
  baked with a native version of the Godot editor
  (e.g. by importing an existing project).

The following features are unlikely to be supported due to inherent limitations
of the Web platform:

- No support for external script editors.
- No support for Android one-click deploy.

.. seealso::

    See the
    `list of open issues on GitHub related to the web editor <https://github.com/godotengine/godot/issues?q=is%3Aopen+is%3Aissue+label%3Aplatform%3Ahtml5+label%3Atopic%3Aeditor>`__ for a list of known bugs.

Importing a project
-------------------

To import an existing project, the current process is as follows:

- Specify a ZIP file to preload on the HTML5 filesystem using the
  **Preload project ZIP** input.
- Run the editor by clicking **Start Godot editor**.
  The Godot Project Manager should appear after 10-20 seconds.
  On slower machines or connections, loading may take up to a minute.
- In the dialog that appears at the middle of the window, specify a name for
  the folder to create then click the **Create Folder** button
  (it doesn't have to match the ZIP archive's name).
- Click **Install & Edit** and the project will open in the editor.

.. attention::

    It's important to place the project folder somewhere in ``/home/web_user/``.
    If your project folder is placed outside ``/home/web_user/``, you will
    lose your project when closing the editor!

    When you follow the steps described above, the project folder will always be
    located in ``/home/web_user/projects``, keeping it safe.

Editing and running a project
-----------------------------

Unlike the native version of Godot, the web editor is constrained to a single
window. Therefore, it cannot open a new window when running the project.
Instead, when you run the project by clicking the Run button or pressing
:kbd:`F5`, it will appear to "replace" the editor window.

The web editor offers an alternative way to deal with the editor and game
windows (which are now "tabs"). You can switch between the **Editor** and
**Game** tabs using the buttons on the top. You can also close the running game
or editor by clicking the **×** button next to those tabs.

Where are my project files?
---------------------------

Due to browser security limitations, the editor will save the project files to
the browser's IndexedDB storage. This storage isn't accessible as a regular folder
on your machine, but is abstracted away in a database.

You can download the project files as a ZIP archive by using
**Project > Tools > Download Project Source**. This can be used to export the
project using a `native Godot editor <https://godotengine.org/download>`__,
since exporting from the web editor isn't supported yet.

In the future, it may be possible to use the
`HTML5 FileSystem API <https://developer.mozilla.org/en-US/docs/Web/API/FileSystem>`__
to store the project files on the user's filesystem as the native editor would do.
However, this isn't implemented yet.
