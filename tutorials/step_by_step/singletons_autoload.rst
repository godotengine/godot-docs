.. _doc_singletons_autoload:

Singletons (AutoLoad)
=====================

Introduction
------------

Scene Singletons are very useful things, as they represent a very common
use case, but it's not clear at the beginning where their value is.

The scene system is very useful, but by itself it has a few drawbacks:

-  There is no "common" place to store information (such as core, items
   obtained, etc) between two scenes.
-  It is possible to make a scene that loads other scenes as children
   and frees them, while keeping that information, but then if that is
   done, it's not possible to run a scene alone by itself and expect it
   to work
-  It is also possible to store persistent information to disk in
   \`user://\` and have scenes always load it, but saving/loading that
   while changing scenes is cumbersome.

So, after using Godot for a while, it becomes clear that it is necessary
to have parts of a scene that:

-  Are always loaded, no matter which scene is opened from the editor.
-  Can keep global variables, such as player information, items, money,
   etc.
-  Can handle switching of scenes and transitions.
-  Just have something that acts like a singleton, since GDScript does
   not support global variables by design.

For this, the option for auto-loading nodes and scripts exists.

AutoLoad
--------

AutoLoad can be a scene, or a script that inherits from Node (a Node
will be created and the script will be set to it). They are added to the
project in the Scene > Project Settings > AutoLoad tab.

Each autoload needs a name, this name will be the node name, and the
node will be always added to the root viewport before any scene is
loaded.

.. image:: /img/singleton.png

This means, that a for a singleton named "playervariables", any node can
access it by requesting:

::

    var player_vars = get_node("/root/playervariables")

Custom scene switcher
---------------------

This short tutorial will explain how to make a scene switcher by using
autoload. For simple scene switching, the
:ref:`SceneTree.change_scene() <class_SceneTree_change_scene>`
method suffices (described in :ref:`doc_scene_tree`), so this method is for
more complex behaviors when switching scenes.

First download the template from here:
:download:`autoload.zip </files/autoload.zip>`, then open it.

Two scenes are present, scene_a.scn and scene_b.scn on an otherwise
empty project. Each are identical and contain a button connected to a
callback for going to the opposite scene. When the project runs, it
starts in scene_a.scn. However, this does nothing and pressing the
button does not work.

global.gd
---------

First of all, create a global.gd script. The easier way to create a
resource from scratch is from the resources tab:

.. image:: /img/newscript.png

Save the script to a file global.gd:

.. image:: /img/saveasscript.png

The script should be opened in the script editor. Next step will be
adding it to autoload, for this, go to: Scene [STRIKEOUT:> Project
Settings]> AutoLoad and add a new autoload with name "global" that
points to this file:

.. image:: /img/addglobal.png

Now, when any scene is run, the script will be always loaded.

So, going back to it, In the _ready() function, the current scene
will be fetched. Both the current scene and global.gd are children of
root, but the autoloaded nodes are always first. This means that the
last child of root is always the loaded scene.

Also, make sure that global.gd extends from Node, otherwise it won't be
loaded.

::

    extends Node

    var current_scene = null

    func _ready():
            var root = get_tree().get_root()
            current_scene = root.get_child( root.get_child_count() -1 )

Next, is the function for changing scene. This function will erase the
current scene and replace it by the requested one.

::

    func goto_scene(path):

        # This function will usually be called from a signal callback,
        # or some other function from the running scene.
        # Deleting the current scene at this point might be
        # a bad idea, because it may be inside of a callback or function of it.
        # The worst case will be a crash or unexpected behavior.

        # The way around this is deferring the load to a later time, when
        # it is ensured that no code from the current scene is running:

        call_deferred("_deferred_goto_scene",path)


    func _deferred_goto_scene(path):

        # Immediately free the current scene,
        # there is no risk here.    
        current_scene.free()

        # Load new scene
        var s = ResourceLoader.load(path)

        # Instance the new scene
        current_scene = s.instance()

        # Add it to the active scene, as child of root
        get_tree().get_root().add_child(current_scene)

        # optional, to make it compatible with the SceneTree.change_scene() API
        get_tree().set_current_scene( current_scene )

As mentioned in the comments above, we really want to avoid the
situation of having the current scene being deleted while being used
(code from functions of it being run), so using
:ref:`Object.call_deferred() <class_Object_call_deferred>`
is desired at this point. The result is that execution of the commands
in the second function will happen at an immediate later time when no
code from the current scene is running.

Finally, all that is left is to fill the empty functions in scene_a.gd
and scene_b.gd:

::

    #add to scene_a.gd

    func _on_goto_scene_pressed():
            get_node("/root/global").goto_scene("res://scene_b.scn")

and

::

    #add to scene_b.gd

    func _on_goto_scene_pressed():
            get_node("/root/global").goto_scene("res://scene_a.scn")

Finally, by running the project it's possible to switch between both
scenes by pressing the button!

(To load scenes with a progress bar, check out the next tutorial,
:ref:`doc_background_loading`)
