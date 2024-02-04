.. _doc_advanced_postprocessing:

Advanced post-processing
========================

Introduction
------------

This tutorial describes an advanced method for post-processing in Godot.
In particular, it will explain how to write a post-processing shader that
uses the depth buffer. You should already be familiar with post-processing
generally and, in particular, with the methods outlined in the :ref:`custom post-processing tutorial <doc_custom_postprocessing>`.

Full screen quad
----------------

One way to make custom post-processing effects is by using a viewport. However,
there are two main drawbacks of using a Viewport:

1. The depth buffer cannot be accessed
2. The effect of the post-processing shader is not visible in the editor

To get around the limitation on using the depth buffer, use a :ref:`MeshInstance3D <class_MeshInstance3D>`
with a :ref:`QuadMesh <class_QuadMesh>` primitive. This allows us to use a
shader and to access the depth texture of the scene. Next, use a vertex shader
to make the quad cover the screen at all times so that the post-processing
effect will be applied at all times, including in the editor.

First, create a new MeshInstance3D and set its mesh to a QuadMesh. This creates
a quad centered at position ``(0, 0, 0)`` with a width and height of ``1``. Set
the width and height to ``2`` and enable **Flip Faces**. Right now, the quad
occupies a position in world space at the origin. However, we want it to move
with the camera so that it always covers the entire screen. To do this, we will
bypass the coordinate transforms that translate the vertex positions through the
difference coordinate spaces and treat the vertices as if they were already in
clip space.

The vertex shader expects coordinates to be output in clip space, which are coordinates
ranging from ``-1`` at the left and bottom of the screen to ``1`` at the top and right
of the screen. This is why the QuadMesh needs to have height and width of ``2``.
Godot handles the transform from model to view space to clip space behind the scenes,
so we need to nullify the effects of Godot's transformations. We do this by setting the
``POSITION`` built-in to our desired position. ``POSITION`` bypasses the built-in transformations
and sets the vertex position directly.

.. code-block:: glsl

  shader_type spatial;

  void vertex() {
    POSITION = vec4(VERTEX, 1.0);
  }

Even with this vertex shader, the quad keeps disappearing. This is due to frustum
culling, which is done on the CPU. Frustum culling uses the camera matrix and the
AABBs of Meshes to determine if the Mesh will be visible *before* passing it to the GPU.
The CPU has no knowledge of what we are doing with the vertices, so it assumes the
coordinates specified refer to world positions, not clip space positions, which results
in Godot culling the quad when we turn away from the center of the scene. In
order to keep the quad from being culled, there are a few options:

1. Add the QuadMesh as a child to the camera, so the camera is always pointed at it
2. Set the Geometry property ``extra_cull_margin`` as large as possible in the QuadMesh

The second option ensures that the quad is visible in the editor, while the first
option guarantees that it will still be visible even if the camera moves outside the cull margin.
You can also use both options.

Depth texture
-------------

To read from the depth texture, we first need to create a texture uniform set to the depth buffer
by using ``hint_depth_texture``.

.. code-block:: glsl

  uniform sampler2D depth_texture : source_color, hint_depth_texture;

Once defined, the depth texture can be read with the ``texture()`` function.

.. code-block:: glsl

  float depth = texture(depth_texture, SCREEN_UV).x;

.. note:: Similar to accessing the screen texture, accessing the depth texture is only
          possible when reading from the current viewport. The depth texture cannot be
          accessed from another viewport to which you have rendered.

The values returned by ``depth_texture`` are between ``0.0`` and ``1.0`` and are nonlinear.
When displaying depth directly from the ``depth_texture``, everything will look almost
white unless it is very close. This is because the depth buffer stores objects closer
to the camera using more bits than those further, so most of the detail in depth
buffer is found close to the camera. In order to make the depth value align with world or
model coordinates, we need to linearize the value. When we apply the projection matrix to the
vertex position, the z value is made nonlinear, so to linearize it, we multiply it by the
inverse of the projection matrix, which in Godot, is accessible with the variable
``INV_PROJECTION_MATRIX``.

Firstly, take the screen space coordinates and transform them into normalized device
coordinates (NDC). NDC run ``-1.0`` to ``1.0`` in ``x`` and ``y`` directions and
from ``0.0`` to ``1.0`` in the ``z`` direction when using the Vulkan backend.
Reconstruct the NDC using ``SCREEN_UV`` for the ``x`` and ``y`` axis, and
the depth value for ``z``.

.. note::

    This tutorial assumes the use of the Vulkan renderer, which uses NDCs with a Z-range
    of ``[0.0, 1.0]``. In contrast, OpenGL uses NDCs with a Z-range of ``[-1.0, 1.0]``.

.. code-block:: glsl

  void fragment() {
    float depth = texture(depth_texture, SCREEN_UV).x;
    vec3 ndc = vec3(SCREEN_UV * 2.0 - 1.0, depth);
  }

Convert NDC to view space by multiplying the NDC by ``INV_PROJECTION_MATRIX``.
Recall that view space gives positions relative to the camera, so the ``z`` value will give us
the distance to the point.

.. code-block:: glsl

  void fragment() {
    ...
    vec4 view = INV_PROJECTION_MATRIX * vec4(ndc, 1.0);
    view.xyz /= view.w;
    float linear_depth = -view.z;
  }

Because the camera is facing the negative ``z`` direction, the position will have a negative ``z`` value.
In order to get a usable depth value, we have to negate ``view.z``.

The world position can be constructed from the depth buffer using the following code. Note
that the ``INV_VIEW_MATRIX`` is needed to transform the position from view space into world space, so
it needs to be passed to the fragment shader with a varying.

.. code-block:: glsl

  varying mat4 CAMERA;

  void vertex() {
    CAMERA = INV_VIEW_MATRIX;
  }

  void fragment() {
    ...
    vec4 world = CAMERA * INV_PROJECTION_MATRIX * vec4(ndc, 1.0);
    vec3 world_position = world.xyz / world.w;
  }

An optimization
---------------

You can benefit from using a single large triangle rather than using a full
screen quad. The reason for this is explained `here <https://michaldrobot.com/2014/04/01/gcn-execution-patterns-in-full-screen-passes>`_.
However, the benefit is quite small and only beneficial when running especially
complex fragment shaders.

Set the Mesh in the MeshInstance3D to an :ref:`ArrayMesh <class_ArrayMesh>`. An
ArrayMesh is a tool that allows you to easily construct a Mesh from Arrays for
vertices, normals, colors, etc.

Now, attach a script to the MeshInstance3D and use the following code:

::

  extends MeshInstance3D

  func _ready():
    # Create a single triangle out of vertices:
    var verts = PackedVector3Array()
    verts.append(Vector3(-1.0, -1.0, 0.0))
    verts.append(Vector3(-1.0, 3.0, 0.0))
    verts.append(Vector3(3.0, -1.0, 0.0))

    # Create an array of arrays.
    # This could contain normals, colors, UVs, etc.
    var mesh_array = []
    mesh_array.resize(Mesh.ARRAY_MAX) #required size for ArrayMesh Array
    mesh_array[Mesh.ARRAY_VERTEX] = verts #position of vertex array in ArrayMesh Array

    # Create mesh from mesh_array:
    mesh.add_surface_from_arrays(Mesh.PRIMITIVE_TRIANGLES, mesh_array)

.. note:: The triangle is specified in normalized device coordinates.
          Recall, NDC run from ``-1.0`` to ``1.0`` in both the ``x`` and ``y``
          directions. This makes the screen ``2`` units wide and ``2`` units
          tall. In order to cover the entire screen with a single triangle, use
          a triangle that is ``4`` units wide and ``4`` units tall, double its
          height and width.

Assign the same vertex shader from above and everything should look exactly the same.

The one drawback to using an ArrayMesh over using a QuadMesh is that the ArrayMesh
is not visible in the editor because the triangle is not constructed until the scene
is run. To get around that, construct a single triangle Mesh in a modeling program
and use that in the MeshInstance3D instead.
