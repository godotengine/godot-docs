.. _class_PackedScene:

PackedScene
===========

**Inherits:** :ref:`Resource<class_resource>`

**Category:** Core



Member Functions
----------------

+--------------------------------------+--------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`                | :ref:`pack<class_PackedScene_pack>`  **(** :ref:`Node<class_node>` path  **)**                               |
+--------------------------------------+--------------------------------------------------------------------------------------------------------------+
| :ref:`Node<class_node>`              | :ref:`instance<class_PackedScene_instance>`  **(** :ref:`bool<class_bool>` gen_edit_state=false  **)** const |
+--------------------------------------+--------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`              | :ref:`can_instance<class_PackedScene_can_instance>`  **(** **)** const                                       |
+--------------------------------------+--------------------------------------------------------------------------------------------------------------+
| :ref:`SceneState<class_scenestate>`  | :ref:`get_state<class_PackedScene_get_state>`  **(** **)**                                                   |
+--------------------------------------+--------------------------------------------------------------------------------------------------------------+

Description
-----------

TODO: explain ownership, and that node does not need to own itself

Member Function Description
---------------------------

.. _class_PackedScene_pack:

- :ref:`int<class_int>`  **pack**  **(** :ref:`Node<class_node>` path  **)**

Pack will ignore any sub-nodes not owned by given node. See :ref:`Node.set_owner<class_node.set_owner>`.

.. _class_PackedScene_instance:

- :ref:`Node<class_node>`  **instance**  **(** :ref:`bool<class_bool>` gen_edit_state=false  **)** const

.. _class_PackedScene_can_instance:

- :ref:`bool<class_bool>`  **can_instance**  **(** **)** const

.. _class_PackedScene_get_state:

- :ref:`SceneState<class_scenestate>`  **get_state**  **(** **)**


