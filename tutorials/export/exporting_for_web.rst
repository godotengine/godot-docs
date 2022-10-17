.. _doc_exporting_for_web:

Exporting for the Web
=====================

.. seealso::

    This page describes how to export a Godot project to HTML5.
    If you're looking to compile editor or export template binaries from source instead,
    read :ref:`doc_compiling_for_web`.

HTML5 export allows publishing games made in Godot Engine to the browser.
This requires support for `WebAssembly
<https://webassembly.org/>`__ and `WebGL <https://www.khronos.org/webgl/>`__
in the user's browser.

.. important:: Use the browser-integrated developer console, usually opened
               with :kbd:`F12`, to view **debug information** like JavaScript,
               engine, and WebGL errors.

.. attention:: `There are significant bugs when running HTML5 projects on iOS
               <https://github.com/godotengine/godot/issues?q=is:issue+is:open+label:platform:html5+ios>`__
               (regardless of the browser). We recommend using
               :ref:`iOS' native export functionality <doc_exporting_for_ios>`
               instead, as it will also result in better performance.

.. note::

    If you use Linux, due to
    `poor Firefox WebGL performance <https://bugzilla.mozilla.org/show_bug.cgi?id=1010527>`__,
    it's recommended to play the exported project using a Chromium-based browser
    instead of Firefox.

WebGL version
-------------

Depending on your choice of renderer, Godot can target WebGL 1.0 (*GLES2*) or
WebGL 2.0 (*GLES3*).

WebGL 1.0 is the recommended option if you want your project to be supported
on all browsers with the best performance.

Godot's GLES3 renderer targets high end devices, and the performance using
WebGL 2.0 can be subpar. Some features are also not supported in WebGL 2.0
specifically.

Additionally, while most browsers support WebGL 2.0, this is not yet the case
for **Safari**. WebGL 2.0 support is coming in Safari 15 for macOS, and is not
available yet for any **iOS** browser (all WebKit-based like Safari).
See `Can I use WebGL 2.0 <https://caniuse.com/webgl2>`__ for details.

.. _doc_javascript_export_options:

Export options
--------------

If a runnable web export template is available, a button appears between the
*Stop scene* and *Play edited Scene* buttons in the editor to quickly open the
game in the default browser for testing.

You can choose the **Export Type** to select which features will be available:

- *Regular*: is the most compatible across browsers, will not support threads,
  nor GDExtension.
- *Threads*: will require the browser to support `SharedArrayBuffer
  <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SharedArrayBuffer>`__.
  See `Can I use SharedArrayBuffer <https://caniuse.com/sharedarraybuffer>`__
  for details.

If you plan to use :ref:`VRAM compression <doc_import_images>` make sure that
**Vram Texture Compression** is enabled for the targeted platforms (enabling
both **For Desktop** and **For Mobile** will result in a bigger, but more
compatible export).

If a path to a **Custom HTML shell** file is given, it will be used instead of
the default HTML page. See :ref:`doc_customizing_html5_shell`.

**Head Include** is appended into the ``<head>`` element of the generated
HTML page. This allows to, for example, load webfonts and third-party
JavaScript APIs, include CSS, or run JavaScript code.

.. important:: Each project must generate their own HTML file. On export,
               several text placeholders are replaced in the generated HTML
               file specifically for the given export options. Any direct
               modifications to that HTML file will be lost in future exports.
               To customize the generated file, use the **Custom HTML shell**
               option.

.. warning:: **Export types** other than *Regular* are not yet supported by the
             C# version.

Limitations
-----------

For security and privacy reasons, many features that work effortlessly on
native platforms are more complicated on the web platform. Following is a list
of limitations you should be aware of when porting a Godot game to the web.

.. _doc_javascript_secure_contexts:

.. important:: Browser vendors are making more and more functionalities only
               available in `secure contexts <https://developer.mozilla.org/en-US/docs/Web/Security/Secure_Contexts>`_,
               this means that such features are only be available if the web
               page is served via a secure HTTPS connection (localhost is
               usually exempt from such requirement).

.. tip:: Check the `list of open HTML5 issues on GitHub
         <https://github.com/godotengine/godot/issues?q=is:open+is:issue+label:platform:html5>`__
         to see if the functionality you're interested in has an issue yet. If
         not, open one to communicate your interest.

Using cookies for data persistence
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Users must **allow cookies** (specifically IndexedDB) if persistence of the
``user://`` file system is desired. When playing a game presented in an
``iframe``, **third-party** cookies must also be enabled. Incognito/private
browsing mode also prevents persistence.

The method ``OS.is_userfs_persistent()`` can be used to check if the
``user://`` file system is persistent, but can give false positives in some
cases.

Background processing
~~~~~~~~~~~~~~~~~~~~~

The project will be paused by the browser when the tab is no longer the active
tab in the user's browser. This means functions such as ``_process()`` and
``_physics_process()`` will no longer run until the tab is made active again by
the user (by switching back to the tab). This can cause networked games to
disconnect if the user switches tabs for a long duration.

This limitation does not apply to unfocused browser *windows*. Therefore, on the
user's side, this can be worked around by running the project in a separate
*window* instead of a separate tab.

Threads
~~~~~~~

As mentioned :ref:`above <doc_javascript_export_options>` multi-threading is
only available if the appropriate **Export Type** is set and support for it
across browsers is still limited.

.. warning:: Requires a :ref:`secure context <doc_javascript_secure_contexts>`.
             Browsers also require that the web page is served with specific
             `cross-origin isolation headers <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cross-Origin-Embedder-Policy>`__.

Full screen and mouse capture
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Browsers do not allow arbitrarily **entering full screen**. The same goes for
**capturing the cursor**. Instead, these actions have to occur as a response to
a JavaScript input event. In Godot, this means entering full screen from within
a pressed input event callback such as ``_input`` or ``_unhandled_input``.
Querying the :ref:`class_Input` singleton is not sufficient, the relevant
input event must currently be active.

For the same reason, the full screen project setting doesn't work unless the
engine is started from within a valid input event handler. This requires
:ref:`customization of the HTML page <doc_customizing_html5_shell>`.

Audio
~~~~~

Chrome restricts how websites may play audio. It may be necessary for the
player to click or tap or press a key to enable audio.

.. seealso:: Google offers additional information about their `Web Audio autoplay
             policies <https://sites.google.com/a/chromium.org/dev/audio-video/autoplay>`__.

.. warning:: Access to microphone requires a
             :ref:`secure context <doc_javascript_secure_contexts>`.

Networking
~~~~~~~~~~

Low level networking is not implemented due to lacking support in browsers.

Currently, only :ref:`HTTP client <doc_http_client_class>`,
:ref:`HTTP requests <doc_http_request_class>`,
:ref:`WebSocket (client) <doc_websocket>` and :ref:`WebRTC <doc_webrtc>` are
supported.

The HTTP classes also have several restrictions on the HTML5 platform:

 -  Accessing or changing the ``StreamPeer`` is not possible
 -  Threaded/Blocking mode is not available
 -  Cannot progress more than once per frame, so polling in a loop will freeze
 -  No chunked responses
 -  Host verification cannot be disabled
 -  Subject to `same-origin policy <https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy>`__

Clipboard
~~~~~~~~~

Clipboard synchronization between engine and the operating system requires a
browser supporting the `Clipboard API <https://developer.mozilla.org/en-US/docs/Web/API/Clipboard_API>`__,
additionally, due to the API asynchronous nature might not be reliable when
accessed from GDScript.

.. warning:: Requires a :ref:`secure context <doc_javascript_secure_contexts>`.

Gamepads
~~~~~~~~

Gamepads will not be detected until one of their button is pressed. Gamepads
might have the wrong mapping depending on the browser/OS/gamepad combination,
sadly the `Gamepad API <https://developer.mozilla.org/en-US/docs/Web/API/Gamepad_API/Using_the_Gamepad_API>`__
does not provide a reliable way to detect the gamepad information necessary
to remap them based on model/vendor/OS due to privacy considerations.

.. warning:: Requires a :ref:`secure context <doc_javascript_secure_contexts>`.

Boot splash is not displayed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The default HTML page does not display the boot splash while loading. However,
the image is exported as a PNG file, so :ref:`custom HTML pages <doc_customizing_html5_shell>`
can display it.

Shader language limitations
~~~~~~~~~~~~~~~~~~~~~~~~~~~

When exporting a GLES2 project to HTML5, WebGL 1.0 will be used. WebGL 1.0
doesn't support dynamic loops, so shaders using those won't work there.

Serving the files
-----------------

Exporting for the web generates several files to be served from a web server,
including a default HTML page for presentation. A custom HTML file can be
used, see :ref:`doc_customizing_html5_shell`.

The generated ``.html`` file can be used as ``DirectoryIndex`` in Apache
servers and can be renamed to e.g. ``index.html`` at any time, its name is
never depended on by default.

The HTML page draws the game at maximum size within the browser window.
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
:mimetype:`application/octet-stream`. The ``.wasm`` file is delivered as
:mimetype:`application/wasm`.

.. caution:: Delivering the WebAssembly module (``.wasm``) with a MIME-type
             other than :mimetype:`application/wasm` can prevent some start-up
             optimizations.

Delivering the files with server-side compression is recommended especially for
the ``.pck`` and ``.wasm`` files, which are usually large in size.
The WebAssembly module compresses particularly well, down to around a quarter
of its original size with gzip compression.

**Hosts that provide on-the-fly compression:** GitHub Pages (gzip)

**Hosts that don't provide on-the-fly compression:** itch.io, GitLab Pages
(`supports manual gzip precompression <https://webd97.de/post/gitlab-pages-compression/>`__)

.. _doc_javascript_eval:

Calling JavaScript from script
------------------------------

In web builds, the ``JavaScript`` singleton is implemented. It offers a single
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
   GDScript :ref:`PackedByteArray<class_PackedByteArray>`

::

    func my_func2():
        var js_return = JavaScript.eval("var myNumber = 1; myNumber + 2;")
        print(js_return) # prints '3.0'

Any other JavaScript value is returned as ``null``.

HTML5 export templates may be :ref:`built <doc_compiling_for_web>` without
support for the singleton to improve security. With such templates, and on
platforms other than HTML5, calling ``JavaScript.eval`` will also return
``null``. The availability of the singleton can be checked with the
``JavaScript`` :ref:`feature tag <doc_feature_tags>`::

    func my_func3():
        if OS.has_feature('JavaScript'):
            JavaScript.eval("""
                console.log('The JavaScript singleton is available')
            """)
        else:
            print("The JavaScript singleton is NOT available")

.. tip:: GDScript's multi-line strings, surrounded by 3 quotes ``"""`` as in
         ``my_func3()`` above, are useful to keep JavaScript code readable.

The ``eval`` method also accepts a second, optional Boolean argument, which
specifies whether to execute the code in the global execution context,
defaulting to ``false`` to prevent polluting the global namespace::

    func my_func4():
        # execute in global execution context,
        # thus adding a new JavaScript global variable `SomeGlobal`
        JavaScript.eval("var SomeGlobal = {};", true)
