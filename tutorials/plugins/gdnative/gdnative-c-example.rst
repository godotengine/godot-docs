.. _doc_gdnative_c_example:

GDNative C example
==================

Introduction
------------
This tutorial will introduce you to the bare minimum required to create GDNative modules. This should be your starting point into the world of GDNative, understanding the contents of this tutorial will help you in understanding all that is to come after this.

Before we begin, you can download the source code to the example object we'll be describing here by following this link:
https://github.com/GodotNativeTools/GDNative-demos/tree/master/c/SimpleDemo

This example project also contains a SConstruct file that makes compiling a little easier but in this tutorial we'll be doing things by hand.

:ref:`GDNative <class_GDNative>` can be used to create several types of additions to Godot, from PluginScript to ARVR interfaces. In this tutorial we are going to look at creating a :ref:`NativeScript <class_NativeScript>` module. NativeScript allows you to write logic in C or C++ in similar fashion as you would write a GDScript file. We'll be creating the C equivalent of this GDScript:

::

    extends Reference

    var data

    func _ready():
        data = "World from GDScript!"

    func get_data():
        return data

We'll be writing separate tutorials on the other types of GDNative modules and explain what each of them is for as we go through them. 

Prerequisites
-------------
Before we start you'll need a few things.

1) A Godot 3.0 executable
2) A C compiler
3) A copy of this repository: https://github.com/GodotNativeTools/godot_headers

The first two pretty much speak for themselves. On Linux, you'll likely have a C compiler, on macOS, it's easiest to install Xcode from the Mac App Store and, on Windows, we've tested this with both MSVC 2015 and 2017.

For number 3, we suggest that you create a folder somewhere that you use to store your code, open up a terminal and CD into that folder. Then execute:

.. code-block:: none

    git clone https://github.com/GodotNativeTools/godot_headers

This will download the required files into that folder.

.. note:: On this repository you will now find different branches. As Godot evolves, so does GDNative. With the exception of one breaking change in ARVR between 3.0 and 3.1, GDNative modules build for older versions of Godot will work with newer versions of Godot but not the other way around.

The master branch of the ``godot_headers`` repository is kept in line with the master branch of Godot and thus contains the GDNative class and structure definitions that will work with the latest Godot master.

The 3.0 branch of the ``godot_headers`` repository contains the GDNative class and structure definitions that will work with Godot 3.0. You can clone this branch by executing:

.. code-block:: none

    git clone https://github.com/GodotNativeTools/godot_headers -b 3.0

If you are building Godot from source with your own changes that impact GDNative, you can find the updated class and structure definition in ``<godotsource>/modules/gdnative/include``

Our C source
------------
Let's start by writing our main code. Ideally, we want to end up with a file structure that looks something like this:

.. code-block:: none

  + <your development folder>
    + godot_headers
      - <lots of files here>
    + simple
      + bin
        - libsimple.dll/so/dylib
        - libsimple.gdnlib
        - simple.gdns
      + src
        - .gdignore
        - simple.c
      main.tscn
      project.godot

Open up Godot and create a new project called simple. This will create the simple folder and project.godot file. Then manually create a bin and src subfolder in this folder.

We're going to start by having a look at what our simple.c file contains. Now, for our example here we're making a single C source file without a header to keep things simple. Once you start writing bigger projects it is advisable you break your project up into multiple files. That however falls outside of the scope of this tutorial.

We'll be looking at the source code bit by bit so all the parts below should all be put together into one big file. I'll explain each section as we add it.

The below code includes our header files that we need and then defines two pointers to two different structs. 
GDNative supports a large collection for functions for calling back into the main Godot executable. In order for your module to have access to these functions, GDNative provides your application with a struct containing pointers to all these functions.

To keep this implementation modular and easily extendable, the core functions are available directly through the "core" API struct, but additional functions have their own "GDNative structs" that are accessible through extensions. 

In our example, we access one of these extension to gain access to the functions specifically needed for NativeScript.

.. code:: C

    #include <gdnative_api_struct.gen.h>
    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>

    const godot_gdnative_core_api_struct *api = NULL;
    const godot_gdnative_ext_nativescript_api_struct *nativescript_api = NULL;

A NativeScript behaves like any other script in Godot. Because the NativeScript API is rather low level, it requires the library to specify many things more verbosely than other scripting systems, such as GDScript. When a NativeScript instance gets created, a library-given constructor gets called. When that instance gets destroyed, the given destructor will be executed.

These are forward declarations for the functions we'll be implementing for our object. A constructor and destructor is needed. Additionally, the object will have a single method called get_data.

.. code:: C

    void *simple_constructor(godot_object *p_instance, void *p_method_data);
    void simple_destructor(godot_object *p_instance, void *p_method_data, void *p_user_data);
    godot_variant simple_get_data(godot_object *p_instance, void *p_method_data
        , void *p_user_data, int p_num_args, godot_variant **p_args);

Next up is the first of the entry points Godot will call when our dynamic library is loaded. These methods are all prefixed with godot (you can change this later on) followed by their name. ``gdnative_init`` is a function that initialises our dynamic library. Godot will give it a pointer to a structure that contains various bits of information we may find useful amongst which the pointers to our API structures.

For any additional API structures we need to loop through our extensions array and check the type of extension.

.. code:: C

    void GDN_EXPORT godot_gdnative_init(godot_gdnative_init_options *p_options) {
        api = p_options->api_struct;

        // now find our extensions
        for (int i = 0; i < api->num_extensions; i++) {
            switch (api->extensions[i]->type) {
                case GDNATIVE_EXT_NATIVESCRIPT: {
                    nativescript_api = (godot_gdnative_ext_nativescript_api_struct *)api->extensions[i];
                }; break;
                default: break;
            }
        }
    }

Next up is ``gdnative_terminate`` which is called before the library is unloaded. Godot will unload the library when no object uses it anymore. Here, you can do any cleanup you may need to do. For our example, we're simply going to clear our API pointers.

.. code:: C

    void GDN_EXPORT godot_gdnative_terminate(godot_gdnative_terminate_options *p_options) {
        api = NULL;
        nativescript_api = NULL;
    }

Finally we have ``nativescript_init`` which is the most important function we'll need today. This function will be called by Godot as part of loading a GDNative library and communicates back to Godot what objects we make available to Godot.

We first tell Godot which classes are implemented by calling ``nativescript_register_class``. The first parameter here is the handle pointer given to us. The second is the name of our object class. The third is the type of object in Godot that we 'inherit' from, this is not true inheritance but it's close enough. Finally, our fourth and fifth parameters are descriptions for our constructor and destructor.

We then tell Godot about our methods (well our one method in this case), by calling ``nativescript_register_method`` for each method of our class. In our case, that is just ``get_data``. Our first parameter is yet again our handle pointer. The second is again the name of the object class we're registering. The third is the name of our function as it will be known to GDScript. The fourth is our attributes setting. The fifth and final parameter is a description of which function to call when the method gets called.

The descriptions contain the function pointers to the functions themselves. The other two fields in these structs are for specifying per-method userdata. The value in the ``method_data`` field will be passed on every function call as the ``p_method_data`` argument. This is useful to reuse one function for different methods on possibly multiple different script-classes. If the ``method_data`` value is a pointer to memory that needs to be freed, the ``free_func`` field can contain a pointer to a function that will free that memory. That free function gets called when the script itself (not instance!) gets unloaded (so usually at library-unload time).

.. code:: C

    void GDN_EXPORT godot_nativescript_init(void *p_handle) {
        godot_instance_create_func create = { NULL, NULL, NULL };
        create.create_func = &simple_constructor;

        godot_instance_destroy_func destroy = { NULL, NULL, NULL };
        destroy.destroy_func = &simple_destructor;

        nativescript_api->godot_nativescript_register_class(p_handle, "SIMPLE", "Reference",
            create, destroy);

        godot_instance_method get_data = { NULL, NULL, NULL };
        get_data.method = &simple_get_data;

        godot_method_attributes attributes = { GODOT_METHOD_RPC_MODE_DISABLED };

        nativescript_api->godot_nativescript_register_method(p_handle, "SIMPLE", "get_data",
            attributes, get_data);
    }

Now, it's time to start working on the functions of our object. First, we define a structure that we use to store the member data of an instance of our GDNative class. 

.. code:: C

    typedef struct user_data_struct {
        char data[256];
    } user_data_struct;

And then, we define our constructor. All we do in our constructor is allocate memory for our structure and fill it with some data. Note that we use Godot's memory functions so the memory gets tracked and then return the pointer to our new structure. This pointer will act as our instance identifier in case multiple objects are instantiated.

This pointer will be passed to any of our functions related to our object as a parameter called ``p_user_data``, and can both be used to identify our instance and to access its member data.

.. code:: C

    void *simple_constructor(godot_object *p_instance, void *p_method_data) {        
        user_data_struct *user_data = api->godot_alloc(sizeof(user_data_struct));
        strcpy(user_data->data, "World from GDNative!");

        return user_data;
    }

Our destructor is called when Godot is done with our object and we free our instances' member data.

.. code:: C

    void simple_destructor(godot_object *p_instance, void *p_method_data, void *p_user_data) {
        api->godot_free(p_user_data);
    }

And finally, we implement our get_data function. Data is always sent and returned as variants so in order to return our data, which is a string, we first need to convert our C string to a Godot string object, and then copy that string object into the variant we are returning.

Strings are heap-allocated in Godot, so they have a destructor which frees the memory. Destructors are named ``godot_TYPENAME_destroy``. When a Variant gets created with a String, it references the String. That means that the original String can be "destroyed" to decrease the ref-count. If that does not happen the String memory will leak since the ref-count will never be zero and the memory never deallocated. The returned variant gets automatically destroyed by Godot.

(In more complex operations it can be confusing the keep track of which value needs to be deallocated and which does not. As a general rule: call godot_XXX_destroy when a C++ destructor would be called instead. The String destructor would be called in C++ after the Variant was created, so the same is necessary in C)

The variant we return is destroyed automatically by Godot.

.. code:: C

    godot_variant simple_get_data(godot_object *p_instance, void *p_method_data,
            void *p_user_data, int p_num_args, godot_variant **p_args) {
        godot_string data;
        godot_variant ret;
        user_data_struct * user_data = (user_data_struct *) p_user_data;

        api->godot_string_new(&data);
        api->godot_string_parse_utf8(&data, user_data->data);
        api->godot_variant_new_string(&ret, &data);
        api->godot_string_destroy(&data);

        return ret;
    }

And that is the whole source code of our module.

If you add a blank .gdignore file to the src folder, Godot will not try to import the compiler-generated temporary files.

Compiling
---------
We now need to compile our source code. As mentioned our example project on GitHub contains a Scons configuration that does all the hard work for you but for our tutorial here we are going to call the compilers directly. 

Assuming you are sticking to the folder structure suggested above it is best to CD into the src subfolder in a terminal session and execute the commands from there. Make sure to create the bin folder before you proceed.

On Linux:

.. code-block:: none

    clang -std=c11 -fPIC -c -I/PATH/TO/GODOT/HEADERS simple.c -o simple.os
    clang -shared simple.os -o ../bin/libsimple.so

On Mac OS X:

.. code-block:: none

    clang -std=c11 -fPIC -c -I/PATH/TO/GODOT/HEADERS simple.c -o simple.os -arch i386 -arch x86_64
    clang -dynamiclib simple.os -o ../bin/libsimple.dylib -arch i386 -arch x86_64

On Windows:

.. code-block:: none

    cl /Fosimple.obj /c simple.c /nologo -EHsc -DNDEBUG /MD /I. /IC:\PATH\TO\GODOT\HEADERS
    link /nologo /dll /out:..\bin\libsimple.dll /implib:..\bin\libsimple.lib simple.obj

.. note:: on the Windows build you also end up with a libsimple.lib library. This is a library that you can compile into a project to provide access to the DLL. We get it as a bonus and we do not need it :) When exporting your game for release this file will be ignored.

Creating our GDNLIB file
------------------------
With our module compiled we now need to create a gdnlib file for our module which we place alongside our dynamic libraries. This file tells Godot what dynamic libraries are part of our module and need to be loaded per platform. At the time of writing this tutorial work is still being done on making this configurable from within Godot so for now grab your favourite text editor, create a file called libsimple.gdnlib and add the following into this file:

.. code-block:: none

    [general]

    singleton=false
    load_once=true
    symbol_prefix="godot_"

    [entry]

    X11.64="res://bin/libsimple.so"
    Windows.64="res://bin/libsimple.dll"
    OSX.64="res://bin/libsimple.dylib"

    [dependencies]

    X11.64=[]
    Windows.64=[]
    OSX.64=[]

This file contains 3 sections.

The **general** section contains some info that tells Godot how to use our module.

If singleton is true our library is automatically loaded and a function called godot_singleton_init is called. We'll leave that for another tutorial.

If load_once is true our library is loaded only once and each individual script that uses our library will use the same data. Any variable you define globally will be accessible from any instance of your object you create. If load_once is false a new copy of the library is loaded into memory each time a script access the library.

The symbol_prefix is a prefix for our core functions. So the godot in godot_nativescript_init for instance. If you use multiple GDnative libraries that you wish to statically link you'll have to use different prefixes. This again is a subject to dive into deeper in a separate tutorial, it is only needed at this time for deployment to iOS as this platform does not like dynamic libraries.

The **entry** section tells us for each platform and feature combination which dynamic library has to be loaded. This also informs the exporter which files need to be exported when exporting to a specific platform.

The **dependencies** section tells Godot what other files need to be exported for each platform in order for our library to work. Say that your GDNative module uses another DLL to implement functionality from a 3rd party library, this is where you list that DLL.

Putting it all together
-----------------------
Now that we should have a working GDNative library it is time to fire up Godot and use it. Open up the sample project if you haven't left it open after creating the project all the way at the beginning of this tutorial.

Creating our GDNS file
----------------------
With our GDNLIB file we've told Godot how to load our library, now we need to tell it about our "Simple" object class. This we do by creating a GDNS resource file.

Start by clicking the create resource button in the Inspector:

.. image:: img/new_resource.gif

And select NativeScript:

.. image:: img/nativescript_resource.png

Press Create, now the inspector will show a few fields we need to enter. In Class Name we enter "SIMPLE" which is the object class name we used in our C source when calling godot_nativescript_register_class. We also need to select our GDNLIB file by clicking on Library and selecting Load:

.. image:: img/nativescript_library.png

Finally click on the save icon and save this as bin/simple.gdns:

.. image:: img/save_gdns.gif

Now it's time to build our scene. Add a control node to your scene as your root and call it main. Then add a button and a label as subnodes. Place them somewhere nice on screen and give your button a name.

.. image:: img/c_main_scene_layout.png

Select the control node and create a script for the control node:

.. image:: img/add_main_script.gif

Next link up the pressed signal on the button to your script:

.. image:: img/connect_button_signal.gif

Don't forget to save your scene, call it main.tscn.

Now we can implement our main.gd code:

::

    extends Control

    # load the SIMPLE library
    onready var data = preload("res://bin/simple.gdns").new()

    func _on_Button_pressed():
        $Label.text = "Data = " + data.get_data()

After all that, our project should work. The first time you run it Godot will ask you what your main scene is and you select your main.tscn file and presto:

.. image:: img/c_sample_result.png
