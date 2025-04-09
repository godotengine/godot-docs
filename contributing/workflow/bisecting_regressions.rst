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
and release candidates `here <https://godotengine.org/download/archive/>`__.

.. danger::

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~

To start bisecting, you must first determine the commit hashes (identifiers) of
the "bad" and "good" build. "bad" refers to the build that exhibits the bug,
whereas "good" refers to the version that doesn't exhibit the bug. 

You can use either a commit hash (like ``06acfccf8``), the tag of a stable
release (like ``4.2.1-stable``), or a branch like ``master``.

If you're using a pre-release build as the "good" or "bad" build, you can find
the commit hash in the Project Manager in the lower-right corner, or in in the
**Help > About Godot** dialog in the Godot editor. The version information will
look something like ``v4.4.beta3.official [06acfccf8]``, and the commit hash is
within the brackets, in this case ``06acfccf8``. You can click on the version
information to copy it, including the commit hash.

Alternately, you can browse the `interactive changelog
<https://godotengine.github.io/godot-interactive-changelog/>`__ to find commits
for all releases, including development builds. The commits will be listed as a
range, like ``commits: a013481b0...06acfccf8``, and the second commit is the one
you should use for bisecting. You can also browse the `Godot Archive
<https://godotengine.org/download/archive/>`__, and find the commit hash within
the release page linked from the **News** button.

If you're using a stable release as the "good" or "bad" build, you can use the
tag of that release directly, such as ``4.2-stable`` or ``4.2.1-stable``. A full
list of release tags is available `on GitHub
<https://github.com/godotengine/godot/tags>`__, and you can also find the actual
commit hash that corresponds to a stable release there.

To refer to the latest state of the master branch, you can use ``master``
instead of a commit hash. Note that unlike tagged releases or snapshot commit
hashes, ``master`` is a perpetually moving target.

Build the engine
~~~~~~~~~~~~~~~~

:ref:`Get Godot's source code using Git <doc_getting_source>`. Once this
is done, in the terminal window, use ``cd`` to reach the Godot repository
folder and enter the following command:

.. code-block:: shell

    # <good commit hash> is hash of the build that works as expected.
    # <bad commit hash> is hash of the build exhibiting the bug.
    git bisect start
    git bisect good <good commit hash>
    git bisect bad <bad commit hash>

Compile Godot. This assumes you've set up a build environment:

.. code-block:: shell

    scons

Run the engine
~~~~~~~~~~~~~~

Run the binary located in the ``bin/`` folder and try to reproduce the bug.

.. note::

    :ref:`Double-check the output file name <doc_introduction_to_the_buildsystem_resulting_binary>`
    in ``bin/`` to make sure you're actually running the binary you've just compiled.
    Different Godot versions will output binaries with different names.

If the build **still** exhibits the bug, run the following command:

.. code-block:: shell

    git bisect bad

If the build **does not** exhibit the bug, run the following command:

.. code-block:: shell

    git bisect good

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

.. seealso::

    You can read the full documentation on ``git bisect``
    `here <https://git-scm.com/docs/git-bisect>`__.
