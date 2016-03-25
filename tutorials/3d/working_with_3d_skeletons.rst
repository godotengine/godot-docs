.. _doc_working_with_3d_skeletons:

Working with 3D skeletons
=========================

Godot 3D skeleton support is currently quite rudimentary. The
:ref:`class_Skeleton` node and class were designed mainly to support importing
skeletal animations as a set of transformation matrices.

Skeleton node
-------------

Skeleton node can be directly added anywhere you want on scene. Usually
mesh is a child of Skeleton, as it easier to manipulate this way, as
Transforms within skeleton are relative to where Skeleton is. But you
can specify Skeleton node in every MeshInstance.

Being obvious, Skeleton is intended to deform meshes, and consists of
structures called "bones". Each "bone" is represented as Transform, which is
applied to a group of vertices within a mesh. You can directly control a group
of vertices from Godot. For that please reference :ref:`class_MeshDataTool`
class, method :ref:`set_vertex_bones <class_MeshDataTool_set_vertex_bones>`.
This class is very powerful.

The "bones" are organized in hierarchy, every bone, except for root
bone(s) have parent. Every bone have associated name you can use to
refer to it (e.g. "root" or "hand.L", etc.). Also bones are all numbered,
these numbers are bone IDs. Bone parents are referred by their numbered
IDs.

For the rest of the article we consider the following scene:

::

    main (Spatial) - script is always here
    == skel (Skeleton)
    ==== mesh (MeshInstance)

This scene is imported from Blender. It contains arm mesh with 2 bones -
upperarm and lowerarm, with lowerarm parented to upperarm.

Skeleton class
--------------

You can view Godot internal help for descriptions of every function.
Basically all operations on bones are done using their numeric ID. You
can convert from name to numeric ID and vise versa.

**To find number of bones in skeleton we use get_bone_count()
function**

::

    extends Spatial
    var skel

    func _ready():
        skel = get_node("skel")
        var id = skel.find_bone("upperarm")
        print("bone id:", id)
        var parent = skel.get_bone_parent(id)
        print("bone parent id:", id)

**to find ID for the bone, use find_bone() function**

::

    extends Spatial
    var skel

    func _ready():
        skel = get_node("skel")
        var id = skel.find_bone("upperarm")
        print("bone id:", id)

Now, we want to do something interesting with ID except for printing it.
Also, we might need additional information - to find bone parents to
complete chain, etc. This all is done with get/set_bone\_\* functions.

**To find bone parent we use get_bone_parent(id) function**

::

    extends Spatial
    var skel

    func _ready():
        skel = get_node("skel")
        var id = skel.find_bone("upperarm")
        print("bone id:", id)
        var parent = skel.get_bone_parent(id)
        print("bone parent id:", id)

Bone transforms is the thing why we're here at all. There are 3 kind of
transforms - local, global, custom.

**To find bone local Transform we use get_bone_pose(id) function**

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

So we see 3x4 matrix there, with first column of 1s. What can we do
about that? It is a Transform, so we can do everything we can do with
Transform, basically translate, rotate and scale. Also we can multiply
transforms to have complex transforms. Remember, "bones" in Godot are
just Transforms over a group of vertices. Also we can copy Transforms of
other objects there. So lets rotate our "upperarm" bone:

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

    func _process(dt):
        var t = skel.get_bone_pose(id)
        t = t.rotated(Vector3(0.0, 1.0, 0.0), 0.1 * dt)
        skel.set_bone_pose(id, t)

Now we can rotate individual bones. The same happens for scale and
translate - try these on your own and see results.

What we used now was local pose. By default all bones are not modified.
But this Transform tells us nothing about relationship between bones.
This information is needed for quite a number of tasks. How can we get
it? Here comes global transform:

**To find bone global Transform we use get_bone_global_pose(id)
function**

We will find global Transform for lowerarm bone:

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

As you see, this transform is not zeroed. While being called global, it
is actually relative to Skeleton origin. For root bone, origin is always
at 0 if not modified. Lets print origin for our lowerarm bone:

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
point of Transform. So it is base part of the bone. In Blender you can
go to Pose mode and try there to rotate bones - they will rotate around
their origin. But what about tip? We can't know things like bone length,
which we need for many things, without knowing tip location. For all
bones in chain except for last one we can calculate tip location - it is
simply a child bone origin. Yes, there are situations when this is not
true, for non-connected bones. But that is OK for us for now, as it is
not important regarding Transforms. But the leaf bone tip is nowhere to
be found. Leaf bone is a bone without children. So you don't have any
information about its tip. But this is not a showstopper. You can
overcome this by either adding extra bone to the chain or just
calculating leaf bone length in Blender and store the value in your
script.

Using 3D "bones" for mesh control
---------------------------------

Now as you know basics we can apply these to make full FK-control of our
arm (FK is forward-kinematics)

To fully control our arm we need the following parameters:

-  Upperarm angle x, y, z
-  Lowerarm angle x, y, z

All of these parameters can be set, incremented and decremented.

Create the following node tree:

::

    main (Spatial) <- script is here
    +-arm (arm scene)
    + DirectionLight (DirectionLight)
    + Camera

Set up Camera so that arm is properly visible. Rotate DirectionLight
so that arm is properly lit while in scene play mode.

Now we need to create new script under main:

First we setup parameters:

::

    var lowerarm_angle = Vector3()
    var upperarm_angle = Vector3()

Now we need to setup a way to change them. Let us use keys for that.

Please create 7 actions under project settings:

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
    func _process(dt):
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

    func _process(dt):
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

Pressing keys 1/2 select upperarm/lowerarm, select axis by pressing x,
y, z, rotate using numpad "+"/"-"

This way you fully control your arm in FK mode using 2 bones. You can
add additional bones and/or improve "feel" of the interface by using
coefficients for the change. I recommend you play with this example a
lot before going to next part.

You can clone the demo code for this chapter using

::

    git clone git@github.com:slapin/godot-skel3d.git
    cd demo1

Or you can browse it using web-interface:

https://github.com/slapin/godot-skel3d

Using 3D "bones" to implement Inverse Kinematics
------------------------------------------------

See :ref:`doc_inverse_kinematics`.

Using 3D "bones" to implement ragdoll-like physics
--------------------------------------------------

TODO.
