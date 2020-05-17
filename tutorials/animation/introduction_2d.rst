.. _doc_introduction_2d_animation:

Introduction to the 2D animation features
=========================================

Overview
--------

The :ref:`class_AnimationPlayer` node allows you to create anything
from simple to complex animations.

In this guide you learn to:

-  Work with the Animation Panel
-  Animate any property of any node
-  Create a simple animation
-  Call functions with the powerful Call Function Tracks

In Godot, you can animate anything available in the Inspector, such as
Node transforms, sprites, UI elements, particles, visibility and color
of materials, and so on. You can also modify values of script variables
and call any function.

Create an AnimationPlayer node
------------------------------

To use the animation tools we first have to create an
:ref:`class_AnimationPlayer` node.

The AnimationPlayer node type is the data container for your animations.
One AnimationPlayer node can hold multiple animations, that can
automatically transition to one another.

.. figure:: img/animation_create_animationplayer.png
   :alt: The AnimationPlayer node

   The AnimationPlayer node

After creating one click on the AnimationPlayer node in the Node tab to
open the Animation Panel at the bottom of the viewport.

.. figure:: img/animation_animation_panel.png
   :alt: The animation panel position

   The animation panel position

It consists of four parts:

.. figure:: img/animation_animation_panel_overview.png
   :alt: The animation panel

   The animation panel

-  Animation controls (i.e. add, load, save, and delete animations)
-  The tracks listing
-  The timeline with keyframes
-  The timeline and track controls, where you can zoom the timeline and
   edit tracks for example.

Computer animation relies on keyframes
--------------------------------------

A keyframe defines the value of a property at a certain point in time.

Diamond shapes represent keyframes in the timeline. A line between two
keyframes indicates that the value hasn't changed.

.. figure:: img/animation_keyframes.png
   :alt: Keyframes in Godot

   Keyframes in Godot

The engine interpolates values between keyframes, resulting in a gradual
change in values over time.

.. figure:: img/animation_illustration.png
   :alt: Two keyframes are all it takes to obtain a smooth motion

   Two keyframes are all it takes to obtain a smooth motion

The timeline lets you insert keyframes and change their timing. It also
defines how long the animation is.

.. figure:: img/animation_timeline.png
   :alt: The timeline in the animation panel

   The timeline in the animation panel

Each line of the Animation Panel is an animation track. Normal and
Transform tracks reference node properties. Their name or id is a path
to the node and the affected property.

.. figure:: img/animation_normal_track.png
   :alt: Example of Normal animation tracks

   Example of Normal animation tracks

.. tip::

   If you animate the wrong property, you can edit a track's path anytime.
   Double click on it and type the new path. Play the animation using the
   "Play from beginning" button |Play from beginning| (or pressing
   :kbd:`Shift + D` on keyboard) to see the changes instantly.

Tutorial: Creating a simple animation
-------------------------------------

Scene setup
~~~~~~~~~~~

For this tutorial, we'll create an AnimationPlayer node and a sprite node as its
child.

.. figure:: img/animation_animation_player_tree.png
   :alt: Our scene setup

   Our scene setup

The sprite holds an image texture. We animate that sprite to move
between two points on the screen. For this tutorial, use the default Godot
icon as the sprite's texture. As a starting point, move the sprite
to a left position on the screen.

.. tip::

   Adding animated nodes as children to the AnimationPlayer node is not
   required, but it is a nice way of distinguishing animated nodes from
   non-animated nodes in the Scene Tree.

Select the AnimationPlayer node, then click the "Animation" button in the
animation editor. From the list select "New" (|Add
Animation|) to add a new animation. And Enter a name for the animation in the
dialog box.

.. figure:: img/animation_create_new_animation.png
   :alt: Add a new animation

   Add a new animation

Adding a track
~~~~~~~~~~~~~~

To add a new track for our sprite, select it and take a look in the
toolbar:

.. figure:: img/animation_convenience_buttons.png
   :alt: Convenience buttons

   Convenience buttons

These switches and buttons allow you to add keyframes for the selected
node's location, rotation, and scale respectively.

Deselect rotation, because we are only interested in the location of our
sprite for this tutorial and click on the key button.

As we don't have a track already set up for the transform/location
property, Godot asks whether it should set it up for us. Click **Create**.

This creates a new track and our first keyframe at the beginning of
the timeline:

.. figure:: img/animation_track.png
   :alt: The sprite track

   The sprite track

The second keyframe
~~~~~~~~~~~~~~~~~~~

Now we need to set the destination where our sprite should be headed and
how much time it takes to get there.

Let's say, we want it to take 2 seconds to go to the other point. By
default the animation is set to last only 1 second, so change this in
the timeline controls in animation panel's lower panel to 2.

.. figure:: img/animation_set_length.png
   :alt: Animation length

   Animation length

Click on the timeline header near the 2-second mark and move the sprite
to the target destination on the right side.

Again, click the key button in the toolbar. This creates our second
keyframe.

Run the animation
~~~~~~~~~~~~~~~~~

Click on the "Play from beginning" (|Play from beginning|) button.

Yay! Our animation runs:

.. figure:: img/animation_simple.gif
   :alt: The animation

   The animation

Back and forth
~~~~~~~~~~~~~~

Godot has an additional feature here. Like said before,
Godot always calculates the frames between two keyframes. In a loop, the
first keyframe is also the last keyframe, if no keyframe is specified at
the end.

.. figure:: img/animation_loop.png
   :alt: Animation loop

   Animation loop

If you set the animation length to 4 seconds now, the animation moves
back and forth. You can change this behavior if you change the track's
loop mode. This is covered in the next chapter.

Track settings
~~~~~~~~~~~~~~

Each track has a settings panel at the end, where you can set the update
mode, the track interpolation, and the loop mode.

.. figure:: img/animation_track_settings.png
   :alt: Track settings

   Track settings

The update mode of a track tells Godot when to update the property
values. This can be:

-  Continuous: Update the property on each frame
-  Discrete: Only update the property on keyframes
-  Trigger: Only update the property on keyframes or triggers
-  Capture: The current value of a property is remembered, and it will blend with the first animation key found

.. figure:: img/animation_track_rate.png
   :alt: Track mode

   Track mode

In normal animations, you usually use "Continuous". The other types are
used to script complex animations.

The interpolation tells Godot how to calculate the frame values between
the keyframes. These interpolation modes are supported:

-  Nearest: Set the nearest keyframe value
-  Linear: Set the value based on a linear function calculation between
   the two keyframes
-  Cubic: Set the value based on a cubic function calculation between
   the two keyframes

.. figure:: img/animation_track_interpolation.png
   :alt: Track interpolation

   Track interpolation

Cubic interpolation leads to a more natural movement, where the
animation is slower at a keyframe and faster between keyframes. This is
usually used for character animation. Linear interpolation creates more
of a robotic movement.

Godot supports two loop modes, which affect the animation if it's set to
loop:

.. figure:: img/animation_track_loop_modes.png
   :alt: Loop modes

   Loop modes

-  Clamp loop interpolation: When this is selected, the animation stops
   after the last keyframe for this track. When the first keyframe is
   reached again, the animation will reset to its values.
-  Wrap loop interpolation: When this is selected, Godot calculates the
   animation after the last keyframe to reach the values of the first
   keyframe again.

Keyframes for other properties
------------------------------

Godot doesn't restrict you to only edit transform properties. Every
property can be used as a track where you can set keyframes.

If you select your sprite while the animation panel is visible, you get
a small keyframe button for all the sprite's properties. Click on
this button and Godot automatically adds a track and keyframe to the
current animation.

.. figure:: img/animation_properties_keyframe.png
   :alt: Keyframes for other properties

   Keyframes for other properties

Edit keyframes
--------------

For advanced use and to edit keyframes in detail, You can click on them
to bring up the keyframe editor in the inspector. You can use this to
directly edit its values.

.. figure:: img/animation_keyframe_editor_key.png
   :alt: Keyframe editor editing a key

   Keyframe editor editing a key

Additionally, you can also edit the easing value for this keyframe by
clicking and dragging the easing setting. This tells Godot, how to change
the property values when it reaches this keyframe.

You usually tweak your animations this way, when the movement doesn't
"look right".

Advanced: Call Method tracks
----------------------------

Godot's animation engine doesn't stop here. If you're already
comfortable with Godot's scripting language
:ref:`doc_gdscript` and :doc:`/classes/index` you
know that each node type is a class and has a bunch of callable
methods.

For example, the :ref:`class_AudioStreamPlayer` node type has a
method to play an audio stream.

Wouldn't it be great to use a method at a specific keyframe in an
animation? This is where "Call Method Tracks" come in handy. These tracks
reference a node again, this time without a reference to a property.
Instead, a keyframe holds the name and arguments of a method, that
Godot should call when it reaches this keyframe.

To demonstrate, we're going to use a call method track to play audio at a
specific keyframe. Normally to play audio you should use an audio track,
but for the sake of demonstrating methods we're going to do it this way.

Add a :ref:`class_AudioStreamPlayer` to the Scene Tree and setup a
stream using an audio file you put in your project.

Click on "Add track" (|Add track|) on the animation panel's track
controls.

Select "Add Call Method Track" from the list of possible track types.

.. figure:: img/animation_add_call_method_track.png
   :alt: Add Call Method Track

   Add Call Method Track

Select the :ref:`class_AudioStreamPlayer` node in the selection
window. Godot adds the track with the reference to the node.

.. figure:: img/animation_select_audiostreamplayer.png
   :alt: Select AudioStreamPlayer

   Select AudioStreamPlayer

Right click the timeline where Godot should play the sample and
click the "Insert Key" option. This will bring up a list of methods
that can be called for the AudioStreamPlayer node. Select the first
one.

.. image:: img/animation_method_options.png

When Godot reaches the keyframe, Godot calls the
:ref:`class_AudioStreamPlayer` node's "play" function and the stream
plays.

You can change its position by dragging it on the timeline, you can also
click on the keyframe and use the keyframe settings in the inspector.

.. image:: img/animation_call_method_keyframe.png

.. |Play from beginning| image:: img/animation_play_from_beginning.png
.. |Add Animation| image:: img/animation_add.png
.. |Add track| image:: img/animation_add_track.png
