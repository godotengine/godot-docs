.. _doc_about_intro:

Introduction
============

::

    func _ready():
        $Label.text = "Hello world!"

Welcome to the official documentation of Godot Engine, the free and open source
community-driven 2D and 3D game engine! Behind this mouthful, you will find a
powerful yet user-friendly tool that you can use to develop any kind of game,
for any platform and with no usage restriction whatsoever.

This page gives a broad presentation of the engine and of the contents
of this documentation, so that you know where to start if you are a beginner or
where to look if you need info on a specific feature.

Before you start
----------------

The :ref:`Tutorials and resources <doc_community_tutorials>` page lists
video tutorials contributed by the community. If you prefer video to text,
those may be worth a look.

In case you have trouble with one of the tutorials or your project,
you can find help on the various :ref:`Community channels <doc_community_channels>`,
especially the Godot Discord community, Q&A, and IRC.

About Godot Engine
------------------

A game engine is a complex tool, and it is therefore difficult to present Godot
in a few words. Here's a quick synopsis, which you are free to reuse
if you need a quick writeup about Godot Engine.

    Godot Engine is a feature-packed, cross-platform game engine to create 2D
    and 3D games from a unified interface. It provides a comprehensive set of
    common tools, so users can focus on making games without having to
    reinvent the wheel. Games can be exported in one click to a number of
    platforms, including the major desktop platforms (Linux, macOS, Windows)
    as well as mobile (Android, iOS) and web-based (HTML5) platforms.

    Godot is completely free and open source under the permissive MIT
    license. No strings attached, no royalties, nothing. Users' games are
    theirs, down to the last line of engine code. Godot's development is fully
    independent and community-driven, empowering users to help shape their
    engine to match their expectations. It is supported by the `Software
    Freedom Conservancy <https://sfconservancy.org>`_ not-for-profit.

For a more in-depth view of the engine, you are encouraged to read this
documentation further, especially the :ref:`Step by step
<toc-learn-step_by_step>` tutorial.

About the documentation
-----------------------

This documentation is continuously written, corrected, edited, and revamped by
members of the Godot Engine community. It is edited via text files in the
`reStructuredText <http://www.sphinx-doc.org/en/stable/rest.html>`_ markup
language and then compiled into a static website/offline document using the
open source `Sphinx <http://www.sphinx-doc.org>`_ and `ReadTheDocs
<https://readthedocs.org/>`_ tools.

.. note:: You can contribute to Godot's documentation by opening issue tickets
          or sending patches via pull requests on its GitHub
          `source repository <https://github.com/godotengine/godot-docs>`_, or
          translating it into your language on `Hosted Weblate
          <https://hosted.weblate.org/projects/godot-engine/godot-docs/>`_.

All the contents are under the permissive Creative Commons Attribution 3.0
(`CC-BY 3.0 <https://creativecommons.org/licenses/by/3.0/>`_) license, with
attribution to "Juan Linietsky, Ariel Manzur and the Godot Engine community".

Organization of the documentation
---------------------------------

This documentation is organized in five sections with an impressively
unbalanced distribution of contents – but the way it is split up should be
relatively intuitive:

- The :ref:`sec-general` section contains this introduction as well as
  information about the engine, its history, its licensing, authors, etc. It
  also contains the :ref:`doc_faq`.
- The :ref:`sec-learn` section is the *raison d'être* of this
  documentation, as it contains all the necessary information on using the
  engine to make games. It starts with the :ref:`Step by step
  <toc-learn-step_by_step>` tutorial which should be the entry point for all
  new users.
- The :ref:`sec-tutorials` section can be read as needed,
  in any order. It contains feature-specific tutorials and documentation.
- The :ref:`sec-devel` section is intended for advanced users and contributors
  to the engine development, with information on compiling the engine,
  developing C++ modules or editor plugins.
- The :ref:`sec-community` section gives information related to contributing to
  engine development and the life of its community, e.g. how to report bugs,
  help with the documentation, etc. It also points to various community channels
  like IRC and Discord and contains a list of recommended third-party tutorials
  outside of this documentation.
- Finally, the :ref:`sec-class-ref` is the documentation of the Godot API,
  which is also available directly within the engine's script editor. It is
  generated automatically from a file in the main source repository, therefore
  the generated files of the documentation are not meant to be modified. See
  :ref:`doc_updating_the_class_reference` for details.

In addition to this documentation you may also want to take a look at the
various `Godot demo projects <https://github.com/godotengine/godot-demo-projects>`_.

Have fun reading and making games with Godot Engine!
