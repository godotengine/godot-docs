.. _unity3D_to_godot:

..	references : 
..	https://wiki.unrealengine.com/Unity3D_Developer's_Guide_to_Unreal_Engine_4
..	https://docs.unrealengine.com/latest/INT/GettingStarted/FromUnity/

From Unity3D to Godot Engine
============================

This guide provides an overview of Godot Engine from the viewpoint of a Unity user, and aims to help you migrate your existing Unity experience into the world of Godot.

Differences
-----------

.. ##############################################################################################
.. ################## MODIFY THIS TABLE USING THIS URL : http://bit.ly/1tcxxJP ##################
.. ##############################################################################################


+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+
|                   | Unity                                                                                                                                                                                                                                                                | Godot                                                                                                          |
+===================+======================================================================================================================================================================================================================================================================+================================================================================================================+
| Licence           | proprietary                                                                                                                                                                                                                                                          | MIT Licence                                                                                                    |
+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+
| OS (editor)       |  Windows, OSX, Linux (unofficial)                                                                                                                                                                                                                                    | Windows, X11 (Linux, *BSD), Haiku, OSX                                                                         |
+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+
| OS (export)       | Desktop: Windows, Linux/SteamOS, OSX
Mobile: Android, iOS, WindowsPhone, Tizen,
Web: WebGL
Consoles: PS4, PSVita, XBoxOne, XBox360, WiiU, 3DS
VR: Occulus Rift, SteamVR, Google Cardboard, PlaystationVR, GearVR, HoloLens
TV: AndroidTV, Samsung SMARTTV, tvOS      | Desktop: Windows, X11, OSX
Mobile: Android, iOS, Blackberry (deprecated)
Web: HTML5 (via emscripten, broken)   |
+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+
| Scene system      | Entity-Component System (ECS) (GameObject > Component).                                                                                                                                                                                                              | Scene tree and nodes, allowing scenes to be nested and/or inherit other scenes                                 |
+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+
| Third-party tools | Visual Studio or SharpEditor                                                                                                                                                                                                                                         | Android SDK for Android export
External editors are possible                                                   |
+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+
|  Killer features  |                                                                                                                                                                                                                                                                      | Live-editing
Signals
Animation tool
Shader graphs
GDScript
integrated debugger                                 |
+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+


The editor
----------

Godot Engine provides a rich-featured editor that allows you to build your games. The pictures below display both editors with colored blocks to indicate common functionalities.

.. image:: /img/unity-gui-overlay.png
.. image:: /img/godot-gui-overlay.png


Note that Godot editor allows you to dock each panel at the side of the scene editor you wish.

As you can see, there are some similarities between both editors: first of course, the scene which allows you to display and organize your game elements on screen. Second, the inspector which allows you to edit the parameters of the selected object. Also, the Hierarchy panel in Unity finds its correspondance with Godot's Scene tree panel, although we will see in the next section the differences between how Unity and Godot manage scenes and scene elements.

Unity and Godot both directly use the folder architecture you define for your project. There is no real good solution, and every folder architecture will work for both engines. You can thus continue with your current way to organize your project. However, we have some advices to share a bit further, in order to match your project architecture and Godot scene system.

To finish, the toolbar at the top of the screen is also similar between Unity and Godot. However, Godot provides some new buttons aside the classic "Play", "Pause" and "Stop" buttons. These buttons are introduced in the `Toolbar <introduction/editor#toolbar>`_ section as they a bit out of the scope of this page.

The scene system
----------------

This is the most important difference between Unity and Godot, and actually the favourite feature of most Godot users.

Unity's scene system generally consist in embedding all the required assets in a scene, and link them together by setting components and scripts to them. 

Godot's scene system is different: it actually consists in a tree made of nodes. Each node serves a purpose: Sprite, Mesh, Light... Basically, this is similar to Unity scene system. However, each node can have multiple children, which make each a subscene of the main scene. This means you can compose a whole scene with different scenes, stored in different files.

For example, think of a platformer level. You would compose it with multiple elements:

    - Bricks

    - Coins

    - The player

    - The enemies


In Unity, you would put all the GameObjects in the scene: the player, multiple instances of enemies, bricks everywhere to form the ground of the level, and multiple instances of coins all over the level. You would then add various components to each element to link them and add logic in the level: for example, you'd add a BoxCollider2D to all the elements of the scene so that they can collide. This principle is different in Godot.

In Godot, you would split your whole scene into 3 separate, smaller scenes, which you would then instance in the main scene.

    1. First, a scene for the Player alone.

Consider the player as a reusable element in other levels. It is composed of one node in particular: an AnimatedSprite node, which contains the sprite textures to form various animations (for example, walking animation)


    2. Second, a scene for the Enemy.

There again, an enemy is a reusable element in other levels. It is almost the same as the Player node - the only differences are the script (that manages IA, mostly) and sprite textures used by the AnimatedSprite.

    3. Lastly, the Level scene.

It is composed of Bricks (for platforms), Coins (for the player to grab) and a certain number of instances of the previous Enemy scene. These will be different, separate enemies, whose behaviour and appearance will be the same as defined in the Enemy scene. Each instance is then considered as a node in the Level scene tree. Of course, you can set different properties for each enemy node (to change its color for example).

Finally, the main scene would then be composed of one root node with 2 children: a Player instance node, and a Level instance node. 
The root node can be anything, generally a "root" type such as "Node" which is the most global type, or "Node2D" (root type of all 2D-related nodes), "Spatial" (root type of all 3D-related nodes) or "Control" (root type of all GUI-related nodes).


As you can see, every scene is organized as a tree. The same goes for nodes' properties: you don't *add* a collision component to a node to make it collidable like Unity does. Instead, you make this node a *child* of a new specific node that has collision properties. Godot features various collision types nodes, depending of the use (see the `Physics introduction <tutorials/2d/physics_introduction>`_).

<< Question
What are the advantages of this system? Wouldn't this system potentially increase the depth of the scene tree? Besides, Unity allows organizing GameObjects by putting them in empty GameObjects.
>> Answer
First, this system is closer to the well-known Object-Oriented paradigm: Godot provides a number of nodes which are not clearly "Game Objects", but they provide their children with their own capabilities: this is inheritance.
Second, it allows the extraction a subtree of scene to make it a scene of its own, which answers to the second and third questions: even if a scene tree gets too deep, it can be split into smaller subtrees. This also allows a better solution for reusability, as you can include any subtree as a child of any node. Putting multiple nodes in an empty GameObject in Unity does not provide the same possibility, apart from a visual organization.
<<

These are the most important concepts you need to remind: "node", "parent node" and "child node".


Project organization
--------------------

.. image:: /img/unity-project-organization-example.png

We previously observed that there is no perfect solution to set a project architecture. Any solution will work for Unity and Godot, so this point has a lesser importance.

However, we often observe a common architecture for Unity projects, which consists in having one Assets folder in the root directory, that contains various folders, one per type of asset: Audio, Graphics, Models, Materials, Scripts, Scenes, etc.

As described before, Godot scene system allows splitting scenes in smaller scenes. Since each scene and subscene is actually one scene file in the project, we recommend organizing your project a bit differently. This wiki provides a page for this: `Project Organization <engine/project_organization.html>`_.


Where are my prefabs?
---------------------

The concept of prefabs as provided by Unity is a 'template' element of the scene. It is reusable, and each instance of the prefab that exists in the scene has an existence of its own, but all of them have the same properties as defined by the prefab.

Godot does not provide prefabs as such, but this functionality is here again filled thanks to its scene system: as we saw the scene system is organized as a tree. Godot allows you to save a subtree of a scene as its own scene, thus saved in its own file. This new scene can then be instanced any times you want. Any change you make to this new, separate scene will be applied to the instance. However, any change you make to the instance will not have any impact on the 'template' scene.

.. image:: /img/save-branch-as-scene.png

To be precise, you can modify the parameters of the instance in the Inspector panel. However, the nodes that compose this instance are locked and you can unlock them if you need to by clicking the clapperboard icon next to the instance in the Scene tree, and select "Editable children" in the menu. You don't need to do this to add new children nodes to this node, but remember that these new children will belong to the instance, not the 'template' scene. If you want to add new children to all the instances of your 'template' scene, then you need to add it once in the 'template' scene.

.. image:: /img/editable-children.png

Glossary correspondance
-----------------------

GameObject -> Node
Add a component -> Inheriting
Prefab -> Externalized branch


Scripting : From C# to GDScript
-------------------------------

As you may know already, Unity provides support for 2 scripting languages for its API: C# and Javascript. 

By design, you can attach one script 


