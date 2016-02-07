.. _class_Node:

Node
====

**Inherits:** :ref:`Object<class_object>`

**Inherited By:** :ref:`Viewport<class_viewport>`, :ref:`Timer<class_timer>`, :ref:`CanvasLayer<class_canvaslayer>`, :ref:`EventPlayer<class_eventplayer>`, :ref:`SoundRoomParams<class_soundroomparams>`, :ref:`Spatial<class_spatial>`, :ref:`AnimationPlayer<class_animationplayer>`, :ref:`EditorPlugin<class_editorplugin>`, :ref:`ResourcePreloader<class_resourcepreloader>`, :ref:`AnimationTreePlayer<class_animationtreeplayer>`, :ref:`SamplePlayer<class_sampleplayer>`, :ref:`InstancePlaceholder<class_instanceplaceholder>`, :ref:`StreamPlayer<class_streamplayer>`, :ref:`CanvasItem<class_canvasitem>`, :ref:`Tween<class_tween>`

**Category:** Core

Brief Description
-----------------

Base class for all the "Scene" elements.

Member Functions
----------------

+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                               | :ref:`_enter_tree<class_Node__enter_tree>`  **(** **)** virtual                                                                                                         |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                               | :ref:`_exit_tree<class_Node__exit_tree>`  **(** **)** virtual                                                                                                           |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                               | :ref:`_fixed_process<class_Node__fixed_process>`  **(** :ref:`float<class_float>` delta  **)** virtual                                                                  |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                               | :ref:`_input<class_Node__input>`  **(** :ref:`InputEvent<class_inputevent>` event  **)** virtual                                                                        |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                               | :ref:`_process<class_Node__process>`  **(** :ref:`float<class_float>` delta  **)** virtual                                                                              |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                               | :ref:`_ready<class_Node__ready>`  **(** **)** virtual                                                                                                                   |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                               | :ref:`_unhandled_input<class_Node__unhandled_input>`  **(** :ref:`InputEvent<class_inputevent>` event  **)** virtual                                                    |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                               | :ref:`_unhandled_key_input<class_Node__unhandled_key_input>`  **(** :ref:`InputEvent<class_inputevent>` key_event  **)** virtual                                        |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                               | :ref:`set_name<class_Node_set_name>`  **(** :ref:`String<class_string>` name  **)**                                                                                     |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`String<class_string>`        | :ref:`get_name<class_Node_get_name>`  **(** **)** const                                                                                                                 |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                               | :ref:`add_child<class_Node_add_child>`  **(** :ref:`Node<class_node>` node, :ref:`bool<class_bool>` legible_unique_name=false  **)**                                    |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                               | :ref:`remove_child<class_Node_remove_child>`  **(** :ref:`Node<class_node>` node  **)**                                                                                 |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`              | :ref:`get_child_count<class_Node_get_child_count>`  **(** **)** const                                                                                                   |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Array<class_array>`          | :ref:`get_children<class_Node_get_children>`  **(** **)** const                                                                                                         |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Node<class_node>`            | :ref:`get_child<class_Node_get_child>`  **(** :ref:`int<class_int>` idx  **)** const                                                                                    |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`            | :ref:`has_node<class_Node_has_node>`  **(** :ref:`NodePath<class_nodepath>` path  **)** const                                                                           |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Node<class_node>`            | :ref:`get_node<class_Node_get_node>`  **(** :ref:`NodePath<class_nodepath>` path  **)** const                                                                           |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Parent                             | :ref:`get_parent<class_Node_get_parent>`  **(** **)** const                                                                                                             |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Node<class_node>`            | :ref:`find_node<class_Node_find_node>`  **(** :ref:`String<class_string>` mask, :ref:`bool<class_bool>` recursive=true, :ref:`bool<class_bool>` owned=true  **)** const |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`            | :ref:`has_node_and_resource<class_Node_has_node_and_resource>`  **(** :ref:`NodePath<class_nodepath>` path  **)** const                                                 |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Array<class_array>`          | :ref:`get_node_and_resource<class_Node_get_node_and_resource>`  **(** :ref:`NodePath<class_nodepath>` path  **)**                                                       |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`            | :ref:`is_inside_tree<class_Node_is_inside_tree>`  **(** **)** const                                                                                                     |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`            | :ref:`is_a_parent_of<class_Node_is_a_parent_of>`  **(** :ref:`Node<class_node>` node  **)** const                                                                       |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`            | :ref:`is_greater_than<class_Node_is_greater_than>`  **(** :ref:`Node<class_node>` node  **)** const                                                                     |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`NodePath<class_nodepath>`    | :ref:`get_path<class_Node_get_path>`  **(** **)** const                                                                                                                 |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`NodePath<class_nodepath>`    | :ref:`get_path_to<class_Node_get_path_to>`  **(** :ref:`Node<class_node>` node  **)** const                                                                             |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                               | :ref:`add_to_group<class_Node_add_to_group>`  **(** :ref:`String<class_string>` group, :ref:`bool<class_bool>` persistent=false  **)**                                  |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                               | :ref:`remove_from_group<class_Node_remove_from_group>`  **(** :ref:`String<class_string>` group  **)**                                                                  |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`            | :ref:`is_in_group<class_Node_is_in_group>`  **(** :ref:`String<class_string>` group  **)** const                                                                        |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                               | :ref:`move_child<class_Node_move_child>`  **(** :ref:`Node<class_node>` child_node, :ref:`int<class_int>` to_pos  **)**                                                 |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Array<class_array>`          | :ref:`get_groups<class_Node_get_groups>`  **(** **)** const                                                                                                             |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                               | :ref:`raise<class_Node_raise>`  **(** **)**                                                                                                                             |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                               | :ref:`set_owner<class_Node_set_owner>`  **(** :ref:`Node<class_node>` owner  **)**                                                                                      |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Node<class_node>`            | :ref:`get_owner<class_Node_get_owner>`  **(** **)** const                                                                                                               |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                               | :ref:`remove_and_skip<class_Node_remove_and_skip>`  **(** **)**                                                                                                         |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`              | :ref:`get_index<class_Node_get_index>`  **(** **)** const                                                                                                               |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                               | :ref:`print_tree<class_Node_print_tree>`  **(** **)**                                                                                                                   |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                               | :ref:`set_filename<class_Node_set_filename>`  **(** :ref:`String<class_string>` filename  **)**                                                                         |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`String<class_string>`        | :ref:`get_filename<class_Node_get_filename>`  **(** **)** const                                                                                                         |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                               | :ref:`propagate_notification<class_Node_propagate_notification>`  **(** :ref:`int<class_int>` what  **)**                                                               |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                               | :ref:`set_fixed_process<class_Node_set_fixed_process>`  **(** :ref:`bool<class_bool>` enable  **)**                                                                     |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`          | :ref:`get_fixed_process_delta_time<class_Node_get_fixed_process_delta_time>`  **(** **)** const                                                                         |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`            | :ref:`is_fixed_processing<class_Node_is_fixed_processing>`  **(** **)** const                                                                                           |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                               | :ref:`set_process<class_Node_set_process>`  **(** :ref:`bool<class_bool>` enable  **)**                                                                                 |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`          | :ref:`get_process_delta_time<class_Node_get_process_delta_time>`  **(** **)** const                                                                                     |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`            | :ref:`is_processing<class_Node_is_processing>`  **(** **)** const                                                                                                       |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                               | :ref:`set_process_input<class_Node_set_process_input>`  **(** :ref:`bool<class_bool>` enable  **)**                                                                     |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`            | :ref:`is_processing_input<class_Node_is_processing_input>`  **(** **)** const                                                                                           |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                               | :ref:`set_process_unhandled_input<class_Node_set_process_unhandled_input>`  **(** :ref:`bool<class_bool>` enable  **)**                                                 |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`            | :ref:`is_processing_unhandled_input<class_Node_is_processing_unhandled_input>`  **(** **)** const                                                                       |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                               | :ref:`set_process_unhandled_key_input<class_Node_set_process_unhandled_key_input>`  **(** :ref:`bool<class_bool>` enable  **)**                                         |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`            | :ref:`is_processing_unhandled_key_input<class_Node_is_processing_unhandled_key_input>`  **(** **)** const                                                               |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                               | :ref:`set_pause_mode<class_Node_set_pause_mode>`  **(** :ref:`int<class_int>` mode  **)**                                                                               |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`              | :ref:`get_pause_mode<class_Node_get_pause_mode>`  **(** **)** const                                                                                                     |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`            | :ref:`can_process<class_Node_can_process>`  **(** **)** const                                                                                                           |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                               | :ref:`print_stray_nodes<class_Node_print_stray_nodes>`  **(** **)**                                                                                                     |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`              | :ref:`get_position_in_parent<class_Node_get_position_in_parent>`  **(** **)** const                                                                                     |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`SceneTree<class_scenetree>`  | :ref:`get_tree<class_Node_get_tree>`  **(** **)** const                                                                                                                 |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Node<class_node>`            | :ref:`duplicate<class_Node_duplicate>`  **(** :ref:`bool<class_bool>` use_instancing=false  **)** const                                                                 |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                               | :ref:`replace_by<class_Node_replace_by>`  **(** :ref:`Node<class_node>` node, :ref:`bool<class_bool>` keep_data=false  **)**                                            |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                               | :ref:`set_scene_instance_load_placeholder<class_Node_set_scene_instance_load_placeholder>`  **(** :ref:`bool<class_bool>` load_placeholder  **)**                       |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`            | :ref:`get_scene_instance_load_placeholder<class_Node_get_scene_instance_load_placeholder>`  **(** **)** const                                                           |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Object<class_object>`        | :ref:`get_viewport<class_Node_get_viewport>`  **(** **)** const                                                                                                         |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                               | :ref:`queue_free<class_Node_queue_free>`  **(** **)**                                                                                                                   |
+------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Signals
-------

-  **renamed**  **(** **)**
-  **enter_tree**  **(** **)**
-  **exit_tree**  **(** **)**

Numeric Constants
-----------------

- **NOTIFICATION_ENTER_TREE** = **10**
- **NOTIFICATION_EXIT_TREE** = **11**
- **NOTIFICATION_MOVED_IN_PARENT** = **12**
- **NOTIFICATION_READY** = **13**
- **NOTIFICATION_FIXED_PROCESS** = **16**
- **NOTIFICATION_PROCESS** = **17** --- Notification received every frame when the process flag is set (see :ref:`set_process<class_Node_set_process>`).
- **NOTIFICATION_PARENTED** = **18** --- Notification received when a node is set as a child of another node. Note that this doesn't mean that a node entered the Scene Tree.
- **NOTIFICATION_UNPARENTED** = **19** --- Notification received when a node is unparented (parent removed it from the list of children).
- **NOTIFICATION_PAUSED** = **14**
- **NOTIFICATION_UNPAUSED** = **15**
- **NOTIFICATION_INSTANCED** = **20**
- **PAUSE_MODE_INHERIT** = **0**
- **PAUSE_MODE_STOP** = **1**
- **PAUSE_MODE_PROCESS** = **2**

Description
-----------

Nodes can be set as children of other nodes, resulting in a tree arrangement. Any tree of nodes is called a "Scene".

Scenes can be saved to disk, and then instanced into other scenes. This allows for very high flexibility in the architecture and data model of the projects.

:ref:`SceneMainLoop<class_scenemainloop>` contains the "active" tree of nodes, and a node becomes active (receiving NOTIFICATION_ENTER_SCENE) when added to that tree.

A node can contain any number of nodes as a children (but there is only one tree root) with the requirement that no two children with the same name can exist.

Nodes can, optionally, be added to groups. This makes it easy to reach a number of nodes from the code (for example an "enemies" group).

Nodes can be set to "process" state, so they constantly receive a callback requesting them to process (do anything). Normal processing (:ref:`_process<class_Node__process>`) happens as fast as possible and is dependent on the frame rate, so the processing time delta is variable. Fixed processing (:ref:`_fixed_process<class_Node__fixed_process>`) happens a fixed amount of times per second (by default 60) and is useful to link itself to the physics.

Nodes can also process input events. When set, the :ref:`_input<class_Node__input>` function will be called with every input that the program receives. Since this is usually too overkill (unless used for simple projects), an :ref:`_unhandled_input<class_Node__unhandled_input>` function is called when the input was not handled by anyone else (usually, GUI :ref:`Control<class_control>` nodes).

To keep track of the scene hierarchy (specially when instancing scenes into scenes) an "owner" can be set to a node. This keeps track of who instanced what. This is mostly useful when writing editors and tools, though.

Finally, when a node is freed, it will free all its children nodes too.

Member Function Description
---------------------------

.. _class_Node__enter_tree:

- void  **_enter_tree**  **(** **)** virtual

.. _class_Node__exit_tree:

- void  **_exit_tree**  **(** **)** virtual

.. _class_Node__fixed_process:

- void  **_fixed_process**  **(** :ref:`float<class_float>` delta  **)** virtual

Called for fixed processing (synced to the physics).

.. _class_Node__input:

- void  **_input**  **(** :ref:`InputEvent<class_inputevent>` event  **)** virtual

Called when any input happens (also must enable with :ref:`set_process_input<class_Node_set_process_input>` or the property).

.. _class_Node__process:

- void  **_process**  **(** :ref:`float<class_float>` delta  **)** virtual

Called for processing. This is called every frame, with the delta time from the previous frame.

.. _class_Node__ready:

- void  **_ready**  **(** **)** virtual

Called when ready (entered scene and children entered too).

.. _class_Node__unhandled_input:

- void  **_unhandled_input**  **(** :ref:`InputEvent<class_inputevent>` event  **)** virtual

Called when any input happens that was not handled by something else (also must enable with :ref:`set_process_unhandled_input<class_Node_set_process_unhandled_input>` or the property).

.. _class_Node__unhandled_key_input:

- void  **_unhandled_key_input**  **(** :ref:`InputEvent<class_inputevent>` key_event  **)** virtual

Called when any key input happens that was not handled by something else.

.. _class_Node_set_name:

- void  **set_name**  **(** :ref:`String<class_string>` name  **)**

Set the name of the :ref:`Node<class_node>`. Name must be unique within parent, and setting an already existing name will cause for the node to be automatically renamed.

.. _class_Node_get_name:

- :ref:`String<class_string>`  **get_name**  **(** **)** const

Return the name of the :ref:`Node<class_node>`. Name is be unique within parent.

.. _class_Node_add_child:

- void  **add_child**  **(** :ref:`Node<class_node>` node, :ref:`bool<class_bool>` legible_unique_name=false  **)**

Add a child :ref:`Node<class_node>`. Nodes can have as many children as they want, but every child must have a unique name. Children nodes are automatically deleted when the parent node is deleted, so deleting a whole scene is performed by deleting its topmost node.

The optional boolean argument enforces creating child node with human-readable names, based on the name of node being instanced instead of its type only.

.. _class_Node_remove_child:

- void  **remove_child**  **(** :ref:`Node<class_node>` node  **)**

Remove a child :ref:`Node<class_node>`. Node is NOT deleted and will have to be deleted manually.

.. _class_Node_get_child_count:

- :ref:`int<class_int>`  **get_child_count**  **(** **)** const

Return the amount of children nodes.

.. _class_Node_get_children:

- :ref:`Array<class_array>`  **get_children**  **(** **)** const

.. _class_Node_get_child:

- :ref:`Node<class_node>`  **get_child**  **(** :ref:`int<class_int>` idx  **)** const

Return a children node by it's index (see :ref:`get_child_count<class_Node_get_child_count>`). This method is often used for iterating all children of a node.

.. _class_Node_has_node:

- :ref:`bool<class_bool>`  **has_node**  **(** :ref:`NodePath<class_nodepath>` path  **)** const

.. _class_Node_get_node:

- :ref:`Node<class_node>`  **get_node**  **(** :ref:`NodePath<class_nodepath>` path  **)** const

Fetch a node. NodePath must be valid (or else error will occur) and can be either the path to child node, a relative path (from the current node to another node), or an absolute path to a node.

Note: fetching absolute paths only works when the node is inside the scene tree (see :ref:`is_inside_scene<class_Node_is_inside_scene>`). Examples. Assume your current node is Character and following tree:



 root/

 root/Character

 root/Character/Sword

 root/Character/Backpack/Dagger

 root/MyGame

 root/Swamp/Alligator

 root/Swamp/Mosquito

 root/Swamp/Goblin



 Possible paths are:

 - get_node("Sword")

 - get_node("Backpack/Dagger")

 - get_node("../Swamp/Alligator")

 - get_node("/root/MyGame")

.. _class_Node_get_parent:

- Parent  **get_parent**  **(** **)** const

Return the parent :ref:`Node<class_node>` of the current :ref:`Node<class_node>`, or an empty Object if the node lacks a parent.

.. _class_Node_find_node:

- :ref:`Node<class_node>`  **find_node**  **(** :ref:`String<class_string>` mask, :ref:`bool<class_bool>` recursive=true, :ref:`bool<class_bool>` owned=true  **)** const

.. _class_Node_has_node_and_resource:

- :ref:`bool<class_bool>`  **has_node_and_resource**  **(** :ref:`NodePath<class_nodepath>` path  **)** const

.. _class_Node_get_node_and_resource:

- :ref:`Array<class_array>`  **get_node_and_resource**  **(** :ref:`NodePath<class_nodepath>` path  **)**

.. _class_Node_is_inside_tree:

- :ref:`bool<class_bool>`  **is_inside_tree**  **(** **)** const

.. _class_Node_is_a_parent_of:

- :ref:`bool<class_bool>`  **is_a_parent_of**  **(** :ref:`Node<class_node>` node  **)** const

Return *true* if the "node" argument is a direct or indirect child of the current node, otherwise return *false*.

.. _class_Node_is_greater_than:

- :ref:`bool<class_bool>`  **is_greater_than**  **(** :ref:`Node<class_node>` node  **)** const

Return *true* if "node" occurs later in the scene hierarchy than the current node, otherwise return *false*.

.. _class_Node_get_path:

- :ref:`NodePath<class_nodepath>`  **get_path**  **(** **)** const

Return the absolute path of the current node. This only works if the current node is inside the scene tree (see :ref:`is_inside_scene<class_Node_is_inside_scene>`).

.. _class_Node_get_path_to:

- :ref:`NodePath<class_nodepath>`  **get_path_to**  **(** :ref:`Node<class_node>` node  **)** const

Return the relative path from the current node to the specified node in "node" argument. Both nodes must be in the same scene, or else the function will fail.

.. _class_Node_add_to_group:

- void  **add_to_group**  **(** :ref:`String<class_string>` group, :ref:`bool<class_bool>` persistent=false  **)**

Add a node to a group. Groups are helpers to name and organize group of nodes, like for example: "Enemies", "Collectables", etc. A :ref:`Node<class_node>` can be in any number of groups. Nodes can be assigned a group at any time, but will not be added to it until they are inside the scene tree (see :ref:`is_inside_scene<class_Node_is_inside_scene>`).

.. _class_Node_remove_from_group:

- void  **remove_from_group**  **(** :ref:`String<class_string>` group  **)**

Remove a node from a group.

.. _class_Node_is_in_group:

- :ref:`bool<class_bool>`  **is_in_group**  **(** :ref:`String<class_string>` group  **)** const

.. _class_Node_move_child:

- void  **move_child**  **(** :ref:`Node<class_node>` child_node, :ref:`int<class_int>` to_pos  **)**

Move a child node to a different position (order) amongst the other children. Since calls, signals, etc are performed by tree order, changing the order of children nodes may be useful.

.. _class_Node_get_groups:

- :ref:`Array<class_array>`  **get_groups**  **(** **)** const

.. _class_Node_raise:

- void  **raise**  **(** **)**

Move this node to the top of the array of nodes of the parent node. This is often useful on GUIs (:ref:`Control<class_control>`), because their order of drawing fully depends on their order in the tree.

.. _class_Node_set_owner:

- void  **set_owner**  **(** :ref:`Node<class_node>` owner  **)**

Set the node owner. A node can have any other node as owner (as long as a valid parent, grandparent, etc ascending in the tree). When saving a node (using SceneSaver) all the nodes it owns will be saved with it. This allows to create complex SceneTrees, with instancing and subinstancing.

.. _class_Node_get_owner:

- :ref:`Node<class_node>`  **get_owner**  **(** **)** const

Get the node owner (see :ref:`set_node_owner<class_Node_set_node_owner>`).

.. _class_Node_remove_and_skip:

- void  **remove_and_skip**  **(** **)**

Remove a node and set all its children as children of the parent node (if exists). All even subscriptions that pass by the removed node will be unsubscribed.

.. _class_Node_get_index:

- :ref:`int<class_int>`  **get_index**  **(** **)** const

Get the node index in the parent (assuming it has a parent).

.. _class_Node_print_tree:

- void  **print_tree**  **(** **)**

Print the scene to stdout. Used mainly for debugging purposes.

.. _class_Node_set_filename:

- void  **set_filename**  **(** :ref:`String<class_string>` filename  **)**

A node can contain a filename. This filename should not be changed by the user, unless writing editors and tools. When a scene is instanced from a file, it topmost node contains the filename from where it was loaded.

.. _class_Node_get_filename:

- :ref:`String<class_string>`  **get_filename**  **(** **)** const

Return a filename that may be containedA node can contained by the node. When a scene is instanced from a file, it topmost node contains the filename from where it was loaded (see :ref:`set_filename<class_Node_set_filename>`).

.. _class_Node_propagate_notification:

- void  **propagate_notification**  **(** :ref:`int<class_int>` what  **)**

Notify the current node and all its children recursively by calling notification() in all of them.

.. _class_Node_set_fixed_process:

- void  **set_fixed_process**  **(** :ref:`bool<class_bool>` enable  **)**

Enables or disables node fixed framerate processing. When a node is being processed, it will receive a NOTIFICATION_PROCESS at a fixed (usually 60 fps, check :ref:`OS<class_os>` to change that) interval (and the :ref:`_fixed_process<class_Node__fixed_process>` callback will be called if exists). It is common to check how much time was elapsed since the previous frame by calling :ref:`get_fixed_process_time<class_Node_get_fixed_process_time>`.

.. _class_Node_get_fixed_process_delta_time:

- :ref:`float<class_float>`  **get_fixed_process_delta_time**  **(** **)** const

Return the time elapsed since the last fixed frame. This is always the same in fixed processing unless the frames per second is changed in :ref:`OS<class_os>`.

.. _class_Node_is_fixed_processing:

- :ref:`bool<class_bool>`  **is_fixed_processing**  **(** **)** const

Return true if fixed processing is enabled (see :ref:`set_fixed_process<class_Node_set_fixed_process>`).

.. _class_Node_set_process:

- void  **set_process**  **(** :ref:`bool<class_bool>` enable  **)**

Enables or disables node processing. When a node is being processed, it will receive a NOTIFICATION_PROCESS on every drawn frame (and the :ref:`_process<class_Node__process>` callback will be called if exists). It is common to check how much time was elapsed since the previous frame by calling :ref:`get_process_time<class_Node_get_process_time>`.

.. _class_Node_get_process_delta_time:

- :ref:`float<class_float>`  **get_process_delta_time**  **(** **)** const

Return the time elapsed (in seconds) since the last process callback. This is almost always different each time.

.. _class_Node_is_processing:

- :ref:`bool<class_bool>`  **is_processing**  **(** **)** const

Return whether processing is enabled in the current node (see :ref:`set_process<class_Node_set_process>`).

.. _class_Node_set_process_input:

- void  **set_process_input**  **(** :ref:`bool<class_bool>` enable  **)**

Enable input processing for node. This is not required for GUI controls! It hooks up the node to receive all input (see :ref:`_input<class_Node__input>`).

.. _class_Node_is_processing_input:

- :ref:`bool<class_bool>`  **is_processing_input**  **(** **)** const

Return true if the node is processing input (see :ref:`set_process_input<class_Node_set_process_input>`).

.. _class_Node_set_process_unhandled_input:

- void  **set_process_unhandled_input**  **(** :ref:`bool<class_bool>` enable  **)**

Enable unhandled input processing for node. This is not required for GUI controls! It hooks up the node to receive all input that was not previously handled before (usually by a :ref:`Control<class_control>`). (see :ref:`_unhandled_input<class_Node__unhandled_input>`).

.. _class_Node_is_processing_unhandled_input:

- :ref:`bool<class_bool>`  **is_processing_unhandled_input**  **(** **)** const

Return true if the node is processing unhandled input (see :ref:`set_process_unhandled_input<class_Node_set_process_unhandled_input>`).

.. _class_Node_set_process_unhandled_key_input:

- void  **set_process_unhandled_key_input**  **(** :ref:`bool<class_bool>` enable  **)**

.. _class_Node_is_processing_unhandled_key_input:

- :ref:`bool<class_bool>`  **is_processing_unhandled_key_input**  **(** **)** const

.. _class_Node_set_pause_mode:

- void  **set_pause_mode**  **(** :ref:`int<class_int>` mode  **)**

.. _class_Node_get_pause_mode:

- :ref:`int<class_int>`  **get_pause_mode**  **(** **)** const

.. _class_Node_can_process:

- :ref:`bool<class_bool>`  **can_process**  **(** **)** const

Return true if the node can process.

.. _class_Node_print_stray_nodes:

- void  **print_stray_nodes**  **(** **)**

.. _class_Node_get_position_in_parent:

- :ref:`int<class_int>`  **get_position_in_parent**  **(** **)** const

.. _class_Node_get_tree:

- :ref:`SceneTree<class_scenetree>`  **get_tree**  **(** **)** const

.. _class_Node_duplicate:

- :ref:`Node<class_node>`  **duplicate**  **(** :ref:`bool<class_bool>` use_instancing=false  **)** const

.. _class_Node_replace_by:

- void  **replace_by**  **(** :ref:`Node<class_node>` node, :ref:`bool<class_bool>` keep_data=false  **)**

Replace a node in a scene by a given one. Subscriptions that pass through this node will be lost.

.. _class_Node_set_scene_instance_load_placeholder:

- void  **set_scene_instance_load_placeholder**  **(** :ref:`bool<class_bool>` load_placeholder  **)**

.. _class_Node_get_scene_instance_load_placeholder:

- :ref:`bool<class_bool>`  **get_scene_instance_load_placeholder**  **(** **)** const

.. _class_Node_get_viewport:

- :ref:`Object<class_object>`  **get_viewport**  **(** **)** const

.. _class_Node_queue_free:

- void  **queue_free**  **(** **)**


