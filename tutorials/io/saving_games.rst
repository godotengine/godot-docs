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

Identify persistent objects
---------------------------

Firstly, we should identify what objects we want to keep between game
sessions and what information we want to keep from those objects. For
this tutorial, we will use groups to mark and handle objects to be saved,
but other methods are certainly possible.

We will start by adding objects we wish to save to the "persist" group. We can
do this through either the GUI or script. Let's add the relevant nodes using the
GUI:

.. image:: img/groups.png

.. tabs::
 .. code-tab:: gdscript GDScript

    var save_nodes = get_tree().get_nodes_in_group("persist")
    for i in save_nodes:
        # Now, we can call our save function on each node.

 .. code-tab:: csharp

    Godot.Collections.Array saveNodes = GetTree().GetNodesInGroup("persist");
    foreach (Node saveNode in saveNodes)
    {
        // Now, we can call our save function on each node.
    }


Serializing
-----------

The next step is to serialize the data. This makes it much easier to
read from and store to disk. In this case, we're assuming each member of
group persist is an instanced node and thus has a path. We will use a dictionary
for serialization. Our node needs to contain a save function that returns
this data. The save function will look like this:

.. tabs::
 .. code-tab:: gdscript GDScript

    func save():
        var save_dict = {
            "name": name,
            "filename": Filename,
            "parent": get_parent().get_path(),
            "pos": position,
            "current_health": current_health,
            "experience": experience,
            "level": level,
            "is_alive": is_alive,
        }
        return save_dict

 .. code-tab:: csharp

    public Godot.Collections.Dictionary<string, object> Save()
    {
        return new Godot.Collections.Dictionary<string, object>()
        {
            { "Name", Name },
            { "Filename", GetFilename() },
            { "Parent", GetParent().GetPath() },
            { "Pos", Position },
            { "CurrentHealth", CurrentHealth },
            { "Experience", Experience },
            { "Level", Level },
            { "IsAlive", IsAlive },
        };
    }


This gives us a dictionary with the style
``{ "variable_name": value_of_variable }``, which will be useful when
loading.

Saving and reading data
-----------------------

Now that we have a way to call our groups and get their relevant data,
let's use :ref:`ConfigFile.set_value()<class_configfile_method_set_value>`
to store them in a file.

.. tabs::
 .. code-tab:: gdscript GDScript
    
    # Note: This can be called from anywhere inside the tree. This function is
    # path independent.
    # Go through everything in the persist category and ask them to return a
    # dict of relevant variables.
    func save_game():
        var save_game = ConfigFile.new()
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

            # Iterates through save dict and stores each key-value pair under the node's name's section
            for key in node_data:
                save_game.set_value(node_data["name"], key, node_data[key])
        save_game.save("user://savegame.save")
    
 .. code-tab:: csharp

    // Note: This can be called from anywhere inside the tree. This function is
    // path independent.
    // Go through everything in the persist category and ask them to return a
    // dict of relevant variables.
    public void SaveGame()
    {
        var saveGame = new ConfigFile();

        Godot.Collections.Array saveNodes = GetTree().GetNodesInGroup("persist");
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
            var nodeData = (Godot.Collections.Dictionary)saveNode.Call("Save");

            // Iterates through save dict and stores each key-value pair under the node's name's section
            foreach (string key in nodeData.Keys)
            {
                saveGame.SetValue(NodeData["name"], Key, NodeData[Key]);
            }
            saveGame.Save("user://savegame.save");
        }
    }


Game saved! Loading is fairly simple as well. For that, we'll use a nested
for loop to get each dictionary and then iterate over the dict to read our values.
But we'll need to first create the object using the filename and parent values.
Here is our load function:

.. note::

    :ref:`load()<class_@gdscript_method_load>` is a reserved function. Do not
    name your load function that.

.. tabs::
 .. code-tab:: gdscript GDScript

    # Note: This can be called from anywhere inside the tree. This function
    # is path independent.
    func load_game():
        var save_game = ConfigFile.new()
        var err = save_game.load("user://savegame.save"):
        if not err == OK:
            return # Error! We don't have a save to load.

        # We need to revert the game state so we're not cloning objects
        # during loading. This will vary wildly depending on the needs of a
        # project, so take care with this step.
        # For our example, we will accomplish this by deleting saveable objects.
        var save_nodes = get_tree().get_nodes_in_group("persist")
        for node in save_nodes:
            node.queue_free()

        # Process each section in the file to restore the object it represents.
        for section in save_game.get_sections():
            var node_data = {}
            # Adds each key in the section to the dictionary.
            for key in save_game.get_section_keys(section):
                node_data[key] = save_game.get_value(section, key)

            # Firstly, we need to create the object and add it to the tree and set its position.
            var new_object = load(node_data["filename"]).instance()
            get_node(node_data["parent"]).add_child(new_object)
            new_object.position = node_data["pos"]

            # Now we set the remaining variables.
            for key in node_data.keys():
                if key == "filename" or key == "parent" or key == "pos":
                    continue
                new_object.set(key, node_data[key])


 .. code-tab:: csharp

    // Note: This can be called from anywhere inside the tree. This function is
    // path independent.
    public void LoadGame()
    {
        var saveGame = new ConfigFile();
        var err = saveGame.Load("user://savegame.save");
        if (err != Error.Ok)
        {
            return ; // Error! We don't have a save to load.
        }

        // We need to revert the game state so we're not cloning objects during loading.
        // This will vary wildly depending on the needs of a project, so take care with
        // this step.
        // For our example, we will accomplish this by deleting saveable objects.
        var saveNodes = GetTree().GetNodesInGroup("Persist");
        foreach (Node saveNode in saveNodes)
            saveNode.QueueFree();

        // Process each section in the file to restore the object it represents.
        foreach (var Section in SaveGame.GetSections())
        {
            var nodeData = {};
            // Adds each key in the section to the dictionary.
            foreach (var Key in SaveGame.GetSectionKeys(Section))
            {
                nodeData[Key] = SaveGame.GetValue(Section, Key);
            }

        {
            // Firstly, we need to create the object and add it to the tree and set its position.
            var newObjectScene = (PackedScene)ResourceLoader.Load(nodeData["Filename"].ToString());
            var newObject = (Node)newObjectScene.Instance();
            GetNode(nodeData["Parent"].ToString()).AddChild(newObject);
            newObject.Set("Position", nodeData["Pos"]));

            // Now we set the remaining variables.
            foreach (KeyValuePair<string, object> entry in nodeData)
            {
                if (entry.Key == "Filename" || entry.Key == "Parent" || entry.Key == "Pos")
                {
                    continue;
                }
                newObject.Set(entry.Key, entry.Value);
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

Additionally, our implementation assumes no persist objects are children of other
persist objects. Otherwise, invalid paths would be created. To
accommodate nested persist objects, consider saving objects in stages.
Load parent objects first so they are available for the :ref:`add_child()
<class_node_method_add_child>`
call when child objects are loaded. You will also need a way to link
children to parents as the :ref:`NodePath
<class_nodepath>` will likely be invalid.

ConfigFile is only one way to save. :ref:`File.store_var()
<class_file_method_store_var>` can also be used to store any value with Godot's
built-in serialization. It's also possible to store data with JSON files
if one is planning on using the files with other software. See
:ref:`doc_saving_with_json` for more information.
