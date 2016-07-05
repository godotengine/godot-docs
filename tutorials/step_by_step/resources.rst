.. _doc_resources:

Resources
=========

Nodes and resources
-------------------

So far, :ref:`Nodes <class_Node>`
have been the most important datatype in Godot, as most of the behaviors
and features of the engine are implemented through them. There is,
though, another datatype that is equally as important. That is
:ref:`Resource <class_Resource>`.

Where *Nodes* focus on behaviors, such as drawing a sprite, drawing a
3D model, physics, GUI controls, etc,

**Resources** are mere **data containers**. This means that they don't
do any action nor process any information. Resources just contain
data.

Examples of resources are
:ref:`Texture <class_Texture>`,
:ref:`Script <class_Script>`,
:ref:`Mesh <class_Mesh>`,
:ref:`Animation <class_Animation>`,
:ref:`Sample <class_Sample>`,
:ref:`AudioStream <class_AudioStream>`,
:ref:`Font <class_Font>`,
:ref:`Translation <class_Translation>`,
etc.

When Godot saves or loads (from disk) a scene (.scn or .xml), an image
(png, jpg), a script (.gd) or pretty much anything, that file is
considered a resource.

When a resource is loaded from disk, **it is always loaded once**. That
means, if there is a copy of that resource already loaded in memory,
trying to load the resource again will just return the same copy again
and again. This corresponds with the fact that resources are just data
containers, so there is no need to have them duplicated.

Typically, every object in Godot (Node, Resource, or anything else) can
export properties, properties can be of many types (like a string,
integer, Vector2, etc) and one of those types can be a resource. This
means that both nodes and resources can contain resources as properties.
To make it a little more visual:

.. image:: /img/nodes_resources.png

External vs built-in
--------------------

The resource properties can reference resources in two ways,
*external* (on disk) or **built-in**.

To be more specific, here's a :ref:`Texture <class_Texture>`
in a :ref:`Sprite <class_Sprite>` node:

.. image:: /img/spriteprop.png

Pressing the the ">" button the right side of the preview, allows to
view and edit the resources properties. One of the properties (path)
shows where it came from. In this case, it came from a png image.

.. image:: /img/resourcerobi.png

When the resource comes from a file, it is considered an *external*
resource. If the path property is erased (or never had a path to begin
with), it is then considered a built-in resource.

For example, if the path \`"res://robi.png"\` is erased from the "path"
property in the above example, and then the scene is saved, the resource
will be saved inside the .scn scene file, no longer referencing the
external "robi.png". However, even if saved as built-in, and even though
the scene can be instanced multiple times, the resource will still
always be loaded once. That means, different Robi robot scenes instanced
at the same time will still share the same image.

Loading resources from code
---------------------------

Loading resources from code is easy, there are two ways to do it. The
first is to use load(), like this:

::

    func _ready():
            var res = load("res://robi.png") # resource is loaded when line is executed
            get_node("sprite").set_texture(res)

The second way is more optimal, but only works with a string constant
parameter, because it loads the resource at compile-time.

::

    func _ready():
            var res = preload("res://robi.png") # resource is loaded at compile time
            get_node("sprite").set_texture(res)

Loading scenes
--------------

Scenes are also resources, but there is a catch. Scenes saved to disk
are resources of type :ref:`PackedScene <class_PackedScene>`,
this means that the scene is packed inside a resource.

To obtain an instance of the scene, the method
:ref:`PackedScene.instance() <class_PackedScene_instance>`
must be used.

::

    func _on_shoot():
            var bullet = preload("res://bullet.scn").instance()
            add_child(bullet)                  

This method creates the nodes in hierarchy, configures them (sets all
the properties) and returns the root node of the scene, which can be
added to any other node.

The approach has several advantages. As the
:ref:`PackedScene.instance() <class_PackedScene_instance>`
function is pretty fast, adding extra content to the scene can be done
efficiently. New enemies, bullets, effects, etc can be added or
removed quickly, without having to load them again from disk each
time. It is important to remember that, as always, images, meshes, etc
are all shared between the scene instances.

Freeing resources
-----------------

Resource extends from :ref:`Reference <class_Reference>`.
As such, when a resource is no longer in use, it will automatically free
itself. Since, in most cases, Resources are contained in Nodes, scripts
or other resources, when a node is removed or freed, all the children
resources are freed too.

Scripting
---------

Like any object in Godot, not just nodes, resources can be scripted too.
However, there isn't generally much of a win, as resources are just data
containers.
