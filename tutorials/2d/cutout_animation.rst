.. _doc_cutout_animation:

Cutout animation
================

What is it?
~~~~~~~~~~~

Cut-out is a technique of animating in 2D where pieces of paper (or
similar material) are cut in special shapes and laid one over the other.
The papers are animated and photographed, frame by frame using a stop
motion technique (more info
`here <http://en.wikipedia.org/wiki/Cutout_animation>`__).

With the advent of the digital age, this technique became possible using
computers, which resulted in an increased amount of animation TV shows
using digital Cut-out. Notable examples are `South
Park <http://en.wikipedia.org/wiki/South_Park>`__ or `Jake and the Never
Land
Pirates <http://en.wikipedia.org/wiki/Jake_and_the_Never_Land_Pirates>`__
.

In video games, this technique also become very popular. Examples of
this are `Paper
Mario <http://en.wikipedia.org/wiki/Super_Paper_Mario>`__ or `Rayman
Origins <http://en.wikipedia.org/wiki/Rayman_Origins>`__ .

Cutout in Godot
~~~~~~~~~~~~~~~

Godot provides a few tools for working with these kind of assets, but
it's overall design makes it ideal for the workflow. The reason is that,
unlike other tools meant for this, Godot has the following advantages:

-  **The animation system is fully integrated with the engine**: This
   means, animations can control much more than just motion of objects,
   such as textures, sprite sizes, pivots, opacity, color modulation,
   etc. Everything can be animated and blended.
-  **Mix with Traditional**: AnimatedSprite allows traditional animation
   to be mixed, very useful for complex objects, such as shape of hands
   and foot, changing facial expression, etc.
-  **Custom Shaped Elements**: Can be created with
   :ref:`Polygon2D <class_Polygon2D>`
   allowing the mixing of UV animation, deformations, etc.
-  **Particle Systems**: Can also be mixed with the traditional
   animation hierarchy, useful for magic effects, jetpacks, etc.
-  **Custom Colliders**: Set colliders and influence areas in different
   parts of the skeletons, great for bosses, fighting games, etc.
-  **Animation Tree**: Allows complex combinations and blendings of
   several animations, the same way it works in 3D.

And much more!

Making of GBot!
~~~~~~~~~~~~~~~

For this tutorial, we will use as demo content the pieces of the
`GBot <https://www.youtube.com/watch?v=S13FrWuBMx4&list=UUckpus81gNin1aV8WSffRKw>`__
character, created by Andreas Esau.

.. image:: /img/tuto_cutout_walk.gif

Get your assets: :download:`gbot_resources.zip </files/gbot_resources.zip>`.

Setting up the rig
~~~~~~~~~~~~~~~~~~

Create an empty Node2D as root of the scene, we will work under it:

.. image:: /img/tuto_cutout1.png

OK, the first node of the model that we will create will be the hip.
Generally, both in 2D and 3D, the hip is the root of the skeleton. This
makes it easier to animate:

.. image:: /img/tuto_cutout2.png

Next will be the torso. The torso needs to be a child of the hip, so
create a child sprite and load the torso, later accommodate it properly:

.. image:: /img/tuto_cutout3.png

This looks good. Let's see if our hierarchy works as a skeleton by
rotating the torso:

.. image:: /img/tutovec_torso1.gif

Ouch, that doesn't look good! The rotation pivot is wrong, this means
it needs to be adjusted.

This small little cross in the middle of the
:ref:`Sprite <class_Sprite>` is
the rotation pivot:

.. image:: /img/tuto_cutout4.png

Adjusting the pivot
~~~~~~~~~~~~~~~~~~~

The pivot can be adjusted by changing the *offset* property in the
Sprite:

.. image:: /img/tuto_cutout5.png

However, there is a way to do it more *visually*. While hovering over the
desired pivot point, simply press the "v" key to move the pivot there for the
selected Sprite. Alternately, there is a tool in the tool bar that has a
similar function.

.. image:: /img/tutovec_torso2.gif

Now it looks good! Let's continue adding body pieces, starting by the
right arm. Make sure to put the sprites in hierarchy, so their rotations
and translations are relative to the parent:

.. image:: /img/tuto_cutout6.png

This seems easy, so continue with the right arm. The rest should be
simple! Or maybe not:

.. image:: /img/tuto_cutout7.png

Right. Remember your tutorials, Luke. In 2D, parent nodes appear below
children nodes. Well, this sucks. It seems Godot does not support cutout
rigs after all. Come back next year, maybe for 3.0.. no wait. Just
Kidding! It works just fine.

But how can this problem be solved? We want the left arm to appear behind
the hip and the torso. For this, we can move the nodes behind the hip
(note that you can bypass this by setting the Node2D Z property, but then you
won't learn about all this!):

.. image:: /img/tuto_cutout8.png

But then, we lose the hierarchy layout, which allows to control the
skeleton like.. a skeleton. Is there any hope?.. Of Course!

RemoteTransform2D node
~~~~~~~~~~~~~~~~~~~~~~

Godot provides a special node, :ref:`RemoteTransform2D <class_RemoteTransform2D>`.
This node will transform nodes that are sitting somewhere else in the
hierarchy, by applying the transform to the remote nodes.

This enables to have a visibility order independent from the
hierarchy.

Simply create two more nodes as children from torso, remote_arm_l and
remote_hand_l and link them to the actual sprites:

.. image:: /img/tuto_cutout9.png

Moving the remote transform nodes will move the sprites, allowing you to
easily animate and pose the character:

.. image:: /img/tutovec_torso4.gif

Completing the skeleton
~~~~~~~~~~~~~~~~~~~~~~~

Complete the skeleton by following the same steps for the rest of the
parts. The resulting scene should look similar to this:

.. image:: /img/tuto_cutout10.png

The resulting rig will be easy to animate. By selecting the nodes and
rotating them you can animate forward kinematics (FK) efficiently.

For simple objects and rigs this is fine, however the following problems
are common:

-  Selecting sprites can become difficult for complex rigs, and the
   scene tree ends being used due to the difficulty of clicking over the
   proper sprite.
-  Inverse Kinematics is often desired for extremities.

To solve these problems, Godot supports a simple method of skeletons.

Skeletons
~~~~~~~~~

Godot doesn't actually support *true* Skeketons, but it does feature a
helper to create "bones" between nodes. This is enough for most cases, 
but the way it works is not completely obvious.



As an example, let's turn the right arm into a skeleton. To create
skeletons, a chain of nodes must be selected from top to bottom:

.. image:: /img/tuto_cutout11.png

Then, the option to create a skeleton is located at Edit > Make Bones:

.. image:: /img/tuto_cutout12.png

This will add bones covering the arm, but the result is not quite what
is expected.

.. image:: /img/tuto_cutout13.png

It looks like the bones are shifted up in the hierarchy. The hand
connects to the arm, and the arm to the body. So the question is:

-  Why does the hand lack a bone?
-  Why does the arm connect to the body?

This might seem strange at first, but will make sense later on. In
traditional skeleton systems, bones have a position, an orientation and
a length. In Godot, bones are mostly helpers so they connect the current
node with the parent. Because of this, **toggling a node as a bone will
just connect it to the parent**.

So, with this knowledge. Let's do the same again so we have an actual,
useful skeleton.

The first step is creating an endpoint node. Any kind of node will do,
but :ref:`Position2D <class_Position2D>` is preferred because it's
visible in the editor. The endpoint node will ensure that the last bone
has orientation.

.. image:: /img/tuto_cutout14.png

Now select the whole chain, from the endpoint to the arm and create
bones:

.. image:: /img/tuto_cutout15.png

The result resembles a skeleton a lot more, and now the arm and forearm
can be selected and animated.

Finally, create endpoints in all meaningful extremities and connect the
whole skeleton with bones up to the hip:

.. image:: /img/tuto_cutout16.png

Finally! the whole skeleton is rigged! On close look, it is noticeable
that there is a second set of endpoints in the hands. This will make
sense soon.

Now that a whole skeleton is rigged, the next step is setting up the IK
chains. IK chains allow for more natural control of extremities.

IK chains
~~~~~~~~~

IK chains are a powerful animation tool. Imagine you want to pose a character's foot in a specific position on the ground. Without IK chains, each motion of the foot would require rotating and positioning several other bones. This would be quite complex and lead to imprecise results.

What if we could move the foot and let the rest of the leg self-adjust?

This type of posing is called IK (Inverse Kinematic).

To create an IK chain, simply select a chain of bones from endpoint to
the base for the chain. For example, to create an IK chain for the right
leg, select the following:

.. image:: /img/tuto_cutout17.png

Then enable this chain for IK. Go to Edit > Make IK Chain.

.. image:: /img/tuto_cutout18.png

As a result, the base of the chain will turn *Yellow*.

.. image:: /img/tuto_cutout19.png

Once the IK chain is set-up, simply grab any of the bones in the
extremity, any child or grand-child of the base of the chain and try to
grab it and move it. Result will be pleasant, satisfaction warranted!

.. image:: /img/tutovec_torso5.gif

Animation
~~~~~~~~~

The following section will be a collection of tips for creating
animation for your rigs. If unsure about how the animation system in
Godot works, refresh it by checking again the :ref:`doc_animations`.

2D animation
------------

When doing animation in 2D, a helper will be present in the top menu.
This helper only appears when the animation editor window is opened:

.. image:: /img/tuto_cutout20.png

The key button will insert location/rotation/scale keyframes to the
selected objects or bones. This depends on the mask enabled. Green items
will insert keys while red ones will not, so modify the key insertion
mask to your preference.

Rest pose
~~~~~~~~~

These kind of rigs do not have a "rest" pose, so it's recommended to
create a reference rest pose in one of the animations.

Simply do the following steps:

1. Make sure the rig is in "rest" (not doing any specific pose).

2. Create a new animation, rename it to "rest".

3. Select all nodes (box selection should work fine).

4. Select "loc" and "rot" on the top menu.

5. Push the key button. Keys will be inserted for everything, creating
a default pose.

.. image:: /img/tuto_cutout21.png

Rotation
~~~~~~~~

Animating these models means only modifying the rotation of the nodes.
Location and scale are rarely used, with the only exception of moving
the entire rig from the hip (which is the root node).

As a result, when inserting keys, only the "rot" button needs to be
pressed most of the time:

.. image:: /img/tuto_cutout22.png

This will avoid the creation of extra animation tracks for the position
that will remain unused.

Keyframing IK
~~~~~~~~~~~~~

When editing IK chains, is is not necessary to select the whole chain to
add keyframes. Selecting the endpoint of the chain and inserting a
keyframe will automatically insert keyframes until the chain base too.
This makes the task of animating extremities much simpler.

Moving sprites above and behind others.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

RemoteTransform2D works in most cases, but sometimes it is really
necessary to have a node above and below others during an animation. To
aid on this the "Behind Parent" property exists on any Node2D:

.. image:: /img/tuto_cutout23.png

Batch setting transition curves
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When creating really complex animations and inserting lots of keyframes,
editing the individual keyframe curves for each can become an endless
task. For this, the Animation Editor has a small menu where changing all
the curves is easy. Just select every single keyframe and (generally)
apply the "Out-In" transition curve to smooth the animation:

.. image:: /img/tuto_cutout24.png
