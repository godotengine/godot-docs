.. _doc_using_multimesh:

Optimization Using Multimeshes
============

For large amount of instances (in the thousands), that need to be constantly processed (and certain amount of control needs to be retained), :ref:`using servers directly<doc_using_servers>` is the recommended optimization.

When the amount of objects reach the dozens of thousands, hundreds of thousands or even millions, none of these approaches are efficient anymore. Still, depending on the requirements, there is one more optimization possible.


Multimeshes
-----------

A :ref:`MultiMesh<class_MultiMesh>` is a single draw primitive that can draw up to millions of objects in one go. It's extremely efficient because it uses the GPU hardware to do this (In OpenGL ES 2.0, it's less efficient because there is no hardware support for it, though).

The only drawback is that there is no *screen* or *frustum* culling possible for individual instances. This means, that millions of objects will be *always* or *never* drawn, depending on the visibility of the whole MultiMesh. It is possible to provide a custom visibility rect for them, but it will always be *all-or-none* visibility.

If the objects are simple enough (just a couple of vertices), this is generally not much of a problem as most modern GPUs are optimized for this use case. A workaround is to create several multimeshes for different areas of the world.

If logic is too simple, it is also possible to execute it inside the vertex shader (using the INSTANCE_ID integer built-in constant). Information to it can be provided via textures (there are floating point :ref:`Image<class_Image>` formats which are ideal for this).

Another alternative is to use GDNative and C++, which should be extremely efficient (it's possible to set the entire state for all objects using linear memory via the :ref:`VisualServer.multimesh_set_as_bulk_array()<class_VisualServer_method_multimesh_set_as_bulk_array>` function. This way, the array can be created with multiple threads, then set in one call, providing high cache efficiency.

Finally, it's not required to have all multimesh instances visible. The amount of visible ones can be controlled with the *MultiMesh.visible_instance_count* property. The typical workflow is to allocate the maximum amount of instances that will be used,
then change the amount visible depending on how many are currently needed.

Multimesh Example
-----------

Here is a simple example of using a multimesh from code (using GDScript). Other languages may be more efficient for millions of objects, but for a few thousands, GDScript should be fine.

.. tabs::
 .. code-tab:: gdscript GDScript

    extends MultiMeshInstance
    
    
    func _ready():

        # Create multimesh
        multimesh = MultiMesh.new()
        # Set format first
        multimesh.transform_format = MultiMesh.TRANSFORM_3D
        multimesh.color_format = MultiMesh.COLOR_NONE
        multimesh.custom_data_format = MultiMesh.CUSTOM_DATA_NONE
        # Then resize (else changing format is not allowed)
        multimesh.instance_count = 10000
        # Maybe not all of them should be visible at first
        multimesh.visible_instance_count = 1000
        # Set instance transforms
        for i in range(multimesh.visible_instance_count):
            multimesh.set_instance_transform(i,Transform( Basis(), Vector3(i*20,0,0) ) )


