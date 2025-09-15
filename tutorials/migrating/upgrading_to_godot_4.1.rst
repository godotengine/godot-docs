.. _doc_upgrading_to_godot_4.1:

Upgrading from Godot 4.0 to Godot 4.1
=====================================

For most games and apps made with 4.0, it should be relatively safe to migrate to 4.1.
This page intends to cover everything you need to pay attention to when migrating
your project.

Breaking changes
----------------

If you are migrating from 4.0 to 4.1, the breaking changes listed here might
affect you. Changes are grouped by areas/systems.

.. warning::

    The GDExtension API completely breaks compatibility in 4.1, so it's not included
    in the table below. See the :ref:`updating_your_gdextension_for_godot_4_1` section
    for more information.

This article indicates whether each breaking change affects GDScript and whether
the C# breaking change is *binary compatible* or *source compatible*:

- **Binary compatible** - Existing binaries will load and execute successfully without
  recompilation, and the runtime behavior won't change.
- **Source compatible** - Source code will compile successfully without changes when
  upgrading Godot.

Core
~~~~

========================================================================================================================  ===================  ====================  ====================  ===========
Change                                                                                                                    GDScript Compatible  C# Binary Compatible  C# Source Compatible  Introduced
========================================================================================================================  ===================  ====================  ====================  ===========
**Basis**
Method ``looking_at`` adds a new ``use_model_front`` optional parameter                                                   |✔️|                 |✔️|                  |✔️|                  `GH-76082`_
**Object**
Method ``get_meta_list`` changes return type from ``PackedStringArray`` to ``Array[StringName]``                          |✔️|                 |❌|                  |❌|                  `GH-76418`_
**Transform3D**
Method ``looking_at`` adds a new ``use_model_front`` optional parameter                                                   |✔️|                 |✔️|                  |✔️|                  `GH-76082`_
**UndoRedo**
Method ``create_action`` adds a new ``backward_undo_ops`` optional parameter                                              |✔️|                 |✔️ with compat|      |✔️|                  `GH-76688`_
**WorkerThreadPool**
Method ``wait_for_task_completion`` changes return type from ``void`` to ``Error``                                        |✔️|                 |❌|                  |✔️|                  `GH-77143`_
========================================================================================================================  ===================  ====================  ====================  ===========

Animation
~~~~~~~~~

========================================================================================================================  ===================  ====================  ====================  ===========
Change                                                                                                                    GDScript Compatible  C# Binary Compatible  C# Source Compatible  Introduced
========================================================================================================================  ===================  ====================  ====================  ===========
**AnimationNode**
Method ``_process`` adds a new ``test_only`` parameter                                                                    |❌|                 |❌|                  |❌|                  `GH-75759`_
Method ``blend_input`` adds a new ``test_only`` optional parameter                                                        |✔️|                 |✔️ with compat|      |✔️|                  `GH-75759`_
Method ``blend_node`` adds a new ``test_only`` optional parameter                                                         |✔️|                 |✔️ with compat|      |✔️|                  `GH-75759`_
**AnimationNodeStateMachinePlayback**
Method ``get_travel_path`` changes return type from ``PackedStringArray`` to ``Array[StringName]``                        |✔️|                 |❌|                  |❌|                  `GH-76418`_
========================================================================================================================  ===================  ====================  ====================  ===========

2D nodes
~~~~~~~~

========================================================================================================================  ===================  ====================  ====================  ===========
Change                                                                                                                    GDScript Compatible  C# Binary Compatible  C# Source Compatible  Introduced
========================================================================================================================  ===================  ====================  ====================  ===========
**PathFollow2D**
Property ``lookahead`` removed                                                                                            |❌|                 |❌|                  |❌|                  `GH-72842`_
========================================================================================================================  ===================  ====================  ====================  ===========

3D nodes
~~~~~~~~

========================================================================================================================  ===================  ====================  ====================  ===========
Change                                                                                                                    GDScript Compatible  C# Binary Compatible  C# Source Compatible  Introduced
========================================================================================================================  ===================  ====================  ====================  ===========
**Geometry3D**
Method ``segment_intersects_convex`` changes ``planes`` parameter type from untyped ``Array`` to ``Array[Plane]``         |✔️|                 |✔️ with compat|      |❌|                  `GH-76418`_
**MeshInstance3D**
Method ``create_multiple_convex_collisions`` adds a new ``settings`` optional parameter                                   |✔️|                 |✔️ with compat|      |✔️|                  `GH-72152`_
**Node3D**
Method ``look_at`` adds a new ``use_model_front`` optional parameter                                                      |✔️|                 |✔️ with compat|      |✔️|                  `GH-76082`_
Method ``look_at_from_position`` adds a new ``use_model_front`` optional parameter                                        |✔️|                 |✔️ with compat|      |✔️|                  `GH-76082`_
========================================================================================================================  ===================  ====================  ====================  ===========

GUI nodes
~~~~~~~~~

========================================================================================================================  ===================  ====================  ====================  ===========
Change                                                                                                                    GDScript Compatible  C# Binary Compatible  C# Source Compatible  Introduced
========================================================================================================================  ===================  ====================  ====================  ===========
**CodeEdit**
Method ``add_code_completion_option`` adds a new ``location`` optional parameter                                          |✔️|                 |✔️ with compat|      |✔️|                  `GH-75746`_
**RichTextLabel**
Method ``push_list`` adds a new ``bullet`` optional parameter                                                             |✔️|                 |✔️ with compat|      |✔️|                  `GH-75017`_
Method ``push_paragraph`` adds a new ``justification_flags`` optional parameter                                           |✔️|                 |✔️ with compat|      |✔️|                  `GH-75250`_
Method ``push_paragraph`` adds a new ``tab_stops`` optional parameter                                                     |✔️|                 |✔️ with compat|      |✔️|                  `GH-76401`_
**Tree**
Method ``edit_selected`` adds a new ``force_edit`` optional parameter                                                     |✔️|                 |✔️ with compat|      |✔️|                  `GH-76794`_
========================================================================================================================  ===================  ====================  ====================  ===========

Physics
~~~~~~~

========================================================================================================================  ===================  ====================  ====================  ===========
Change                                                                                                                    GDScript Compatible  C# Binary Compatible  C# Source Compatible  Introduced
========================================================================================================================  ===================  ====================  ====================  ===========
**Area2D**
Property ``priority`` changes type from ``float`` to ``int``                                                              |❌|                 |❌|                  |❌|                  `GH-72749`_
**Area3D**
Property ``priority`` changes type from ``float`` to ``int``                                                              |❌|                 |❌|                  |❌|                  `GH-72749`_
**PhysicsDirectSpaceState2D**
Method ``collide_shape`` changes return type from ``Array[PackedVector2Array]`` to ``Array[Vector2]``                     |❌|                 |❌|                  |❌|                  `GH-75260`_
**PhysicsDirectSpaceState3D**
Method ``collide_shape`` changes return type from ``Array[PackedVector3Array]`` to ``Array[Vector3]``                     |❌|                 |❌|                  |❌|                  `GH-75260`_
========================================================================================================================  ===================  ====================  ====================  ===========

Rendering
~~~~~~~~~

========================================================================================================================  ===================  ====================  ====================  ===========
Change                                                                                                                    GDScript Compatible  C# Binary Compatible  C# Source Compatible  Introduced
========================================================================================================================  ===================  ====================  ====================  ===========
**RDShaderFile**
Method ``get_version_list`` changes return type from ``PackedStringArray`` to ``Array[StringName]``                       |✔️|                 |❌|                  |❌|                  `GH-76418`_
**RenderingDevice**
Method ``draw_list_begin`` changes ``storage_textures`` parameter type from untyped ``Array`` to ``Array[RID]``           |✔️|                 |✔️ with compat|      |❌|                  `GH-76418`_
**RenderingServer**
Method ``global_shader_parameter_get_list`` changes return type from ``PackedStringArray`` to ``Array[StringName]``       |✔️|                 |❌|                  |❌|                  `GH-76418`_
**SurfaceTool**
Method ``add_triangle_fan`` changes ``tangents`` parameter type from untyped ``Array`` to ``Array[Plane]``                |✔️|                 |✔️ with compat|      |❌|                  `GH-76418`_
========================================================================================================================  ===================  ====================  ====================  ===========

Navigation
~~~~~~~~~~

========================================================================================================================  ===================  ====================  ====================  ===========
Change                                                                                                                    GDScript Compatible  C# Binary Compatible  C# Source Compatible  Introduced
========================================================================================================================  ===================  ====================  ====================  ===========
**NavigationAgent2D**
Method ``set_velocity`` replaced with ``velocity`` property                                                               |✔️|                 |❌|                  |❌|                  `GH-69988`_
Property ``time_horizon`` split into ``time_horizon_agents`` and ``time_horizon_obstacles``                               |❌|                 |❌|                  |❌|                  `GH-69988`_
**NavigationAgent3D**
Property ``agent_height_offset`` renamed to ``path_height_offset``                                                        |❌|                 |❌|                  |❌|                  `GH-69988`_
Property ``ignore_y`` removed                                                                                             |❌|                 |❌|                  |❌|                  `GH-69988`_
Method ``set_velocity`` replaced with ``velocity`` property                                                               |✔️|                 |❌|                  |❌|                  `GH-69988`_
Property ``time_horizon`` split into ``time_horizon_agents`` and ``time_horizon_obstacles``                               |❌|                 |❌|                  |❌|                  `GH-69988`_
**NavigationObstacle2D**
Property ``estimate_radius`` removed                                                                                      |❌|                 |❌|                  |❌|                  `GH-69988`_
Method ``get_rid`` renamed to ``get_agent_rid``                                                                           |❌|                 |❌|                  |❌|                  `GH-69988`_
**NavigationObstacle3D**
Property ``estimate_radius`` removed                                                                                      |❌|                 |❌|                  |❌|                  `GH-69988`_
Method ``get_rid`` renamed to ``get_agent_rid``                                                                           |❌|                 |❌|                  |❌|                  `GH-69988`_
**NavigationServer2D**
Method ``agent_set_callback`` renamed to ``agent_set_avoidance_callback``                                                 |❌|                 |❌|                  |❌|                  `GH-69988`_
Method ``agent_set_target_velocity`` removed                                                                              |❌|                 |❌|                  |❌|                  `GH-69988`_
Method ``agent_set_time_horizon`` split into ``agent_set_time_horizon_agents`` and ``agent_set_time_horizon_obstacles``   |❌|                 |❌|                  |❌|                  `GH-69988`_
**NavigationServer3D**
Method ``agent_set_callback`` renamed to ``agent_set_avoidance_callback``                                                 |❌|                 |❌|                  |❌|                  `GH-69988`_
Method ``agent_set_target_velocity`` removed                                                                              |❌|                 |❌|                  |❌|                  `GH-69988`_
Method ``agent_set_time_horizon`` split into ``agent_set_time_horizon_agents`` and ``agent_set_time_horizon_obstacles``   |❌|                 |❌|                  |❌|                  `GH-69988`_
========================================================================================================================  ===================  ====================  ====================  ===========

Networking
~~~~~~~~~~

========================================================================================================================  ===================  ====================  ====================  ===========
Change                                                                                                                    GDScript Compatible  C# Binary Compatible  C# Source Compatible  Introduced
========================================================================================================================  ===================  ====================  ====================  ===========
**WebRTCPeerConnectionExtension**
Method ``_create_data_channel`` changes return type from ``Object`` to ``WebRTCDataChannel``                              |✔️|                 |❌|                  |✔️|                  `GH-78237`_
========================================================================================================================  ===================  ====================  ====================  ===========

Editor plugins
~~~~~~~~~~~~~~

========================================================================================================================  ===================  ====================  ====================  ===========
Change                                                                                                                    GDScript Compatible  C# Binary Compatible  C# Source Compatible  Introduced
========================================================================================================================  ===================  ====================  ====================  ===========
**AnimationTrackEditPlugin**
Type ``AnimationTrackEditPlugin`` removed                                                                                 |❌|                 |❌|                  |❌|                  `GH-76413`_
**EditorInterface**
Type ``EditorInterface`` changes inheritance from ``Node`` to ``Object``                                                  |✔️|                 |❌|                  |❌|                  `GH-76176`_
Method ``set_movie_maker_enabled`` replaced with ``movie_maker_enabled`` property                                         |✔️|                 |❌|                  |❌|                  `GH-76176`_
Method ``is_movie_maker_enabled`` replaced with ``movie_maker_enabled`` property                                          |✔️|                 |❌|                  |❌|                  `GH-76176`_
**EditorResourcePreviewGenerator**
Method ``_generate`` adds a new ``metadata`` parameter                                                                    |❌|                 |❌|                  |❌|                  `GH-64628`_
Method ``_generate_from_path`` adds a new ``metadata`` parameter                                                          |❌|                 |❌|                  |❌|                  `GH-64628`_
**EditorUndoRedoManager**
Method ``create_action`` adds a new ``backward_undo_ops`` optional parameter                                              |✔️|                 |✔️ with compat|      |✔️|                  `GH-76688`_
========================================================================================================================  ===================  ====================  ====================  ===========


Behavior changes
----------------

In 4.1, some behavior changes have been introduced, which might require you to adjust your project.

==================================================================================================================================================================================================  ===========
Change                                                                                                                                                                                              Introduced
==================================================================================================================================================================================================  ===========
**SubViewportContainer**
When input events should reach SubViewports and their children, ``SubViewportContainer.mouse_filter`` now needs to be ``MOUSE_FILTER_STOP`` or ``MOUSE_FILTER_PASS``. See `GH-79271`_ for details.  `GH-57894`_
Multiple layered ``SubViewportContainer`` nodes, that should all receive mouse input events, now need to be replaced by ``Area2D`` nodes. See `GH-79128`_ for details.                              `GH-57894`_
**Viewport**
``Viewport`` nodes, that have Physics Picking enabled, now automatically set InputEvents as handled. See `GH-79897`_ for workarounds.                                                               `GH-77595`_
==================================================================================================================================================================================================  ===========


.. |❌| replace:: :abbr:`❌ (This API breaks compatibility.)`
.. |✔️| replace:: :abbr:`✔️ (This API does not break compatibility.)`
.. |✔️ with compat| replace:: :abbr:`✔️ (This API does not break compatibility. A compatibility method was added.)`

.. _GH-57894: https://github.com/godotengine/godot/pull/57894
.. _GH-64628: https://github.com/godotengine/godot/pull/64628
.. _GH-69988: https://github.com/godotengine/godot/pull/69988
.. _GH-72152: https://github.com/godotengine/godot/pull/72152
.. _GH-72749: https://github.com/godotengine/godot/pull/72749
.. _GH-72842: https://github.com/godotengine/godot/pull/72842
.. _GH-75017: https://github.com/godotengine/godot/pull/75017
.. _GH-75250: https://github.com/godotengine/godot/pull/75250
.. _GH-75260: https://github.com/godotengine/godot/pull/75260
.. _GH-75746: https://github.com/godotengine/godot/pull/75746
.. _GH-75759: https://github.com/godotengine/godot/pull/75759
.. _GH-76082: https://github.com/godotengine/godot/pull/76082
.. _GH-76176: https://github.com/godotengine/godot/pull/76176
.. _GH-76401: https://github.com/godotengine/godot/pull/76401
.. _GH-76413: https://github.com/godotengine/godot/pull/76413
.. _GH-76418: https://github.com/godotengine/godot/pull/76418
.. _GH-76688: https://github.com/godotengine/godot/pull/76688
.. _GH-76794: https://github.com/godotengine/godot/pull/76794
.. _GH-77143: https://github.com/godotengine/godot/pull/77143
.. _GH-77595: https://github.com/godotengine/godot/pull/77595
.. _GH-78237: https://github.com/godotengine/godot/pull/78237
.. _GH-79128: https://github.com/godotengine/godot/issues/79128
.. _GH-79271: https://github.com/godotengine/godot/issues/79271
.. _GH-79897: https://github.com/godotengine/godot/issues/79897

.. _updating_your_gdextension_for_godot_4_1:

Updating your GDExtension for 4.1
---------------------------------

In order to fix a serious bug, in Godot 4.1 we had to break binary compatibility in a big
way and source compatibility in a small way.

This means that GDExtensions made for Godot 4.0 will need to be recompiled for Godot 4.1
(using the  ``4.1`` branch of godot-cpp), with a small change to their source code.

In Godot 4.0, your "entry_symbol" function looks something like this:

.. code-block:: cpp

  GDExtensionBool GDE_EXPORT example_library_init(const GDExtensionInterface *p_interface, const GDExtensionClassLibraryPtr p_library, GDExtensionInitialization *r_initialization) {
      godot::GDExtensionBinding::InitObject init_obj(p_interface, p_library, r_initialization);

      init_obj.register_initializer(initialize_example_module);
      init_obj.register_terminator(uninitialize_example_module);
      init_obj.set_minimum_library_initialization_level(MODULE_INITIALIZATION_LEVEL_SCENE);

      return init_obj.init();
  }

However, for Godot 4.1, it should look like:

.. code-block:: cpp

  GDExtensionBool GDE_EXPORT example_library_init(GDExtensionInterfaceGetProcAddress p_get_proc_address, const GDExtensionClassLibraryPtr p_library, GDExtensionInitialization *r_initialization) {
      godot::GDExtensionBinding::InitObject init_obj(p_get_proc_address, p_library, r_initialization);

      init_obj.register_initializer(initialize_example_module);
      init_obj.register_terminator(uninitialize_example_module);
      init_obj.set_minimum_library_initialization_level(MODULE_INITIALIZATION_LEVEL_SCENE);

      return init_obj.init();
  }

There are two small changes:

#. The first argument changes from ``const GDExtensionInterface *p_interface`` to ``GDExtensionInterfaceGetProcAddress p_get_proc_address``
#. The constructor for the `init_obj` variable now receives ``p_get_proc_address`` as its first parameter

You also need to add an extra ``compatibility_minimum`` line to your ``.gdextension`` file, so that it looks something like:

::

  [configuration]

  entry_symbol = "example_library_init"
  compatibility_minimum = 4.1

This lets Godot know that your GDExtension has been updated and is safe to load in Godot 4.1.
