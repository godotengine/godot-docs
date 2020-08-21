.. _doc_animation_track_types:

Animation Track types
=====================

Overview
--------

This page goes over the different track types in Godot's animation player
node.

.. image:: img/track_types.png

This page will assume you have already read :ref:`doc_introduction_2d_animation`,
or have basic knowledge of animation in Godot. Property tracks will not be
explained here.

3D Transform Track
------------------

3D transform tracks have a very specific use. They are used exclusively to
adjust the location, rotation and scale of a 3D object. This exists because
adjusting those properties with a property track would be cumbersome.

.. image:: img/3D_transform_track.png

Call Method tracks
------------------

Call method tracks allow you to use the method of a node while an animation
is playing. For example deleting a node after a death animation.

To create one click "Add Track" and then "Call Method Track." Then select
the node whose method you want to call during the animation. To call the
method right click the timeline and select "Insert Key," this will bring
up a list of every method in that node.

.. image:: img/node_methods.png

Selecting the key on the timeline will bring up the animation track key
editor in the inspector. If you expand the "Args" tab you will see a
list of arguments the method takes that you can edit.

.. image:: img/node_method_args.png

Bezier Curve Track
------------------

A bezier curve track is a specific type of property track. In a property
track properties are changed at a consistent rate. Bezier curve tracks
allow you to change properties according to a bezier curve.

To create one click "Add Track" and then "Bezier Curve Track." Like a
property track you need to select a node and then a property to animate.
Create some keys and click the curve icon on the right side of the
animation player.

.. image:: img/bezier_curve_icon.png

This should open the bezier curve editor. Keys will be represented
by white diamonds, and the transparent diamonds connected to them are
manipulators that can be moved to manipulate the shape of the curve.

.. image:: img/bezier_curves.png

In the bottom right of the editor you can select the manipulator mode.

.. image:: img/manipulator_modes.png

-  Free: either manipulator of a key can be moved completely without
   affecting the position of the other.
-  Balanced: The position of one manipulator perfectly mirrors the other.
   But the distance of the manipulator from the key is not mirrored.
-  Mirror: The position of one manipulator perfectly mirrors the other.
   Including the distance of the manipulator from the key.

Audio Playback Track
--------------------

If you want to create an animation with audio you need to use an audio
playback track. Before you create one your scene must have either a
AudioStreamPlayer, AudioStreamPlayer2D, or AudioStreamPlayer3D node. When
creating the track you must select one of those nodes.

If you need to you can create multiple audio tracks using the same node.
To add an audio file to your audio playback track, find the file you want
in the file system panel, then drag and drop it onto the audio playback
track in the animation player. After that you should see the waveform
of your audio file in the track.

.. image:: img/audio_track.png

To delete an audio file from your audio playback track, select it in the
track and press your delete key, or right click it and select "Delete
Key(s)"

Animation Playback Track
------------------------

Animation playback tracks are used to access the animations of other
animation player nodes in a scene. For example you may have several
characters in a scene for a cutscene, and want to use their own animations
for the cutscene.

To create one select "New Track" and "Animation Playback Track." You then
need to select the animation player you want to access. If you have a instanced
scene where the animation player of that scene is not the root node, you need
to enable "Editable Children" in the scene tree to access that animation player.
And an animation player cannot access itself.

To play an animation right click the timeline and insert a key. Select the
key you just created to open animation track key edit in the inspector. From
there you can select the specific animation you want to paly.

.. image:: img/animation_player_animation.png

If an animation is already playing and you want to stop it early, you can create
a key and have it set to `[STOP]` under animation. The current animation will then
stop when it hits that key.
