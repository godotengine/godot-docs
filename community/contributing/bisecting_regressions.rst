.. _doc_bisecting_regressions:

Bisecting regressions
=====================

.. highlight:: shell

Bisecting is a way to find regressions in software. After reporting a bug on the
`Godot repository on GitHub <https://github.com/godotengine/godot>`__, you may
be asked by a contributor to *bisect* the issue. Bisecting makes it possible for
contributors to fix bugs faster, as they can know in advance which commit caused
the regression. Your effort will be widely appreciated :)

The guide below explains how to find a regression by bisecting.

What is bisecting?
------------------

Godot developers use the `Git <https://git-scm.com/>`__ version control system.
In the context of Git, bisecting is the process of performing a manual
`binary search <https://en.wikipedia.org/wiki/Binary_search_algorithm>`__
to determine when a regression appeared. While it's typically used for bugs,
it can also be used to find other kinds of unexpected changes such as
performance regressions.

Using official builds to speed up bisecting
-------------------------------------------

Before using Git's ``bisect`` command, we strongly recommend trying to reproduce
the bug with an older (or newer) official release. This greatly reduces the
range of commits that potentially need to be built from source and tested.
You can find binaries of official releases, as well as alphas, betas,
and release candidates `here <https://downloads.tuxfamily.org/godotengine/>`__.

For example, if you've reported a bug against Godot 3.2, you should first try to
reproduce the bug in Godot 3.1 (not a patch release, see below for the reason).
If the bug doesn't occur there, try to reproduce it in Godot 3.2 *beta 1* (which
is roughly in the middle of all test builds available). If you can't reproduce
the bug with Godot 3.2 beta 1, then try newer betas and RC builds. If you do
manage to reproduce the bug with Godot 3.2 beta 1, then try older alpha builds.

.. warning::

    For bisecting regressions, don't use patch releases such as Godot 3.1.2.
    Instead, use the minor version's first release like Godot 3.1. This is
    because patch releases are built from a separate *stable branch*. This kind
    of branch doesn't follow the rest of Godot's development, which is done in
    the ``master`` branch.

The Git bisect command
----------------------

If you've found a build that didn't exhibit the bug in the above testing
process, you can now start bisecting the regression. The Git version control
system offers a built-in command for this: ``git bisect``. This makes the
process semi-automated as you only have to build the engine, run it and try to
reproduce the bug.

.. note::

    Before bisecting a regression, you need to set up a build environment to
    compile Godot from source. To do so, read the
    :ref:`Compiling <toc-devel-compiling>` page for your target platform.
    (Compiling Godot from source doesn't require C++ programming knowledge.)

    Note that compiling Godot can take a while on slow hardware (up an hour for
    each full rebuild on a slow dual-core CPU). This means the full process can
    take up to several hours. If your hardware is too slow, you may want to stop
    there and report the results of your "pre-bisecting" on the GitHub issue so
    another contributor can continue bisecting from there.

To start bisecting, you must first determine the commit hashes (identifiers) of
the "bad" and "good" build. "bad" refers to the build that exhibits the bug,
whereas "good" refers to the version that doesn't exhibit the bug. If you're
using a pre-release build as the "good" or "bad" build, browse the `download
mirror <https://downloads.tuxfamily.org/godotengine/>`__, go to the folder that
contains the pre-release you downloaded and look for the ``README.txt`` file.
The commit hash is written inside that file.

If you're using a stable release as the "good" or "bad" build, use one of the
following commit hashes depending on the version:

.. code-block:: none

    3.2-stable
    3.1-stable
    3.0-stable

To refer to the latest state of the master branch, you can use ``master``
instead of a commit hash.

:ref:`Get Godot's source code using Git <doc_getting_source>`. Once this
is done, in the terminal window, use ``cd`` to reach the Godot repository
folder and enter the following command:

.. code-block:: shell

    # <good> is the commit hash of the build that works as expected.
    # <bad> is the commit hash of the build exhibiting the bug.
    $ git bisect start <good> <bad>

Compile Godot. This assumes you've set up a build environment:

.. code-block:: shell

    # <platform> is the platform you're targeting for regression testing,
    # like "windows", "x11" or "osx".
    $ scons platform=<platform> -j4

Since building Godot takes a while, you want to dedicate as many CPU threads as
possible to the task. This is what the ``-j`` parameter does. Here, the command
assigns 4 CPU threads to compiling Godot.

Run the binary located in the ``bin/`` folder and try to reproduce the bug.

If the build **still** exhibits the bug, run the following command:

.. code-block:: shell

    $ git bisect bad

If the build **does not** exhibit the bug, run the following command:

.. code-block:: shell

    $ git bisect good

After entering one of the commands above, Git will switch to a different commit.
You should now build Godot again, try to reproduce the bug, then enter ``git
bisect good`` or ``git bisect bad`` depending on the result. You'll have to
repeat this several times. The longer the commit range, the more steps will be
required. 5 to 10 steps are usually sufficient to find most regressions; Git
will remind you of the number of steps remaining (in the worst case scenario).

Once you've completed enough steps, Git will display the commit hash where the
regression appeared. Write this commit hash as a comment to the GitHub issue
you've bisected. This will help in solving the issue. Thanks again for
contributing to Godot :)

.. note::

    You can read the full documentation on ``git bisect``
    `here <https://git-scm.com/docs/git-bisect>`__.
