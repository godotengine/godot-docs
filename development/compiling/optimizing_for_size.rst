.. _doc_optimizing_for_size:

Optimizing a Build for Size
===========================

.. highlight:: shell

Rationale
------------

Sometimes, it is desired to optimize a build for size, rather than speed.
This means reducing unused functions from the engine, as well as using specific compiler flags to aid on this job. Common situations are creating smaller mobile or HTML5 builds.

This tutorial aims to give an overview on different methods to create a smaller binary.

It is recommended that the previous tutorials in this section (on how to build Godot for every paltform) are well understood before continuing.

Disabling 3D
-------------

For 2D games, having the whole 3D engine available usually makes no sense. Because of this, there is a build flag to disable it:

::

	scons p=windows target=release tools=no disable_3d=yes

Tools must be disabled in order to use this flag, as the editor is not designed to operate without 3D support. Without it, the binary size can be reduced about 15%.

Disabling Advanced GUI
-----------------------

Most small games don't require complex GUI controls such as trees, itemlists, text editor, graph editor, etc. They can be disabled with a command line flag:

::

	scons p=windows target=release tools=no disable_advanced_gui=yes

Disabling unwanted modules
--------------------------

A lot of Godot functions are offered as modules. When asking for build options with:

::

	scons --help

The list of modules that can be disabled will appear, together with all the build options. If you are working on a simple 2D game, you could disable a lot of them:

::

	scons p=windows target=release tools=no module_bmp_enabled=no module_bullet_enabled=no module_csg_enabled=no module_dds_enabled=no module_enet_enabled=no module_etc_enabled=no module_gdnative_enabled=no module_gridmap_enabled=no module_hdr_enabled=no module_mbedtls_enabled=no module_mobile_vr_enabled=no module_mono_enabled=no module_opus_enabled=no module_pvr_enabled=no module_recast_enabled=no module_regex_enabled=no module_squish_enabled=no module_tga_enabled=no module_thekla_unwrap_enabled=no module_theora_enabled=no module_tinyexr_enabled=no module_vorbis_enabled=no module_webm_enabled=no module_websocket_enabled=no

Optimizing for size, instead of speed
--------------------------------------

Godot 3.1 onwards allows to compile using size optimizations. To enable this, just use the *optimize* flag:

::

	scons p=windows target=release tools=no optimize=size

Keep in mind some platforms such as HTML5 already use this mode by default.

Link Time Optimization
----------------------

Enabling link time optimization produces more efficient binaries, both in
performance and size. Duplicate template functions are removed, as well as
unused code. 

::

	scons p=windows target=release tools=no use_lto=yes

Linking is slower with this option, so use mainly for release builds.

Strip your binaries
-------------------

If you build from scratch, remember to strip your binaries:

::

	strip godot.64


Using UPX
---------

If you are aiming for desktop platforms, the UPX compressor can be used:

https://upx.github.io/

This can reduce binary size considerably. Keep in mind some greedy
anti-virus can detect upx compiled binaries as a virus so, if you are
releasing a commercial game, make sure to sign your binaries or use a
platform that will distribute them.



