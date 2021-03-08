.. _doc_saving_with_json:

Saving with JSON
================

What is JSON?
-------------

JSON is a data-interchange format. That means that it is not
dependent on any language and can be used to send data between them.
JSON should be used to store data if it will be used with software
other than Godot.

Saving and reading data
-----------------------

Assuming that we already have every node we want to save data from
in a group and a function to serialize their data like in the
:ref:`doc_saving_games` tutorial, we can store that data in a JSON file.

As covered in the :ref:`doc_filesystem` tutorial, we'll need to open a file
so we can write to it or read from it. Let's use :ref:`to_json()
<class_@GDScript_method_to_json>` to convert it into an easily stored
string and store them in a file. Doing it this way ensures that each
line is its own object, so we have an easy way to pull the data out
of the file as well.

.. tabs::
 .. code-tab:: gdscript GDScript

    # Note: This can be called from anywhere inside the tree. This function is
    # path independent.
    # Go through everything in the persist category and ask them to return a
    # dict of relevant variables.
    func save_game():
        var save_game = File.new()
        save_game.open("user://savegame.save", File.WRITE)
        var save_nodes = get_tree().get_nodes_in_group("persist")
        for node in save_nodes:
            # Check the node is an instanced scene so it can be instanced again during load.
            if node.filename.empty():
                print("persistent node '%s' is not an instanced scene, skipped" % node.name)
                continue

            # Check the node has a save function.
            if !node.has_method("save"):
                print("persistent node '%s' is missing a save() function, skipped" % node.name)
                continue

            # Call the node's save function.
            var node_data = node.call("save")

            # Store the save dictionary as a new line in the save file.
            save_game.store_line(to_json(node_data))
        save_game.close()

 .. code-tab:: csharp

    // Note: This can be called from anywhere inside the tree. This function is
    // path independent.
    // Go through everything in the persist category and ask them to return a
    // dict of relevant variables.
    public void SaveGame()
    {
        var saveGame = new File();
        saveGame.Open("user://savegame.save", (int)File.ModeFlags.Write);

        var saveNodes = GetTree().GetNodesInGroup("persist");
        foreach (Node saveNode in saveNodes)
        {
            // Check the node is an instanced scene so it can be instanced again during load.
            if (saveNode.Filename.Empty())
            {
                GD.Print(String.Format("persistent node '{0}' is not an instanced scene, skipped", saveNode.Name));
                continue;
            }

            // Check the node has a save function.
            if (!saveNode.HasMethod("Save"))
            {
                GD.Print(String.Format("persistent node '{0}' is missing a Save() function, skipped", saveNode.Name));
                continue;
            }

            // Call the node's save function.
            var nodeData = saveNode.Call("Save");

            // Store the save dictionary as a new line in the save file.
            saveGame.StoreLine(JSON.Print(nodeData));
        }

        saveGame.Close();
    }


Game saved! Loading is fairly simple as well. For that, we'll read each
line, use parse_json() to read it back to a dict, and then iterate over
the dict to read our values. But we'll need to first create the object
and we can use the filename and parent values to achieve that. Here is our
load function:

.. note::

    :ref:`load()<class_@gdscript_method_load>` is a reserved function. Do not
    name the load function that.

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
        var save_nodes = get_tree().get_nodes_in_group("persist")
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
            for key in node_data.keys():
                if key == "filename" or key == "parent" or key == "pos_x" or key == "pos_y":
                    continue
                new_object.set(key, node_data[key])

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
        var saveNodes = GetTree().GetNodesInGroup("persist");
        foreach (Node saveNode in saveNodes)
            saveNode.QueueFree();

        // Load the file line by line and process that dictionary to restore the object
        // it represents.
        saveGame.Open("user://savegame.save", (int)File.ModeFlags.Read);

        while (saveGame.GetPosition() < saveGame.GetLen())
        {
            // Get the saved dictionary from the next line in the save file
            var nodeData = new Godot.Collections.Dictionary<string, object>((Godot.Collections.Dictionary)JSON.Parse(saveGame.GetLine()).Result);

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


Now we can store our save data in a format that is human-readable and can
also be used in other applications outside of Godot.
