.. _doc_development_philosophy:

Development philosophy
======================

.. note::

    If you're interested in knowing the *design* philosophy behind Godot Engine
    as a user, refer to :ref:`doc_godot_design_philosophy` instead. This page
    describes the *development* philosophy behind the engine itself, for people
    interested in contributing to the engine development.

    If you're already familiar with the engine's scope and goals, proceed to
    :ref:`doc_best_practices_for_engine_contributors` to get familiar with the
    established software engineering practices in relation to Godot development.

Introduction
------------

The development of Godot Engine is governed by various explicit and implicit
thinking processes which might not be instantly or completely obvious to a new
person interested in contributing, especially if that person has already some
preconceived notions regarding the purpose and ideas behind Godot, so it's
important that both new contributors and existing core developers share the same
understanding and vision regarding Godot Engine development to achieve best
results.

This allows to eliminate any confusion and to further improve existing
relationships between contributors, as revealing development ideas is essential
to reaching a general consensus regarding the direction of the project.

Taking into account various cultural differences, the purpose of this page is to
document the history, culture, philosophy, vision, mission, priorities, goals,
non-goals, principles, direction and intention of the Godot Engine project as an
open-source game engine and as a community in general.

History and culture
-------------------

One of the best ways to understand the ideas behind the engine is by going
through the history of Godot development.

The following are some resources which outline the origins of Godot Engine, some
of which may already suggest a general direction of the project, so you can
better see all the aspects and the background behind the engine development for
yourself.

Release news
~~~~~~~~~~~~

* `First public release! <https://godotengine.org/article/first-public-release>`_
* `Godot Engine reaches 1.0, first stable release <https://godotengine.org/article/godot-engine-reaches-1-0>`_
* `Godot 1.1 is out! <https://godotengine.org/article/godot-1-1-out>`_
* `Godot Engine reaches 2.0 stable <https://godotengine.org/article/godot-engine-reaches-2-0-stable>`_
* `Godot reaches 2.1 stable! <https://godotengine.org/article/godot-reaches-2-1-stable>`_
* `Godot 3.0 is out and ready for the big leagues <https://godotengine.org/article/godot-3-0-released>`_
* `Godot 3.1 is out, improving usability and features <https://godotengine.org/article/godot-3-1-released>`_
* `Here comes Godot 3.2, with quality as priority <https://godotengine.org/article/here-comes-godot-3-2>`_

Articles
~~~~~~~~

* `Godot history in images <https://godotengine.org/article/godot-history-images>`_
* `Open source Godot gets two years old! <https://godotengine.org/article/open-source-godot-gets-two-years-old>`_
* `As an Open Source project, Godot is more than a game engine <https://godotengine.org/article/as-oss-godot-is-more-than-a-game-engine>`_
* `A decade in retrospective and future <https://godotengine.org/article/retrospective-and-future>`_

General principles
------------------

In short, there is no *absolute* philosophy behind Godot Engine development.
Community discussion is the only reliable tool currently used to determine what
kind of features are deemed meaningful for Godot development.

As a community-driven, open-source game engine, the core development philosophy
of Godot is created through the uncertainty regarding the direction of the
project, and accepting the reality of that nothing can be truly finished,
because of the very nature of the never-ending process of growth as orchestrated
by community needs.

Due to this,
`Godot Improvement Proposals <https://github.com/godotengine/godot-proposals>`_
was created as the main platform which allows contributors to share and discuss
ideas which could benefit Godot in its current state in order to satisfy
those needs.

.. seealso::

    `Introducing the Godot Proposals repository <https://godotengine.org/article/introducing-godot-proposals-repository>`_

Nonetheless, there are still more or less firm objectives which govern the
engine development that might not be completely obvious to contributors at
first, so it's worth to outline them here.

**Every game engine is different and fits different needs**, and it's impossible
for an engine to solve *every problem that exists under the sun*, so lets
describe those differences and try to setup correct expectations for what
constitutes Godot as a game engine and determine the scope of features being
developed, so you can better understand where our priorities are.

Vision, goals and non-goals
---------------------------

Unlike other game engines with a dedicated editor, Godot aims for high-level
functionality and implementing back-ends which allow to make games to look
pretty, cover **the most common use cases** and only allow **some tweaking**.
The idea is that out of the box the games made in Godot should look as good as
in other game engines, while at the same time making the engine easy to use and
accessible for most people, which may also include non-programmers.

Due to this, the ability to tweak the engine performance for corner use cases
may be lacking, although it should still be good for most games. If we take the
rendering part, the vision here is that ability to customize can be achieved
with a relatively simple renderer, so that any renderer engineer can still tweak
the rendering by themselves that require specific functionality in their game
projects.

Likewise, if there are too many different possible approaches to implement
something (such as AI), the default decision is to not support such a feature
out of the box, but instead provide necessary tools to facilitate implementing
those kind of features by the community via modules and plugins.

The goal is to provide only the most common tools which are typically used by at
least 70% of developers creating video games. This is why Godot is striving to
have a good set of editor tools which allow developers to customize virtually
any part of the editor to satisfy specific use cases.

This way, the core can stay lean and mean, so the engine developers can better
focus on other aspects such as usability, stability and extensibility provided
by modules and plugins. We do our best to make the community plugin ecosystem
grow without bloating the engine with features that will be rarely used in most
game projects.

That said, Godot's philosophy is to favor ease of use and maintenance over
absolute performance. We understand that performance may still be an important
aspect for some projects which use Godot, so performance optimizations will be
considered, but they may not be acceptable if they make something too difficult
to use or if they add too much complexity to the codebase.
