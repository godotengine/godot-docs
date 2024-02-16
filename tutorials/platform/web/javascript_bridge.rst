.. _doc_web_javascript_bridge:

The JavaScriptBridge Singleton
==============================

In web builds, the :ref:`JavaScriptBridge <class_JavaScriptBridge>` singleton
allows interaction with JavaScript and web browsers, and can be used to implement some
functionalities unique to the web platform.

Interacting with JavaScript
---------------------------

Sometimes, when exporting Godot for the Web, it might be necessary to interface
with external JavaScript code like third-party SDKs, libraries, or
simply to access browser features that are not directly exposed by Godot.

The ``JavaScriptBridge`` singleton provides methods to wrap a native JavaScript object into
a Godot :ref:`JavaScriptObject <class_JavaScriptObject>` that tries to feel
natural in the context of Godot scripting (e.g. GDScript and C#).

The :ref:`JavaScriptBridge.get_interface() <class_JavaScriptBridge_method_get_interface>`
method retrieves an object in the global scope.

.. code-block:: gdscript

    extends Node

    func _ready():
        # Retrieve the `window.console` object.
        var console = JavaScriptBridge.get_interface("console")
        # Call the `window.console.log()` method.
        console.log("test")

The :ref:`JavaScriptBridge.create_object() <class_JavaScriptBridge_method_create_object>`
creates a new object via the JavaScript ``new`` constructor.

.. code-block:: gdscript

    extends Node

    func _ready():
        # Call the JavaScript `new` operator on the `window.Array` object.
        # Passing 10 as argument to the constructor:
        # JS: `new Array(10);`
        var arr = JavaScriptBridge.create_object("Array", 10)
        # Set the first element of the JavaScript array to the number 42.
        arr[0] = 42
        # Call the `pop` function on the JavaScript array.
        arr.pop()
        # Print the value of the `length` property of the array (9 after the pop).
        print(arr.length)

As you can see, by wrapping JavaScript objects into ``JavaScriptObject`` you can
interact with them like they were native Godot objects, calling their methods,
and retrieving (or even setting) their properties.

Base types (int, floats, strings, booleans) are automatically converted (floats
might lose precision when converted from Godot to JavaScript). Anything else
(i.e. objects, arrays, functions) are seen as ``JavaScriptObjects`` themselves.

Callbacks
---------

Calling JavaScript code from Godot is nice, but sometimes you need to call a
Godot function from JavaScript instead.

This case is a bit more complicated. JavaScript relies on garbage collection,
while Godot uses reference counting for memory management. This means you have
to explicitly create callbacks (which are returned as ``JavaScriptObjects``
themselves) and you have to keep their reference.

Arguments passed by JavaScript to the callback will be passed as a single Godot
``Array``.

.. code-block:: gdscript

    extends Node

    # Here we create a reference to the `_my_callback` function (below).
    # This reference will be kept until the node is freed.
    var _callback_ref = JavaScriptBridge.create_callback(_my_callback)

    func _ready():
        # Get the JavaScript `window` object.
        var window = JavaScriptBridge.get_interface("window")
        # Set the `window.onbeforeunload` DOM event listener.
        window.onbeforeunload = _callback_ref

    func _my_callback(args):
        # Get the first argument (the DOM event in our case).
        var js_event = args[0]
        # Call preventDefault and set the `returnValue` property of the DOM event.
        js_event.preventDefault()
        js_event.returnValue = ''

Here is another example that asks the user for the `Notification permission <https://developer.mozilla.org/en-US/docs/Web/API/Notifications_API>`__
and waits asynchronously to deliver a notification if the permission is
granted:

.. code-block:: gdscript

    extends Node

    # Here we create a reference to the `_on_permissions` function (below).
    # This reference will be kept until the node is freed.
    var _permission_callback = JavaScriptBridge.create_callback(_on_permissions)

    func _ready():
        # NOTE: This is done in `_ready` for simplicity, but SHOULD BE done in response
        # to user input instead (e.g. during `_input`, or `button_pressed` event, etc.),
        # otherwise it might not work.

        # Get the `window.Notification` JavaScript object.
        var notification = JavaScriptBridge.get_interface("Notification")
        # Call the `window.Notification.requestPermission` method which returns a JavaScript
        # Promise, and bind our callback to it.
        notification.requestPermission().then(_permission_callback)

    func _on_permissions(args):
        # The first argument of this callback is the string "granted" if the permission is granted.
        var permission = args[0]
        if permission == "granted":
            print("Permission granted, sending notification.")
            # Create the notification: `new Notification("Hi there!")`
            JavaScriptBridge.create_object("Notification", "Hi there!")
        else:
            print("No notification permission.")

Can I use my favorite library?
------------------------------

You most likely can. First, you have to
include your library in the page. You can simply customize the
:ref:`Head Include <doc_javascript_export_options>` during export (see below),
or even :ref:`write your own template <doc_customizing_html5_shell>`.

In the example below, we customize the ``Head Include`` to add an external library
(`axios <https://axios-http.com/>`__) from a content delivery network, and a
second ``<script>`` tag to define our own custom function:

.. code-block:: html

    <!-- Axios -->
    <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
    <!-- Custom function -->
    <script>
    function myFunc() {
        alert("My func!");
    }
    </script>

We can then access both the library and the function from Godot, like we did in
previous examples:

.. code-block:: gdscript

    extends Node

    # Here create a reference to the `_on_get` function (below).
    # This reference will be kept until the node is freed.
    var _callback = JavaScriptBridge.create_callback(_on_get)

    func _ready():
        # Get the `window` object, where globally defined functions are.
        var window = JavaScriptBridge.get_interface("window")
        # Call the JavaScript `myFunc` function defined in the custom HTML head.
        window.myFunc()
        # Get the `axios` library (loaded from a CDN in the custom HTML head).
        var axios = JavaScriptBridge.get_interface("axios")
        # Make a GET request to the current location, and receive the callback when done.
        axios.get(window.location.toString()).then(_callback)

    func _on_get(args):
        OS.alert("On Get")


The eval interface
------------------

The ``eval`` method works similarly to the JavaScript function of the same
name. It takes a string as an argument and executes it as JavaScript code.
This allows interacting with the browser in ways not possible with script
languages integrated into Godot.

.. tabs::
 .. code-tab:: gdscript

    func my_func():
        JavaScriptBridge.eval("alert('Calling JavaScript per GDScript!');")

 .. code-tab:: csharp

    private void MyFunc()
    {
        JavaScriptBridge.Eval("alert('Calling JavaScript per C#!');")
    }

The value of the last JavaScript statement is converted to a GDScript value and
returned by ``eval()`` under certain circumstances:

 * JavaScript ``number`` is returned as :ref:`class_float`
 * JavaScript ``boolean`` is returned as :ref:`class_bool`
 * JavaScript ``string`` is returned as :ref:`class_String`
 * JavaScript ``ArrayBuffer``, ``TypedArray``, and ``DataView`` are returned as :ref:`PackedByteArray<class_PackedByteArray>`

.. tabs::
 .. code-tab:: gdscript

    func my_func2():
        var js_return = JavaScriptBridge.eval("var myNumber = 1; myNumber + 2;")
        print(js_return) # prints '3.0'

 .. code-tab:: csharp

    private void MyFunc2()
    {
        var jsReturn = JavaScriptBridge.Eval("var myNumber = 1; myNumber + 2;");
        GD.Print(jsReturn); // prints '3.0'
    }

Any other JavaScript value is returned as ``null``.

HTML5 export templates may be :ref:`built <doc_compiling_for_web>` without
support for the singleton to improve security. With such templates, and on
platforms other than HTML5, calling ``JavaScriptBridge.eval`` will also return
``null``. The availability of the singleton can be checked with the
``web`` :ref:`feature tag <doc_feature_tags>`:

.. tabs::
 .. code-tab:: gdscript

    func my_func3():
        if OS.has_feature('web'):
            JavaScriptBridge.eval("""
                console.log('The JavaScriptBridge singleton is available')
            """)
        else:
            print("The JavaScriptBridge singleton is NOT available")

 .. code-tab:: csharp

    private void MyFunc3()
    {
        if (OS.HasFeature("web"))
        {
            JavaScriptBridge.Eval("console.log('The JavaScriptBridge singleton is available')");
        }
        else
        {
            GD.Print("The JavaScriptBridge singleton is NOT available");
        }
    }

.. tip:: GDScript's multi-line strings, surrounded by 3 quotes ``"""`` as in
         ``my_func3()`` above, are useful to keep JavaScript code readable.

The ``eval`` method also accepts a second, optional Boolean argument, which
specifies whether to execute the code in the global execution context,
defaulting to ``false`` to prevent polluting the global namespace:

.. tabs::
 .. code-tab:: gdscript

    func my_func4():
        # execute in global execution context,
        # thus adding a new JavaScript global variable `SomeGlobal`
        JavaScriptBridge.eval("var SomeGlobal = {};", true)

 .. code-tab:: csharp

    private void MyFunc4()
    {
        // execute in global execution context,
        // thus adding a new JavaScript global variable `SomeGlobal`
        JavaScriptBridge.Eval("var SomeGlobal = {};", true);
    }


.. _doc_web_downloading_files:

Downloading files
-----------------

Downloading files (e.g. a save game) from the Godot Web export to the user's computer can be done by directly interacting with JavaScript, but given it is a
very common use case, Godot exposes this functionality to scripting via
a dedicated :ref:`JavaScriptBridge.download_buffer() <class_JavaScriptBridge_method_download_buffer>`
function which lets you download any generated buffer.

Here is a minimal example on how to use it:

extends Node

.. code-block:: gdscript

    func _ready():
        # Asks the user download a file called "hello.txt" whose content will be the string "Hello".
        JavaScriptBridge.download_buffer("Hello".to_utf8_buffer(), "hello.txt")

And here is a more complete example on how to download a previously saved file:

.. code-block:: gdscript

    extends Node

    # Open a file for reading and download it via the JavaScript singleton.
    func _download_file(path):
        var file = FileAccess.open(path, FileAccess.READ)
        if file == null:
            push_error("Failed to load file")
            return
        # Get the file name.
        var fname = path.get_file()
        # Read the whole file to memory.
        var buffer = file.get_buffer(file.get_len())
        # Prompt the user to download the file (will have the same name as the input file).
        JavaScriptBridge.download_buffer(buffer, fname)

    func _ready():
        # Create a temporary file.
        var config = ConfigFile.new()
        config.set_value("option", "one", false)
        config.save("/tmp/test.cfg")

        # Download it
        _download_file("/tmp/test.cfg")
