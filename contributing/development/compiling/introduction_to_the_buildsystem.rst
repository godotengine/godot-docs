.. _doc_introduction_to_the_buildsystem:

Introduction to the buildsystem
===============================

.. highlight:: shell


Godot is a primarily C++ project and it :ref:`uses the SCons build system. <doc_faq_why_scons>`
We love SCons for how maintainable and easy to set up it makes our buildsystem. And thanks to
that compiling Godot from source can be as simple as running:

::

    scons

This produces an editor build for your current platform, operating system, and architecture.
You can change what gets built by specifying a target, a platform, and/or an architecture.
For example, to build an export template used for running exported games, you can run:

::

    scons target=template_release

If you plan to debug or develop the engine, then you might want to enable the ``dev_build``
option to enable dev-only debugging code:

::

    scons dev_build=yes

Following sections in the article will explain these and other universal options in more detail. But
before you can compile Godot, you need to install a few prerequisites. Please refer to the platform
documentation to learn more:

- :ref:`doc_compiling_for_android`
- :ref:`doc_compiling_for_ios`
- :ref:`doc_compiling_for_linuxbsd`
- :ref:`doc_compiling_for_macos`
- :ref:`doc_compiling_for_web`
- :ref:`doc_compiling_for_windows`

These articles cover in great detail both how to setup your environment to compile Godot on a specific
platform, and how to compile for that platform. Please feel free to go back and forth between them and
this article to reference platform-specific and universal configuration options.

Using multi-threading
---------------------

The build process may take a while, depending on how powerful your system is. By default, Godot's
SCons setup is configured to use all CPU threads but one (to keep the system responsive during
compilation). If the system has 4 CPU threads or fewer, it will use all threads by default.

If you want to adjust how many CPU threads SCons will use, use the ``-j<threads>``
parameter to specify how many threads will be used for the build.

Example for using 12 threads:

::

    scons -j12

Platform selection
------------------

Godot's build system will begin by detecting the platforms it can build
for. If not detected, the platform will simply not appear on the list of
available platforms. The build requirements for each platform are
described in the rest of this tutorial section.

SCons is invoked by just calling ``scons``. If no platform is specified,
SCons will detect the target platform automatically based on the host platform.
It will then start building for the target platform right away.

To list the available target platforms, use ``scons platform=list``:

.. code:: text

    scons platform=list
    scons: Reading SConscript files ...
    The following platforms are available:

        android
        ios
        linuxbsd
        macos
        web
        windows

    Please run SCons again and select a valid platform: platform=<string>

To build for a platform (for example, ``linuxbsd``), run with the ``platform=``
(or ``p=`` to make it short) argument:

::

    scons platform=linuxbsd

.. _doc_introduction_to_the_buildsystem_resulting_binary:

Resulting binary
----------------

The resulting binaries will be placed in the ``bin/`` subdirectory,
generally with this naming convention:

::

    godot.<platform>.<target>[.dev][.double].<arch>[.<extra_suffix>][.<ext>]

For the previous build attempt, the result would look like this:

.. code-block:: console

    ls bin
    bin/godot.linuxbsd.editor.x86_64

This means that the binary is for Linux *or* \*BSD (*not* both), is not optimized, has the
whole editor compiled in, and is meant for 64 bits.

A Windows binary with the same configuration will look like this:

.. code-block:: doscon

    C:\godot> dir bin/
    godot.windows.editor.64.exe

Copy that binary to any location you like, as it contains the Project Manager,
editor and all means to execute the game. However, it lacks the data to export
it to the different platforms. For that the export templates are needed (which
can be either downloaded from `godotengine.org <https://godotengine.org/>`__, or
you can build them yourself).

Aside from that, there are a few standard options that can be set in all
build targets, and which will be explained below.

.. _doc_introduction_to_the_buildsystem_target:

Target
------

The ``target`` option controls if the editor is compiled and debug flags are used.
Optimization levels (``optimize``) and whether each build contains debug symbols
(``debug_symbols``) is controlled separately from the target. Each mode means:

-  ``target=editor``: Build an editor binary (defines ``TOOLS_ENABLED`` and ``DEBUG_ENABLED``)
-  ``target=template_debug``: Build a debug export template (defines ``DEBUG_ENABLED``)
-  ``target=template_release``: Build a release export template

The editor is enabled by default in all PC targets (Linux, Windows, macOS),
disabled for everything else. Disabling the editor produces a binary that can
run projects but does not include the editor or the Project Manager.

The list of :ref:`command line arguments <doc_command_line_tutorial>`
available varies depending on the build type.

::

    scons platform=<platform> target=editor|template_debug|template_release

.. _doc_introduction_to_the_buildsystem_development_and_production_aliases:

Development and production aliases
----------------------------------

When creating builds for development (running debugging/:ref:`profiling <doc_using_cpp_profilers>`
tools), you often have different goals compared to production builds
(making binaries as fast and small as possible).

Godot provides two aliases for this purpose:

- ``dev_mode=yes`` is an alias for ``verbose=yes warnings=extra werror=yes
  tests=yes``. This enables warnings-as-errors behavior (similar to Godot's
  continuous integration setup) and also builds :ref:`unit tests
  <doc_unit_testing>` so you can run them locally.
- ``production=yes`` is an alias for ``use_static_cpp=yes debug_symbols=no
  lto=auto``. Statically linking libstdc++ allows for better binary portability
  when compiling for Linux. This alias also enables link-time optimization when
  compiling for Linux, Web and Windows with MinGW, but keeps LTO disabled when
  compiling for macOS, iOS or Windows with MSVC. This is because LTO on those
  platforms is very slow to link or has issues with the generated code.

You can manually override options from those aliases by specifying them on the
same command line with different values. For example, you can use ``scons
production=yes debug_symbols=yes`` to create production-optimized binaries with
debugging symbols included.

Dev build
---------

.. note::

    ``dev_build`` should **not** be confused with ``dev_mode``, which is an
    alias for several development-related options (see above).

When doing engine development the ``dev_build`` option can be used together
with ``target`` to enable dev-specific code. ``dev_build`` defines ``DEV_ENABLED``,
disables optimization (``-O0``/``/0d``), enables generating debug symbols, and
does not define ``NDEBUG`` (so ``assert()`` works in thirdparty libraries).

::

    scons platform=<platform> dev_build=yes

This flag appends the ``.dev`` suffix (for development) to the generated
binary name.

.. seealso::

    There are additional SCons options to enable *sanitizers*, which are tools
    you can enable at compile-time to better debug certain engine issues.
    See :ref:`doc_using_sanitizers` for more information.

.. _doc_introduction_to_the_buildsystem_debugging_symbols:

Debugging symbols
-----------------

By default, ``debug_symbols=no`` is used, which means **no** debugging symbols
are included in compiled binaries. Use ``debug_symbols=yes`` to include debug
symbols within compiled binaries, which allows debuggers and profilers to work
correctly. Debugging symbols are also required for Godot's crash stacktraces to
display with references to source code files and lines.

The downside is that debugging symbols are large files (significantly larger
than the binaries themselves). As a result, official binaries currently do not
include debugging symbols. This means you need to compile Godot yourself to have
access to debugging symbols.

When using ``debug_symbols=yes``, you can also use
``separate_debug_symbols=yes`` to put debug information in a separate file with
a ``.debug`` suffix. This allows distributing both files independently. Note
that on Windows, when compiling with MSVC, debugging information is *always*
written to a separate ``.pdb`` file regardless of ``separate_debug_symbols``.

.. tip::

    Use the ``strip <path/to/binary>`` command to remove debugging symbols from
    a binary you've already compiled.

Optimization level
------------------

Several compiler optimization levels can be chosen from:

- ``optimize=speed_trace`` *(default when targeting non-Web platforms)*: Favors
  execution speed at the cost of larger binary size. Optimizations may sometimes
  negatively impact debugger usage (stack traces may be less accurate. If this
  occurs to you, use ``optimize=debug`` instead.
- ``optimize=speed``: Favors even more execution speed, at the cost of even
  larger binary size compared to ``optimize=speed_trace``. Even less friendly to
  debugging compared to ``optimize=debug``, as this uses the most aggressive
  optimizations available.
- ``optimize=size`` *(default when targeting the Web platform)*: Favors small
  binaries at the cost of slower execution speed.
- ``optimize=size_extra``: Favors even smaller binaries, at the cost of even
  slower execution speed compared to ``optimize=size``.
- ``optimize=debug``: Only enables optimizations that do not impact debugging in
  any way. This results in faster binaries than ``optimize=none``, but slower
  binaries than ``optimize=speed_trace``.
- ``optimize=none``: Do not perform any optimization. This provides the fastest
  build times, but the slowest execution times.
- ``optimize=custom`` *(advanced users only)*: Do not pass optimization
  arguments to the C/C++ compilers. You will have to pass arguments manually
  using the ``cflags``, ``ccflags`` and ``cxxflags`` SCons options.

Architecture
------------

The ``arch`` option is meant to control the CPU or OS version intended to run the
binaries. It is focused mostly on desktop platforms and ignored everywhere
else.

Supported values for the ``arch`` option are **auto**, **x86_32**, **x86_64**,
**arm32**, **arm64**, **rv64**, **ppc32**, **ppc64** and **wasm32**.

::

    scons platform=<platform> arch={auto|x86_32|x86_64|arm32|arm64|rv64|ppc32|ppc64|wasm32}

This flag appends the value of ``arch`` to resulting binaries when
relevant.  The default value ``arch=auto`` detects the architecture
that matches the host platform.

.. _doc_buildsystem_custom_modules:

Custom modules
--------------

It's possible to compile modules residing outside of Godot's directory
tree, along with the built-in modules.

A ``custom_modules`` build option can be passed to the command line before
compiling. The option represents a comma-separated list of directory paths
containing a collection of independent C++ modules that can be seen as C++
packages, just like the built-in ``modules/`` directory.

For instance, it's possible to provide both relative, absolute, and user
directory paths containing such modules:

::

    scons custom_modules="../modules,/abs/path/to/modules,~/src/godot_modules"

.. note::

    If there's any custom module with the exact directory name as a built-in
    module, the engine will only compile the custom one. This logic can be used
    to override built-in module implementations.

.. seealso::

    :ref:`doc_custom_modules_in_cpp`

Cleaning generated files
------------------------

Sometimes, you may encounter an error due to generated files being present. You
can remove them by using ``scons --clean <options>``, where ``<options>`` is the
list of build options you've used to build Godot previously.

Alternatively, you can use ``git clean -fixd`` which will clean build artifacts
for all platforms and configurations. Beware, as this will remove all untracked
and ignored files in the repository. Don't run this command if you have
uncommitted work!

Other build options
-------------------

There are several other build options that you can use to configure the
way Godot should be built (compiler, debug options, etc.) as well as the
features to include/disable.

Check the output of ``scons --help`` for details about each option for
the version you are willing to compile.

.. _doc_overriding_build_options:

Overriding the build options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Using a file
^^^^^^^^^^^^

The default ``custom.py`` file can be created at the root of the Godot Engine
source to initialize any SCons build options passed via the command line:

.. code-block:: python
    :caption: custom.py

    optimize = "size"
    module_mono_enabled = "yes"
    use_llvm = "yes"
    extra_suffix = "game_title"

You can also disable some of the built-in modules before compiling, saving some
time it takes to build the engine. See :ref:`doc_optimizing_for_size` page for more details.

.. seealso::

    You can use the online
    `Godot build options generator <https://godot-build-options-generator.github.io/>`__
    to generate a ``custom.py`` file containing SCons options.
    You can then save this file and place it at the root of your Godot source directory.

Another custom file can be specified explicitly with the ``profile`` command
line option, both overriding the default build configuration:

.. code-block:: shell

    scons profile=path/to/custom.py

.. note:: Build options set from the file can be overridden by the command line
          options.

It's also possible to override the options conditionally:

.. code-block:: python
    :caption: custom.py

    import version

    # Override options specific for Godot 3.x and 4.x versions.
    if version.major == 3:
        pass
    elif version.major == 4:
        pass

Using the SCONSFLAGS
^^^^^^^^^^^^^^^^^^^^

``SCONSFLAGS`` is an environment variable which is used by the SCons to set the
options automatically without having to supply them via the command line.

For instance, you may want to force a number of CPU threads with the
aforementioned ``-j`` option for all future builds:

.. tabs::
 .. code-tab:: bash Linux/macOS

     export SCONSFLAGS="-j4"

 .. code-tab:: bat Windows (cmd)

     set SCONSFLAGS=-j4

 .. code-tab:: powershell Windows (PowerShell)

     $env:SCONSFLAGS="-j4"

SCU (single compilation unit) build
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Regular builds tend to be bottlenecked by including large numbers of headers
in each compilation translation unit. Primarily to speed up development (rather
than for production builds), Godot offers a "single compilation unit" build
(aka "Unity / Jumbo" build).

For the folders accelerated by this option, multiple ``.cpp`` files are
compiled in each translation unit, so headers can be shared between multiple
files, which can dramatically decrease build times.

To perform an SCU build, use the ``scu_build=yes`` SCons option.

.. note:: When developing a Pull Request using SCU builds, be sure to make a
          regular build prior to submitting the PR. This is because SCU builds
          by nature include headers from earlier ``.cpp`` files in the
          translation unit, therefore won't catch all the includes you will
          need in a regular build. The CI will catch these errors, but it will
          usually be faster to catch them on a local build on your machine.

Export templates
----------------

Official export templates are downloaded from the Godot Engine site:
`godotengine.org <https://godotengine.org/>`__. However, you might want
to build them yourself (in case you want newer ones, you are using custom
modules, or simply don't trust your own shadow).

If you download the official export templates package and unzip it, you
will notice that most files are optimized binaries or packages for each
platform:

.. code-block:: none

    android_debug.apk
    android_release.apk
    android_source.zip
    ios.zip
    linux_debug.arm32
    linux_debug.arm64
    linux_debug.x86_32
    linux_debug.x86_64
    linux_release.arm32
    linux_release.arm64
    linux_release.x86_32
    linux_release.x86_64
    macos.zip
    version.txt
    web_debug.zip
    web_dlink_debug.zip
    web_dlink_nothreads_debug.zip
    web_dlink_nothreads_release.zip
    web_dlink_release.zip
    web_nothreads_debug.zip
    web_nothreads_release.zip
    web_release.zip
    windows_debug_x86_32_console.exe
    windows_debug_x86_32.exe
    windows_debug_x86_64_console.exe
    windows_debug_x86_64.exe
    windows_debug_arm64_console.exe
    windows_debug_arm64.exe
    windows_release_x86_32_console.exe
    windows_release_x86_32.exe
    windows_release_x86_64_console.exe
    windows_release_x86_64.exe
    windows_release_arm64_console.exe
    windows_release_arm64.exe

To create those yourself, follow the instructions detailed for each
platform in this same tutorial section. Each platform explains how to
create its own template.

The ``version.txt`` file should contain the corresponding Godot version
identifier. This file is used to install export templates in a version-specific
directory to avoid conflicts. For instance, if you are building export templates
for Godot 3.1.1, ``version.txt`` should contain ``3.1.1.stable`` on the first
line (and nothing else). This version identifier is based on the ``major``,
``minor``, ``patch`` (if present) and ``status`` lines of the
`version.py file in the Godot Git repository <https://github.com/godotengine/godot/blob/master/version.py>`__.

If you are developing for multiple platforms, macOS is definitely the most
convenient host platform for cross-compilation, since you can cross-compile for
every target. Linux and Windows come in second place,
but Linux has the advantage of being the easier platform to set this up.
