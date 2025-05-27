.. _doc_optimizing_for_size:

Optimizing a build for size
===========================

.. highlight:: shell

Rationale
---------

Sometimes, it is desired to optimize a build for size rather than speed.
This means not compiling unused functions from the engine, as well as using
specific compiler flags to aid on decreasing build size.
Common situations include creating builds for mobile and Web platforms.

This tutorial aims to give an overview on different methods to create
a smaller binary. Before continuing, it is recommended to read the previous tutorials
on compiling Godot for each platform.

The options below are listed from the most important (greatest size savings)
to the least important (lowest size savings).

Stripping binaries
------------------

- **Space savings:** Very high
- **Difficulty:** Easy
- **Performed in official builds:** Yes

If you build Windows (MinGW), Linux or macOS binaries from source, remember to
strip debug symbols from binaries by installing the ``strip`` package from your
distribution then running:

::

    strip path/to/godot.binary

On Windows, ``strip.exe`` is included in most MinGW toolchain setups.

This will reduce the size of compiled binaries by a factor between 5× and 10×.
The downside is that crash backtraces will no longer provide accurate information
(which is useful for troubleshooting the cause of a crash).
:ref:`C++ profilers <doc_using_cpp_profilers>` will also no longer be able to display
function names (this does not affect the built-in GDScript profiler).

.. note::

    The above command will not work on Windows binaries compiled with MSVC
    and platforms such as Android and Web. Instead, pass ``debug_symbols=no``
    on the SCons command line when compiling.

Compiling with link-time optimization
-------------------------------------

- **Space savings:** High
- **Difficulty:** Easy
- **Performed in official builds:** Yes

Enabling link-time optimization produces more efficient binaries, both in
terms of performance and file size. It works by eliminating duplicate
template functions and unused code. It can currently be used with the GCC
and MSVC compilers:

::

    scons target=template_release lto=full

Linking becomes much slower and more RAM-consuming with this option,
so it should be used only for release builds. You need to have at least
8 GB of RAM available for successful linking with LTO enabled. Since the operating
system and programs will take up some RAM, in practice, you need 12 GB of RAM
installed in your system (preferably 16 GB) to compile Godot with LTO enabled.

Optimizing for size instead of speed
------------------------------------

- **Space savings:** High
- **Difficulty:** Easy
- **Performed in official builds:** Yes, but only for web builds

Godot 3.1 onwards allows compiling using size optimizations (instead of speed).
To enable this, set the ``optimize`` flag to ``size``:

::

    scons target=template_release optimize=size

Some platforms such as WebAssembly already use this mode by default.

Godot 4.5 introduced the ``size_extra`` option, which can further reduce size.

::

    scons target=template_release optimize=size_extra

Disabling advanced text server
------------------------------

- **Space savings:** High
- **Difficulty:** Easy
- **Performed in official builds:** No

By default, Godot uses an advanced text server with the support for the
following features:

- Right-to-left typesetting and complex scripts, required to write languages
  such as Arabic and Hebrew.
- Font ligatures and OpenType features (such as small capitals, fractions and
  slashed zero).

Godot provides a fallback text server that isn't compiled by default. This text
server can be used as a lightweight alternative to the default advanced text
server:

::

    scons target=template_release module_text_server_adv_enabled=no module_text_server_fb_enabled=yes

If you only intend on supporting Latin, Greek and Cyrillic-based languages in
your project, the fallback text server should suffice.

This fallback text server can also process large amounts of text more quickly
than the advanced text server. This makes the fallback text server a good fit
for mobile/web projects.

.. note::

    Remember to always pass ``module_text_server_fb_enabled=yes`` when using
    ``module_text_server_adv_enabled=no``. Otherwise, the compiled binary won't
    contain any text server, which means no text will be displayed at all when
    running the project.

Disabling 3D
------------

- **Space savings:** Moderate
- **Difficulty:** Easy
- **Performed in official builds:** No

For 2D games, having the whole 3D engine available usually makes no sense.
Because of this, there is a build flag to disable it:

::

    scons target=template_release disable_3d=yes

Tools must be disabled in order to use this flag, as the editor is not designed
to operate without 3D support. Without it, the binary size can be reduced
by about 15%.

Disabling advanced GUI objects
------------------------------

- **Space savings:** Moderate
- **Difficulty:** Easy
- **Performed in official builds:** No

Most small games don't require complex GUI controls such as Tree, ItemList,
TextEdit or GraphEdit. They can be disabled using a build flag:

::

    scons target=template_release disable_advanced_gui=yes

This is everything that will be disabled:

- :ref:`class_AcceptDialog`
- :ref:`class_CharFXTransform`
- :ref:`class_CodeEdit`
- :ref:`class_CodeHighlighter`
- :ref:`class_ColorPicker`
- :ref:`class_ColorPickerButton`
- :ref:`class_ConfirmationDialog`
- :ref:`class_FileDialog`
- :ref:`class_FoldableContainer`
- :ref:`class_FoldableGroup`
- :ref:`class_GraphEdit`
- :ref:`class_GraphElement`
- :ref:`class_GraphFrame`
- :ref:`class_GraphNode`
- :ref:`class_HSplitContainer`
- :ref:`class_MenuBar`
- :ref:`class_MenuButton`
- :ref:`class_OptionButton`
- :ref:`class_PopupMenu` (will make all popup menus unavailable in code for classes that use them,
  like :ref:`class_LineEdit`, even though those classes are still available)
- :ref:`class_RichTextEffect`
- :ref:`class_RichTextLabel`
- :ref:`class_SpinBox`
- :ref:`class_SplitContainer`
- :ref:`class_SubViewportContainer`
- :ref:`class_SyntaxHighlighter`
- :ref:`class_TextEdit`
- :ref:`class_Tree`
- :ref:`class_TreeItem`
- :ref:`class_VSplitContainer`

Disabling physics engines
-------------------------

- **Space savings:** Low to moderate
- **Difficulty:** Easy
- **Performed in official builds:** No

If your 3D project uses Jolt Physics, you can disable GodotPhysics3D at compile-time as
it will never be used:

::

    scons target=template_release module_godot_physics_3d_enabled=no

Inversely, if your 3D project uses GodotPhysics3D, you can disable Jolt Physics at compile-time:

::

    scons target=template_release module_jolt_enabled=no

If your project uses 3D rendering but not physics (or 2D rendering but not physics),
you can also disable 2D or 3D physics entirely. Most 3D projects can take advantage
of this, as they don't make use of 2D physics:

::

    scons target=template_release disable_physics_2d=yes

::

    scons target=template_release disable_physics_3d=yes

Disabling unwanted modules
--------------------------

- **Space savings:** Very low to moderate depending on modules
- **Difficulty:** Medium to hard depending on modules
- **Performed in official builds:** No

A lot of Godot's functions are offered as modules.
You can see a list of modules with the following command:

::

    scons --help

The list of modules that can be disabled will appear, together with all
build options. If you are working on a simple 2D game, you could disable
a lot of them:

::

    scons target=template_release module_astcenc_enabled=no module_basis_universal_enabled=no module_bcdec_enabled=no module_bmp_enabled=no module_camera_enabled=no module_csg_enabled=no module_dds_enabled=no module_enet_enabled=no module_etcpak_enabled=no module_fbx_enabled=no module_gltf_enabled=no module_gridmap_enabled=no module_hdr_enabled=no module_interactive_music_enabled=no module_jsonrpc_enabled=no module_ktx_enabled=no module_mbedtls_enabled=no module_meshoptimizer_enabled=no module_minimp3_enabled=no module_mobile_vr_enabled=no module_msdfgen_enabled=no module_multiplayer_enabled=no module_noise_enabled=no module_navigation_2d_enabled=no module_navigation_3d_enabled=no module_ogg_enabled=no module_openxr_enabled=no module_raycast_enabled=no module_regex_enabled=no module_svg_enabled=no module_tga_enabled=no module_theora_enabled=no module_tinyexr_enabled=no module_upnp_enabled=no module_vhacd_enabled=no module_vorbis_enabled=no module_webrtc_enabled=no module_websocket_enabled=no module_webxr_enabled=no module_zip_enabled=no

If this proves not to work for your use case, you should review the list of
modules and see which ones you actually still need for your game (e.g. you might
want to keep networking-related modules, regex support,
``minimp3``/``ogg``/``vorbis`` to play music, or ``theora`` to play videos).

Alternatively, you can supply a list of disabled modules by creating
``custom.py`` at the root of the source, with the contents similar to the
following:

.. code-block:: python
    :caption: custom.py

    module_astcenc_enabled = "no"
    module_basis_universal_enabled = "no"
    module_bcdec_enabled = "no"
    module_bmp_enabled = "no"
    module_camera_enabled = "no"
    module_csg_enabled = "no"
    module_dds_enabled = "no"
    module_enet_enabled = "no"
    module_etcpak_enabled = "no"
    module_fbx_enabled = "no"
    module_gltf_enabled = "no"
    module_gridmap_enabled = "no"
    module_hdr_enabled = "no"
    module_interactive_music_enabled = "no"
    module_jsonrpc_enabled = "no"
    module_ktx_enabled = "no"
    module_mbedtls_enabled = "no"
    module_meshoptimizer_enabled = "no"
    module_minimp3_enabled = "no"
    module_mobile_vr_enabled = "no"
    module_msdfgen_enabled = "no"
    module_multiplayer_enabled = "no"
    module_noise_enabled = "no"
    module_navigation_2d_enabled = "no"
    module_navigation_3d_enabled = "no"
    module_ogg_enabled = "no"
    module_openxr_enabled = "no"
    module_raycast_enabled = "no"
    module_regex_enabled = "no"
    module_svg_enabled = "no"
    module_tga_enabled = "no"
    module_theora_enabled = "no"
    module_tinyexr_enabled = "no"
    module_upnp_enabled = "no"
    module_vhacd_enabled = "no"
    module_vorbis_enabled = "no"
    module_webrtc_enabled = "no"
    module_websocket_enabled = "no"
    module_webxr_enabled = "no"
    module_zip_enabled = "no"

.. seealso::

    :ref:`doc_overriding_build_options`.

Optimizing the distribution of your project
-------------------------------------------

Desktop
~~~~~~~

.. note::

    This section is only relevant when distributing the files on a desktop
    platform that doesn't perform its own compression or packing. As such, this
    advice is relevant when you distribute ZIP archives on itch.io or GitHub
    Releases.

    Platforms like Steam already apply their own compression scheme, so you
    don't need to create a ZIP archive to distribute files in the first place.

As an aside, you can look into optimizing the distribution of your project itself.
This can be done even without recompiling the export template.

`7-Zip <https://7-zip.org/>`__ can be used to create ZIP archives that are more
efficient than usual, while remaining compatible with every ZIP extractor
(including Windows' own built-in extractor). ZIP size reduction in a large
project can reach dozens of megabytes compared to a typical ZIP compressor,
although average savings are in the 1-5 MB range. Creating this ZIP archive will
take longer than usual, but it will extract just as fast as any other ZIP
archive.

When using the 7-Zip GUI, this is done by creating a ZIP archive with the Ultra
compression mode. When using the command line, this is done using the following
command:

::

    7z a -mx9 my_project.zip folder_containing_executable_and_pck

Web
~~~

Enabling gzip or Brotli compression for all file types from the web export
(especially the ``.wasm`` and ``.pck``) can reduce the download size
significantly, leading to faster loading times, especially on slow connections.

Creating precompressed gzip or Brotli files with a high compression level can be
even more efficient, as long as the web server is configured to serve those
files when they exist. When supported, Brotli should be preferred over gzip as
it has a greater potential for file size reduction.

See :ref:`doc_exporting_for_web_serving_the_files` for instructions.
