.. _doc_inverse_kinematics:

Inverse kinematics
==================

This tutorial is a follow-up of :ref:`doc_working_with_3d_skeletons`.

Previously, we were able to control the rotations of bones in order to manipulate
where our arm was (forward kinematics). But what if we wanted to solve this problem
in reverse? Inverse kinematics (IK) tells us *how* to rotate our bones in order to reach
a desired position.

A simple example of IK is the human arm: While we intuitively know the target
position of an object we want to reach for, our brains need to figure out how much to
move each joint in our arm to get to that target.

Initial problem
~~~~~~~~~~~~~~~

Talking in Godot terminology, the task we want to solve here is to position
the 2 angles on the joints of our upperarm and lowerarm so that the tip of the
lowerarm bone is as close to the target point (which is set by the target Vector3)
as possible using only rotations. This task is calculation-intensive and never
resolved by analytical equation solving, as it is an under-constrained
problem which means that there is more than one solution to an
IK problem.

.. image:: img/inverse_kinematics.png

For easy calculation in this chapter, we consider the target being a
child of Skeleton. If this is not the case for your setup you can always
reparent it in your script, as you will save on calculations if you
do so.

In the picture, you see the angles alpha and beta. In this case, we don't
use poles and constraints, so we need to add our own. On the picture
the angles are 2D angles living in a plane which is defined by bone
base, bone tip, and target.

The rotation axis is easily calculated using the cross-product of the bone
vector and the target vector. The rotation in this case will be always in
positive direction. If ``t`` is the Transform which we get from the
get_bone_global_pose() function, the bone vector is

::

    t.basis[2]

So we have all the information we need to execute our algorithm.

In game dev it is common to resolve this problem by iteratively closing
to the desired location, adding/subtracting small numbers to the angles
until the distance change achieved is less than some small error value.
Sounds easy enough, but there are still Godot problems we need to resolve
to achieve our goal.

-  **How to find coordinates of the tip of the bone?**
-  **How to find the vector from the bone base to the target?**

For our goal (tip of the bone moved within area of target), we need to know
where the tip of our IK bone is. As we don't use a leaf bone as IK bone, we
know the coordinate of the bone base is the tip of the parent bone. All these
calculations are quite dependent on the skeleton's structure. You could use
pre-calculated constants, or you could add an extra bone at the tip of the
IK bone and calculate using that.

Implementation
~~~~~~~~~~~~~~

We will use an exported variable for the bone length to make it easy.

::

    export var ik_bone = "lowerarm"
    export var ik_bone_length = 1.0
    export var ik_error = 0.1

Now, we need to apply our transformations from the IK bone to the base of
the chain, so we apply a rotation to the IK bone, then move from our IK bone up to
its parent, apply rotation again, then move to the parent of the
current bone again, etc. So we need to limit our chain somewhat.

::

    export var ik_limit = 2

For the ``_ready()`` function:

::

    var skel
    func _ready():
        skel = get_node("arm/Armature/Skeleton")
        set_process(true)

Now we can write our chain-passing function:

::

    func pass_chain():
        var b = skel.find_bone(ik_bone)
        var l = ik_limit
        while b >= 0 and l > 0:
            print( "name":", skel.get_bone_name(b))
            print( "local transform":", skel.get_bone_pose(b))
            print( "global transform":", skel.get_bone_global_pose(b))
            b = skel.get_bone_parent(b)
            l = l - 1

And for the ``_process()`` function:

::

    func _process(delta):
        pass_chain(delta)

Executing this script will pass through the bone chain, printing bone
transforms.

::

    extends Spatial

    export var ik_bone = "lowerarm"
    export var ik_bone_length = 1.0
    export var ik_error = 0.1
    export var ik_limit = 2
    var skel

    func _ready():
        skel = get_node("arm/Armature/Skeleton")
        set_process(true)

    func pass_chain(delta):
        var b = skel.find_bone(ik_bone)
        var l = ik_limit
        while b >= 0 and l > 0:
            print("name: ", skel.get_bone_name(b))
            print("local transform: ", skel.get_bone_pose(b))
            print( "global transform:", skel.get_bone_global_pose(b))
            b = skel.get_bone_parent(b)
            l = l - 1

    func _process(delta):
        pass_chain(delta)

Now we need to actually work with the target. The target should be placed
somewhere accessible. Since "arm" is an imported scene, we better place
the target node within our top level scene. But for us to work with target
easily its Transform should be on the same level as the Skeleton.

To cope with this problem, we create a "target" node under our scene root
node and at runtime we will reparent it, copying the global transform
which will achieve the desired effect.

Create a new Spatial node under the root node and rename it to "target".
Then modify the ``_ready()`` function to look like this:

::

    var skel
    var target

    func _ready():
        skel = get_node("arm/Armature/Skeleton")
        target = get_node("target")
        var ttrans = target.get_global_transform()
        remove_child(target)
        skel.add_child(target)
        target.set_global_transform(ttrans)
        set_process(true)
