:allow_comments: False

.. _doc_your_first_2d_game:

Your first 2D game
==================

In this step-by-step tutorial series, you will create your first complete 2D
game with Godot. By the end of the series, you will have a simple yet complete
game of your own, like the image below.

|image0|

You will learn how the Godot editor works, how to structure a project, and build
a 2D game.

.. note:: This project is an introduction to the Godot engine. It assumes that
          you have some programming experience already. If you're new to
          programming entirely, you should start here: :ref:`doc_scripting`.

The game is called "Dodge the Creeps!". Your character must move and avoid the
enemies for as long as possible.

You will learn to:

- Create a complete 2D game with the Godot editor.
- Structure a simple game project.
- Move the player character and change its sprite.
- Spawn random enemies.
- Count the score.

And more.

You'll find another series where you'll create a similar game but in 3D. We
recommend you to start with this one, though.

**Why start with 2D?**

If you are new to game development or unfamiliar with Godot, we recommend
starting with 2D games. This will allow you to become comfortable with both
before tackling 3D games, which tend to be more complicated.

You can find a completed version of this project at this location:

- https://github.com/godotengine/godot-demo-projects/tree/master/2d/dodge_the_creeps

Prerequisites
-------------

This step-by-step tutorial is intended for beginners who followed the complete
:ref:`Getting Started <toc-learn-step_by_step>`.

If you're an experienced programmer, you can find the complete demo's source
code here: `Dodge the Creeps source code
<https://github.com/godotengine/godot-demo-projects/tree/master/2d/dodge_the_creeps>`__.

We prepared some game assets you'll need to download so we can jump straight to
the code.

You can download them by clicking the link below.

`dodge_the_creeps_2d_assets.zip <https://github.com/godotengine/godot-docs-project-starters/releases/download/latest-4.x/dodge_the_creeps_2d_assets.zip>`_.

Contents
--------

.. toctree::
   :maxdepth: 1
   :name: toc-learn-first_2d_game

   01.project_setup
   02.player_scene
   03.coding_the_player
   04.creating_the_enemy
   05.the_main_game_scene
   06.heads_up_display
   07.finishing-up

.. |image0| image:: img/dodge_preview.gif
