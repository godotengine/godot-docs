.. _doc_saving_games:

Saving games
============

Introduction
------------

Save games can be complicated. It can be desired to store more
information than the current level or number of stars earned on a level.
More advanced save games may need to store additional information about
an arbitrary number of objects. This will allow the save function to
scale as the game grows more complex.

Identify persistent objects
---------------------------

First we should identify what objects we want to keep between game
sessions and what information we want to keep from those objects. For
this tutorial, we will use groups to mark and handle objects to be saved
but other methods are certainly possible.

We will start by adding objects we wish to save to the "Persist" group.
As in the :ref:`doc_scripting_continued` tutorial, we can do this through
the GUI or through script. Let's add the relevant nodes using the GUI:

.. image:: img/groups.png

Once this is done when we need to save the game we can get all objects
to save them and then tell them all to save with this script:

.. tabs::
 .. code-tab:: gdscript GDScript

    var save_nodes = get_tree().get_nodes_in_group("Persist")
    for i in save_nodes:
        # Now we can call our save function on each node.

 .. code-tab:: csharp

    var saveNodes = GetTree().GetNodesInGroup("Persist");
    foreach (Node saveNode in saveNodes)
    {
        // Now we can call our save function on each node.
    }


Serializing
-----------

The next step is to serialize the data. This makes it much easier to
read and store to disk. In this case, we're assuming each member of
group Persist is an instanced node and thus has a path. GDScript
has helper functions for this, such as :ref:`to_json()
<class_@GDScript_to_json>` and :ref:`parse_json()
<class_@GDScript_parse_json>`, so we will use a dictionary. Our node needs to
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

    public Dictionary<object, object> Save()
    {
        return new Dictionary<object, object>()
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
``{ "variable_name":that_variables_value }`` which will be useful when
loading.

Saving and reading data
-----------------------

As covered in the :ref:`doc_filesystem` tutorial, we'll need to open a file
and write to it and then later read from it. Now that we have a way to
call our groups and get their relevant data, let's use to_json() to
convert it into an easily stored string and store them in a file. Doing
it this way ensures that each line is its own object so we have an easy
way to pull the data out of the file as well.

.. tabs::
 .. code-tab:: gdscript GDScript

    # Note: This can be called from anywhere inside the tree.  This function is path independent.
    # Go through everything in the persist category and ask them to return a dict of relevant variables
    func save_game():
        var save_game = File.new()
        save_game.open("user://savegame.save", File.WRITE)
        var save_nodes = get_tree().get_nodes_in_group("Persist")
        for i in save_nodes:
            var node_data = i.call("save");
            save_game.store_line(to_json(node_data))
        save_game.close()

 .. code-tab:: csharp

    // Note: This can be called from anywhere inside the tree.  This function is path independent.
    // Go through everything in the persist category and ask them to return a dict of relevant variables
    public void SaveGame()
    {
        var saveGame = new File();
        saveGame.Open("user://savegame.save", (int)File.ModeFlags.Write);

        var saveNodes = GetTree().GetNodesInGroup("Persist");
        foreach (Node saveNode in saveNodes)
        {
            var nodeData = saveNode.Call("Save");
            saveGame.StoreLine(JSON.Print(nodeData));
        }

        saveGame.Close();
    }


Game saved! Loading is fairly simple as well. For that we'll read each
line, use parse_json() to read it back to a dict, and then iterate over
the dict to read our values. But we'll need to first create the object
and we can use the filename and parent values to achieve that. Here is our
load function:

.. tabs::
 .. code-tab:: gdscript GDScript

    # Note: This can be called from anywhere inside the tree. This function is path independent.
    func load_game():
        var save_game = File.new()
        if not save_game.file_exists("user://save_game.save"):
            return # Error! We don't have a save to load.

        # We need to revert the game state so we're not cloning objects during loading. This will vary wildly depending on the needs of a project, so take care with this step.
        # For our example, we will accomplish this by deleting savable objects.
        var save_nodes = get_tree().get_nodes_in_group("Persist")
        for i in save_nodes:
            i.queue_free()

        # Load the file line by line and process that dictionary to restore the object it represents
        save_game.open("user://savegame.save", File.READ)
        while not save_game.eof_reached():
            var current_line = parse_json(save_game.get_line())
            # First we need to create the object and add it to the tree and set its position.
            var new_object = load(current_line["filename"]).instance()
            get_node(current_line["parent"]).add_child(new_object)
            new_object.position = Vector2(current_line["pos_x"], current_line["pos_y"]))
            # Now we set the remaining variables.
            for i in current_line.keys():
                if i == "filename" or i == "parent" or i == "pos_x" or i == "pos_y":
                    continue
                new_object.set(i, current_line[i])
        save_game.close()

 .. code-tab:: csharp

    // Note: This can be called from anywhere inside the tree.  This function is path independent.
    public void LoadGame()
    {
        var saveGame = new File();
        if (!saveGame.FileExists("user://savegame.save"))
            return; // Error!  We don't have a save to load.

        // We need to revert the game state so we're not cloning objects during loading.  This will vary wildly depending on the needs of a project, so take care with this step.
        // For our example, we will accomplish this by deleting savable objects.
        var saveNodes = GetTree().GetNodesInGroup("Persist");
        foreach (Node saveNode in saveNodes)
            saveNode.QueueFree();

        // Load the file line by line and process that dictionary to restore the object it represents
        saveGame.Open("user://savegame.save", (int)File.ModeFlags.Read);

        while (!saveGame.EofReached())
        {
            var currentLine = (Dictionary<object, object>)JSON.Parse(saveGame.GetLine()).Result;
            if (currentLine == null)
                continue;

            // First we need to create the object and add it to the tree and set its position.
            var newObjectScene = (PackedScene)ResourceLoader.Load(currentLine["Filename"].ToString());
            var newObject = (Node)newObjectScene.Instance();
            GetNode(currentLine["Parent"].ToString()).AddChild(newObject);
            newObject.Set("Position", new Vector2((float)currentLine["PosX"], (float)currentLine["PosY"]));

            // Now we set the remaining variables.
            foreach (KeyValuePair<object, object> entry in currentLine)
            {
                string key = entry.Key.ToString();
                if (key == "Filename" || key == "Parent" || key == "PosX" || key == "PosY")
                    continue;
                newObject.Set(key, entry.Value);
            }
        }

        saveGame.Close();
    }


And now we can save and load an arbitrary number of objects laid out
almost anywhere across the scene tree! Each object can store different
data depending on what it needs to save.

Some notes
----------

We may have glossed over a step, but setting the game state to one fit
to start loading data can be complicated. This step will need to be
heavily customized based on the needs of an individual project.

This implementation assumes no Persist objects are children of other
Persist objects. Doing so would create invalid paths. If this is one of
the needs of a project this needs to be considered. Saving objects in
stages (parent objects first) so they are available when child objects
are loaded will make sure they're available for the add_child() call.
There will also need to be some way to link children to parents as the
NodePath will likely be invalid.
