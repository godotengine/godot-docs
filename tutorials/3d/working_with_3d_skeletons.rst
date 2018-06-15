.. _doc_working_with_3d_skeletons:

Working with 3D skeletons
=========================

Godot 3D skeleton support is currently quite rudimentary. The
:ref:`class_Skeleton` node and class were designed mainly to support importing
skeletal animations as a set of transformation matrices.

Skeleton node
-------------

The Skeleton node can be directly added anywhere you want on a scene. Usually
the target mesh is a child of Skeleton, as it easier to manipulate this way, since
Transforms within a skeleton are relative to where the Skeleton is. But you
can specify a Skeleton node in every MeshInstance.

Naturally, Skeleton is intended to deform meshes and consists of
structures called "bones". Each "bone" is represented as a Transform, which is
applied to a group of vertices within a mesh. You can directly control a group
of vertices from Godot. For that please reference the :ref:`class_MeshDataTool`
class and its method :ref:`set_vertex_bones <class_MeshDataTool_set_vertex_bones>`.

The "bones" are organized hierarchically. Every bone, except for root
bone(s) have a parent. Every bone also has an associated name you can use to
refer to it (e.g. "root" or "hand.L", etc.). All bones are numbered, and
these numbers are bone IDs. Bone parents are referred by their numbered
IDs.

For the rest of the article we consider the following scene:

::

    main (Spatial) - script is always here
    == skel (Skeleton)
    ==== mesh (MeshInstance)

This scene is imported from Blender. It contains an arm mesh with 2 bones,
upperarm and lowerarm, with the lowerarm bone parented to the upperarm.

Skeleton class
--------------

You can view Godots internal help for descriptions of all functions.
Basically, all operations on bones are done using their numeric ID. You
can convert from a name to a numeric ID and vice versa.

**To find the number of bones in a skeleton we use the get_bone_count()
function:**

::

    extends Spatial
    var skel

    func _ready():
        skel = get_node("skel")
        var count = skel.get_bone_count()
        print("bone count:", count)

**To find the ID of a bone, use the find_bone() function:**

::

    extends Spatial
    var skel

    func _ready():
        skel = get_node("skel")
        var id = skel.find_bone("upperarm")
        print("bone id:", id)

Now, we want to do something interesting with the ID, not just printing it.
Also, we might need additional information, finding bone parents to
complete chains, etc. This is done with the get/set_bone\_\* functions.

**To find the parent of a bone we use the get_bone_parent(id) function:**

::

    extends Spatial
    var skel

    func _ready():
        skel = get_node("skel")
        var id = skel.find_bone("upperarm")
        print("bone id:", id)
        var parent = skel.get_bone_parent(id)
        print("bone parent id:", id)

The bone transforms are the things of our interest here. There are 3 kind of
transforms: local, global, custom.

**To find the local Transform of a bone we use get_bone_pose(id) function:**

::

    extends Spatial
    var skel

    func _ready():
        skel = get_node("skel")
        var id = skel.find_bone("upperarm")
        print("bone id:", id)
        var parent = skel.get_bone_parent(id)
        print("bone parent id:", id)
        var t = skel.get_bone_pose(id)
        print("bone transform: ", t)

So we get a 3x4 matrix there, with the first column filled with 1s. What can we do
with this matrix? It is a Transform, so we can do everything we can do with
Transforms (basically translate, rotate and scale). We could also multiply
transforms to have more complex transforms. Remember, "bones" in Godot are
just Transforms over a group of vertices. We could also copy Transforms of
other objects there. So let's rotate our "upperarm" bone:

::

    extends Spatial
    var skel
    var id

    func _ready():
        skel = get_node("skel")
        id = skel.find_bone("upperarm")
        print("bone id:", id)
        var parent = skel.get_bone_parent(id)
        print("bone parent id:", id)
        var t = skel.get_bone_pose(id)
        print("bone transform: ", t)
        set_process(true)

    func _process(delta):
        var t = skel.get_bone_pose(id)
        t = t.rotated(Vector3(0.0, 1.0, 0.0), 0.1 * delta)
        skel.set_bone_pose(id, t)

Now we can rotate individual bones. The same happens for scale and
translate. Try these on your own and check the results.

What we used here was the local pose. By default all bones are not modified.
But this Transform tells us nothing about the relationship between bones.
This information is needed for quite a number of tasks. How can we get
it? Here the global transform comes into play:

**To find the bone global Transform we use get_bone_global_pose(id)
function:**

Let's find the global Transform for the lowerarm bone:

::

    extends Spatial
    var skel

    func _ready():
        skel = get_node("skel")
        var id = skel.find_bone("lowerarm")
        print("bone id:", id)
        var parent = skel.get_bone_parent(id)
        print("bone parent id:", id)
        var t = skel.get_bone_global_pose(id)
        print("bone transform: ", t)

As you can see, this transform is not zeroed. While being called global, it
is actually relative to the Skeleton origin. For a root bone, the origin is always
at 0 if not modified. Let's print the origin for our lowerarm bone:

::

    extends Spatial
    var skel

    func _ready():
        skel = get_node("skel")
        var id = skel.find_bone("lowerarm")
        print("bone id:", id)
        var parent = skel.get_bone_parent(id)
        print("bone parent id:", id)
        var t = skel.get_bone_global_pose(id)
        print("bone origin: ", t.origin)

You will see a number. What does this number mean? It is a rotation
point of the Transform. So it is base part of the bone. In Blender you can
go to Pose mode and try there to rotate bones. They will rotate around
their origin.

But what about the bone tip? We can't know things like the bone length,
which we need for many things, without knowing the tip location. For all
bones in a chain, except for the last one, we can calculate the tip location. It is
simply a child bone's origin. There are situations when this is not
true, such as for non-connected bones, but that is OK for us for now, as it is
not important regarding Transforms.

Notice that the leaf bone tip is nowhere to be found. A leaf bone is a bone
without children, so you don't have any information about its tip.
But this is not a showstopper. You can overcome this by either adding an extra
bone to the chain or just calculating the length of the leaf bone in Blender
and storing the value in your script.

Using 3D "bones" for mesh control
---------------------------------

Now as you know the basics we can apply these to make full FK-control of our
arm (FK is forward-kinematics).

To fully control our arm we need the following parameters:

-  Upperarm angle x, y, z
-  Lowerarm angle x, y, z

All of these parameters can be set, incremented, and decremented.

Create the following node tree:

::

    main (Spatial) <- script is here
    +-arm (arm scene)
    + DirectionLight (DirectionLight)
    + Camera

Set up the Camera so that the arm is properly visible. Rotate DirectionLight
so that the arm is properly lit while in scene play mode.

Now we need to create a new script under main:

First we define the setup parameters:

::

    var lowerarm_angle = Vector3()
    var upperarm_angle = Vector3()

Now we need to setup a way to change them. Let us use keys for that.

Please create 7 actions under project settings -> Input Map:

-  **selext_x** - bind to X key
-  **selext_y** - bind to Y key
-  **selext_z** - bind to Z key
-  **select_upperarm** - bind to key 1
-  **select_lowerarm** - bind to key 2
-  **increment** - bind to key numpad +
-  **decrement** - bind to key numpad -

So now we want to adjust the above parameters. Therefore we create code
which does that:

::

    func _ready():
        set_process(true)

    var bone = "upperarm"
    var coordinate = 0

    func _process(delta):
        if Input.is_action_pressed("select_x"):
            coordinate = 0
        elif Input.is_action_pressed("select_y"):
            coordinate = 1
        elif Input.is_action_pressed("select_z"):
            coordinate = 2
        elif Input.is_action_pressed("select_upperarm"):
            bone = "upperarm"
        elif Input.is_action_pressed("select_lowerarm"):
            bone = "lowerarm"
        elif Input.is_action_pressed("increment"):
            if bone == "lowerarm":
                lowerarm_angle[coordinate] += 1
            elif bone == "upperarm":
                upperarm_angle[coordinate] += 1

The full code for arm control is this:

::

    extends Spatial

    # member variables here, example:
    # var a=2
    # var b="textvar"
    var upperarm_angle = Vector3()
    var lowerarm_angle = Vector3()
    var skel

    func _ready():
        skel = get_node("arm/Armature/Skeleton")
        set_process(true)

    var bone = "upperarm"
    var coordinate = 0

    func set_bone_rot(bone, ang):
        var b = skel.find_bone(bone)
        var rest = skel.get_bone_rest(b)
        var newpose = rest.rotated(Vector3(1.0, 0.0, 0.0), ang.x)
        var newpose = newpose.rotated(Vector3(0.0, 1.0, 0.0), ang.y)
        var newpose = newpose.rotated(Vector3(0.0, 0.0, 1.0), ang.z)
        skel.set_bone_pose(b, newpose)

    func _process(delta):
        if Input.is_action_pressed("select_x"):
            coordinate = 0
        elif Input.is_action_pressed("select_y"):
            coordinate = 1
        elif Input.is_action_pressed("select_z"):
            coordinate = 2
        elif Input.is_action_pressed("select_upperarm"):
            bone = "upperarm"
        elif Input.is_action_pressed("select_lowerarm"):
            bone = "lowerarm"
        elif Input.is_action_pressed("increment"):
            if bone == "lowerarm":
                lowerarm_angle[coordinate] += 1
            elif bone == "upperarm":
                upperarm_angle[coordinate] += 1
        elif Input.is_action_pressed("decrement"):
            if bone == "lowerarm":
                lowerarm_angle[coordinate] -= 1
            elif bone == "upperarm":
                upperarm_angle[coordinate] -= 1
        set_bone_rot("lowerarm", lowerarm_angle)
        set_bone_rot("upperarm", upperarm_angle)

Pressing keys 1/2 selects upperarm/lowerarm, select the axis by pressing x,
y, z, rotate using numpad "+"/"-"

This way you fully control your arm in FK mode using 2 bones. You can
add additional bones and/or improve the "feel" of the interface by using
coefficients for the change. I recommend you play with this example a
lot before going to next part.

You can clone the demo code for this chapter using

::

    git clone git@github.com:slapin/godot-skel3d.git
    cd demo1

Or you can browse it using the web-interface:

https://github.com/slapin/godot-skel3d

Using 3D "bones" to implement Inverse Kinematics
------------------------------------------------

See :ref:`doc_inverse_kinematics`.

Using 3D "bones" to implement ragdoll-like physics
--------------------------------------------------

TODO.
