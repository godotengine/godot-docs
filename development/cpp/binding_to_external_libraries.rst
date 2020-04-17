.. _doc_binding_to_external_libraries:

Binding to external libraries
=============================

Modules
-------

The Summator example in :ref:`doc_custom_modules_in_c++` is great for small,
custom modules, but what if you want to use a larger, external library?
Let's look at an example using Festival, a speech synthesis (text-to-speech)
library written in C++.

To bind to an external library, set up a module directory similar to the Summator example:

.. code-block:: none

    godot/modules/tts/

Next, you will create a header file with a simple TTS class:

.. code-block:: cpp

    /* tts.h */

    #ifndef GODOT_TTS_H
    #define GODOT_TTS_H

    #include "core/reference.h"

    class TTS : public Reference {
        GDCLASS(TTS, Reference);

    protected:
        static void _bind_methods();

    public:
        bool say_text(String p_txt);

        TTS();
    };

    #endif // GODOT_TTS_H

And then you'll add the cpp file.

.. code-block:: cpp

    /* tts.cpp */

    #include "tts.h"

    #include <festival.h>

    bool TTS::say_text(String p_txt) {

        //convert Godot String to Godot CharString to C string
        return festival_say_text(p_txt.ascii().get_data());
    }

    void TTS::_bind_methods() {

        ClassDB::bind_method(D_METHOD("say_text", "txt"), &TTS::say_text);
    }

    TTS::TTS() {
        festival_initialize(true, 210000); //not the best way to do it as this should only ever be called once.
    }

Just as before, the new class needs to be registered somehow, so two more files
need to be created:

.. code-block:: none

    register_types.h
    register_types.cpp

With the following contents:

.. code-block:: cpp

    /* register_types.h */

    void register_tts_types();
    void unregister_tts_types();
    /* yes, the word in the middle must be the same as the module folder name */

.. code-block:: cpp

    /* register_types.cpp */

    #include "register_types.h"

    #include "core/class_db.h"
    #include "tts.h"

    void register_tts_types() {
        ClassDB::register_class<TTS>();
    }

    void unregister_tts_types() {
        // Nothing to do here in this example.
    }

Next, you need to create a ``SCsub`` file so the build system compiles
this module:

.. code-block:: python

    # SCsub

    Import('env')

    env_tts = env.Clone()
    env_tts.add_source_files(env.modules_sources, "*.cpp") # Add all cpp files to the build

You'll need to install the external library on your machine to get the .a library files.  See the library's official
documentation for specific instructions on how to do this for your operation system.  We've included the
installation commands for Linux below, for reference.

.. code-block:: shell

    sudo apt-get install festival festival-dev <-- Installs festival and speech_tools libraries
    apt-cache search festvox-* <-- Displays list of voice packages
    sudo apt-get install festvox-don festvox-rablpc16k festvox-kallpc16k festvox-kdlpc16k <-- Installs voices

.. note::
    **Important:** The voices that Festival uses (and any other potential external/3rd-party
    resource) all have varying licenses and terms of use; some (if not most) of them may be
    be problematic with Godot, even if the Festival Library itself is MIT License compatible.
    Please be sure to check the licenses and terms of use.

The external library will also need to be installed inside your module to make the source
files accessible to the compiler, while also keeping the module code self-contained.  The
festival and speech_tools libraries can be installed from the modules/tts/ directory via
git using the following commands:

.. code-block:: shell

    git clone https://github.com/festvox/festival
    git clone https://github.com/festvox/speech_tools

If you don't want the external repository source files committed to your repository, you
can link to them instead by adding them as submodules (from within the modules/tts/ directory), as seen below:

.. code-block:: shell

    git submodule add https://github.com/festvox/festival
    git submodule add https://github.com/festvox/speech_tools

.. note::
    **Important:** Please note that Git submodules are not used in the Godot repository.  If
    you are developing a module to be merged into the main Godot repository, you should not
    use submodules.  If your module doesn't get merged in, you can always try to implement
    the external library as a GDNative C++ plugin.

To add include directories for the compiler to look at you can append it to the
environment's paths:

.. code-block:: python

    env_tts.Append(CPPPATH=["speech_tools/include", "festival/src/include"]) # this is a path relative to /modules/tts/
    # http://www.cstr.ed.ac.uk/projects/festival/manual/festival_28.html#SEC132 <-- Festival library documentation
    env_tts.Append(LIBPATH=['libpath']) # this is a path relative to /modules/tts/ where your .a library files reside
    # You should check with the documentation of the external library to see which library files should be included/linked
    env_tts.Append(LIBS=['Festival', 'estools', 'estbase', 'eststring'])

If you want to add custom compiler flags when building your module, you need to clone
`env` first, so it won't add those flags to whole Godot build (which can cause errors).
Example `SCsub` with custom flags:

.. code-block:: python

    # SCsub

    Import('env')

    env_tts = env.Clone()
    env_tts.add_source_files(env.modules_sources, "*.cpp")
    env_tts.Append(CCFLAGS=['-O2']) # Flags for C and C++ code
    env_tts.Append(CXXFLAGS=['-std=c++11']) # Flags for C++ code only

The final module should look like this:

.. code-block:: none

    godot/modules/tts/festival/
    godot/modules/tts/libpath/libestbase.a
    godot/modules/tts/libpath/libestools.a
    godot/modules/tts/libpath/libeststring.a
    godot/modules/tts/libpath/libFestival.a
    godot/modules/tts/speech_tools/
    godot/modules/tts/config.py
    godot/modules/tts/tts.h
    godot/modules/tts/tts.cpp
    godot/modules/tts/register_types.h
    godot/modules/tts/register_types.cpp
    godot/modules/tts/SCsub

Using the module
----------------

You can now use your newly created module from any script:

::

    var t = TTS.new()
    var script = "Hello world. This is a test!"
    var is_spoken = t.say_text(script)
    print('is_spoken: ', is_spoken)

And the output will be ``is_spoken: True`` if the text is spoken.
