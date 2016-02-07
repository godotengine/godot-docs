.. _class_MultiMeshInstance:

MultiMeshInstance
=================

Inherits: :ref:`GeometryInstance<class_geometryinstance>`
---------------------------------------------------------

Category: Core
--------------

Brief Description
-----------------

Node that instances a :ref:`MultiMesh<class_multimesh>`.

Member Functions
----------------

+------------------------------+-----------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`set_multimesh<class_MultiMeshInstance_set_multimesh>`  **(** :ref:`Object<class_object>` multimesh  **)** |
+------------------------------+-----------------------------------------------------------------------------------------------------------------+
| :ref:`Object<class_object>`  | :ref:`get_multimesh<class_MultiMeshInstance_get_multimesh>`  **(** **)** const                                  |
+------------------------------+-----------------------------------------------------------------------------------------------------------------+

Description
-----------

MultiMeshInstance is a :ref:`Node<class_node>` that takes a :ref:`MultiMesh<class_multimesh>` resource and adds it to the current :ref:`Scenario<class_scenario>` by creating an instance of it (yes, this is an instance of instances).

Member Function Description
---------------------------

.. _class_MultiMeshInstance_set_multimesh:

- void  **set_multimesh**  **(** :ref:`Object<class_object>` multimesh  **)**

Set the :ref:`MultiMesh<class_multimesh>` to be instance.

.. _class_MultiMeshInstance_get_multimesh:

- :ref:`Object<class_object>`  **get_multimesh**  **(** **)** const

Return the :ref:`MultiMesh<class_multimesh>` that is used for instancing.


