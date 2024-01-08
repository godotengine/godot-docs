.. _doc_compiling_for_ios:

Compiling for iOS
=================

.. highlight:: shell

.. seealso::

    This page describes how to compile iOS export template binaries from source.
    If you're looking to export your project to iOS instead, read :ref:`doc_exporting_for_ios`.

Requirements
------------

- `Python 3.6+ <https://www.python.org/downloads/macos/>`_.
- `SCons 3.0+ <https://scons.org/pages/download.html>`_ build system.
- `Xcode <https://apps.apple.com/us/app/xcode/id497799835>`_.

If you are building the ``master`` branch:

-  Download and follow README instructions to build a static ``.xcframework``
   from the `MoltenVK SDK <https://github.com/KhronosGroup/MoltenVK#fetching-moltenvk-source-code>`__.

.. note:: If you have `Homebrew <https://brew.sh/>`_ installed, you can easily
          install SCons using the following command::

              brew install scons

          Installing Homebrew will also fetch the Command Line Tools
          for Xcode automatically if you don't have them already.

          Similarly, if you have `MacPorts <https://www.macports.org/>`_
          installed, you can easily install SCons using the
          following command::

              sudo port install scons

.. seealso:: To get the Godot source code for compiling, see
             :ref:`doc_getting_source`.

             For a general overview of SCons usage for Godot, see
             :ref:`doc_introduction_to_the_buildsystem`.

Compiling
---------

Open a Terminal, go to the root dir of the engine source code and type:

::

    $ scons p=ios target=template_debug

for a debug build, or:

::

    $ scons p=ios target=template_release

for a release build (check ``platform/ios/detect.py`` for the compiler
flags used for each configuration).

Alternatively, you can run

::

    $ scons p=ios target=template_debug ios_simulator=yes arch=x86_64
    $ scons p=ios target=template_debug ios_simulator=yes arch=arm64

for a Simulator libraries.

To create an Xcode project like in the official builds, you need to use the
template located in ``misc/dist/ios_xcode``. The release and debug libraries
should be placed in ``libgodot.ios.debug.xcframework`` and ``libgodot.ios.release.xcframework`` respectively.

::

    $ cp -r misc/dist/ios_xcode .

    $ cp libgodot.ios.template_debug.arm64.a ios_xcode/libgodot.ios.debug.xcframework/ios-arm64/libgodot.a
    $ lipo -create libgodot.ios.template_debug.arm64.simulator.a libgodot.ios.template_debug.x86_64.simulator.a -output ios_xcode/libgodot.ios.debug.xcframework/ios-arm64_x86_64-simulator/libgodot.a

    $ cp libgodot.ios.template_release.arm64.a ios_xcode/libgodot.ios.release.xcframework/ios-arm64/libgodot.a
    $ lipo -create libgodot.ios.template_release.arm64.simulator.a libgodot.ios.template_release.x86_64.simulator.a -output ios_xcode/libgodot.ios.release.xcframework/ios-arm64_x86_64-simulator/libgodot.a

The MoltenVK static ``.xcframework`` folder must also be placed in the ``ios_xcode``
folder once it has been created.

Run
---

To run on a device or simulator, follow these instructions:
:ref:`doc_exporting_for_ios`.
