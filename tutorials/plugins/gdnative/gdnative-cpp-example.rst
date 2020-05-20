.. _doc_gdnative_cpp_example:

GDNative C++ example
====================

Introduction
------------

This tutorial builds on top of the information given in the
:ref:`GDNative C example <doc_gdnative_c_example>`, so we highly recommend you
read that first.

The C++ bindings for GDNative are built on top of the NativeScript GDNative API
and provide a nicer way to "extend" nodes in Godot using C++. This is equivalent
to writing scripts in GDScript, but in C++ instead.

Godot 3.1 saw the introduction of the NativeScript 1.1 additions that enabled
the GDNative team to build a nicer C++ bindings library. These changes have now
been merged into the master branch and will be the way we go forward. If you
want to write a C++ GDNative plugin that also supports Godot 3.0 you will need
to use the 3.0 branch and the NativeScript 1.0 syntax. We'll be showing them
side by side in this writeup.

You can download the full example we'll be creating in this tutorial `on
GitHub <https://github.com/BastiaanOlij/gdnative_cpp_example>`__.

Setting up the project
----------------------

There are a few prerequisites you'll need:

- a Godot 3.x executable,
- a C++ compiler,
- SCons as a build tool,
- a copy of the `godot-cpp
  repository <https://github.com/GodotNativeTools/godot-cpp>`__.

See also :ref:`Compiling <toc-devel-compiling>` as the build tools are identical
to the ones you need to compile Godot from source.

You can download these repositories from GitHub or let Git do the work for you.
Note that these repositories now have different branches for different versions
of Godot. GDNative modules written for an earlier version of Godot will work in
newer versions (with the exception of one breaking change in ARVR interfaces
between 3.0 and 3.1) but not vice versa so make sure you download the correct
branch. Also note that the version of Godot you use to generate the ``api.json``
with becomes your minimum version.

If you are versioning your project using Git, it is a good idea to add them as
Git submodules:

.. tabs::
 .. code-tab:: none Godot

    mkdir gdnative_cpp_example
    cd gdnative_cpp_example
    git init
    git submodule add https://github.com/GodotNativeTools/godot-cpp
    cd godot-cpp
    git submodule update --init

 .. code-tab:: none Godot 3.0

    mkdir gdnative_cpp_example
    cd gdnative_cpp_example
    git init
    git submodule add -b 3.0 https://github.com/GodotNativeTools/godot-cpp
    cd godot-cpp
    git submodule update --init

If you decide to just download the repositories or clone them into your project
folder, make sure to keep the folder layout identical to the one described here,
as much of the code we'll be showcasing here assumes the project follows this
layout.

Do make sure you clone recursive to pull in both repositories:

.. tabs::
 .. code-tab:: none Godot

    mkdir gdnative_cpp_example
    cd gdnative_cpp_example
    git clone --recursive https://github.com/GodotNativeTools/godot-cpp

 .. code-tab:: none Godot 3.0

    mkdir gdnative_cpp_example
    cd gdnative_cpp_example
    git clone --recursive -b 3.0 https://github.com/GodotNativeTools/godot-cpp

.. note::

    ``godot-cpp`` now includes ``godot_headers`` as a nested submodule, if you've
    manually downloaded them please make sure to place ``godot_headers`` inside
    of the ``godot-cpp`` folder.

    You don't have to do it this way but we've found it easiest to manage. If you
    decide to just download the repositories or just clone them into your folder,
    make sure to keep the folder layout the same as we've setup here as much of
    the code we'll be showcasing here assumes the project has this layout.

If you cloned the example from the link specified in the introduction, the
submodules are not automatically initialized. You will need to execute the
following commands:

.. code-block:: none

    cd gdnative_cpp_example
    git submodule update --init --recursive

This will clone these two repositories into your project folder.

Building the C++ bindings
-------------------------

Now that we've downloaded our prerequisites, it is time to build the C++
bindings.

The repository contains a copy of the metadata for the current Godot release,
but if you need to build these bindings for a newer version of Godot, simply
call the Godot executable:

.. code-block:: none

    godot --gdnative-generate-json-api api.json

Place the resulting ``api.json`` file in the project folder and add
``use_custom_api_file=yes custom_api_file=../api.json`` to the scons command
below.

To generate and compile the bindings, use this command (replacing ``<platform>``
with ``windows``, ``linux`` or ``osx`` depending on your OS):

To speed up compilation, add `-jN` at the end of the SCons command line where `N` is the number of CPU threads you have on your system. The example below uses 4 threads.

.. code-block:: none

    cd godot-cpp
    scons platform=<platform> generate_bindings=yes -j4
    cd ..

This step will take a while. When it is completed, you should have static
libraries that can be compiled into your project stored in ``godot-cpp/bin/``.

At some point in the future, compiled binaries will be available, making this
step optional.

.. note::

    You may need to add ``bits=64`` to the command on Windows or Linux. We're
    still working on better auto detection.

Creating a simple plugin
------------------------

Now it's time to build an actual plugin. We'll start by creating an empty Godot
project in which we'll place a few files.

Open Godot and create a new project. For this example, we will place it in a
folder called ``demo`` inside our GDNative module's folder structure.

In our demo project, we'll create a scene containing a Node called "Main" and
we'll save it as ``main.tscn``. We'll come back to that later.

Back in the top-level GDNative module folder, we're also going to create a
subfolder called ``src`` in which we'll place our source files.

You should now have ``demo``, ``godot-cpp``, ``godot_headers``, and ``src``
directories in your GDNative module.

In the ``src`` folder, we'll start with creating our header file for the
GDNative node we'll be creating. We will name it ``gdexample.h``:

.. tabs::
 .. code-tab:: C++ NativeScript 1.1

    #ifndef GDEXAMPLE_H
    #define GDEXAMPLE_H

    #include <Godot.hpp>
    #include <Sprite.hpp>

    namespace godot {

    class GDExample : public Sprite {
        GODOT_CLASS(GDExample, Sprite)

    private:
        float time_passed;

    public:
        static void _register_methods();

        GDExample();
        ~GDExample();

        void _init(); // our initializer called by Godot

        void _process(float delta);
    };

    }

    #endif

 .. code-tab:: C++ NativeScript 1.0

    #ifndef GDEXAMPLE_H
    #define GDEXAMPLE_H

    #include <Godot.hpp>
    #include <Sprite.hpp>

    namespace godot {

    class GDExample : public godot::GodotScript<Sprite> {
        GODOT_CLASS(GDExample)

    private:
        float time_passed;

    public:
        static void _register_methods();

        GDExample();
        ~GDExample();

        void _process(float delta);
    };

    }

    #endif

There are a few things of note to the above. We're including ``Godot.hpp`` which
contains all our basic definitions. After that, we include ``Sprite.hpp`` which
contains bindings to the Sprite class. We'll be extending this class in our
module.

We're using the namespace ``godot``, since everything in GDNative is defined
within this namespace.

Then we have our class definition, which inherits from our Sprite through a
container class. We'll see a few side effects of this later on. The
``GODOT_CLASS`` macro sets up a few internal things for us.

After that, we declare a single member variable called ``time_passed``.

In the next block we're defining our methods, we obviously have our constructor
and destructor defined, but there are two other functions that will likely look
familiar to some, and one new method.

The first is ``_register_methods``, which is a static function that Godot will
call to find out which methods can be called on our NativeScript and which
properties it exposes. The second is our ``_process`` function, which will work
exactly the same as the ``_process`` function you're used to in GDScript. The
third is our ``_init`` function which is called after Godot has properly set up
our object. It has to exist even if you don't place any code in it.

Let's implement our functions by creating our ``gdexample.cpp`` file:

.. tabs::
 .. code-tab:: C++ NativeScript 1.1

    #include "gdexample.h"

    using namespace godot;

    void GDExample::_register_methods() {
        register_method("_process", &GDExample::_process);
    }

    GDExample::GDExample() {
    }

    GDExample::~GDExample() {
        // add your cleanup here
    }

    void GDExample::_init() {
        // initialize any variables here
        time_passed = 0.0;
    }

    void GDExample::_process(float delta) {
        time_passed += delta;

        Vector2 new_position = Vector2(10.0 + (10.0 * sin(time_passed * 2.0)), 10.0 + (10.0 * cos(time_passed * 1.5)));

        set_position(new_position);
    }

 .. code-tab:: C++ NativeScript 1.0

    #include "gdexample.h"

    using namespace godot;

    void GDExample::_register_methods() {
        register_method((char *)"_process", &GDExample::_process);
    }

    GDExample::GDExample() {
        // Initialize any variables here
        time_passed = 0.0;
    }

    GDExample::~GDExample() {
        // Add your cleanup procedure here
    }

    void GDExample::_process(float delta) {
        time_passed += delta;

        Vector2 new_position = Vector2(10.0 + (10.0 * sin(time_passed * 2.0)), 10.0 + (10.0 * cos(time_passed * 1.5)));

        owner->set_position(new_position);
    }

This one should be straightforward. We're implementing each method of our class
that we defined in our header file. Note that the ``register_method`` call
**must** expose the ``_process`` method, otherwise Godot will not be able to use
it. However, we do not have to tell Godot about our constructor, destructor and
``_init`` functions.

The other method of note is our ``_process`` function, which simply keeps track
of how much time has passed and calculates a new position for our sprite using a
simple sine and cosine function. What stands out is calling
``owner->set_position`` to call one of the build in methods of our Sprite. This
is because our class is a container class; ``owner`` points to the actual Sprite
node our script relates to. In the upcoming NativeScript 1.1, ``set_position``
can be called directly on our class.

There is one more C++ file we need; we'll name it ``gdlibrary.cpp``. Our
GDNative plugin can contain multiple NativeScripts, each with their own header
and source file like we've implemented ``GDExample`` up above. What we need now
is a small bit of code that tells Godot about all the NativeScripts in our
GDNative plugin.

.. code-block:: C++

    #include "gdexample.h"

    extern "C" void GDN_EXPORT godot_gdnative_init(godot_gdnative_init_options *o) {
        godot::Godot::gdnative_init(o);
    }

    extern "C" void GDN_EXPORT godot_gdnative_terminate(godot_gdnative_terminate_options *o) {
        godot::Godot::gdnative_terminate(o);
    }

    extern "C" void GDN_EXPORT godot_nativescript_init(void *handle) {
        godot::Godot::nativescript_init(handle);

        godot::register_class<godot::GDExample>();
    }

Note that we are not using the ``godot`` namespace here, since the three
functions implemented here need to be defined without a namespace.

The ``godot_gdnative_init`` and ``godot_gdnative_terminate`` functions get
called respectively when Godot loads our plugin and when it unloads it. All
we're doing here is parse through the functions in our bindings module to
initialize them, but you might have to set up more things depending on your
needs.

The important function is the third function called ``godot_nativescript_init``.
We first call a function in our bindings library that does its usual stuff.
After that, we call the function ``register_class`` for each of our classes in
our library.

Compiling the plugin
--------------------

We cannot easily write by hand a ``SConstruct`` file that SCons would use for
building. For the purpose of this example, just use
:download:`this hardcoded SConstruct file <files/cpp_example/SConstruct>` we've
prepared. We'll cover a more customizable, detailed example on how to use these
build files in a subsequent tutorial.

.. note::

    This ``SConstruct`` file was written to be used with the latest ``godot-cpp``
    master, you may need to make small changes using it with older versions or
    refer to the ``SConstruct`` file in the Godot 3.0 documentation.

Once you've downloaded the ``SConstruct`` file, place it in your GDNative module
folder besides ``godot-cpp``, ``godot_headers`` and ``demo``, then run:

.. code-block:: none

    scons platform=<platform>

You should now be able to find the module in ``demo/bin/<platform>``.

.. note::

    Here, we've compiled both godot-cpp and our gdexample library as debug
    builds. For optimized builds, you should compile them using the
    ``target=release`` switch.

Using the GDNative module
-------------------------

Before we jump back into Godot, we need to create two more files in
``demo/bin/``. Both can be created using the Godot editor, but it may be faster
to create them directly.

The first one is a file that lets Godot know what dynamic libraries should be
loaded for each platform and is called ``gdexample.gdnlib``.

.. code-block:: none

    [general]

    singleton=false
    load_once=true
    symbol_prefix="godot_"
    reloadable=false

    [entry]

    X11.64="res://bin/x11/libgdexample.so"
    Windows.64="res://bin/win64/libgdexample.dll"
    OSX.64="res://bin/osx/libgdexample.dylib"

    [dependencies]

    X11.64=[]
    Windows.64=[]
    OSX.64=[]

This file contains a ``general`` section that controls how the module is loaded.
It also contains a prefix section which should be left on ``godot_`` for now. If
you change this, you'll need to rename various functions that are used as entry
points. This was added for the iPhone platform because it doesn't allow dynamic
libraries to be deployed, yet GDNative modules are linked statically.

The ``entry`` section is the important bit: it tells Godot the location of the
dynamic library in the project's filesystem for each supported platform. It will
also result in *just* that file being exported when you export the project,
which means the data pack won't contain libraries that are incompatible with the
target platform.

Finally, the ``dependencies`` section allows you to name additional dynamic
libraries that should be included as well. This is important when your GDNative
plugin implements someone else's library and requires you to supply a
third-party dynamic library with your project.

If you double click on the ``gdexample.gdnlib`` file within Godot, you'll see
there are far more options to set:

.. image:: img/gdnative_library.png

The second file we need to create is a file used by each NativeScript we've
added to our plugin. We'll name it ``gdexample.gdns`` for our gdexample
NativeScript.

.. code-block:: none

    [gd_resource type="NativeScript" load_steps=2 format=2]

    [ext_resource path="res://bin/gdexample.gdnlib" type="GDNativeLibrary" id=1]

    [resource]

    resource_name = "gdexample"
    class_name = "GDExample"
    library = ExtResource( 1 )

This is a standard Godot resource; you could just create it directly in your
scene, but saving it to a file makes it much easier to reuse it in other places.
This resource points to our gdnlib file, so that Godot can know which dynamic
library contains our NativeScript. It also defines the ``class_name`` which
identifies the NativeScript in our plugin we want to use.

Time to jump back into Godot. We load up the main scene we created way back in
the beginning and now add a Sprite to our scene:

.. image:: img/gdnative_cpp_nodes.png

We're going to assign the Godot logo to this sprite as our texture, disable the
``centered`` property and drag our ``gdexample.gdns`` file onto the ``script``
property of the sprite:

.. image:: img/gdnative_cpp_sprite.png

We're finally ready to run the project:

.. image:: img/gdnative_cpp_animated.gif

Adding properties
-----------------

GDScript allows you to add properties to your script using the ``export``
keyword. In GDNative you have to register the properties and there are two ways
of doing this. You can either bind directly to a member or use a setter and
getter function.

.. note::

    There is a third option, just like in GDScript you can directly implement the
    ``_get_property_list``, ``_get`` and ``_set`` methods of an object but that
    goes far beyond the scope of this tutorial.

We'll examine both starting with the direct bind. Lets add a property that
allows us to control the amplitude of our wave.

In our ``gdexample.h`` file we simply need to add a member variable like so:

.. code-block:: C++

    ...
    private:
        float time_passed;
        float amplitude;
    ...

In our ``gdexample.cpp`` file we need to make a number of changes, we will only
show the methods we end up changing, don't remove the lines we're omitting:

.. tabs::
 .. code-tab:: C++ NativeScript 1.1

    void GDExample::_register_methods() {
        register_method("_process", &GDExample::_process);
        register_property<GDExample, float>("amplitude", &GDExample::amplitude, 10.0);
    }

    void GDExample::_init() {
        // initialize any variables here
        time_passed = 0.0;
        amplitude = 10.0;
    }

    void GDExample::_process(float delta) {
        time_passed += delta;

        Vector2 new_position = Vector2(
            amplitude + (amplitude * sin(time_passed * 2.0)),
            amplitude + (amplitude * cos(time_passed * 1.5))
        );

        set_position(new_position);
    }

 .. code-tab:: C++ NativeScript 1.0

    void GDExample::_register_methods() {
        register_method((char *)"_process", &GDExample::_process);
        register_property<GDExample, float>("amplitude", &GDExample::amplitude, 10.0);
    }

    GDExample::GDExample() {
        // initialize any variables here
        time_passed = 0.0;
        amplitude = 10.0;
    }

    void GDExample::_process(float delta) {
        time_passed += delta;

        Vector2 new_position = Vector2(
            amplitude + (amplitude * sin(time_passed * 2.0)),
            amplitude + (amplitude * cos(time_passed * 1.5))
        );

        owner->set_position(new_position);
    }

Once you compile the module with these changes in place you will see that a
property has been added to our interface. You can now change this property and
when you run your project, you will see that our Godot icon travels along a
larger figure.

.. note::

    The ``reloadable`` property in the ``gdexample.gdnlib`` file must be set to
    ``true`` for the Godot editor to automatically pick up the newly added
    property.

    However, this setting should be used with care especially when tool classes
    are used, as the editor might hold objects then that have script instances
    attached to them that are managed by a GDNative library.

Lets do the same but for the speed of our animation and use a setter and getter
function. Our ``gdexample.h`` header file again only needs a few more lines of
code:

.. code-block:: C++

    ...
        float amplitude;
        float speed;
    ...
        void _process(float delta);
        void set_speed(float p_speed);
        float get_speed();
    ...

This requires a few more changes to our ``gdexample.cpp`` file, again we're only
showing the methods that have changed so don't remove anything we're omitting:

.. tabs::
 .. code-tab:: C++ NativeScript 1.1

    void GDExample::_register_methods() {
        register_method("_process", &GDExample::_process);
        register_property<GDExample, float>("amplitude", &GDExample::amplitude, 10.0);
        register_property<GDExample, float>("speed", &GDExample::set_speed, &GDExample::get_speed, 1.0);
    }

    void GDExample::_init() {
        // initialize any variables here
        time_passed = 0.0;
        amplitude = 10.0;
        speed = 1.0;
    }

    void GDExample::_process(float delta) {
        time_passed += speed * delta;

        Vector2 new_position = Vector2(
            amplitude + (amplitude * sin(time_passed * 2.0)),
            amplitude + (amplitude * cos(time_passed * 1.5))
        );

        set_position(new_position);
    }

    void GDExample::set_speed(float p_speed) {
        speed = p_speed;
    }

    float GDExample::get_speed() {
        return speed;
    }

 .. code-tab:: C++ NativeScript 1.0

    void GDExample::_register_methods() {
        register_method((char *)"_process", &GDExample::_process);
        register_property<GDExample, float>("amplitude", &GDExample::amplitude, 10.0);
        register_property<GDExample, float>("speed", &GDExample::set_speed, &GDExample::get_speed, 1.0);
    }

    GDExample::GDExample() {
        // initialize any variables here
        time_passed = 0.0;
        amplitude = 10.0;
        speed = 1.0;
    }

    void GDExample::_process(float delta) {
        time_passed += speed * delta;

        Vector2 new_position = Vector2(
            amplitude + (amplitude * sin(time_passed * 2.0)),
            amplitude + (amplitude * cos(time_passed * 1.5))
        );

        owner->set_position(new_position);
    }

    void GDExample::set_speed(float p_speed) {
        speed = p_speed;
    }

    float GDExample::get_speed() {
        return speed;
    }

Now when the project is compiled we'll see another property called speed.
Changing its value will make the animation go faster or slower.

For this example there is no obvious advantage of using a setter and getter. It
is just more code to write. For a simple example as this there may be a good
reason for a setter if you want to react on the variable being changed but in
many cases just binding the variable will be enough.

Getters and setters become far more useful in more complex scenarios where you
need to make additional choices based on the state of your object.

.. note::

    For simplicity we've left out the optional parameters in the
    register_property<class, type> method call. These parameters are
    ``rpc_mode``, ``usage``, ``hint`` and ``hint_string``. These can be used to
    further configure how properties are displayed and set on the Godot side.

    Modern C++ compilers are able to infer the class and variable type and allow
    you to omit the ``<GDExample, float>`` part of our ``register_property``
    method. We've had mixed experiences with this however.

Signals
-------

Last but not least, signals fully work in GDNative as well. Having your module
react to a signal given out by another object requires you to call ``connect``
on that object. We can't think of a good example for our wobbling Godot icon, we
would need to showcase a far more complete example.

This however is the required syntax:

.. tabs::
 .. code-tab:: C++ NativeScript 1.1

    some_other_node->connect("the_signal", this, "my_method");

 .. code-tab:: C++ NativeScript 1.0

    some_other_node->connect("the_signal", owner, "my_method");

Note that you can only call ``my_method`` if you've previously registered it in
your ``_register_methods`` method.

Having your object sending out signals is far more common. For our wobbling
Godot icon we'll do something silly just to show how it works. We're going to
emit a signal every time a second has passed and pass the new location along.

In our ``gdexample.h`` header file we just need to define a new member
``time_emit``:

.. code-block:: C++

    ...
        float time_passed;
        float time_emit;
        float amplitude;
    ...

The changes in ``gdexample.cpp`` are a bit more elaborate this time. First
you'll need to set ``time_emit = 0.0;`` in either our ``_init`` method or in our
constructor. But the other two needed changes we'll look at one by one.

In our ``_register_methods`` method we need to declare our signal and we do this
as follows:

.. tabs::
 .. code-tab:: C++ NativeScript 1.1

    void GDExample::_register_methods() {
        register_method("_process", &GDExample::_process);
        register_property<GDExample, float>("amplitude", &GDExample::amplitude, 10.0);
        register_property<GDExample, float>("speed", &GDExample::set_speed, &GDExample::get_speed, 1.0);

        register_signal<GDExample>((char *)"position_changed", "node", GODOT_VARIANT_TYPE_OBJECT, "new_pos", GODOT_VARIANT_TYPE_VECTOR2);
    }

 .. code-tab:: C++ NativeScript 1.0

    void GDExample::_register_methods() {
        register_method((char *)"_process", &GDExample::_process);
        register_property<GDExample, float>("amplitude", &GDExample::amplitude, 10.0);
        register_property<GDExample, float>("speed", &GDExample::set_speed, &GDExample::get_speed, 1.0);

        Dictionary args;
        args[Variant("node")] = Variant(Variant::OBJECT);
        args[Variant("new_pos")] = Variant(Variant::VECTOR2);
        register_signal<GDExample>((char *)"position_changed", args);
    }

Here we see a nice improvement in the latest version of godot-cpp where our
``register_signal`` method can be a single call first taking the signals name,
then having pairs of values specifying the parameter name and type of each
parameter we'll send along with this signal.

For NativeScript 1.0 we first build a dictionary in which we tell Godot about
the types of arguments we will pass to our signal, and then register it.

Next we'll need to change our ``_process`` method:

.. tabs::
 .. code-tab:: C++ NativeScript 1.1

    void GDExample::_process(float delta) {
        time_passed += speed * delta;

        Vector2 new_position = Vector2(
            amplitude + (amplitude * sin(time_passed * 2.0)),
            amplitude + (amplitude * cos(time_passed * 1.5))
        );

        set_position(new_position);

        time_emit += delta;
        if (time_emit > 1.0) {
            emit_signal("position_changed", this, new_position);

            time_emit = 0.0;
        }
    }

 .. code-tab:: C++ NativeScript 1.0

    void GDExample::_process(float delta) {
        time_passed += speed * delta;

        Vector2 new_position = Vector2(
            amplitude + (amplitude * sin(time_passed * 2.0)),
            amplitude + (amplitude * cos(time_passed * 1.5))
        );

        owner->set_position(new_position);

        time_emit += delta;
        if (time_emit > 1.0) {
            Array args;
            args.push_back(Variant(owner));
            args.push_back(Variant(new_position));
            owner->emit_signal("position_changed", args);

            time_emit = 0.0;
        }
    }

After a second has passed we emit our signal and reset our counter. Again in the
new version of godot-cpp we can add our parameter values directly to
``emit_signal``. In NativeScript 1.0 We first build an array of values and then
call ``emit_signal``.

Once compiled we can go into Godot and select our sprite node. On our ``Node``
tab we find our new signal and link it up by pressing connect. We've added a
script on our main node and implemented our signal like this:

.. code-block:: none

    extends Node

    func _on_Sprite_position_changed(node, new_pos):
        print("The position of " + node.name + " is now " + str(new_pos))

Every second we simply output our position to the console.

NativeScript 1.1 vs NativeScript 1.0
------------------------------------

So far in our example above there doesn't seem to be a lot of difference between
the old and new syntax. The class is defined slightly differently and we no
longer use the ``owner`` member to call methods on the Godot side of our object.
A lot of the improvements are hidden under the hood.

This example only deals with simple variables and simple methods. Especially
once you start passing references to other objects or when you start calling
methods that require more complex parameters, NativeScript 1.1 does start to
show its benefits.

Next steps
----------

The above is only a simple example, but we hope it shows you the basics. You can
build upon this example to create full-fledged scripts to control nodes in Godot
using C++.

You should be able to edit and recompile the plugin while the Godot editor
remains open; just rerun the project after the library has finished building.
