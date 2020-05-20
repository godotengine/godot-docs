Procedural geometry
===================

There are many ways to procedurally generate geometry in Godot. In this tutorial series
we will explore a few of them. Each technique has its own benefits and drawbacks, so
it is best to understand each one and how it can be useful in a given situation.

.. toctree::
   :maxdepth: 1
   :name: toc-procedural_geometry

   arraymesh
   meshdatatool
   surfacetool
   immediategeometry

What is geometry?
-----------------

Geometry is a fancy way of saying shape. In computer graphics, geometry is typically represented
by an array of positions called "vertices". In Godot, geometry is represented by Meshes.

What is a Mesh?
---------------

Many things in Godot have mesh in their name: the :ref:`Mesh <class_Mesh>`, the :ref:`ArrayMesh <class_ArrayMesh>`,
the :ref:`MeshInstance <class_MeshInstance>`, the :ref:`MultiMesh <class_MultiMesh>`, and
the :ref:`MultiMeshInstance <class_MultiMeshInstance>`. While they are all related, they have slightly different uses.

Meshes and ArrayMeshes are resources that are drawn using a MeshInstance node. Resources like
Meshes and ArrayMeshes cannot be added to the scene directly. A MeshInstance represents one
instance of a mesh in your scene. You can reuse a single mesh in multiple MeshInstances
to draw it in different parts of your scene with different materials or transformations (scale,
rotation, position etc.).

If you are going to draw the same object many times, it can be helpful to use a MultiMesh with
a MultiMeshInstance. The MultiMeshInstance draws meshes thousands of times very
cheaply. It takes advantage of hardware instancing in order to do so. The drawback with
using a MultiMeshInstance is that you are limited to one material for all instances. It uses an
instance array to store different colors and transformations for each instance, but all the
instances use the same material.

What a Mesh is
--------------

A Mesh is composed of one or more surfaces. A surface is an array composed of multiple sub-arrays
containing vertices, normals, UVs, etc. Normally the process of constructing surfaces and meshes is
hidden from the user in the :ref:`VisualServer <class_VisualServer>`, but with ArrayMeshes, the user can construct a Mesh
manually by passing in an array containing the surface information.

Surfaces
^^^^^^^^

Each surface has its own material. Alternatively, you can override the material for all surfaces
in the Mesh when you use a MeshInstance using ``MeshInstance.override_material``.

Surface array
^^^^^^^^^^^^^

The surface array is an array of length ``ArrayMesh.ARRAY_MAX``. Each position in the array is
filled with a sub-array containing per-vertex information. For example, the array located at
``ArrayMesh.ARRAY_NORMAL`` is a :ref:`PoolVector3Array <class_PoolVector3Array>` of vertex normals.

The surface array can be indexed or non-indexed. Creating a non-indexed array is as easy as not assigning
an array at the index ``ArrayMesh.ARRAY_INDEX``. A non-indexed array stores unique vertex information for
every triangle, meaning that when two triangle share a vertex, the vertex is duplicated in the array. An
indexed surface array only stores vertex information for each unique vertex and then also stores an array
of indices which maps out how to construct the triangles from the vertex array. In general, using an indexed
array is faster, but it means you have to share vertex data between triangles, which is not always desired
(e.g. when you want per-face normals).

Tools
-----

Godot provides different ways of accessing and working with geometry. More information on each will
be provided in the following tutorials.

ArrayMesh
^^^^^^^^^

The ArrayMesh resource extends Mesh to add a few different quality of life functions, and most
importantly, the ability to construct a Mesh surface through scripting.

For more information about the ArrayMesh, please see the :ref:`ArrayMesh tutorial <doc_arraymesh>`.

MeshDataTool
^^^^^^^^^^^^

The MeshDataTool is a resource that converts Mesh data into arrays of vertices, faces, and edges that can
be modified at runtime.

For more information about the MeshDataTool, please see the :ref:`MeshDataTool tutorial <doc_meshdatatool>`.

SurfaceTool
^^^^^^^^^^^

The SurfaceTool allows the creation of Meshes using an OpenGL 1.x immediate mode style interface.

For more information about the SurfaceTool, please see the :ref:`SurfaceTool tutorial <doc_surfacetool>`.

ImmediateGeometry
^^^^^^^^^^^^^^^^^

ImmediateGeometry is a node that uses an immediate mode style interface (like SurfaceTool) to draw objects. The
difference between ImmediateGeometry and the SurfaceTool is that ImmediateGeometry is a node itself that can be
added to the scene tree and is drawn directly from the code. The SurfaceTool generates a Mesh that needs to be added
a MeshInstance to be seen.

ImmediateGeometry is useful for prototyping because of the straightforward API, but it is slow because the geometry
is rebuilt every frame. It is most useful for quickly adding simple geometry to debug visually (e.g. by drawing lines to
visualize physics raycasts etc.).

For more information about ImmediateGeometry, please see the :ref:`ImmediateGeometry tutorial <doc_immediategeometry>`.

Which one should I use?
-----------------------

Which method you use depends on what you are trying to do and what kind of procedure you are comfortable with.

Both SurfaceTool and ArrayMesh are excellent for generating static geometry (meshes) that don't change over time.

Using an ArrayMesh is slightly faster than using a SurfaceTool, but the API is more a little more challenging.
Additionally, SurfaceTool has a few quality of life methods such as ``generate_normals()`` and ``index()``.

ImmediateGeometry regenerates the mesh every frame, so it is much slower than ArrayMesh or SurfaceTool. However, if you
need the geometry to change every frame anyway it provides a much easier interface that may even be a little faster than generating
an ArrayMesh every frame.

The MeshDataTool is not fast, but it gives you access to all kinds of properties of the mesh that you don't get with the others
(edges, faces, etc.). It is incredibly useful when you need that sort of data to transform the mesh, but it is not a good idea
to use if that information is not needed. The MeshDataTool is best used if you are going to be using an algorithm that requires
access to the face or edge array.
