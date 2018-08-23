TSCN file format
================

A :code:`.tscn` File format is the "Text SCeNe" file format and represents 
a single scene-tree inside Godot. TSCN files have the advantage of being 
nearly human-readable and easy for version control systems to manage. During 
import the TSCN files are compiled into binary :code:`.scn` files stored 
inside the .import folder. This reduces the data size and speed up loading.

The :code:`.escn` file format is identical to the TSCN file format, but is used to 
indicate to Godot that the file has been exported from another program and
should not be edited by the user from within Godot.

For those looking for a complete description, the parsing is handled in the
file `scene_format_text.cpp <https://github.com/godotengine/godot/blob/master/scene/resources/scene_format_text.cpp>`_
in the class :code:`ResourceFormatLoaderText`

File structure
--------------

There are five main sections inside the TSCN File:

0. File Descriptor
1. External resources 
2. Internal resources
3. Nodes
4. Connections

The file descriptor looks like :code:`[gd_scene load_steps=1 format=2]` And 
should be the first entry in the file. The load_steps parameter should (in 
theory) be the number of resources within the file, though in practice it's 
value seems not to matter.

These sections should appear in order, but it can be hard to distinguish 
them. The only difference between them is the first element in the heading
for all of the items in the section.
For example, the heading of all external resources should start with
:code:`[ext_resource .....]`

Entries inside the file
~~~~~~~~~~~~~~~~~~~~~~~

A heading looks like:
:code:`[<resource_type> key=value key=value key=value ...]`
Where resource_type is one of:

- ext_resource
- sub_resource
- node
- connection
 
Underneath every heading comes zero or more :code:`key = value` pairs. The 
values can be complex datatypes such as arrays, transformations, colors, and 
so on. For example, a spatial node looks like:

::

    [node name="Cube" type="Spatial" parent="."]
    transform=Transform( 1.0, 0.0, 0.0 ,0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0 )

The scene tree
--------------

The scene tree is made up of... nodes! The heading of each node consists of
it's name, parent and (most of the time) a type. For example
:code:`[node type="Camera" name="PlayerCamera" parent="Player/Head"]`

Other valid keywords include:

 - instance
 - instance_placeholder
 - owner
 - index (if two nodes have the same name)
 - groups

The first node in the file should not have the :code:`parent=Path/To/Node` 
entry in it's heading, and it is the scene root. All scene files should have 
exactly one scene root. It it does not, Godot will fail to import the file. 
The parent path of other nodes should be absolute, but without the scene 
root's name. If it is a direct child of the scene root, it should be 
:code:`"."`. Here is an example scene tree (but without any node content).

::

    [node name="Player" type="Spatial"]             ; The scene root
    [node name="Arm" parent="." type="Spatial"]     ; Parented to the scene root
    [node name="Hand" parent="Arm" type="Spatial"]
    [node name="Finger" parent="Arm/Hand" type="Spatial"]
    
Similar to the internal resource, the document for each node is currently 
incomplete. Fortunately it is easy to find out because you can simply 
save a file with that node in it. Some example nodes are:

::

    [node  type="CollisionShape" name="SphereCollision" parent="SpherePhysics"]

    shape = SubResource(8)
    transform = Transform( 1.0 , 0.0 , -0.0 , 0.0 , -4.371138828673793e-08 , 1.0 , -0.0 , -1.0 , -4.371138828673793e-08 ,0.0 ,0.0 ,-0.0  )


    [node  type="MeshInstance" name="Sphere" parent="SpherePhysics"]

    mesh = SubResource(9)
    transform = Transform( 1.0 , 0.0 , -0.0 , 0.0 , 1.0 , -0.0 , -0.0 , -0.0 , 1.0 ,0.0 ,0.0 ,-0.0  )


    [node  type="OmniLight" name="Lamp" parent="."]

    light_energy = 1.0
    light_specular = 1.0
    transform = Transform( -0.29086464643478394 , -0.7711008191108704 , 0.5663931369781494 , -0.05518905818462372 , 0.6045246720314026 , 0.7946722507476807 , -0.9551711678504944 , 0.199883371591568 , -0.21839118003845215 ,4.076245307922363 ,7.3235554695129395 ,-1.0054539442062378  )
    omni_range = 30
    shadow_enabled = true
    light_negative = false
    light_color = Color( 1.0, 1.0, 1.0, 1.0 )


    [node  type="Camera" name="Camera" parent="."]

    projection = 0
    near = 0.10000000149011612
    fov = 50
    transform = Transform( 0.6859206557273865 , -0.32401350140571594 , 0.6515582203865051 , 0.0 , 0.8953956365585327 , 0.44527143239974976 , -0.7276763319969177 , -0.3054208755493164 , 0.6141703724861145 ,14.430776596069336 ,10.093015670776367 ,13.058500289916992  )
    far = 100.0

NodePath
~~~~~~~~

A tree structure is not enough to represent the whole scene, Godot use
a :code:`NodePath(Path/To/Node)` structure to refer to another node or
attribute of the node anywhere in the scene tree. Some typical usages of
NodePath like mesh node use :code:`NodePath()` to point to its skeleton,
animation track use :code:`NodePath()` points to animated attribute in node.

::

    [node name="mesh" type="MeshInstance" parent="Armature001"]

    mesh = SubResource(1)
    skeleton = NodePath("..:")

::

    [sub_resource id=3 type="Animation"]

    ...
    tracks/0/type = "transform
    tracks/0/path = NodePath("Cube:")
    ...

Skeleton
~~~~~~~~

Skeleton node inherits Spatial node, besides that it may have a list
of bones described in key, value pair in the format :code:`bones/Id/Attribute=Value`,
attributes of bone consists of 

- name
- parent
- rest
- pose
- enabled
- bound_children

1) :code:`name` must put as the first attribute of each bone

2) :code:`parent` is the index of parent bone in the bone list, with parent index,
   the bone list is built to a bone tree

3) :code:`rest` is the transform matrix of bone in rest position

4) :code:`pose` is the pose matrix use :code:`rest` as basis

5) :code:`bound_children` is a list of NodePath() points to 
   BoneAttachments belong to this bone

An example of a skeleton node with two bones:

::

    [node name="Skeleton" type="Skeleton" parent="Armature001" index="0"]

    bones/0/name = "Bone.001"
    bones/0/parent = -1
    bones/0/rest = Transform( 1, 0, 0, 0, 0, -1, 0, 1, 0, 0.038694, 0.252999, 0.0877164 )
    bones/0/pose = Transform( 1.0, 0.0, -0.0, 0.0, 1.0, -0.0, -0.0, -0.0, 1.0, 0.0, 0.0, -0.0 )
    bones/0/enabled = true
    bones/0/bound_children = [  ]
    bones/1/name = "Bone.002"
    bones/1/parent = 0
    bones/1/rest = Transform( 0.0349042, 0.99939, 0.000512929, -0.721447, 0.0248417, 0.692024, 0.691589, -0.0245245, 0.721874, 0, 5.96046e-08, -1.22688 )
    bones/1/pose = Transform( 1.0, 0.0, -0.0, 0.0, 1.0, -0.0, -0.0, -0.0, 1.0, 0.0, 0.0, -0.0 )
    bones/1/enabled = true
    bones/1/bound_children = [  ]

BoneAttachment
~~~~~~~~~~~~~~

BoneAttachment node is an intermediate node to describe some node being parented
to a single bone in Skeleton node. The BoneAttachment has a :code:`bone_name=NameOfBone`,
and the corresponding bone being the parent has the BoneAttachment node 
in its :code:`bound_children` list.

An example of one MeshInstance parented to a bone in Skeleton:

::

    [node name="Armature" type="Skeleton" parent="."]

    transform = Transform(1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, -0.0219986, 0.0125825, 0.0343127)
    bones/0/name = "Bone"
    bones/0/parent = -1
    bones/0/rest = Transform(1.0, 0.0, 0.0, 0.0, 0.0, -1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0)
    bones/0/pose = Transform(1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0)
    bones/0/enabled = true
    bones/0/bound_children = [NodePath("BoneAttachment:")]

    [node name="BoneAttachment" type="BoneAttachment" parent="Armature"]

    bone_name = "Bone"

    [node name="Cylinder" type="MeshInstance" parent="Armature/BoneAttachment"]

    mesh = SubResource(1)
    transform = Transform(1.0, 0.0, 0.0, 0.0, 1.86265e-09, 1.0, 0.0, -1.0, 0.0, 0.0219986, -0.0343127, 2.25595)

AnimationPlayer
~~~~~~~~~~~~~~~

AnimationPlayer works as an animation lib. it has animations listed in the format
:code:`anim/Name=SubResource(ResourceId)`, each refers to a Animation
internal resource. All the animation resources use the root node of AnimationPlayer.
The root node is stored as :code:`root_node=NodePath(Path/To/Node)`.

::

    [node name="AnimationPlayer" type="AnimationPlayer" parent="." index="1"]

    root_node = NodePath("..")
    autoplay = ""
    playback_process_mode = 1
    playback_default_blend_time = 0.0
    playback_speed = 1.0
    anims/default = SubResource( 2 )
    blend_times = [  ]

Resources
---------

Resources are components that make up the nodes. For example, a MeshInstance
node will have an accompanying ArrayMesh resource. The ArrayMesh resource
may be either internal or external to the TSCN file.

References to the resources are handled by id numbers in the resources heading.
External resources and internal resource are referred to with 
:code:`ExtResource(id)` and :code:`SubResource(id)`. Because there have 
different methods to refer to internal and external resource, you can have
the same ID for both an internal and external resource.

For example, to refer to the resource
:code:`[ext_resource id=3 type="PackedScene" path=....]` you would use 
:code:`ExtResource(3)`

External resources
~~~~~~~~~~~~~~~~~~

External resources are links to resources not contained within the TSCN file
itself. An external resource consists of:

 - A path
 - A type
 - An ID

Godot always generates absolute paths relative to the resource directory and 
thus prefixed with :code:`res://`, but paths relative to the TSCN file's 
location are also valid. 
 
Some example external resources are:

::

    [ext_resource path="res://characters/player.dae" type="PackedScene" id=1]
    [ext_resource path="metal.tres" type="Material" id=2]

Internal resources
~~~~~~~~~~~~~~~~~~

A TSCN file can contain meshes, materials and other data, and these are 
contained in the internal resources section of the file. The heading
for an internal resource looks similar to those of external resources, but
does not have a path. Internal resources also have :code:`key=value` pairs 
under each heading. For example, a capsule collision shape looks like:

::

    [sub_resource  type="CapsuleShape" id=2]

    radius = 0.5
    height = 3.0
    
Some internal resource contain links to other internal resources (such as a 
mesh having a material). In this case, the referring resource must appear 
before the reference to it. Thus, in the internal resources section of the 
file, order does matter.

Unfortunately, documentation on the formats for these subresources is not
complete, and while some can be found through inspecting resources of
saved files, others can only be found by looking through Godot's source.

ArrayMesh
~~~~~~~~~

ArrayMesh consists of several surfaces, each in the format :code:`surface\Index={}`,
each surface is a set of vertex and a material.

TSCN support two format of surface,

1) for the old format, each surface has three essential keys:

- primitive
- arrays
- morph_arrays

    i) :code:`primitive` is an enumerate variable, :code:`primitive=4` which is 
       PRIMITIVE_TRIANGLES is frequently used.

    ii) :code:`arrays` as the name suggests is an array of array, it contains:

        1) An array of vertex position
        2) Tangents array
        3) Vertex color array
        4) UV array 1
        5) UV array 2
        6) Bone index array
        7) Bone weight array
        8) Vertex index array

    iii) :code:`morph_arrays` is an array of morph, each morph is exactly an 
         :code:`arrays` without vertex index array.

An example of ArrayMesh:

::

    [sub_resource id=1 type="ArrayMesh"]

    surfaces/0 = {
        "primitive":4,
        "arrays":[
            Vector3Array(0.0, 1.0, -1.0, 0.866025, -1.0, -0.5, 0.0, -1.0, -1.0, 0.866025, 1.0, -0.5, 0.866025, -1.0, 0.5, 0.866025, 1.0, 0.5, -8.74228e-08, -1.0, 1.0, -8.74228e-08, 1.0, 1.0, -0.866025, -1.0, 0.5, -0.866025, 1.0, 0.5, -0.866025, -1.0, -0.5, -0.866025, 1.0, -0.5),
            Vector3Array(0.0, 0.609973, -0.792383, 0.686239, -0.609973, -0.396191, 0.0, -0.609973, -0.792383, 0.686239, 0.609973, -0.396191, 0.686239, -0.609973, 0.396191, 0.686239, 0.609973, 0.396191, 0.0, -0.609973, 0.792383, 0.0, 0.609973, 0.792383, -0.686239, -0.609973, 0.396191, -0.686239, 0.609973, 0.396191, -0.686239, -0.609973, -0.396191, -0.686239, 0.609973, -0.396191),
            null, ; No Tangents,
            null, ; no Vertex Colors,
            null, ; No UV1,
            null, ; No UV2,
            null, ; No Bones,
            null, ; No Weights,
            IntArray(0, 2, 1, 3, 1, 4, 5, 4, 6, 7, 6, 8, 0, 5, 9, 9, 8, 10, 11, 10, 2, 1, 10, 8, 0, 1, 3, 3, 4, 5, 5, 6, 7, 7, 8, 9, 5, 0, 3, 0, 9, 11, 9, 5, 7, 9, 10, 11, 11, 2, 0, 10, 1, 2, 1, 6, 4, 6, 1, 8)
        ],
        "morph_arrays":[]
    }

Animation
~~~~~~~~~

An animation resource consists of tracks. Besides, it has 'length', 'loop' and
'step' applied to all the tracks.

- length
- loop
- step

1) :code:`length` and :code:`step` are both time in seconds

Each track is described by a list of (key, value) pairs in the format :code:`tracks/Id/Attribute`,
it includes:

- type
- path
- interp
- keys
- loop_wrap
- imported
- enabled

1) The :code:`type` must be put as the first attribute of each track. 
   The value of :code:`type` can be:

    - 'transform'
    - 'value'
    - 'method'

2) The :code:`path` has the format :code:`NodePath(Path/To/Node:Attribute)`. 
   It is the path from animation root node (property of AnimationPlayer) to the 
   animated node or attrbute.

3) The :code:`interp` is the method to interpolate frames from the keyframes.
   it is a enum variable and can has value:

    - 0 (constant)
    - 1 (linear)
    - 2 (cubic)

4) The :code:`keys` is the keyframes, it appears as a PoolRealArray() 
   but have different structure for track with different type

    - A transform track use every 12 real number in the :code:`keys` to describte a keyframe. 
      The first number is the timestamp, the second number is the transition (default 1.0
      in transform track), followed by a three number translation vector, followed by 
      four number rotation quaternion (x,y,z,w) and finally a three number scale vector.

::

    [sub_resource type="Animation" id=2]

    length = 4.95833
    loop = false
    step = 0.1
    tracks/0/type = "transform"
    tracks/0/path = NodePath("Armature001")
    tracks/0/interp = 1
    tracks/0/loop_wrap = true
    tracks/0/imported = true
    tracks/0/enabled = true
    tracks/0/keys = PoolRealArray( 0, 1, -0.0358698, -0.829927, 0.444204, 0, 0, 0, 1, 0.815074, 0.815074, 0.815074, 4.95833, 1, -0.0358698, -0.829927, 0.444204, 0, 0, 0, 1, 0.815074, 0.815074, 0.815074 )
    tracks/1/type = "transform"
    tracks/1/path = NodePath("Armature001/Skeleton:Bone.001")
    tracks/1/interp = 1
    tracks/1/loop_wrap = true
    tracks/1/imported = true
    tracks/1/enabled = false
    tracks/1/keys = PoolRealArray( 0, 1, 0, 5.96046e-08, 0, 0, 0, 0, 1, 1, 1, 1, 4.95833, 1, 0, 5.96046e-08, 0, 0, 0, 0, 1, 1, 1, 1 )
