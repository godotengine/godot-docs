.. _doc_compiling_for_universal_windows_apps:

Compiling for Universal Windows Apps
====================================

.. highlight:: shell

This page documents the current state of the "winrt" platform, used to
support "Windows Store Apps" for Windows 8.1, and Windows Phone 8.1 apps
using Microsoft's new "Universal" APIs.

Requirements
------------

-  Windows 8
-  SCons (see :ref:`doc_compiling_for_windows` for more details)
-  Visual Studio 2013 for Windows (but *not* "for Windows Desktop").
   Tested on "Microsoft Visual Studio Express 2013 for Windows Version
   12.0.31101.00 Update 4".

Compiling
---------

The platform can compile binaries for both Windows 8.1 and Windows Phone
8.1. The architecture is decided by the environment variable "PLATFORM".

Windows 8.1
~~~~~~~~~~~

-  Open a "VS 2013 x64 Cross Tools Command Prompt"
-  The value of environment variable "PLATFORM" should be "x64"
-  Run scons with ``platform=winrt`` from the root of the source tree::

    C:\godot_source> scons platform=winrt

-  You should get an executable file inside bin/ named according to your
   build options, for the architecture "x64", for example
   "godot.winrt.tools.x64.exe".

Windows Phone 8.1
~~~~~~~~~~~~~~~~~

-  Open a "Visual Studio 2012 ARM Phone Tools Command Prompt"
-  The value of environment variable "PLATFORM" should be "arm"
-  Run scons with ``platform=winrt`` from the root of the source tree::

    C:\godot_source> scons platform=winrt

-  You should get an executable file inside bin/ named according to your
   build options, for the architecture "arm", for example
   "godot.winrt.tools.arm.exe".

Running
-------

On Visual studio, create a new project using any of the "Universal App"
templates found under Visual C++ -> Store Apps -> Universal Apps. "Blank
App" should be fine.

On the "Solution Explorer" box, you should have 3 sections, "App.Windows
(Windows 8.1)", "App.WindowsPhone (Windows Phone 8.1)" and "App.Shared".
You need to add files to each section:

App.Shared
~~~~~~~~~~

Add a folder named "game" containing your game content (can be individual
files or your data.pck). Remember to set the "Content" property of each
file to "True", otherwise your files won't get included in the package.

App.Windows
~~~~~~~~~~~

-  Add your windows executable, and all the .dll files found on
   platform/winrt/x64/bin on the godot source. Remember to also set the
   "Content" property.
-  Find the file "Package.appxmanifest". Right click on it and select
   "Open with..." then "XML (Text) Editor" from the list.
-  Find the "Application" section, and add (or modify) the "Executable"
   property with the name of your .exe. Example:

::

    <Application Id="App" Executable="godot.winrt.tools.x64.exe" EntryPoint="App_Windows.App">

App.WindowsPhone
~~~~~~~~~~~~~~~~

Repeat all the steps from App.Windows, using your arm executable and
the dlls found in platform/winrt/arm/bin. Remember to set the
"Content" property for all the files.

Use the green "Play" button on the top to run. The drop down menu next
to it should let you choose the project (App.Windows or
App.WindowsPhone) and the device ("Local Machine", "Device" for an
attached phone, etc).

Angle
-----

ANGLE precompiled binaries are provided on platform/winrt/x64 and
platform/winrt/arm. They are built from MSOpenTech's "future-dev"
branch, found here: https://github.com/MSOpenTech/angle. The visual
studio 'solutions' used are found on ``projects/winrt/windows/angle.sln``
and ``projects/winrt/windowsphone/angle.sln``.

What's missing
--------------

-  Audio
-  Semaphores
-  Keyboard input
-  Proper handling of screen rotation
-  Proper handling of other events such as focus lost, back button, etc.
-  Packaging and deploying to devices from the editor.
-  Adding Angle to our tree and compiling it from there. The same source
   could also be used to build for Windows (and use Angle instead of
   native GL, which will be more compatible with graphics hardware)

Packages
--------

This is what we know:

-  App packages are documented here:
   http://msdn.microsoft.com/en-us/library/windows/apps/xaml/hh464929.aspx
-  There are 2 command line tools that might be useful, `App Packager
   <http://msdn.microsoft.com/en-us/library/windows/apps/xaml/hh446767.aspx>`__
   and `SignTool
   <http://msdn.microsoft.com/en-us/library/windows/apps/xaml/ff551778.aspx>`__.
-  There are a bunch of tools on "powershell" that deal with packages
   that might be relevant:
   http://technet.microsoft.com/library/dn448373.aspx
-  When running a Windows 8.1 app on "Local Machine" from Visual studio,
   the app seems to run from an uncompressed directory on the filesystem
   in an arbitrary location (ie. outside of the proper directory where
   Apps are installed), but there is some special registry entry made
   for it, so we know it's possible to skip the packaging step to run
   locally (in the case of very big games this can be useful).
