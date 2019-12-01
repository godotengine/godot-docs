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

Identify persistent objects
---------------------------

Firstly, we should identify what objects we want to keep between game
sessions and what information we want to keep from those objects. For
this tutorial, we will use groups to mark and handle objects to be saved,
but other methods are certainly possible.

We will start by adding objects we wish to save to the "Persist" group.
As in the :ref:`doc_scripting_continued` tutorial, we can do this through
either the GUI or script. Let's add the relevant nodes using the GUI:

.. image:: img/groups.png

Once this is done, when we need to save the game, we can get all objects
to save them and then tell them all to save with this script:

.. tabs::
 .. code-tab:: gdscript GDScript

    var save_nodes = get_tree().get_nodes_in_group("Persist")
    for i in save_nodes:
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
has helper functions for this, such as :ref:`to_json()
<class_@GDScript_method_to_json>` and :ref:`parse_json()
<class_@GDScript_method_parse_json>`, so we will use a dictionary. Our node needs to
contain a save function that returns this data. The save function will look
like this:

.. tabs::
 .. code-tab:: gdscript GDScript

    func save():
        var save_dict = {
            "filename" : get_filename(),
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

    public Godot.Collections.Dictionary<string, object> Save()
    {
        return new Godot.Collections.Dictionary<string, object>()
        {
            { "Filename", GetFilename() },
            { "Parent", GetParent().GetPath() },
            { "PosX", Position.x }, // Vector2 is not supported by JSON
            { "PosY", Position.y },
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
call our groups and get their relevant data, let's use :ref:`to_json()
<class_@GDScript_method_to_json>` to
convert it into an easily stored string and store them in a file. Doing
it this way ensures that each line is its own object, so we have an easy
way to pull the data out of the file as well.

.. tabs::
 .. code-tab:: gdscript GDScript

    # Note: This can be called from anywhere inside the tree. This function is
    # path independent.
    # Go through everything in the persist category and ask them to return a
    # dict of relevant variables
    func save_game():
        var save_game = File.new()
        save_game.open("user://savegame.save", File.WRITE)
        var save_nodes = get_tree().get_nodes_in_group("Persist")
        for node in save_nodes:
            # Check the node is an instanced scene so it can be instanced again during load
            if node.filename.empty():
                print("persistent node '%s' is not an instanced scene, skipped" % node.name)
                continue

            # Check the node has a save function
            if !node.has_method("save"):
                print("persistent node '%s' is missing a save() function, skipped" % node.name)
                continue

            # Call the node's save function
            var node_data = node.call("save")

            # Store the save dictionary as a new line in the save file
            save_game.store_line(to_json(node_data))
        save_game.close()

 .. code-tab:: csharp

    // Note: This can be called from anywhere inside the tree. This function is
    // path independent.
    // Go through everything in the persist category and ask them to return a
    // dict of relevant variables
    public void SaveGame()
    {
        var saveGame = new File();
        saveGame.Open("user://savegame.save", (int)File.ModeFlags.Write);

        var saveNodes = GetTree().GetNodesInGroup("Persist");
        foreach (Node saveNode in saveNodes)
        {
            // Check the node is an instanced scene so it can be instanced again during load
            if (saveNode.Filename.Empty())
            {
                GD.Print(String.Format("persistent node '{0}' is not an instanced scene, skipped", saveNode.Name));
                continue;
            }

            // Check the node has a save function
            if (!saveNode.HasMethod("Save"))
            {
                GD.Print(String.Format("persistent node '{0}' is missing a Save() function, skipped", saveNode.Name));
                continue;
            }

            // Call the node's save function
            var nodeData = saveNode.Call("Save");

            // Store the save dictionary as a new line in the save file
            saveGame.StoreLine(JSON.Print(nodeData));
        }

        saveGame.Close();
    }


Game saved! Loading is fairly simple as well. For that, we'll read each
line, use parse_json() to read it back to a dict, and then iterate over
the dict to read our values. But we'll need to first create the object
and we can use the filename and parent values to achieve that. Here is our
load function:

.. tabs::
 .. code-tab:: gdscript GDScript

    # Note: This can be called from anywhere inside the tree. This function
    # is path independent.
    func load_game():
        var save_game = File.new()
        if not save_game.file_exists("user://savegame.save"):
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
        save_game.open("user://savegame.save", File.READ)
        while save_game.get_position() < save_game.get_len():
            # Get the saved dictionary from the next line in the save file
            var node_data = parse_json(save_game.get_line())

            # Firstly, we need to create the object and add it to the tree and set its position.
            var new_object = load(node_data["filename"]).instance()
            get_node(node_data["parent"]).add_child(new_object)
            new_object.position = Vector2(node_data["pos_x"], node_data["pos_y"])

            # Now we set the remaining variables.
            for i in node_data.keys():
                if i == "filename" or i == "parent" or i == "pos_x" or i == "pos_y":
                    continue
                new_object.set(i, node_data[i])
        save_game.close()

 .. code-tab:: csharp

    // Note: This can be called from anywhere inside the tree. This function is
    // path independent.
    public void LoadGame()
    {
        var saveGame = new File();
        if (!saveGame.FileExists("user://savegame.save"))
            return; // Error!  We don't have a save to load.

        // We need to revert the game state so we're not cloning objects during loading.
        // This will vary wildly depending on the needs of a project, so take care with
        // this step.
        // For our example, we will accomplish this by deleting saveable objects.
        var saveNodes = GetTree().GetNodesInGroup("Persist");
        foreach (Node saveNode in saveNodes)
            saveNode.QueueFree();

        // Load the file line by line and process that dictionary to restore the object
        // it represents.
        saveGame.Open("user://savegame.save", (int)File.ModeFlags.Read);

        while (saveGame.GetPosition() < save_game.GetLen())
        {
            // Get the saved dictionary from the next line in the save file
            var nodeData = (Godot.Collections.Dictionary<string, object>)JSON.Parse(saveGame.GetLine()).Result;

            // Firstly, we need to create the object and add it to the tree and set its position.
            var newObjectScene = (PackedScene)ResourceLoader.Load(nodeData["Filename"].ToString());
            var newObject = (Node)newObjectScene.Instance();
            GetNode(nodeData["Parent"].ToString()).AddChild(newObject);
            newObject.Set("Position", new Vector2((float)nodeData["PosX"], (float)nodeData["PosY"]));

            // Now we set the remaining variables.
            foreach (KeyValuePair<object, object> entry in nodeData)
            {
                string key = entry.Key.ToString();
                if (key == "Filename" || key == "Parent" || key == "PosX" || key == "PosY")
                    continue;
                newObject.Set(key, entry.Value);
            }
        }

        saveGame.Close();
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
