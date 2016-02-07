.. _class_RectangleShape2D:

RectangleShape2D
================

**Inherits:** :ref:`Shape2D<class_shape2d>`

**Category:** Core

Rectangle Shape for 2D Physics.

Member Functions
----------------

+--------------------------------+------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_extents<class_RectangleShape2D_set_extents>`  **(** :ref:`Vector2<class_vector2>` extents  **)** |
+--------------------------------+------------------------------------------------------------------------------------------------------------+
| :ref:`Vector2<class_vector2>`  | :ref:`get_extents<class_RectangleShape2D_get_extents>`  **(** **)** const                                  |
+--------------------------------+------------------------------------------------------------------------------------------------------------+

Description
-----------

Rectangle Shape for 2D Physics. This shape is useful for modelling box-like 2D objects.

Member Function Description
---------------------------

.. _class_RectangleShape2D_set_extents:

- void  **set_extents**  **(** :ref:`Vector2<class_vector2>` extents  **)**

Set the half extents, the actual width and height of this shape is twice the half extents.

.. _class_RectangleShape2D_get_extents:

- :ref:`Vector2<class_vector2>`  **get_extents**  **(** **)** const

Return the half extents, the actual width and height of this shape is twice the half extents.


