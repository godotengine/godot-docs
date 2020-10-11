.. _doc_immediategeometry:

Using ImmediateGeometry
=======================

Unlike the SurfaceTool or ArrayMesh, :ref:`ImmediateGeometry <class_ImmediateGeometry>` is an actual
node. Being a node makes it quick to add to a scene and get visual output. It uses an OpenGL 1.x-style
API like SurfaceTool, but it's actually designed to create meshes on the fly.

Generating complex geometry (several thousand vertices) with this node is inefficient, even if it's
done only once. Instead, it is designed to generate simple geometry that changes every frame.

Before starting, you should clear the geometry by calling ``clear()``. This ensures that
you are not building upon the geometry from the previous frame. If you want to keep geometry between frames, do
not call ``clear()``.

To begin generating geometry you must call ``begin()``. ``begin()`` takes a ``PrimitiveType`` as an argument.
``PrimitiveType`` is an OpenGL concept that instructs the GPU how to arrange the primitive based on the
vertices given whether it is triangles, lines, points, etc. A complete list can be found under
the :ref:`Mesh <class_mesh>` class reference page.

Once you have called ``begin()`` you are ready to start adding vertices. You add vertices one at a time.
First you add vertex specific attributes such as normals or UVs using ``set_****()`` (e.g. ``set_normal()``).
Then you call ``add_vertex()`` to add a vertex with those attributes. For example:

.. tabs::
  .. code-tab:: gdscript GDScript

    # Add a vertex with normal and uv.
    set_normal(Vector3(0, 1, 0))
    set_uv(Vector2(1, 1))
    add_vertex(Vector3(0, 0, 1))

Only attributes added before the call to ``add_vertex()`` will be included in that vertex.

Finally, once you have added all your vertices call ``end()`` to signal that you have finished generating the mesh.

The example code below draws a single triangle.

.. tabs::
  .. code-tab:: gdscript GDScript

    extends ImmediateGeometry

    func _process(_delta):
        # Clean up before drawing.
        clear()

        # Begin draw.
        begin(Mesh.PRIMITIVE_TRIANGLES)

        # Prepare attributes for add_vertex.
        set_normal(Vector3(0, 0, 1))
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
