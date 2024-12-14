.. _doc_filesystem:

File system
===========

Introduction
------------

A file system manages how assets are stored and how they are accessed.
A well-designed file system also allows multiple developers to edit the
same source files and assets while collaborating. Godot stores
all assets as files in its file system.

Implementation
--------------

The file system stores resources on disk. Anything, from a script, to a scene or a
PNG image is a resource to the engine. If a resource contains properties
that reference other resources on disk, the paths to those resources are also
included. If a resource has sub-resources that are built-in, the resource is
saved in a single file together with all the bundled sub-resources. For
example, a font resource is often bundled together with the font textures.

The Godot file system avoids using metadata files. Existing asset managers and VCSs
are better than anything we can implement, so Godot tries its best to play along
with Subversion, Git, Mercurial, etc.

Example of file system contents:

.. code-block:: none

    /project.godot
    /enemy/enemy.tscn
    /enemy/enemy.gd
    /enemy/enemysprite.png
    /player/player.gd

project.godot
-------------

The ``project.godot`` file is the project description file, and it is always found
at the root of the project. In fact, its location defines where the root is. This
is the first file that Godot looks for when opening a project.

This file contains the project configuration in plain text, using the win.ini
format. Even an empty ``project.godot`` can function as a basic definition of
a blank project.

Path delimiter
--------------

Godot only supports ``/`` as a path delimiter. This is done for
portability reasons. All operating systems support this, even Windows,
so a path such as ``C:\project\project.godot`` needs to be typed as
``C:/project/project.godot``.

Resource path
-------------

When accessing resources, using the host OS file system layout can be
cumbersome and non-portable. To solve this problem, the special path
``res://`` was created.

The path ``res://`` will always point at the project root (where
``project.godot`` is located, so ``res://project.godot`` is always
valid).

This file system is read-write only when running the project locally from
the editor. When exported or when running on different devices (such as
phones or consoles, or running from DVD), the file system will become
read-only and writing will no longer be permitted.

User path
---------

Writing to disk is still needed for tasks such as saving game state or
downloading content packs. To this end, the engine ensures that there is a
special path ``user://`` that is always writable. This path resolves
differently depending on the OS the project is running on. Local path
resolution is further explained in :ref:`doc_data_paths`.

Host file system
----------------

Alternatively host file system paths can also be used, but this is not recommended
for a released product as these paths are not guaranteed to work on all platforms.
However, using host file system paths can be useful when writing development
tools in Godot.

Drawbacks
---------

There are some drawbacks to this file system design. The first issue is that
moving assets around (renaming them or moving them from one path to another inside
the project) will break existing references to these assets. These references will
have to be re-defined to point at the new asset location.

To avoid this, do all your move, delete and rename operations from within Godot, on
the FileSystem dock. Never move assets from outside Godot, or dependencies will have
to be fixed manually (Godot detects this and helps you fix them anyway, but why
go the hard route?).

The second is that, under Windows and macOS, file and path names are case insensitive.
If a developer working in a case insensitive host file system saves an asset as ``myfile.PNG``,
but then references it as ``myfile.png``, it will work fine on their platform, but not
on other platforms, such as Linux, Android, etc. This may also apply to exported binaries,
which use a compressed package to store all files.

It is recommended that your team clearly define a naming convention for files when
working with Godot. One fool-proof convention is to only allow lowercase
file and path names.
