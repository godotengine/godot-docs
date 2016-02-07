.. _class_LineShape2D:

LineShape2D
===========

Inherits: :ref:`Shape2D<class_shape2d>`
---------------------------------------

Category: Core
--------------

Brief Description
-----------------

Line shape for 2D collision objects.

Member Functions
----------------

+--------------------------------+----------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_normal<class_LineShape2D_set_normal>`  **(** :ref:`Vector2<class_vector2>` normal  **)** |
+--------------------------------+----------------------------------------------------------------------------------------------------+
| :ref:`Vector2<class_vector2>`  | :ref:`get_normal<class_LineShape2D_get_normal>`  **(** **)** const                                 |
+--------------------------------+----------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_d<class_LineShape2D_set_d>`  **(** :ref:`float<class_float>` d  **)**                    |
+--------------------------------+----------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`      | :ref:`get_d<class_LineShape2D_get_d>`  **(** **)** const                                           |
+--------------------------------+----------------------------------------------------------------------------------------------------+

Description
-----------

Line shape for 2D collision objects. It works like a 2D plane and will not allow any body to go to the negative side. Not recommended for rigid bodies, and usually not recommended for static bodies either because it forces checks against it on every frame.

Member Function Description
---------------------------

.. _class_LineShape2D_set_normal:

- void  **set_normal**  **(** :ref:`Vector2<class_vector2>` normal  **)**

Set the line normal.

.. _class_LineShape2D_get_normal:

- :ref:`Vector2<class_vector2>`  **get_normal**  **(** **)** const

Return the line normal.

.. _class_LineShape2D_set_d:

- void  **set_d**  **(** :ref:`float<class_float>` d  **)**

Set the line distance from the origin.

.. _class_LineShape2D_get_d:

- :ref:`float<class_float>`  **get_d**  **(** **)** const

Return the line distance from the origin.


