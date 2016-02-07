.. _class_ConcavePolygonShape:

ConcavePolygonShape
===================

**Inherits:** :ref:`Shape<class_shape>`

**Category:** Core

Concave polygon shape.

Member Functions
----------------

+------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| void                                     | :ref:`set_faces<class_ConcavePolygonShape_set_faces>`  **(** :ref:`Vector3Array<class_vector3array>` faces  **)** |
+------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector3Array<class_vector3array>`  | :ref:`get_faces<class_ConcavePolygonShape_get_faces>`  **(** **)** const                                          |
+------------------------------------------+-------------------------------------------------------------------------------------------------------------------+

Description
-----------

Concave polygon shape resource, which can be set into a :ref:`PhysicsBody<class_physicsbody>` or area. This shape is created by feeding a list of triangles.

Member Function Description
---------------------------

.. _class_ConcavePolygonShape_set_faces:

- void  **set_faces**  **(** :ref:`Vector3Array<class_vector3array>` faces  **)**

Set the faces (an array of triangles).

.. _class_ConcavePolygonShape_get_faces:

- :ref:`Vector3Array<class_vector3array>`  **get_faces**  **(** **)** const

Return the faces (an array of triangles).


