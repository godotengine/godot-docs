.. _doc_custom_modules_in_c++:

Custom modules in C++
=====================

Modules
-------

Godot allows extending the engine in a modular way. New modules can be
created and then enabled/disabled. This allows for adding new engine
functionality at every level without modifying the core, which can be
split for use and reuse in different modules.

Modules are located in the ``modules/`` subdirectory of the build system.
By default, two modules exist, GDScript (which, yes, is not part of the
core engine), and the GridMap. As many new modules as desired can be
created and combined, and the SCons build system will take care of it
transparently.

What for?
---------

While it's recommended that most of a game is written in scripting (as
it is an enormous time saver), it's perfectly possible to use C++
instead. Adding C++ modules can be useful in the following scenarios:

-  Binding an external library to Godot (like Bullet, Physx, FMOD, etc).
-  Optimize critical parts of a game.
-  Adding new functionality to the engine and/or editor.
-  Porting an existing game.
-  Write a whole, new game in C++ because you can't live without C++.

Creating a new module
---------------------

Before creating a module, make sure to download the source code of Godot
and manage to compile it. There are tutorials in the documentation for this.

To create a new module, the first step is creating a directory inside
``modules/``. If you want to maintain the module separately, you can checkout
a different VCS into modules and use it.

The example module will be called "sumator", and is placed inside the
Godot source tree (``C:\godot`` refers to wherever the Godot sources are
located):

::

    C:\godot> cd modules
    C:\godot\modules> mkdir sumator
    C:\godot\modules> cd sumator
    C:\godot\modules\sumator>

Inside we will create a simple sumator class:

.. code:: cpp

    /* sumator.h */
    #ifndef SUMATOR_H
    #define SUMATOR_H

    #include "reference.h"

    class Sumator : public Reference {
        OBJ_TYPE(Sumator,Reference);

        int count;

    protected:
        static void _bind_methods();

    public:
        void add(int value);
        void reset();
        int get_total() const;

        Sumator();
    };

    #endif

And then the cpp file.

.. code:: cpp

    /* sumator.cpp */

    #include "sumator.h"

    void Sumator::add(int value) {

        count+=value;
    }

    void Sumator::reset() {

        count=0;
    }

    int Sumator::get_total() const {

        return count;
    }

    void Sumator::_bind_methods() {

        ObjectTypeDB::bind_method("add",&Sumator::add);
        ObjectTypeDB::bind_method("reset",&Sumator::reset);
        ObjectTypeDB::bind_method("get_total",&Sumator::get_total);
    }

    Sumator::Sumator() {
        count=0;
    }

Then, the new class needs to be registered somehow, so two more files
need to be created:

::

    register_types.h
    register_types.cpp

With the following contents:

.. code:: cpp

    /* register_types.h */

    void register_sumator_types();
    void unregister_sumator_types();
    /* yes, the word in the middle must be the same as the module folder name */

.. code:: cpp

    /* register_types.cpp */

    #include "register_types.h"
    #include "object_type_db.h"
    #include "sumator.h"

    void register_sumator_types() {

            ObjectTypeDB::register_type<Sumator>();
    }

    void unregister_sumator_types() {
       //nothing to do here
    }

Next, we need to create a ``SCsub`` file so the build system compiles
this module:

.. code:: python

    # SCsub
    Import('env')

    env.add_source_files(env.modules_sources,"*.cpp") # just add all cpp files to the build

If you want to add custom compiler flags when building your module, you need to clone
`env` first, so it won't add those flags to whole Godot build (which can cause errors).
Example `SCub` with custom flags:

.. code:: python

    # SCsub
    Import('env')

    module_env = env.Clone()
    module_env.add_source_files(env.modules_sources,"*.cpp")
    module_env.Append(CXXFLAGS=['-O2', '-std=c++11'])

And finally, the configuration file for the module, this is a simple
python script that must be named ``config.py``:

.. code:: python

    # config.py

    def can_build(platform):
        return True

    def configure(env):
        pass

The module is asked if it's ok to build for the specific platform (in
this case, True means it will build for every platform).

And that's it. Hope it was not too complex! Your module should look like
this:

::

    godot/modules/sumator/config.py
    godot/modules/sumator/sumator.h
    godot/modules/sumator/sumator.cpp
    godot/modules/sumator/register_types.h
    godot/modules/sumator/register_types.cpp
    godot/modules/sumator/SCsub

You can then zip it and share the module with everyone else. When
building for every platform (instructions in the previous sections),
your module will be included.

Using the module
----------------

Using your newly created module is very easy, from any script you can
now do:

::

    var s = Sumator.new()
    s.add(10)
    s.add(20)
    s.add(30)
    print(s.get_total())
    s.reset()

And the output will be ``60``.

Summing up
----------

As you see, it's really easy to develop Godot in C++. Just write your
stuff normally and remember to:

-  use ``OBJ_TYPE`` macro for inheritance, so Godot can wrap it
-  use ``_bind_methods`` to bind your functions to scripting, and to
   allow them to work as callbacks for signals.

But this is not all, depending what you do, you will be greeted with
some surprises.

-  If you inherit from :ref:`class_Node` (or any derived node type, such as
   Sprite), your new class will appear in the editor, in the inheritance
   tree in the "Add Node" dialog.
-  If you inherit from :ref:`class_Resource`, it will appear in the resource
   list, and all the exposed properties can be serialized when
   saved/loaded.
-  By this same logic, you can extend the Editor and almost any area of
   the engine.
