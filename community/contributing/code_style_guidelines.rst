.. _doc_code_style_guidelines:

Code style guidelines
=====================

.. highlight:: shell

When contributing to Godot's source code, you will be expected to follow the
style guidelines outlined below. Some of them are checked via the Continuous
Integration process and reviewers will ask you to fix potential issues, so
best setup your system as outlined below to ensure all your commits follow the
guidelines.

C++ and Objective-C
-------------------

There are no written guidelines, but the code style agreed upon by the
developers is enforced via the `clang-format <http://clang.llvm.org/docs/ClangFormat.html>`__
code beautifier, which takes care for you of all our conventions.
To name a few:

- Indentation and alignment are both tab based (respectively one and two tabs)
- One space around math and assignments operators as well as after commas
- Pointer and reference operators are affixed to the variable identifier, not
  to the type name

The rules used by clang-format are outlined in the
`.clang-format <https://github.com/godotengine/godot/blob/master/.clang-format>`__
file of the Godot repository.

As long as you ensure that your style matches the surrounding code and that you
not introducing trailing whitespace or space-based indentation, you should be
fine. If you plan to contribute regularly however, we strongly advise that you
setup clang-format locally to check and automatically fix all your commits.

.. warning:: Godot's code style should *not* be applied to thirdparty code,
             i.e. that is included in Godot's source tree but was not written
             specifically for our project. Such code usually come from
             different upstream projects with their own style guides (or lack
             thereof), and don't want to introduce differences that would make
             syncing with upstream repositories harder.

             Thirdparty code is usually included in the ``thirdparty/`` folder
             and can thus easily be excluded from formatting scripts. For the
             rare cases where a thirdparty code snippet needs to be included
             directly within a Godot file, you can use
             ``/* clang-format off */`` and ``/* clang-format on */`` to tell
             clang-format to ignore a chunk of code.

Using clang-format locally
~~~~~~~~~~~~~~~~~~~~~~~~~~

First of all, you will need to install clang-format. As of now, you need to use
**clang-format 5.x** to be compatible with Godot's format. The upcoming 6.x
branch has not been tested yet and my cause inconsistencies; the previous 3.x
branch is incompatible with the style definitions and will error out.

Installation
^^^^^^^^^^^^

Here's how to install clang-format:

- Linux: It will usually be available out-of-the-box with the clang toolchain
  packaged by your distribution. If your distro version is not the required one,
  you can download a pre-compiled version from the
  `LLVM website <http://llvm.org/releases/download.html>`__, or if you are on
  a Debian derivative, use the `upstream repos <http://apt.llvm.org/>`__.
- macOS and Windows: You can download precompiled binaries from the
  `LLVM website <http://llvm.org/releases/download.html>`__. You may need to add
  the path to the binary's folder to your system's ``PATH`` environment
  variable to be able to call ``clang-format`` out of the box.

You then have different possibilities to apply clang-format to your changes:

Manual usage
^^^^^^^^^^^^

You can apply clang-format manually one or more files with the following
command:

::

    clang-format -i <path/to/file(s)>

- ``-i`` means that the changes should be written directly to the file (by
  default clang-format would only output the fixed version to the terminal).
- The path can point to several files, either one after the other or using
  wildcards like in a typical Unix shell. Be careful when globbing so that
  you don't run clang-format on compiled objects (.o and .a files) that are
  in Godot's tree. So better use ``core/*.{cpp,h}`` than ``core/*``.

Pre-commit hook
^^^^^^^^^^^^^^^

For ease of use, we provide a pre-commit hook for Git that will run
clang-format automatically on all your commits to check them, and let you apply
its changes in the final commit.

This "hook" is a script which can be found in ``misc/hooks``, refer to that
folder's README.md for installation instructions.

If your clang-format is not in the ``PATH``, you may have to edit the
``pre-commit-clang-format`` to point to the correct binary for it to work.
The hook was tested on Linux and macOS, but should also work in the Git Shell
on Windows.

IDE plugin
^^^^^^^^^^

Most IDEs or code editors have beautifier plugins that can be configured to run
clang-format automatically, for example each time you save a file.

Here is a non-exhaustive list of beautifier plugins for some IDEs:

- Qt Creator: `Beautifier plugin <http://doc.qt.io/qtcreator/creator-beautifier.html>`__
- Visual Studio Code: `Clang-Format <https://marketplace.visualstudio.com/items?itemName=xaver.clang-format>`__
- vim: `vim-clang-format <https://github.com/rhysd/vim-clang-format>`__

(Pull requests welcome to extend this list with tested plugins.)

Java
----

For Godot's Java code (mostly in ``platform/android``), there is currently no
style guide, so for now try to stay consistent with the existing code.

Once a style is decided upon, it could also be enforced via clang-format.

Python
------

Godot's SCons buildsystem is written in Python 2, and various scripts included
in the source tree are either in Python 2 or Python 3.

For those, we follow the `PEP-8 style guide <https://www.python.org/dev/peps/pep-0008/>`__,
this is however not as strongly enforced as for the C++ code. If you are so
inclined, you can check and format your Python changes using
`autopep8 <https://pypi.python.org/pypi/autopep8>`__.
