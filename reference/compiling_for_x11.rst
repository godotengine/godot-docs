.. _doc_compiling_for_x11:

Compiling for X11 (Linux, *BSD)
===============================

.. highlight:: shell

Requirements
------------

For compiling under Linux or other Unix variants, the following is
required:

-  GCC (G++) or Clang (note: use of GCC6 is discouraged because of optimization problems. Prefer GCC versions <6 for the moment).
-  Python 2.7+ (3.0 is untested as of now)
-  SCons build system
-  pkg-config (used to detect the dependencies below)
-  X11, Xcursor, Xinerama and XRandR development libraries
-  MesaGL development libraries
-  ALSA development libraries
-  PulseAudio development libraries (for sound support)
-  Freetype (for the editor)
-  OpenSSL (for HTTPS and TLS)
-  libudev-dev (optional, for gamepad support)

Distro-specific oneliners
^^^^^^^^^^^^^^^^^^^^^^^^^

+---------------+------------------------------------------------------------------------------------------------------------+
| **Fedora**    | ::                                                                                                         |
|               |                                                                                                            |
|               |     sudo dnf install scons pkgconfig libX11-devel libXcursor-devel libXrandr-devel libXinerama-devel \     |
|               |         mesa-libGL-devel alsa-lib-devel pulseaudio-libs-devel freetype-devel openssl-devel libudev-devel   |
+---------------+------------------------------------------------------------------------------------------------------------+
| **FreeBSD**   | ::                                                                                                         |
|               |                                                                                                            |
|               |     sudo pkg install scons pkg-config xorg-libraries libXcursor libXrandr xineramaproto libglapi libGLU \  |
|               |         freetype2 openssl                                                                                  |
+---------------+------------------------------------------------------------------------------------------------------------+
| **Mageia**    | ::                                                                                                         |
|               |                                                                                                            |
|               |     urpmi scons pkgconfig "pkgconfig(alsa)" "pkgconfig(freetype2)" "pkgconfig(glu)" "pkgconfig(libpulse)" \|
|               |         "pkgconfig(openssl)" "pkgconfig(udev)" "pkgconfig(x11)" "pkgconfig(xcursor)" "pkgconfig(xinerama)"\|
|               |         "pkgconfig(xrandr)"                                                                                |
+---------------+------------------------------------------------------------------------------------------------------------+
| **Ubuntu**    | ::                                                                                                         |
|               |                                                                                                            |
|               |     sudo apt-get install build-essential scons pkg-config libx11-dev libxcursor-dev libxinerama-dev \      |
|               |         libgl1-mesa-dev libglu-dev libasound2-dev libpulse-dev libfreetype6-dev libssl-dev libudev-dev \   |
|               |         libxrandr-dev                                                                                      |
+---------------+------------------------------------------------------------------------------------------------------------+
| **Arch**      | ::                                                                                                         |
|               |                                                                                                            |
|               |     pacman -S scons libxcursor libxinerama libxrandr mesa glu alsa-lib pulseaudio freetype2                |
+---------------+------------------------------------------------------------------------------------------------------------+
| **Gentoo**    | ::                                                                                                         |
|               |                                                                                                            |
|               |     emerge -an dev-util/scons x11-libs/libX11 x11-libs/libXcursor x11-libs/libXinerama media-libs/mesa \   |
|               |         media-libs/glu media-libs/alsa-lib media-sound/pulseaudio media-libs/freetype                      |
+---------------+------------------------------------------------------------------------------------------------------------+

Compiling
---------

Start a terminal, go to the root dir of the engine source code and type:

::

    user@host:~/godot$ scons platform=x11

If all goes well, the resulting binary executable will be placed in the
"bin" subdirectory. This executable file contains the whole engine and
runs without any dependencies. Executing it will bring up the project
manager.

If you wish to compile using Clang rather than GCC, use this command:

::

    user@host:~/godot$ scons platform=x11 use_llvm=yes

Building export templates
-------------------------

To build X11 (Linux, *BSD) export templates, run the build system with the
following parameters:

-  (32 bits)

::

    user@host:~/godot$ scons platform=x11 tools=no target=release bits=32
    user@host:~/godot$ scons platform=x11 tools=no target=release_debug bits=32

-  (64 bits)

::

    user@host:~/godot$ scons platform=x11 tools=no target=release bits=64
    user@host:~/godot$ scons platform=x11 tools=no target=release_debug bits=64

Note that cross compiling for the opposite bits (64/32) as your host
platform is not always straight-forward and might need a chroot environment.

To create standard export templates, the resulting files must be copied to:

::

    /home/youruser/.godot/templates

and named like this (even for *BSD which is seen as "Linux X11" by Godot):

::

    linux_x11_32_debug
    linux_x11_32_release
    linux_x11_64_debug
    linux_x11_64_release

However, if you are writing your custom modules or custom C++ code, you
might instead want to configure your binaries as custom export templates
here:

.. image:: /img/lintemplates.png

You don't even need to copy them, you can just reference the resulting
files in the bin/ directory of your Godot source folder, so the next
time you build you automatically have the custom templates referenced.
