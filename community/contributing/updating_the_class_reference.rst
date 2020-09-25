.. _doc_updating_the_class_reference:

Contributing to the class reference with Git
============================================

.. highlight:: shell

This page gives you an overview of the steps to submit changes to Godot's class
reference using the Git version control system.

The class reference is available online in the :ref:`classes <toc-class-ref>`
section of the documentation and in the Godot editor, from the help menu.

.. seealso::

    This guide focuses on using Git. You can find the writing guidelines for the
    class reference :ref:`here <doc_class_reference_writing_guidelines>`.

    If you want to translate the class reference from English to another
    language, see :ref:`doc_editor_and_docs_localization`.

In the class reference, some methods, variables, and signals lack descriptions.
Others changed with recent releases and need updates. The developers can't write
the entire reference on their own. Godot needs you, and all of us, to
contribute.

**Important:** If you plan to make large changes, you should create an issue on
 the `godot-docs repository <https://github.com/godotengine/godot-docs/>`_
 or comment on an existing issue. Doing so lets others know you're already
 taking care of a given class.

.. seealso::

    Not sure which class to contribute to? Take a look at the class reference's
    completion status `here <https://godotengine.github.io/doc-status/>`__.

How to contribute
-----------------

You can find the source files for the class reference in Godot's GitHub
repository: `doc/classes/
<https://github.com/godotengine/godot/tree/master/doc/classes>`_.

There are five steps to update the class reference:

1. Fork `Godot's repository <https://github.com/godotengine/godot>`_
2. Clone your fork on your computer.
3. Edit the class file in ``doc/classes/`` to write documentation.
4. Commit your changes and push them to your fork.
5. Make a pull request on the Godot repository.

You will find a complete breakdown of these steps below.

.. seealso:: This guide is also available as a `video tutorial on YouTube
             <https://www.youtube.com/watch?v=5jeHXxeX-JY>`_.

.. warning:: Always edit the API reference through these source XML files. Do
             not edit the generated .rst files :ref:`in the online documentation
             <toc-class-ref>`, hosted in the `godot-docs
             <https://github.com/godotengine/godot-docs>`_ repository.

Getting started with GitHub
---------------------------

If you're new to using GitHub, the platform we use to develop Godot, this guide
will help you get started. You will learn to:

- Fork and clone Godot's repository
- Keep your fork up to date with other contributors
- Create a pull request to submit your improvements to the official docs

.. note:: If you're new to Git, the version control system Godot uses, start
          with `GitHub's interactive guide
          <https://try.github.io/levels/1/challenges/1>`_. You'll learn some
          essential vocabulary and get a sense for how the tool works.

Forking Godot
~~~~~~~~~~~~~

Start by forking the Godot Engine into a GitHub repository of your own. Read the
`GitHub forking guide <https://guides.github.com/activities/forking/>`_ to learn
to create forks.

Clone the repository on your computer:

::

    git clone https://github.com/your_name/godot.git

Create a new branch to make your changes. It makes it a lot easier to
synchronize your improvements with other contributors. It's also easier to clean
up your repository if you run into any issues with Git.

::

    git checkout -b your-new-branch-name

The new branch is the same as your master branch until you start to write API
docs. In the ``doc/`` folder, you will find the class reference.

Keeping your local clone up-to-date
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Other writers contribute to Godot's documentation. Your local repository will
fall behind it. You will have to synchronize it, especially if other
contributors update the class reference while working on it.

First, add an ``upstream`` Git *remote*. Remotes are links to online repositories
from which you can download new files. The following command registers a new
remote named "upstream" that links to the original Godot repository.

::

    git remote add upstream https://github.com/godotengine/godot

You can check the list of all remote servers with this command:

::

    git remote -v

You should have two remotes:

1. ``origin``, corresponding to your fork on GitHub. Git adds it by default when
   you clone a repository.
2. ``upstream``, that you just added.

The output should look like the following:

::

    origin https://github.com/your_name/godot.git (fetch) origin
    https://github.com/your_name/godot.git (push) upstream
    https://github.com/godotengine/godot.git (fetch) upstream
    https://github.com/godotengine/godot.git (push)

Each time you want to synchronize your branch with the upstream repository,
enter:

::

    git pull --rebase upstream master

This command will first ``fetch``, that is, download the latest version of the
Godot repository. Then, it will reapply your local changes on top of it.

If you made changes you don't want to keep in your local branch, use the
following commands instead:

::

    git fetch upstream git reset --hard upstream master

**Warning:** The above command will reset your branch to the state of the
 ``upstream master`` branch. It will discard all local changes. Make sure to
 only run this *before* you make important changes.

Another option is to delete the branch you're working on, synchronize the master
branch with the Godot repository, and create a new branch:

::

    git checkout master git branch -d your-new-branch-name git pull --rebase
    upstream master git checkout -b your-new-branch-name

If you're feeling lost by now, come to our `IRC channels
<https://webchat.freenode.net/?channels=#godotengine>`_ and ask for help.
Experienced Git users will give you a hand.

Submitting your changes
~~~~~~~~~~~~~~~~~~~~~~~

Once you finished modifying the reference, push your changes to your GitHub
repository:

::

    git add doc/classes/<edited_file>.xml
    git commit -m "Explain your modifications."
    git push

When it's done, you can ask for a pull request (abbreviated PR) on GitHub.

To learn to create a pull request, read `Creating a pull request
<https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request>`_
in the GitHub documentation.

.. warning::

    You should avoid editing files directly on GitHub in the godot engine
    repository. As hundreds of contributors work on the engine, the Git history
    must stay clean. Each commit should bundle all related improvements you make
    to the class reference.

    Editing from GitHub creates a new branch and Pull Request every time you
    save your changes. Suppose days pass before your changes get a review. In
    that case, you won't be able to update to the latest version of the
    repository cleanly. Also, it's harder to keep clean indents with GitHub's
    text editor. And they're essential in the class reference.

Updating the documentation template
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When classes are modified in the source code, the documentation template might become outdated. To make sure that you are editing an up-to-date version, you first need to compile Godot (you can follow the :ref:`doc_introduction_to_the_buildsystem` page), and then run the following command (assuming 64-bit Linux):

::

    ./bin/godot.linuxbsd.tools.64 --doctool .

The XML files in doc/classes should then be up-to-date with current Godot Engine features. You can then check what changed using the ``git diff`` command. If there are changes to other classes than the one you are planning to document, please commit those changes first before starting to edit the template:

::

    git add doc/classes/*.xml
    git commit -m "Sync classes reference template with current code base"

You are now ready to edit this file to add stuff.

**Note:** If this has been done recently by another contributor, you don't forcefully need to go through these steps (unless you know that the class you plan to edit *has* been modified recently).
