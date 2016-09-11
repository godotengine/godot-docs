.. _doc_compiling_for_uwp:

Compiling for Universal Windows Platform
========================================

.. highlight:: shell

Requirements
------------

-  SCons (see :ref:`doc_compiling_for_windows` for more details).
-  Visual Studio 2015 Update 2. It may work with earlier versions. See
   :ref:`doc_compiling_for_windows` about the caveats of installing it
   and the various prompts.
-  Windows 10 SDK (can be selected in Visual Studio installation).
-  `ANGLE source <https://github.com/Microsoft/angle>`__. Use the 
   ``ms_master`` (default) branch. Keep it in a path without spaces to
   avoid problems.

Compiling
---------

You need to open a proper Visual Studio prompt for the target architecture
you want to build. Check :ref:`doc_compiling_for_windows` to see how these
prompts work.

There are three target architectures for UWP: x86 (32-bits), x64 (64-bits)
and ARM (32-bits). You can run ``vcvarsall.bat`` with ``arm`` as argument to
set the environment for this target architecture.

Set the ``ANGLE_SRC_PATH`` to the directory where you downloaded the ANGLE
source code. The build process will also build ANGLE to produce the
required DLLs for the selected architecture.

Once you're set, run the SCons command similarly to the other platforms::

    C:\godot>scons platform=winrt

Creating UWP export templates
-----------------------------

To export using the editor you need to properly build package the templates.
You need all three architectures with ``debug`` and ``release`` templates to
be able to export.

Open the command prompt for one architecture and run SCons twice (once for
each target)::

    C:\godot>scons platform=winrt target=release_debug
    C:\godot>scons platform=winrt target=release

Repeat for the other architectures.

In the end your ``bin`` folder will have the ``.exe`` binaries with a name
like ``godot.winrt.opt.debug.32.x86.exe`` (with variations for each
target/arch).

Copy one of these to ``tools/dist/uwp_template`` inside the Godot source
folder and rename the binary to ``godot.winrt.exe``. From the ANGLE source,
under ``winrt/10/src/Release_%arch%`` (where ``%arch%`` can be ``Win32``,
``x64`` or ``ARM``), get the ``libEGL.dll`` and the ``libGLESv2.dll``,
putting them along with the executable.

Add the files in the ``uwp_template`` folder to a ZIP. Rename the resulting
Zip according to the target/architecture of the template::

    winrt_x86_debug.zip
    winrt_x86_release.zip
    winrt_x64_debug.zip
    winrt_x64_release.zip
    winrt_arm_debug.zip
    winrt_arm_release.zip

Move those templates to the ``templates`` folder in Godot settings path. If
you don't want to replacet the templates, you can set the "Custom Package"
property in the export window.
