.. _class_Path:

Path
====

Inherits: :ref:`Spatial<class_spatial>`
---------------------------------------

Category: Core
--------------

Brief Description
-----------------

Container for a :ref:`Curve3D<class_curve3d>`.

Member Functions
----------------

+--------------------------------+------------------------------------------------------------------------------------------+
| void                           | :ref:`set_curve<class_Path_set_curve>`  **(** :ref:`Curve3D<class_curve3d>` curve  **)** |
+--------------------------------+------------------------------------------------------------------------------------------+
| :ref:`Curve3D<class_curve3d>`  | :ref:`get_curve<class_Path_get_curve>`  **(** **)** const                                |
+--------------------------------+------------------------------------------------------------------------------------------+

Description
-----------

This class is a container/Node-ification of a :ref:`Curve3D<class_curve3d>`, so it can have :ref:`Spatial<class_spatial>` properties and :ref:`Node<class_node>` info.

Member Function Description
---------------------------

.. _class_Path_set_curve:

- void  **set_curve**  **(** :ref:`Curve3D<class_curve3d>` curve  **)**

Sets the :ref:`Curve3D<class_curve3d>`.

.. _class_Path_get_curve:

- :ref:`Curve3D<class_curve3d>`  **get_curve**  **(** **)** const

Returns the :ref:`Curve3D<class_curve3d>` contained.


