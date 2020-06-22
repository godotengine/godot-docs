.. _doc_release_policy:

Godot release policy
====================

Godot versioning
----------------

Godot uses ``major.minor.patch`` version numbering. However, it does not
strictly follow `Semantic Versioning <https://semver.org/>`__. This means that
releases considered "semver-minor" by that standard (such as 3.1 -> 3.2) will
most likely introduce breaking changes. Still, there won't be as many breaking
changes as a "semver-major" version bump such as 3.2 -> 4.0.

In the interest of stability and usability, patch releases may occasionally
introduce small breaking changes as well. When repackaging Godot projects (e.g.
in a Flatpak), make sure to always use the same patch version as the one used to
initially export the project.

.. note::

    The first release in a major/minor release series doesn't end with a
    trailing zero. For example, the first release in the 3.2 series is ``3.2``,
    not ``3.2.0``.

Release support timeline
------------------------

Godot versions are supported for a certain amount of time. While these durations
are not set in stone, here's a table with the expected level of support
for each Godot version:

+-------------+-------------------+--------------------------------------------------------------------------+
| **Version** | **Release date**  | **Support level**                                                        |
+-------------+-------------------+--------------------------------------------------------------------------+
| Godot 4.0   | ~2021 (see below) | |unstable| *Current focus of development (unstable).*                    |
+-------------+-------------------+--------------------------------------------------------------------------+
| Godot 3.2   | January 2020      | |supported| Backwards-compatible new features (backported from the       |
|             |                   | ``master`` branch) as well as bug, security, and platform support fixes. |
+-------------+-------------------+--------------------------------------------------------------------------+
| Godot 3.1   | March 2019        | |partial| Only critical, security and platform support fixes.            |
+-------------+-------------------+--------------------------------------------------------------------------+
| Godot 3.0   | January 2018      | |partial| Only critical, security and platform support fixes.            |
+-------------+-------------------+--------------------------------------------------------------------------+
| Godot 2.1   | July 2016         | |partial| Only critical, security and platform support fixes.            |
+-------------+-------------------+--------------------------------------------------------------------------+
| Godot 2.0   | February 2016     | |eol| No longer supported.                                               |
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
|supported| Full support -
|partial| Partial support -
|eol| No support (end of life) -
|unstable| Development version

Pre-release Godot versions aren't intended to be used in production and are
provided on a best-effort basis.

When is the next release out?
-----------------------------

While Godot contributors aren't working under any deadlines, there's usually a
major or minor Godot release made available every year. Following this trend,
this means Godot 4.0 will most likely be released in **2021**.

Patch releases are made available more frequently, typically every 2-6 months
while a release is fully supported. Partially supported releases will only have
new patch releases once an important security or platform support fix has been
merged.

.. seealso::

    The `roadmap <https://github.com/godotengine/godot-roadmap>`__ repository
    documents features that have been agreed upon and may be implemented in future
    Godot releases.
