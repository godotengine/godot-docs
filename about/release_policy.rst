.. _doc_release_policy:

Godot release policy
====================

Godot's release policy is in constant evolution. What is described below is
intended to give a general idea of what to expect, but what will actually
happen depends on the choices of core contributors, and the needs of the
community at a given time.

Godot versioning
----------------

Godot loosely follows `Semantic Versioning <https://semver.org/>`__ with a
``major.minor.patch`` versioning system, albeit with an interpretation of each
term adapted to the complexity of a game engine:

- The ``major`` version is incremented when major compatibility breakages happen
  which imply significant porting work to move projects from one major version
  to another.

  For example, porting Godot projects from Godot 2.1 to Godot 3.0 required
  running the project through a conversion tool, and then performing a number
  of further adjustments manually for what the tool could not do automatically.

- The ``minor`` version is incremented for feature releases that do not break
  compatibility in a major way. Minor compatibility breakage in very specific
  areas *may* happen in minor versions, but the vast majority of projects
  should not be affected or require significant porting work.

  The reason for this is that as a game engine, Godot covers many areas such
  as rendering, physics, scripting, etc., and fixing bugs or implementing new
  features in a given area may sometimes require changing the behavior of a
  feature, or modifying the interface of a given class, even if the rest of
  the engine API remains backwards compatible.

.. tip::

    Upgrading to a new minor version is therefore recommended for all users,
    but some testing is necessary to ensure that your project still behaves as
    expected in a new minor version.

- The ``patch`` version is incremented for maintenance releases which focus on
  fixing bugs and security issues, implementing new requirements for platform
  support, and backporting safe usability enhancements. Patch releases are
  backwards compatible.

  Patch versions may include minor new features which do not impact the
  existing API, and thus have no risk of impacting existing projects.

.. tip::

    Updating to new patch versions is therefore considered safe and strongly
    recommended to all users of a given stable branch.

We call ``major.minor`` combinations *stable branches*. Each stable branch
starts with a ``major.minor`` release (without the ``0`` for ``patch``) and is
further developed for maintenance releases in a Git branch of the same name
(for example patch updates for the 3.3 stable branch are developed in the
``3.3`` Git branch).

.. note::

    As mentioned in the introduction, Godot's release policy is evolving, and
    earlier Godot releases may not have followed the above rules to the letter.
    In particular, the 3.2 stable branch received a number of new features in
    3.2.2 that would have warranted a ``minor`` version increment.

Release support timeline
------------------------

Stable branches are supported *at minimum* until the next stable branch is
released and has received its first patch update. In practice, we support
stable branches on a *best effort* basis for as long as they have active users
who need maintenance updates.

Whenever a new major version is released, we make the previous stable branch a
long-term supported release, and do our best to provide fixes for issues
encountered by users of that branch who cannot port complex projects to the new
major version. This was the case for the 2.1 branch, and will be the case for
the latest 3.x stable branch by the time Godot 4.0 is released.

In a given minor release series, only the latest patch release receives support.
If you experience an issue using an older patch release, please upgrade to the
latest patch release of that series and test again before reporting an issue
on GitHub.

+-------------+----------------------+--------------------------------------------------------------------------+
| **Version** | **Release date**     | **Support level**                                                        |
+-------------+----------------------+--------------------------------------------------------------------------+
| Godot 4.0   | Q4 2022              | |unstable| *Beta.* Current focus of development (unstable).              |
+-------------+----------------------+--------------------------------------------------------------------------+
| Godot 3.6   | Q4 2022              | |supported| *Beta.* Receives new features as well as bug fixes while     |
|             |                      | under development.                                                       |
+-------------+----------------------+--------------------------------------------------------------------------+
| Godot 3.5   | August 2022          | |supported| Receives fixes for bugs, security and platform support       |
|             |                      | issues, as well as backwards-compatible usability enhancements.          |
+-------------+----------------------+--------------------------------------------------------------------------+
| Godot 3.4   | November 2021        | |partial| Receives fixes for security and platform support issues only.  |
+-------------+----------------------+--------------------------------------------------------------------------+
| Godot 3.3   | April 2021           | |eol| No longer supported as fully superseded by the compatible 3.4      |
|             |                      | release (last update: 3.3.4).                                            |
+-------------+----------------------+--------------------------------------------------------------------------+
| Godot 3.2   | January 2020         | |eol| No longer supported (last update: 3.2.3).                          |
+-------------+----------------------+--------------------------------------------------------------------------+
| Godot 3.1   | March 2019           | |eol| No longer supported (last update: 3.1.2).                          |
+-------------+----------------------+--------------------------------------------------------------------------+
| Godot 3.0   | January 2018         | |eol| No longer supported (last update: 3.0.6).                          |
+-------------+----------------------+--------------------------------------------------------------------------+
| Godot 2.1   | July 2016            | |eol| No longer supported (last update: 2.1.6).                          |
+-------------+----------------------+--------------------------------------------------------------------------+
| Godot 2.0   | February 2016        | |eol| No longer supported (last update: 2.0.4.1).                        |
+-------------+----------------------+--------------------------------------------------------------------------+
| Godot 1.1   | May 2015             | |eol| No longer supported.                                               |
+-------------+----------------------+--------------------------------------------------------------------------+
| Godot 1.0   | December 2014        | |eol| No longer supported.                                               |
+-------------+----------------------+--------------------------------------------------------------------------+

.. |supported| image:: img/supported.png
.. |partial| image:: img/partial.png
.. |eol| image:: img/eol.png
.. |unstable| image:: img/unstable.png

**Legend:**
|supported| Full support –
|partial| Partial support –
|eol| No support (end of life) –
|unstable| Development version

Pre-release Godot versions aren't intended to be used in production and are
provided for testing purposes only.

.. seealso::

    See :ref:`doc_upgrading_to_godot_4` for instructions on migrating a project.

.. _doc_release_policy_when_is_next_release_out:

When is the next release out?
-----------------------------

While Godot contributors aren't working under any deadlines, we strive to
publish minor releases relatively frequently, with an average of two 3.x minor
releases per year since Godot 3.3.

Maintenance (patch) releases are released as needed with potentially very
short development cycles, to provide users of the current stable branch with
the latest bug fixes for their production needs.

As for the upcoming Godot 4.0, as of August 2022, we are aiming for a *beta*
release in Q3 2022, and possibly a stable release by Q4 2022 (but experience
has shown time and time again that such estimates tend to be overly optimistic).
`Follow the Godot blog <https://godotengine.org/news>`__ for the latest updates.
