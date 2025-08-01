.. _doc_javaclasswrapper_and_androidruntimeplugin:

Integrating with Android APIs
=============================

The Android platform has numerous APIs as well as a rich ecosystem of third-party libraries with wide and
diverse functionality, like push notifications, analytics, authentication, ads, etc...

These don't make sense in Godot core itself so Godot has long provided an :ref:`Android plugin system <doc_android_plugin>`.
The :ref:`Android plugin system <doc_android_plugin>` enables developers to create Godot Android plugins using Java or Kotlin code,
which provides an interface to access and use Android APIs or third-party libraries in Godot projects from GDScript, C# or GDExtension.

.. code-block:: kotlin

    class MyAndroidSingleton(godot: Godot?) : GodotPlugin(godot) {
	    @UsedByGodot
	    fun doSomething(value: String) {
		    // ...
	    }
    }


Writing an Android plugin however requires knowledge of Java or Kotlin code, which most Godot developers do not have. 
As such there are many Android APIs and third-party libraries that don't have a Godot plugin that developers can interface with.
In fact, this is one of the main reasons that developers cite for not being able to switch to Godot from other game engines.

To address this, we've introduced a couple of tools in **Godot 4.4** to simplify the process for developers to access Android APIs and third-party libraries.

JavaClassWrapper (Godot singleton)
----------------------------------

``JavaClassWrapper`` is a :ref:`Godot singleton <class_JavaClassWrapper>` which allows
creating instances of Java / Kotlin classes and calling methods on them using only GDScript, C# or GDExtension.

.. code-block:: gdscript

    var LocalDateTime = JavaClassWrapper.wrap("java.time.LocalDateTime")
    var DateTimeFormatter = JavaClassWrapper.wrap("java.time.format.DateTimeFormatter")

    var datetime = LocalDateTime.now()
    var formatter = DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm:ss")

    print(datetime.format(formatter))

In the code snippet above, ``JavaClassWrapper`` is used from GDScript to access the Java ``LocalDateTime`` and ``DateTimeFormatter`` classes.
Through ``JavaClassWrapper``, we can call the Java classes methods directly from GDScript as if they were GDScript methods.

AndroidRuntime plugin
---------------------

``JavaClassWrapper`` is great, but to do many things on Android, you need access to various Android lifecycle / runtime objects.
``AndroidRuntime`` plugin is a `built-in Godot Android plugin <https://javadoc.io/doc/org.godotengine/godot/latest/org/godotengine/godot/plugin/AndroidRuntimePlugin.html>`_ that allows you to do this.

Combining ``JavaClassWrapper`` and ``AndroidRuntime`` plugin allows developers to access and use Android APIs without switching away from GDScript, or using any tools aside from Godot itself.
This is **huge** for the adoption of Godot for Android development:

- If you need to do something simple, or only use a small part of a third-party library, you don't have to make a plugin
- It allows developers to quickly integrate Android functionality
- It allows developers to create Godot addons using only GDScript and ``JavaClassWrapper`` (no Java or Kotlin needed)

.. note::

    For exports using ``gradle``, Godot will automatically include ``.jar`` or ``.aar`` files it find in the project ``addons`` directory.
    So to use a third-party library, you can just drop its ``.jar`` or ``.aar`` file in the ``addons`` directory, and call its method directly from GDScript using ``JavaClassWrapper``.

Example: Show an Android toast 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: gdscript

    # Retrieve the AndroidRuntime singleton.
    var android_runtime = Engine.get_singleton("AndroidRuntime")
    if android_runtime:
        # Retrieve the Android Activity instance.
        var activity = android_runtime.getActivity()

        # Create a Godot Callable to wrap the toast display logic.
        var toast_callable = func():
            # Use JavaClassWrapper to retrieve the android.widget.Toast class, then make and show a toast using the class APIs.
            var ToastClass = JavaClassWrapper.wrap("android.widget.Toast")
            ToastClass.makeText(activity, "This is a test", ToastClass.LENGTH_LONG).show()

        # Wrap the Callable in a Java Runnable and run it on the Android UI thread to show the toast.
        activity.runOnUiThread(android_runtime.createRunnableFromGodotCallable(toast_callable))

Example: Vibrate the device
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: gdscript

    # Retrieve the AndroidRuntime singleton.
    var android_runtime = Engine.get_singleton("AndroidRuntime")
    if android_runtime:
        # Retrieve the Android Vibrator system service and check if the device supports it.
        var vibrator_service = android_runtime.getApplicationContext().getSystemService("vibrator")
        if vibrator_service and vibrator_service.hasVibrator():
            # Configure and run a VibrationEffect. 
            var VibrationEffect = JavaClassWrapper.wrap("android.os.VibrationEffect")
            var effect = VibrationEffect.createOneShot(500, VibrationEffect.DEFAULT_AMPLITUDE)
            vibrator_service.vibrate(effect)

Example: Accessing inner classes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Java inner classes can be accessed using the ``$`` sign:

.. code-block:: gdscript

    # Accessing 'VERSION' class, which is an inner class from the 'android.os.Build' class.
    var version = JavaClassWrapper.wrap("android.os.Build$VERSION")
    var sdk_int = version.SDK_INT
    if sdk_int == 30:
        # Do something specific on android 11 devices.
    else:
        # All other devices

Example: Calling a constructor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A constructor is invoked by calling a method with the same name as the class.

This example creates an intent to send a text:

.. code-block:: gdscript

    # Retrieve the AndroidRuntime singleton.
    var android_runtime = Engine.get_singleton("AndroidRuntime")
    if android_runtime:
        var Intent = JavaClassWrapper.wrap("android.content.Intent")
        var activity = android_runtime.getActivity()
        var intent = Intent.Intent() # Call the constructor.
        intent.setAction(Intent.ACTION_SEND)
        intent.putExtra(Intent.EXTRA_TEXT, "This is a test message.")
        intent.setType("text/plain")
        activity.startActivity(intent)
