.. _class_Shape2D:

Shape2D
=======

**Inherits:** :ref:`Resource<class_resource>`

**Category:** Core

Base class for all 2D Shapes.

Member Functions
----------------

+----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                       | :ref:`set_custom_solver_bias<class_Shape2D_set_custom_solver_bias>`  **(** :ref:`float<class_float>` bias  **)**                                                                                                                                                                                                                         |
+----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`  | :ref:`get_custom_solver_bias<class_Shape2D_get_custom_solver_bias>`  **(** **)** const                                                                                                                                                                                                                                                   |
+----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`    | :ref:`collide<class_Shape2D_collide>`  **(** :ref:`Matrix32<class_matrix32>` local_xform, :ref:`Shape2D<class_shape2d>` with_shape, :ref:`Matrix32<class_matrix32>` shape_xform  **)**                                                                                                                                                   |
+----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`    | :ref:`collide_with_motion<class_Shape2D_collide_with_motion>`  **(** :ref:`Matrix32<class_matrix32>` local_xform, :ref:`Vector2<class_vector2>` local_motion, :ref:`Shape2D<class_shape2d>` with_shape, :ref:`Matrix32<class_matrix32>` shape_xform, :ref:`Vector2<class_vector2>` shape_motion  **)**                                   |
+----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Variant                    | :ref:`collide_and_get_contacts<class_Shape2D_collide_and_get_contacts>`  **(** :ref:`Matrix32<class_matrix32>` local_xform, :ref:`Shape2D<class_shape2d>` with_shape, :ref:`Matrix32<class_matrix32>` shape_xform  **)**                                                                                                                 |
+----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Variant                    | :ref:`collide_with_motion_and_get_contacts<class_Shape2D_collide_with_motion_and_get_contacts>`  **(** :ref:`Matrix32<class_matrix32>` local_xform, :ref:`Vector2<class_vector2>` local_motion, :ref:`Shape2D<class_shape2d>` with_shape, :ref:`Matrix32<class_matrix32>` shape_xform, :ref:`Vector2<class_vector2>` shape_motion  **)** |
+----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Description
-----------

Base class for all 2D Shapes. All 2D shape types inherit from this.

Member Function Description
---------------------------

.. _class_Shape2D_set_custom_solver_bias:

- void  **set_custom_solver_bias**  **(** :ref:`float<class_float>` bias  **)**

Use a custom solver bias. No need to change this unless you really know what you are doing.

The solver bias is a factor controlling how much two objects "rebound" off each other, when colliding, to avoid them getting into each other because of numerical imprecision.

.. _class_Shape2D_get_custom_solver_bias:

- :ref:`float<class_float>`  **get_custom_solver_bias**  **(** **)** const

Return the custom solver bias.

.. _class_Shape2D_collide:

- :ref:`bool<class_bool>`  **collide**  **(** :ref:`Matrix32<class_matrix32>` local_xform, :ref:`Shape2D<class_shape2d>` with_shape, :ref:`Matrix32<class_matrix32>` shape_xform  **)**

Return whether this shape is colliding with another.

This method needs the transformation matrix for this shape (:ref:`code<class_code>`local_xform:ref:`/code<class_/code>`), the shape to check collisions with (:ref:`code<class_code>`with_shape:ref:`/code<class_/code>`), and the transformation matrix of that shape (:ref:`code<class_code>`shape_xform:ref:`/code<class_/code>`).

.. _class_Shape2D_collide_with_motion:

- :ref:`bool<class_bool>`  **collide_with_motion**  **(** :ref:`Matrix32<class_matrix32>` local_xform, :ref:`Vector2<class_vector2>` local_motion, :ref:`Shape2D<class_shape2d>` with_shape, :ref:`Matrix32<class_matrix32>` shape_xform, :ref:`Vector2<class_vector2>` shape_motion  **)**

Return whether this shape would collide with another, if a given movemen was applied.

This method needs the transformation matrix for this shape (:ref:`code<class_code>`local_xform:ref:`/code<class_/code>`), the movement to test on this shape (:ref:`code<class_code>`local_motion:ref:`/code<class_/code>`), the shape to check collisions with (:ref:`code<class_code>`with_shape:ref:`/code<class_/code>`), the transformation matrix of that shape (:ref:`code<class_code>`shape_xform:ref:`/code<class_/code>`), and the movement to test ont the other object (:ref:`code<class_code>`shape_motion:ref:`/code<class_/code>`).

.. _class_Shape2D_collide_and_get_contacts:

- Variant  **collide_and_get_contacts**  **(** :ref:`Matrix32<class_matrix32>` local_xform, :ref:`Shape2D<class_shape2d>` with_shape, :ref:`Matrix32<class_matrix32>` shape_xform  **)**

Return a list of the points where this shape touches another. If there are no collisions, the list is empty.

This method needs the transformation matrix for this shape (:ref:`code<class_code>`local_xform:ref:`/code<class_/code>`), the shape to check collisions with (:ref:`code<class_code>`with_shape:ref:`/code<class_/code>`), and the transformation matrix of that shape (:ref:`code<class_code>`shape_xform:ref:`/code<class_/code>`).

.. _class_Shape2D_collide_with_motion_and_get_contacts:

- Variant  **collide_with_motion_and_get_contacts**  **(** :ref:`Matrix32<class_matrix32>` local_xform, :ref:`Vector2<class_vector2>` local_motion, :ref:`Shape2D<class_shape2d>` with_shape, :ref:`Matrix32<class_matrix32>` shape_xform, :ref:`Vector2<class_vector2>` shape_motion  **)**

Return a list of the points where this shape would touch another, if a given movement was applied. If there are no collisions, the list is empty.

This method needs the transformation matrix for this shape (:ref:`code<class_code>`local_xform:ref:`/code<class_/code>`), the movement to test on this shape (:ref:`code<class_code>`local_motion:ref:`/code<class_/code>`), the shape to check collisions with (:ref:`code<class_code>`with_shape:ref:`/code<class_/code>`), the transformation matrix of that shape (:ref:`code<class_code>`shape_xform:ref:`/code<class_/code>`), and the movement to test ont the other object (:ref:`code<class_code>`shape_motion:ref:`/code<class_/code>`).


