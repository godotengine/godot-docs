.. _doc_custom_platform_ports:

Custom platform ports
=====================

Similar to :ref:`doc_custom_modules_in_cpp`, Godot's multi-platform architecture
is designed in a way that allows creating platform ports without modifying any
existing source code.

An example of a custom platform port distributed independently from the engine
is `FRT <https://github.com/efornara/frt>`__, which targets single-board
computers. Note that this platform port currently targets Godot 3.x; therefore,
it does not use the :ref:`class_DisplayServer` abstraction that is new in Godot 4.

Some reasons to create custom platform ports might be:

- You want to :ref:`port your game to consoles <doc_consoles>`, but wish to
  write the platform layer yourself. This is a long and arduous process, as it
  requires signing NDAs with console manufacturers, but it allows you to have
  full control over the console porting process.
- You want to port Godot to an exotic platform that isn't currently supported.

If you have questions about creating a custom platform port, feel free to ask in
the ``#platforms`` channel of the
`Godot Contributors Chat <https://chat.godotengine.org/channel/platforms>`__.

.. note::

    Godot is a modern engine with modern requirements. Even if you only
    intend to run simple 2D projects on the target platform, it still requires
    an amount of memory that makes it unviable to run on most retro consoles.
    For reference, in Godot 4, an empty project with nothing visible requires
    about 100 MB of RAM to run on Linux (50 MB in headless mode).

    If you want to run Godot on heavily memory-constrained platforms, older
    Godot versions have lower memory requirements. The porting process is
    similar, with the exception of :ref:`class_DisplayServer` not being split
    from the :ref:`class_OS` singleton.

Official platform ports
-----------------------

The official platform ports can be used as a reference when creating a custom platform port:

- `Windows <https://github.com/godotengine/godot/tree/master/platform/windows>`__
- `macOS <https://github.com/godotengine/godot/tree/master/platform/macos>`__
- `Linux/\*BSD <https://github.com/godotengine/godot/tree/master/platform/linuxbsd>`__
- `Android <https://github.com/godotengine/godot/tree/master/platform/android>`__
- `iOS <https://github.com/godotengine/godot/tree/master/platform/ios>`__
- `Web <https://github.com/godotengine/godot/tree/master/platform/web>`__

While platform code is usually self-contained, there are exceptions to this
rule. For instance, audio drivers that are shared across several platforms and
rendering backends are located in the
`drivers/ folder <https://github.com/godotengine/godot/tree/master/drivers>`__
of the Godot source code.

Creating a custom platform port
-------------------------------

Creating a custom platform port is a large undertaking which requires prior
knowledge of the platform's SDKs. Depending on what features you need, the
amount of work needed varies:

Required features of a platform port
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

At the very least, a platform port must have methods from the :ref:`class_OS`
singleton implemented to be buildable and usable for headless operation.
A ``logo.svg`` (32×32) vector image must also be present within the platform
folder. This logo is displayed in the Export dialog for each export preset
targeting the platform in question.

See `this implementation <https://github.com/godotengine/godot/blob/master/platform/linuxbsd/os_linuxbsd.cpp>`__
for the Linux/\*BSD platform as an example. See also the
`OS singleton header <https://github.com/godotengine/godot/blob/master/core/os/os.h>`__
for reference.

.. note::

    If your target platform is UNIX-like, consider inheriting from the ``OS_Unix``
    class to get much of the work done automatically.

    If the platform is not UNIX-like, you might use the
    `Windows port <https://github.com/godotengine/godot/blob/master/platform/windows/os_windows.cpp>`
    as a reference.

**detect.py file**

A ``detect.py`` file must be created within the platform's folder with all
methods implemented. This file is required for SCons to detect the platform as a
valid option for compiling. See the
`detect.py file <https://github.com/godotengine/godot/blob/master/platform/linuxbsd/detect.py>`__
for the Linux/\*BSD platform as an example.

All methods should be implemented within ``detect.py`` as follows:

- ``is_active()``: Can be used to temporarily disable building for a platform.
  This should generally always return ``True``.
- ``get_name()``: Returns the platform's user-visible name as a string.
- ``can_build()``: Return ``True`` if the host system is able to build for the
  target platform, ``False`` otherwise. Do not put slow checks here, as this is
  queried when the list of platforms is requested by the user. Use
  ``configure()`` for extensive dependency checks instead.
- ``get_opts()``: Returns the list of SCons build options that can be defined by
  the user for this platform.
- ``get_flags()``: Returns the list of overridden SCons flags for this platform.
- ``configure()``: Perform build configuration, such as selecting compiler
  options depending on SCons options chosen.

Optional features of a platform port
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In practice, headless operation doesn't suffice if you want to see anything on
screen and handle input devices. You may also want audio output for most
games.

*Some links on this list point to the Linux/\*BSD platform implementation as a reference.*

- One or more `DisplayServers <https://github.com/godotengine/godot/blob/master/platform/linuxbsd/x11/display_server_x11.cpp>`__,
  with the windowing methods implemented. DisplayServer also covers features such
  as mouse support, touchscreen support and tablet driver (for pen input).
  See the
  `DisplayServer singleton header <https://github.com/godotengine/godot/blob/master/servers/display_server.h>`__
  for reference.

  - For platforms not featuring full windowing support (or if it's not relevant
    for the port you are making), most windowing functions can be left mostly
    unimplemented. These functions can be made to only check if the window ID is
    ``MAIN_WINDOW_ID`` and specific operations like resizing may be tied to the
    platform's screen resolution feature (if relevant). Any attempt to create
    or manipulate other window IDs can be rejected.
- *If the target platform supports the graphics APIs in question:* Rendering
  context for `Vulkan <https://github.com/godotengine/godot/blob/master/platform/linuxbsd/x11/vulkan_context_x11.cpp>`__,
  `OpenGL 3.3 or OpenGL ES 3.0 <https://github.com/godotengine/godot/blob/master/platform/linuxbsd/x11/gl_manager_x11.cpp>`__.
- Input handlers for `keyboard <https://github.com/godotengine/godot/blob/master/platform/linuxbsd/x11/key_mapping_x11.cpp>`__
  and `controller <https://github.com/godotengine/godot/blob/master/platform/linuxbsd/joypad_linux.cpp>`__.
- One or more `audio drivers <https://github.com/godotengine/godot/blob/master/drivers/pulseaudio/audio_driver_pulseaudio.cpp>`__.
  The audio driver can be located in the ``platform/`` folder (this is done for
  the Android and Web platforms), or in the ``drivers/`` folder if multiple
  platforms may be using this audio driver. See the
  `AudioServer singleton header <https://github.com/godotengine/godot/blob/master/servers/audio_server.h>`__
  for reference.
- `Crash handler <https://github.com/godotengine/godot/blob/master/platform/linuxbsd/crash_handler_linuxbsd.cpp>`__,
  for printing crash backtraces when the game crashes. This allows for easier
  troubleshooting on platforms where logs aren't readily accessible.
- `Text-to-speech driver <https://github.com/godotengine/godot/blob/master/platform/linuxbsd/tts_linux.cpp>`__
  (for accessibility).
- `Export handler <https://github.com/godotengine/godot/tree/master/platform/linuxbsd/export>`__
  (for exporting from the editor, including :ref:`doc_one-click_deploy`).
  Not required if you intend to export only a PCK from the editor, then run the
  export template binary directly by renaming it to match the PCK file. See the
  `EditorExportPlatform header <https://github.com/godotengine/godot/blob/master/editor/export/editor_export_platform.h>`__
  for reference.
  ``run_icon.svg`` (16×16) should be present within the platform folder if
  :ref:`doc_one-click_deploy` is implemented for the target platform. This icon
  is displayed at the top of the editor when one-click deploy is set up for the
  target platform.

If the target platform doesn't support running Vulkan, OpenGL 3.3 or OpenGL ES 3.0,
you have two options:

- Use a library at run-time to translate Vulkan or OpenGL calls to another graphics API.
  For example, `MoltenVK <https://moltengl.com/moltenvk/>`__ is used on macOS
  to translate Vulkan to Metal at run-time.
- Create a new renderer from scratch. This is a large undertaking, especially if
  you want to support both 2D and 3D rendering with advanced features.

Distributing a custom platform port
-----------------------------------

.. warning::

    Before distributing a custom platform port, make sure you're allowed to
    distribute all the code that is being linked against. Console SDKs are
    typically under NDAs which prevent redistribution to the public.

Platform ports are designed to be as self-contained as possible. Most of the
code can be kept within a single folder located in ``platform/``. Like
:ref:`doc_custom_modules_in_cpp`, this allows for streamlining the build process
by making it possible to ``git clone`` a platform folder within a Godot repository
clone's ``platform/`` folder, then run ``scons platform=<name>``. No other steps are
necessary for building, unless third-party platform-specific dependencies need
to be installed first.

However, when a custom rendering backend is needed, another folder must be added
in ``drivers/``. In this case, the platform port can be distributed as a fork of
the Godot repository, or as a collection of several folders that can be added
over a Godot Git repository clone.
