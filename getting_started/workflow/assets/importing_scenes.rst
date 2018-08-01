.. _doc_importing_3d_scenes:

Importing 3D Scenes
===================

Godot Scene Importer
--------------------

When dealing with 3D assets, Godot has a flexible and configurable importer.

Godot works with *scenes*. This means that the entire scene being worked on in your favorite 3D DCC will be
transferred as close as possible.

Godot supports the following 3D *scene file fomats*: 

* DAE (Collada), which is currently the most mature workflow.
* GLTF 2.0. Both text and binary formats are supported. Godot has full support for it, but the format is new and gaining traction.
* OBJ (Wavefront) formats. It is also fully supported, but pretty limited (no support for pivots, skeletons, etc).

Just copy the scene file together with the texture to the project repository, and Godot will do a full import.

Why not FBX?
~~~~~~~~~~~~

Most game engines use the FBX format for importing 3D scenes, which is
definitely one of the most standardized in the industry. However, this
format requires the use of a closed library from Autodesk which is
distributed with a more restrictive licensing terms than Godot. 

The plan is, sometime in the future, to offer a binary plug-in using GDNative.

Exporting DAE files from Maya and 3DS Max
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Autodesk added built-in collada support to Maya and 3DS Max, but it's
broken by default and should not be used. The best way to export this format
is by using the
`OpenCollada <https://github.com/KhronosGroup/OpenCOLLADA/wiki/OpenCOLLADA-Tools>`__
plugins. They work well, although they are not always up-to date
with the latest version of the software.

Exporting DAE files from Blender
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Blender has built-in collada support too, but it's also broken and
should not be used.

Godot provides a `Python
Plugin <https://github.com/godotengine/collada-exporter>`__
that will do a much better job of exporting the scenes.

Exporting ESCN files from Blender
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The most powerful one, called `godot-blender-exporter
<https://github.com/godotengine/godot-blender-exporter>`__. 
It uses .escn files which is kind of another name of .tscn file(Godot scene file),
it keeps as much information as possible from a Blender scene.

ESCN exporter has a detailed `document <escn_exporter/index.html>`__ describing
its functionality and usage.

Import workflows
----------------

Godot scene importer allows different workflows regarding how data is imported. Depending on many options, it is possible to
import a scene with:

* External materials (default): Where each material is saved to a file resource. Modifications to them are kept.
* External meshes: Where each mesh is saved to a different file. Many users prefer to deal with meshes directly.
* External animations: Allowing saved animations to be modified and merged when sources change.
* External scenes: Save the root nodes of the imported scenes each as a separate scene.
* Single Scene: A single scene file with everything built in.

.. image:: img/scene_import1.png

As different developers have different needs, this import process is highly customizable.

Import Options
---------------

The importer has several options, which will be discussed below:

.. image:: img/scene_import2.png

Nodes:
~~~~~~~

Root Type
^^^^^^^^^

By default, the type of the root node in imported scenes is "Spatial", but this can be modified.

Root Name
^^^^^^^^^

Allows setting a specific name to the generated root node.

Custom Script
^^^^^^^^^^^^^

A special script to process the whole scene after import can be provided. 
This is great for post processing, changing materials, doing funny stuff
with the geometry etc.

Create a script that like this:

::

    tool # needed so it runs in editor
    extends EditorScenePostImport

    func post_import(scene):
      # do your stuff here
      return scene # remember to return the imported scene

The post-import function takes the imported scene as argument (the
parameter is actually the root node of the scene). The scene that
will finally be used must be returned. It can be a different one.

Storage
^^^^^^^

By default, Godot imports a single scene. This option allows specifying
that nodes below the root will each be a separate scene and instanced
into the imported one. 

Of course, instancing such imported scenes in other places manually works too.


Materials 
~~~~~~~~~

Location
^^^^^^^^

Godot supports materials in meshes or nodes. By default, materials will be put
on each node.

Storage
^^^^^^^

Materials can be stored within the scene or in external files. By default,
they are stored in external files so editing them is possible. This is because
most 3D DCCs don't have the same material options as those present in Godot.

When materials are built-in, they will be lost each time the source scene
is modified and re-imported.

Keep on Reimport
^^^^^^^^^^^^^^^^

Once materials are edited to use Godot features, the importer will keep the
edited ones and ignore the ones coming from the source scene. This option
is only present if materials are saved as files.

Compress
^^^^^^^^

Makes meshes use less precise numbers for multiple aspects of the mesh in order
to save space.

These are:
 * Transform Matrix (Location, rotation, and scale)             : 32-bit float to 16-bit signed integer.
 * Vertices                                                     : 32-bit float to 16-bit signed integer.
 * Normals                                                      : 32-bit float to 32-bit unsigned integer.
 * Tangents                                                     : 32-bit float to 32-bit unsigned integer.
 * Vertex Colors                                                : 32-bit float to 32-bit unsigned integer.
 * UV                                                           : 32-bit float to 32-bit unsigned integer.
 * UV2                                                          : 32-bit float to 32-bit unsigned integer.
 * Vertex weights                                               : 32-bit float to 16-bit unsigned integer.
 * Armature bones                                               : 32-bit float to 16-bit unsigned integer.
 * Array index                                                  : 32-bit or 16-bit unsigned integer based on how many elements there are.

Additional info:
 * UV2 = The second UV channel for detail textures and baked lightmap textures.
 * Array index = An array of numbers that number each element of the arrays above; i.e. they number the vertices and normals.

In some cases, this might lead to loss of precision so disabling this option
may be needed. For instance, if a mesh is very big or there are multiple meshes
being imported that cover a large area, compressing the import of this mesh(s)
may lead to gaps in geometry or vertices not being exactly where they should be.

Meshes
~~~~~~~

Ensure Tangents
^^^^^^^^^^^^^^^

If textures with normalmapping are to be used, meshes need to have tangent arrays.
This option ensures that these are generated if not present in the source scene.
Godot uses Mikktspace for this, but it's always better to have them generated in
the exporter.

Storage
^^^^^^^

Meshes can be stored in separate files (resources) instead of built-in. This does
not have much practical use unless one wants to build objects with them directly.

This option is provided to help those who prefer working directly with meshes
instead of scenes.

External Files
~~~~~~~~~~~~~~

Generated meshes and materials can be optionally stored in a subdirectory with the
name of the scene.

Animation Options
------------------

Godot provides many options regarding how animation data is dealt with. Some exporters
(such as Blender), can generate many animations in a single file. Others, such as
3DS Max or Maya, need many animations put into the same timeline or, at worst, put
each animation in a separate file.

.. image:: img/scene_import3.png

Import of animations is enabled by default.

FPS
~~~~~~~~~~~~~~~

Most 3D export formats store animation timeline in seconds instead of frames. To ensure
animations are imported as faithfully as possible, please specify the frames per second
used to edit them. Failing to do this may result in minimal jitter.

Filter Script
~~~~~~~~~~~~~~~~~~~~~~~~~

It is possible to specify a filter script in a special syntax to decide which tracks from which
animations should be kept. (@TODO this needs documentation)

Storage
~~~~~~~~~~~~~~~~~~~

By default, animations are saved as built-in. It is possible to save them to a file instead. This
allows adding custom tracks to the animations and keeping them after a reimport.


Optimizer
~~~~~~~~~~~~~~~~~~~~~

When animations are imported, an optimizer is run which reduces the size of the animation considerably.
In general, this should always be turned on unless you suspect that an animation might be broken due to it being enabled.

Clips
~~~~~~~~~~~~~~~~~~~~~

It is possible to specify multiple animations from a single timeline as clips. Specify from which frame to which frame each
clip must be taken (and, of course, don't forget to specify the FPS option above).

Scene Inheritance
-----------------

In many cases, it may be desired to do modifications to the imported scene. By default, this is not possible because
if the source asset changes (source .dae,.gltf,.obj file re-exported from 3D modelling app), Godot will re-import the whole scene.

It is possible, however, to do local modifications by using *Scene Inheritance*. Try to open the imported scene and the
following dialog will appear:

.. image:: img/scene_import4.png

In inherited scenes, the only limitations for modifications are: 

* Nodes can't be removed (but can be added anywhere).
* Sub-Resources can't be edited (save them externally as described above for this)

Other than that, everything is allowed!

Import Hints
------------

Many times, when editing a scene, there are common tasks that need to be done after exporting:

* Adding collision detection to objects:
* Setting objects as navigation meshes
* Deleting nodes that are not used in the game engine (like specific lights used for modelling)

To simplify this workflow, Godot offers a few suffixes that can be added to the names of the
objects in your 3D modelling software. When imported, Godot will detect them and perform
actions automatically:

Remove nodes (-noimp)
~~~~~~~~~~~~~~~~~~~~~

Node names that have this suffix will be removed at import time, no
matter what their type is. They will not appear in the imported scene.

Create collisions (-col, -colonly, -convcolonly)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Option "-col" will work only for Mesh nodes. If it is detected, a child
static collision node will be added, using the same geometry as the mesh.

However, it is often the case that the visual geometry is too complex or
too un-smooth for collisions, which ends up not working well. 

To solve this, the "-colonly" modifier exists, which will remove the mesh upon
import and create a :ref:`class_staticbody` collision instead.
This helps the visual mesh and actual collision to be separated.

Option "-convcolonly" will create :ref:`class_convexpolygonshape` instead of :ref:`class_concavepolygonshape`.

Option "-colonly" can be also used with Blender's empty objects.
On import it will create a :ref:`class_staticbody` with
collision node as a child. Collision node will have one of predefined shapes,
depending on the Blender's empty draw type:

.. image:: img/3dimp_BlenderEmptyDrawTypes.png

-  Single arrow will create :ref:`class_rayshape`
-  Cube will create :ref:`class_boxshape`
-  Image will create :ref:`class_planeshape`
-  Sphere (and other non-listed) will create :ref:`class_sphereshape`

For better visibility in Blender's editor user can set "X-Ray" option on collision
empties and set some distinct color for them in User Preferences / Themes / 3D View / Empty.

Create navigation (-navmesh)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A mesh node with this suffix will be converted to a navigation mesh. Original Mesh node will be
removed.

Rigid Body (-rigid)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Creates a rigid body from this mesh.


