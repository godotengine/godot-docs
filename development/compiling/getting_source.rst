.. _doc_getting_source:

Getting the source
==================

.. highlight:: shell

Downloading the Godot source code
---------------------------------

Before :ref:`getting into the SCons build system <doc_introduction_to_the_buildsystem>`
and compiling Godot, you need to actually download the Godot source code.

The source code is available on `GitHub <https://github.com/godotengine/godot>`__
and while you can manually download it via the website, in general you want to
do it via the ``git`` version control system.

If you are compiling in order to make contributions or pull requests, you should
follow the instructions from the :ref:`Pull Request workflow <doc_pr_workflow>`.

If you don't know much about ``git`` yet, there are a great number of
`tutorials <https://git-scm.com/book>`__ available on various websites.

In general, you need to install ``git`` and/or one of the various GUI clients.

Afterwards, to get the latest development version of the Godot source code
(the unstable ``master`` branch), you can use ``git clone``.

If you are using the ``git`` command line client, this is done by entering
the following in a terminal:

::

    git clone https://github.com/godotengine/godot.git
    # You can add the --depth 1 argument to omit the commit history.
    # Faster, but not all Git operations (like blame) will work.

For any stable release, visit the `release page <https://github.com/godotengine/godot/releases>`__
and click on the link for the release you want.
You can then download and extract the source from the download link on the page.

With ``git``, you can also clone a stable release by specifying its branch or tag
after the ``--branch`` (or just ``-b``) argument::

    # Clone the continuously maintained stable branch (`3.x` as of writing).
    git clone https://github.com/godotengine/godot.git -b 3.x

    # Clone the `3.2.3-stable` tag. This is a fixed revision that will never change.
    git clone https://github.com/godotengine/godot.git -b 3.2.3-stable

There are also generally branches besides ``master`` for each major version.

After downloading the Godot source code,
you can :ref:`continue to compiling Godot <doc_introduction_to_the_buildsystem>`.
