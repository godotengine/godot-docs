:allow_comments: False

Godot Docs – *master* branch
============================

.. only:: not i18n

  .. note:: Godot's documentation is available in various languages and versions.
            Expand the "Read the Docs" panel at the bottom of the sidebar to see
            the list.

.. only:: i18n

  .. note:: This documentation is translated from the `original English one
            <https://docs.godotengine.org/en/stable>`_ by community members
            on `Weblate <https://hosted.weblate.org/projects/godot-engine/godot-docs>`_.

            Depending on the translation effort's completion level, you may
            find paragraphs or whole pages which are still in English. You can
            help the community by providing new translations or reviewing existing
            ones on Weblate.

            For the time being, localized translations are only available for
            the "stable" branch. You can still view the English documentation for
            other engine versions using the "Read the Docs" panel at the bottom
            of the sidebar.

Welcome to the official documentation of `Godot Engine <https://godotengine.org>`__,
the free and open source community-driven 2D and 3D game engine! If you are new
to this documentation, we recommend that you read the
:ref:`introduction page <doc_about_intro>` to get an overview of what this
documentation has to offer.

To begin reading the relevant documentation, select the tile that matches your profile:

.. raw:: html

    <style>
        .grid-container {
            display: grid;
            grid-template-columns: 1fr 1fr;
            grid-template-rows: 1fr 1fr;
            gap: 0.375rem;
            grid-auto-flow: row;
            grid-template-areas:
            "new-to-game know-game-learn-godot"
            "know-godot-learn-godot contribute-to-godot";
        }

        .grid-item {
            color: hsla(0, 0%, 100%, 0.9);
            padding: 1rem;
            border-radius: 0.375rem;
            text-align: center;
        }

        .grid-item:visited {
            color: unset;
        }

        .grid-item:hover,
        .grid-item:focus {
            text-decoration: none;
            filter: brightness(120%);
        }

        .grid-item:active {
            filter: brightness(80%);
        }

        .new-to-game {
            grid-area: new-to-game;
            background-color: #166534;
        }

        .know-game-learn-godot {
            grid-area: know-game-learn-godot;
            background-color: #115e59;
        }

        .know-godot-learn-godot {
            grid-area: know-godot-learn-godot;
            background-color: #1e3a8a;
        }

        .contribute-to-godot {
            grid-area: contribute-to-godot;
            background-color: #831843;
        }
    </style>
    <div class="grid-container">
        <a class="grid-item new-to-game" href="about/introduction.html">
            I've never made a game before,<br>
            <strong>I want to make a game.</strong>
        </a>
        <a class="grid-item know-game-learn-godot" href="getting_started/step_by_step/index.html">
            I know how to make a game,<br>
            <strong>I want to know how to use Godot.</strong>
            </a>
        <a class="grid-item know-godot-learn-godot" href="tutorials/index.html">
            I know how to use Godot,<br>
            <strong>I want to learn more advanced Godot topics.</strong>
        </a>
        <a class="grid-item contribute-to-godot" href="https://contributing.godotengine.org/en/latest/organization/how_to_contribute.html">
            I know how to use Godot,<br>
            <strong>I want to contribute to Godot.</strong>
        </a>
    </div>
    <br>

You can also use the table of contents in the sidebar to easily access
any section of the documentation for your topic of interest. You can 
also use the search function in the top-left corner.

Get involved
------------

Godot Engine is an open source project developed by a community of volunteers.
The documentation team can always use your feedback and help to improve the
tutorials and class reference. If you don't understand something, or cannot find
what you are looking for in the docs, help us make the documentation better
by letting us know!

Submit an issue or pull request on the `GitHub repository <https://github.com/godotengine/godot-docs/issues>`_,
help us `translate the documentation <https://hosted.weblate.org/engage/godot-engine/>`_
into your language, or talk to us on the ``#documentation`` channel on the
`Godot Contributors Chat <https://chat.godotengine.org/>`_!

.. centered:: |weblate_widget|

Offline documentation
---------------------

To browse the documentation offline, you can download an HTML copy (updated every Monday): `stable <https://nightly.link/godotengine/godot-docs/workflows/build_offline_docs/master/godot-docs-html-stable.zip>`__, `latest <https://nightly.link/godotengine/godot-docs/workflows/build_offline_docs/master/godot-docs-html-master.zip>`__, `3.6 <https://nightly.link/godotengine/godot-docs/workflows/build_offline_docs/master/godot-docs-html-3.6.zip>`__. Extract the ZIP archive then open
the top-level ``index.html`` in a web browser.

For mobile devices or e-readers, you can also download an ePub copy (updated every Monday): `stable <https://nightly.link/godotengine/godot-docs/workflows/build_offline_docs/master/godot-docs-epub-stable.zip>`__, `latest <https://nightly.link/godotengine/godot-docs/workflows/build_offline_docs/master/godot-docs-epub-master.zip>`__, `3.6 <https://nightly.link/godotengine/godot-docs/workflows/build_offline_docs/master/godot-docs-epub-3.6.zip>`__. Extract the ZIP archive then open
the ``GodotEngine.epub`` file in an e-book reader application.

.. Below is the main table-of-content tree of the documentation website.
   It is hidden on the page itself, but it makes up the sidebar for navigation.

.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: About
   :name: sec-general

   about/introduction
   about/list_of_features
   about/system_requirements
   about/faq
   about/complying_with_licenses
   about/release_policy
   about/docs_changelog

.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: Getting started
   :name: sec-learn

   getting_started/introduction/index
   getting_started/step_by_step/index
   getting_started/first_2d_game/index
   getting_started/first_3d_game/index


.. Sections below are split into two groups. First come meta sections, covering
   general matters. Below that different areas of the engine are listed.
   These sections are sorted alphabetically. Please keep them that way.
.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: Manual
   :name: sec-tutorials

   tutorials/best_practices/index
   tutorials/troubleshooting
   tutorials/editor/index
   tutorials/migrating/index

   tutorials/2d/index
   tutorials/3d/index
   tutorials/animation/index
   tutorials/assets_pipeline/index
   tutorials/audio/index
   tutorials/export/index
   tutorials/io/index
   tutorials/i18n/index
   tutorials/inputs/index
   tutorials/math/index
   tutorials/navigation/index
   tutorials/networking/index
   tutorials/performance/index
   tutorials/physics/index
   tutorials/platform/index
   tutorials/plugins/index
   tutorials/rendering/index
   tutorials/scripting/index
   tutorials/shaders/index
   tutorials/ui/index
   tutorials/xr/index


.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: Engine details
   :name: sec-engine-details

   engine_details/architecture/index
   engine_details/engine_api/index
   engine_details/development/index
   engine_details/editor/index
   engine_details/class_reference/index
   engine_details/file_formats/index


.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: Community
   :name: sec-community

   community/asset_library/index
   community/channels
   community/tutorials


.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: Class reference
   :name: sec-class-ref

   classes/index
