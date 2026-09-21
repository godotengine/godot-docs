:allow_comments: False

.. _doc_complying_with_licenses:

Complying with licenses
=======================

.. warning::

    The recommendations in this page **are not legal advice.** They are provided
    in good faith to help users navigate license attribution requirements.

What are licenses?
------------------

Godot is created and distributed under the `MIT License <https://opensource.org/licenses/MIT>`_.
It doesn't have a sole owner, as every contributor that submits code to
the project does it under this same license and keeps ownership of their
contribution.

The license is the legal requirement for you (or your company) to use and
distribute the software (and derivative projects, including games made with it).
Your game or project can have a different license, but it still needs to comply
with the original one.

.. note::

    This section covers compliance with licenses from a user perspective.
    If you are interested in licence compliance as a contributor, you can find
    guidelines `here <https://contributing.godotengine.org/en/latest/engine/guidelines/best_practices.html#don-t-use-complex-canned-solutions-for-simple-problems>`__.

.. tip::

    Alongside the Godot license text, remember to also list third-party notices
    for assets you're using, such as textures, models, sounds, music and fonts.
    This includes free assets, which often come with licenses that require
    attribution.

Requirements
------------

In the case of the MIT license, the only requirement is to include the license
text somewhere in your game or derivative project.

This text reads as follows:

.. code-block:: none

    This game uses Godot Engine, available under the following license:

    Copyright (c) 2014-present Godot Engine contributors.
    Copyright (c) 2007-2014 Juan Linietsky, Ariel Manzur.

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

Beside its own MIT license, Godot includes code from a number of third-party
libraries. See :ref:`doc_complying_with_licenses_thirdparty` for details.

.. note::

    Your games do not need to be under the same license. You are free to release
    your Godot projects under any license and to create commercial games with
    the engine.

Inclusion
---------

The license text must be made available to the user. The license doesn't specify
how the text has to be included, but here are the most common approaches (you
only need to implement one of them, not all).

Credits screen
~~~~~~~~~~~~~~

Include the above license text somewhere in the credits screen. It can be at the
bottom after showing the rest of the credits. Most large studios use this
approach with open source licenses.

Licenses screen
~~~~~~~~~~~~~~~

Some games have a special menu (often in the settings) to display licenses.
This menu is typically accessed with a button called **Third-party Licenses**
or **Open Source Licenses**.

Output log
~~~~~~~~~~

Printing the license text using the :ref:`print() <class_@GlobalScope_method_print>`
function may be enough on platforms where a global output log is readable.
This is the case on desktop platforms, Android and HTML5 (but not iOS).

Accompanying file
~~~~~~~~~~~~~~~~~

If the game is distributed on desktop platforms, a file containing the license
text can be added to the software that is installed to the user PC.

Printed manual
~~~~~~~~~~~~~~

If the game includes a printed manual, the license text can be included there.

Link to the license
~~~~~~~~~~~~~~~~~~~

The Godot Engine developers consider that a link to ``godotengine.org/license``
in your game documentation or credits would be an acceptable way to satisfy
the license terms.

.. tip::

    Godot provides several methods to get license information in the
    :ref:`Engine <class_Engine>` singleton. This allows you to source the
    license information directly from the engine binary, which prevents the
    information from becoming outdated if you update engine versions.

    For the engine itself:

    - :ref:`Engine.get_license_text<class_Engine_method_get_license_text>`

    For third-party components used by the engine:

    - :ref:`Engine.get_license_info<class_Engine_method_get_license_info>`
    - :ref:`Engine.get_copyright_info<class_Engine_method_get_copyright_info>`

.. _doc_complying_with_licenses_thirdparty:

Third-party licenses
--------------------

Godot itself contains software written by
`third parties <https://github.com/godotengine/godot/blob/master/thirdparty/README.md>`_,
which is compatible with, but not covered by Godot's MIT license.

Many of these dependencies are distributed under permissive open source licenses
which require attribution by explicitly citing their copyright statement and
license text in the final product's documentation.

Given the scope of the Godot project, this is fairly difficult to do thoroughly.
For the Godot editor, the full documentation of third-party copyrights and
licenses is provided in the `COPYRIGHT.txt <https://github.com/godotengine/godot/blob/master/COPYRIGHT.txt>`_
file.

A good option for end users to document third-party licenses is to include this
file in your project's distribution, which you can e.g. rename to
``GODOT_COPYRIGHT.txt`` to prevent any confusion with your own code and assets.
