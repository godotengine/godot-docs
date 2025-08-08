.. _doc_custom_modules_in_cpp:

Custom modules in C++
=====================

Modules
-------

Godot allows extending the engine in a modular way. New modules can be
created and then enabled/disabled. This allows for adding new engine
functionality at every level without modifying the core, which can be
split for use and reuse in different modules.

Modules are located in the ``modules/`` subdirectory of the build system.
By default, dozens of modules are enabled, such as GDScript (which, yes,
is not part of the base engine), the Mono runtime, a regular expressions
module, and others. As many new modules as desired can be
created and combined. The SCons build system will take care of it
transparently.

What for?
---------

While it's recommended that most of a game be written in scripting (as
it is an enormous time saver), it's perfectly possible to use C++
instead. Adding C++ modules can be useful in the following scenarios:

-  Binding an external library to Godot (like PhysX, FMOD, etc).
-  Optimize critical parts of a game.
-  Adding new functionality to the engine and/or editor.
-  Porting an existing game to Godot.
-  Write a whole, new game in C++ because you can't live without C++.

Creating a new module
---------------------

Before creating a module, make sure to :ref:`download the source code of Godot
and compile it <toc-devel-compiling>`.

To create a new module, the first step is creating a directory inside
``modules/``. If you want to maintain the module separately, you can checkout
a different VCS into modules and use it.

The example module will be called "summator" (``godot/modules/summator``).
Inside we will create a summator class:

.. code-block:: cpp
    :caption: godot/modules/summator/summator.h

    #pragma once

    #include "core/object/ref_counted.h"

    class Summator : public RefCounted {
        GDCLASS(Summator, RefCounted);

        int count;

    protected:
        static void _bind_methods();

    public:
        void add(int p_value);
        void reset();
        int get_total() const;

        Summator();
    };

And then the cpp file.

.. code-block:: cpp
    :caption: godot/modules/summator/summator.cpp

    #include "summator.h"

    void Summator::add(int p_value) {
        count += p_value;
    }

    void Summator::reset() {
        count = 0;
    }

    int Summator::get_total() const {
        return count;
    }

    void Summator::_bind_methods() {
        ClassDB::bind_method(D_METHOD("add", "value"), &Summator::add);
        ClassDB::bind_method(D_METHOD("reset"), &Summator::reset);
        ClassDB::bind_method(D_METHOD("get_total"), &Summator::get_total);
    }

    Summator::Summator() {
        count = 0;
    }

Then, the new class needs to be registered somehow, so two more files
need to be created:

.. code-block:: none

    register_types.h
    register_types.cpp

.. important::
    These files must be in the top-level folder of your module (next to your
    ``SCsub`` and ``config.py`` files) for the module to be registered properly.

These files should contain the following:

.. code-block:: cpp
    :caption: godot/modules/summator/register_types.h

    #include "modules/register_module_types.h"

    void initialize_summator_module(ModuleInitializationLevel p_level);
    void uninitialize_summator_module(ModuleInitializationLevel p_level);
    /* yes, the word in the middle must be the same as the module folder name */

.. code-block:: cpp
    :caption: godot/modules/summator/register_types.cpp

    #include "register_types.h"

    #include "core/object/class_db.h"
    #include "summator.h"

    void initialize_summator_module(ModuleInitializationLevel p_level) {
        if (p_level != MODULE_INITIALIZATION_LEVEL_SCENE) {
            return;
        }
        ClassDB::register_class<Summator>();
    }

    void uninitialize_summator_module(ModuleInitializationLevel p_level) {
        if (p_level != MODULE_INITIALIZATION_LEVEL_SCENE) {
            return;
        }
       // Nothing to do here in this example.
    }

Next, we need to create an ``SCsub`` file so the build system compiles
this module:

.. code-block:: python
    :caption: godot/modules/summator/SCsub

    # SCsub

    Import('env')

    env.add_source_files(env.modules_sources, "*.cpp") # Add all cpp files to the build

With multiple sources, you can also add each file individually to a Python
string list:

.. code-block:: python

    src_list = ["summator.cpp", "other.cpp", "etc.cpp"]
    env.add_source_files(env.modules_sources, src_list)

This allows for powerful possibilities using Python to construct the file list
using loops and logic statements. Look at some modules that ship with Godot by
default for examples.

To add include directories for the compiler to look at you can append it to the
environment's paths:

.. code-block:: python

    env.Append(CPPPATH=["mylib/include"]) # this is a relative path
    env.Append(CPPPATH=["#myotherlib/include"]) # this is an 'absolute' path

If you want to add custom compiler flags when building your module, you need to clone
``env`` first, so it won't add those flags to whole Godot build (which can cause errors).
Example ``SCsub`` with custom flags:

.. code-block:: python
    :caption: godot/modules/summator/SCsub

    Import('env')

    module_env = env.Clone()
    module_env.add_source_files(env.modules_sources, "*.cpp")
    # Append CCFLAGS flags for both C and C++ code.
    module_env.Append(CCFLAGS=['-O2'])
    # If you need to, you can:
    # - Append CFLAGS for C code only.
    # - Append CXXFLAGS for C++ code only.

And finally, the configuration file for the module, this is a
Python script that must be named ``config.py``:

.. code-block:: python
    :caption: godot/modules/summator/config.py

    # config.py

    def can_build(env, platform):
        return True

    def configure(env):
        pass

The module is asked if it's OK to build for the specific platform (in
this case, ``True`` means it will build for every platform).

And that's it. Hope it was not too complex! Your module should look like
this:

.. code-block:: none

    godot/modules/summator/config.py
    godot/modules/summator/summator.h
    godot/modules/summator/summator.cpp
    godot/modules/summator/register_types.h
    godot/modules/summator/register_types.cpp
    godot/modules/summator/SCsub

You can then zip it and share the module with everyone else. When
building for every platform (instructions in the previous sections),
your module will be included.

Using the module
----------------

You can now use your newly created module from any script:

.. tabs::
 .. code-tab:: gdscript GDScript

    var s = Summator.new()
    s.add(10)
    s.add(20)
    s.add(30)
    print(s.get_total())
    s.reset()

The output will be ``60``.

.. seealso:: The previous Summator example is great for small, custom modules,
  but what if you want to use a larger, external library? Refer to
  :ref:`doc_binding_to_external_libraries` for details about binding to
  external libraries.

.. warning:: If your module is meant to be accessed from the running project
             (not just from the editor), you must also recompile every export
             template you plan to use, then specify the path to the custom
             template in each export preset. Otherwise, you'll get errors when
             running the project as the module isn't compiled in the export
             template. See the :ref:`Compiling <toc-devel-compiling>` pages
             for more information.

Compiling a module externally
-----------------------------

Compiling a module involves moving the module's sources directly under the
engine's ``modules/`` directory. While this is the most straightforward way to
compile a module, there are a couple of reasons as to why this might not be a
practical thing to do:

1. Having to manually copy modules sources every time you want to compile the
   engine with or without the module, or taking additional steps needed to
   manually disable a module during compilation with a build option similar to
   ``module_summator_enabled=no``. Creating symbolic links may also be a solution,
   but you may additionally need to overcome OS restrictions like needing the
   symbolic link privilege if doing this via script.

2. Depending on whether you have to work with the engine's source code, the
   module files added directly to ``modules/`` changes the working tree to the
   point where using a VCS (like ``git``) proves to be cumbersome as you need to
   make sure that only the engine-related code is committed by filtering
   changes.

So if you feel like the independent structure of custom modules is needed, lets
take our "summator" module and move it to the engine's parent directory:

.. code-block:: shell

    mkdir ../modules
    mv modules/summator ../modules

Compile the engine with our module by providing ``custom_modules`` build option
which accepts a comma-separated list of directory paths containing custom C++
modules, similar to the following:

.. code-block:: shell

    scons custom_modules=../modules

The build system shall detect all modules under the ``../modules`` directory
and compile them accordingly, including our "summator" module.

.. warning::

    Any path passed to ``custom_modules`` will be converted to an absolute path
    internally as a way to distinguish between custom and built-in modules. It
    means that things like generating module documentation may rely on a
    specific path structure on your machine.

.. seealso::

    :ref:`Introduction to the buildsystem - Custom modules build option <doc_buildsystem_custom_modules>`.

Customizing module types initialization
---------------------------------------

Modules can interact with other built-in engine classes during runtime and even
affect the way core types are initialized. So far, we've been using
``register_summator_types`` as a way to bring in module classes to be available
within the engine.

A crude order of the engine setup can be summarized as a list of the following
type registration methods:

.. code-block:: cpp

    preregister_module_types();
    preregister_server_types();
    register_core_singletons();
    register_server_types();
    register_scene_types();
    EditorNode::register_editor_types();
    register_platform_apis();
    register_module_types();
    initialize_physics();
    initialize_navigation_server();
    register_server_singletons();
    register_driver_types();
    ScriptServer::init_languages();

Our ``Summator`` class is initialized during the ``register_module_types()``
call. Imagine that we need to satisfy some common module runtime dependency
(like singletons), or allow us to override existing engine method callbacks
before they can be assigned by the engine itself. In that case, we want to
ensure that our module classes are registered *before* any other built-in type.

This is where we can define an optional ``preregister_summator_types()``
method which will be called before anything else during the
``preregister_module_types()`` engine setup stage.

We now need to add this method to ``register_types`` header and source files:

.. code-block:: cpp
    :caption: godot/modules/summator/register_types.h

    #define MODULE_SUMMATOR_HAS_PREREGISTER
    void preregister_summator_types();

    void register_summator_types();
    void unregister_summator_types();

.. note:: Unlike other register methods, we have to explicitly define
          ``MODULE_SUMMATOR_HAS_PREREGISTER`` to let the build system know what
          relevant method calls to include at compile time. The module's name
          has to be converted to uppercase as well.

.. code-block:: cpp
    :caption: godot/modules/summator/register_types.cpp

    #include "register_types.h"

    #include "core/object/class_db.h"
    #include "summator.h"

    void preregister_summator_types() {
        // Called before any other core types are registered.
        // Nothing to do here in this example.
    }

    void register_summator_types() {
        ClassDB::register_class<Summator>();
    }

    void unregister_summator_types() {
       // Nothing to do here in this example.
    }

Improving the build system for development
------------------------------------------

.. warning::

    This shared library support is not designed to support distributing a module
    to other users without recompiling the engine. For that purpose, use
    a GDExtension instead.

So far, we defined a clean SCsub that allows us to add the sources
of our new module as part of the Godot binary.

This static approach is fine when we want to build a release version of our
game, given we want all the modules in a single binary.

However, the trade-off is that every single change requires a full recompilation of the
game. Even though SCons is able to detect and recompile only the file that was
changed, finding such files and eventually linking the final binary takes a long time.

The solution to avoid such a cost is to build our own module as a shared
library that will be dynamically loaded when starting our game's binary.

.. code-block:: python
    :caption: godot/modules/summator/SCsub

    Import('env')

    sources = [
        "register_types.cpp",
        "summator.cpp"
    ]

    # First, create a custom env for the shared library.
    module_env = env.Clone()

    # Position-independent code is required for a shared library.
    module_env.Append(CCFLAGS=['-fPIC'])

    # Don't inject Godot's dependencies into our shared library.
    module_env['LIBS'] = []

    # Define the shared library. By default, it would be built in the module's
    # folder, however it's better to output it into `bin` next to the
    # Godot binary.
    shared_lib = module_env.SharedLibrary(target='#bin/summator', source=sources)

    # Finally, notify the main build environment it now has our shared library
    # as a new dependency.

    # LIBPATH and LIBS need to be set on the real "env" (not the clone)
    # to link the specified libraries to the Godot executable.

    env.Append(LIBPATH=['#bin'])

    # SCons wants the name of the library with it custom suffixes
    # (e.g. ".linuxbsd.tools.64") but without the final ".so".
    shared_lib_shim = shared_lib[0].name.rsplit('.', 1)[0]
    env.Append(LIBS=[shared_lib_shim])

Once compiled, we should end up with a ``bin`` directory containing both the
``godot*`` binary and our ``libsummator*.so``. However given the .so is not in
a standard directory (like ``/usr/lib``), we have to help our binary find it
during runtime with the ``LD_LIBRARY_PATH`` environment variable:

.. code-block:: shell

    export LD_LIBRARY_PATH="$PWD/bin/"
    ./bin/godot*

.. note::
  You have to ``export`` the environment variable. Otherwise,
  you won't be able to run your project from the editor.

On top of that, it would be nice to be able to select whether to compile our
module as shared library (for development) or as a part of the Godot binary
(for release). To do that we can define a custom flag to be passed to SCons
using the ``ARGUMENT`` command:

.. code-block:: python
    :caption: godot/modules/summator/SCsub

    Import('env')

    sources = [
        "register_types.cpp",
        "summator.cpp"
    ]

    module_env = env.Clone()
    module_env.Append(CCFLAGS=['-O2'])

    if ARGUMENTS.get('summator_shared', 'no') == 'yes':
        # Shared lib compilation
        module_env.Append(CCFLAGS=['-fPIC'])
        module_env['LIBS'] = []
        shared_lib = module_env.SharedLibrary(target='#bin/summator', source=sources)
        shared_lib_shim = shared_lib[0].name.rsplit('.', 1)[0]
        env.Append(LIBS=[shared_lib_shim])
        env.Append(LIBPATH=['#bin'])
    else:
        # Static compilation
        module_env.add_source_files(env.modules_sources, sources)

Now by default ``scons`` command will build our module as part of Godot's binary
and as a shared library when passing ``summator_shared=yes``.

Finally, you can even speed up the build further by explicitly specifying your
shared module as target in the SCons command:

.. code-block:: shell

    scons summator_shared=yes platform=linuxbsd bin/libsummator.linuxbsd.tools.64.so

Writing custom documentation
----------------------------

Writing documentation may seem like a boring task, but it is highly recommended
to document your newly created module to make it easier for users to benefit
from it. Not to mention that the code you've written one year ago may become
indistinguishable from the code that was written by someone else, so be kind to
your future self!

There are several steps in order to setup custom docs for the module:

1. Make a new directory in the root of the module. The directory name can be
   anything, but we'll be using the ``doc_classes`` name throughout this section.

2. Now, we need to edit ``config.py``, add the following snippet:

   .. code-block:: python

        def get_doc_path():
            return "doc_classes"

        def get_doc_classes():
            return [
                "Summator",
            ]

The ``get_doc_path()`` function is used by the build system to determine
the location of the docs. In this case, they will be located in the
``modules/summator/doc_classes`` directory. If you don't define this,
the doc path for your module will fall back to the main ``doc/classes``
directory.

The ``get_doc_classes()`` method is necessary for the build system to
know which registered classes belong to the module. You need to list all of your
classes here. The classes that you don't list will end up in the
main ``doc/classes`` directory.

.. tip::

    You can use Git to check if you have missed some of your classes by checking the
    untracked files with ``git status``. For example:

    ::

        git status

    Example output:

    ::

        Untracked files:
            (use "git add <file>..." to include in what will be committed)

            doc/classes/MyClass2D.xml
            doc/classes/MyClass4D.xml
            doc/classes/MyClass5D.xml
            doc/classes/MyClass6D.xml
            ...


3. Now we can generate the documentation:

We can do this via running Godot's doctool i.e. ``godot --doctool <path>``,
which will dump the engine API reference to the given ``<path>`` in XML format.

In our case we'll point it to the root of the cloned repository. You can point it
to an another folder, and just copy over the files that you need.

Run command:

::

    bin/<godot_binary> --doctool .

Now if you go to the ``godot/modules/summator/doc_classes`` folder, you will see
that it contains a ``Summator.xml`` file, or any other classes, that you referenced
in your ``get_doc_classes`` function.

Edit the file(s) following the `class reference primer <https://contributing.godotengine.org/en/latest/documentation/class_reference/class_reference_primer.html>`__ and recompile the engine.

Once the compilation process is finished, the docs will become accessible within
the engine's built-in documentation system.

In order to keep documentation up-to-date, all you'll have to do is simply modify
one of the XML files and recompile the engine from now on.

If you change your module's API, you can also re-extract the docs, they will contain
the things that you previously added. Of course if you point it to your godot
folder, make sure you don't lose work by extracting older docs from an older engine build
on top of the newer ones.

Note that if you don't have write access rights to your supplied ``<path>``,
you might encounter an error similar to the following:

.. code-block:: console

    ERROR: Can't write doc file: docs/doc/classes/@GDScript.xml
       At: editor/doc/doc_data.cpp:956

.. _doc_custom_module_unit_tests:

Writing custom unit tests
-------------------------

It's possible to write self-contained unit tests as part of a C++ module. If you
are not familiar with the unit testing process in Godot yet, please refer to
:ref:`doc_unit_testing`.

The procedure is the following:

1. Create a new directory named ``tests/`` under your module's root:

.. code-block:: console

    cd modules/summator
    mkdir tests
    cd tests

2. Create a new test suite: ``test_summator.h``. The header must be prefixed
   with ``test_`` so that the build system can collect it and include it as part
   of the ``tests/test_main.cpp`` where the tests are run.

3. Write some test cases. Here's an example:

.. code-block:: cpp
    :caption: godot/modules/summator/tests/test_summator.h

    #pragma once

    #include "tests/test_macros.h"

    #include "modules/summator/summator.h"

    namespace TestSummator {

    TEST_CASE("[Modules][Summator] Adding numbers") {
        Ref<Summator> s = memnew(Summator);
        CHECK(s->get_total() == 0);

        s->add(10);
        CHECK(s->get_total() == 10);

        s->add(20);
        CHECK(s->get_total() == 30);

        s->add(30);
        CHECK(s->get_total() == 60);

        s->reset();
        CHECK(s->get_total() == 0);
    }

    } // namespace TestSummator

4. Compile the engine with ``scons tests=yes``, and run the tests with the
   following command:

.. code-block:: console

    ./bin/<godot_binary> --test --source-file="*test_summator*" --success

You should see the passing assertions now.

.. _doc_custom_module_icons:

Adding custom editor icons
--------------------------

Similarly to how you can write self-contained documentation within a module,
you can also create your own custom icons for classes to appear in the editor.

For the actual process of creating editor icons to be integrated within the engine,
please refer to :ref:`doc_editor_icons` first.

Once you've created your icon(s), proceed with the following steps:

1. Make a new directory in the root of the module named ``icons``. This is the
   default path for the engine to look for module's editor icons.

2. Move your newly created ``svg`` icons (optimized or not) into that folder.

3. Recompile the engine and run the editor. Now the icon(s) will appear in
   editor's interface where appropriate.

If you'd like to store your icons somewhere else within your module,
add the following code snippet to ``config.py`` to override the default path:

   .. code-block:: python

       def get_icons_path():
           return "path/to/icons"

Summing up
----------

Remember to:

-  Use ``GDCLASS`` macro for inheritance, so Godot can wrap it.
-  Use ``_bind_methods`` to bind your functions to scripting, and to
   allow them to work as callbacks for signals.
-  **Avoid multiple inheritance for classes exposed to Godot**, as ``GDCLASS``
   doesn't support this. You can still use multiple inheritance in your own
   classes as long as they're not exposed to Godot's scripting API.

But this is not all, depending what you do, you will be greeted with
some (hopefully positive) surprises.

-  If you inherit from :ref:`class_Node` (or any derived node type, such as
   Sprite2D), your new class will appear in the editor, in the inheritance
   tree in the "Add Node" dialog.
-  If you inherit from :ref:`class_Resource`, it will appear in the resource
   list, and all the exposed properties can be serialized when
   saved/loaded.
-  By this same logic, you can extend the Editor and almost any area of
   the engine.
