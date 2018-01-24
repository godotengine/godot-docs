Godot’s design philosophy
=========================

**Every game engine is different and fits different needs**. They do not
only offer a wide range of features: each engine’s design is unique. This
leads to different workflows and different ways to reason about your
games’ structure. This all stems from their design philosophy.

This page is here to **help you understand how Godot works**, starting
from some of its core pillars. It is not a list of available features or
an engine comparison. To know whether any engine can be a good fit for
your project or not, you need to both try it out for yourself and
understand its design and limitations.

Object-oriented design and composition
--------------------------------------

Godot embraces object-oriented design at its core with its **flexible
scene system and Node hierarchy**. It tries to stay away from strict
programming patterns to offer an intuitive way to structure your game.

For one, Godot lets you **compose or aggregate** scenes.
It's like nested prefabs: you can create a BlinkingLight scene and
a BrokenLantern scene that uses the BlinkingLight.
Then, create a city filled with BrokenLanterns.
Change the BlinkingLight's color, save, and all the
BrokenLanterns in the city will update instantly.

On top of that, you can **inherit** from any scene.

A Godot scene could be a Weapon, a Character, an Item, a Door, a Level,
part of a level… anything you’d like. It works like a class in pure code
except you’re free to design it using the editor, using only the
code, or mixing and matching the two.

It’s different from prefabs you find in several 3d engines as you can
then inherit from and extend those scenes. You may create a Magician
that extends your Character. Modify the Character in the editor and the Magician
will update as well. It helps you build your projects so that their
structure matches the game’s design.

|image0|

Also note that Godot offers many different types of objects called
nodes, each with a specific purpose. Nodes are part of a tree and always
inherit from their parents up to the Node class. Although the engine
does feature some components like collision shapes, they’re the
exception, not the norm.

|image1|

Sprite is a Node2D, a CanvasItem and a Node. It has all the properties
and features of its three parent classes, like transforms or the ability
to draw custom shapes and render with a custom shader.

All-inclusive package
---------------------

Godot tries to provide its own tools to answer all of the most common
needs. It has a dedicated scripting workspace, an animation editor, a
tilemap editor, a shader editor, a debugger, a profiler,
hot-reload locally and on remote devices, etc.

|image2|

The goal is to offer a full package to create games and a continuous
user experience. You can still work with external programs as long as
there is an import plugin for it or you can create one, like the `Tiled
map editor importer <https://github.com/vnen/godot-tiled-importer>`__.

That is also partly why Godot offers its own programming languages
GDscript and VisualScript, along with C#. They’re designed for the needs
of game developers, game designers, and they’re tightly integrated in
the engine and the editor.

GDscript lets you write simple code using a Python-like syntax,
yet it detects types and offers a static-language's quality of auto-completion.
It's also optimized for gameplay code with built-in types like Vectors, Colors, etc.

Note that with GDNative, you can write high performance code using compiled
languages like C, C++, Rust or Python (Cython compiler) without recompiling
the engine.


|image3|

*VisualScript is a node-based programming language that integrates well
in the editor. You can drag and drop nodes or resources into the graph
to create new code blocks.*

Note that if this is true for 2d at the time of writing, the 3d
workspace still doesn’t feature as many tools. You’ll need external
programs or add-ons to edit terrains, animate complex characters, etc.
Godot provides a complete API to extend the editor’s functionality using
game code. See `The Godot editor is a Godot game <#>`__ below.

|image4|

*A State Machine editor plugin in Godot 2 by kubecz3k. It lets you
manage states and transitions visually*

Open source
-----------

Godot offers a fully open source code-base under the MIT license. This
means all the technologies that ship with it have to be Free as well.
For the most part, they’re coded from the ground up by contributors.

Anyone can plug in proprietary tools for the needs of their projects.
They just won’t ship with the engine. This may include NViDia PhysX,
Google Admob or an FBX file importer. Any of these can come as
third-party plugins instead.

On the other hand, an open codebase means you can learn from and extend
the engine to your heart’s content. You can also debug games easily
as Godot will print errors with a stack trace, even if they come from the engine itself.

Note this does not affect the work you do with Godot in any way: there’s
no strings attached to the engine or anything you make with it.

Community-driven
----------------

**Godot is made by its community, for the community and all game
creators out there**. It’s the needs of the users and open discussions
that drive the core updates. New features from the core developers often
focus on what will benefit the most users first.

That said, although a handful of core developers work on it full-time,
the project has over 500 contributors at the time of writing. Benevolent
programmers work on features they may need themselves so you’ll see
improvements in all corners of the engine at the same time in every
major release.

The Godot editor is a Godot game
--------------------------------

The Godot editor runs on the game engine. It uses the engine’s own UI
system, it can hot reload code and scenes when you test your projects,
or run game code in the editor. This means you can **use the same code**
and scenes for your games or **to build plugins and extend the editor**.

This leads to a reliable and flexible UI system as it powers the editor
itself. With the ``tool`` keyword, you can run any game code in the editor.

|image5|

*RPG in a Box is a voxel RPG editor made in Godot 2. It uses Godot’s UI
tools for its node-based programming system and for the rest of the
interface.*

Put the ``tool`` keyword at the top of any GDscript file and it will run
in the editor. This lets you create plugins like custom level editors,
import and export plugins or scripts with the same nodes and API you use
in your projects.


Separate 2d and 3d engines
--------------------------

Godot offers dedicated 2d and 3d rendering engines. As a result **the
base unit for 2d scenes is pixels**. Even though the engines are
separate, you can render 2d in 3d, 3d in 2d, and overlay 2d sprites and
interface over your 3d world.

.. |image0| image:: ./img/engine_design_01.png
.. |image1| image:: ./img/engine_design_02.png
.. |image2| image:: ./img/engine_design_03.png
.. |image3| image:: ./img/engine_design_visual_script.png
.. |image4| image:: ./img/engine_design_fsm_plugin.png
.. |image5| image:: ./img/engine_design_rpg_in_a_box.png
