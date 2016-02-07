.. _class_DampedSpringJoint2D:

DampedSpringJoint2D
===================

**Inherits:** :ref:`Joint2D<class_joint2d>` **<** :ref:`Node2D<class_node2d>` **<** :ref:`CanvasItem<class_canvasitem>` **<** :ref:`Node<class_node>` **<** :ref:`Object<class_object>`

**Category:** Core

Brief Description
-----------------

Damped spring constraint for 2D physics.

Member Functions
----------------

+----------------------------+-----------------------------------------------------------------------------------------------------------------------+
| void                       | :ref:`set_length<class_DampedSpringJoint2D_set_length>`  **(** :ref:`float<class_float>` length  **)**                |
+----------------------------+-----------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`  | :ref:`get_length<class_DampedSpringJoint2D_get_length>`  **(** **)** const                                            |
+----------------------------+-----------------------------------------------------------------------------------------------------------------------+
| void                       | :ref:`set_rest_length<class_DampedSpringJoint2D_set_rest_length>`  **(** :ref:`float<class_float>` rest_length  **)** |
+----------------------------+-----------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`  | :ref:`get_rest_length<class_DampedSpringJoint2D_get_rest_length>`  **(** **)** const                                  |
+----------------------------+-----------------------------------------------------------------------------------------------------------------------+
| void                       | :ref:`set_stiffness<class_DampedSpringJoint2D_set_stiffness>`  **(** :ref:`float<class_float>` stiffness  **)**       |
+----------------------------+-----------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`  | :ref:`get_stiffness<class_DampedSpringJoint2D_get_stiffness>`  **(** **)** const                                      |
+----------------------------+-----------------------------------------------------------------------------------------------------------------------+
| void                       | :ref:`set_damping<class_DampedSpringJoint2D_set_damping>`  **(** :ref:`float<class_float>` damping  **)**             |
+----------------------------+-----------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`  | :ref:`get_damping<class_DampedSpringJoint2D_get_damping>`  **(** **)** const                                          |
+----------------------------+-----------------------------------------------------------------------------------------------------------------------+

Description
-----------

Damped spring constraint for 2D physics. This resembles a spring joint that always want to go back to a given length.

Member Function Description
---------------------------

.. _class_DampedSpringJoint2D_set_length:

- void  **set_length**  **(** :ref:`float<class_float>` length  **)**

Set the maximum length of the spring joint.

.. _class_DampedSpringJoint2D_get_length:

- :ref:`float<class_float>`  **get_length**  **(** **)** const

Return the maximum length of the spring joint.

.. _class_DampedSpringJoint2D_set_rest_length:

- void  **set_rest_length**  **(** :ref:`float<class_float>` rest_length  **)**

Set the resting length of the spring joint. The joint will always try to go to back this length when pulled apart.

.. _class_DampedSpringJoint2D_get_rest_length:

- :ref:`float<class_float>`  **get_rest_length**  **(** **)** const

Return the resting length of the spring joint. The joint will always try to go to back this length when pulled apart.

.. _class_DampedSpringJoint2D_set_stiffness:

- void  **set_stiffness**  **(** :ref:`float<class_float>` stiffness  **)**

Set the stiffness of the spring joint.

.. _class_DampedSpringJoint2D_get_stiffness:

- :ref:`float<class_float>`  **get_stiffness**  **(** **)** const

Return the stiffness of the spring joint.

.. _class_DampedSpringJoint2D_set_damping:

- void  **set_damping**  **(** :ref:`float<class_float>` damping  **)**

Set the damping of the spring joint.

.. _class_DampedSpringJoint2D_get_damping:

- :ref:`float<class_float>`  **get_damping**  **(** **)** const

Return the damping of the spring joint.


