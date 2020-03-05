TSCN file format
================

The TSCN (text scene) file format represents a single scene tree inside
Godot. TSCN files have the advantage of being mostly human-readable and easy for
version control systems to manage. During import, TSCN files are compiled into
binary ``.scn`` files stored inside the .import folder. This reduces the data
size and speeds up loading.

The ESCN (exported scene) file format is identical to the TSCN file format, but
is used to indicate to Godot that the file has been exported from another
program and should not be edited by the user from within Godot.

For those looking for a complete description, the parsing is handled in the file
`resource_format_text.cpp <https://github.com/godotengine/godot/blob/master/scene/resources/resource_format_text.cpp>`_
in the ``ResourceFormatLoaderText`` class.

File structure
--------------

There are five main sections inside the TSCN file:

0. File Descriptor
1. External resources
2. Internal resources
3. Nodes
4. Connections

The file descriptor looks like ``[gd_scene load_steps=1 format=2]`` and should
be the first entry in the file. The ``load_steps`` parameter should (in theory)
be the number of resources within the file. However, in practice, its value seems
not to matter.

These sections should appear in order, but it can be hard to distinguish them.
The only difference between them is the first element in the heading for all of
the items in the section. For example, the heading of all external resources
should start with ``[ext_resource .....]``.

A TSCN file may contain single-line comments starting with a semicolon (``;``).
However, comments will be discarded when saving the file using the Godot editor.

Entries inside the file
~~~~~~~~~~~~~~~~~~~~~~~

A heading looks like
``[<resource_type> key=value key=value key=value ...]``
where resource_type is one of:

- ``ext_resource``
- ``sub_resource``
- ``node``
- ``connection``

Below every heading comes zero or more ``key = value`` pairs. The
values can be complex datatypes such as Arrays, Transforms, Colors, and
so on. For example, a spatial node looks like:

::

    [node name="Cube" type="Spatial" parent="."]
    transform=Transform( 1.0, 0.0, 0.0 ,0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0 )


The scene tree
--------------

The scene tree is made up of… nodes! The heading of each node consists of
its name, parent and (most of the time) a type. For example
``[node type="Camera" name="PlayerCamera" parent="Player/Head"]``

Other valid keywords include:

 - ``instance``
 - ``instance_placeholder``
 - ``owner``
 - ``index`` (if two nodes have the same name)
 - ``groups``

The first node in the file, which is also the scene root, must not have a
``parent=Path/To/Node`` entry in its heading. All scene files should have
exactly *one* scene root. If it doesn't, Godot will fail to import the file.
The parent path of other nodes should be absolute, but shouldn't contain
the scene root's name. If the node is a direct child of the scene root,
the path should be ``"."``. Here is an example scene tree
(but without any node content):

::

    [node name="Player" type="Spatial"]             ; The scene root
    [node name="Arm" parent="." type="Spatial"]     ; Parented to the scene root
    [node name="Hand" parent="Arm" type="Spatial"]
    [node name="Finger" parent="Arm/Hand" type="Spatial"]


Similar to the internal resource, the document for each node is currently
incomplete. Fortunately, it is easy to find out because you can simply
save a file with that node in it. Some example nodes are:

::

    [node type="CollisionShape" name="SphereCollision" parent="SpherePhysics"]

    shape = SubResource(8)
    transform = Transform( 1.0 , 0.0 , -0.0 , 0.0 , -4.371138828673793e-08 , 1.0 , -0.0 , -1.0 , -4.371138828673793e-08 ,0.0 ,0.0 ,-0.0  )


    [node type="MeshInstance" name="Sphere" parent="SpherePhysics"]

    mesh = SubResource(9)
    transform = Transform( 1.0 , 0.0 , -0.0 , 0.0 , 1.0 , -0.0 , -0.0 , -0.0 , 1.0 ,0.0 ,0.0 ,-0.0  )


    [node type="OmniLight" name="Lamp" parent="."]

    light_energy = 1.0
    light_specular = 1.0
    transform = Transform( -0.29086464643478394 , -0.7711008191108704 , 0.5663931369781494 , -0.05518905818462372 , 0.6045246720314026 , 0.7946722507476807 , -0.9551711678504944 , 0.199883371591568 , -0.21839118003845215 ,4.076245307922363 ,7.3235554695129395 ,-1.0054539442062378  )
    omni_range = 30
    shadow_enabled = true
    light_negative = false
    light_color = Color( 1.0, 1.0, 1.0, 1.0 )


    [node type="Camera" name="Camera" parent="."]

    projection = 0
    near = 0.10000000149011612
    fov = 50
    transform = Transform( 0.6859206557273865 , -0.32401350140571594 , 0.6515582203865051 , 0.0 , 0.8953956365585327 , 0.44527143239974976 , -0.7276763319969177 , -0.3054208755493164 , 0.6141703724861145 ,14.430776596069336 ,10.093015670776367 ,13.058500289916992  )
    far = 100.0


NodePath
~~~~~~~~

A tree structure is not enough to represent the whole scene. Godot uses a
``NodePath(Path/To/Node)`` structure to refer to another node or attribute of
the node anywhere in the scene tree. For instance, MeshInstance uses
``NodePath()`` to point to its skeleton. Likewise, Animation tracks use
``NodePath()`` to point to node properties to animate.

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

The Skeleton node inherits the Spatial node, but also may have a list of bones
described in key-value pairs in the format ``bones/Id/Attribute=Value``. The
bone attributes consist of:

- ``name``
- ``parent``
- ``rest``
- ``pose``
- ``enabled``
- ``bound_children``

1. ``name`` must be the first attribute of each bone.
2. ``parent`` is the index of parent bone in the bone list, with parent index,
   the bone list is built to a bone tree.
3. ``rest`` is the transform matrix of bone in its "resting" position.
4. ``pose`` is the pose matrix; use ``rest`` as the basis.
5. ``bound_children`` is a list of ``NodePath()`` which point to
   BoneAttachments belonging to this bone.

Here's an example of a skeleton node with two bones:

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
to a single bone in a Skeleton node. The BoneAttachment has a
``bone_name=NameOfBone`` attribute, and the corresponding bone being the parent has the
BoneAttachment node in its ``bound_children`` list.

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

AnimationPlayer works as an animation library. It stores animations listed in
the format ``anim/Name=SubResource(ResourceId)``; each line refers to an
Animation resource. All the animation resources use the root node of
AnimationPlayer. The root node is stored as
``root_node=NodePath(Path/To/Node)``.

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

References to the resources are handled by ``id`` numbers in the resource's
heading. External resources and internal resources are referred to with
``ExtResource(id)`` and ``SubResource(id)``, respectively. Because there
have different methods to refer to internal and external resources, you can have
the same ID for both an internal and external resource.

For example, to refer to the resource ``[ext_resource id=3 type="PackedScene"
path=....]``, you would use ``ExtResource(3)``.

External resources
~~~~~~~~~~~~~~~~~~

External resources are links to resources not contained within the TSCN file
itself. An external resource consists of a path, a type and an ID.

Godot always generates absolute paths relative to the resource directory and
thus prefixed with ``res://``, but paths relative to the TSCN file's location
are also valid.

Some example external resources are:

::

    [ext_resource path="res://characters/player.dae" type="PackedScene" id=1]
    [ext_resource path="metal.tres" type="Material" id=2]


Like TSCN files, a TRES file may contain single-line comments starting with a
semicolon (``;``). However, comments will be discarded when saving the resource
using the Godot editor.

Internal resources
~~~~~~~~~~~~~~~~~~

A TSCN file can contain meshes, materials and other data. These are contained in
the *internal resources* section of the file. The heading for an internal
resource looks similar to those of external resources, except that it doesn't
have a path. Internal resources also have ``key=value`` pairs under each
heading. For example, a capsule collision shape looks like:

::

    [sub_resource  type="CapsuleShape" id=2]

    radius = 0.5
    height = 3.0


Some internal resources contain links to other internal resources (such as a
mesh having a material). In this case, the referring resource must appear
*before* the reference to it. This means that order matters in the file's
internal resources section.

Unfortunately, documentation on the formats for these subresources isn't
complete. Some examples can be found by inspecting saved resource files, but
others can only be found by looking through Godot's source.

ArrayMesh
~~~~~~~~~

ArrayMesh consists of several surfaces, each in the format ``surface\Index={}``.
Each surface is a set of vertices and a material.

TSCN files support two surface formats:

1. For the old format, each surface has three essential keys:

- ``primitive``
- ``arrays``
- ``morph_arrays``

    i. ``primitive`` is an enumerate variable, ``primitive=4`` which is
       ``PRIMITIVE_TRIANGLES`` is frequently used.

    ii. ``arrays`` is a two-dimensional array, it contains:

        1. Vertex positions array
        2. Tangents array
        3. Vertex colors array
        4. UV array 1
        5. UV array 2
        6. Bone indexes array
        7. Bone weights array
        8. Vertex indexes array

    iii. ``morph_arrays`` is an array of morphs. Each morph is exactly an
         ``arrays`` without the vertex indexes array.

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

An animation resource consists of tracks. Besides, it has ``length``, ``loop``
and ``step`` applied to all the tracks.

1. ``length`` and ``step`` are both durations in seconds.

Each track is described by a list of key-value pairs in the format
``tracks/Id/Attribute``. Each track includes:

- ``type``
- ``path``
- ``interp``
- ``keys``
- ``loop_wrap``
- ``imported``
- ``enabled``

1. The ``type`` must be the first attribute of each track.
   The value of ``type`` can be:

    - ``transform``
    - ``value``
    - ``method``

2. The ``path`` has the format ``NodePath(Path/To/Node:attribute)``.
   It's the path to the animated node or attribute, relative to the root node
   defined in the AnimationPlayer.

3. The ``interp`` is the method to interpolate frames from the keyframes.
   It is an enum variable with one of the following values:

    - ``0`` (constant)
    - ``1`` (linear)
    - ``2`` (cubic)

4. The ``keys`` correspond to the keyframes. It appears as a ``PoolRealArray()``,
   but may have a different structure for tracks with different types.

    - A Transform track uses every 12 real numbers in the ``keys`` to describe
      a keyframe. The first number is the timestamp. The second number is the
      transition followed by a 3-number translation vector, followed by a
      4-number rotation quaternion (X, Y, Z, W) and finally a 3-number
      scale vector. The default transition in a Transform track is 1.0.

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
