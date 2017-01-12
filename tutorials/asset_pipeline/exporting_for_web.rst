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

The default ``.html`` file can be used as ``DirectoryIndex`` and can be
renamed to e.g. ``index.html`` at any time, its name is never depended on.
It can also be inserted into another HTML file as an ``<iframe>`` element.
Users must allow **third-party** cookies when playing a game presented in an
iframe.

The ``.mem`` and ``.pck`` files are binary, usually delivered with MIME-type
``application/octet-stream``.

Delivering the files with gzip compression is recommended especially for the
``.pck``, ``.asm.js`` and ``.mem`` files, which are usually large in size.

Export options
--------------

Turning on **Debugging Enabled** when exporting will display a debug output
below the canvas, displaying JavaScript and engine errors. If controls are
enabled as well, display of this output can be toggled.

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
