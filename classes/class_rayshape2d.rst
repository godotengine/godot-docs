.. _class_RayShape2D:

RayShape2D
==========

**Inherits:** :ref:`Shape2D<class_shape2d>` **<** :ref:`Resource<class_resource>` **<** :ref:`Reference<class_reference>` **<** :ref:`Object<class_object>`

**Category:** Core

Brief Description
-----------------

Ray 2D shape resource for physics.

Member Functions
----------------

+----------------------------+-----------------------------------------------------------------------------------------------+
| void                       | :ref:`set_length<class_RayShape2D_set_length>`  **(** :ref:`float<class_float>` length  **)** |
+----------------------------+-----------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`  | :ref:`get_length<class_RayShape2D_get_length>`  **(** **)** const                             |
+----------------------------+-----------------------------------------------------------------------------------------------+

Description
-----------

Ray 2D shape resource for physics. A ray is not really a collision body, isntead it tries to separate itself from whatever is touching its far endpoint. It's often useful for characters.

Member Function Description
---------------------------

.. _class_RayShape2D_set_length:

- void  **set_length**  **(** :ref:`float<class_float>` length  **)**

Set the length of the ray.

.. _class_RayShape2D_get_length:

- :ref:`float<class_float>`  **get_length**  **(** **)** const

Return the length of the ray.


