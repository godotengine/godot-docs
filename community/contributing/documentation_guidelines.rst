.. _doc_documentation_guidelines:

Contributing to the documentation
=================================

This guide explains how to contribute to Godot's documentation, be it by
writing, reviewing, or translating pages.

.. seealso::

   If you want to translate pages or the class reference from English to other
   languages, read :ref:`doc_editor_and_docs_localization`.

Getting started
---------------

To modify or create pages in the reference manual, you need to edit ``.rst``
files in the `godot-docs GitHub repository
<https://github.com/godotengine/godot-docs>`_. Modifying those pages in a pull
request and triggers a rebuild of the online documentation upon merging.



.. seealso:: For details on Git usage and the pull request workflow, please
             refer to the :ref:`doc_pr_workflow` page. Most of what it describes
             regarding the main godotengine/godot repository is also valid for
             the docs repository.

.. warning:: The class reference's source files are in the `Godot engine repository
             <https://github.com/godotengine/godot>`_. We generate the :ref:`Godot API
             <toc-class-ref>` section of this documentation from them. If you want to update the
             description of a class, its methods, or properties, read
             :ref:`doc_updating_the_class_reference`.

Editing pages online
--------------------

You can edit the documentation online by clicking the **Edit on GitHub** link in
the top-right of every page.

Doing so takes you to the GitHub text editor. You need to have a GitHub account
and to log in to use it. Once logged in, you can propose change like so:

1. Click the **Edit on GitHub** button.

2. On the GitHub page you're taken to, click the pencil icon in the top-right
   corner near the **Raw**, **Blame**, and **History** buttons. It has the
   tooltip "Edit the file in a fork of this project".

3. Edit the text in the text editor.

4. At the bottom of the web page, summarize the changes you made and click the
   button **Propose file change**.

5. On the following screens, click the **Create pull request** button until you
   see a message like *Username wants to merge 1 commit into godotengine:master
   from Username:patch-6*.

Another contributor will review your changes and merge them into the docs if
they're good. They may also make changes or ask you to do so before merging.

What is the Godot documentation
-------------------------------

The Godot documentation is intended as a comprehensive reference manual for the
Godot game engine. It is not meant to contain step-by-step tutorials, with the
exception of two game creation tutorials in the Getting Started section.

We strive to write objective content in accessible and well-written English. To
contribute, you should also read:

- The :ref:`doc_docs_writing_guidelines`. There, you will find rules to write

- Tutorial: a page aiming at explaining how to use one or more concepts in the
   editor or scripts in order to achieve a specific goal with a learning purpose
   (e.g. "Making a simple 2d Pong game", "Applying forces to an object").
- Documentation: a page describing precisely one and only one concept at a time,
   if possible exhaustively (e.g. the list of methods of the Sprite class, or an
   overview of the input management in Godot).

You are free to write the kind of documentation you wish, as long as you respect
the following rules (and the ones on the repo).

Titles
------

Always begin pages with their title and a Sphinx reference name:

::

    .. _doc_insert_your_title_here:

    Insert your title here
    ======================

The reference allows linking to this page using the ``:ref:`` format, e.g.
``:ref:`doc_insert_your_title_here``` would link to the above example page
(note the lack of leading underscore in the reference).

Also, avoid American CamelCase titles: title's first word should begin
with a capitalized letter, and every following word should not. Thus,
this is a good example:

-  Insert your title here

And this is a bad example:

-  Insert Your Title Here

Only project, people and node class names should have capitalized first
letter.

License
-------

This documentation and every page it contains is published under the terms of
the `Creative Commons Attribution 3.0 license (CC-BY-3.0) <https://tldrlegal.com/license/creative-commons-attribution-(cc)>`_, with attribution to "Juan Linietsky, Ariel Manzur and the Godot community".

By contributing to the documentation on the GitHub repository, you agree that
your changes are distributed under this license.
