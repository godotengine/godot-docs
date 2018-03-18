.. _doc_using_multi_mesh_instance:

Using multiMeshInstance
------------------------

Introduction
~~~~~~~~~~~~~~~~

In normal scenario, you would use a :ref:`meshInstance <class_MeshInstance>` node to display a 3D mesh. For example, a human model as the main character. In some cases, you would like to create multiple instances, you could duplicate the same node for multiple times and adjust the transforms manually. This may be a tedious process and the result may look mechanical. Also, this method is not favourable to rapid iterations. :ref:`MultiMeshInstance <class_MultiMeshInstance>` is one of the possible solutions to the problem.

MultiMeshInstance as the name suggests, create multiple copies of the meshInstance over a surface of a specific mesh. An example would be having a tree mesh populate a landscape in random scale and orientation. 

Setting up the nodes
~~~~~~~~~~~~~~~~~~~~~~

The basic set up requires three nodes. Firstly, the multiMeshInstance node. Then, two meshInstance nodes. 

One node is used as the target, the mesh that you want to place multiple meshes on. In the tree case, this is the landscape.

Another node is used as the source, the mesh that you want to have multiple duplications. In the tree case, this is the tree.

In our example, we would use a :ref:`Node <class_Node>` node as the root node of the scene. Your scene tree would look like this:

.. image:: img/multimesh_scene_tree.png

.. note:: For simplification purpose, this tutorial would use built-in primitives. 

Now you have everything ready for mesh duplications. Select the multiMeshInstance node and look at the toolbar, you should see an extra button called ``MultiMesh`` next to ``View``. Click it and select populate surface in the dropdown menu. A new window titled Populate MultiMesh will popup.

.. image:: img/multimesh_toolbar.png

.. image:: img/multimesh_settings.png

MultiMesh Settings
~~~~~~~~~~~~~~~~~~~~~~~

Below are the descriptions about the options.

Target Surface
+++++++++++++++
The mesh you would be using as the surface for placing copies of you source mesh.

Source Mesh
+++++++++++++++
The mesh you would be duplicating on the target surface.

Mesh Up Axis
+++++++++++++++
The axis used as the up axis of the source mesh.

Random Rotation
+++++++++++++++++
Randomizing the rotation around the mesh up axis of the source mesh.

Random Tilt
+++++++++++++++++++
Randomizing the overall rotation of the source mesh.

Random Scale
++++++++++++++++++
Randomizing the scale of the source mesh.

Scale
++++++++++++++++++
The scale of the source mesh that will be placed over the target surface.

Amount
+++++++++++++++++++
The amount of mesh instances placed over the target surface. 

Select the target surface, in the tree case, this should be the landscape node. And the source mesh should be the tree node. Adjust the other parameters according to your preference. Press ``populate`` and multiple copies of the source mesh will be placing over the target mesh. If you are satisfied with the result, you can delete the mesh instance used as the source mesh. 

The end result should look like this:

.. image:: img/multimesh_result.png

To change the result, repeat the same step with different parameters.
