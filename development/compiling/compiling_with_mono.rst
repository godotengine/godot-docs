.. _doc_compiling_with_mono:

Compiling with Mono
===================

.. highlight:: shell

Requirements
------------

- Mono 5.12.0 or greater
- MSBuild
- pkg-config

Environment variables
---------------------

By default, SCons will try to find Mono in the Windows Registry on Windows or via ``pkg-config`` on other platforms. You can specify a different installation directory by using the following environment variables for the respective ``bits`` option: ``MONO32_PREFIX`` and ``MONO64_PREFIX``.

The specified directory must contain the subdirectories ``bin``, ``include``, and ``lib``.

Enable the Mono module
----------------------

By default, the mono module is disabled for builds. To enable it you can pass the option ``module_mono_enabled=yes`` to your SCons command.

Generate the glue
-------------------

The glue sources are the wrapper functions that will be called by managed methods. These source files must be generated before building your final binaries. In order to generate them, first, you must build a temporary Godot binary with the options ``tools=yes`` and ``mono_glue=no``:

::

    scons p=<platform> tools=yes module_mono_enabled=yes mono_glue=no

After the build finishes, you need to run the compiled executable with the parameter ``--generate-mono-glue`` followed by the path to an output directory. This path must be ``modules/mono/glue`` in the Godot directory.

::

    <godot_binary> --generate-mono-glue modules/mono/glue

This command will tell Godot to generate the file ``modules/mono/glue/mono_glue.gen.cpp``.
Once this file is generated, you can build Godot for all the desired targets without the need to repeat this process.

``<godot_binary>`` refers to the tools binary you compiled above with the Mono module enabled.
Its exact name will differ based on your system and configuration, but should be of the form ``bin/godot.<platform>.tools.<bits>.mono``, e.g. ``bin/godot.x11.tools.64.mono`` or ``bin/godot.windows.tools.64.exe``.
Be especially aware of the **.mono** suffix! If you compiled Godot without Mono support previously, you might have similarly named binaries without this suffix which can't be used to generate the Mono glue.

Notes
^^^^^
-  **Do not** build your final binaries with ``mono_glue=no``. This disables C# scripting. This option must be used only for the temporary binary that will generate the glue. Godot will print a warning at startup if it was built without the glue sources.
-  The glue sources must be regenerated every time the ClassDB bindings changes. That is, for example, when a new method is added to ClassDB or one of the parameter of such a method changes. Godot will print an error at startup if there is an API mismatch between ClassDB and the glue sources.

Rebuild with Mono glue
----------------------

Once you have generated the Mono glue, you can build the final binary with ``mono_glue=yes``.
It's the default value for ``mono_glue`` so you can also omit it. You can build the Mono-enabled editor:

::

    scons p=<platform> tools=yes module_mono_enabled=yes mono_glue=yes

And Mono-enabled export templates:

::

    scons p=<platform> tools=no module_mono_enabled=yes mono_glue=yes

Examples
--------

Example (Windows)
^^^^^^^^^^^^^^^^^
::

    # Build temporary binary
    scons p=windows tools=yes module_mono_enabled=yes mono_glue=no
    # Generate glue sources
    bin\godot.windows.tools.64.mono --generate-mono-glue modules/mono/glue

    ### Build binaries normally
    # Editor
    scons p=windows target=release_debug tools=yes module_mono_enabled=yes
    # Export templates
    scons p=windows target=debug tools=no module_mono_enabled=yes
    scons p=windows target=release tools=no module_mono_enabled=yes

Example (X11)
^^^^^^^^^^^^^
::

    # Build temporary binary
    scons p=x11 tools=yes module_mono_enabled=yes mono_glue=no
    # Generate glue sources
    bin/godot.x11.tools.64.mono --generate-mono-glue modules/mono/glue

    ### Build binaries normally
    # Editor
    scons p=x11 target=release_debug tools=yes module_mono_enabled=yes
    # Export templates
    scons p=x11 target=debug tools=no module_mono_enabled=yes
    scons p=x11 target=release tools=no module_mono_enabled=yes

If everything went well, apart from the normal output, SCons should have also built the *GodotSharpTools.dll* assembly and copied it together with the mono runtime shared library to the ``bin`` subdirectory.

Command-line options
--------------------

The following is the list of command-line options available when building with the mono module:

-  **module_mono_enabled**: Build Godot with the mono module enabled (yes|no)
     default: no

-  **mono_glue**: Whether to include the glue source files in the build and define `MONO_GLUE_DISABLED` as a preprocessor macro (yes|no)
     default: yes

-  **xbuild_fallback**: Whether to fallback to xbuild if MSBuild is not available (yes|no)
     default: no

-  **mono_static**: Whether to link the mono runtime statically (yes|no)
     default: no

-  **mono_assemblies_output_dir**: Path to the directory where all the managed assemblies will be copied to. The '#' token indicates de top of the source directory, the directory in which SConstruct is located
     default: #bin
