.. _doc_compiling_for_osx:

Compiling for OSX
=================

.. highlight:: shell

Requirements
------------

For compiling under Linux or other Unix variants, the following is
required:

-  Python 2.7+ or Python 3.5+
-  SCons build system
-  Xcode (or the more lightweight Command Line Tools for Xcode)

Compiling
---------

Start a terminal, go to the root dir of the engine source code and type:

::

    user@host:~/godot$ scons platform=osx

If all goes well, the resulting binary executable will be placed in the
"bin" subdirectory. This executable file contains the whole engine and
runs without any dependencies. Executing it will bring up the project
manager.

To create an .app like in the official builds, you need to use the template
located in ``misc/dist/osx_tools.app``. Typically, for a ".64" optimised binary 
built with `scons p=osx target=release_debug`:

::

    user@host:~/godot$ cp -r misc/dist/osx_tools.app ./Godot.app
    user@host:~/godot$ mkdir -p Godot.app/Contents/MacOS
    user@host:~/godot$ cp bin/godot.osx.tools.64 Godot.app/Contents/MacOS/Godot
    user@host:~/godot$ chmod +x Godot.app/Contents/MacOS/Godot
    
Compiling for 32 and 64-bit
---------------------------

All macOS versions after 10.6 are 64-bit exclusive, so the executable
will be a ".64" file by default for most users. If you would like to 
compile a ".fat" executable which contains both 32 and 64-bit code, 
you can do so by specifying the bits in the scons command like so:

::

    user@host:~/godot$ scons platform=osx bits=fat
    
Cross-compiling
---------------

It is possible to compile for OSX in a Linux environment (and maybe
also in Windows with Cygwin). For that you will need
`OSXCross <https://github.com/tpoechtrager/osxcross>`__ to be able
to use OSX as target. First, follow the instructions to install it:

Clone the `OSXCross repository <https://github.com/tpoechtrager/osxcross>`
somewhere on your machine (or download a zip file and extract it somewhere),
e.g.:

::

    user@host:~$ git clone https://github.com/tpoechtrager/osxcross.git /home/myuser/sources/osxcross

1. Follow the instructions to package the SDK:
   https://github.com/tpoechtrager/osxcross#packaging-the-sdk
2. Follow the instructions to install OSXCross:
   https://github.com/tpoechtrager/osxcross#installation

After that, you will need to define the ``OSXCROSS_ROOT`` as the path to
the OSXCross installation (the same place where you cloned the
repository/extracted the zip), e.g.:

::

    user@host:~$ export OSXCROSS_ROOT=/home/myuser/sources/osxcross

Now you can compile with SCons like you normally would:

::

    user@host:~/godot$ scons platform=osx

If you have an OSXCross SDK version different from the one expected by the SCons buildsystem, you can specify a custom one with the ``osxcross_sdk`` argument:

::

    user@host:~/godot$ scons platform=osx osxcross_sdk=darwin15
