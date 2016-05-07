.. _doc_compiling_for_windows:

Compiling for Windows
=====================

.. highlight:: shell

Requirements
------------

For compiling under Windows, the following is required:

-  `Visual C++ <http://www.microsoft.com/visualstudio>`__, Visual C++
   Express compiler or Visual Studio Community (recommended) at least
   the 2013 version (12.0) up to 2015 (14.0). **Make sure you get a
   version that can compile for C++, Desktop**.
-  `Python 2.7+ <https://www.python.org/downloads/>`__ (3.0 is
   untested as of now). Using the 32-bits installer is recommended.
-  `Pywin32 Python Extension <http://sourceforge.net/projects/pywin32>`__
   for parallel builds (which increase the build speed by a great factor).
-  `SCons <http://www.scons.org>`__ build system.

Setting up SCons
----------------

Python adds the interpreter (python.exe) to the path. It usually
installs in ``C:\Python`` (or ``C:\Python[Version]``). SCons installs
inside the python install and provides a .bat file called "scons.bat".
The location of this file can be added to the path or it can simply be
copied to ``C:\Python`` together with the interpreter executable.

Compiling
---------

Start a Visual Studio command prompt (it sets up environment variables
needed by SCons to locate the compiler and SDK). It should be called
"Developer Command Prompt for VS2015" or similar. SCons will not be able
to compile from the standard Windows "Command Prompt".

Once inside the Developer Console, go to the root dir of the engine
source code and type:

::

    C:\godot> scons platform=windows

If all goes well, the resulting binary executable will be placed in
``C:\godot\bin\godot.windows.tools.exe``. This executable file
contains the whole engine and runs without any dependencies. Executing
it will bring up the project manager.

Note for Godot 2.0+ if you are having issues:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You might also find other command prompts in your VS installation. Make
sure you do not use x64 Native or Cross Tools Command Prompts, because
64 bit version of the Visual C compiler can not compile Godot 2.0+, only
the 32 bit (x86) **compiler** can. If you get compiler errors about
``_asm`` (assembly instructions) in theora, switch the command prompt
(compiler if not using VS IDE). One more thing, 32 bit compiler can
compile **both** 32 bit Godot and 64 bit Godot. The process is called
cross compiling for different architectures.

How to know which compiler SCons will use? Open your Developer Command
Prompt (or whatever prompt you are using) and type in ``cl.exe``:

If it says this, you're good to go (note x86 at the end):

::

    Microsoft (R) C/C++ Optimizing Compiler Version 18.00.31101 for x86

If it says (x64), wrong prompt/compiler, find the right one. If the
prompt you are using can't find ``cl.exe``, you are using the standard
Windows Command Prompt... find the right developer prompt.

Development in Visual Studio or other IDEs
------------------------------------------

For most projects, using only scripting is enough but when development
in C++ is needed, for creating modules or extending the engine, working
with an IDE is usually desirable. The visual studio command prompt calls
a .bat file that sets up environment variables (vcvarsall.bat). To build
the whole engine from a single command outside the command prompt, the
following should be called in a .bat file:

::

    C:\path_to_sdk\vcvarsall.bat && scons bin/godot.windows.tools.exe

**NOTE:** It seems the latest Visual Studio does not include a desktop
command prompt (No, Native tools for x86 is not it). The only way to
build it seems to be by running:

::

    "C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\vcvarsall.bat" && c:\python27\scons p=windows

(or however your VS and Scons are installed)

Cross-compiling
---------------

If you are a Linux or Mac user, you need to install mingw32 and
mingw-w64. Under Ubuntu or Debian, just run the following commands:

::

    apt-get install mingw32 mingw-w64

If you are using another distro, scons will check for the following
binaries:

::

    i586-mingw32msvc-gcc
    i686-w64-mingw32-gcc

If the binaries are named or located somewhere else, export the
following env variables:

::

    export MINGW32_PREFIX="/path/to/i586-mingw32msvc-"
    export MINGW64_PREFIX="/path/to/i686-w64-mingw32-"

To make sure you are doing things correctly, executing the following in
the shell should result in a working compiler:

::

    user@host:~$ ${MINGW32_PREFIX}gcc
    gcc: fatal error: no input files

Creating Windows export templates
---------------------------------

Windows export templates are created by compiling Godot as release, with
the following flags:

-  (for 32 bits, using Mingw32 command prompt or Visual Studio command
   prompt)

::

    C:\godot> scons platform=windows tools=no target=release bits=32
    C:\godot> scons platform=windows tools=no target=release_debug bits=32

-  (for 64 bits, using Mingw-w64 or Visual Studio command prompt)

::

    C:\godot> scons platform=windows tools=no target=release bits=64
    C:\godot> scons platform=windows tools=no target=release_debug bits=64

If you plan on replacing the standard templates, copy these to:

::

    C:\USERS\YOURUSER\AppData\Roaming\Godot\Templates

With the following names:

::

    windows_32_debug.exe
    windows_32_release.exe
    windows_64_debug.exe
    windows_64_release.exe

However, if you are writing your custom modules or custom C++ code, you
might instead want to configure your binaries as custom export templates
here:

.. image:: /img/wintemplates.png

You don't even need to copy them, you can just reference the resulting
files in the ``bin\`` directory of your Godot source folder, so the next
time you build you automatically have the custom templates referenced.
