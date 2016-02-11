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

Run
---

To run on a device or simulator, follow these instructions:
:ref:`doc_exporting_for_ios`.

Replace or add your executable to the Xcode project, and change the
"executable name" property on Info.plist accordingly if you use an
alternative build.
