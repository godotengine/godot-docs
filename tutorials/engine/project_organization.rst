.. _doc_project_organization:

Project organization
====================

Introduction
------------

This tutorial is aimed to propose a simple workflow on how to organize
projects. Since Godot allows the programmer to use the file-system as he
or she pleases, figuring out a way to organize the projects when
starting to use the engine can be a little challenging. Because of this,
a simple workflow will be described, which can be used or not, but
should work as a starting point.

Additionally, using version control can be challenging so this
proposition will include that too.

Organization
------------

Other game engines often work by having an asset database, were you can
browse images, models, sounds, etc. Godot is more scene-based in nature
so most of the time the assets are bundled inside the scenes or just
exist as files but are referenced from scenes.

Importing & game folder
-----------------------

It is very often necessary to use asset importing in Godot. As the
source assets for importing are also recognized as resources by the
engine, this can become a problem if both are inside the project folder,
because at the time of export the exporter will recognize them and
export both.

To solve this, it is a good practice to have your game folder inside
another folder (the actual project folder). This allows to have the game
assets separated from the source assets, and also allows to use version
control (such as svn or git) for both. Here is an example:

::

    myproject/art/models/house.max
    myproject/art/models/sometexture.png
    myproject/sound/door_open.wav
    myproject/sound/door_close.wav
    myproject/translations/sheet.csv

Then also, the game itself is, in this case, inside a game/ folder:

::

    myproject/game/engine.cfg
    myproject/game/scenes/house/house.scn
    myproject/game/scenes/house/sometexture.tex
    myproject/game/sound/door_open.smp
    myproject/game/sound/door_close.smp
    myproject/game/translations/sheet.en.xl
    myproject/game/translations/sheet.es.xl

Following this layout, many things can be done:

-  The whole project is still inside a folder (myproject/).
-  Exporting the project will not export the .wav and .png files which
   were imported.
-  myproject/ can be put directly inside a VCS (like svn or git) for
   version control, both game and source assets are kept track of.
-  If a team is working on the project, assets can be re-imported by
   other project members, because Godot keeps track of source assets
   using relative paths.

Scene organization
------------------

Inside the game folder, a question that often arises is how to organize
the scenes in the filesystem. Many developers try asset-type based
organization and end up having a mess after a while, so the best answer
is probably to organize them based on how the game works and not based
on asset type. Here are some examples.

If you were organizing your project based on asset type, it would look
like this:

::

    game/engine.cfg
    game/scenes/scene1.scn
    game/scenes/scene2.scn
    game/textures/texturea.png
    game/textures/another.tex
    game/sounds/sound1.smp
    game/sounds/sound2.wav
    game/music/music1.ogg

Which is generally a bad idea. When a project starts growing beyond a
certain point, this becomes unmanageable. It's really difficult to tell
what belongs to what.

It's generally a better idea to use game-context based organization,
something like this:

::

    game/engine.cfg
    game/scenes/house/house.scn
    game/scenes/house/texture.tex
    game/scenes/valley/canyon.scn
    game/scenes/valley/rock.scn
    game/scenes/valley/rock.tex
    game/scenes/common/tree.scn
    game/scenes/common/tree.tex
    game/player/player.scn
    game/player/player.gd
    game/npc/theking.scn
    game/npc/theking.gd
    game/gui/main_screen/main_sceen.scn
    game/gui/options/options.scn

This model or similar models allows projects to grow to really large
sizes and still be completely manageable. Notice that everything is
based on parts of the game that can be named or described, like the
settings screen or the valley. Since everything in Godot is done with
scenes, and everything that can be named or described can be a scene,
this workflow is very smooth and easygoing.

Cache files
-----------

Godot uses a hidden file called ".fscache" at the root of the project.
On it, it caches project files and is used to quickly know when one is
modified. Make sure to **not commit this file** to git or svn, as it
contains local information and might confuse another editor instance in
another computer.
