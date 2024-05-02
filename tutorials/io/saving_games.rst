.. _doc_saving_games:

Saving games
============

Introduction
------------

Save games can be complicated. For example, it may be desirable
to store information from multiple objects across multiple levels.
Advanced save game systems should allow for additional information about
an arbitrary number of objects. This will allow the save function to
scale as the game grows more complex.

.. note::

    If you're looking to save user configuration, you can use the
    :ref:`class_ConfigFile` class for this purpose.

.. seealso::

    You can see how saving and loading works in action using the
    `Saving and Loading (Serialization) demo project <https://github.com/godotengine/godot-demo-projects/blob/master/loading/serialization>`__.

Identify persistent objects
---------------------------

Firstly, we should identify what objects we want to keep between game
sessions and what information we want to keep from those objects. For
this tutorial, we will use groups to mark and handle objects to be saved,
but other methods are certainly possible.

We will start by adding objects we wish to save to the "Persist" group. We can
do this through either the GUI or script. Let's add the relevant nodes using the
GUI:

.. image:: img/groups.png

Once this is done, when we need to save the game, we can get all objects
to save them and then tell them all to save with this script:

.. tabs::
 .. code-tab:: gdscript GDScript

    var save_nodes = get_tree().get_nodes_in_group("Persist")
    for node in save_nodes:
        # Now, we can call our save function on each node.

 .. code-tab:: csharp

    var saveNodes = GetTree().GetNodesInGroup("Persist");
    foreach (Node saveNode in saveNodes)
    {
        // Now, we can call our save function on each node.
    }


Serializing
-----------

The next step is to serialize the data. This makes it much easier to
read from and store to disk. In this case, we're assuming each member of
group Persist is an instanced node and thus has a path. GDScript
has helper class :ref:`JSON<class_json>` to convert between dictionary and string,
Our node needs to contain a save function that returns this data.
The save function will look like this:

.. tabs::
 .. code-tab:: gdscript GDScript

    func save():
        var save_dict = {
            "filename" : get_scene_file_path(),
            "parent" : get_parent().get_path(),
            "pos_x" : position.x, # Vector2 is not supported by JSON
            "pos_y" : position.y,
            "attack" : attack,
            "defense" : defense,
            "current_health" : current_health,
            "max_health" : max_health,
            "damage" : damage,
            "regen" : regen,
            "experience" : experience,
            "tnl" : tnl,
            "level" : level,
            "attack_growth" : attack_growth,
            "defense_growth" : defense_growth,
            "health_growth" : health_growth,
            "is_alive" : is_alive,
            "last_attack" : last_attack
        }
        return save_dict

 .. code-tab:: csharp

    public Godot.Collections.Dictionary<string, Variant> Save()
    {
        return new Godot.Collections.Dictionary<string, Variant>()
        {
            { "Filename", SceneFilePath },
            { "Parent", GetParent().GetPath() },
            { "PosX", Position.X }, // Vector2 is not supported by JSON
            { "PosY", Position.Y },
            { "Attack", Attack },
            { "Defense", Defense },
            { "CurrentHealth", CurrentHealth },
            { "MaxHealth", MaxHealth },
            { "Damage", Damage },
            { "Regen", Regen },
            { "Experience", Experience },
            { "Tnl", Tnl },
            { "Level", Level },
            { "AttackGrowth", AttackGrowth },
            { "DefenseGrowth", DefenseGrowth },
            { "HealthGrowth", HealthGrowth },
            { "IsAlive", IsAlive },
            { "LastAttack", LastAttack }
        };
    }


This gives us a dictionary with the style
``{ "variable_name":value_of_variable }``, which will be useful when
loading.

Saving and reading data
-----------------------

As covered in the :ref:`doc_filesystem` tutorial, we'll need to open a file
so we can write to it or read from it. Now that we have a way to
call our groups and get their relevant data, let's use the class :ref:`JSON<class_json>` to
convert it into an easily stored string and store them in a file. Doing
it this way ensures that each line is its own object, so we have an easy
way to pull the data out of the file as well.

.. tabs::
 .. code-tab:: gdscript GDScript

    # Note: This can be called from anywhere inside the tree. This function is
    # path independent.
    # Go through everything in the persist category and ask them to return a
    # dict of relevant variables.
    func save_game():
        var save_file = FileAccess.open("user://savegame.save", FileAccess.WRITE)
        var save_nodes = get_tree().get_nodes_in_group("Persist")
        for node in save_nodes:
            # Check the node is an instanced scene so it can be instanced again during load.
            if node.scene_file_path.is_empty():
                print("persistent node '%s' is not an instanced scene, skipped" % node.name)
                continue

            # Check the node has a save function.
            if !node.has_method("save"):
                print("persistent node '%s' is missing a save() function, skipped" % node.name)
                continue

            # Call the node's save function.
            var node_data = node.call("save")

            # JSON provides a static method to serialized JSON string.
            var json_string = JSON.stringify(node_data)

            # Store the save dictionary as a new line in the save file.
            save_file.store_line(json_string)

 .. code-tab:: csharp

    // Note: This can be called from anywhere inside the tree. This function is
    // path independent.
    // Go through everything in the persist category and ask them to return a
    // dict of relevant variables.
    public void SaveGame()
    {
        using var saveFile = FileAccess.Open("user://savegame.save", FileAccess.ModeFlags.Write);

        var saveNodes = GetTree().GetNodesInGroup("Persist");
        foreach (Node saveNode in saveNodes)
        {
            // Check the node is an instanced scene so it can be instanced again during load.
            if (string.IsNullOrEmpty(saveNode.SceneFilePath))
            {
                GD.Print($"persistent node '{saveNode.Name}' is not an instanced scene, skipped");
                continue;
            }

            // Check the node has a save function.
            if (!saveNode.HasMethod("Save"))
            {
                GD.Print($"persistent node '{saveNode.Name}' is missing a Save() function, skipped");
                continue;
            }

            // Call the node's save function.
            var nodeData = saveNode.Call("Save");

            // Json provides a static method to serialized JSON string.
            var jsonString = Json.Stringify(nodeData);

            // Store the save dictionary as a new line in the save file.
            saveFile.StoreLine(jsonString);
        }
    }


Game saved! Now, to load, we'll read each
line. Use the :ref:`parse<class_JSON_method_parse>` method to read the
JSON string back to a dictionary, and then iterate over
the dict to read our values. But we'll need to first create the object
and we can use the filename and parent values to achieve that. Here is our
load function:

.. tabs::
 .. code-tab:: gdscript GDScript

    # Note: This can be called from anywhere inside the tree. This function
    # is path independent.
    func load_game():
        if not FileAccess.file_exists("user://savegame.save"):
            return # Error! We don't have a save to load.

        # We need to revert the game state so we're not cloning objects
        # during loading. This will vary wildly depending on the needs of a
        # project, so take care with this step.
        # For our example, we will accomplish this by deleting saveable objects.
        var save_nodes = get_tree().get_nodes_in_group("Persist")
        for i in save_nodes:
            i.queue_free()

        # Load the file line by line and process that dictionary to restore
        # the object it represents.
        var save_file = FileAccess.open("user://savegame.save", FileAccess.READ)
        while save_file.get_position() < save_file.get_length():
            var json_string = save_file.get_line()

            # Creates the helper class to interact with JSON
            var json = JSON.new()

            # Check if there is any error while parsing the JSON string, skip in case of failure
            var parse_result = json.parse(json_string)
            if not parse_result == OK:
                print("JSON Parse Error: ", json.get_error_message(), " in ", json_string, " at line ", json.get_error_line())
                continue

            # Get the data from the JSON object
            var node_data = json.get_data()

            # Firstly, we need to create the object and add it to the tree and set its position.
            var new_object = load(node_data["filename"]).instantiate()
            get_node(node_data["parent"]).add_child(new_object)
            new_object.position = Vector2(node_data["pos_x"], node_data["pos_y"])

            # Now we set the remaining variables.
            for i in node_data.keys():
                if i == "filename" or i == "parent" or i == "pos_x" or i == "pos_y":
                    continue
                new_object.set(i, node_data[i])

 .. code-tab:: csharp

    // Note: This can be called from anywhere inside the tree. This function is
    // path independent.
    public void LoadGame()
    {
        if (!FileAccess.FileExists("user://savegame.save"))
        {
            return; // Error! We don't have a save to load.
        }

        // We need to revert the game state so we're not cloning objects during loading.
        // This will vary wildly depending on the needs of a project, so take care with
        // this step.
        // For our example, we will accomplish this by deleting saveable objects.
        var saveNodes = GetTree().GetNodesInGroup("Persist");
        foreach (Node saveNode in saveNodes)
        {
            saveNode.QueueFree();
        }

        // Load the file line by line and process that dictionary to restore the object
        // it represents.
        using var saveFile = FileAccess.Open("user://savegame.save", FileAccess.ModeFlags.Read);

        while (saveFile.GetPosition() < saveFile.GetLength())
        {
            var jsonString = saveFile.GetLine();

            // Creates the helper class to interact with JSON
            var json = new Json();
            var parseResult = json.Parse(jsonString);
            if (parseResult != Error.Ok)
            {
                GD.Print($"JSON Parse Error: {json.GetErrorMessage()} in {jsonString} at line {json.GetErrorLine()}");
                continue;
            }

            // Get the data from the JSON object
            var nodeData = new Godot.Collections.Dictionary<string, Variant>((Godot.Collections.Dictionary)json.Data);

            // Firstly, we need to create the object and add it to the tree and set its position.
            var newObjectScene = GD.Load<PackedScene>(nodeData["Filename"].ToString());
            var newObject = newObjectScene.Instantiate<Node>();
            GetNode(nodeData["Parent"].ToString()).AddChild(newObject);
            newObject.Set(Node2D.PropertyName.Position, new Vector2((float)nodeData["PosX"], (float)nodeData["PosY"]));

            // Now we set the remaining variables.
            foreach (var (key, value) in nodeData)
            {
                if (key == "Filename" || key == "Parent" || key == "PosX" || key == "PosY")
                {
                    continue;
                }
                newObject.Set(key, value);
            }
        }
    }


Now we can save and load an arbitrary number of objects laid out
almost anywhere across the scene tree! Each object can store different
data depending on what it needs to save.

Some notes
----------

We have glossed over setting up the game state for loading. It's ultimately up
to the project creator where much of this logic goes.
This is often complicated and will need to be heavily
customized based on the needs of the individual project.

Additionally, our implementation assumes no Persist objects are children of other
Persist objects. Otherwise, invalid paths would be created. To
accommodate nested Persist objects, consider saving objects in stages.
Load parent objects first so they are available for the :ref:`add_child()
<class_node_method_add_child>`
call when child objects are loaded. You will also need a way to link
children to parents as the :ref:`NodePath
<class_nodepath>` will likely be invalid.

JSON vs binary serialization
----------------------------

For simple game state, JSON may work and it generates human-readable files that are easy to debug.

But JSON has many limitations. If you need to store more complex game state or
a lot of it, :ref:`binary serialization<doc_binary_serialization_api>`
may be a better approach.

JSON limitations
~~~~~~~~~~~~~~~~

Here are some important gotchas to know about when using JSON.

* **Filesize:**
  JSON stores data in text format, which is much larger than binary formats.
* **Data types:**
  JSON only offers a limited set of data types. If you have data types
  that JSON doesn't have, you will need to translate your data to and
  from types that JSON can handle. For example, some important types that JSON
  can't parse are: ``Vector2``, ``Vector3``, ``Color``, ``Rect2``, and ``Quaternion``.
* **Custom logic needed for encoding/decoding:**
  If you have any custom classes that you want to store with JSON, you will
  need to write your own logic for encoding and decoding those classes.

Binary serialization
~~~~~~~~~~~~~~~~~~~~

:ref:`Binary serialization<doc_binary_serialization_api>` is an alternative
approach for storing game state, and you can use it with the functions
``get_var`` and ``store_var`` of :ref:`class_FileAccess`.

* Binary serialization should produce smaller files than JSON.
* Binary serialization can handle most common data types.
* Binary serialization requires less custom logic for encoding and decoding
  custom classes.

Note that not all properties are included. Only properties that are configured
with the :ref:`PROPERTY_USAGE_STORAGE<class_@GlobalScope_constant_PROPERTY_USAGE_STORAGE>`
flag set will be serialized. You can add a new usage flag to a property by overriding the
:ref:`_get_property_list<class_Object_private_method__get_property_list>`
method in your class. You can also check how property usage is configured by
calling ``Object._get_property_list``.
See :ref:`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>` for the
possible usage flags.
