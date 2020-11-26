.. _doc_animation_track_types:

Animation Track types
=====================

This page gives an overview of the track types available for Godot's animation
player node on top of the default property tracks.

.. seealso::

   We assume you already read :ref:`doc_introduction_animation`, which covers
   the basics, including property tracks.

.. image:: img/track_types.png


3D Transform Track
------------------

3D transform tracks control the location, rotation, and scale of a 3D object.
They make it easier to animate a 3D object's transform compared to using regular
property tracks.

.. image:: img/3D_transform_track.png

Call Method tracks
------------------

Call method tracks allow you to call a function at a precise time from within an
animation. For example, you can call ``queue_free()`` to delete a node at the
end of a death animation.

To create such a track, click "Add Track -> Call Method Track." Then, a window
opens and lets you select the node to associate with the track. To call one of
the node's methods, right-click the timeline and select "Insert Key". A window
opens with a list of available methods. Double-click one to finish creating the
keyframe.

.. image:: img/node_methods.png

To change the method call or its arguments, click on the key and head to the
inspector dock. There, you can change the method to call. If you expand the
"Args" section, you will see a list of arguments you can edit.

.. image:: img/node_method_args.png

Bezier Curve Track
------------------

A bezier curve track is similar to a property track, except it allows you to
animate a property's value using a bezier curve.

To create one, click "Add Track -> Bezier Curve Track". As with property tracks,
you need to select a node and a property to animate. To open the bezier curve
editor, click the curve icon to the right of the animation track.

.. image:: img/bezier_curve_icon.png

In the editor, keys are represented by white diamonds and the transparent
diamonds connected to them by a line control curve's shape.

.. image:: img/bezier_curves.png

In the bottom-right of the editor, you can select the manipulator mode:

- Free allows you to orient a manipulator in any direction without affecting the
  other's position.
- Balanced makes it so manipulators rotate together, but the distance between
  the key and a manipulator is not mirrored.
- Mirror makes the position of one manipulator perfectly mirror the other,
  including their distance to the key.

.. image:: img/manipulator_modes.png

Audio Playback Track
--------------------

If you want to create an animation with audio, you need to create an audio
playback track. To create one, your scene must have either an AudioStreamPlayer,
AudioStreamPlayer2D, or AudioStreamPlayer3D node. When creating the track, you
must select one of those nodes.

To play a sound in your animation, drag and drop an audio file from the file
system dock onto the animation track. You should see the waveform of your audio
file in the track.

.. image:: img/audio_track.png

To remove a sound from the animation, you can right-click it and select "Delete
Key(s)" or click on it and press the :kbd:`Del` key.

.. note:: If you need to, you can create multiple audio tracks that trigger
          playback on the same node.

Animation Playback Track
------------------------

Animation playback tracks allow you to sequence the animations of other
animation player nodes in a scene. For example, you can use it to animate
several characters in a cut-scene.

To create an animation playback track, select "New Track -> Animation Playback
Track."

Then, select the animation player you want to associate with the track.

To add an animation to the track, right-click on it and insert a key. Select the
key you just created to select an animation in the inspector dock.

.. image:: img/animation_player_animation.png

If an animation is already playing and you want to stop it early, you can create
a key and have it set to `[STOP]` in the inspector.

.. note:: If you instanced a scene that contains an animation player into your
          scene, you need to enable "Editable Children" in the scene tree to
          access its animation player. Also, an animation player cannot
          reference itself.

.. questions-answers:: animation track
