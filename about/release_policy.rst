.. _doc_release_policy:

Godot release policy
====================

Godot's release policy is in constant evolution. The description below
provides a general idea of what to expect, but what will actually
happen depends on the choices of core contributors and the needs of the
community at a given time.

Godot versioning
----------------

Godot loosely follows `Semantic Versioning <https://semver.org/>`__ with a
``major.minor.patch`` versioning system, albeit with an interpretation of each
term adapted to the complexity of a game engine:

- The ``major`` version is incremented when major compatibility breakages happen
  which imply significant porting work to move projects from one major version
  to another.

  For example, porting Godot projects from Godot 3.x to Godot 4.x requires
  running the project through a conversion tool, and then performing a number
  of further adjustments manually for what the tool could not do automatically.

- The ``minor`` version is incremented for feature releases that do not break
  compatibility in a major way. Minor compatibility breakage in very specific
  areas *may* happen in minor versions, but the vast majority of projects
  should not be affected or require significant porting work.

  This is because Godot, as a game engine, covers many areas like rendering,
  physics, and scripting. Fixing bugs or implementing new features in one area
  might sometimes require changing a feature's behavior or modifying a class's
  interface, even if the rest of the engine API remains backwards compatible.

.. tip::

    Upgrading to a new minor version is recommended for all users,
    but some testing is necessary to ensure that your project still behaves as
    expected.

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
(for example patch updates for the 4.0 stable branch are developed in the
``4.0`` Git branch).

Release support timeline
------------------------

Stable branches are supported *at least* until the next stable branch is
released and has received its first patch update. In practice, we support
stable branches on a *best effort* basis for as long as they have active users
who need maintenance updates.

Whenever a new major version is released, we make the previous stable branch a
long-term supported release, and do our best to provide fixes for issues
encountered by users of that branch who cannot port complex projects to the new
major version. This was the case for the 2.1 branch, and is the case for the
3.6 branch.

In a given minor release series, only the latest patch release receives support.
If you experience an issue using an older patch release, please upgrade to the
latest patch release of that series and test again before reporting an issue
on GitHub.

+-------------+----------------------+--------------------------------------------------------------------------+
| **Version** | **Release date**     | **Support level**                                                        |
+-------------+----------------------+--------------------------------------------------------------------------+
| Godot 4.1   | Q2-Q3 2023 (estimate)| |unstable| *Development.* Receives new features as well as bug fixes     |
| (`master`)  |                      | while under development.                                                 |
+-------------+----------------------+--------------------------------------------------------------------------+
| Godot 4.0   | March 2023           | |supported| Receives fixes for bugs, security and platform support       |
|             |                      | issues, as well as backwards-compatible usability enhancements.          |
+-------------+----------------------+--------------------------------------------------------------------------+
| Godot 3.6   | Q2-Q3 2023 (estimate)| |supported| *Beta.* Receives new features as well as bug fixes while     |
| (`3.x`, LTS)|                      | under development. Will be released *after* 4.0.                         |
+-------------+----------------------+--------------------------------------------------------------------------+
| Godot 3.5   | August 2022          | |supported| Receives fixes for bugs, security and platform support       |
|             |                      | issues, as well as backwards-compatible usability enhancements.          |
+-------------+----------------------+--------------------------------------------------------------------------+
| Godot 3.4   | November 2021        | |eol| No longer supported, as fully superseded by the compatible 3.5     |
|             |                      | release (last update: 3.4.5).                                            |
+-------------+----------------------+--------------------------------------------------------------------------+
| Godot 3.3   | April 2021           | |eol| No longer supported, as fully superseded by the compatible 3.4     |
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

    See :ref:`doc_upgrading_to_godot_4` for instructions on migrating a project
    from Godot 3.x to 4.x.

.. _doc_release_policy_when_is_next_release_out:

When is the next release out?
-----------------------------

While Godot contributors aren't working under any deadlines, we strive to
publish minor releases relatively frequently.

In particular, after the very length release cycle for 4.0, we are pivoting to
a faster paced development workflow, with the 4.1 release expected within late
Q2 / early Q3 2023.

Frequent minor releases will enable us to ship new features faster (possibly
as experimental), get user feedback quickly, and iterate to improve those
features and their usability. Likewise, the general user experience will be
improved more steadily with a faster path to the end users.

Maintenance (patch) releases are released as needed with potentially very
short development cycles, to provide users of the current stable branch with
the latest bug fixes for their production needs.

The 3.6 release is still planned and should be the last stable branch of Godot
3.x. It will be a Long-Term Support (LTS) release, which we plan to support for
as long as users still need it (due to missing features in Godot 4.x, or
having published games which they need to keep updating for platform
requirements).
