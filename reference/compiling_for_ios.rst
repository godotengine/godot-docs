.. _doc_compiling_for_ios:

Compiling for iOS
=================

.. highlight:: shell

Requirements
------------

-  SCons (you can get it from macports, you should be able to run
   ``scons`` in a terminal when installed)
-  Xcode with the iOS SDK and the command line tools.

Compiling
---------

Open a Terminal, go to the root dir of the engine source code and type:

::

    $ scons p=iphone bin/godot.iphone.debug

for a debug build, or:

::

    $ scons p=iphone bin/godot.iphone.opt target=release

for a release build (check ``platform/iphone/detect.py`` for the compiler
flags used for each configuration).

Alternatively, you can run

::

    $ scons p=isim bin/godot.isim.tools

for a Simulator executable.

Additionally since some time Apple requires 64 bit version of application binary when you are uploading to iStore.
The best way to provide these is to create a bundle in which there are both 32bit and 64 binaries, so every device will be able to run the game.
It can be done in three steps, first compile 32 bit version, then compile 64 bit version and then use ``lipo`` to bundle them into one fat binary, all those steps can be performed with following commands: 

::

    $ scons p=iphone tools=no bits=32 target=release 
    $ scons p=iphone tools=no bits=64 target=release
    $ lipo -create bin/godot.iphone.opt.32 arm64 bin/godot.iphone.opt.64 -output bin/godot.iphone.opt.universal


Run
---

To run on a device or simulator, follow these instructions:
:ref:`doc_exporting_for_ios`.

Replace or add your executable to the Xcode project, and change the
"executable name" property on Info.plist accordingly if you use an
alternative build.
