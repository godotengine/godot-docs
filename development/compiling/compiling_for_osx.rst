.. _doc_compiling_for_osx:

Compiling for macOS
===================

.. highlight:: shell

Requirements
------------

For compiling under macOS, the following is required:

- `Python 3.5+ <https://www.python.org>`_.
- `SCons 3.0+ <https://www.scons.org>`_ build system.
- `Xcode <https://apps.apple.com/us/app/xcode/id497799835>`_
  (or the more lightweight Command Line Tools for Xcode).
- *Optional* - `yasm <https://yasm.tortall.net/>`_ (for WebM SIMD optimizations).

If you are building the ``master`` branch:
- Download and install the `Vulkan SDK for macOS <https://vulkan.lunarg.com/sdk/home>`__.

.. note:: If you have `Homebrew <https://brew.sh/>`_ installed, you can easily
          install SCons and yasm using the following command::

              brew install scons yasm

          Installing Homebrew will also fetch the Command Line Tools
          for Xcode automatically if you don't have them already.

.. seealso:: For a general overview of SCons usage for Godot, see
             :ref:`doc_introduction_to_the_buildsystem`.

Compiling
---------

Start a terminal, go to the root directory of the engine source code.

To compile for Intel (x86-64) powered Macs, use::

    scons platform=osx arch=x86_64 --jobs=$(sysctl -n hw.logicalcpu)

To compile for Apple Silicon (ARM64) powered Macs, use::

    scons platform=osx arch=arm64 --jobs=$(sysctl -n hw.logicalcpu)

To support both architectures in a single "Universal 2" binary, run the above two commands and then use ``lipo`` to bundle them together::

    lipo -create bin/godot.osx.tools.x86_64 bin/godot.osx.tools.arm64 -output bin/godot.osx.tools.universal

If all goes well, the resulting binary executable will be placed in the
``bin/`` subdirectory. This executable file contains the whole engine and
runs without any dependencies. Executing it will bring up the project
manager.

.. note:: If you want to use separate editor settings for your own Godot builds
          and official releases, you can enable
          :ref:`doc_data_paths_self_contained_mode` by creating a file called
          ``._sc_`` or ``_sc_`` in the ``bin/`` folder.

To create an ``.app`` bundle like in the official builds, you need to use the
template located in ``misc/dist/osx_tools.app``. Typically, for an optimized
editor binary built with ``target=release_debug``::

    cp -r misc/dist/osx_tools.app ./Godot.app
    mkdir -p Godot.app/Contents/MacOS
    cp bin/godot.osx.opt.tools.universal Godot.app/Contents/MacOS/Godot
    chmod +x Godot.app/Contents/MacOS/Godot

If you are building the ``master`` branch, additionally copy the Vulkan library::

    mkdir -p Godot.app/Contents/Frameworks
    cp <Vulkan SDK path>/macOS/libs/libMoltenVK.dylib Godot.app/Contents/Frameworks/libMoltenVK.dylib

Compiling a headless/server build
---------------------------------

To compile a *headless* build which provides editor functionality to export
projects in an automated manner, use::

    scons platform=server tools=yes target=release_debug --jobs=$(sysctl -n hw.logicalcpu)

To compile a *server* build which is optimized to run dedicated game servers,
use::

    scons platform=server tools=no target=release --jobs=$(sysctl -n hw.logicalcpu)

Cross-compiling for macOS from Linux
------------------------------------

It is possible to compile for macOS in a Linux environment (and maybe also in
Windows using the Windows Subsystem for Linux). For that, you'll need to install
`OSXCross <https://github.com/tpoechtrager/osxcross>`__ to be able to use macOS
as a target. First, follow the instructions to install it:

Clone the `OSXCross repository <https://github.com/tpoechtrager/osxcross>`__
somewhere on your machine (or download a ZIP file and extract it somewhere),
e.g.::

    git clone --depth=1 https://github.com/tpoechtrager/osxcross.git "$HOME/osxcross"

1. Follow the instructions to package the SDK:
   https://github.com/tpoechtrager/osxcross#packaging-the-sdk
2. Follow the instructions to install OSXCross:
   https://github.com/tpoechtrager/osxcross#installation

After that, you will need to define the ``OSXCROSS_ROOT`` as the path to
the OSXCross installation (the same place where you cloned the
repository/extracted the zip), e.g.::

    export OSXCROSS_ROOT="$HOME/osxcross"

Now you can compile with SCons like you normally would::

    scons platform=osx

If you have an OSXCross SDK version different from the one expected by the SCons buildsystem, you can specify a custom one with the ``osxcross_sdk`` argument::

    scons platform=osx osxcross_sdk=darwin15
