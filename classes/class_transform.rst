.. _class_Transform:

Transform
=========

**Category:** Built-In Types

Brief Description
-----------------

3D Transformation.

Member Functions
----------------

+------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Transform<class_transform>`  | :ref:`affine_inverse<class_Transform_affine_inverse>`  **(** **)**                                                                                                                                               |
+------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Transform<class_transform>`  | :ref:`inverse<class_Transform_inverse>`  **(** **)**                                                                                                                                                             |
+------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Transform<class_transform>`  | :ref:`looking_at<class_Transform_looking_at>`  **(** :ref:`Vector3<class_vector3>` target, :ref:`Vector3<class_vector3>` up  **)**                                                                               |
+------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Transform<class_transform>`  | :ref:`orthonormalized<class_Transform_orthonormalized>`  **(** **)**                                                                                                                                             |
+------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Transform<class_transform>`  | :ref:`rotated<class_Transform_rotated>`  **(** :ref:`Vector3<class_vector3>` axis, :ref:`float<class_float>` phi  **)**                                                                                          |
+------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Transform<class_transform>`  | :ref:`scaled<class_Transform_scaled>`  **(** :ref:`Vector3<class_vector3>` scale  **)**                                                                                                                          |
+------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Transform<class_transform>`  | :ref:`translated<class_Transform_translated>`  **(** :ref:`Vector3<class_vector3>` ofs  **)**                                                                                                                    |
+------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| var                                | :ref:`xform<class_Transform_xform>`  **(** var v  **)**                                                                                                                                                          |
+------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| var                                | :ref:`xform_inv<class_Transform_xform_inv>`  **(** var v  **)**                                                                                                                                                  |
+------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Transform<class_transform>`  | :ref:`Transform<class_Transform_Transform>`  **(** :ref:`Vector3<class_vector3>` x_axis, :ref:`Vector3<class_vector3>` y_axis, :ref:`Vector3<class_vector3>` z_axis, :ref:`Vector3<class_vector3>` origin  **)** |
+------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Transform<class_transform>`  | :ref:`Transform<class_Transform_Transform>`  **(** :ref:`Matrix3<class_matrix3>` basis, :ref:`Vector3<class_vector3>` origin  **)**                                                                              |
+------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Transform<class_transform>`  | :ref:`Transform<class_Transform_Transform>`  **(** :ref:`Matrix32<class_matrix32>` from  **)**                                                                                                                   |
+------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Transform<class_transform>`  | :ref:`Transform<class_Transform_Transform>`  **(** :ref:`Quat<class_quat>` from  **)**                                                                                                                           |
+------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Transform<class_transform>`  | :ref:`Transform<class_Transform_Transform>`  **(** :ref:`Matrix3<class_matrix3>` from  **)**                                                                                                                     |
+------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Member Variables
----------------

- :ref:`Matrix3<class_matrix3>` **basis**
- :ref:`Vector3<class_vector3>` **origin**

Description
-----------

Transform is used to store transformations, including translations. It consists of a Matrix3 "basis" and Vector3 "origin". Transform is used to represent transformations of any object in space. It is similar to a 4x3 matrix.

Member Function Description
---------------------------

.. _class_Transform_affine_inverse:

- :ref:`Transform<class_transform>`  **affine_inverse**  **(** **)**

.. _class_Transform_inverse:

- :ref:`Transform<class_transform>`  **inverse**  **(** **)**

Returns the inverse of the transform.

.. _class_Transform_looking_at:

- :ref:`Transform<class_transform>`  **looking_at**  **(** :ref:`Vector3<class_vector3>` target, :ref:`Vector3<class_vector3>` up  **)**

.. _class_Transform_orthonormalized:

- :ref:`Transform<class_transform>`  **orthonormalized**  **(** **)**

.. _class_Transform_rotated:

- :ref:`Transform<class_transform>`  **rotated**  **(** :ref:`Vector3<class_vector3>` axis, :ref:`float<class_float>` phi  **)**

.. _class_Transform_scaled:

- :ref:`Transform<class_transform>`  **scaled**  **(** :ref:`Vector3<class_vector3>` scale  **)**

.. _class_Transform_translated:

- :ref:`Transform<class_transform>`  **translated**  **(** :ref:`Vector3<class_vector3>` ofs  **)**

.. _class_Transform_xform:

- var  **xform**  **(** var v  **)**

Transforms vector "v" by this transform.

.. _class_Transform_xform_inv:

- var  **xform_inv**  **(** var v  **)**

Inverse-transforms vector "v" by this transform.

.. _class_Transform_Transform:

- :ref:`Transform<class_transform>`  **Transform**  **(** :ref:`Vector3<class_vector3>` x_axis, :ref:`Vector3<class_vector3>` y_axis, :ref:`Vector3<class_vector3>` z_axis, :ref:`Vector3<class_vector3>` origin  **)**

.. _class_Transform_Transform:

- :ref:`Transform<class_transform>`  **Transform**  **(** :ref:`Matrix3<class_matrix3>` basis, :ref:`Vector3<class_vector3>` origin  **)**

.. _class_Transform_Transform:

- :ref:`Transform<class_transform>`  **Transform**  **(** :ref:`Matrix32<class_matrix32>` from  **)**

.. _class_Transform_Transform:

- :ref:`Transform<class_transform>`  **Transform**  **(** :ref:`Quat<class_quat>` from  **)**

.. _class_Transform_Transform:

- :ref:`Transform<class_transform>`  **Transform**  **(** :ref:`Matrix3<class_matrix3>` from  **)**


