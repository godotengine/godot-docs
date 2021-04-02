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

- The ``minor`` version is incremented for feature releases which do not break
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
    3.2.2 which would have warranted a ``minor`` version increment.

Release support timeline
------------------------

Stable branches are supported *at minimum* until the next stable branch is
released and has received its first patch update. In practice, we support
stable branches on a *best effort* basis for as long as they have active users
who need maintenance updates.

Whenever a new major version is released, we make the previous stable branch a
long-term supported release, and do our best to provide fixes for issues
encountered by users of that branch who cannot port complex projects to the new
major version. This is the case for the 2.1 branch, and will be the case for
the latest 3.x stable branch by the time Godot 4.0 is released.

.. To add once 3.3 is released:
   | Godot 3.4   | Q2 or Q3 2021     | |supported| *Beta.* Receives new features as well as bug fixes while     |
   |             |                   | under development.                                                       |

+-------------+-------------------+--------------------------------------------------------------------------+
| **Version** | **Release date**  | **Support level**                                                        |
+-------------+-------------------+--------------------------------------------------------------------------+
| Godot 4.0   | ~2021 (see below) | |unstable| *Current focus of development (unstable).*                    |
+-------------+-------------------+--------------------------------------------------------------------------+
| Godot 3.3   | April 2021        | |supported| Receives bug, security and platform support fixes, as well   |
|             |                   | as backwards-compatible usability enhancements.                          |
+-------------+-------------------+--------------------------------------------------------------------------+
| Godot 3.2   | January 2020      | |partial| Only critical, security and platform support fixes             |
|             |                   | (last update: 3.2.3).                                                    |
+-------------+-------------------+--------------------------------------------------------------------------+
| Godot 3.1   | March 2019        | |partial| Only critical, security and platform support fixes             |
|             |                   | (last update: 3.1.2).                                                    |
+-------------+-------------------+--------------------------------------------------------------------------+
| Godot 3.0   | January 2018      | |eol| No longer supported (last update: 3.0.6).                          |
+-------------+-------------------+--------------------------------------------------------------------------+
| Godot 2.1   | July 2016         | |partial| Only critical, security and platform support fixes             |
|             |                   | (last update: 2.1.6).                                                    |
+-------------+-------------------+--------------------------------------------------------------------------+
| Godot 2.0   | February 2016     | |eol| No longer supported (last update: 2.0.4.1).                        |
+-------------+-------------------+--------------------------------------------------------------------------+
| Godot 1.1   | May 2015          | |eol| No longer supported.                                               |
+-------------+-------------------+--------------------------------------------------------------------------+
| Godot 1.0   | December 2014     | |eol| No longer supported.                                               |
+-------------+-------------------+--------------------------------------------------------------------------+

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

.. _doc_release_policy_when_is_next_release_out:

When is the next release out?
-----------------------------

While Godot contributors aren't working under any deadlines, we have
historically had one major or minor release per year, with several maintenance
updates between each.

Starting with Godot 3.3, we aim to accelerate our development cycles for minor
releases, so you can expect a new minor release every 3 to 6 months.

Maintenance (patch) releases will be released as needed with potentially very
short development cycles, to provide users of the current stable branch with
the latest bug fixes for their production needs.

As for the upcoming Godot 4.0, we can only say that we aim for a **2021**
release, but any closer estimate is likely to be hard to uphold. Alpha builds
will be published as soon as the main features for Godot 4.0 are finalized.
