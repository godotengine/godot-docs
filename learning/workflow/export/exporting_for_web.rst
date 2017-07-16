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

Web export uses *asm.js*, a highly optimizable subset of JavaScript.
A 64-bit browser is required to run games in asm.js format. Most notably,
this is a problem with Firefox, which on Windows is shipped as a
32-bit application by default.

Serving the files
-----------------

The default ``.html`` file can be used as ``DirectoryIndex`` and can be
renamed to e.g. ``index.html`` at any time, its name is never depended on.
It can also be inserted into another HTML file as an ``<iframe>`` element.
Users must allow **third-party** cookies when playing a game presented in an
iframe.

The other exported files are served as they are next to the ``.html`` file,
names unchanged.

The ``.mem`` and ``.pck`` files are binary, usually delivered with the
MIME-type ``application/octet-stream``.

Delivering the files with gzip compression is recommended especially for the
``.pck``, ``.asm.js`` and ``.mem`` files, which are usually large in size.

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

Web export limitations
----------------------

Exported files must not be reused
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The exported files ending with ``.html`` and ``fs.js`` are adjusted on export
specifically for that game's version and the given export options. They must
not be reused in futher exports.

Some functions must be called from input callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Browsers do not allow arbitrarily **entering full screen** at any time. The same
goes for **capturing the cursor**. Instead, these actions have to occur as a
response to a JavaScript input event. In Godot, this is most easily done by
entering full screen from within an input callback such as ``_input`` or
``_unhandled_input``.

Starting exported games from the local file system
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Many browsers will not load exported projects when **opened locally**
per ``file://`` protocol. To get around this, use a local server.

Python offers an easy method for this, using ``python -m SimpleHTTPServer``
with Python 2 or ``python -m http.server`` with Python 3 will serve the current
working directory on ``http://localhost:8000``.

Locale lookup
~~~~~~~~~~~~~

Godot tries to detect the user's locale using information provided by the
browser, but this is rather unreliable. A better way is to use CGI to read the
HTTP ``Accept-Language`` header. If you assign its value to the JavaScript
property ``Module.locale`` after the ``Module`` objects is created, but before
the engine starts, Godot will use that value to initialize the locale.
In any case, users should always be offered the option to configure the locale
manually.
