.. _doc_exporting_for_web:

Exporting for the Web
=====================

Exporting for the web generates several files to be served from a web server,
including a default HTML page for presentation. A custom HTML file can be
used, see :ref:`doc_compiling_for_web`.

The default HTML file is designed to fit the game perfectly without cutting off
parts of the canvas when the browser window is scaled to the game's dimensions.
This way it can be inserted into an ``<iframe>`` with the game's size, as is
common on most web game hosting sites.

Serving the files
-----------------

The generated ``.html`` file can be used as ``DirectoryIndex`` and can be
renamed to e.g. ``index.html`` at any time, its name is never depended on.
It can also be inserted into another HTML file as an ``<iframe>`` element.
Users must allow **third-party** cookies when playing a game presented in an
iframe.

The ``.mem``, ``.pck`` (and ``.wasm`` when using WebAssembly) files are
binary, usually delivered with MIME-type ``application/octet-stream``.

Delivering the files with gzip compression is recommended especially for the
``.pck``, ``.asm.js``, ``.mem`` and ``.wasm`` files, which are usually large in
size. The WebAssembly binary (``.wasm``) file compresses particularly well.

Export options
--------------

Turning on **Debugging Enabled** when exporting will, in addition to enabling
various debug features of the engine, display a debug output below the canvas,
displaying JavaScript and engine errors. If controls are
enabled as well, display of this output can be toggled.
You can also use the browser-integrated developer console, usually opened with
the F12 key, which often shows more information, including WebGL errors.

**Memory Size** is fixed and must thus be set during export. Try using no more
than necessary to strain users' browsers as little as possible.
For WebAssembly builds, memory growth is enabled, so this only sets the
initially allocated amount, which will grow as needed.

**Enable Run** will add a button between the *Stop scene* and *Play edited Scene*
buttons in the editor to quickly open the game in the default browser for
testing.

The remaining options customize the generated HTML page:

**Title** is the content of the ``<title>`` element of the page, usually used by
browsers as the tab and window name. The title set here is only displayed until
the game is started, afterwards the title is set to the application name set in
the project settings.

**Head Include** and **Style Include** are appended into the ``<head>`` and
CSS ``<style>`` elements respectively. This allows, for example, linking
web fonts for use in the page.

**Font Family** is the CSS ``font-family`` used on the page, without terminating
semicolon.

**Controls Enabled** toggles display of controls, offering e.g. a toggle for
output display in debug mode and a fullscreen button.
In the default page, the controls are displayed in the top-right corner on top
of the canvas, which can get in the way in games that use the cursor.

Security restrictions
---------------------

Browsers do not allow arbitrarily **entering full screen** at any time. The same
goes for **capturing the cursor**. Instead, these actions have to occur as a
response to a JavaScript input event. In Godot, this is most easily done by
entering full screen from within an ``_input()`` callback.

Chromium-derived browsers will not load exported projects when
**opened locally** per ``file://`` protocol. To get around this, you can start
the browser with the ``--allow-file-access-from-files`` flag, or use a local
server. Python offers an easy way for this, using ``python -m SimpleHTTPServer``
with Python 2 or ``python -m http.server`` with Python 3 will serve the
current working directory on ``http://localhost:8000``.

Locale
------

Godot tries to detect the user's locale using information provided by the
browser, but this is rather unreliable. A better way is to use CGI to read the
HTTP ``Accept-Language`` header. If you assign its value to the JavaScript
property ``Module.locale`` after the ``Module`` objects is created, but before
the engine starts, Godot will use that value to initialize the locale.
In any case, users should always be offered the option to configure the locale
manually.

Calling JavaScript from script
------------------------------

In web builds, the ``JavaScript`` singleton is available. If offers a single
method called ``eval`` that works similarly to the JavaScript function of the
same name. It takes a string as an argument and executes it as JavaScript code.
This allows interacting with the browser in ways not possible with script
languages integrated into Godot.

In order to keep your code compatible with other platforms, check if the
JavaScript singleton is available before using it::

    var JavaScript

    func _ready():
        # retrieve the singleton here, will return `null` on platforms other than web
        JavaScript = Globals.get_singleton("JavaScript")

    func my_func():
        # call JavaScript.eval only if available
        if JavaScript:
            JavaScript.eval("alert('Calling JavaScript per GDScript!');")

The return value of the last JavaScript statement is converted to a GDScript
value and returned by ``eval()`` under certain circumstances:

 * JavaScript ``number`` is returned as GDScript :ref:`class_int` if it is an
   integer or as :ref:`class_float` otherwise
 * JavaScript ``boolean`` is returned as GDScript :ref:`class_bool`
 * JavaScript ``string`` is returned as GDScript :ref:`class_String`
 * JavaScript ``object`` is only converted and returned if it has certain
   ``Number``-type properties, listed in order of priority:

    * Objects with ``x``, ``y`` and ``z`` properties are returned as a :ref:`class_Vector3`
    * Objects with ``x``, ``y``, ``width`` and ``height`` properties are returned as a :ref:`class_Rect2`
    * Objects with ``x`` and ``y`` properties are returned as a :ref:`class_Vector2`
    * Objects with an ``r``, ``g``, ``b`` and an optional ``a``  property are
      returned as a :ref:`class_Color`, the JavaScript values are interpreted
      as 8-bit values (0-255)

Any other JavaScript value is returned as ``null``.

The ``eval`` method also accepts a second, optional Boolean argument, which
specifies whether to execute the code in the global execution context,
defaulting to ``false`` to prevent polluting the global namespace::

    func my_func2():
        if JavaScript:
            # execute in global execution context,
            # thus adding a new JavaScript global variable `MyGlobal`
            JavaScript.eval("var MyGlobal = {};", true)
