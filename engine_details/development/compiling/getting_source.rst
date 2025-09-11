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
follow the instructions from the `Pull Request workflow <https://contributing.godotengine.org/en/latest/organization/pull_requests/creating_pull_requests.html>`__.

If you don't know much about ``git`` yet, there are a great number of
`tutorials <https://git-scm.com/book>`__ available on various websites.

In general, you need to install ``git`` and/or one of the various GUI clients.

Afterwards, to get the latest development version of the Godot source code
(the unstable ``master`` branch), you can use ``git clone``.

If you are using the ``git`` command line client, this is done by entering
the following in a terminal:

::

    git clone https://github.com/godotengine/godot.git
    # You can add the --depth 1 argument to omit the commit history (shallow clone).
    # A shallow clone is faster, but not all Git operations (like blame) will work.

For any stable release, visit the `release page <https://github.com/godotengine/godot/releases>`__
and click on the link for the release you want.
You can then download and extract the source from the download link on the page.

With ``git``, you can also clone a stable release by specifying its branch or tag
after the ``--branch`` (or just ``-b``) argument:

::

    # Clone the continuously maintained stable branch (`4.4` as of writing).
    git clone https://github.com/godotengine/godot.git -b 4.4

    # Clone the `4.4-stable` tag. This is a fixed revision that will never change.
    git clone https://github.com/godotengine/godot.git -b 4.4-stable

    # After cloning, optionally go to a specific commit.
    # This can be used to access the source code at a specific point in time,
    # e.g. for development snapshots, betas and release candidates.
    cd godot
    git checkout f4af8201bac157b9d47e336203d3e8a8ef729de2

The `maintenance branches <https://github.com/godotengine/godot/branches/all>`__
are used to release further patches on each minor version.

You can get the source code for each release and pre-release in ``.tar.xz`` format from
`godotengine/godot-builds on GitHub <https://github.com/godotengine/godot-builds/releases>`__.
This lacks version control information but has a slightly smaller download size.

After downloading the Godot source code,
you can :ref:`continue to compiling Godot <doc_introduction_to_the_buildsystem>`.
