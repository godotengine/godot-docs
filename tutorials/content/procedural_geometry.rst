.. _doc_procedural_geometry:

Procedural geometry generation
==============================

Users often ask how to generate geometry from code. This is not very complicated, but it's not obvious.
Godot provides a few classes entirely dedicated to make it this easy. Still, the best tool for the job depends
entirely on the use case.

SurfaceTool
-----------

This is the most common helper. :ref:`SurfaceTool<class_SurfaceTool>` is a class you can instantiate to generate :ref:`Meshes<class_Mesh>`, specifically *Mesh Surfaces*.

It has a similar API to OpenGL 1.x, and it's meant for static content. This means, the mesh is generated once and then used.

Here is a simple example of how to use it to add a single triangle.

.. tabs::
 .. code-tab:: gdscript GDScript

    var st = SurfaceTool.new()

    st.begin(Mesh.PRIMITIVE_TRIANGLE)

    # Prepare attributes for add_vertex.
    st.add_normal(Vector3(0, 0, 1))
    st.add_uv(Vector2(0, 0))
    # Call last for each vertex, adds the above attributes.
    st.add_vertex(Vector3(-1, -1, 0))

    st.add_normal(Vector3(0, 0, 1))
    st.add_uv(Vector2(0, 1))
    st.add_vertex(Vector3(-1, 1, 0))

    st.add_normal(Vector3(0, 0, 1))
    st.add_uv(Vector2(1, 1))
    st.add_vertex(Vector3(1, 1, 0))

    # Create indices, indices are optional.
    st.index()

    # Commit to a mesh.
    var mesh = st.commit()

Just explore the APIs and the possibilities.

ImmediateGeometry
-----------------

Unlike *SurfaceTool*, :ref:`ImmediateGeometry<class_ImmediateGeometry>` is an actual node. It's similar in the "OpenGL 1.x" style API,
but it's actually designed to create content on the fly and modify it every frame efficiently.

Generating complex geometry (several thousand vertices) with this node is inefficient, even if it's done only once. Instead, *ImmediateGeometry* is designed to generate simple geometry that changes every frame.

It's used similar to *SurfaceTool*.

.. tabs::
 .. code-tab:: gdscript GDScript

    extends ImmediateGeometry

    void _process(delta):
        # Clean up before drawing.
        clear()

        # Begin draw.
        begin(Mesh.PRIMITIVE_TRIANGLE)

        # Prepare attributes for add_vertex.
        set_normal( Vector3(0, 0, 1))
        set_uv(Vector2(0, 0))
        # Call last for each vertex, adds the above attributes.
        add_vertex(Vector3(-1, -1, 0))

        set_normal(Vector3(0, 0, 1))
        set_uv(Vector2(0, 1))
        add_vertex(Vector3(-1, 1, 0))

        set_normal(Vector3(0, 0, 1))
        set_uv(Vector2(1, 1))
        add_vertex(Vector3(1, 1, 0))

        # End drawing.
        end()

Arrays
------

Lastly, the final way to do this is to create arrays themselves. This is the most efficient way to create static geometry, and is only
recommended when SurfaceTool is not fast enough.

Similar code as before, but draw a square using indices:


.. tabs::
 .. code-tab:: gdscript GDScript

    var arrays = []
    arrays.resize(Mesh.ARRAY_MAX)

    var normal_array = []
    var uv_array = []
    var vertex_array = []
    var index_array = []

    normal_array.resize(4)
    uv_array.resize(4)
    vertex_array.resize(4)
    index_array.resize(6)

    normal_array[0] = Vector3(0, 0, 1)
    uv_array[0] = Vector2(0, 0)
    vertex_array[0] = Vector3(-1, -1)

    normal_array[1] = Vector3(0, 0, 1)
    uv_array[1] = Vector2(0,1)
    vertex_array[1] = Vector3(-1, 1)

    normal_array[2] = Vector3(0, 0, 1)
    uv_array[2] = Vector2(1, 1)
    vertex_array[2] = Vector3(1, 1)

    normal_array[3] = Vector3(0, 0, 1)
    uv_array[3] = Vector2(1, 0)
    vertex_array[3] = Vector3(1, -1)

    # Indices are optional in Godot, but if they exist they are used.
    index_array[0] = 0
    index_array[1] = 1
    index_array[2] = 2

    index_array[3] = 2
    index_array[4] = 3
    index_array[5] = 0

    arrays[Mesh.ARRAY_VERTEX] = vertex_array
    arrays[Mesh.ARRAY_NORMAL] = normal_array
    arrays[Mesh.ARRAY_TEX_UV] = uv_array
    arrays[Mesh.ARRAY_INDEX] = index_array

    var mesh = ArrayMesh.new()

    mesh.add_surface_from_arrays(Mesh.PRIMITIVE_TRIANGLES,arrays)
