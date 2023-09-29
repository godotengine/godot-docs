.. _doc_ways_to_contribute:

Ways to contribute
==================

Godot Engine is a non-profit, community-driven free and open source project.
Almost all (but our lead dev Juan, more on that below) developers are working
*pro bono* on their free time, out of personal interest and for the love of
creating a libre engine of exceptional quality.

This means that to thrive, Godot needs as many users as possible to get
involved by contributing to the engine. There are many ways to contribute to
such a big project, making it possible for everybody to bring something
positive to the engine, regardless of their skill set:

-  **Be part of the community.** The best way to contribute to Godot and help
   it become ever better is simply to use the engine and promote it by
   word-of-mouth, in the credits or splash screen of your games, blog posts, tutorials,
   videos, demos, gamedev or free software events, support on the Q&A, forums,
   Contributors Chat, Discord, etc. Participate!
   Being a user and advocate helps spread the word about our great engine,
   which has no marketing budget and can therefore only rely on its community
   to become more mainstream.

-  **Make games.** It's no secret that, to convince new users and especially the
   industry at large that Godot is a relevant market player, we need great games
   made with Godot. We know that the engine has a lot of potential, both for 2D
   and 3D games, but given its young age we still lack big releases that will
   draw attention to Godot. So keep working on your awesome projects, each new
   game increases our credibility on the gamedev market!

-  **Get involved in the engine's development.** This can be by contributing
   code via pull requests, testing the development snapshots or directly the
   git *master* branch, report bugs or suggest enhancements on the issue
   tracker, improve the official documentation (both the class reference and
   tutorials) and its translations.
   The following sections will cover each of those "direct" ways
   of contributing to the engine.

-  **Donate.** Godot is a non-profit project, but it can still benefit from
   user donations for many things. Apart from usual expenses such as hosting
   costs or promotional material on events, we also use donation money to
   acquire hardware when necessary (e.g. we used donation money to buy a
   MacBook Pro to implement Retina/HiDPI support and various other
   macOS-related features).
   Most importantly, we also used donation money to hire core developers so they
   can work full-time on the engine. Even with a low
   monthly wage, we need a steady donation income to continue doing this, which
   has been very beneficial to the project so far. So if you want to donate
   some money to the project, check `our website <https://godotengine.org/donate>`_
   for details.

Contributing code
-----------------

The possibility to study, use, modify and redistribute modifications of the
engine's source code are the fundamental rights that
Godot's `MIT <https://tldrlegal.com/license/mit-license>`_ license grants you,
making it `free and open source software <https://en.wikipedia.org/wiki/Free_and_open-source_software>`_.

As such, everyone is entitled to modify
`Godot's source code <https://github.com/godotengine/godot>`_, and send those
modifications back to the upstream project in the form of a patch (a text file
describing the changes in a ready-to-apply manner) or - in the modern workflow
that we use - via a so-called "pull request" (PR), i.e. a proposal to directly
merge one or more Git commits (patches) into the main development branch.

Contributing code changes upstream has two big advantages:

-  Your own code will be reviewed and improved by other developers, and will be
   further maintained directly in the upstream project, so you won't have to
   reapply your own changes every time you move to a newer version. On the
   other hand it comes with a responsibility, as your changes have to be
   generic enough to be beneficial to all users, and not just your project; so
   in some cases it might still be relevant to keep your changes only for your
   own project, if they are too specific.

-  The whole community will benefit from your work, and other contributors will
   behave the same way, contributing code that will be beneficial to you. At
   the time of this writing, over 2,000 developers have contributed code
   changes to the engine!

To ensure good collaboration and overall quality, the Godot developers
enforce some rules for code contributions, for example regarding the style to
use in the C++ code (indentation, brackets, etc.) or the Git and PR workflow.

A good place to start is by searching for issues tagged as
`good first issue <https://github.com/godotengine/godot/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22>`_
on GitHub.

.. seealso:: Technical details about the PR workflow are outlined in a
             specific section, :ref:`doc_pr_workflow`.

             Details about the code style guidelines and the ``clang-format``
             tool used to enforce them are outlined in
             :ref:`doc_code_style_guidelines`.

All pull requests must go through a review process before being accepted.
Depending on the scope of the changes, it may take some time for a maintainer
responsible for the modified part of the engine to provide their review.
We value all of our contributors and ask them to be patient in the meantime,
as it is expected that in an open source project like Godot, there is going to be
way more contributions than people validating them.

To make sure that your time and efforts aren't wasted, it is recommended to vet the idea
first before implementing it and putting it for a review as a PR. To that end, Godot
has a `proposal system <https://github.com/godotengine/godot-proposals>`_. Its
usage is encouraged to plan changes and discuss them with the community. Implementation
details can also be discussed with other contributors on the `Godot Contributors Chat <https://chat.godotengine.org/>`_.

.. note:: Proposals are only required when working on an enhancement or a new feature.
          Bug reports are sufficient for fixing issues.

Testing and reporting issues
----------------------------

Another great way of contributing to the engine is to test development releases
or the development branch and to report issues. It is also helpful to report
issues discovered in stable releases, so that they can be fixed in
the development branch and in future maintenance releases.

Testing development versions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To help with the testing, you have several possibilities:

-  Compile the engine from source yourself, following the instructions of the
   :ref:`Compiling <toc-devel-compiling>` page for your platform.

-  Test official pre-release binaries when they are announced (usually on the
   blog and other community platforms), such as alpha, beta and release candidate (RC) builds.

-  Test "trusted" unofficial builds of the development branch; just ask
   community members for reliable providers. Whenever possible, it's best to
   use official binaries or to compile yourself though, to be sure about the
   provenance of your binaries.

As mentioned previously, it is also helpful to keep your eyes peeled for
potential bugs that might still be present in the stable releases, especially
when using some niche features of the engine which might get less testing by
the developers.

Filing an issue on GitHub
~~~~~~~~~~~~~~~~~~~~~~~~~

Godot uses `GitHub's issue tracker <https://github.com/godotengine/godot/issues>`_
for bug reports. When you start filing a bug report, you’ll be given a form to
fill out. Please try to follow it so that all issues are consistent and provide
the required information.

Contributing to the documentation
---------------------------------

There are two separate resources referred to as "documentation" in Godot:

- **The class reference.** This is the documentation for the complete Godot API
  as exposed to GDScript and the other scripting languages. It can be consulted
  offline, directly in Godot's code editor, or online at Godot :ref:`Class Reference
  <doc_class_reference>`. To contribute to the class reference, you have to edit the
  XML file corresponding to the class and make a pull request.
  See :ref:`doc_updating_the_class_reference` and :ref:`doc_class_reference_primer`
  for more details.

- **The tutorials and engine documentation and its translations.**
  This is the part you are reading now, which is distributed in the HTML format.
  Its contents are generated from plain text files in the reStructured Text
  (rst) format, to which you can contribute via pull requests on the
  `godot-docs <https://github.com/godotengine/godot-docs>`_ GitHub repository.
  See :ref:`doc_contributing_to_the_documentation` for more details.

Contributing translations
-------------------------

To make Godot accessible to everyone, including users who may prefer resources
in their native language instead of English, our community helps translate both
the Godot editor and its documentation in many languages.

See :ref:`doc_editor_and_docs_localization` for more details.
