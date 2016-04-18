.. _doc_compiling_for_freebsd:

Compiling for FreeBSD
=====================

.. highlight:: shell

Requirements
------------

For compiling under FreeBSD, the following is
required:

-  GCC (G++) or Clang
-  Python 2.7+ (3.0 is untested as of now)
-  SCons build system
-  X11 and Mesa development libraries
-  Xinerama libraries
-  ALSA development libraries (for sound support)
-  Freetype (for the editor)
-  OpenSSL (for HTTPS and TLS)
-  pkg-config (used to detect the above dependencies)

Currently, there's no libudev port available for gamepad support.

For FreeBSD:

::

    sudo pkg install scons pkg-config xorg-libraries libXcursor freetype2 libglapi libGLU openssl xineramaproto

Compiling
---------

Start a terminal, go to the root dir of the engine source code and type:

::

    user@host:~/godot$ scons platform=x11

If all goes well, the resulting binary executable will be placed in the
"bin" subdirectory. This executable file contains the whole engine and
runs without any dependencies. Executing it will bring up the project
manager.

Building export templates
-------------------------

To build FreeBSD export templates, run the build system with the following
parameters:

-  (32 bits)

::

    user@host:~/godot$ scons platform=x11 tools=no target=release bits=32
    user@host:~/godot$ scons platform=x11 tools=no target=release_debug bits=32

-  (64 bits)

::

    user@host:~/godot$ scons platform=x11 tools=no target=release bits=64
    user@host:~/godot$ scons platform=x11 tools=no target=release_debug bits=64

Note that cross compiling for the opposite bits (64/32) as your host
platform in FreeBSD is quite difficult and might need a chroot
environment.

In FreeBSD, compilation works without a chroot but some libraries (.so)
might be missing from ``/usr/lib32``. Symlinking the missing .so files from
``/usr/lib`` results in a working build.

To create standard export templates, the resulting files must be copied
to:

::

    /home/youruser/.godot/templates

and named like this:

::

    freebsd_x11_32_debug
    freebsd_x11_32_release
    freebsd_x11_64_debug
    freebsd_x11_64_release

However, if you are writing your custom modules or custom C++ code, you
might instead want to configure your binaries as custom export templates
here:

.. image:: /img/lintemplates.png

You don't even need to copy them, you can just reference the resulting
files in the bin/ directory of your Godot source folder, so the next
time you build you automatically have the custom templates referenced.
