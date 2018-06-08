.. _doc_gdnative_cpp_scons:

GDNative C++ Scons Overview
===========================

Introduction
------------

This tutorial builds on top of the information given in the :ref:`GDNative C++ example <doc_gdnative_cpp_example>` so we highly recommend you read that first.

The C++ compilation workflow from the basic C++ example is targeted specifically at working for that example alone. It has many assumptions and hardcoded values that prevent you from re-using the same build file for other projects.

This tutorial will instead cover recommendations for how to use scons and its various options to build GDNative C++ bindings and libraries.

By the end of this tutorial, we'll have made a fully customizable ``SConstruct`` build file that functions well for the most common use cases.

Note that in the previous tutorial, you first built a static library of the bindings by using scons within the ``godot-cpp`` directory. This tutorial will guide you through the process of building and using the *other* ``SConstruct`` file which you downloaded and used to build your dynamic library code (though ours won't be hardcoded). It will therefore assume you already have the ``godot-cpp`` repository cloned/downloaded somewhere.

If you don't really care to get a breakdown of how it works and just **want the SConstruct file now, then click here**: :download:`SConstruct <files/scons-tutorial/SConstruct>`

How To Build Shared Libraries
-----------------------------

The most important part of your scons file will be the following lines.

.. code-block:: python

    library = env.SharedLibrary(target="", source=[], LIBS=[], LIBPATH=[])
    Default(library)

Here, we are declaring that scons should build a dynamic library. We tell it the full filepath that should be given to this library (the "target" filename) and the filepaths to all of the \*.cpp files that should be included in it (the "source" array).

We also provide a list of library files to link into the dynamic library in the "LIBS" array (so the dynamic library we build may be dependent on libraries of its own, like the C++ bindings). Finally, we also specify the list of directories in which scons should search for these libraries (the "LIBPATH" array).

.. code-block:: python

    # example usage
    library = env.SharedLibrary(
        target="./libtest.dll",
        source=["./test.cpp", "./folder/test2.cpp"],
        LIBS=[libgodot-cpp.windows.debug.64.dll],
        LIBPATH=[godot-cpp/bin']
    )
    Default(library)

Here, as an example, you can see that we are building "libtest.dll" at the current directory by including our two test C++ files in various directories. We then include the godot-cpp bindings which we need to build our GDNative code.

The ``Default()`` method is an important piece as well. One can actually use scons to build multiple libraries and/or programs in sequence. In this case, however, we only need to build the one library. As such, we don't want our potential use of other build operations to trigger multiple compilations. Instead, we tell scons to default to building our shared library if we do not specify what program/library to build.

.. note::

  Handling multiple builds in sequence is, in fact, what the Godot Engine source code does. Several top-level directories build into their own static libraries, e.g. 'editor', 'modules', 'core', etc. These are then all linked together to build the final executable.

Our next step is to setup an environment which will supply the context of our build operations.

.. code-block:: python

    env = Environment()

Not so fast though! When Windows compilation is done using Visual Studio, it will require environment variables that Windows has already setup to access Visual Studio's compiler ``cl``. As such, we can ensure that scons finds the appropriate compiler for all tools by cloning the existing environment in the Windows case.

To do this, we'll need to import the ``os`` Python module (to get the OS's environment) and ``sys`` module (to determine the host operating system).

.. code-block:: python

    import os

    if sys.platform.startswith('linux'):
        host_platform = 'linux'
    elif sys.platform == 'darwin':
        host_platform = 'osx'
    elif sys.platform == 'win32':
        host_platform = 'windows'
    else:
        raise ValueError('Could not detect platform automatically, please specify with platform=<platform>')

    platform = <get 'platform' from input, default to host_platform if not provided> # will cover soon

    env = Environment()
    if platform == "windows":
        env = Environment(ENV = os.environ)

        if env['bits'] == '64':
            env['TARGET_ARCH'] = 'amd64'
        elif env['bits'] == '32':
            env['TARGET_ARCH'] = 'x86'
        else:
            print("Warning: bits argument not specified, target arch is=" + env['TARGET_ARCH'])

We start by sorting our current operating system into one of the 3 major desktop platforms using ``sys``. Now, if the user does not specify a platform, we can deduce which one it is.

If we are compiling for Windows, then we set our ``env`` to be a new ``Environment`` in which its internal environment is a copy of the operating system's environment variables.

Windows also cares about what the environment's target architecture is labeled. We update that environment value here in our virtual environment based on the input.

Input handling
--------------

So, we glossed over how we got the ``platform`` input, but it's time to dive in:

.. code-block:: python

    opts = Variables([], ARGUMENTS)
    opts.Add(name, help_text, default_value)
    unknown = tops.UnknownVariables()
    if unknown:
        print("Unknown variables:" + unknown.keys())
        Exit(1)
    opts.Update(env)
    Help(opts.GenerateHelpText(env))

Several things to see here:

ARGUMENTS is a global variable in scons that provides us with a dictionary of the arguments passed to scons.

Variables is a helper object to assist us in managing a collection of variables for our application. The first parameter provides a list of files whose variables can be recognized by the variable collection. See references to 'custom.py' in this scons docs page for reference: https://scons.org/doc/1.1.0/HTML/scons-user/x2361.html. We have also passed in our ARGUMENTS so that users can provide values from the command line.

We can use the ``Add`` method to specify a variable name to look for in our variable sources, the help text associated with it, and a default value if it cannot be found.

If the user provides an unrecognized variable, then we stop immediately. We don't want to prematuraly trigger compilations with bad settings if the user submits a typo by accident.

After we perform all of the ``Add``s we want, we need to merge the variable collection into our environment using the ``env.Update()`` method.

Lastly, we need to generate all the help text we defined for our input variables. We can define what the help text for our script is using the global ``Help`` method. Our ``opts`` then helps us to generate the string which is passed in. Now, if the user does ``scons -h``, they will see a full list of available options.

Now, let's finally show what the correct introduction of our ``platform`` variable looks like.

.. code-block:: python

    # build options, must be the same setting as used for cpp_bindings
    opts.Add(EnumVariable('platform', 'Target platform', host_platform,
                        allowed_values=('linux', 'osx', 'windows'),
                        ignorecase=2))

Whoa! That's a lot more than we bargained for! What's going on here?

Well, in addition to passing in specific name/help_text/default_value combinations, we can also pass in validation helper objects that guarantee input parameters have the structure we expect.

In this case, we are using the EnumVariable class. It supplies 2 additional parameters, ``allowed_values`` (describing what strings are permissible values) and ``ignorecase`` a flag indicating how it should handle case. 2 is the value that tells it to interpret and compare all values as lowercase.

In addition to ``platform``, two more build parameters must also be taken into account.

.. code-block:: python

    opts.Add(EnumVariable('bits', 'Target platform bits', 'default', ('default', '32', '64')))
    opts.Add(EnumVariable('target', 'Compilation target', 'debug',
                        allowed_values=('debug', 'release'),
                        ignorecase=2))

As you might expect, this gives us a 'bits' which can be default, 32, or 64, and a 'target' which can be debug or release.

While we've already covered the EnumVariable, there are several more that can be found here: https://scons.org/doc/HTML/scons-api/SCons.Variables-module.html

We will use the PathVariable and BoolVariable objects in some of the remaining parameters. We've listed the parameter categories below, including the build options we already have.

- build options
- compiler options
- output options
- bindings options
- dependency options

Let's see what these options actually look like:

.. code-block:: python
    
    # compiler options
    opts.Add(BoolVariable('use_llvm', 'Use the LLVM compiler - only effective when targeting Linux', False))
    opts.Add(BoolVariable('use_mingw', 'Use the MinGW compiler - only effective on Windows', False))
    opts.Add('std', 'The version of C++ to use. Defaults to \'c++14\'', 'c++14')

    # output options
    opts.Add('name', 'The name of the library to generate: lib<name>.extensions.', 'default')
    opts.Add(PathVariable('buildpath', 'Path to the directory where builds will go. Defaults to \'bin\'.', 'bin', PathVariable.PathIsDir))

    # bindings dependency options
    opts.Add(PathVariable('godot_cpp', 'Path to the godot-cpp bindings directory.', 'godot-cpp', PathVariable.PathIsDir))
    opts.Add(PathVariable('godot_headers', 'Path to the godot_headers bindings directory.', 'godot-cpp/godot_headers', PathVariable.PathIsDir))

    # build dependency options
    opts.Add('includes', 'Path to the directories containing header files, delimited by semi-colons, e.g. \'dir1;path1/dir2\'', '.;includes;headers')
    opts.Add('sources', 'Path to the directories containing source files, delimited by semi-colons, e.g. \'dir1;path1/dir2\'', '.;sources;source;src')
    opts.Add('libpath', 'Path to the directories containing libraries, delimited by semi-colons. Defaults to \'.;lib\'', '.;lib')
    opts.Add('libs', 'File names of libraries to link, delimited by semi-colons, e.g. \'liblinux.so;libosx.dylib;libwindows.dll;\'', '')

The BoolVariable object will convert things into Bool values for us, so '1', 'yes', 'true', and 'True' all convert to ``True`` in the Python code. Same for false values.

The PathVariable helps us guarantee that something is a file, a directory, etc. The final parameter has a number of options that can be used. See the previously linked documentation for reference.

Now to address the actual options:

The compiler options are pretty straightforward. If you are on Linux and want to use llvm instead of g++, you do ``use_llvm=yes``. If you are on Windows and want to use mingww instead of cl, you do ``use_mingw=yes``. The ``std`` parameter is for specifying a version of C++ to use. If you need newer C++17 features, for example, then you'll need ``std=c++17``.

The output options refer to where our shared library will go (``buildpath``) and what name will be in its filename ``lib<name>.<extensions>``. The extensions will be based on the platform/bits/target and must match the extensions of the C++ bindings library you link into your build.

If the user provides a path to the ``godot-cpp`` directory, then we can make some assumptions about other variables. If they don't provide one, and ``godot-cpp`` isn't in the same directory as the SConstruct file, then we will need the user to specify where we can find the godot headers. That's what ``godot_headers`` is for (as a fallback).

We then have the content parameters. Here we specify all things that our library will consist of. It needs a list of directories in which to pull in source code files (``sources``). It needs a list of include paths (``includes``) so that it knows where to look for any ``#includes`` made by the source code. It then needs a list of library file names to link into the library (``libs``) and the paths in which it should search for them (``libpath``).

Okay, let's review everything so far:

.. code-block:: python
    
    #!python

    import os, sys

    ### define input variables ###

    # Try to detect the host platform automatically
    # This is used if no `platform` argument is passed
    if sys.platform.startswith('linux'):
        host_platform = 'linux'
    elif sys.platform == 'darwin':
        host_platform = 'osx'
    elif sys.platform == 'win32':
        host_platform = 'windows'
    else:
        raise ValueError('Could not detect platform automatically, please specify with platform=<platform>')

    # Initiate option handling
    opts = Variables([], ARGUMENTS)

    # build options, must be the same setting as used for cpp_bindings
    opts.Add(EnumVariable('platform', 'Target platform', host_platform,
                        allowed_values=('linux', 'osx', 'windows'),
                        ignorecase=2))
    opts.Add(EnumVariable('bits', 'Target platform bits', 'default', ('default', '32', '64')))
    opts.Add(EnumVariable('target', 'Compilation target', 'debug',
                        allowed_values=('debug', 'release'),
                        ignorecase=2))

    # compiler options
    opts.Add(BoolVariable('use_llvm', 'Use the LLVM compiler - only effective when targeting Linux', False))
    opts.Add(BoolVariable('use_mingw', 'Use the MinGW compiler - only effective on Windows', False))
    opts.Add('std', 'The version of C++ to use. Defaults to \'c++14\'', 'c++14')

    # output options
    opts.Add('name', 'The name of the library to generate: lib<name>.extensions.', 'default')
    opts.Add(PathVariable('buildpath', 'Path to the directory where builds will go. Defaults to \'bin\'.', 'bin', PathVariable.PathIsDir))

    # bindings dependency options
    opts.Add(PathVariable('godot_cpp', 'Path to the godot-cpp bindings directory.', 'godot-cpp', PathVariable.PathIsDir))
    opts.Add(PathVariable('godot_headers', 'Path to the godot_headers bindings directory.', 'godot-cpp/godot_headers', PathVariable.PathIsDir))

    # content options
    opts.Add('includes', 'Path to the directories containing header files, delimited by semi-colons, e.g. \'dir1;path1/dir2\'', '.;includes;headers')
    opts.Add('sources', 'Path to the directories containing source files, delimited by semi-colons, e.g. \'dir1;path1/dir2\'', '.;sources;source;src')
    opts.Add('libpath', 'Path to the directories containing libraries, delimited by semi-colons. Defaults to \'.;lib\'', '.;lib')
    opts.Add('libs', 'File names of libraries to link, delimited by semi-colons, e.g. \'liblinux.so;libosx.dylib;libwindows.dll;\'', '')

    # stop if given unrecognized options
    unknown = opts.UnknownVariables()
    if unknown:
        print("Unknown variables:" + unknown.keys())
        Exit(1)

    ### define compiler and linker program + flags ###

    # This makes sure to keep the session environment variables on Windows
    # This way, you can run SCons in a Visual Studio 2017 prompt and it will find all the required tools
    if env['platform'] == 'windows':
        env = Environment(ENV = os.environ)

        if env['bits'] == '64':
            env['TARGET_ARCH'] = 'amd64'
        elif env['bits'] == '32':
            env['TARGET_ARCH'] = 'x86'
        else:
            print("Warning: bits argument not specified, target arch is=" + env['TARGET_ARCH'])
    else:
        env = Environment()

    # Regardless, bind options to a virtual environment.
    opts.Update(env)
    Help(opts.GenerateHelpText(env))

Setup compiler, compilation flags, and linker flags
---------------------------------------------------

The next segment of our build script breaks things down into each target platform and let's us decide which settings to use for compiling and linking our code. The relevant environment values here are:

- CXX: This is the name of the compiler program we will use to compile our code. Each platform has different ones available. Scons will use a platform-default one unless you manually set a different one with this variable.
- CCFLAGS: These are the compilation flags we pass into our compiler. There are many flags available for each compiler, so consult the documentation on your compiler to see which ones are available/suitable for your desired binary. The defaults used are ``g++`` for linux/osx and ``cl`` for Windows.
- LINKFLAGS: These are the linking flags we pass into our linker.

An overview of the compiler and linker options for ``g++`` can be found here: https://developers.redhat.com/blog/2018/03/21/compiler-and-linker-flags-gcc/

An overview of the compiler options for ``cl`` can be found here: https://msdn.microsoft.com/en-us/library/19z1t1wy.aspx

The linux segment is as follows:

.. code-block:: python

    if env['platform'] == 'linux':
        if env['use_llvm']:
            env['CXX'] = 'clang++'

        env.Append(CCFLAGS=['-fPIC', '-g', std, '-Wwrite-strings'])
        env.Append(LINKFLAGS=["-Wl,-R,'$$ORIGIN'"])

        if env['target'] == 'debug':
            env.Append(CCFLAGS=['-Og'])
        elif env['target'] == 'release':
            env.Append(CCFLAGS=['-O3'])

        if env['bits'] == '64':
            env.Append(CCFLAGS=['-m64'])
            env.Append(LINKFLAGS=['-m64'])
        elif env['bits'] == '32':
            env.Append(CCFLAGS=['-m32'])
            env.Append(LINKFLAGS=['-m32'])

The first thing we must do for the linux environment is update to use the llvm compiler if the user has requested it. We then establish a default set of arguments for the compiler and linker. Then we finish by settig up conditional options for them based on the given values for the target and bits architecture.

.. code-block:: python

    elif env['platform'] == 'osx':
        if env['bits'] == '32':
            raise ValueError('Only 64-bit builds are supported for the macOS target.')

        env.Append(CCFLAGS=['-g', std, '-arch', 'x86_64'])
        env.Append(LINKFLAGS=['-arch', 'x86_64', '-framework', 'Cocoa', '-Wl,-undefined,dynamic_lookup'])

        if env['target'] == 'debug':
            env.Append(CCFLAGS=['-Og'])
        elif env['target'] == 'release':
            env.Append(CCFLAGS=['-O3'])

In the Mac case, we filter out all 32-bit builds (since they aren't allowed) and then do more or less the same thing as the linux side: set up defaults and override per the given parameters.

.. code-block:: python

    elif env['platform'] == 'windows':
        if host_platform == 'windows' and not env['use_mingw']:
            # MSVC
            env.Append(LINKFLAGS=['/WX'])
            if env['target'] == 'debug':
                env.Append(CCFLAGS=['/EHsc', '/D_DEBUG', '/MDd'])
            elif env['target'] == 'release':
                env.Append(CCFLAGS=['/O2', '/EHsc', '/DNDEBUG', '/MD'])
        else:
            # MinGW
            if env['bits'] == '64':
                env['CXX'] = 'x86_64-w64-mingw32-g++'
            elif env['bits'] == '32':
                env['CXX'] = 'i686-w64-mingw32-g++'

            env.Append(CCFLAGS=['-g', '-O3', std, '-Wwrite-strings'])
            env.Append(LINKFLAGS=['--static', '-Wl,--no-undefined', '-static-libgcc', '-static-libstdc++'])

The MSVC compiler on the Windows operating system, ``cl``, will use a different set of arguments on the command line than using mingw to build for Windows with the cross-platform ``mingw``. As such, we create alternative sets of parameters based on both which compiler we use and which arguments we supply.

Prepare sources, includes, and libraries
----------------------------------------

Now we need to start breaking down how the compiler/linker will collect all of the materials they need to create our library. These requirements remain consistent regardless of whether you are building an executable program, a static library, or a dynamic library. They need...

1. a list of the individual source code files (\*.cpp, \*.c) to use.

2. a list of the directories in which to look for included, i.e. depended on, header files (\*.hpp, \*.h ).

3. a list of the library files to link into the build (\*.dll, \*.dylib, \*.so, \*.a, \*.lib).

4. a list of the directories in which to look for the library files to link.

One thing that may seem inconsistent, given the scons parameters we described earlier, is that we asked that users provide an array of source directories, rather than a list of individual files. This is because we will be *assuming* that the user wishes to include all source code files in the given list of directories.

In our case, we made each of our parameters, ``sources``, ``includes``, ``libs``, and ``libpaths``, respectively, be a semi-colon-delimited list of paths (files for ``libs``, directories for others). Here, we split the string by semi-colons to divide it up based on 

.. code-block::python

    import re

    def add_sources(p_sources, p_path):
        if not os.path.isdir(p_path):
            if p_path.endswith('.cpp') or p_path.endswith('.c'):
                p_sources.append(p_path)
        else:
            for file in os.listdir(p_path):
                if file.endswith('.cpp') or file.endswith('.c'):
                    p_sources.append(p_path + file)

    def parse_paths(p_param, p_dirs = True):
        paths = list(set(map(lambda x: x.split("\\").join("/"), re.split(';|\n', p_param))))
        if p_dirs:
            paths = list(map(lambda x: x if x[-1:] == "/" else x + "/"))
        return paths

    sources = []
    libs = parse_paths(env['libs'], False)
    src_paths = parse_paths(env['sources'])
    include_paths = parse_paths(env['includes'])
    lib_paths = parse_paths(env['libpath'])

    for a_path in src_paths:
        add_sources(sources, a_path)

First we import a built-in library for handling Regular Expressions. We then define two helper functions to parse out and format the various paths passed through our arguments and add source code files from a path. The ``parse_paths`` function keeps our internal values consistent even if the user provides an inconsistent or variable input format. Then, we finally convert the source code paths into individual source code files for pass off to the main SharedLibrary function.

``add_sources`` will iterate through the directory passed into the second argument (presumably having already passed through ``parse_paths``, so we know there is a slash at the end of it). If the file has a C++ source code extension, then we append it to the end of the path and add it as a source file.

``parse_paths`` will do the following:

1. Use RegEx to split the given string of paths into an array. This enables users to use both semi-colons and new lines to divide their paths.

2. We then map each of these individual paths against a lambda, aka an inlined function, that replaces all backslashes with forward slashes (making the Windows paths consistent with Linux/OSX paths).

3. We put this mapping through a ``set`` wrapper which guarantees that every record is unique and then re-convert it into a list.

4. If the paths are supposed to be directories, then we remap the records to guarantee that the last element of the string is a forward slash.

Auto-handling dependencies
--------------------------

Now that we've figured out how we will accept our inputs and convert them into data for our SharedLibrary function, we need to find ways to make life easier for our users, so they don't have to supply everything to us manually.

If the user provides us with a ``godot-cpp`` path (in their ``godot_cpp`` argument) or they don't but it is in the current directory, then we can use it to pre-populate include and lib paths.

What we absolutely **must** have are the Godot header files and the godot-cpp library. Either we can grab both from the ``godot-cpp`` directory (assuming one has already built the godot-cpp bindings) or the user will need to specify arguments for ``libpaths`` and ``godot_headers`` so that we can satisfy our dependencies.

The first thing we will need to do is cache whether we've found our header files. If we have a godot-cpp, then we'll assume they are in there. If we've checked for godot-cpp and we still don't have them, then we'll need the user to give them to us.

.. code-block:: python

    headers_handled = False
    godot_cpp_handled = False
    godot_cpp = env['godot_cpp']
    if os.path.isdir(godot_cpp):
        godot_cpp_handled = True
        if not godot_cpp.endswith('/'):
            godot_cpp += '/'

        godot_headers = env['godot_headers']
        if godot_headers and os.path.isdir(godot_headers):
            headers_handled = True
            if not godot_headers.endswith('/'):
                godot_headers += '/'

        header_dirs = [
            godot_headers,
            godot_cpp + 'include',
            godot_cpp + 'include/core',
            godot_cpp + 'include/gen'
        ]

        include_paths += header_dirs
        lib_paths += ['godot-cpp/bin']

    godot_headers = env['godot_headers']
    if not headers_handled and godot_headers and os.path.isdir(godot_headers):
        include_paths += [godot_headers]
    elif godot_cpp_handled:
        raise ValueError('Could not detect Godot header files in godot-cpp, please specify with godot_headers=<path>.')
    else:
        raise ValueError('Could not detect Godot header files, please specify with godot_headers=<path> or godot_cpp=<path>.')

    env.Append(CPPPATH=include_paths)

As a final measure, we also give the user the option to forego the final slash on their chosen ``buildpath``, if they do not wish to use the default ``bin/`` directory.

.. code-block:: python

    build_path = env['buildpath']
    if not build_path.endswith('/'):
        build_path += '/'

Summing up
----------

Okay, we've covered a lot of material here. The final format doesn't need to match the structure of this tutorial, so let's reorder and review things to make the script a bit more coherent:

1. Import any necessary libraries for our build operations.

2. Define helper methods that may be used later in the script.

3. Define all of the parameters that we will need for our script as well as any default values and help texts they may have. If an unrecognized variable is given, we error out.

4. Perform any final changes to our parameters, bind our parameters to a virtual environment, and generate a help string associated with the script.

5. Perform any OS-specific initializations for our compiler and linker programs (which program to use, what flags to set, etc.).

6. Parse through and format any multi-value strings in our parameters

7. Use any given parameters we can to pre-populate dependencies. Raise errors if we don't satisfy our dependencies.

8. Ensure the buildpath is a directory.

9. Declare that we wish to build the SharedLibrary.

10. Establish the SharedLibrary build operation as the default behavior for the script.

Special Operations - Visual Studio Project Generation
-----------------------------------------------------

The last thing we want to address is for Windows users to be able to generate a Visual Studio project solution since many Windows devs rely on it.

Scons has another built-in method for doing this, similar to the ``SharedLibrary()`` method, called ``MSVSProject()``. It's syntax looks like this (taken from the scons documentation):

.. code-block:: python

    #!python

    barsrcs = ['bar.cpp']
    barincs = ['bar.h']
    barlocalincs = ['StdAfx.h']
    barresources = ['bar.rc','resource.h']
    barmisc = ['bar_readme.txt']

    dll = env.SharedLibrary(target = 'bar.dll', source = barsrcs)

    env.MSVSProject(
        target = 'Bar' + env['MSVSPROJECTSUFFIX'], srcs = barsrcs,
        incs = barincs,
        localincs = barlocalincs,
        resources = barresources,
        misc = barmisc,
        buildtarget = dll,
        variant = 'Release')

Now, this process can become very complicated, very quickly, so if you're interested in understanding how this is broken down, then follow along. Otherwise, you might as well skip past this section.

.. note:

    For those who are privy to Godot Engine's compilation, the ``vsproj`` and ``num_jobs`` parameters are identical to and serve the same purpose as the similarly named parameters for Godot Engine's main ``SConstruct`` file that builds the engine itself.

.. code-block:: python

    #!python

    # the name of our output library. We'll use this to define the name of our solution file
    lib_name = ARGUMENTS.get("name", "libdefault")

    # Whether or not we will even generate a Visual Studio project
    vsproj = ARGUMENTS.get("vsproj", "no")

    # The number of processes we'll use to aggregate files into our Visual Studio project.
    num_jobs = ARGUMENTS.get("num_jobs", 1)

    if vsproj == "yes":
        env.vs_incs = []
        env.vs_srcs = []

        def AddToVSProject(sources):
            for x in sources:
                if type(x) == type(""):
                    fname = env.File(x).path
                else:
                    fname = env.File(x)[0].path
                pieces = fname.split(".")
                if len(pieces) > 0:
                    basename = pieces[0]
                    basename = basename.replace('\\\\', '/')
                    if os.path.isfile(basename + ".h"):
                        env.vs_incs = env.vs_incs + [basename + ".h"]
                    elif os.path.isfile(basename + ".hpp"):
                        env.vs_incs = env.vs_incs + [basename + ".hpp"]
                    if os.path.isfile(basename + ".c"):
                        env.vs_srcs = env.vs_srcs + [basename + ".c"]
                    elif os.path.isfile(basename + ".cpp"):
                        env.vs_srcs = env.vs_srcs + [basename + ".cpp"]

        def build_commandline(commands):
            common_build_prefix = ['cmd /V /C set "plat=$(PlatformTarget)"',
                                    '(if "$(PlatformTarget)"=="x64" (set "plat=x86_amd64"))',
                                    'call "' + batch_file + '" !plat!']

            result = " ^& ".join(common_build_prefix + [commands])
            # print("Building commandline: ", result)
            return result

        def find_visual_c_batch_file(env):
            from  SCons.Tool.MSCommon.vc import get_default_version, get_host_target, find_batch_file

            version = get_default_version(env)
            (host_platform, target_platform, req_target_platform) = get_host_target(env)
            return find_batch_file(env, version, host_platform, target_platform)[0]

        env.AddToVSProject = AddToVSProject
        env.build_commandline = build_commandline

        env['CPPPATH'] = [Dir(path) for path in env['CPPPATH']]

        batch_file = find_visual_c_batch_file(env)
        if batch_file:
            env.AddToVSProject(source_files)

            # windows allows us to have spaces in paths, so we need
            # to double quote off the directory. However, the path ends
            # in a backslash, so we need to remove this, lest it escape the
            # last double quote off, confusing MSBuild
            env['MSVSBUILDCOM'] = build_commandline('scons --directory="$(ProjectDir.TrimEnd(\'\\\'))" platform=windows target=$(Configuration) -j' + str(num_jobs))
            env['MSVSREBUILDCOM'] = build_commandline('scons --directory="$(ProjectDir.TrimEnd(\'\\\'))" platform=windows target=$(Configuration) vsproj=yes -j' + str(num_jobs))
            env['MSVSCLEANCOM'] = build_commandline('scons --directory="$(ProjectDir.TrimEnd(\'\\\'))" --clean platform=windows target=$(Configuration) -j' + str(num_jobs))

            # This version information (Win32, x64, Debug, Release, Release_Debug seems to be
            # required for Visual Studio to understand that it needs to generate an NMAKE
            # project. Do not modify without knowing what you are doing.
            debug_variants = ['debug|Win32'] + ['debug|x64']
            release_variants = ['release|Win32'] + ['release|x64']
            release_debug_variants = ['release_debug|Win32'] + ['release_debug|x64']
            variants = debug_variants + release_variants + release_debug_variants

            # Sets up output executable names for each variant. The ordering of the final 'targets' array should match that of the final 'variants' array.

            target_name = 'bin\\' + lib_name + '.windows.'

            debug_targets = [target_name + 'tools.32.' + dl_suffix] + [target_name + 'tools.64.' + dl_suffix]
            release_targets = [target_name + 'opt.32.' + dl_suffix] + [target_name + 'opt.64.' + dl_suffix]
            release_debug_targets = [target_name + 'opt.tools.32.' + dl_suffix] + [target_name + 'opt.tools.64.' + dl_suffix]
            targets = debug_targets + release_targets + release_debug_targets

            msvproj = env.MSVSProject(target=['#' + lib_name + env['MSVSPROJECTSUFFIX']],
                                        incs=env.vs_incs,
                                        srcs=env.vs_srcs,
                                        runfile=targets,
                                        buildtarget=library, #recall that 'library' is the result of our 'env.SharedLibrary()' method call
                                        auto_build_solution=1,
                                        variant=variants)

        # handle cpp hint file
        if os.path.isfile(filename):
            # Don't overwrite an existing hint file since the user may have customized it.
            pass
        else:
            try:
                fd = open(filename, "w")
                fd.write("#define GDCLASS(m_class, m_inherits)\n")
            except IOError:
                print("Could not write cpp.hint file.")

Okay, this entire section looks incredibly complicated. Some parts of it are verbose, but ultimately simple. We'll break things down.

The first thing we do is grab our relevant parameters. One you'll recognize as the ``lib_name`` which we are using to decide on the name of our output dynamic library. In this case, we are doubling up the use of this name to also give a name to our generated solution file. The ``vsproj`` parameter, when equal to "yes", is just a flag to trigger all of this behavior. Finally, we get ``num_jobs``. This is a value that will enable us to rely on multithreading to build up our solution file, in case our dynamic library happens to be building from an exceptionally large set of files.

After grabbing our parameters and checking for the ``vsproj`` flag, we declare two arrays in our environment: one each for the *.cpp and *.h files we intend to include in our VS Project.

Then we declare a set of utility methods. ``AddToVSProject`` just does some parsing of filepath structure to make sure that files have the right extension, before adding them to the two arrays. The ``build_commandline`` method does some contextual preparation for each build command specific to Visual Studio. Finally, we get the ``find_visual_c_batch_file`` method that locates the batch file used to initialize Visual Studio Compiler access. For more details, visit the ``find_batch_file`` source code here: https://scons.org/sphinx_wip/_modules/SCons/Tool/MSCommon/vc.html

With the declarations all out of the way, we add the methods to our ``Environment`` for later use by the ``build_commandline`` method and re-assert that all directories in our CPPPATH are indeed SCons Directory objects.

If we look for the Visual Studio batch file and find one, then it means we'll be capable of building a VS Project, so we proceed.

In the if-statement section, there are 4 things happening.

1. We first add the C++ code files we've collected to our respective header and source file directories by calling AddToVSProject.

2. We then define what command line operations to execute when users attempt to build, rebuild, or clean their VS Project. In these lines, you can clearly see us redefining these operations to use scons instead. This is also where you see the ``num_jobs`` parameter come into play, passing the "-j" + number of threads value at the end.

3. We define the set of platform and target combinations that will be available to the project as well as what resulting dynamic library they will each produce.

4. We go ahead and build the VS Project.

After having built the project, we top things off by building a simple C++ hint file that gives the compiler some extra definitions of C++ content for IntelliSense assistance.

In order to integrate this content, we place this content after our created ``library`` variable. We must also amend our OS-specific logic to include a determination of the appropriate dynamic library extension for the ``dl_suffix`` variable.

Conclusion
----------

And there you have it! That is the entire process. Below is the full ``SConstruct`` file that integrates all of the information we have covered.

Note that, because the Visual Studio Project Generation requires the header files to explicitly be supplied separately from the source files, we create analogous utilities to acquire those files as well.

This tutorial will likely evolve over time as more platforms are adapted into it, but it should at least get people started.

Here is a list of parameters and usage examples available for this build file. If you would like to learn more about developing your own ``SConstruct`` build file, I recommend you check out the official SCons User Guide here: https://scons.org/doc/production/PDF/scons-user.pdf

===================== ======== ================================= ================================= ==============================================
Name                  Required Default                           Format                            Description
--------------------- -------- --------------------------------- --------------------------------- ----------------------------------------------
platform              yes      "windows"                         "windows"|"linux"|"osx"           The targeted platform.
target                no       "debug"                           "debug"|"release"|"debug_release" The targeted release version.
bits                  no       64                                32|64                             The targeted bit version.
name                  no       "libdefault"                      any string                        The first portion of the library name.
lib                   no       "bin/"                            Directory Path                    The output directory.
headers               no       "godot_headers/"                  Directory Path                    The location of the godot_headers directory.
cpp_bindings_path     no       "godot-cpp/"                      Directory Path                    The location of the godot-cpp directory.
cpp_bindings_library  no       "godot-cpp/bin/godot-cpp"         Directory Path + bindings libname The location and name of the cpp bindings lib.
sources               no       "" ("." and "src/" auto-included) "DirPath,DirPath,..."             Additional source directories to include.
other_libs            no       ""                                "FilePath,FilePath,..."           Additional lib files to include.
vsproj                no       "no"                              "yes"|"no"                        Whether to generate a VS Project Solution.
num_jobs              no       1                                 Integer                           For 'vsproj', the number of threads to use.

==================================================================================================================================================

.. code-block:: python

    #!python
    import os

    ### utility method definitions ###

    def add_sources(sources, directory):
        for file in os.listdir(directory):
            if file.endswith('.cpp') or file.endswith('.c'):
                sources.append(directory + '/' + file)

    def add_headers(headers, directory):
        for file in os.listdir(directory):
            if file.endswith('.hpp') or file.endswith('.h'):
                headers.append(directory + '/' + file)

    ### output lib preparation ###

    target = ARGUMENTS.get("target", "debug")
    platform = ARGUMENTS.get("platform", "windows")
    bits = ARGUMENTS.get("bits", 64)
    lib_name = ARGUMENTS.get("name", "libdefault")

    library_file = lib_name + "." + platform + "." + str(bits)

    lib_path = ARGUMENTS.get("lib", "bin/")

    lib_path = lib_path.split("\\").join("/")
    if lib_path[-1:] != "/":
        lib_path += "/"

    ### library dependencies ###

    cpp_bindings_library_path = ARGUMENTS.get("cpp_bindings_library", "godot-cpp/bin/godot-cpp")

    ext = "z"
    while ext != "":
        cpp_bindings_library_path, ext = os.path.splitext(cpp_bindings_library_path)

    cpp_bindings_library = cpp_bindings_library_path + "." + platform + "." + str(bits)

    other_libs = ARGUMENTS.get("other_libs", "")
    other_libs = other_libs.split(",")

    libs = [cpp_bindings_library] + other_libs

    ### source dependencies ###

    godot_headers_path = ARGUMENTS.get("headers", "godot_headers/")
    cpp_bindings_path = ARGUMENTS.get("cpp_bindings_path", "godot-cpp/")
    sources = ARGUMENTS.get("sources", "")

    source_files = []
    header_files = []

    source_dirs = sources.split(",")

    for path in source_dirs:
        if os.path.isdir(path):
            add_sources(source_files, path)
            add_headers(header_files, path)

    source_dirs.append(godot_headers_path)
    source_dirs.append(cpp_bindings_path + "include/")
    source_dirs.append(cpp_bindings_path + "include/core/")

    ### OS-specific logic for flags and the output lib directory ###

    platform_dir = ""
    dl_suffix = ""

    if platform == "osx":
        env.Append(CCFLAGS = ['-g','-O3', '-arch', 'x86_64'])
        env.Append(LINKFLAGS = ['-arch', 'x86_64'])

        platform_dir = "osx"
        dl_suffix = "dylib"
    
    elif platform == "linux":
        env.Append(CCFLAGS = ['-fPIC', '-g','-O3', '-std=c++14'])

        platform_dir = "x11"
        dl_suffix = "so"
    
    elif platform == "windows":

        # Set exception handling model to avoid warnings caused by Windows system headers.
        env.Append(CCFLAGS=['-EHsc'])

        if target == "debug":
            env.Append(CCFLAGS = ['-D_DEBUG', '-MDd'])
        else:
            env.Append(CCFLAGS = ['-O2', '-DNDEBUG', '-MD'])

        platform_dir = "win"
        dl_suffix = "dll"

    else:
        # do nothing if we don't recognize the platform
        print 'unrecognized platform provided. Please enter a valid platform.'
        return

    final_lib_path = lib_path + platform_dir + str(bits) + "/" + lib_name

    env.Append(LIBS=libs)
    env.Append(CPPPATH=source_dirs)

    if ARGUMENTS.get("use_llvm", "no") == "yes":
        env["CXX"] = "clang++"
    
    library = env.SharedLibrary(target=final_lib_path, source=source_files)
    Default(library)

    ### VS Project Generation ###

    vsproj = ARGUMENTS.get("vsproj", "no")
    num_jobs = ARGUMENTS.get("num_jobs", 1)

    if vsproj == "yes":
        env.vs_incs = []
        env.vs_srcs = []

        def AddToVSProject(sources):
            for x in sources:
                if type(x) == type(""):
                    fname = env.File(x).path
                else:
                    fname = env.File(x)[0].path
                pieces = fname.split(".")
                if len(pieces) > 0:
                    basename = pieces[0]
                    basename = basename.replace('\\\\', '/')
                    if os.path.isfile(basename + ".h"):
                        env.vs_incs = env.vs_incs + [basename + ".h"]
                    elif os.path.isfile(basename + ".hpp"):
                        env.vs_incs = env.vs_incs + [basename + ".hpp"]
                    if os.path.isfile(basename + ".c"):
                        env.vs_srcs = env.vs_srcs + [basename + ".c"]
                    elif os.path.isfile(basename + ".cpp"):
                        env.vs_srcs = env.vs_srcs + [basename + ".cpp"]

        def build_commandline(commands):
            common_build_prefix = ['cmd /V /C set "plat=$(PlatformTarget)"',
                                    '(if "$(PlatformTarget)"=="x64" (set "plat=x86_amd64"))',
                                    'call "' + batch_file + '" !plat!']

            result = " ^& ".join(common_build_prefix + [commands])
            # print("Building commandline: ", result)
            return result

        def find_visual_c_batch_file(env):
            from  SCons.Tool.MSCommon.vc import get_default_version, get_host_target, find_batch_file

            version = get_default_version(env)
            (host_platform, target_platform, req_target_platform) = get_host_target(env)
            return find_batch_file(env, version, host_platform, target_platform)[0]

        env.AddToVSProject = AddToVSProject
        env.build_commandline = build_commandline

        env['CPPPATH'] = [Dir(path) for path in env['CPPPATH']]

        batch_file = find_visual_c_batch_file(env)
        if batch_file:
            env.AddToVSProject(source_files)
            env.AddToVSProject(header_files)

            # windows allows us to have spaces in paths, so we need
            # to double quote off the directory. However, the path ends
            # in a backslash, so we need to remove this, lest it escape the
            # last double quote off, confusing MSBuild
            env['MSVSBUILDCOM'] = build_commandline('scons --directory="$(ProjectDir.TrimEnd(\'\\\'))" platform=windows target=$(Configuration) -j' + str(num_jobs))
            env['MSVSREBUILDCOM'] = build_commandline('scons --directory="$(ProjectDir.TrimEnd(\'\\\'))" platform=windows target=$(Configuration) vsproj=yes -j' + str(num_jobs))
            env['MSVSCLEANCOM'] = build_commandline('scons --directory="$(ProjectDir.TrimEnd(\'\\\'))" --clean platform=windows target=$(Configuration) -j' + str(num_jobs))

            # This version information (Win32, x64, Debug, Release, Release_Debug seems to be
            # required for Visual Studio to understand that it needs to generate an NMAKE
            # project. Do not modify without knowing what you are doing.
            debug_variants = ['debug|Win32'] + ['debug|x64']
            release_variants = ['release|Win32'] + ['release|x64']
            release_debug_variants = ['release_debug|Win32'] + ['release_debug|x64']
            variants = debug_variants + release_variants + release_debug_variants

            # Sets up output executable names for each variant. The ordering of the final 'targets' array should match that of the final 'variants' array.

            target_name = 'bin\\' + lib_name + '.windows.'

            debug_targets = [target_name + 'tools.32.' + dl_suffix] + [target_name + 'tools.64.' + dl_suffix]
            release_targets = [target_name + 'opt.32.' + dl_suffix] + [target_name + 'opt.64.' + dl_suffix]
            release_debug_targets = [target_name + 'opt.tools.32.' + dl_suffix] + [target_name + 'opt.tools.64.' + dl_suffix]
            targets = debug_targets + release_targets + release_debug_targets

            msvproj = env.MSVSProject(target=['#' + lib_name + env['MSVSPROJECTSUFFIX']],
                                        incs=env.vs_incs,
                                        srcs=env.vs_srcs,
                                        runfile=targets,
                                        buildtarget=library, #recall that 'library' is the result of our 'env.SharedLibrary()' method call
                                        auto_build_solution=1,
                                        variant=variants)

        # handle cpp hint file
        if os.path.isfile(filename):
            # Don't overwrite an existing hint file since the user may have customized it.
            pass
        else:
            try:
                fd = open(filename, "w")
                fd.write("#define GDCLASS(m_class, m_inherits)\n")
            except IOError:
                print("Could not write cpp.hint file.")

