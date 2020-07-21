.. _doc_getting_start_with_gdnative_cc++:

Getting Start With GDNative C++
==================

Introduction
------------

This tutorial will give you the basic knowlage to start working with GDNative C++
Before we begin, you should be familiar with godot and scons.


What are the pros and cons?
------------

Pros:

-High performance.

-Ability to add third part libraries and customization.

Cons:

-Debugging Could be hard.

-Each platform need its own dll


What is DLL?
-------------

DLL or Dynamic Link Library, Is Library of Functions and Data that can be called by the programme/game.
It get generated after compiling.

Prerequisites
-------------
Before we start you'll need :

1-Visual Studio 2015 or later.

2-Scons.

3-copy of the <https://github.com/GodotNativeTools/godot-cpp> repository.(Make sure you have godot_headers inside it).

Plane Structor
-------------------------

The files we will cover should be orgnized well, in order to avoid mistakes.
There for the Structor should me

- godot-cpp

-Folder/Your project

  * /Your Cpp project
  * /Your SConstruct file

Building the C++ bindings
-------------------------

This is an important step, Now that we have downloaded godot-cpp file, 
Put it in a safe folder.
And Open Native Tools Command Prompt (if you don't find it, make sure you installed Visual Studio right)

 .. code-tab:: none Godot 3.0
    cd godot-cpp 
    scons p=windows generate_bindings=yes -j4

This will generate .lib file in the bin of the godot-cpp folder



Setting up the Cpp project.
-------------------
Now that we got our Library ready, time to open a C++ project in Visual studio.
After opening a C++ project and setting up the include files, we can go to the next step

Node: if you don't use visual studio you can still follow along.

Setting SConstruct
-------------------
Download This SConstruct File.

And edit this parameters 

"Path to your project/bin" (if there is no bin folder, create one)

"Name of your library" (something like "Projectname_lib")

"Path to cpp files" (This must show cpp files, not the folder that has a folder that contains cpp files)

"Path to cpp files"*cpp (its same as first one, dont remove the *cpp)

"../godot-cpp/godot_headers"

"../godot-cpp/" // If you follow the structor that i showed you, you don't need to change this two. but in case you didn't follow , change them to godot-cpp and godot_headers

important node: whats inside "" and '' , don't replace them as well.



First Cpp file.
-------------------

The first Cpp file that you should make is the entry to the library, its very important as it will tell godot some important information about the DLL file.
Maake cpp files and call it something like "Nativlib"

 .. code-tab:: none Godot 3.0
   #include <Godot.hpp>
    using namespace std;
    using namespace godot;
    #include "Script1.h"
    #include "Script2.h"
    extern "C" void GDN_EXPORT godot_gdnative_init(godot_gdnative_init_options * o) {
    godot::Godot::gdnative_init(o);
    }

    extern "C" void GDN_EXPORT godot_gdnative_terminate(godot_gdnative_terminate_options * o) {
    godot::Godot::gdnative_terminate(o);
    }

    extern "C" void GDN_EXPORT godot_nativescript_init(void* handle) {
    godot::Godot::nativescript_init(handle);

    godot::register_class<Script1>();
    godot::register_class<Script2>();
    }
After you make this file it is expect that you will have errors, since we don't have Script1 and Script2.

that's why we are going to create them.
create a .cpp and .h with the same name.

and follow this structor:
In the Header file (.h):
    .. code-tab:: none Godot 3.0
      #pragma once
      #include "Commen.h"  // it has #include <Godot.hpp> using namespace std; using namespace godot;
      #include <WhatEveryYouNeed.hpp>
    
      class Name : public NodeType {

	    GODOT_CLASS(Name, NodeType);
      //You can have here a list of variables that you may want declare.

      public:
      	static void _register_methods(); //This tells godot what functions there are in the script, and ITS A MUST!!
       	void _init();                    //This function happen when godot finishes settings everything, ITS A MUST even if you don't fill it up
        void _ready();                  // normal ready function (remove it if you don't need it)
       	void _physics_process(float delta); // normal _physics_process function (remove it if you don't need it)
       	void _input(Object event); // normal input function (remove it if you don't need it)
        void YourOWnCustomFunction; // you must decalre your function here before setting its body on the cpp file.
        };


in the cpp file (.cpp):
    .. code-tab:: none Godot 3.0
      #include "YourSameNameHeader.h"
      #include <Anything you need.hpp>
    
      void Name::_register_methods() // This is aa must
      {
       // in this file declare every single function you have in the code, using same patten just changing the names.
 
      register_method("_ready", &Player::_ready);
      register_method("_physics_process", &Player::_physics_process);
      register_method("YourCustomFunction", &Player::YourCustomFunction);
      
        // you don't have to declare _init()
      }

      void name::_init()
      {
	      // you can leave it empty, or fill it with stuff you need when godot finishes setting up the code.
      }
      void name::_ready(){ 
      Godot::print("My first cpp file , YAY"); // this will print the text  on the output in godot.
      }
      void name::_physics_process(){ 
     
      }

Now that we have the files, we need to set them on the Nativlib file,
     .. code-tab:: none Godot 3.0
      #include <Godot.hpp>
      using namespace std;
      using namespace godot;
      #include "name.h"
      extern "C" void GDN_EXPORT godot_gdnative_init(godot_gdnative_init_options * o) {
      godot::Godot::gdnative_init(o);
      }

      extern "C" void GDN_EXPORT godot_gdnative_terminate(godot_gdnative_terminate_options * o) {
      godot::Godot::gdnative_terminate(o);
      }

      extern "C" void GDN_EXPORT godot_nativescript_init(void* handle) {
      godot::Godot::nativescript_init(handle);

      godot::register_class<name>();
      }
Then we are ready to compile.

Compiling and setting the file in Godot.
-------------------
After you made sure that you made your first code work (by replacing the place holders)
Its time to compile, using native commend go to the SConstruct.
    .. code-tab:: none Godot 3.0
    scons p=windows
And wait for it to compile.

Nodes: if you got any errors, Check the paths you set up at SConstruct and the code.

If everything worked well you will end up with DLL file in your godot project.

Now we need to set up the script in godot project it self.

Make GDNativeLibrary and fill the inputs based on your export.
Then make NativeScript. fill it as shown here:
Class name : The name of the class you made in the code
Library : The GDNativeLibrary we just created
Drag the NativeScript file into your node, and try it out, if something went wrong then check the code and debug it.



Important notes
-------------------

When making NativeScript any mistake will result in Godot crach.
So double check that all the data you are using in the cpp file are valid when needed.

The DLL file and the blinking lib is set up for debug export,
If you want to go for release export, make the release vesrion of Building C++ lib, then the release version of the DLL.

During your c++ coding you will have alot of problems that requare you to know C++ very well and not godot headers problem.
