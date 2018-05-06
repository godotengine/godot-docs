.. _doc_project_organization:

Project organization
====================

Introduction
------------

This tutorial is aimed to propose a simple workflow on how to organize
projects. Since Godot allows the programmer to use the file-system as
they please, figuring out a way to organize the projects when
starting to use the engine can be a little challenging. Because of this,
a simple workflow will be described, which can be used or not, but
should work as a starting point.

Additionally, using version control can be challenging so this
proposition will include that too.

Organization
------------

Godot is scene based in nature, and uses the filesystem as-is,
without metadata or an asset database. 

Unlike other engines, a lot of resource are contained within the scene
itself, so the amount of files in the filesystem is considerably lower.

Considering that, the most common approach is to group assets close to scenes as,
when a project grows, it makes it more maintainable.

As example, base sprite images, 3D model scenes or meshes, materials, etc.
can usually be organized in a place, while a separate folder is used
to store built levels that use them.

::

    /project.godot
    /docs/.gdignore
    /docs/learning.html
    /models/town/house/house.dae
    /models/town/house/window.png
    /models/town/house/door.png
    /characters/player/cubio.dae
    /characters/player/cubio.png
    /characters/enemies/goblin/goblin.dae
    /characters/enemies/goblin/goblin.png
    /characters/npcs/suzanne/suzanne.dae
    /characters/npcs/suzanne/suzanne.png
    /levels/riverdale/riverdale.scn

Importing
---------

Godot version previous to 3.0 did the import process from files outside
the project. While this can be useful in large projects, it
resulted in an organization hassle for most developers.

Because of this, assets are now imported from within the project
folder transparently.

If a folder shouldn't be imported into Godot an exception can be made with a
.gdignore file.
