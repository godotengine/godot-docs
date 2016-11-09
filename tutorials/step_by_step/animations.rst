.. _doc_animations:

Animations
==========

Introduction
------------

This tutorial will explain how everything is animated in Godot. Godot's
animation system is extremely powerful and flexible.

To begin, let's just use the scene from the previous tutorial (:ref:`doc_splash_screen`).
The goal will be to add a simple animation to it. Here's a copy
just in case: :download:`robisplash.zip </files/robisplash.zip>`.

Creating the animation
----------------------

First of all, add an :ref:`AnimationPlayer <class_AnimationPlayer>`
node to the scene as a child of bg (the root node):

.. image:: /img/animplayer.png

When a node of this type is selected, the animation editor panel will
appear:

.. image:: /img/animpanel.png

So, it's time to create a new animation! Press the new animation button
and name the animation "intro".

.. image:: /img/animnew.png

After the animation has been created, then it's time to edit it, by
pressing the "edit" button:

.. image:: /img/animedit.png

Editing the animation
---------------------

Now this is when the magic happens! Several things happen when the
"edit" button is pressed, the first one is that the animation editor
appears above the animation panel. (In Godot 2.x, this button has been
removed, instead, click on the 'animation' toggle at the bottom right 
for similar functionality.)

.. image:: /img/animeditor.png

But the second, and most important, is that the property editor enters
into "animation editing" mode. In this mode, a key icon appears next to
every property of the property editor. This means that, in Godot, *any
property of any object* can be animated:

.. image:: /img/propertykeys.png

Making the logo appear
----------------------

Next, the logo will appear from the top of the screen. After selecting
the animation player, the editor panel will stay visible until
manually hidden (or the animation node is erased). Taking advantage of
this, select the "logo" node and go to the "pos" property, move it up,
to position: 114,-400.

Once in this position, press the key button next to the property:

.. image:: /img/keypress.png

As the track is new, a dialog will appear asking to create it. Confirm
it!

.. image:: /img/addtrack.png

And the keyframe will be added in the animation player editor:

.. image:: /img/keyadded.png

Second, move the editor cursor to the end, by clicking here:

.. image:: /img/move_cursor.png

Change the logo position to 114,0 and add a keyframe again. With two
keyframes, the animation happens.

.. image:: /img/animation.png

Pressing Play on the animation panel will make the logo descend. To test
it by running the scene, the autoplay button can tag the animation to
start automatically when the scene starts:

.. image:: /img/autoplay.png

And finally, when running the scene, the animation should look like
this:

.. image:: /img/out.gif
