:allow_comments: False

.. _doc_procedural_geometry:

Procedural geometry
===================

There are many ways to procedurally generate geometry in Godot. In this tutorial series,
we will explore a few of them. Each technique has its own benefits and drawbacks, so
it is best to understand each one and how it can be useful in a given situation.

.. toctree::
   :maxdepth: 1
   :name: toc-procedural_geometry

   arraymesh
   meshdatatool
   surfacetool
   immediatemesh

.. note::

      All the procedural geometry generation methods described here run on the
      CPU. Godot doesn't support generating geometry on the GPU yet.

What is geometry?
-----------------

Geometry is a fancy way of saying shape. In computer graphics, geometry is typically represented
by an array of positions called "vertices". In Godot, geometry is represented by Meshes.

What is a Mesh?
---------------

Many things in Godot have mesh in their name: the :ref:`Mesh <class_Mesh>`, the
:ref:`ArrayMesh <class_ArrayMesh>`, the :ref:`ImmediateMesh
<class_ImmediateMesh>`, the :ref:`MeshInstance3D <class_MeshInstance3D>`, the
:ref:`MultiMesh <class_MultiMesh>`, and the :ref:`MultiMeshInstance3D
<class_MultiMeshInstance3D>`. While they are all related, they have slightly
different uses.

Meshes and ArrayMeshes are resources that are drawn using a MeshInstance3D node. Resources like
Meshes and ArrayMeshes cannot be added to the scene directly. A MeshInstance3D represents one
instance of a mesh in your scene. You can reuse a single mesh in multiple MeshInstance3Ds
to draw it in different parts of your scene with different materials or transformations (scale,
rotation, position etc.).

If you are going to draw the same object many times, it can be helpful to use a MultiMesh with
a MultiMeshInstance3D. MultiMeshInstance3Ds draw meshes thousands of times very
cheaply by taking advantage of hardware instancing. The drawback with
using a MultiMeshInstance3D is that each of your mesh's surfaces are limited to one material for
all instances. It uses an instance array to store different colors and transformations for each
instance, but all the instances of each surface use the same material.

What a Mesh is
--------------

A Mesh is composed of one or more surfaces. A surface is an array composed of multiple sub-arrays
containing vertices, normals, UVs, etc. Normally the process of constructing surfaces and meshes is
hidden from the user in the :ref:`RenderingServer <class_RenderingServer>`, but with ArrayMeshes, the user can construct a Mesh
manually by passing in an array containing the surface information.

Surfaces
^^^^^^^^

Each surface has its own material. Alternatively, you can override the material for all surfaces
in the Mesh when you use a MeshInstance3D using the :ref:`material_override <class_GeometryInstance3D_property_material_override>` property.

Surface array
^^^^^^^^^^^^^

The surface array is an array of length ``ArrayMesh.ARRAY_MAX``. Each position in the array is
filled with a sub-array containing per-vertex information. For example, the array located at
``ArrayMesh.ARRAY_NORMAL`` is a :ref:`PackedVector3Array <class_PackedVector3Array>` of vertex normals.
See :ref:`Mesh.ArrayType <enum_Mesh_ArrayType>` for more information.

The surface array can be indexed or non-indexed. Creating a non-indexed array is as easy as not assigning
an array at the index ``ArrayMesh.ARRAY_INDEX``. A non-indexed array stores unique vertex information for
every triangle, meaning that when two triangles share a vertex, the vertex is duplicated in the array. An
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

The ArrayMesh resource extends Mesh to add a few different quality of life functions and, most
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

ImmediateMesh
^^^^^^^^^^^^^

ImmediateMesh is a mesh that uses an immediate mode style interface (like
SurfaceTool) to draw objects. The difference between ImmediateMesh and the
SurfaceTool is that ImmediateMesh is drawn directly with code dynamically, while
the SurfaceTool is used to generate a Mesh that you can do whatever you want
with.

ImmediateMesh is useful for prototyping because of its straightforward API, but
it is slow because the geometry is rebuilt each time you make a change. It is
most useful for adding simple geometry for visual debugging (e.g. by drawing
lines to visualize physics raycasts etc.).

For more information about ImmediateMesh, please see the :ref:`ImmediateMesh tutorial <doc_immediatemesh>`.

Which one should I use?
-----------------------

Which approach you use depends on what you are trying to do and what kind of procedure you are comfortable with.

Both SurfaceTool and ArrayMesh are excellent for generating static geometry (meshes) that don't change over time.

Using an ArrayMesh is slightly faster than using a SurfaceTool, but the API is a little more challenging.
Additionally, SurfaceTool has a few quality of life methods such as ``generate_normals()`` and ``index()``.

ImmediateMesh is more limited than both ArrayMesh and SurfaceTool. However, if
you need the geometry to change every frame anyway, it provides a much easier
interface that can be slightly faster than generating an ArrayMesh every frame.

The MeshDataTool is not fast, but it gives you access to all kinds of properties of the mesh that you don't get with the others
(edges, faces, etc.). It is incredibly useful when you need that sort of data to transform the mesh, but it is not a good idea
to use it if that extra information is not needed. The MeshDataTool is best used if you are going to be using an algorithm that requires
access to the face or edge array.
