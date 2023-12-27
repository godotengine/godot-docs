.. _doc_common_engine_methods_and_macros:

Common engine methods and macros
================================

Godot's C++ codebase makes use of dozens of custom methods and macros which are
used in almost every file. This page is geared towards beginner contributors,
but it can also be useful for those writing custom C++ modules.

Print text
----------

.. code-block:: cpp

    // Prints a message to standard output.
    print_line("Message");

    // Non-String arguments are automatically converted to String for printing.
    // If passing several arguments, they will be concatenated together with a
    // space between each argument.
    print_line("There are", 123, "nodes");

    // Prints a message to standard output, but only when the engine
    // is started with the `--verbose` command line argument.
    print_verbose("Message");

    // Prints a rich-formatted message using BBCode to standard output.
    // This supports a subset of BBCode tags supported by RichTextLabel
    // and will also appear formatted in the editor Output panel.
    // On Windows, this requires Windows 10 or later to work in the terminal.
    print_line_rich("[b]Bold[/b], [color=red]Red text[/color]")

    // Prints a formatted error or warning message with a trace.
    ERR_PRINT("Message");
    WARN_PRINT("Message");

    // Prints an error or warning message only once per session.
    // This can be used to avoid spamming the console output.
    ERR_PRINT_ONCE("Message");
    WARN_PRINT_ONCE("Message");

If you need to add placeholders in your messages, use format strings as
described below.

Format a string
---------------

The ``vformat()`` function returns a formatted :ref:`class_String`. It behaves
in a way similar to C's ``sprintf()``:

.. code-block:: cpp

    vformat("My name is %s.", "Godette");
    vformat("%d bugs on the wall!", 1234);
    vformat("Pi is approximately %f.", 3.1416);

    // Converts the resulting String into a `const char *`.
    // You may need to do this if passing the result as an argument
    // to a method that expects a `const char *` instead of a String.
    vformat("My name is %s.", "Godette").c_str();

In most cases, try to use ``vformat()`` instead of string concatenation as it
makes for more readable code.

Convert an integer or float to a string
---------------------------------------

This is not needed when printing numbers using ``print_line()``, but you may
still need to perform manual conversion for some other use cases.

.. code-block:: cpp

    // Stores the string "42" using integer-to-string conversion.
    String int_to_string = itos(42);

    // Stores the string "123.45" using real-to-string conversion.
    String real_to_string = rtos(123.45);

Internationalize a string
-------------------------

There are two types of internationalization in Godot's codebase:

- ``TTR()``: **Editor ("tools") translations** will only be processed in the
  editor. If a user uses the same text in one of their projects, it won't be
  translated if they provide a translation for it. When contributing to the
  engine, this is generally the macro you should use for localizable strings.
- ``RTR()``: **Run-time translations** will be automatically localized in
  projects if they provide a translation for the given string. This kind of
  translation shouldn't be used in editor-only code.

.. code-block:: cpp

    // Returns the translated string that matches the user's locale settings.
    // Translations are located in `editor/translations`.
    // The localization template is generated automatically; don't modify it.
    TTR("Exit the editor?");

To insert placeholders in localizable strings, wrap the localization macro in a
``vformat()`` call as follows:

.. code-block:: cpp

    String file_path = "example.txt";
    vformat(TTR("Couldn't open \"%s\" for reading."), file_path);

.. note::

    When using ``vformat()`` and a translation macro together, always wrap the
    translation macro in ``vformat()``, not the other way around. Otherwise, the
    string will never match the translation as it will have the placeholder
    already replaced when it's passed to TranslationServer.

Clamp a value
-------------

Godot provides macros for clamping a value with a lower bound (``MAX``), an
upper bound (``MIN``) or both (``CLAMP``):

.. code-block:: cpp

    int a = 3;
    int b = 5;

    MAX(b, 6); // 6
    MIN(2, a); // 2
    CLAMP(a, 10, 30); // 10

This works with any type that can be compared to other values (like ``int`` and
``float``).

Microbenchmarking
-----------------

If you want to benchmark a piece of code but don't know how to use a profiler,
use this snippet:

.. code-block:: cpp

    uint64_t begin = Time::get_singleton()->get_ticks_usec();

    // Your code here...

    uint64_t end = Time::get_singleton()->get_ticks_usec();
    print_line(vformat("Snippet took %d microseconds", end - begin));

This will print the time spent between the ``begin`` declaration and the ``end``
declaration.

.. note::

    You may have to ``#include "core/os/os.h"`` if it's not present already.

    When opening a pull request, make sure to remove this snippet as well as the
    include if it wasn't there previously.

Get project/editor settings
---------------------------

There are four macros available for this:

.. code-block:: cpp

    // Returns the specified project setting's value,
    // defaulting to `false` if it doesn't exist.
    GLOBAL_DEF("section/subsection/value", false);

    // Returns the specified editor setting's value,
    // defaulting to "Untitled" if it doesn't exist.
    EDITOR_DEF("section/subsection/value", "Untitled");

If a default value has been specified elsewhere, don't specify it again to avoid
repetition:

.. code-block:: cpp

    // Returns the value of the project setting.
    GLOBAL_GET("section/subsection/value");
    // Returns the value of the editor setting.
    EDITOR_GET("section/subsection/value");

It's recommended to use ``GLOBAL_DEF``/``EDITOR_DEF`` only once per setting and
use ``GLOBAL_GET``/``EDITOR_GET`` in all other places where it's referenced.

Error macros
------------

Godot features many error macros to make error reporting more convenient.

.. warning::

    Conditions in error macros work in the **opposite** way of GDScript's
    built-in ``assert()`` function. An error is reached if the condition inside
    evaluates to ``true``, not ``false``.

.. note::

    Only variants with custom messages are documented here, as these should
    always be used in new contributions. Make sure the custom message provided
    includes enough information for people to diagnose the issue, even if they
    don't know C++. In case a method was passed invalid arguments, you can print
    the invalid value in question to ease debugging.

    For internal error checking where displaying a human-readable message isn't
    necessary, remove ``_MSG`` at the end of the macro name and don't supply a
    message argument.

    Also, always try to return processable data so the engine can keep running
    well.

.. code-block:: cpp

    // Conditionally prints an error message and returns from the function.
    // Use this in methods which don't return a value.
    ERR_FAIL_COND_MSG(!mesh.is_valid(), vformat("Couldn't load mesh at: %s", path));

    // Conditionally prints an error message and returns `0` from the function.
    // Use this in methods which must return a value.
    ERR_FAIL_COND_V_MSG(rect.x < 0 || rect.y < 0, 0,
            "Couldn't calculate the rectangle's area.");

    // Prints an error message if `index` is < 0 or >= `SomeEnum::QUALITY_MAX`,
    // then returns from the function.
    ERR_FAIL_INDEX_MSG(index, SomeEnum::QUALITY_MAX,
            vformat("Invalid quality: %d. See SomeEnum for allowed values.", index));

    // Prints an error message if `index` is < 0 >= `some_array.size()`,
    // then returns `-1` from the function.
    ERR_FAIL_INDEX_V_MSG(index, some_array.size(), -1,
            vformat("Item %d is out of bounds.", index));

    // Unconditionally prints an error message and returns from the function.
    // Only use this if you need to perform complex error checking.
    if (!complex_error_checking_routine()) {
        ERR_FAIL_MSG("Couldn't reload the filesystem cache.");
    }

    // Unconditionally prints an error message and returns `false` from the function.
    // Only use this if you need to perform complex error checking.
    if (!complex_error_checking_routine()) {
        ERR_FAIL_V_MSG(false, "Couldn't parse the input arguments.");
    }

    // Crashes the engine. This should generally never be used
    // except for testing crash handling code. Godot's philosophy
    // is to never crash, both in the editor and in exported projects.
    CRASH_NOW_MSG("Can't predict the future! Aborting.");


.. seealso::

    See `core/error/error_macros.h <https://github.com/godotengine/godot/blob/master/core/error/error_macros.h>`__
    in Godot's codebase for more information about each error macro.

    Some functions return an error code (materialized by a return type of
    ``Error``). This value can be returned directly from an error macro.
    See the list of available error codes in
    `core/error/error_list.h <https://github.com/godotengine/godot/blob/master/core/error/error_list.h>`__.
