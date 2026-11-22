:allow_comments: False

.. _doc_release_policy:

Godot release policy
====================

This article describes Godot's versioning scheme and release policy, as of today.

We do not expect this policy to change substantially anytime soon, though each
version might deviate in minor ways in practice. Major changes to our release
policy will be announced on the `Godot blog <https://godotengine.org/blog/>`__.

Godot versioning
----------------

Godot loosely follows `Semantic Versioning <https://semver.org/>`__ with a
``major.minor.patch`` versioning system, albeit an interpretation more suitable
for Godot's development and users:

- The ``major`` version (for example, "Godot 4") is incremented when we break
  compatibility and remove deprecated features. Upgrading to a new major version
  might require substantial effort from you to change your project files.

- The ``minor`` version is incremented for feature releases that do not break
  compatibility in a major way for the vast majority of projects.

  The exception is when breaking compatibility is necessary for a change or fix
  that unblocks substantially more projects than it breaks compatibility for.

- The ``patch`` version is incremented for maintenance releases, which provide
  low-risk changes such as bug fixes and security improvements, and meeting
  new platform requirements.

.. note::

    Features marked as ``experimental`` can change at any time.

.. _doc_release_policy_which_version_should_i_use:

Which version should I use for a new project?
---------------------------------------------

We recommend using the newest stable version of Godot 4 for new projects.

Godot 3 is still supported, but receives fewer bug fixes and new features than
Godot 4, and will likely stop receiving support long before Godot 4 does.

.. _doc_release_policy_should_i_upgrade_my_project:

Should I upgrade my project to new engine versions?
---------------------------------------------------

We recommend for all projects to upgrade to new ``patch`` versions as soon
as possible, as they bring important bug fixes and security improvements while
not requiring any additional work to upgrade for the vast majority of projects.

For new ``minor`` releases, we recommend updating as soon as you are able, but to
set some time aside for the upgrade, to read the relevant :ref:`migration guides <doc_migrating_to_a_new_version>`
and to test your game for any regressions.

This is because we do not provide long-term support (LTS) releases, so a game
sticking to an older ``minor`` release :ref:`stops receiving important fixes <doc_release_support_timeline>`
eventually. However, our policies ensure that even ``minor`` updates should be
easy and low-risk for most projects.

As for new ``major`` releases:

- We do not yet have a timeline for Godot 5. When it comes, an upgrade is expected
  to be easy for users, as long as they don't use deprecated features.

- Upgrading from Godot 3 to Godot 4 can be difficult for larger projects.
  We recommend carefully weighing the :ref:`cost and benefit <doc_upgrading_to_godot_4>`
  for anyone considering the upgrade, since a lot of changes came with no
  easy compatibility path.

Can I use deprecated features?
------------------------------

We recommend avoiding deprecated features. If you already use any, we recommend
switching away from them at your convenience, according to each deprecation notes'
advice.

Deprecated features generally stay supported until the eventual Godot 5 release,
so you should not have issues continuing to use them as you upgrade to new
``minor`` and ``patch`` releases.

However, we deprecate features only when there's a good reason to, so please read
deprecation notes carefully and consider using the recommended alternatives.
Deprecated features will receive some support in the form of bug fixes and
improvements, but generally less than the recommended alternatives.

.. _doc_release_support_timeline:

Release support timeline
------------------------

.. UPDATE: Table changes every minor version. Support policy may change.

Godot releases are supported *at least* until the next stable version is
released and has received its first patch update. In practice, we support
stable branches on a *best effort* basis for as long as they have active users
who need maintenance updates.

+--------------+----------------------+--------------------------------------------------------------------------+
| **Version**  | **Release date**     | **Support level**                                                        |
+--------------+----------------------+--------------------------------------------------------------------------+
| Godot 4.8    | Q4 2026 (estimate)   | |unstable| *Development.* Receives new features, usability and           |
| (`master`)   |                      | performance improvements, as well as bug fixes, while under development. |
+--------------+----------------------+--------------------------------------------------------------------------+
| Godot 4.7    | June 2026            | |supported| Receives fixes for bugs and security issues, as well as      |
|              |                      | patches that enable platform support.                                    |
+--------------+----------------------+--------------------------------------------------------------------------+
| Godot 4.6    | January 2026         | |supported| Receives fixes for bugs and security issues, as well as      |
|              |                      | patches that enable platform support.                                    |
+--------------+----------------------+--------------------------------------------------------------------------+
| Godot 4.5    | September 2025       | |partial| Receives fixes for security and platform support issues only.  |
+--------------+----------------------+--------------------------------------------------------------------------+
| Godot 4.4    | March 2025           | |eol| No longer supported (last update: 4.4.1).                          |
+--------------+----------------------+--------------------------------------------------------------------------+
| Godot 4.3    | August 2024          | |eol| No longer supported (last update: 4.3).                            |
+--------------+----------------------+--------------------------------------------------------------------------+
| Godot 4.2    | November 2023        | |eol| No longer supported (last update: 4.2.2).                          |
+--------------+----------------------+--------------------------------------------------------------------------+
| Godot 4.1    | July 2023            | |eol| No longer supported (last update: 4.1.4).                          |
+--------------+----------------------+--------------------------------------------------------------------------+
| Godot 4.0    | March 2023           | |eol| No longer supported (last update: 4.0.4).                          |
+--------------+----------------------+--------------------------------------------------------------------------+
| Godot 3.7    | No ETA for now       | |supported| *Beta.* Receives new features, usability and performance     |
| (`3.x`)      |                      | improvements, as well as bug fixes, while under development.             |
+--------------+----------------------+--------------------------------------------------------------------------+
| Godot 3.6    | September 2024       | |supported| Receives fixes for bugs and security issues, as well as      |
|              |                      | patches that enable platform support.                                    |
+--------------+----------------------+--------------------------------------------------------------------------+
| Godot 3.5    | August 2022          | |eol| No longer supported (last update: 3.5.3).                          |
+--------------+----------------------+--------------------------------------------------------------------------+
| Godot 3.4    | November 2021        | |eol| No longer supported (last update: 3.4.5).                          |
+--------------+----------------------+--------------------------------------------------------------------------+
| Godot 3.3    | April 2021           | |eol| No longer supported (last update: 3.3.4).                          |
+--------------+----------------------+--------------------------------------------------------------------------+
| Godot 3.2    | January 2020         | |eol| No longer supported (last update: 3.2.3).                          |
+--------------+----------------------+--------------------------------------------------------------------------+
| Godot 3.1    | March 2019           | |eol| No longer supported (last update: 3.1.2).                          |
+--------------+----------------------+--------------------------------------------------------------------------+
| Godot 3.0    | January 2018         | |eol| No longer supported (last update: 3.0.6).                          |
+--------------+----------------------+--------------------------------------------------------------------------+
| Godot 2.1    | July 2016            | |eol| No longer supported (last update: 2.1.6).                          |
+--------------+----------------------+--------------------------------------------------------------------------+
| Godot 2.0    | February 2016        | |eol| No longer supported (last update: 2.0.4.1).                        |
+--------------+----------------------+--------------------------------------------------------------------------+
| Godot 1.1    | May 2015             | |eol| No longer supported.                                               |
+--------------+----------------------+--------------------------------------------------------------------------+
| Godot 1.0    | December 2014        | |eol| No longer supported.                                               |
+--------------+----------------------+--------------------------------------------------------------------------+

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

We have no concrete timeline for when the next ``major`` update (Godot 4 to
Godot 5) will happen, but it will be motivated by needing to drop compatibility
for technical reasons.

New ``minor`` versions are released 2-3 times a year.

New ``patch`` versions are released as necessary, but expect them to arrive
more often than new ``minor`` versions.
