.. _doc_compiling_for_osx:

Compiling for OSX
=================

.. highlight:: shell

Requirements
------------

For compiling under Linux or other Unix variants, the following is
required:

-  Python 2.7+ (3.0 is untested as of now)
-  SCons build system
-  XCode

Compiling
---------

Start a terminal, go to the root dir of the engine source code and type:

::

    user@host:~/godot$ scons platform=osx

If all goes well, the resulting binary executable will be placed in the
"bin" subdirectory. This executable file contains the whole engine and
runs without any dependencies. Executing it will bring up the project
manager. There is a .app template to put the binary into in
``tools/Godot.app``.

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
