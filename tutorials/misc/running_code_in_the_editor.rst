.. _doc_running_code_in_the_editor:

Running code in the editor
==========================

What is ``tool``?
-----------------

``tool`` is a powerful line of code that, when added at the top of your script, makes it execute in the editor. You can also decide which parts of the script execute in the editor, which in game, and which in both.

You can use it for doing many things, but it is mostly useful in level design for visually presenting things that are hard to predict ourselves. Here are some use cases:

- If you have a cannon that shoots cannonballs affected by physics (gravity), you can draw cannonball's trajectory in the editor, making level design a lot easier.
- If you have jumppads with varying jump heights, you can draw the maximum jump height a player would reach if it jumped on one, also making level design easier.
- If your player doesn't use a sprite, but draws itself using code, you can make that drawing code execute in the editor to see your player.

.. DANGER::

    ``tool`` scripts run inside the editor, and let you access the scene tree
    of the currently edited scene. This is a powerful feature which also comes
    with caveats, as the editor does not include protections for potential
    misuse of ``tool`` scripts.
    Be **extremely** cautious when manipulating the scene tree, especially via
    :ref:`Node.queue_free<class_Node_method_queue_free>`, as it can cause
    crashes if you free a node while the editor runs logic involving it.

How to use it
-------------

To turn a script into a tool, add ``tool`` keyword at the top of your code.

To check if you are currently in the editor, use: ``Engine.editor_hint``.

For example, if you want to execute some code only in editor, use:

.. tabs::
 .. code-tab:: gdscript GDScript

    if Engine.editor_hint:
        # Code to execute when in editor.

On the other hand, if you want to execute code only in game, simply negate previous expression:

.. tabs::
 .. code-tab:: gdscript GDScript

    if not Engine.editor_hint:
        # Code to execute when in game.

Pieces of code that are not having any of the 2 conditions above will run both in editor and in game.

Here is how a ``_process()`` function might look like for you:

.. tabs::
 .. code-tab:: gdscript GDScript

    func _process(delta):
        if Engine.editor_hint:
            # Code to execute in editor.

        if not Engine.editor_hint:
            # Code to execute in game.

        # Code to execute both in editor and in game.

.. note:: Modifications in editor are permanent. In our case, when we remove the script, the node will keep its rotation direction. Be careful so that you don't make unwanted modifications.

Try it out
-----------

Add a ``Sprite`` node to your scene and set the texture to Godot icon. Attach and open a script, and change it to this:

.. tabs::
 .. code-tab:: gdscript GDScript

    tool
    extends Sprite

    func _process(delta):
        rotation_degrees += 180 * delta

Save the script and return to the editor. You should now see your object rotate. If you run the game, it will also rotate.

.. image:: img/rotating_in_editor.gif

.. note:: If you don't see the changes, reload the scene (close it and open it again).

Now let's choose which code runs when. Modify your ``_process()`` function to look like this:

.. tabs::
 .. code-tab:: gdscript GDScript

    func _process(delta):
        if Engine.editor_hint:
            rotation_degrees += 180 * delta
        else:
            rotation_degrees -= 180 * delta

Save the script. Now the object will spin clockwise in the editor, but if you run the game, it will spin counter-clockwise.

Editing variables
-----------------
Add and export a variable speed to the script. The function set_speed after "setget" is executed with your input to change the variable.
Modify  ``_process()`` to include the rotation speed.

.. tabs::
 .. code-tab:: gdscript GDScript

    tool
    extends Sprite


    export var speed = 1 setget set_speed


    # Update speed and reset the rotation.
    func set_speed(new_speed):
    	speed = new_speed
    	rotation_degrees = 0


    func _process(delta):
    	rotation_degrees += 180 * delta * speed

.. note:: Code from other nodes doesn't run in the editor. Your access to other nodes is limited. You can access the tree and nodes, and their default properties, but you can't access user variables. If you want to do so, other nodes have to run in the editor too. AutoLoad nodes cannot be accessed in the editor at all.

Instancing scenes
-----------------

You can instantiate packed scenes normally and add them to the scene currently opened in the editor. Be sure to set the scene root as the owner of all the nodes created this way or the nodes won't be visible in the editor.

If you are using ``tool``:

.. tabs::
 .. code-tab:: gdscript GDScript

    func _ready():
        var node = Spatial.new()
        add_child(node) # Parent could be any node in the scene
        node.set_owner(get_tree().edited_scene_root)

If you are using :ref:`EditorScript<class_EditorScript>`:

.. tabs::
 .. code-tab:: gdscript GDScript

    func _run():
        var parent = get_scene().find_node("Parent") # Parent could be any node in the scene
        var node = Spatial.new()
        parent.add_child(node)
        node.set_owner(get_scene())

.. warning:: Using ``tool`` improperly can yield many errors. It is advised to first write the code how you want it, and only then add the ``tool`` keyword to the top. Also make sure you divide your code into part that runs in editor and part that runs in game. This way you can find your bug easier.
