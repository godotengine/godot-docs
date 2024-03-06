.. _doc_change_scenes_manually:

Change scenes manually
======================

Sometimes it helps to have more control over how one swaps scenes around.
A :ref:`Viewport <class_Viewport>`'s child nodes will render to the image
it generates, this holds true even for nodes outside
of the "current" scene. Autoloads fall into this category, but so do
scenes which one instances and adds to the tree at runtime:

.. tabs::
 .. code-tab:: gdscript GDScript

    var simultaneous_scene = preload("res://levels/level2.tscn").instantiate()

    func _add_a_scene_manually():
        # This is like autoloading the scene, only
        # it happens after already loading the main scene.
        get_tree().root.add_child(simultaneous_scene)

 .. code-tab:: csharp

    public Node simultaneousScene;

    public MyClass()
    {
        simultaneousScene = ResourceLoader.Load<PackedScene>("res://levels/level2.tscn").Instantiate();
    }

    public void _AddASceneManually()
    {
        // This is like autoloading the scene, only
        // it happens after already loading the main scene.
        GetTree().Root.AddChild(simultaneousScene);
    }

To complete the cycle and swap out the new scene with the old one,
developers have a choice to make. Many strategies exist for removing a scene
from view of the :ref:`Viewport <class_Viewport>`. The tradeoffs involve
balancing operation speed and memory consumption as well as balancing data
access and integrity.

1. **We can delete the existing scene.**
   :ref:`SceneTree.change_scene_to_file() <class_SceneTree_method_change_scene_to_file>` and
   :ref:`SceneTree.change_scene_to_packed() <class_SceneTree_method_change_scene_to_packed>`
   will delete the current scene immediately. Developers can also delete the
   main scene though. Assuming the root node's name is "Main", one could do
   ``get_node("/root/Main").free()`` to delete the whole scene.

    - Unloads memory.

        - Pro: RAM is no longer dragging the dead weight.

        - Con: Returning to that scene is now more expensive since it must be
          loaded back into memory again (takes time AND memory). Not a problem
          if returning soon is unnecessary.

        - Con: No longer have access to that scene's data. Not a problem if
          using that data soon is unnecessary.

        - Note: It can be useful to preserve the data in a soon-to-be-deleted
          scene by re-attaching one or more of its nodes to a different scene,
          or even directly to the :ref:`SceneTree <class_SceneTree>`.

    - Processing stops.

        - Pro: No nodes means no process, physics process, or input
          handling. The CPU is available to work on the new scene's contents.

        - Con: Those nodes' processing and input handling no longer operate.
          Not a problem if using the updated data is unnecessary.

2. **We can hide the existing scene.** By changing the visibility or collision
   detection of the nodes, we can hide the entire node sub-tree from the
   player's perspective.

    - Memory still exists.

        - Pro: One can still access the data if need be.

        - Pro: There's no need to move any more nodes around to save data.

        - Con: More data is being kept in memory which will be become a problem
          on memory-sensitive platforms like web or mobile.

    - Processing continues.

        - Pro: Data continues to receive processing updates, so the scene will
          keep updated any data within it that relies on delta time or frame
          data.

        - Pro: Nodes are still members of groups (since groups belong to the
          :ref:`SceneTree <class_SceneTree>`).

        - Con: The CPU's attention is now divided between both scenes. Too much
          load could result in low frame rates. One should be sure to test
          performance as they go to ensure the target platform can support the
          load they are giving it.

3. **We can remove the existing scene from the tree.** Assign a variable
   to the existing scene's root node. Then use
   :ref:`Node.remove_child(Node) <class_Node_method_remove_child>` to detach the entire
   scene from the tree.

    - Memory still exists (similar pros/cons as with hiding it from view).

    - Processing stops (similar pros/cons as with deleting it completely).

    - Pro: This variation of "hiding" it is much easier to show/hide. Rather
      than potentially keeping track of multiple changes to the scene, one
      must only call the one method add/remove_child pair of methods. It is
      similar to disabling game objects in other engines.

    - Con: Unlike with hiding it from view only, the data contained within
      the scene will become stale if it relies on delta time, input, groups,
      or other data that is derived from :ref:`SceneTree <class_SceneTree>`
      access.

There are also cases where one may wish to have many scenes present at the same
time. Perhaps one is adding their own singleton at runtime, or preserving a
a scene's data between scene changes (adding the scene to the root node).

.. tabs::
 .. code-tab:: gdscript GDScript

        get_tree().root.add_child(scene)

 .. code-tab:: csharp

        GetTree().Root.AddChild(scene);

Perhaps instead they wish to display multiple scenes at the same time using
:ref:`SubViewportContainers <class_SubViewportContainer>`. This is optimal in
cases where the intent is to render different content in different parts of the
screen. Minimaps and split-screen multiplayer are good examples.

Each option will have cases where it is best appropriate, so one must
examine the effects of each and determine what path best fits
their unique situation.
