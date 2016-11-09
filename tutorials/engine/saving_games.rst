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

.. image:: /img/groups.png

Once this is done when we need to save the game we can get all objects
to save them and then tell them all to save with this script:

::

    var savenodes = get_tree().get_nodes_in_group("Persist")
        for i in savenodes:
        # Now we can call our save function on each node.

Serializing
-----------

The next step is to serialize the data. This makes it much easier to
read and store to disk. In this case, we're assuming each member of
group Persist is an instanced node and thus has a path. GDScript
has helper functions for this, such as :ref:`Dictionary.to_json()
<class_Dictionary_to_json>` and :ref:`Dictionary.parse_json()
<class_Dictionary_parse_json>`, so we will use a dictionary. Our node needs to
contain a save function that returns this data. The save function will look
like this:

::

    func save():
        var savedict = {
            filename=get_filename(),
            parent=get_parent().get_path(),
            posx=get_pos().x, #Vector2 is not supported by json
            posy=get_pos().y,
            attack=attack,
            defense=defense,
            currenthealth=currenthealth,
            maxhealth=maxhealth,
            damage=damage,
            regen=regen,
            experience=experience,
            TNL=TNL,
            level=level,
            AttackGrowth=AttackGrowth,
            DefenseGrowth=DefenseGrowth,
            HealthGrowth=HealthGrowth,
            isalive=isalive,
            last_attack=last_attack
        }
        return savedict

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

::

    # Note: This can be called from anywhere inside the tree.  This function is path independent.
    # Go through everything in the persist category and ask them to return a dict of relevant variables
    func save_game():
        var savegame = File.new()
        savegame.open("user://savegame.save", File.WRITE)
        var savenodes = get_tree().get_nodes_in_group("Persist")
        for i in savenodes:
            var nodedata = i.save()
            savegame.store_line(nodedata.to_json())
        savegame.close()

Game saved! Loading is fairly simple as well. For that we'll read each
line, use parse_json() to read it back to a dict, and then iterate over
the dict to read our values. But we'll need to first create the object
and we can use the filename and parent values to achieve that. Here is our
load function:

::

    # Note: This can be called from anywhere inside the tree.  This function is path independent.
    func load_game():
        var savegame = File.new()
        if !savegame.file_exists("user://savegame.save"):
            return #Error!  We don't have a save to load

        # We need to revert the game state so we're not cloning objects during loading.  This will vary wildly depending on the needs of a project, so take care with this step.
        # For our example, we will accomplish this by deleting savable objects.
        var savenodes = get_tree().get_nodes_in_group("Persist")
        for i in savenodes:
            i.queue_free()

        # Load the file line by line and process that dictionary to restore the object it represents
        var currentline = {} # dict.parse_json() requires a declared dict.
        savegame.open("user://savegame.save", File.READ)
        while (!savegame.eof_reached()):
            currentline.parse_json(savegame.get_line())
            # First we need to create the object and add it to the tree and set its position.
            var newobject = load(currentline["filename"]).instance()
            get_node(currentline["parent"]).add_child(newobject)
            newobject.set_pos(Vector2(currentline["posx"],currentline["posy"]))
            # Now we set the remaining variables.
            for i in currentline.keys():
                if (i == "filename" or i == "parent" or i == "posx" or i == "posy"):
                    continue
                newobject.set(i, currentline[i])
        savegame.close()

And now we can save and load an arbitrary number of objects laid out
almost anywhere across the scene tree! Each object can store different
data depending on what it needs to save.

Some notes
----------

We may have glossed over a step, but setting the game state to one fit
to start loading data can be very complicated. This step will need to be
heavily customized based on the needs of an individual project.

This implementation assumes no Persist objects are children of other
Persist objects. Doing so would create invalid paths. If this is one of
the needs of a project this needs to be considered. Saving objects in
stages (parent objects first) so they are available when child objects
are loaded will make sure they're available for the add_child() call.
There will also need to be some way to link children to parents as the
nodepath will likely be invalid.
