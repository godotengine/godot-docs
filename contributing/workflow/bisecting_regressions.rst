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

If you have experience with Godot 3.x and can reproduce an issue with Godot 4.0,
we recommend trying to reproduce the issue in the latest Godot 3.x version (if
the feature exhibiting the bug is present in 3.x). This can be used to check
whether the issue is a regression in 4.0 or not.

- If the issue **is present** in 3.x, then you'll need to check whether the issue
  occurs in older 3.x versions as well.
- If the issue is **not present** in 3.x, then you can try older 4.0 alphas and
  betas to determine when the regression started.

.. warning::

    Project files may be incompatible between Godot versions.
    **Make a backup of your project** before starting the bisection process.

    Going from the oldest to the newest build generally reduces the risk of the
    project not being able to successfully open in the editor, thanks to
    backwards compatibility. Try to reduce your project to the smallest
    repeatable example too. The more minimal the project is, the more likely
    you'll be able to open it without compatibility issues in newer engine
    versions.

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

Determine the commit hashes
^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

    4.1.1-stable
    4.1-stable
    4.0.3-stable
    4.0.2-stable
    4.0.1-stable
    4.0-stable
    3.5.2-stable
    3.5.1-stable
    3.5-stable
    3.4.5-stable
    3.4.4-stable
    3.4.3-stable
    3.4.2-stable
    3.4.1-stable
    3.4-stable
    3.3.4-stable
    3.3.3-stable
    3.3.2-stable
    3.3.1-stable
    3.3-stable
    3.2-stable
    3.1-stable
    3.0-stable

You can also use this Bash function to retrieve the Git commit hash of a
pre-release build (add it to your ``$HOME/.bashrc`` or similar):

::

    gd_snapshot_commit() {
        curl -s https://downloads.tuxfamily.org/godotengine/$1/$2/README.txt \
            | grep 'from commit' \
            | sed 's/^Built from commit \(.*\)\.$/\1/'
    }

Example usage:

.. code-block:: shell

    $ gd_snapshot_commit 4.0 beta4

To refer to the latest state of the master branch, you can use ``master``
instead of a commit hash. Note that unlike tagged releases or snapshot commit
hashes, ``master`` is a perpetually moving target.

Build the engine
^^^^^^^^^^^^^^^^

:ref:`Get Godot's source code using Git <doc_getting_source>`. Once this
is done, in the terminal window, use ``cd`` to reach the Godot repository
folder and enter the following command:

.. code-block:: shell

    # <good commit hash> is hash of the build that works as expected.
    # <bad commit hash> is hash of the build exhibiting the bug.
    $ git bisect start
    $ git bisect good <good commit hash>
    $ git bisect bad <bad commit hash>

Compile Godot. This assumes you've set up a build environment:

.. code-block:: shell

    $ scons

Run the engine
^^^^^^^^^^^^^^

Run the binary located in the ``bin/`` folder and try to reproduce the bug.

.. note::

    :ref:`Double-check the output file name <doc_introduction_to_the_buildsystem_resulting_binary>`
    in ``bin/`` to make sure you're actually running the binary you've just compiled.
    Different Godot versions will output binaries with different names.

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
