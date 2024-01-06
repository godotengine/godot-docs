.. _doc_logic_preferences:

Logic preferences
=================

Ever wondered whether one should approach problem X with strategy Y or Z?
This article covers a variety of topics related to these dilemmas.

Adding nodes and changing properties: which first?
--------------------------------------------------

When initializing nodes from a script at runtime, you may need to change
properties such as the node's name or position. A common dilemma is, when
should you change those values?

It is the best practice to change values on a node before adding it to the
scene tree. Some property's setters have code to update other
corresponding values, and that code can be slow! For most cases, this code
has no impact on your game's performance, but in heavy use cases such as
procedural generation, it can bring your game to a crawl.

For these reasons, it is always a best practice to set the initial values
of a node before adding it to the scene tree.

Loading vs. preloading
----------------------

In GDScript, there exists the global
:ref:`preload <class_@GDScript_method_preload>` method. It loads resources as
early as possible to front-load the "loading" operations and avoid loading
resources while in the middle of performance-sensitive code.

Its counterpart, the :ref:`load <class_@GDScript_method_load>` method, loads a
resource only when it reaches the load statement. That is, it will load a
resource in-place which can cause slowdowns when it occurs in the middle of
sensitive processes. The ``load()`` function is also an alias for
:ref:`ResourceLoader.load(path) <class_ResourceLoader_method_load>` which is
accessible to *all* scripting languages.

So, when exactly does preloading occur versus loading, and when should one use
either? Let's see an example:

.. tabs::
  .. code-tab:: gdscript GDScript

    # my_buildings.gd
    extends Node

    # Note how constant scripts/scenes have a different naming scheme than
    # their property variants.

    # This value is a constant, so it spawns when the Script object loads.
    # The script is preloading the value. The advantage here is that the editor
    # can offer autocompletion since it must be a static path.
    const BuildingScn = preload("res://building.tscn")

    # 1. The script preloads the value, so it will load as a dependency
    #    of the 'my_buildings.gd' script file. But, because this is a
    #    property rather than a constant, the object won't copy the preloaded
    #    PackedScene resource into the property until the script instantiates
    #    with .new().
    #
    # 2. The preloaded value is inaccessible from the Script object alone. As
    #    such, preloading the value here actually does not benefit anyone.
    #
    # 3. Because the user exports the value, if this script stored on
    #    a node in a scene file, the scene instantiation code will overwrite the
    #    preloaded initial value anyway (wasting it). It's usually better to
    #    provide null, empty, or otherwise invalid default values for exports.
    #
    # 4. It is when one instantiates this script on its own with .new() that
    #    one will load "office.tscn" rather than the exported value.
    @export var a_building : PackedScene = preload("office.tscn")

    # Uh oh! This results in an error!
    # One must assign constant values to constants. Because `load` performs a
    # runtime lookup by its very nature, one cannot use it to initialize a
    # constant.
    const OfficeScn = load("res://office.tscn")

    # Successfully loads and only when one instantiates the script! Yay!
    var office_scn = load("res://office.tscn")

  .. code-tab:: csharp

    using Godot;

    // C# and other languages have no concept of "preloading".
    public partial class MyBuildings : Node
    {
        //This is a read-only field, it can only be assigned when it's declared or during a constructor.
        public readonly PackedScene Building = ResourceLoader.Load<PackedScene>("res://building.tscn");

        public PackedScene ABuilding;

        public override void _Ready()
        {
            // Can assign the value during initialization.
            ABuilding = GD.Load<PackedScene>("res://Office.tscn");
        }
    }

Preloading allows the script to handle all the loading the moment one loads the
script. Preloading is useful, but there are also times when one doesn't wish
for it. To distinguish these situations, there are a few things one can
consider:

1. If one cannot determine when the script might load, then preloading a
   resource, especially a scene or script, could result in further loads one
   does not expect. This could lead to unintentional, variable-length
   load times on top of the original script's load operations.

2. If something else could replace the value (like a scene's exported
   initialization), then preloading the value has no meaning. This point isn't
   a significant factor if one intends to always create the script on its own.

3. If one wishes only to 'import' another class resource (script or scene),
   then using a preloaded constant is often the best course of action. However,
   in exceptional cases, one may wish not to do this:

   1. If the 'imported' class is liable to change, then it should be a property
      instead, initialized either using an ``export`` or a ``load()`` (and
      perhaps not even initialized until later).

   2. If the script requires a great many dependencies, and one does not wish
      to consume so much memory, then one may wish to, load and unload various
      dependencies at runtime as circumstances change. If one preloads
      resources into constants, then the only way to unload these resources
      would be to unload the entire script. If they are instead loaded
      properties, then one can set them to ``null`` and remove all references
      to the resource entirely (which, as a
      :ref:`RefCounted <class_RefCounted>`-extending type, will cause the
      resources to delete themselves from memory).

Large levels: static vs. dynamic
--------------------------------

If one is creating a large level, which circumstances are most appropriate?
Should they create the level as one static space? Or should they load the
level in pieces and shift the world's content as needed?

Well, the simple answer is, "when the performance requires it." The
dilemma associated with the two options is one of the age-old programming
choices: does one optimize memory over speed, or vice versa?

The naive answer is to use a static level that loads everything at once.
But, depending on the project, this could consume a large amount of
memory. Wasting users' RAM leads to programs running slow or outright
crashing from everything else the computer tries to do at the same time.

No matter what, one should break larger scenes into smaller ones (to aid
in reusability of assets). Developers can then design a node that manages the
creation/loading and deletion/unloading of resources and nodes in real-time.
Games with large and varied environments or procedurally generated
elements often implement these strategies to avoid wasting memory.

On the flip side, coding a dynamic system is more complex, i.e. uses more
programmed logic, which results in opportunities for errors and bugs. If one
isn't careful, they can develop a system that bloats the technical debt of
the application.

As such, the best options would be...

1. To use a static level for smaller games.

2. If one has the time/resources on a medium/large game, create a library or
   plugin that can code the management of nodes and resources. If refined
   over time, so as to improve usability and stability, then it could evolve
   into a reliable tool across projects.

3. Code the dynamic logic for a medium/large game because one has the coding
   skills, but not the time or resources to refine the code (game's
   gotta get done). Could potentially refactor later to outsource the code
   into a plugin.

For an example of the various ways one can swap scenes around at runtime,
please see the :ref:`"Change scenes manually" <doc_change_scenes_manually>`
documentation.
