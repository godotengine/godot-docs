TSCN File Format
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


File Structure
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
them. The only difference between them is the the first element in the heading
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


External Resources
~~~~~~~~~~~~~~~~~~

External resources are links to resources not contained within the TSCN file
itself. An external resource consists of:

 - A path
 - A type
 - An ID

Godot alway generates absolute paths relative to the resource directory and 
thus prefixed with :code:`res://`, but paths relative to the TSCN file's 
location are also valid. 
 
Some example external resources are:

::

    [ext_resource path="res://characters/player.dae" type="PackedScene" id=1]
    [ext_resource path="metal.tres" type="Material" id=2]


Internal Resources
~~~~~~~~~~~~~~~~~~

A TSCN file can contain meshes, materials and other data, and these are 
contained in the internal resources section of the file. The heading
for an internal resource looks very similar to those of external resources, but
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

Unfortunately, documentation on the formats for these subresources is
completely absent, and while some can be found through inspecting resources of
saved files, but others can only be found by looking through Godot's source.


The Scene Tree
--------------

The scene tree is made up of ... nodes! The heading of each node consists of
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
    
Similar to the internal resource, the content for each node is currently 
undocumented. Fortunately it is very easy to find out because you can simply 
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

