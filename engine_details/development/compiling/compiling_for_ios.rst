.. _doc_compiling_for_ios:

Compiling for iOS
=================

.. highlight:: shell

.. seealso::

    This page describes how to compile iOS export template binaries from source.
    If you're looking to export your project to iOS instead, read :ref:`doc_exporting_for_ios`.

Requirements
------------

- `Python 3.8+ <https://www.python.org/downloads/macos/>`_.
- `SCons 4.0+ <https://scons.org/pages/download.html>`_ build system.
- `Xcode <https://apps.apple.com/us/app/xcode/id497799835>`_.
    - Launch Xcode once and install iOS support. If you have already launched
      Xcode and need to install iOS support, go to *Xcode -> Settings... -> Platforms*.
    - Go to *Xcode -> Settings... -> Locations -> Command Line Tools* and select
      an installed version. Even if one is already selected, re-select it.
-  Download and follow README instructions to build a static ``.xcframework``
   from the `MoltenVK SDK <https://github.com/KhronosGroup/MoltenVK#fetching-moltenvk-source-code>`__.

.. note:: If you have `Homebrew <https://brew.sh/>`_ installed, you can easily
          install SCons using the following command:

          ::

              brew install scons

          Installing Homebrew will also fetch the Command Line Tools
          for Xcode automatically if you don't have them already.

          Similarly, if you have `MacPorts <https://www.macports.org/>`_
          installed, you can easily install SCons using the
          following command:

          ::

              sudo port install scons

.. seealso:: To get the Godot source code for compiling, see
             :ref:`doc_getting_source`.

             For a general overview of SCons usage for Godot, see
             :ref:`doc_introduction_to_the_buildsystem`.

Compiling
---------

Open a Terminal, go to the root folder of the engine source code and type
the following to compile a debug build:

::

    scons platform=ios target=template_debug generate_bundle=yes

To compile a release build:

::

    scons platform=ios target=template_release generate_bundle=yes

To create an Xcode project like in the official builds, you need to use the
template located in ``misc/dist/ios_xcode``. The release and debug libraries
should be placed in ``libgodot.ios.debug.xcframework`` and
``libgodot.ios.release.xcframework`` respectively. This process can be automated
by using the ``generate_bundle=yes`` option on the *last* SCons command used to
build export templates (so that all binaries can be included).

The MoltenVK static ``.xcframework`` folder must also be placed in the
``ios_xcode`` folder once it has been created. MoltenVK is always statically
linked on iOS; there is no dynamic linking option available, unlike macOS.

.. warning::

    Compiling for the iOS simulator is currently not supported as per
    `GH-102149 <https://github.com/godotengine/godot/issues/102149>`__.

    Apple Silicon Macs can run iOS apps natively, so you can run exported iOS projects
    directly on an Apple Silicon Mac without needing the iOS simulator.

Run
---

To run on a device, follow these instructions:
:ref:`doc_exporting_for_ios`.

iOS exports can run directly on an Apple Silicon Mac. To run exported iOS project
on Mac, open exported project in Xcode and select ``My Mac`` in the ``Run Destinations``
dropdown.

Troubleshooting
---------------

Fatal error: 'cstdint' file not found
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you get a compilation error of this form early on, it's likely because
the Xcode command line tools installation needs to be repaired after
a macOS or Xcode update:

::

    ./core/typedefs.h:45:10: fatal error: 'cstdint' file not found
    45 | #include <cstdint>
       |          ^~~~~~~~~

Run these two commands to reinstall Xcode command line tools
(enter your administrator password as needed):

::

    sudo rm -rf /Library/Developer/CommandLineTools
    sudo xcode-select --install

If it still does not work, try updating Xcode from the Mac App Store and try again.
