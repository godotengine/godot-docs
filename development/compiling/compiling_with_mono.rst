.. _doc_compiling_with_mono:

Compiling with Mono
===================

.. highlight:: shell

Requirements
------------

- Mono (the required version is listed here: :ref:`doc_c_sharp`)
- MSBuild
- pkg-config

Environment Variables
---------------------

By default, SCons will try to find Mono in the Windows Registry on Windows or via ``pkg-config`` on other platforms. You can specify a different installation directory by using the following environment variables for the respective ``bits`` option: ``MONO32_PREFIX`` and ``MONO64_PREFIX``.

The specified directory must contain the subdirectories ``bin``, ``include``, and ``lib``.

Enable Mono Module
--------------------

By default, the mono module is disabled for builds. To enable it you can pass the option ``module_mono_enabled=yes`` to your SCons command.

Generate The Glue
-------------------

The glue sources are the wrapper functions that will be called by the managed side. In order to generate them, first, you must build Godot with the options ``tools=yes`` and ``mono_glue=no``:

::

    scons p=<platform> tools=yes module_mono_enabled=yes mono_glue=no

After the build finishes, you need to run the compiled executable with the parameter ``--generate-mono-glue`` followed by the path to an output directory. This path must be ``modules/mono/glue`` in the Godot directory.

::

    godot --generate-mono-glue modules/mono/glue

This command will tell Godot to generate the file *modules/mono/glue/mono_glue.gen.cpp*. Once this file is generated, you can build Godot for all the desired targets without the need to repeat this process.

As always, ``godot`` refers to the compiled Godot binary, so if it isn't in your PATH, you need to give the full path to the executable, e.g. if it is located in the ``bin`` subfolder, it becomes ``bin/godot``.

Notes
^^^^^
-  **Do not** build normal binaries with ``mono_glue=no``. This option disables C# scripting and therefore must only be used for the temporary binary that will be used to generate the glue. Godot should print a message at startup warning you about this.
-  The glue sources must be regenerated every time the ClassDB API changes. If there is an API mismatch with the generated glue, Godot will print an error at startup.

Example (x11)
-------------

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

