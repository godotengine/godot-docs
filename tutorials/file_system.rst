File System
===========

Introduction
------------

Filesystem usage is yet another hot topic in engine development. This
means, where are assets stored, how are they accessed, how do multiple
programmers edit the same repository, etc.

Initial versions of the engine (and previous iterations before it was
named Godot) used a database. Assets were stored there and assigned an
ID. Other approaches were tested, too, with local databases, files with
metadata, etc. To say truth, and after a long time, simplicity proved to
be best and Godot stores all assets as files in the flesystem.

Implementation
--------------

Godot stores resources to disk. Anything, from a script, to a scene or a
PNG image is a resource to the engine. If a resource contains properties
that referece other resources on disk, the path to that resource is
included. If it has sub-resources that are built-in, the resource is
saved in a single file together with all the bundled sub-resources. For
example, a font resource is often saved with the character textures
bundled inside.

Metadata files were also dropped and the whole engine design tries to
avoid them. The reason for this is simple, existing asset managers and
VCSs are just much better than anything we can implement, so Godot tries
the best to play along with SVN, Git, Mercurial, Perforce, etc.

engine.cfg
----------

| The mere existence of this file marks that there is a Godot project in
  that directory and all sub-directories.
| This file contains the project configuration in plain text, win.ini
  style, though it will work to mark the existence of a project even if
  the file is empty.

Example of a filesystem:

::

    /engine.cfg
    /enemy/enemy.scn
    /enemy/enemy.gd
    /enemy/enemysprite.png
    /player/player.gd

Directory Delimiter
-------------------

Godot only supports "/" as a directory delimiter. This is done for
portability reasons. All operating systems support this, even Windows,
so a path such as c:\\\\project\\\\engine.cfg needs to be typed as
c:/project/engine.cfg.

Resource Path
-------------

For accessing resources, using the host OS filesystem layout can be
cumbersome and non portable. To solve this problem, the specal path
\`"res://"\` was created.

The path \`"res://"\` will always point at the project root (where
engine.cfg is located, so in fact \`"res://engine.cfg"\` is always
valid).

This filesystem is read-write only when running the project locally from
the editor. When exported or when running on different devices (such as
phones or consoles, or running from DVD), the filesystem will become
read-only and writing will no longer be permitted.

User Path
---------

Writing to disk is still needed often, from doing a savegame to
downloading content packs. For this, the engine ensures that there is a
special path \`"user://"\` that is always writable.

Host Filesystem
---------------

Of course, opening the host filesystem always works, as this is always
useful when Godot is used to write tools, but for shipped projects this
is discouraged and may not even be supported in some platforms.

Drawbacks
---------

Not everything is rosy. Using resources and files and the plain
filesystem has two main drawbacks. The first is that moving assets
around (renaming them or moving them from a directory to another inside
the project) once they are referenced is not that easy. If this is done,
then dependencies will need to be re-satisfied upon load.

The second is that under Windows or OSX, file access is case
insensitive. If a developer works in this operating system and saves a
file like "myfile.PNG", then references it as "myfile.png", it will work
there, but not on any other platform, such as Linux, Android, etc. It
may also not work on exported binaries, which use a compressed package
for files.

Because of this, please instruct your team to use a specific naming
convention for files when working with Godot!

*Juan Linietsky, Ariel Manzur, Distributed under the terms of the `CC
By <https://creativecommons.org/licenses/by/3.0/legalcode>`__ license.*
