Skeleton
========

.. image:: img/armature.jpg

Rest Bone
---------

Armature object in Blender is exported as a Skeleton node along with
rest position (transform in Godot) of bones. 

.. warning:: 
    The three check boxes :code:`Inheirt Rotation`, :code:`Inheirt Scale`,
    :code:`Local Location` (colored in red) must be ticked when building
    armature in Blender, so that the exported bone transform would be
    consistant between Blender and Godot

Bone Weights
------------

Blender put rigged mesh vertices which has no bone weights at its original
position, but these vertices would be placed at (0, 0, 0) in Godot, which making the mesh
deformed. Therefore, the exporter would raise an error for any no bone weights vertex
detected in a rigged mesh.

Non-Deform Bone
---------------

Note that the non-deform bone can be configured as not exported
by enable the :code:`Exclude Control Bones`, the deform bone
checkbox is shown in picture.


Bone Attachment
---------------
Bone can be parent of object in Blender, this relation is exported
as a BoneAttachment node in the Godot scene.
