.. _doc_resources:

Resources
=========

Nodes and resources
-------------------

Up to this tutorial, we focused on the :ref:`Node <class_Node>`
class in Godot as that's the one you use to code behavior and
most of the engine's features rely on it. There is
another datatype that is just as important:
:ref:`Resource <class_Resource>`.

*Nodes* give you functionality: they draw sprites, 3D models, simulate physics,
arrange user interfaces, etc. **Resources** are **data containers**. They don't
do anything on their own: instead, nodes use the data contained in resources.

Anything Godot saves or loads from disk is a resource. Be it a scene (a ``.tscn``
or an ``.scn`` file), an image, a script... Here are some ``Resource`` examples:
:ref:`Texture <class_Texture>`, :ref:`Script <class_Script>`, :ref:`Mesh
<class_Mesh>`, :ref:`Animation <class_Animation>`, :ref:`AudioStream
<class_AudioStream>`, :ref:`Font <class_Font>`, :ref:`Translation
<class_Translation>`.

When the engine loads a resource from disk, **it only loads it once**. If a copy
of that resource is already in memory, trying to load the resource again will
return the same copy every time. As resources only contain data, there is no need
to duplicate them.

Every object, be it a Node or a Resource, can export properties. There are many
types of Properties, like String, integer, Vector2, etc., and any of these types
can become a resource. This means that both nodes and resources can contain
resources as properties:

.. image:: img/nodes_resources.png

External vs built-in
--------------------

There are two ways to save resources. They can be:

1. **External** to a scene, saved on the disk as individual files.
2. **Built-in**, saved inside the ``.tscn`` or the ``.scn`` file they're attached to.

To be more specific, here's a :ref:`Texture <class_Texture>`
in a :ref:`Sprite <class_Sprite>` node:

.. image:: img/spriteprop.png

Clicking the resource preview allows us to view and edit the resource's properties.

.. image:: img/resourcerobi.png

The path property tells us where the resource comes from. In this case, it comes
from a PNG image called ``robi.png``. When the resource comes from a file like
this, it is an external resource. If you erase the path or this path is empty,
it becomes a built-in resource.

The switch between built-in and external resources happens when you save the
scene. In the example above, if you erase the path ``"res://robi.png"`` and
save, Godot will save the image inside the ``.tscn`` scene file.

.. note::

    Even if you save a built-in resource, when you instance a scene multiple
    times, the engine will only load one copy of it.

Loading resources from code
---------------------------

There are two ways to load resources from code. First, you can use the ``load()`` function anytime:

.. tabs::
 .. code-tab:: gdscript GDScript

    func _ready():
            var res = load("res://robi.png") # Godot loads the Resource when it reads the line.
            get_node("sprite").texture = res

 .. code-tab:: csharp

    public override void _Ready()
    {
        var texture = (Texture)GD.Load("res://robi.png"); // Godot loads the Resource when it reads the line.
        var sprite = (Sprite)GetNode("sprite");
        sprite.Texture = texture;
    }

You can also ``preload`` resources. Unlike ``load``, this function will read the
file from disk and load it at compile-time. As a result, you cannot call preload
with a variable path: you need to use a constant string.

.. tabs::
 .. code-tab:: gdscript GDScript

    func _ready():
            var res = preload("res://robi.png") # Godot loads the resource at compile-time
            get_node("sprite").texture = res

 .. code-tab:: csharp

    // 'preload()' is unavailable in C Sharp.

Loading scenes
--------------

Scenes are also resources, but there is a catch. Scenes saved to disk are
resources of type :ref:`PackedScene <class_PackedScene>`. The
scene is packed inside a resource.

To get an instance of the scene, you have to use the
:ref:`PackedScene.instance() <class_PackedScene_method_instance>` method.

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

This method creates the nodes in the scene's hierarchy, configures them, and
returns the root node of the scene. You can then add it as a child of any other
node.

The approach has several advantages. As the :ref:`PackedScene.instance()
<class_PackedScene_method_instance>` function is fast, you can create new
enemies, bullets, effects, etc. without having to load them again from disk each
time. Remember that, as always, images, meshes, etc. are all shared between the
scene instances.

Freeing resources
-----------------

When a ``Resource`` is no longer in use, it will automatically free itself.
Since, in most cases, Resources are contained in Nodes, when you free a node,
the engine frees all the resources it owns as well if no other node uses them.

Creating your own resources
---------------------------

Like any Object in Godot, users can also script Resources. Resource scripts
inherit the ability to freely translate between object properties and serialized
text or binary data (/*.tres, /*.res). They also inherit the reference-counting
memory management from the Reference type.

This comes with many distinct advantages over alternative data
structures, such as JSON, CSV, or custom TXT files. Users can only import these
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

Godot makes it easy to create custom Resources in the Inspector.

1. Create a plain Resource object in the Inspector. This can even be a type that derives Resource, so long as your script is extending that type.
2. Set the ``script`` property in the Inspector to be your script.

The Inspector will now display your Resource script's custom properties. If one edits
those values and saves the resource, the Inspector serializes the custom properties
too! To save a resource from the Inspector, click the Inspector's tools menu (top right),
and select "Save" or "Save As...".

If the script's language supports :ref:`script classes <doc_scripting_continued_class_name>`,
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
        # Uses an implicit, duck-typed interface for any 'health'-compatible resources.
        if stats:
            print(stats.health) # Prints '10'.
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
                    if (Stats != null && Stats is BotStats botStats) {
                        GD.Print(botStats.Health); // Prints '10'.
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
            "GodotBot": BotStats.new(10), # Creates instance with 10 health.
            "DifferentBot": BotStats.new(20) # A different one with 20 health.
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
                _stats["GodotBot"] = new BotStats(10); // Creates instance with 10 health.
                _stats["DifferentBot"] = new BotStats(20); // A different one with 20 health.
                GD.Print(_stats);
            }
        }

    Instead of just inlining the Dictionary values, one could also, alternatively...

    1. Import a table of values from a spreadsheet and generate these key-value pairs, or...

    2. Design a visualization within the editor and create a simple plugin that adds it
       to the Inspector when you open these types of Resources.

    CurveTables are the same thing, except mapped to an Array of float values
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

            # This will NOT serialize the 'value' property.
            ResourceSaver.save("res://my_res.tres", my_res)
      .. code-tab:: csharp
        using System;
        using Godot;

        public class MyNode : Node
        {
            public class MyResource : Resource
            {
                [Export]
                public int Value { get; set; } = 5;
            }

            public override void _Ready()
            {
                var res = new MyResource();

                // This will NOT serialize the 'Value' property.
                ResourceSaver.Save("res://MyRes.tres", res);
            }
        }
