.. _doc_creating_android_modules:

Creating Android modules
========================

Introduction
------------

Making video games portable is all fine and dandy, until mobile
gaming monetization shows up.

This area is complex, usually a mobile game that monetizes needs
special connections to a server for stuff such as:

-  Analytics
-  In-app purchases
-  Receipt validation
-  Install tracking
-  Ads
-  Video ads
-  Cross-promotion
-  In-game soft & hard currencies
-  Promo codes
-  A/B testing
-  Login
-  Cloud saves
-  Leaderboards and scores
-  User support & feedback
-  Posting to Facebook, Twitter, etc.
-  Push notifications

Oh yeah, developing for mobile is a lot of work. On iOS, you can just
write a C++ module and take advantage of the C++/ObjC
intercommunication, so this is rather easy.

For C++ developers Java is a pain, the build system is severely bloated
and interfacing it with C++ through JNI (Java Native Interface) is more
pain that you don't want even for your worst enemy.

Maybe REST?
-----------

Most of these APIs allow communication via REST+JSON APIs. Godot has
great support for HTTP, HTTPS and JSON, so consider this as an option
that works in every platform. Only write the code once and you are set
to go.

Popular engines that have half the share of apps published on mobile get
special plugins written just for them. Godot does not have that luxury
yet. So, if you write a REST implementation of a SDK for Godot, please
share it with the community.

Android module
--------------

Writing an Android module is similar to :ref:`doc_custom_modules_in_c++`, but
needs a few more steps.

Make sure you are familiar with building your own :ref:`Android export templates <doc_compiling_for_android>`,
as well as creating :ref:`doc_custom_modules_in_c++`.

config.py
~~~~~~~~~

In the config.py for the module, some extra functions are provided for
convenience. First, it's often wise to detect if android is being built
and only enable building in this case:

.. code:: python

    def can_build(plat):
        return plat=="android"

If more than one platform can be built (typical if implementing the
module also for iOS), check manually for Android in the configure
functions:

.. code:: python

    def can_build(plat):
        return plat=="android" or plat=="iphone"

    def configure(env):
        if env['platform'] == 'android':
            # android specific code

Java singleton
--------------

An android module will usually have a singleton class that will load it,
this class inherits from ``Godot.SingletonBase``. A singleton object
template follows:

.. code:: java

    // package com.android.godot; // for 1.1
    package org.godotengine.godot; // for 2.0

    public class MySingleton extends Godot.SingletonBase {

        public int myFunction(String p_str) {
            // a function to bind
        }

        static public Godot.SingletonBase initialize(Activity p_activity) {
            return new MySingleton(p_activity);
        } 

        public MySingleton(Activity p_activity) {
            //register class name and functions to bind
            registerClass("MySingleton", new String[]{"myFunction"});

            // you might want to try initializing your singleton here, but android
            // threads are weird and this runs in another thread, so you usually have to do
            activity.runOnUiThread(new Runnable() {
                    public void run() {
                        //useful way to get config info from engine.cfg
                        String key = GodotLib.getGlobal("plugin/api_key");
                        SDK.initializeHere();
                    }
            });

        }

        // forwarded callbacks you can reimplement, as SDKs often need them

        protected void onMainActivityResult(int requestCode, int resultCode, Intent data) {}

        protected void onMainPause() {}
        protected void onMainResume() {}
        protected void onMainDestroy() {}

        protected void onGLDrawFrame(GL10 gl) {}
        protected void onGLSurfaceChanged(GL10 gl, int width, int height) {} // singletons will always miss first onGLSurfaceChanged call

    }

Calling back to Godot from Java is a little more difficult. The instance
ID of the script must be known first, this is obtained by calling
``get_instance_ID()`` on the script. This returns an integer that can be
passed to Java.

From Java, use the ``calldeferred`` function to communicate back with Godot.
Java will most likely run in a separate thread, so calls are deferred:

.. code:: java

    GodotLib.calldeferred(<instanceid>, "<function>", new Object[]{param1,param2,etc});

Add this singleton to the build of the project by adding the following
to config.py:

(Before Version 2.0)

.. code:: python

    def can_build(plat):
        return plat=="android" or plat=="iphone"

    def configure(env):
        if env['platform'] == 'android':
            # will copy this to the java folder
            env.android_module_file("MySingleton.java")
            #env.android_module_file("MySingleton2.java") call again for more files


(After Version 2.0)

.. code:: python

    def can_build(plat):
        return plat=="android" or plat=="iphone"

    def configure(env):
        if env['platform'] == 'android':
            # will copy this to the java folder
            env.android_add_java_dir("Directory that contain MySingleton.java")



AndroidManifest
---------------

Some SDKs need custom values in AndroidManifest.xml. Permissions can be
edited from the godot exporter so there is no need to add those, but
maybe other functionalities are needed.

Create the custom chunk of android manifest and put it inside the
module, add it like this:

(Before Version 2.0)

.. code:: python

    def can_build(plat):
        return plat=="android" or plat=="iphone"

    def configure(env):
        if env['platform'] == 'android':
            # will copy this to the java folder
            env.android_module_file("MySingleton.java") 
            env.android_module_manifest("AndroidManifestChunk.xml")

(After Version 2.0)

.. code:: python

    def can_build(plat):
        return plat=="android" or plat=="iphone"

    def configure(env):
        if env['platform'] == 'android':
            # will copy this to the java folder
            env.android_add_java_dir("Directory that contain MySingelton.java") 
            env.android_add_to_manifest("AndroidManifestChunk.xml")

SDK library
-----------

So, finally it's time to add the SDK library. The library can come in
two flavors, a JAR file or an Android project for ant. JAR is the
easiest to integrate, just put it in the module directory and add it:

(Before Version 2.0)

.. code:: python

    def can_build(plat):
        return plat=="android" or plat=="iphone"

    def configure(env):
        if env['platform'] == 'android':
            # will copy this to the java folder
            env.android_module_file("MySingleton.java") 
            env.android_module_manifest("AndroidManifestChunk.xml")
            env.android_module_library("MyLibrary-3.1.jar")
            

(After Version 2.0)  

.. code:: python

    def can_build(plat):
        return plat=="android" or plat=="iphone"

    def configure(env):
        if env['platform'] == 'android':
            # will copy this to the java folder
            env.android_add_java_dir("Directory that contain MySingelton.java") 
            env.android_add_to_manifest("AndroidManifestChunk.xml")
            env.android_add_dependency("compile files('something_local.jar')") # if you have a jar, the path is relative to platform/android/java/gradlew, so it will start with ../../../modules/module_name/
            env.android_add_maven_repository("maven url") #add a maven url
            env.android_add_dependency("compile 'com.google.android.gms:play-services-ads:8'") #get dependency from maven repository
           

SDK project
-----------

When this is an Android project, things usually get more complex. Copy
the project folder inside the module directory and configure it:

::

    c:\godot\modules\mymodule\sdk-1.2> android -p . -t 15

As of this writing, Godot uses minsdk 10 and target sdk 15. If this ever
changes, it should be reflected in the manifest template:
`AndroidManifest.xml.template <https://github.com/godotengine/godot/blob/master/platform/android/AndroidManifest.xml.template>`

Then, add the module folder to the project:

(Before Version 2.0)

.. code:: python

    def can_build(plat):
        return plat=="android" or plat=="iphone"

    def configure(env):
        if env['platform'] == 'android':
            # will copy this to the java folder
            env.android_module_file("MySingleton.java") 
            env.android_module_manifest("AndroidManifestChunk.xml")
            env.android_module_source("sdk-1.2","")

(After Version 2.0)
    
    
Building
--------

As you probably modify the contents of the module, and modify your .java
inside the module, you need the module to be built with the rest of
Godot, so compile android normally.

::

    c:\godot> scons p=android

This will cause your module to be included, the .jar will be copied to
the java folder, the .java will be copied to the sources folder, etc.
Each time you modify the .java, scons must be called.

Afterwards, just continue the steps for compiling android  :ref:`doc_compiling_for_android`.

Using the module
~~~~~~~~~~~~~~~~

To use the module from GDScript, first enable the singleton by adding
the following line to engine.cfg (Godot Engine 2.0 and greater):

::

    [android]

    modules="org/godotengine/godot/MySingleton"

For Godot Engine 1.1 is 

::

    [android]

    modules="com/android/godot/MySingleton"

More than one singleton module can be enabled by separating with commas:

::

    [android]

    modules="com/android/godot/MySingleton,com/android/godot/MyOtherSingleton"

Then just request the singleton Java object from Globals like this:

::

    # in any file

    var singleton = null

    func _init():
        singleton = Globals.get_singleton("MySingleton")
        print(singleton.myFunction("Hello"))

Troubleshooting
---------------

(This section is a work in progress, report your problems here!)

Godot crashes upon load
~~~~~~~~~~~~~~~~~~~~~~~

Check ``adb logcat`` for possible problems, then:

-  Make sure libgodot_android.so is in the ``libs/armeabi`` folder
-  Check that the methods used in the Java singleton only use simple
   Java datatypes, more complex ones are not supported.

Future
------

Godot has an experimental Java API Wrapper that allows to use the
entire Java API from GDScript.

It's simple to use and it's used like this:

::

    class = JavaClassWrapper.wrap(<javaclass as text>)

This is most likely not functional yet, if you want to test it and help
us make it work, contact us through the `developer mailing
list <https://groups.google.com/forum/#!forum/godot-engine>`__.
