.. _doc_compiling_with_dotnet:

Compiling with .NET
===================

.. highlight:: shell

Requirements
------------

- `.NET SDK 6.0+ <https://dotnet.microsoft.com/download>`_

  You can use ``dotnet --info`` to check which .NET SDK versions are installed.

Enable the .NET module
----------------------

.. note:: C# support for Godot has historically used the
          `Mono <https://www.mono-project.com/>`_ runtime instead of the
          `.NET Runtime <https://github.com/dotnet/runtime>`_ and internally
          many things are still named ``mono`` instead of ``dotnet`` or
          otherwise referred to as ``mono``.

By default, the .NET module is disabled when building. To enable it, add the
option ``module_mono_enabled=yes`` to the SCons command line, while otherwise
following the instructions for building the desired Godot binaries.

The editor build also generates the C# glue bindings, builds the managed assemblies
by default, and makes the built NuGet packages available to projects by
setting up a NuGet source pointing to the ``bin/GodotSharp/Tools/nupkgs`` folder.

Full build example for the current platform
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    # Build editor binary
    scons target=editor module_mono_enabled=yes
    # Build export templates
    scons target=template_debug module_mono_enabled=yes
    scons target=template_release module_mono_enabled=yes


Full build example, specifying the platform and precision
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    # Build editor binary
    scons p=linuxbsd target=editor module_mono_enabled=yes precision=double
    # Build export templates
    scons p=linuxbsd target=template_debug module_mono_enabled=yes precision=double
    scons p=linuxbsd target=template_release module_mono_enabled=yes precision=double


Generate the glue
-----------------

Parts of the sources of the managed libraries are generated from the ClassDB.
These source files must be generated before building the managed libraries.
This step happens by default when building the editor with the .NET module enabled.
It can also be run manually with any .NET-enabled Godot editor binary by running it with
the parameters ``--headless --generate-mono-glue`` followed by the path to an
output directory.
This path must be ``modules/mono/glue`` in the Godot directory::

    <godot_binary> --headless --generate-mono-glue modules/mono/glue

This command will tell Godot to generate the C# bindings for the Godot API at
``modules/mono/glue/GodotSharp/GodotSharp/Generated``, and the C# bindings for
the editor tools at ``modules/mono/glue/GodotSharp/GodotSharpEditor/Generated``.
Once these files are generated, you can build Godot's managed libraries for all
the desired targets without having to repeat this process.

``<godot_binary>`` refers to the editor binary you compiled with the .NET module
enabled. Its exact name will differ based on your system and configuration, but
should be of the form ``bin/godot.<platform>.editor.<arch>.mono``, e.g.
``bin/godot.linuxbsd.editor.x86_64.mono`` or 
``bin/godot.windows.editor.x86_32.mono.exe``. Be especially aware of the
**.mono** suffix! If you've previously compiled Godot without .NET support, you
might have similarly named binaries without this suffix. These binaries can't be
used to generate the .NET glue.

.. note:: The glue sources must be regenerated every time the ClassDB-registered
          API changes. That is, for example, when a new method is registered to
          the scripting API or one of the parameters of such a method changes.
          Godot will print an error at startup if there is an API mismatch
          between ClassDB and the glue sources.

Building the managed libraries
------------------------------

Once you have generated the .NET glue, you can build the managed libraries with
the ``build_assemblies.py`` script::

    ./modules/mono/build_scripts/build_assemblies.py --godot-output-dir=./bin

If everything went well, the ``GodotSharp`` directory, containing the managed
libraries, should have been created in the ``bin`` directory.

.. note:: By default, all development builds share a version number, which can
          cause some issues with caching of the NuGet packages. To solve this
          issue either use ``GODOT_VERSION_STATUS`` to give every build a unique
          version or delete ``GodotNuGetFallbackFolder`` after every build to
          clear the package cache.

Unlike "classical" Godot builds, when building with the .NET module enabled
(and depending on the target platform), a data directory may be created both
for the editor and for exported projects. This directory is important for
proper functioning and must be distributed together with Godot.
More details about this directory in
:ref:`Data directory<compiling_with_dotnet_data_directory>`.

Build Platform
^^^^^^^^^^^^^^

Provide the ``--godot-platform=<platform>`` argument to control for which
platform specific the libraries are built. Omit this argument to build for the
current system.

This currently only controls the inclusion of the support for Visual Studio as
an external editor, the libraries are otherwise identical.

NuGet packages
^^^^^^^^^^^^^^

The API assemblies, source generators, and custom MSBuild project SDK are
distributed as NuGet packages. NuGet exposes these packages to builds via a list
of configured sources that point to local paths or web URLS, where the packages
are stored.

By default, the .NET enabled editor build configures a ``GodotSourceBuild``
NuGet source that points to the ``bin/GodotSharp/Tools/nupkgs`` directory,
making locally built packages automatically available to projects that match
that version of Godot.

You can also manually publish NuGet packages to another location when running
the ``build_assemblies.py`` manually. This is required if you disable the
``build_assemblies`` step of the editor build (which will skip the configuration
of the NuGet source pointing to the locally built packages), or if you want to
manually control which packages are used.

The ``--push-nupkgs-local`` option will publish packages to the provided path,
and will make sure there are no other versions of the package in the NuGet cache,
as MSBuild may pick one of those instead::

    ./modules/mono/build_scripts/build_assemblies.py --godot-output-dir ./bin --push-nupkgs-local ~/MyLocalNugetSource

In order to use these packages, a local NuGet source must be created where MSBuild
can find them. This can be done with the .NET CLI::

    dotnet nuget add source ~/MyLocalNugetSource --name MyLocalNugetSource

Double Precision Support (REAL_T_IS_DOUBLE)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When building Godot with double precision support, i.e. the ``precision=double``
argument for scons, the managed libraries must be adjusted to match by passing
the ``--precision=double`` argument:

::

    ./modules/mono/build_scripts/build_assemblies.py --godot-output-dir ./bin --push-nupkgs-local ~/MyLocalNugetSource --precision=double


.. _compiling_with_dotnet_data_directory:

Data directory
--------------

The data directory is a dependency for Godot binaries built with the .NET module
enabled. It contains important files for the correct functioning of Godot. It
must be distributed together with the Godot executable.

Editor
^^^^^^

The name of the data directory for the Godot editor will always be
``GodotSharp``. This directory contains an ``Api`` subdirectory with the Godot
API assemblies and a ``Tools`` subdirectory with the tools required by the
editor, like the ``GodotTools`` assemblies and its dependencies.

On macOS, if the Godot editor is distributed as a bundle, the ``GodotSharp``
directory may be placed in the ``<bundle_name>.app/Contents/Resources/``
directory inside the bundle.

Export templates
^^^^^^^^^^^^^^^^

The data directory for exported projects is generated by the editor during the
export. It is named ``data_<APPNAME>_<ARCH>``, where ``<APPNAME>`` is the
application name as specified in the project setting ``application/config/name``
and ``<ARCH>`` is the current architecture of the export.

In the case of multi-architecture exports multiple such data directories will be
generated.


More Examples
-------------

Editor build example, skipping the managed assembly build steps
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    scons target=editor module_mono_enabled=yes build_assemblies=no


Editor build example, skipping the glue generation and managed assembly build steps
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    scons target=editor module_mono_enabled=yes generate_mono_glue=no build_assemblies=no


Generating the glue code manually (Windows)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    bin/godot.windows.editor.x86_64.mono --generate-mono-glue modules/mono/glue


Generating the glue code manually (Linux, \*BSD)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    bin/godot.linuxbsd.editor.x86_64.mono --generate-mono-glue modules/mono/glue


Building managed assemblies manually (Windows)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    ./modules/mono/build_scripts/build_assemblies.py --godot-output-dir=./bin --godot-platform=windows --push-nupkgs-local ~/MyLocalNugetSource


Command-line options
--------------------

The following is the list of command-line options available when building with
the .NET module:

- **module_mono_enabled**\ =yes | **no**

  - Build Godot with the .NET module enabled.


- **generate_mono_glue**\ =yes | **no** (default:: yes)

  - Generate the C# glue bindings


- **build_assemblies**\ =yes | **no** (default:: yes)

  - Build managed assemblies and nuget packages
