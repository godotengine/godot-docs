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

Disabling 3D
------------

For 2D games, having the whole 3D engine available usually makes no sense. Because of this, there is a build flag to disable it:

::

    scons p=windows target=release tools=no disable_3d=yes

Tools must be disabled in order to use this flag, as the editor is not designed
to operate without 3D support. Without it, the binary size can be reduced
by about 15%.

Disabling advanced GUI nodes
----------------------------

Most small games don't require complex GUI controls such as Tree, ItemList,
TextEditor or GraphEdit. They can be disabled using a build flag:

::

    scons p=windows target=release tools=no disable_advanced_gui=yes

Disabling unwanted modules
--------------------------

A lot of Godot's functions are offered as modules.
You can see a list of modules with the following command:

::

    scons --help

The list of modules that can be disabled will appear, together with all
build options. If you are working on a simple 2D game, you could disable
a lot of them:

::

    scons p=windows target=release tools=no module_arkit_enabled=no module_assimp_enabled=no module_bmp_enabled=no module_bullet_enabled=no module_camera_enabled=no module_csg_enabled=no module_dds_enabled=no module_enet_enabled=no module_etc_enabled=no module_gdnative_enabled=no module_gridmap_enabled=no module_hdr_enabled=no module_jsonrpc_enabled=no module_mbedtls_enabled=no module_mobile_vr_enabled=no module_opensimplex_enabled=no module_opus_enabled=no module_pvr_enabled=no module_recast_enabled=no module_regex_enabled=no module_squish_enabled=no module_svg_enabled=no module_tga_enabled=no module_theora_enabled=no module_tinyexr_enabled=no module_upnp_enabled=no module_vhacd_enabled=no module_vorbis_enabled=no module_webm_enabled=no module_webp_enabled=no module_webrtc_enabled=no module_websocket_enabled=no module_xatlas_unwrap_enabled=no

If this proves not to work for your use case, you should review the list of
modules and see which ones you actually still need for your game (e.g. you
might want to keep networking-related modules, regex support, or theora/webm
to play videos).

Alternatively, you can supply a list of disabled modules by creating
``custom.py`` at the root of the source, with the contents similar to the
following:

.. code-block:: python

    # custom.py
    
    module_arkit_enabled = "no"
    module_assimp_enabled = "no"
    module_bmp_enabled = "no"
    module_bullet_enabled = "no"
    module_camera_enabled = "no"
    module_csg_enabled = "no"
    module_dds_enabled = "no"
    module_enet_enabled = "no"
    module_etc_enabled = "no"
    module_gdnative_enabled = "no"
    module_gridmap_enabled = "no"
    module_hdr_enabled = "no"
    module_jsonrpc_enabled = "no"
    module_mbedtls_enabled = "no"
    module_mobile_vr_enabled = "no"
    module_opensimplex_enabled = "no"
    module_opus_enabled = "no"
    module_pvr_enabled = "no"
    module_recast_enabled = "no"
    module_regex_enabled = "no"
    module_squish_enabled = "no"
    module_svg_enabled = "no"
    module_tga_enabled = "no"
    module_theora_enabled = "no"
    module_tinyexr_enabled = "no"
    module_upnp_enabled = "no"
    module_vhacd_enabled = "no"
    module_vorbis_enabled = "no"
    module_webm_enabled = "no"
    module_webp_enabled = "no"
    module_webrtc_enabled = "no"
    module_websocket_enabled = "no"
    module_xatlas_unwrap_enabled = "no"
    
.. seealso::

    :ref:`doc_overriding_build_options`.

Optimizing for size instead of speed
------------------------------------

Godot 3.1 onwards allows compiling using size optimizations (instead of speed).
To enable this, set the ``optimize`` flag to ``size``:

::

    scons p=windows target=release tools=no optimize=size

Some platforms such as WebAssembly already use this mode by default.

Compiling with link-time optimization
-------------------------------------

Enabling link-time optimization produces more efficient binaries, both in
terms of performance and file size. It works by eliminating duplicate
template functions and unused code. It can currently be used with the GCC
and MSVC compilers:

::

    scons p=windows target=release tools=no use_lto=yes

Linking becomes much slower with this option, so it should be used only for
release builds.

Stripping binaries
------------------

If you build from source, remember to strip debug symbols from binaries:

::

    strip godot.64

Using UPX to compress binaries
------------------------------

If you are targeting desktop platforms, the
`UPX <https://upx.github.io/>`_ compressor can be used.
This can reduce binary size considerably.

However, keep in mind that some antivirus programs may detect UPX-packed
binaries as a virus. Therefore, if you are releasing a commercial game,
make sure to sign your binaries or use a platform that will distribute them.
