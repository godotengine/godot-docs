.. _doc_arraymesh:

Using the ArrayMesh
===================

This tutorial will present the basics of using an :ref:`ArrayMesh <class_arraymesh>`

To do so, we will use the function :ref:`add_surface_from_arrays() <class_ArrayMesh_method_add_surface_from_arrays>`,
which takes up to four parameters. The first two are required, while the second two are optional.

The first is the ``PrimitiveType``, this is an OpenGL concept that instructs the GPU
how to arrange the primitive based on the vertices given whether it is triangles,
lines, points, etc. A complete list can be found under the :ref:`Mesh <class_mesh>`
class reference page.

The second is the actual Array that stores the mesh information. The array is a normal Godot array that
is constructed with empty brackets ``[]``. It stores a ``Pool**Array`` (e.g. PoolVector3Array,
PoolIntArray, etc.) for each type of information.

- ``ARRAY_VERTEX`` = 0 | PoolVector3Array or PoolVector2Array
- ``ARRAY_NORMAL`` = 1 | PoolVector3Array
- ``ARRAY_TANGENT`` = 2 | PoolRealArray of groups of 4 floats. first 3 floats determine the tangent, and
  the last the binormal direction as -1 or 1.
- ``ARRAY_COLOR`` = 3 | PoolColorArray
- ``ARRAY_TEX_UV`` = 4 | PoolVector2Array or PoolVector3Array
- ``ARRAY_TEX_UV2`` = 5 | PoolVector2Array or PoolVector3Array
- ``ARRAY_BONES`` = 6 | PoolRealArray of groups of 4 floats or PoolIntArray of groups of 4 ints
- ``ARRAY_WEIGHTS`` = 7 | PoolRealArray of groups of 4 floats
- ``ARRAY_INDEX`` = 8 | PoolIntArray

The Array of vertices is always required. All the others are optional and will only be used if included.

Each array needs to have the same number of elements as the vertex array except for the index array.
For arrays like tangents, an element is a group of 4 floats. So the array size will be four times
the size of the vertex array size, but they will have the same number of elements

The index array is unique.

The third parameter is an array of blendshapes for the Mesh to use. While this tutorial does not cover
using blendshapes, it is possible to specify them when creating a surface from arrays.

The last parameter is the compress flags which specifies which arrays to store with half as many bits. The
values can be found in the classref for :ref:`VisualServer <class_visualserver>` under :ref:`ArrayFormat <enum_visualserver_arrayformat>`.

For normal usage you will find it is best to leave the last two parameters empty.

ArrayMesh
---------

Add an :ref:`ArrayMesh <class_arraymesh>` to a MeshInstance. Normally, adding an ArrayMesh in
the editor is not useful, but in this case it allows as to access the ArrayMesh from code
without creating one.

Next, add a script to the MeshInstance.

Under ``_ready()``, create a new Array.

.. tabs::
  .. code-tab:: gdscript GDScript

    var arr = []

This will be the array that we keep our surface information in, it will hold
all the arrays of data that the surface needs. Godot will expect it to be of
size ``Mesh.ARRAY_MAX``, so resize it accordingly.

.. tabs::
 .. code-tab:: gdscript GDScript

    var arr = []
    arr.resize(Mesh.ARRAY_MAX)

Next create the arrays for each data type you will use.

.. tabs::
 .. code-tab:: gdscript GDScript

    var verts = PoolVector3Array()
    var uvs = PoolVector2Array()
    var normals = PoolVector3Array()
    var indices = PoolIntArray()

Once you have filled your data arrays with your geometry you can create a mesh
by adding each array to ``surface_array`` and then committing to the mesh.

.. tabs::
 .. code-tab:: gdscript GDScript

    arr[Mesh.ARRAY_VERTEX] = verts
    arr[Mesh.ARRAY_TEX_UV] = uvs
    arr[Mesh.ARRAY_NORMAL] = normals
    arr[Mesh.ARRAY_INDEX] = indices

    mesh.add_surface_from_arrays(Mesh.PRIMITIVE_TRIANGLES, arr) # No blendshapes or compression used.

.. note:: In this example, we used ``Mesh.PRIMITIVE_TRIANGLES``, but you can use any primitive type
          available from mesh.

Put together the full code looks like:

.. tabs::
 .. code-tab:: gdscript GDScript

    extends MeshInstance

    func _ready():
        var arr = []
        arr.resize(Mesh.ARRAY_MAX)

        # PoolVectorXXArrays for mesh construction.
        var verts = PoolVector3Array()
        var uvs = PoolVector2Array()
        var normals = PoolVector3Array()
        var indices = PoolIntArray()

        #######################################
        ## Insert code here to generate mesh ##
        #######################################

        # Assign arrays to mesh array.
        arr[Mesh.ARRAY_VERTEX] = verts
        arr[Mesh.ARRAY_TEX_UV] = uvs
        arr[Mesh.ARRAY_NORMAL] = normals
        arr[Mesh.ARRAY_INDEX] = indices

        # Create mesh surface from mesh array.
        mesh.add_surface_from_arrays(Mesh.PRIMITIVE_TRIANGLES, arr) # No blendshapes or compression used.


The code that goes in the middle can be whatever you want. Below we will present some example code that
could go in the middle.

Generating geometry
-------------------

Here is sample code for generating a sphere. Although the code is presented in
GDScript, there is nothing Godot specific about the approach to generating it.
This implementation has nothing in particular to do with ArrayMeshes and is just a
generic approach to generating a sphere. If you are having trouble understanding it
or want to learn more about procedural geometry in general, you can use any tutorial
that you find online.

.. tabs::
 .. code-tab:: gdscript GDScript

    extends MeshInstance

    var rings = 50
    var radial_segments = 50
    var height = 1
    var radius = 1

    func _ready():

        # Set up the PoolVectorXArrays.

        # Vertex indices.
        var thisrow = 0
        var prevrow = 0
        var point = 0

        # Loop over rings.
        for i in range(rings + 1):
            var v = float(i) / rings
            var w = sin(PI * v)
            var y = cos(PI * v)

            # Loop over segments in ring.
            for j in range(radial_segments):
                var u = float(j) / radial_segments
                var x = sin(u * PI * 2.0)
                var z = cos(u * PI * 2.0)
                var vert = Vector3(x * radius * w, y, z * radius * w)
                verts.append(vert)
                normals.append(vert.normalized())
                uvs.append(Vector2(u, v))
                point += 1

                # Create triangles in ring using indices.
                if i > 0 and j > 0:
                    indices.append(prevrow + j - 1)
                    indices.append(prevrow + j)
                    indices.append(thisrow + j - 1)

                    indices.append(prevrow + j)
                    indices.append(thisrow + j)
                    indices.append(thisrow + j - 1)

            if i > 0:
                indices.append(prevrow + radial_segments - 1)
                indices.append(prevrow)
                indices.append(thisrow + radial_segments - 1)

                indices.append(prevrow)
                indices.append(prevrow + radial_segments)
                indices.append(thisrow + radial_segments - 1)

            prevrow = thisrow
            thisrow = point

      # Commit to the ArrayMesh.

Combined with the code above, this code will generate a sphere.

When it comes to generating geometry with the ArrayMesh you need to understand what goes
in each array and then you can follow tutorials for any language/engine and convert it into Godot.

Saving
------

Finally, Godot provides a single method to save ArrayMeshes using the :ref:`ResourceSaver <class_resourcesaver>`
class. This is useful when you want to generate a mesh and then use it later without having to re-generate.

.. tabs::
 .. code-tab:: gdscript GDScript

    # Saves mesh to a .tres file with compression enabled.
    ResourceSaver.save("res://sphere.tres", mesh, 32)
