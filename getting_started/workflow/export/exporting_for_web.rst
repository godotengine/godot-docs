.. _doc_exporting_for_web:

Exporting for the Web
=====================

HTML5 export allows publishing games made in Godot Engine to the browser.
This requires support for the recent technologies `WebAssembly
<https://webassembly.org/>`__ and `WebGL 2.0 <https://www.khronos.org/webgl/>`__
in the user's browser. **Firefox** and **Chromium** (Chrome, Opera) are
the most popular supported browsers, **Safari** and **Edge** do not work yet.
On **iOS**, all browsers must be based on WebKit (i.e. Safari), so they will also
not work.

Limitations
-----------

For security and privacy reasons, many features that work effortlessly on
native platforms are more complicated on the web platform. Following is a list
of limitations you should be aware of when porting a Godot game to the web.

Exported ``.html`` file must not be reused
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On export, several text placeholders are replaced in the **generated HTML
file** specifically for the given export options. It must not be reused in
further exports.

Using cookies for data persistence
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Users must **allow cookies** (specifically IndexedDB) if persistence of the
``user://`` file system is desired. When playing a game presented in an
``iframe``, **third-party** cookies must also be enabled. Incognito/private
browsing mode also prevents persistence.

The method ``OS.is_userfs_persistent()`` can be used to check if the
``user://`` file system is persistent, but can give false positives in some
cases.

Full screen and mouse capture
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Browsers do not allow arbitrarily **entering full screen** at any time. The same
goes for **capturing the cursor**. Instead, these actions have to occur as a
response to a JavaScript input event. In Godot, this is most easily done by
entering full screen from within an input callback such as ``_input`` or
``_unhandled_input``.

For the same reason, the full screen project setting is ignored.

HTTPClient
~~~~~~~~~~

The ``HTTPClient`` implementation for the HTML5 platform has several
restrictions:

 -  Accessing or changing the ``StreamPeer`` is not possible
 -  Blocking mode is not available
 -  Cannot progress more than once per frame, so polling in a loop will freeze
 -  No chunked responses
 -  Host verification cannot be disabled
 -  Subject to `same-origin policy <https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy>`_

Unimplemented functionality
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following functionality is currently unavailable on the HTML5 platform:

 -  Threads
 -  GDNative
 -  Clipboard synchronisation between engine and operating system
 -  Networking other than ``HTTPClient``

Check the `list of open HTML5 issues on Github <https://github.com/godotengine/godot/issues?q=is:open+is:issue+label:platform:html5>`_
to see if functionality you're interested in has an issue yet. If not, open one
to communicate your interest.

Starting exported games from the local file system
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Many browsers, Chromium-based browsers specifically, will not load exported
projects when **opened locally** per ``file://`` protocol. To get around this,
use a local server.

Python offers an easy method for this, using ``python -m SimpleHTTPServer``
with Python 2 or ``python -m http.server`` with Python 3 will serve the current
working directory on ``http://localhost:8000``.

Serving the files
-----------------

Exporting for the web generates several files to be served from a web server,
including a default HTML page for presentation. A custom HTML file can be
used, see :ref:`doc_customizing_html5_shell`.

The generated ``.html`` file can be used as ``DirectoryIndex`` in Apache
servers and can be renamed to e.g. ``index.html`` at any time, its name is
never depended on by default.

The HTML page is designed to fit the game perfectly without cutting off
parts of the canvas when the browser window is scaled to the game's dimensions.
This way it can be inserted into an ``<iframe>`` with the game's size, as is
common on most web game hosting sites.

The other exported files are served as they are, next to the ``.html`` file,
names unchanged. The ``.wasm`` file is a binary WebAssembly module implementing
the engine. The ``.pck`` file is the Godot main pack containing your game. The
``.js`` file contains start-up code and is used by the ``.html`` file to access
the engine. The ``.png`` file contains the boot splash image. It is not used in
the default HTML page, but is included for
:ref:`custom HTML pages <doc_customizing_html5_shell>`.

The ``.pck`` file is binary, usually delivered with the MIME-type
``application/octet-stream``. The ``.wasm`` file is delivered as
``application/wasm``.

Delivering the files with server-side compression is recommended especially for
the ``.pck`` and ``.wasm`` files, which are usually large in size.
The WebAssembly module compresses particularly well, down to around a quarter
of its original size with gzip compression.

Export options
--------------

If a runnable web export template is available, a button appears between the
*Stop scene* and *Play edited Scene* buttons in the editor to quickly open the
game in the default browser for testing.

If a path to a **Custom HTML shell** file is given, it will be used instead of
the default HTML page. See :ref:`doc_customizing_html5_shell`.

**Head Include** is appended into the ``<head>`` element of the generated
HTML page. This allows to, for example, load webfonts and third-party
JavaScript APIs, include CSS, or run JavaScript code.

Turning on **Export with Debug** when exporting will, in addition to enabling
various debug features of the engine, display a debug output below the canvas
when using the default HTML page, displaying JavaScript and engine errors.
You can also use the browser-integrated developer console, usually opened with
the F12 key, which often shows more information, including WebGL errors.

.. _doc_javascript_eval:

Calling JavaScript from script
------------------------------

In web builds, the ``JavaScript`` singleton is implemented. If offers a single
method called ``eval`` that works similarly to the JavaScript function of the
same name. It takes a string as an argument and executes it as JavaScript code.
This allows interacting with the browser in ways not possible with script
languages integrated into Godot.

::

    func my_func():
        JavaScript.eval("alert('Calling JavaScript per GDScript!');")

The value of the last JavaScript statement is converted to a GDScript value and
returned by ``eval()`` under certain circumstances:

 * JavaScript ``number`` is returned as GDScript :ref:`class_float`
 * JavaScript ``boolean`` is returned as GDScript :ref:`class_bool`
 * JavaScript ``string`` is returned as GDScript :ref:`class_String`
 * JavaScript ``ArrayBuffer``, ``TypedArray`` and ``DataView`` are returned as
   GDScript :ref:`class_PoolByteArray`

::

    func my_func2():
        var js_return = JavaScript.eval("var myNumber = 1; myNumber + 2;")
        print(js_return) # prints '3.0'

Any other JavaScript value is returned as ``null``.

HTML5 export templates may be built without support for the singleton. With such
templates, and on platforms other than HTML5, calling ``JavaScript.eval`` will
also return ``null``.  The availability of the singleton can be checked with the
``JavaScript`` :ref:`feature tag <doc_feature_tags>`::

    func my_func3():
        if OS.has_feature('JavaScript'):
            JavaScript.eval("console.log('The JavaScript singleton is available')")
        else:
            print("The JavaScript singleton is NOT available")

The ``eval`` method also accepts a second, optional Boolean argument, which
specifies whether to execute the code in the global execution context,
defaulting to ``false`` to prevent polluting the global namespace::

    func my_func4():
        # execute in global execution context,
        # thus adding a new JavaScript global variable `MyGlobal`
        JavaScript.eval("var SomeGlobal = {};", true)
