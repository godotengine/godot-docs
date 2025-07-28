.. _doc_upgrading_to_godot_4.4:

Upgrading from Godot 4.3 to Godot 4.4
=====================================

For most games and apps made with 4.3 it should be relatively safe to migrate to 4.4.
This page intends to cover everything you need to pay attention to when migrating
your project.

Breaking changes
----------------

If you are migrating from 4.3 to 4.4, the breaking changes listed here might
affect you. Changes are grouped by areas/systems.

This article indicates whether each breaking change affects GDScript and whether
the C# breaking change is *binary compatible* or *source compatible*:

- **Binary compatible** - Existing binaries will load and execute successfully without
  recompilation, and the run-time behavior won't change.
- **Source compatible** - Source code will compile successfully without changes when
  upgrading Godot.

Core
~~~~

========================================================================================================================  ===================  ====================  ====================  ============
Change                                                                                                                    GDScript Compatible  C# Binary Compatible  C# Source Compatible  Introduced
========================================================================================================================  ===================  ====================  ====================  ============
**FileAccess**
Method ``open_encrypted`` adds a new ``iv`` optional parameter                                                            |✔️|                 |✔️ with compat|      |✔️ with compat|      `GH-98918`_
Method ``store_8`` changes return type from ``void`` to ``bool``                                                          |✔️|                 |❌|                  |✔️|                  `GH-78289`_
Method ``store_16`` changes return type from ``void`` to ``bool``                                                         |✔️|                 |❌|                  |✔️|                  `GH-78289`_
Method ``store_32`` changes return type from ``void`` to ``bool``                                                         |✔️|                 |❌|                  |✔️|                  `GH-78289`_
Method ``store_64`` changes return type from ``void`` to ``bool``                                                         |✔️|                 |❌|                  |✔️|                  `GH-78289`_
Method ``store_buffer`` changes return type from ``void`` to ``bool``                                                     |✔️|                 |❌|                  |✔️|                  `GH-78289`_
Method ``store_csv_line`` changes return type from ``void`` to ``bool``                                                   |✔️|                 |❌|                  |✔️|                  `GH-78289`_
Method ``store_double`` changes return type from ``void`` to ``bool``                                                     |✔️|                 |❌|                  |✔️|                  `GH-78289`_
Method ``store_float`` changes return type from ``void`` to ``bool``                                                      |✔️|                 |❌|                  |✔️|                  `GH-78289`_
Method ``store_half`` changes return type from ``void`` to ``bool``                                                       |✔️|                 |❌|                  |✔️|                  `GH-78289`_
Method ``store_line`` changes return type from ``void`` to ``bool``                                                       |✔️|                 |❌|                  |✔️|                  `GH-78289`_
Method ``store_pascal_string`` changes return type from ``void`` to ``bool``                                              |✔️|                 |❌|                  |✔️|                  `GH-78289`_
Method ``store_real`` changes return type from ``void`` to ``bool``                                                       |✔️|                 |❌|                  |✔️|                  `GH-78289`_
Method ``store_string`` changes return type from ``void`` to ``bool``                                                     |✔️|                 |❌|                  |✔️|                  `GH-78289`_
Method ``store_var`` changes return type from ``void`` to ``bool``                                                        |✔️|                 |❌|                  |✔️|                  `GH-78289`_
**OS**
Method ``execute_with_pipe`` adds a new ``blocking`` optional parameter                                                   |✔️|                 |✔️ with compat|      |✔️ with compat|      `GH-94434`_
Method ``read_string_from_stdin`` adds a new ``buffer_size`` parameter [#f1]_                                             |❌|                 |✔️ with compat|      |✔️ with compat|      `GH-91201`_
**RegEx**
Method ``compile`` adds a new ``show_error`` optional parameter                                                           |✔️|                 |✔️ with compat|      |✔️ with compat|      `GH-95212`_
Method ``create_from_string`` adds a new ``show_error`` optional parameter                                                |✔️|                 |✔️ with compat|      |✔️ with compat|      `GH-95212`_
**Semaphore**
Method ``post`` adds a new ``count`` optional parameter                                                                   |✔️|                 |✔️ with compat|      |✔️ with compat|      `GH-93605`_
**TranslationServer**
Method ``standardize_locale`` adds a new ``add_defaults`` optional parameter                                              |✔️|                 |✔️ with compat|      |✔️ with compat|      `GH-98972`_
========================================================================================================================  ===================  ====================  ====================  ============

**Export annotations**

.. warning::

    The behavior of ``@export_file`` changed in Godot 4.4. When assigning a new value
    from the Inspector, the path is now stored and returned as a ``uid://`` reference
    instead of the traditional ``res://`` path(`GH-97912`_). This is a **breaking change** and may
    cause issues if you're expecting ``res://``-based paths in scripts or serialized
    files.

    For example, exported arrays of files may now contain a mix of ``uid://`` and
    ``res://`` paths, especially if they were partially edited in the Inspector.

    In 4.4, the only way to retain the ``res://`` format is to **manually edit** the
    `.tscn` or `.tres` files in a text editor. Starting in Godot 4.5, a new annotation
    ``@export_file_path`` can be used to explicitly retain the old behavior and export
    raw ``res://`` paths.

.. [#f1] Default buffer size in 4.3 is ``1024``.


GUI nodes
~~~~~~~~~

========================================================================================================================  ===================  ====================  ====================  ============
Change                                                                                                                    GDScript Compatible  C# Binary Compatible  C# Source Compatible  Introduced
========================================================================================================================  ===================  ====================  ====================  ============
**RichTextLabel**
Method ``push_meta`` adds a new ``tooltip`` optional parameter                                                            |✔️|                 |✔️ with compat|      |✔️ with compat|      `GH-99481`_
Method ``set_table_column_expand`` adds a new ``shrink`` optional parameter                                               |✔️|                 |✔️ with compat|      |✔️ with compat|      `GH-101482`_
**GraphEdit**
Method ``connect_node`` adds a new ``keep_alive`` optional parameter                                                      |✔️|                 |✔️ with compat|      |✔️ with compat|      `GH-97449`_
Signal ``frame_rect_changed`` changes ``new_rect`` parameter type from ``Vector2`` to ``Rect2``                           |❌|                 |❌|                  |❌|                  `GH-102796`_
========================================================================================================================  ===================  ====================  ====================  ============

Physics
~~~~~~~

========================================================================================================================  ===================  ====================  ====================  ============
Change                                                                                                                    GDScript Compatible  C# Binary Compatible  C# Source Compatible  Introduced
========================================================================================================================  ===================  ====================  ====================  ============
**SoftBody3D**
Method ``set_point_pinned`` adds a new ``insert_at`` optional parameter                                                   |✔️|                 |✔️ with compat|      |✔️ with compat|      `GH-94684`_
========================================================================================================================  ===================  ====================  ====================  ============

Rendering
~~~~~~~~~

========================================================================================================================  ===================  ====================  ====================  ============
Change                                                                                                                    GDScript Compatible  C# Binary Compatible  C# Source Compatible  Introduced
========================================================================================================================  ===================  ====================  ====================  ============
**CPUParticles2D**
Method ``restart`` adds a new ``keep_seed`` optional parameter                                                            |✔️|                 |✔️ with compat|      |✔️ with compat|      `GH-92089`_
**CPUParticles3D**
Method ``restart`` adds a new ``keep_seed`` optional parameter                                                            |✔️|                 |✔️ with compat|      |✔️ with compat|      `GH-92089`_
**GPUParticles2D**
Method ``restart`` adds a new ``keep_seed`` optional parameter                                                            |✔️|                 |✔️ with compat|      |✔️ with compat|      `GH-92089`_
**GPUParticles3D**
Method ``restart`` adds a new ``keep_seed`` optional parameter                                                            |✔️|                 |✔️ with compat|      |✔️ with compat|      `GH-92089`_
**RenderingDevice**
Method ``draw_list_begin`` adds a new ``breadcrumb`` optional parameter                                                   |✔️|                 |✔️ with compat|      |✔️ with compat|      `GH-90993`_
Method ``draw_list_begin`` removes many parameters                                                                        |❌|                 |✔️ with compat|      |✔️ with compat|      `GH-98670`_
Method ``index_buffer_create`` adds a new ``enable_device_address`` optional parameter                                    |✔️|                 |✔️ with compat|      |✔️ with compat|      `GH-100062`_
Method ``uniform_buffer_create`` adds a new ``enable_device_address`` optional parameter                                  |✔️|                 |✔️ with compat|      |✔️ with compat|      `GH-100062`_
Method ``vertex_buffer_create`` adds a new ``enable_device_address`` optional parameter                                   |✔️|                 |✔️ with compat|      |✔️ with compat|      `GH-100062`_
**RenderingServer**
Method ``multimesh_allocate_data`` adds a new ``use_indirect`` optional parameter                                         |✔️|                 |✔️ with compat|      |✔️ with compat|      `GH-99455`_
**Shader**
Method ``get_default_texture_parameter`` changes return type from ``Texture2D`` to ``Texture``                            |✔️|                 |❌|                  |❌|                  `GH-95126`_
Method ``set_default_texture_parameter`` changes ``texture`` parameter type from ``Texture2D`` to ``Texture``             |✔️|                 |❌|                  |✔️|                  `GH-95126`_
**VisualShaderNodeCubemap**
Property ``cube_map`` changes type from ``Cubemap`` to ``TextureLayered``                                                 |✔️|                 |❌|                  |❌|                  `GH-95126`_
**VisualShaderNodeTexture2DArray**
Property ``texture_array`` changes type from ``Texture2DArray`` to ``TextureLayered``                                     |✔️|                 |❌|                  |❌|                  `GH-95126`_
========================================================================================================================  ===================  ====================  ====================  ============

.. note::

    In C#, the enum ``RenderingDevice.StorageBufferUsage`` breaks compatibility because of the way the bindings generator
    detects the enum prefix. New members where added in `GH-100062`_ to the enum that caused the enum members to be renamed.

Navigation
~~~~~~~~~~

========================================================================================================================  ===================  ====================  ====================  ============
Change                                                                                                                    GDScript Compatible  C# Binary Compatible  C# Source Compatible  Introduced
========================================================================================================================  ===================  ====================  ====================  ============
**NavigationServer2D**
Method ``query_path`` adds a new ``callback`` optional parameter                                                          |✔️|                 |✔️ with compat|      |✔️ with compat|      `GH-100129`_
**NavigationServer3D**
Method ``query_path`` adds a new ``callback`` optional parameter                                                          |✔️|                 |✔️ with compat|      |✔️ with compat|      `GH-100129`_
========================================================================================================================  ===================  ====================  ====================  ============

Editor plugins
~~~~~~~~~~~~~~

========================================================================================================================  ===================  ====================  ====================  ============
Change                                                                                                                    GDScript Compatible  C# Binary Compatible  C# Source Compatible  Introduced
========================================================================================================================  ===================  ====================  ====================  ============
**EditorInterface**
Method ``open_scene_from_path`` adds a new ``set_inherited`` optional parameter                                           |✔️|                 |✔️ with compat|      |✔️ with compat|      `GH-90057`_
Method ``popup_node_selector`` adds a new ``current_value`` optional parameter                                            |✔️|                 |✔️ with compat|      |✔️ with compat|      `GH-94323`_
Method ``popup_property_selector`` adds a new ``current_value`` optional parameter                                        |✔️|                 |✔️ with compat|      |✔️ with compat|      `GH-94323`_
**EditorSceneFormatImporter**
Method ``_get_import_flags`` removed                                                                                      |❌|                 |❌|                  |❌|                  `GH-101531`_
**EditorTranslationParserPlugin**
Method ``_parse_file`` changes return type to ``Array`` and removes ``msgids`` and ``msgids_context_plural`` parameters   |❌|                 |❌|                  |❌|                  `GH-99297`_
========================================================================================================================  ===================  ====================  ====================  ============

.. note::

    The method ``_get_import_flags`` was never used by the engine. It was removed despite the
    compatibility breakage as there's no way for users to rely on this affecting engine behavior.

Behavior changes
----------------

Core
~~~~

.. note::

    The ``Curve`` resource now enforces its value range, so ``min_value`` and ``max_value`` need to be changed
    if any of the points fall outside of the default ``[0, 1]`` range.

Rendering
~~~~~~~~~

.. note::

    The ``VisualShaderNodeVec4Constant`` shader node had its input type changed to ``Vector4``. Users need to
    recreate the values in their constants.

CSG
~~~

.. note::

    The CSG implementation now uses Emmett Lalish's `Manifold <https://github.com/elalish/manifold>`_ library (`GH-94321`_).
    The new implementation is more consistent with manifold definitions and fixes a number of bugs and stability
    issues. As a result, non-manifold meshes are no longer supported. You can use ``MeshInstance3D`` for
    rendering non-manifold geometry, such as quads or planes.

Android
~~~~~~~

.. note::

    Android sensor events are no longer enabled by default (`GH-94799`_). Projects that use sensor events can
    enable them as needed in Project Settings under **Input Devices > Sensors**.

.. |❌| replace:: :abbr:`❌ (This API breaks compatibility.)`
.. |✔️| replace:: :abbr:`✔️ (This API does not break compatibility.)`
.. |✔️ with compat| replace:: :abbr:`✔️ (This API does not break compatibility. A compatibility method was added.)`

.. _GH-78289: https://github.com/godotengine/godot/pull/78289
.. _GH-90057: https://github.com/godotengine/godot/pull/90057
.. _GH-90993: https://github.com/godotengine/godot/pull/90993
.. _GH-91201: https://github.com/godotengine/godot/pull/91201
.. _GH-92089: https://github.com/godotengine/godot/pull/92089
.. _GH-93605: https://github.com/godotengine/godot/pull/93605
.. _GH-94321: https://github.com/godotengine/godot/pull/94321
.. _GH-94323: https://github.com/godotengine/godot/pull/94323
.. _GH-94434: https://github.com/godotengine/godot/pull/94434
.. _GH-99455: https://github.com/godotengine/godot/pull/99455
.. _GH-94684: https://github.com/godotengine/godot/pull/94684
.. _GH-94799: https://github.com/godotengine/godot/pull/94799
.. _GH-95212: https://github.com/godotengine/godot/pull/95212
.. _GH-95126: https://github.com/godotengine/godot/pull/95126
.. _GH-97449: https://github.com/godotengine/godot/pull/97449
.. _GH-97912: https://github.com/godotengine/godot/pull/97912
.. _GH-98670: https://github.com/godotengine/godot/pull/98670
.. _GH-98918: https://github.com/godotengine/godot/pull/98918
.. _GH-98972: https://github.com/godotengine/godot/pull/98972
.. _GH-99297: https://github.com/godotengine/godot/pull/99297
.. _GH-99481: https://github.com/godotengine/godot/pull/99481
.. _GH-100062: https://github.com/godotengine/godot/pull/100062
.. _GH-100129: https://github.com/godotengine/godot/pull/100129
.. _GH-101482: https://github.com/godotengine/godot/pull/101482
.. _GH-101531: https://github.com/godotengine/godot/pull/101531
.. _GH-102796: https://github.com/godotengine/godot/pull/102796
