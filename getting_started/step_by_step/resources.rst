.. _doc_resources:

Resources
=========

Nodes and resources
-------------------

So far, :ref:`Nodes <class_Node>`
have been the most important datatype in Godot as most of the behaviors
and features of the engine are implemented through them. There is
another datatype that is equally important:
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
:ref:`AudioStream <class_AudioStream>`,
:ref:`Font <class_Font>`,
:ref:`Translation <class_Translation>`,
etc.

When Godot saves or loads (from disk) a scene (.tscn or .scn), an image
(png, jpg), a script (.gd) or pretty much anything, that file is
considered a resource.

When a resource is loaded from disk, **it is always loaded once**. That
means, if there is a copy of that resource already loaded in memory,
trying to load the resource again will return the same copy again
and again. This corresponds with the fact that resources are just data
containers, so there is no need to have them duplicated.

Typically, every object in Godot (Node, Resource, or anything else) can
export properties. Properties can be of many types (like a string,
integer, Vector2, etc) and one of those types can be a resource. This
means that both nodes and resources can contain resources as properties.
To make it a little more visual:

.. image:: img/nodes_resources.png

External vs built-in
--------------------

The resource properties can reference resources in two ways,
*external* (on disk) or **built-in**.

To be more specific, here's a :ref:`Texture <class_Texture>`
in a :ref:`Sprite <class_Sprite>` node:

.. image:: img/spriteprop.png

Pressing the ">" button on the right side of the preview allows us to
view and edit the resources properties. One of the properties (path)
shows where it comes from. In this case, it comes from a png image.

.. image:: img/resourcerobi.png

When the resource comes from a file, it is considered an *external*
resource. If the path property is erased (or it never had a path to
begin with), it is considered a built-in resource.

For example, if the path \`"res://robi.png"\` is erased from the "path"
property in the above example, and then the scene is saved, the resource
will be saved inside the .tscn scene file, no longer referencing the
external "robi.png". However, even if saved as built-in, and even though
the scene can be instanced multiple times, the resource will always
be loaded only once. That means, different Robi robot scenes instanced
at the same time will still share the same image.

Loading resources from code
---------------------------

Loading resources from code is easy. There are two ways to do it. The
first is to use load(), like this:

.. tabs::
 .. code-tab:: gdscript GDScript

    func _ready():
            var res = load("res://robi.png") # resource is loaded when line is executed
            get_node("sprite").texture = res

 .. code-tab:: csharp

    public override void _Ready()
    {
        var texture = (Texture)GD.Load("res://robi.png"); // resource is loaded when line is executed
        var sprite = (Sprite)GetNode("sprite");
        sprite.Texture = texture;
    }

The second way is more optimal, but only works with a string constant
parameter because it loads the resource at compile-time.

.. tabs::
 .. code-tab:: gdscript GDScript

    func _ready():
            var res = preload("res://robi.png") # resource is loaded at compile time
            get_node("sprite").texture = res

 .. code-tab:: csharp

    // preload() is unavailable in C Sharp

Loading scenes
--------------
Scenes are also resources, but there is a catch. Scenes saved to disk
are resources of type :ref:`PackedScene <class_PackedScene>`. This means that
the scene is packed inside a resource.

To obtain an instance of the scene, the method
:ref:`PackedScene.instance() <class_PackedScene_instance>`
must be used.

.. tabs::
 .. code-tab:: gdscript GDScript

    func _on_shoot():
            var bullet = preload("res://bullet.tscn").instance()
            add_child(bullet)


 .. code-tab:: csharp

    private PackedScene _bulletScene = (PackedScene)GD.Load("res://bullet.tscn");

    public void OnShoot()
    {
        Node bullet = _bulletScene.Instance();
        AddChild(bullet);
    }

This method creates the nodes in the scene's hierarchy, configures
them (sets all the properties) and returns the root node of the scene,
which can be added to any other node.

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
or other resources, when a node is removed or freed, all the owned
resources are freed too.

Scripting
---------

Like any Object in Godot, users can also script Resources. As Resources,
Resource scripts inherit the ability to freely translate between object
properties and serialized text or binary data (*.tres, *.res). They also
inherit the reference-counting memory management from the Reference type.

This comes with many distinct advantages over alternative data
structures such as JSON, CSV, or custom TXT files. Users can only import these 
assets as a :ref:`Dictionary <class_Dictionary>` (JSON) or as a 
:ref:`File <class_File>` to parse. What sets Resources apart is their 
inheritance of :ref:`Object <class_Object>`, :ref:`Reference <class_Reference>`,
and :ref:`Resource <class_Resource>` features:

- They can define constants, so constants from other data fields or objects are not needed.

- They can define methods, including setter/getter methods for properties. This allows for abstraction and encapsulation of the underlying data. If the Resource script's structure needs to change, the game using the Resource need not also change.

- They can define signals, so Resources can trigger responses to changes in the data they manage.

- They have defined properties, so users know 100% that their data will exist.

- Resource auto-serialization and deserialization is a built-in Godot Engine feature. Users do not need to implement custom logic to import/export a resource file's data.

- Resources can even serialize sub-Resources recursively, meaning users can design even more sophisticated data structures.

- Users can save Resources as version-control-friendly text files (\*.tres). Upon exporting a game, Godot serializes resource files as binary files (\*.res) for increased speed and compression.

- Godot Engine's Inspector renders and edits Resource files out-of-the-box. As such, users often do not need to implement custom logic to visualize or edit their data. To do so, double-click the resource file in the FileSystem dock or click the folder icon in the Inspector and open the file in the dialog.

- They can extend **other** resource types besides just the base Resource.

.. warning::
    
    Resources and Dictionaries are also different in that both are passed by reference,
    but only Resources are reference-counted. This means that if a Dictionary is passed
    between objects, and the first object is deleted, it will invalidate the second
    object's variable. This is not so for Resources which won't free their memory until
    *all* instances are gone.

    .. tabs::
      .. code-tab:: gdscript GDScript

        extends Node

        class MyObject:
            extends Object
            var dict = {}

        func _ready():
            var obj1 = MyObject.new()
            var obj2 = MyObject.new()
            obj1.dict.greeting = "hello"
            obj2.dict = obj1.dict             # obj2.dict now references obj1's Dictionary
            obj1.free()                       # obj1 is freed and the Dictionary too!
            print(obj2.dict.greeting)         # Error! 'greeting' index accessed on null instance!

            # to avoid this, we must manually duplicate the Dictionary
            obj1 = MyObject.new()
            obj1.dict.greeting = "hello"
            obj2.dict = obj1.dict.duplicate() # now we are passing a copy, not a reference
            obj1.free()                       # obj2's Dictionary still exists
            print(obj2.dict.greeting)         # prints 'hello'

Godot makes it easy to create custom Resources in the Inspector.

1. Create a plain Resource object in the Inspector. This can even be a type that derives Resource, so long as your script is extending that type.
2. Set the ``script`` property in the Inspector to be your script.

The Inspector will now display your Resource script's custom properties. If one edits
those values and saves the resource, the Inspector serializes the custom properties
too! To save a resource from the Inspector, click the Inspector's tools menu (top right),
and select "Save" or "Save As...".

If the script's language supports `script classes <https://godot.readthedocs.io/en/latest/getting_started/step_by_step/scripting_continued.html#register-scripts-as-classes>`__, 
then it streamlines the process. Defining a name for your script alone will add it to
the Inspector's creation dialog. This will auto-add your script to the Resource
object you create.

Let's see some examples.

.. tabs::
  .. code-tab:: gdscript GDScript

    # bot_stats.gd
    extends Resource
    export(int) var health
    export(Resource) var sub_resource
    export(Array, String) var strings

    func _init(p_health = 0, p_sub_resource = null, p_strings = []):
        health = p_health
        sub_resource = p_sub_resource
        strings = p_strings

    # bot.gd
    extends KinematicBody

    export(Resource) var stats

    func _ready():
        # uses an implicit, duck-typed interface for any 'health'-compatible resources
        if stats:
            print(stats.health) # prints '10'
  .. code-tab:: csharp

        // BotStats.cs
        using System;
        using Godot;

        namespace ExampleProject {
            public class BotStats : Resource
            {
                [Export]
                public int Health { get; set; }

                [Export]
                public Resource SubResource { get; set; }

                [Export]
                public String[] Strings { get; set; }

                public BotStats(int health = 0, Resource subResource = null, String[] strings = null)
                {
                    Health = health;
                    SubResource = subResource;
                    Strings = strings ?? new String[0];
                }
            }
        }

        // Bot.cs
        using System;
        using Godot;

        namespace ExampleProject {
            public class Bot : KinematicBody
            {
                [Export]
                public Resource Stats;

                public override void _Ready()
                {
                    if (Stats != null && Stats is BotStats) {
                        Godot.print((Stats as BotStats).Health);
                    }
                }
            }
        }

.. note::

    Resource scripts are similar to Unity's ScriptableObjects. The Inspector 
    provides built-in support for custom resources. If desired though, users 
    can even design their own Control-based tool scripts and combine them 
    with an :ref:`EditorPlugin <class_EditorPlugin>` to create custom 
    visualizations and editors for their data.

    Unreal Engine 4's DataTables and CurveTables are also easy to recreate with
    Resource scripts. DataTables are a String mapped to a custom struct, similar
    to a Dictionary mapping a String to a secondary custom Resource script.

    .. tabs::
      .. code-tab:: gdscript GDScript

        # bot_stats_table.gd
        extends Resource

        const BotStats = preload("bot_stats.gd") 

        var data = {
            "GodotBot": BotStats.new(10), # creates instance with 10 health
            "DifferentBot": BotStats.new(20) # a different one with 20 health
        }

        func _init():
            print(data)
      .. code-tab:: csharp

        using System;
        using Godot;

        public class BotStatsTable : Resource
        {
            private Godot.Dictionary<String, BotStats> _stats = new Godot.Dictionary<String, BotStats>();

            public BotStatsTable()
            {
                _stats["GodotBot"] = new BotStats(10);
                _stats["DifferentBot"] = new BotStats(20);
                Godot.print(_stats);
            }
        }
    
    Instead of just inlining the Dictionary values, one could also, alternatively...

    1. Import a table of values from a spreadsheet and generate these key-value pairs, or...

    2. Design a visualization within the editor and create a simple plugin that adds it
       to the Inspector when you open these types of Resources.

    CurveTables are the same thing except mapped to an Array of float values
    or a :ref:`Curve <class_Curve>`/:ref:`Curve2D <class_Curve2D>` resource object.

.. warning::

    Beware that resource files (\*.tres/\*.res) will store the path of the script
    they use in the file. When loaded, they will fetch and load this script as an
    extension of their type. This means that trying to assign a subclass, i.e. an
    inner class of a script (such as using the ``class`` keyword in GDScript) won't
    work. Godot will not serialize the custom properties on the script subclass properly.

    In the example below, Godot would load the ``Node`` script, see that it doesn't
    extend ``Resource``, and then determine that the script failed to load for the 
    Resource object since the types are incompatible.

    .. tabs::
      .. code-tab:: gdscript GDScript

        extends Node

        class MyResource:
            extends Resource
            export var value = 5

        func _ready():
            var my_res = MyResource.new()

            # this will NOT serialize the `value` property.
            ResourceSaver.save("res://my_res.tres", my_res) 
      .. code-tab:: csharp
        using System;
        using Godot;

        public class MyNode : Node
        {

            public class MyResource : Resource {
                [Export]
                public int Value { get; set; } = 5;
            }

            public override void _Ready()
            {
                MyResource res = new MyResource();

                // this will NOT serialize the `Value` property.
                ResourceSaver.save("res://MyRes.tres", res);
            }
        }

After seeing all of this, we hope you can see how Resource scripts can truly 
revolutionize the way you construct your projects!