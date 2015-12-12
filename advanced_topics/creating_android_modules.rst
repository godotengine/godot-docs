Creating Android modules
========================

Introduction
------------

| Making videogames portable is all fine and dandy, until mobile gaming
  monetization shows up.
| This area is complex, usually a mobile game that monetizes needs
  special connections to a server for stuff such as:

-  Analytics
-  In-app purchases
-  Receipt validation
-  Install tracking
-  Ads
-  Video ads
-  Cross promotion
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

Writing an Android module is similar to [[Custom modules in C++]], but
needs a few more steps.

Make sure you are familiar with building your own [[Compiling for
Android\|Android export templates]], as well as creating [[Custom
modules in C++\|custom modules]].

config.py
~~~~~~~~~

In the config.py for the module, some extra functions are provided for
convenience. First, it's often wise to detect if android is being built
and only enable building in this case:

| <pre class=\\"python\\">
| def can\_build(plat):
| return plat==\\"android\\"

.. raw:: html

   </pre>

If more than one platform can be built (typical if implementing the
module also for iOS), check manually for Android in the configure
functions:

| <pre class=\\"python\\">
| def can\_build(plat):
| return plat\\"android\\" or plat\\"iphone\\"

| def configure(env):
| if env['platform'] == 'android':
| #androd specific code

.. raw:: html

   </pre>

Java singleton
--------------

An android module will usually have a singleton class that will load it,
this class inherits from ``Godot.SingletonBase``. A singleton object
template follows:

| <pre class=\\"java\\">
| //namespace is wrong, will eventually change
| package com.android.godot;

public class MySingleton extends Godot.SingletonBase {

| public int myFunction(String p\_str) {
| // a function to bind
| }

static public Godot.SingletonBase initialize(Activity p\_activity) {

| return new MySingleton(p\_activity);
| }

| public MySingleton(Activity p\_activity) {
| //register class name and functions to bind
| registerClass(\\"MySingleton\\", new String[]{\\"myFunction\\"});

| // you might want to try initializing your singleton here, but android
| // threads are weird and this runs in another thread, so you usually
  have to do
| activity.runOnUiThread(new Runnable() {
| public void run() {
| //useful way to get config info from engine.cfg
| String key = GodotLib.getGlobal(\\"plugin/api\_key\\");
| SDK.initializeHere();
| }
| });

}

// forwarded callbacks you can reimplement, as SDKs often need them

protected void onMainActivityResult(int requestCode, int resultCode,
Intent data) {}

| protected void onMainPause() {}
| protected void onMainResume() {}
| protected void onMainDestroy() {}

| protected void onGLDrawFrame(GL10 gl) {}
| protected void onGLSurfaceChanged(GL10 gl, int width, int height) {}
  // singletons will always miss first onGLSurfaceChanged call

}

.. raw:: html

   </pre>

Calling back to Godot from Java is a little more difficult. The instance
ID of the script must be known first, this is obtained by calling
``get_instance_ID()`` on the script. This returns an integer that can be
passed to Java.

From Java, use the calldeferred function to communicate back with Godot.
Java will most likely run in a separate thread, so calls are deferred:

<pre class=\\"java\\">GodotLib.calldeferred(, \\"\\", new
Object[]{param1,param2,etc});

.. raw:: html

   </pre>

Add this singleton to the build of the project by adding the following
to config.py:

| <pre class=\\"python\\">
| def can\_build(plat):
| return plat\\"android\\" or plat\\"iphone\\"

| def configure(env):
| if env['platform'] == 'android':
| # will copy this to the java folder
| env.android\_module\_file(\\"MySingleton.java\\")
| #env.android\_module\_file(\\"MySingleton2.java\\") call again for
  more files

.. raw:: html

   </pre>

AndroidManifest
---------------

Some SDKs need custom values in AndroidManifest.xml. Permissions can be
edited from the godot exporter so there is no need to add those, but
maybe other functionalities are needed.

Create the custom chunk of android manifest and put it inside the
module, add it like this:

| <pre class=\\"python\\">
| def can\_build(plat):
| return plat\\"android\\" or plat\\"iphone\\"

| def configure(env):
| if env['platform'] == 'android':
| # will copy this to the java folder
| env.android\_module\_file(\\"MySingleton.java\\")
| env.android\_module\_manifest(\\"AndroidManifestChunk.xml\\")

.. raw:: html

   </pre>

SDK library
-----------

So, finally it's time to add the SDK library. The library can come in
two flavors, a JAR file or an Android project for ant. JAR is the
easiest to integrate, just put it in the module directory and add it:

| <pre class=\\"python\\">
| def can\_build(plat):
| return plat\\"android\\" or plat\\"iphone\\"

| def configure(env):
| if env['platform'] == 'android':
| # will copy this to the java folder
| env.android\_module\_file(\\"MySingleton.java\\")
| env.android\_module\_manifest(\\"AndroidManifestChunk.xml\\")
| env.android\_module\_library(\\"MyLibrary-3.1.jar\\")

.. raw:: html

   </pre>

SDK project
-----------

When this is an Android project, things usually get more complex. Copy
the project folder inside the module directory and configure it:

::

    c:\\godot\\modules\\mymodule\\sdk-1.2> android -p . -t 15

As of this writing, godot uses minsdk 10 and target sdk 15. If this ever
changes, should be reflected in the manifest template:

\\\ `https://github.com/okamstudio/godot/blob/master/platform/android/AndroidManifest.xml.template\\ <https://github.com/okamstudio/godot/blob/master/platform/android/AndroidManifest.xml.template>`__

Then, add the module folder to the project:

| <pre class=\\"python\\">
| def can\_build(plat):
| return plat\\"android\\" or plat\\"iphone\\"

| def configure(env):
| if env['platform'] == 'android':
| # will copy this to the java folder
| env.android\_module\_file(\\"MySingleton.java\\")
| env.android\_module\_manifest(\\"AndroidManifestChunk.xml\\")
| env.android\_module\_source(\\"sdk-1.2\\",\\"\\")

.. raw:: html

   </pre>

Building
--------

As you probably modify the contents of the module, and modify your .java
inside the module, you need the module to be built with the rest of
Godot, so compile android normally.

::

    c:\\godot> scons p=android

This will cause your module to be included, the .jar will be copied to
the java folder, the .java will be copied to the sources folder, etc.
Each time you modify the .java scons must be called.

Afterwards, just build the ant project normally:

::

    c:\\godot\\platform\\android\\java> ant release

This should generate the apk used as export template properly, as
defined in the [[Compiling for Android\|Android build instructions]].

Usually to generate the apk, again both commands must be run in
sequence:

::

    c:\\godot> scons p=android
    c:\\godot\\platform\\android\\java> ant release

Using the Module
~~~~~~~~~~~~~~~~

To use the Module from GDScript, first enable the singleton by adding
the following line to engine.cfg:

::

    [android]

    modules=\"com/android/godot/MySingleton\"

More than one singleton module can be enable by separating with comma:

::

    [android]

    modules=\"com/android/godot/MySingleton,com/android/godot/MyOtherSingleton\"

Then just request the singleton Java object from Globals like this:

| <pre class=\\"python\\">
| #in any file

var singleton=null

| func \_init():
| singleton = Globals.get\_singleton(\\"MySingleton\\")
| print( singleton.myFunction(\\"Hello\\") )

.. raw:: html

   </pre>

Troubleshooting
---------------

(This section is a work in progress, report your problems here!)

Godot crashes upon load
~~~~~~~~~~~~~~~~~~~~~~~

Check ``adb logcat`` for possible problems, then:

-  Make sure libgodot\_android.so is in the libs/armeabi folder
-  Check that the methods used in the Java singleton only use simple
   Java datatypes, more complex ones are not supported.

Future
------

| Godot has an experimental Java API Wrapper that allows to use the
  entire Java API fro GDScript.
| It's simple to use and it's used like this:

::

    class = JavaClassWrapper.wrap()

This is most likely not functional yet, if you want to test it and help
us make it work, contact us through the \\\ `developer mailing
list\\ <https://groups.google.com/forum/#!forum/godot-engine>`__.
