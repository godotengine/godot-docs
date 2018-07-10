Animation
=========

Supported Animation
-------------------
 - transform animation of all types of object
 - transform animation of pose bone

Action Lib
----------
Every action in object's nla tracks would be exported as
a separate track and placed in AnimationPlayer.

Placing of AnimationPlayer
---------------------------
Godot and Blender have different structure to store animation data.
In Godot animation data is stored in an AnimationPlayer node, instead
of in each animated node.

The exporter has an option :code:`Separate AnimationPlayer For Each Object`
which controls how the exported AnimationPlayers are placed.

.. note::
    If :code:`Separate AnimationPlayer For Each Object` is **disabled**
    children of any animated object shares one AnimationPlayer

In the following case, animation data of Mesh is also exported to
AnimationPlayer "RigAnimation"

.. image:: img/animation_non_sep.jpg


.. note::
    If :code:`Separate AnimationPlayer For Each Object` is **enabled**
    every animated object got its own AnimationPlayer. It is useful when
    artists want to play multiple animation concurrently, because one
    AnimationPlayer node can only play one track at a time.

In the following case, Mesh and Rig have their own AnimationPlayer

.. image:: img/animation_sep.jpg
