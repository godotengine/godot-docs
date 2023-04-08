:article_outdated: True

.. _doc_using_multimesh:

Optimization using MultiMeshes
==============================

For large amount of instances (in the thousands), that need to be constantly processed
(and certain amount of control needs to be retained),
:ref:`using servers directly <doc_using_servers>` is the recommended optimization.

When the amount of objects reach the hundreds of thousands or millions,
none of these approaches are efficient anymore. Still, depending on the requirements, there
is one more optimization possible.

MultiMeshes
-----------

A :ref:`MultiMesh<class_MultiMesh>` is a single draw primitive that can draw up to millions
of objects in one go. It's extremely efficient because it uses the GPU hardware to do this
(in OpenGL ES 2.0, it's less efficient because there is no hardware support for it, though).

The only drawback is that there is no *screen* or *frustum* culling possible for individual instances.
This means, that millions of objects will be *always* or *never* drawn, depending on the visibility
of the whole MultiMesh. It is possible to provide a custom visibility rect for them, but it will always
be *all-or-none* visibility.

If the objects are simple enough (just a couple of vertices), this is generally not much of a problem
as most modern GPUs are optimized for this use case. A workaround is to create several MultiMeshes
for different areas of the world.

It is also possible to execute some logic inside the vertex shader (using the ``INSTANCE_ID`` or
``INSTANCE_CUSTOM`` built-in constants). For an example of animating thousands of objects in a MultiMesh,
see the :ref:`Animating thousands of fish <doc_animating_thousands_of_fish>` tutorial. Information
to the shader can be provided via textures (there are floating-point :ref:`Image<class_Image>` formats
which are ideal for this).

Another alternative is to use a GDExtension and C++, which should be extremely efficient (it's possible
to set the entire state for all objects using linear memory via the
:ref:`RenderingServer.multimesh_set_buffer() <class_RenderingServer_method_multimesh_set_buffer>`
function). This way, the array can be created with multiple threads, then set in one call, providing
high cache efficiency.

Finally, it's not required to have all MultiMesh instances visible. The amount of visible ones can be
controlled with the :ref:`MultiMesh.visible_instance_count <class_MultiMesh_property_visible_instance_count>`
property. The typical workflow is to allocate the maximum amount of instances that will be used,
then change the amount visible depending on how many are currently needed.

Multimesh example
-----------------

Here is an example of using a MultiMesh from code. Languages other than GDScript may be more
efficient for millions of objects, but for a few thousands, GDScript should be fine.

.. tabs::
 .. code-tab:: gdscript GDScript

    extends MultiMeshInstance3D


    func _ready():
        # Create the multimesh.
        multimesh = MultiMesh.new()
        # Set the format first.
        multimesh.transform_format = MultiMesh.TRANSFORM_3D
        # Then resize (otherwise, changing the format is not allowed).
        multimesh.instance_count = 10000
        # Maybe not all of them should be visible at first.
        multimesh.visible_instance_count = 1000

        # Set the transform of the instances.
        for i in multimesh.visible_instance_count:
            multimesh.set_instance_transform(i, Transform3D(Basis(), Vector3(i * 20, 0, 0)))

 .. code-tab:: csharp C#

    using Godot;

    public partial class MyMultiMeshInstance3D : MultiMeshInstance3D
    {
        public override void _Ready()
        {
            // Create the multimesh.
            Multimesh = new MultiMesh();
            // Set the format first.
            Multimesh.TransformFormat = MultiMesh.TransformFormatEnum.Transform3D;
            // Then resize (otherwise, changing the format is not allowed)
            Multimesh.InstanceCount = 1000;
            // Maybe not all of them should be visible at first.
            Multimesh.VisibleInstanceCount = 1000;

            // Set the transform of the instances.
            for (int i = 0; i < Multimesh.VisibleInstanceCount; i++)
            {
                Multimesh.SetInstanceTransform(i, new Transform3D(Basis.Identity, new Vector3(i * 20, 0, 0)));
            }
        }
    }
