.. _doc_compiling_for_windows:

Compiling for Windows
=====================

.. highlight:: shell

.. seealso::

    This page describes how to compile Windows editor and export template binaries from source.
    If you're looking to export your project to Windows instead, read :ref:`doc_exporting_for_windows`.

Requirements
------------

For compiling under Windows, the following is required:

- `Visual Studio Community <https://www.visualstudio.com/vs/community/>`_,
  version 2019 or later. Visual Studio 2022 is recommended.
  **Make sure to read "Installing Visual Studio caveats" below or you
  will have to run/download the installer again.**
- `MinGW-w64 <https://mingw-w64.org/>`_ with GCC can be used as an alternative to
  Visual Studio. Be sure to install/configure it to use the ``posix`` thread model.
  **Important:** When using MinGW to compile the ``master`` branch, you need GCC 9 or later.
- `Python 3.6+ <https://www.python.org/downloads/windows/>`_.
  **Make sure to enable the option to add Python to the ``PATH`` in the installer.**
- `SCons 3.0+ <https://scons.org/pages/download.html>`_ build system. Using the
  latest release is recommended, especially for proper support of recent Visual
  Studio releases.

.. note:: If you have `Scoop <https://scoop.sh/>`_ installed, you can easily
          install MinGW and other dependencies using the following command::

              scoop install gcc python scons make mingw

.. note:: If you have `MSYS2 <https://www.msys2.org/>`_ installed, you can easily
          install MinGW and other dependencies using the following command::

              pacman -S mingw-w64-x86_64-python3-pip mingw-w64-x86_64-gcc  \
                  mingw-w64-i686-python3-pip mingw-w64-i686-gcc make

          For each MSYS2 MinGW subsystem, you should then run
          `pip3 install scons` in its shell.

.. seealso:: To get the Godot source code for compiling, see
             :ref:`doc_getting_source`.

             For a general overview of SCons usage for Godot, see
             :ref:`doc_introduction_to_the_buildsystem`.

Setting up SCons
----------------

To install SCons, open the command prompt and run the following command::

    python -m pip install scons

If you are prompted with the message
``Defaulting to user installation because normal site-packages is not
writeable``, you may have to run that command again using elevated
permissions. Open a new command prompt as an Administrator then run the command
again to ensure that SCons is available from the ``PATH``.

To check whether you have installed Python and SCons correctly, you can
type ``python --version`` and ``scons --version`` into a command prompt
(``cmd.exe``).

If the commands above don't work, make sure to add Python to your ``PATH``
environment variable after installing it, then check again.
You can do so by running the Python installer again and enabling the option
to add Python to the ``PATH``.

If SCons cannot detect your Visual Studio installation, it might be that your
SCons version is too old. Update it to the latest version with
``python -m pip install --upgrade scons``.

.. _doc_compiling_for_windows_install_vs:

Installing Visual Studio caveats
--------------------------------

If installing Visual Studio 2017 or 2019, make sure to enable **C++** in
the list of workflows to install.

If installing Visual Studio 2015, make sure to run a **Custom**
installation instead of **Typical** and select **C++** as a language there.

If you've already made the mistake of installing Visual Studio without
C++ support, run the installer again; it should present you a **Modify** button.
Running the installer from *Add/Remove Programs* will only give you
a **Repair** option, which won't let you install C++ tools.

Downloading Godot's source
--------------------------

Refer to :ref:`doc_getting_source` for detailed instructions.

The tutorial will assume from now on that you placed the source code in
``C:\godot``.

.. warning::

    To prevent slowdowns caused by continuous virus scanning during compilation,
    add the Godot source folder to the list of exceptions in your antivirus
    software.

    For Windows Defender, hit the :kbd:`Windows` key, type "Windows Security"
    then hit :kbd:`Enter`. Click on **Virus & threat protection** on the left
    panel. Under **Virus & threat protection settings** click on **Mange Settings**
    and scroll down to **Exclusions**. Click **Add or remove exclusions** then
    add the Godot source folder.

Compiling
---------

Selecting a compiler
~~~~~~~~~~~~~~~~~~~~

SCons will automatically find and use an existing Visual Studio installation.
If you do not have Visual Studio installed, it will attempt to use
MinGW instead. If you already have Visual Studio installed and want to
use MinGW, pass ``use_mingw=yes`` to the SCons command line. Note that MSVC
builds cannot be performed from the MSYS2 or MinGW shells. Use either
``cmd.exe`` or PowerShell instead.

.. tip::

    During development, using the Visual Studio compiler is usually a better
    idea, as it links the Godot binary much faster than MinGW. However, MinGW
    can produce more optimized binaries using link-time optimization (see
    below), making it a better choice for production use. This is particularly
    the case for the GDScript VM which performs much better with MinGW compared
    to MSVC. Therefore, it's recommended to use MinGW to produce builds that you
    distribute to players.

    All official Godot binaries are built in
    `custom containers <https://github.com/godotengine/build-containers>`__
    using MinGW.

Running SCons
~~~~~~~~~~~~~

After opening a command prompt, change to the root directory of
the engine source code (using ``cd``) and type:

.. code-block:: doscon

    C:\godot> scons platform=windows

.. note:: When compiling with multiple CPU threads, SCons may warn about
          pywin32 being missing. You can safely ignore this warning.

If all goes well, the resulting binary executable will be placed in
``C:\godot\bin\`` with the name ``godot.windows.editor.x86_32.exe`` or
``godot.windows.editor.x86_64.exe``. By default, SCons will build a binary matching
your CPU architecture, but this can be overridden using ``arch=x86_64`` or
``arch=x86_32``.

This executable file contains the whole engine and runs without any
dependencies. Running it will bring up the Project Manager.

.. tip:: If you are compiling Godot for production use, you can
         make the final executable smaller and faster by adding the
         SCons option ``production=yes``. This enables additional compiler
         optimizations and link-time optimization.

         LTO takes some time to run and requires about 7 GB of available RAM
         while compiling. If you're running out of memory with the above option,
         use ``production=yes lto=none`` or ``production=yes lto=thin`` for a
         lightweight but less effective form of LTO.

.. note:: If you want to use separate editor settings for your own Godot builds
          and official releases, you can enable
          :ref:`doc_data_paths_self_contained_mode` by creating a file called
          ``._sc_`` or ``_sc_`` in the ``bin/`` folder.

Compiling with support for Direct3D 12
--------------------------------------

By default, builds of Godot do not contain support for the Direct3D 12 graphics
API.

To compile Godot with Direct3D 12 support you need at least the following:

- `The DirectX Shader Compiler <https://github.com/Microsoft/DirectXShaderCompiler/releases>`_.
  The zip folder will be named "dxc\_" followed by the date of release. Download
  it anywhere, unzip it and remember the path to the unzipped folder, you will
  need it below.
- `godot-nir-static library <https://github.com/godotengine/godot-nir-static/releases/>`_.
  We compile the Mesa libraries you will need into a static library. Download it
  anywhere, unzip it and remember the path to the unzipped folder, you will
  need it below.

.. note:: You can optionally build the godot-nir-static libraries yourself with
          the following steps:

          1. Install the Python package `mako <https://www.makotemplates.org>`_
             which is needed to generate some files.
          2. Clone the `godot-nir-static <https://github.com/godotengine/godot-nir-static>`_
             directory and navigate to it.
          3. Run the following::

              git submodule update --init
              ./update_mesa.sh
              scons

             If you are building with MinGW, add ``use_mingw=yes`` to the ``scons``
             command, you can also specify build architecture using ``arch={architecture}``.

             Mesa static library should be built using the same compiler you are
             using for building Godot.

Optionally, you can compile with the following for additional features:

- `PIX <https://devblogs.microsoft.com/pix/download>`_ is a performance tuning
  and debugging application for Direct3D12 applications. If you compile-in
  support for it, you can get much more detailed information through PIX that
  will help you optimize your game and troubleshoot graphics bugs. To use it,
  download the WinPixEventRuntime package. You will be taken to a NuGet package
  page where you can click "Download package" to get it. Once downloaded, change
  the file extension to .zip and unzip the file to some path.
- `Agility SDK <https://devblogs.microsoft.com/directx/directx12agility>`_ can
  be used to provide access to the latest Direct3D 12 features without relying
  on driver updates. To use it, download the latest Agility SDK package. You
  will be taken to a NuGet package page where you can click "Download package"
  to get it. Once downloaded, change the file extension to .zip and unzip the
  file to some path.

.. note:: If you use a preview version of the Agility SDK, remember to enable
          developer mode in Windows; otherwise it won't be used.

.. note:: If you want to use a PIX with MinGW build, navigate to PIX runtime
          directory and use the following commands to generate import library::

            # For x86-64:
            gendef ./bin/x64/WinPixEventRuntime.dll
            dlltool --machine i386:x86-64 --no-leading-underscore -d WinPixEventRuntime.def -D WinPixEventRuntime.dll -l ./bin/x64/libWinPixEventRuntime.a

            # For ARM64:
            gendef ./bin/ARM64/WinPixEventRuntime.dll
            dlltool --machine arm64 --no-leading-underscore -d WinPixEventRuntime.def -D WinPixEventRuntime.dll -l ./bin/ARM64/libWinPixEventRuntime.a

When building Godot, you will need to tell SCons to use Direct3D 12 and where to
look for the additional libraries:

.. code-block:: doscon

    C:\godot> scons platform=windows d3d12=yes dxc_path=<...> mesa_libs=<...>

Or, with all options enabled:

.. code-block:: doscon

    C:\godot> scons platform=windows d3d12=yes dxc_path=<...> mesa_libs=<...> agility_sdk_path=<...> pix_path=<...>

.. note:: The build process will copy ``dxil.dll`` from the ``bin/<arch>/``
          directory in the DXC folder to the Godot binary directory and the
          appropriate ``bin/<arch>`` file in the Godot binary directory.
          Direct3D 12-enabled Godot packages for distribution to end users must
          include the ``dxil.dll`` (and relevant folders if using multi-arch),
          both for the editor and games. At runtime, the renderer will try to
          load the DLL from the arch-specific folders, and will fall back to the
          same directory as the Godot executable if the appropriate arch isn't
          found.

.. note:: For the Agility SDK's DLLs you have to explicitly choose the kind of
          workflow. Single-arch is the default (DLLs copied to ``bin/``). If you
          pass ``agility_sdk_multi_arch=yes`` to SCons, you'll opt-in for
          multi-arch. DLLs will be copied to the appropriate ``bin/<arch>/``
          subdirectories and at runtime the right one will be loaded.

Compiling with ANGLE support
----------------------------

ANGLE provides a translation layer from OpenGL ES 3.x to Direct3D 11 and can be used
to improve support for the Compatibility renderer on some older GPUs with outdated
OpenGL drivers and on Windows for ARM.

By default, Godot is built with dynamically linked ANGLE, you can use it by placing
``libEGL.dll`` and ``libGLESv2.dll`` alongside the executable.

.. note:: You can use dynamically linked ANGLE with export templates as well, rename
          aforementioned DLLs to ``libEGL.{architecture}.dll`` and ``libGLESv2.{architecture}.dll``
          and place them alongside export template executables, and libraries will
          be automatically copied during the export process.

To compile Godot with statically linked ANGLE:

- Download pre-built static libraries from `godot-angle-static library <https://github.com/godotengine/godot-angle-static/releases>`_, and unzip them.
- When building Godot, add ``angle_libs={path}`` to tell SCons where to look for the ANGLE libraries::

    scons platform=windows angle_libs=<...>

.. note:: You can optionally build the godot-angle-static libraries yourself with
          the following steps:

          1. Clone the `godot-angle-static <https://github.com/godotengine/godot-angle-static>`_
             directory and navigate to it.
          2. Run the following command::

              scons

             If you are buildng with MinGW, add ``use_mingw=yes`` to the command,
             you can also specify build architecture using ``arch={architecture}``.

             ANGLE static library should be built using the same compiler you are
             using for building Godot.

Development in Visual Studio
----------------------------

Using an IDE is not required to compile Godot, as SCons takes care of everything.
But if you intend to do engine development or debugging of the engine's C++ code,
you may be interested in configuring a code editor or an IDE.

Folder-based editors don't require any particular setup to start working with Godot's
codebase. To edit projects with Visual Studio they need to be set up as a solution.

You can create a Visual Studio solution via SCons by running SCons with
the ``vsproj=yes`` parameter, like this::

   scons p=windows vsproj=yes

You will be able to open Godot's source in a Visual Studio solution now,
and able to build Godot using Visual Studio's **Build** button.

.. seealso:: See :ref:`doc_configuring_an_ide_vs` for further details.

Cross-compiling for Windows from other operating systems
--------------------------------------------------------

If you are a Linux or macOS user, you need to install
`MinGW-w64 <https://mingw-w64.org/doku.php>`__, which typically comes in 32-bit
and 64-bit variants. The package names may differ based on your distribution,
here are some known ones:

+----------------+--------------------------------------------------------------+
| **Arch Linux** | ::                                                           |
|                |                                                              |
|                |     pacman -Sy mingw-w64                                     |
+----------------+--------------------------------------------------------------+
| **Debian** /   | ::                                                           |
| **Ubuntu**     |                                                              |
|                |     apt install mingw-w64                                    |
+----------------+--------------------------------------------------------------+
| **Fedora**     | ::                                                           |
|                |                                                              |
|                |     dnf install mingw64-gcc-c++ mingw64-winpthreads-static \ |
|                |                 mingw32-gcc-c++ mingw32-winpthreads-static   |
+----------------+--------------------------------------------------------------+
| **macOS**      | ::                                                           |
|                |                                                              |
|                |     brew install mingw-w64                                   |
+----------------+--------------------------------------------------------------+
| **Mageia**     | ::                                                           |
|                |                                                              |
|                |     urpmi mingw64-gcc-c++ mingw64-winpthreads-static \       |
|                |           mingw32-gcc-c++ mingw32-winpthreads-static         |
+----------------+--------------------------------------------------------------+

Before attempting the compilation, SCons will check for
the following binaries in your ``PATH`` environment variable::

    i686-w64-mingw32-gcc
    x86_64-w64-mingw32-gcc

If the binaries are not located in the ``PATH`` (e.g. ``/usr/bin``),
you can define the following environment variable to give a hint to
the build system::

    export MINGW_PREFIX="/path/to/mingw"

Where ``/path/to/mingw`` is the path containing the ``bin`` directory where
``i686-w64-mingw32-gcc`` and ``x86_64-w64-mingw32-gcc`` are located (e.g.
``/opt/mingw-w64`` if the binaries are located in ``/opt/mingw-w64/bin``).

To make sure you are doing things correctly, executing the following in
the shell should result in a working compiler (the version output may
differ based on your system)::

    ${MINGW_PREFIX}/bin/x86_64-w64-mingw32-gcc --version
    # x86_64-w64-mingw32-gcc (GCC) 13.2.0

.. note:: When cross-compiling for Windows using MinGW-w64, keep in mind only
          ``x86_64`` and ``x86_32`` architectures are supported. Be sure to
          specify the right ``arch=`` option when invoking SCons if building
          from a different architecture.

Troubleshooting
~~~~~~~~~~~~~~~

Cross-compiling from some Ubuntu versions may lead to
`this bug <https://github.com/godotengine/godot/issues/9258>`_,
due to a default configuration lacking support for POSIX threading.

You can change that configuration following those instructions,
for 64-bit::

    sudo update-alternatives --config x86_64-w64-mingw32-gcc
    <choose x86_64-w64-mingw32-gcc-posix from the list>
    sudo update-alternatives --config x86_64-w64-mingw32-g++
    <choose x86_64-w64-mingw32-g++-posix from the list>

And for 32-bit::

    sudo update-alternatives --config i686-w64-mingw32-gcc
    <choose i686-w64-mingw32-gcc-posix from the list>
    sudo update-alternatives --config i686-w64-mingw32-g++
    <choose i686-w64-mingw32-g++-posix from the list>

Creating Windows export templates
---------------------------------

Windows export templates are created by compiling Godot without the editor,
with the following flags:

.. code-block:: doscon

    C:\godot> scons platform=windows target=template_debug arch=x86_32
    C:\godot> scons platform=windows target=template_release arch=x86_32
    C:\godot> scons platform=windows target=template_debug arch=x86_64
    C:\godot> scons platform=windows target=template_release arch=x86_64

If you plan on replacing the standard export templates, copy these to the
following location, replacing ``<version>`` with the version identifier
(such as ``3.1.1.stable`` or ``3.2.dev``):

.. code-block:: none

    %USERPROFILE%\AppData\Roaming\Godot\templates\<version>\

With the following names::

    windows_32_debug.exe
    windows_32_release.exe
    windows_64_debug.exe
    windows_64_release.exe

However, if you are using custom modules or custom engine code, you
may instead want to configure your binaries as custom export templates
here:

.. image:: img/wintemplates.png

You don't need to copy them in this case, just reference the resulting
files in the ``bin\`` directory of your Godot source folder, so the next
time you build, you will automatically have the custom templates referenced.
