.. _doc_complying_with_licenses:

Complying with licenses
=======================

.. warning::

    The information on this page is intended to be helpful, but is **not legal advice**.
    We recommend checking the licensing information in the relevant version of Godot's source code.
    If you plan to distribute your game, we also recommend consulting with an attorney.

.. note::

    After reviewing this page, ensure you have met all of these requirements:

    - You have an easily accessible license page either within your game or in an external file.

    - The license page includes the full Godot license text (seen below).

    - The license page includes the full attribution of all other third-party libraries.
    If you automate this with code, Godot's license will be included automatically.

    - The license page attributes all copyrighted assets based on their requirements.
    For example, CC0 has no requirements, but CC-BY requires you attribute the creator.

What are licenses?
------------------

Godot is created and distributed under the `MIT License <https://opensource.org/licenses/MIT>`_.
It doesn't have a sole owner either, as every contributor that submits code to
the project does it under this same license and keeps ownership of the
contribution.

.. note::

    Your games do not need to be under the same license as Godot. You are free to release
    your Godot projects under any license and to create commercial games with
    the engine.

Licenses are the legal requirement(s) that you (or your company) must follow if you
distribute the software or derivative works, including games made with it.
Your game or project can have a different license, but it still needs to comply
with the original one.

.. note::

    In your project's credits screen, remember to also list third-party notices
    for assets you're using, such as textures, models, sounds, music, and fonts.

    Free assets in particular often come with licenses that require attribution.
    Double-check their license before using those assets in a project.

Requirements
------------

For Godot itself, the only requirement is to include the license text somewhere in your game or derivative project.

This text reads as follows:

    This project uses Godot Engine, available under the following license:

    Copyright (c) 2007-2022 Juan Linietsky, Ariel Manzur.
    Copyright (c) 2014-2022 Godot Engine contributors.

    Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

.. warning::

    Since Godot itself utilizes other `third-party libraries <https://github.com/godotengine/godot/blob/master/COPYRIGHT.txt>`_, you must also follow the licensing requirements of all enabled libraries.
    Most of them do not require attribution, but some do.
    If you are using the official export templates, all libraries are enabled.
    This means you need to provide attribution for all of them.

Third-party licenses
--------------------

Godot utilizes software written by
`third parties <https://github.com/godotengine/godot/blob/master/COPYRIGHT.txt>`_.
Most of it does not require license inclusion, but some do.
Make sure to do it if these are compiled in your Godot export template. If
you're using the official export templates, all libraries are enabled. This
means you need to provide attribution for all the libraries listed below.

We recommend utilizing the :ref:`Engine <class_Engine>` singleton to attribute all licenses including Godot's.

.. tabs::

 .. code-tab:: gdscript

    var t = ""
    
    t += "Components: \n----------------\n\n"
    for item in Engine.get_copyright_info():
        t += "%s\n\n" % item.name
        for part in item.parts:
            for holder in part.copyright:
                t += "Copyright (c) %s\n" % holder
            t += "License: %s\n\n" % part.license
        t += "\n\n"
    
    t += "Licenses: \n----------------\n"
    var licenses = Engine.get_license_info()
    for item in licenses:
        t += "%s\n\n" % item
        t += "%s\n" % licenses[item]
        t += "\n\n"
    
    # Set text on RichTextLabel with scrolling active.
    text = t

 .. code-tab:: csharp

    string t = "";
    
    t += "Components: \n----------------\n\n";
    foreach(Godot.Collections.Dictionary item in Engine.GetCopyrightInfo())
    {
        t += string.Format("{0}\n\n", item["name"]);
        foreach(Godot.Collections.Dictionary part in item["parts"] as Godot.Collections.Array)
        {
            foreach(string holder in part["copyright"] as Godot.Collections.Array)
            {
                t += string.Format("Copyright (c) {0}\n", holder);
            }
            t += string.Format("License: {0}\n\n", part["license"]);
        }
        t += "\n\n";
    }
    
    t += "Licenses: \n----------------\n";
    foreach(System.Collections.DictionaryEntry item in Engine.GetLicenseInfo())
    {
        t += string.Format("{0}\n\n", item.Key);
        t += string.Format("{0}\n", item.Value);
        t += "\n\n";
    }
    
    // Set text on RichTextLabel with scrolling active.
    Text = t;

Inclusion
---------

The license does not specify how it has to be included, so anything is valid as
long as it can be displayed under some condition. These are the most common
approaches (only one of these is required, not all).

Credits screen
^^^^^^^^^^^^^^

Include the above license text somewhere in the credits screen. It can be at the
bottom after showing the rest of the credits. Most large studios use this
approach with open source licenses. Make sure the credits are accessible
without completing the game, such as in the settings.

Licenses screen
^^^^^^^^^^^^^^^

Some games have a special menu (often in the settings) to display licenses.

Output log
^^^^^^^^^^

Just printing the licensing text using the :ref:`print() <class_@GlobalScope_method_print>`
function may be enough on platforms where a global output log is readable.
This is the case on desktop platforms, Android and HTML5 (but not iOS and UWP).

Accompanying file
^^^^^^^^^^^^^^^^^

If the game is distributed on desktop platforms, a file containing the license
can be added to the software that is installed to the user's computer.

Printed manual
^^^^^^^^^^^^^^

If the game includes printed manuals, license text can be included there.
