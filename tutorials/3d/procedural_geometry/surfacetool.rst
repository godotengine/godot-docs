.. _doc_surfacetool:

Using the SurfaceTool
=====================

The :ref:`SurfaceTool <class_surfacetool>` provides a useful interface for constructing geometry.
The interface is similar to the :ref:`ImmediateMesh <class_ImmediateMesh>` class. You
set each per-vertex attribute (e.g. normal, uv, color) and then when you add a vertex it
captures the attributes.

The SurfaceTool also provides some useful helper functions like ``index()`` and ``generate_normals()``.

Attributes are added before each vertex is added:

.. tabs::
 .. code-tab:: gdscript GDScript

    var st = SurfaceTool.new()

    st.begin(Mesh.PRIMITIVE_TRIANGLES)

    st.set_normal() # Overwritten by normal below.
    st.set_normal() # Added to next vertex.
    st.set_color() # Added to next vertex.
    st.add_vertex() # Captures normal and color above.
    st.set_normal() # Normal never added to a vertex.

 .. code-tab:: csharp
    
    st.SetNormal(); // Overwritten by normal below.
    st.SetNormal(); // Added to next vertex.
    st.SetColor(); // Added to next vertex.
    st.AddVertex(); // Captures normal and color above.
    st.SetNormal(); // Normal never added to a vertex.

When finished generating your geometry with the :ref:`SurfaceTool <class_surfacetool>`,
call ``commit()`` to finish generating the mesh. If an :ref:`ArrayMesh <class_ArrayMesh>` is passed
to ``commit()``, then it appends a new surface to the end of the ArrayMesh. While if nothing is passed
in, ``commit()`` returns an ArrayMesh.

.. tabs::
 .. code-tab:: gdscript GDScript

    # Add surface to existing ArrayMesh.
    st.commit(mesh)

    # -- Or Alternatively --

    # Create new ArrayMesh.
    var mesh = st.commit()

 .. code-tab:: csharp

    st.Commit(mesh);
    // Or:
    var mesh = st.Commit();

The code below creates a triangle without indices.

.. tabs::
 .. code-tab:: gdscript GDScript

    var st = SurfaceTool.new()

    st.begin(Mesh.PRIMITIVE_TRIANGLES)

    # Prepare attributes for add_vertex.
    st.set_normal(Vector3(0, 0, 1))
    st.set_uv(Vector2(0, 0))
    # Call last for each vertex, adds the above attributes.
    st.add_vertex(Vector3(-1, -1, 0))

    st.set_normal(Vector3(0, 0, 1))
    st.set_uv(Vector2(0, 1))
    st.add_vertex(Vector3(-1, 1, 0))

    st.set_normal(Vector3(0, 0, 1))
    st.set_uv(Vector2(1, 1))
    st.add_vertex(Vector3(1, 1, 0))

    # Commit to a mesh.
    var mesh = st.commit()

 .. code-tab:: csharp

    var st = new SurfaceTool();

    st.Begin(Mesh.PrimitiveType.Triangles);

    // Prepare attributes for AddVertex.
    st.SetNormal(new Vector3(0, 0, 1));
    st.SetUV(new Vector2(0, 0));
    // Call last for each vertex, adds the above attributes.
    st.AddVertex(new Vector3(-1, -1, 0));

    st.SetNormal(new Vector3(0, 0, 1));
    st.SetUV(new Vector2(0, 1));
    st.AddVertex(new Vector3(-1, 1, 0));

    st.SetNormal(new Vector3(0, 0, 1));
    st.SetUV(new Vector2(1, 1));
    st.AddVertex(new Vector3(1, 1, 0));

    // Commit to a mesh.
    var mesh = st.Commit();

You can optionally add an index array, either by calling ``add_index()`` and adding
vertices to the index array manually, or by calling ``index()`` once,
which generates the index array automatically and
shrinks the vertex array to remove duplicate vertices.

.. tabs::
 .. code-tab:: gdscript GDScript

    # Suppose we have a quad defined by 6 vertices as follows
    st.add_vertex(Vector3(-1, 1, 0))
    st.add_vertex(Vector3(1, 1, 0))
    st.add_vertex(Vector3(-1, -1, 0))

    st.add_vertex(Vector3(1, 1, 0))
    st.add_vertex(Vector3(1, -1, 0))
    st.add_vertex(Vector3(-1, -1, 0))

    # We can make the quad more efficient by using an index array and only utilizing 4 vertices

    # Suppose we have a quad defined by 6 vertices as follows
    st.add_vertex(Vector3(-1, 1, 0))
    st.add_vertex(Vector3(1, 1, 0))
    st.add_vertex(Vector3(-1, -1, 0))

    st.add_vertex(Vector3(1, 1, 0))
    st.add_vertex(Vector3(1, -1, 0))
    st.add_vertex(Vector3(-1, -1, 0))

    # We can make the quad more efficient by using an index array and only utilizing 4 vertices

    # Creates a quad from four corner vertices.
    # add_index() can be called before or after add_vertex()
    # since it's not an attribute of a vertex itself.
    st.add_index(0)
    st.add_index(1)
    st.add_index(2)

    st.add_index(1)
    st.add_index(3)
    st.add_index(2)

    # Alternatively we can use ``st.index()`` which will create the quad for us and remove the duplicate vertices
    st.index()

 .. code-tab:: csharp

    // Creates a quad from four corner vertices.
    // AddIndex does not need to be called before AddVertex.
    st.AddIndex(0);
    st.AddIndex(1);
    st.AddIndex(2);

    st.AddIndex(1);
    st.AddIndex(3);
    st.AddIndex(2);

    // Alternatively:
    st.Index();

Similarly, if you have an index array, but you want each vertex to be unique (e.g. because
you want to use unique normals or colors per face instead of per-vertex), you can call ``deindex()``.

.. tabs::
 .. code-tab:: gdscript GDScript

    st.deindex()

 .. code-tab:: csharp

    st.Deindex();

If you don't add custom normals yourself, you can add them using ``generate_normals()``, which should
be called after generating geometry and before committing the mesh using ``commit()`` or
``commit_to_arrays()``. Calling ``generate_normals(true)`` will flip the resulting normals. As a side
note, ``generate_normals()`` only works if the primitive type is set to ``Mesh.PRIMITIVE_TRIANGLES``.

You may notice that normal mapping or other material properties look broken on
the generated mesh. This is because normal mapping **requires** the mesh to
feature *tangents*, which are separate from *normals*. You can either add custom
tangents manually, or generate them automatically with
``generate_tangents()``. This method requires that each vertex have UVs and
normals set already.

.. tabs::
 .. code-tab:: gdscript GDScript

    st.generate_normals()
    st.generate_tangents()

    st.commit(mesh)

 .. code-tab:: csharp
    
    st.GenerateNormals();
    st.GenerateTangents();

By default, when generating normals, they will be calculated on a per-vertex basis (i.e. they will
be "smooth normals"). If you want flat vertex normals (i.e. a single normal vector per face), when
adding vertices, call ``add_smooth_group(i)`` where ``i`` is a unique number per vertex.
``add_smooth_group()`` needs to be called while building the geometry, e.g. before the call to
``add_vertex()``.
