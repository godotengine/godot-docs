.. _doc_fog_shader:

Fog shaders
===========

Fog shaders are used to define how fog is added (or subtracted) from a scene in
a given area. Fog shaders are always used together with
:ref:`FogVolumes <class_FogVolume>` and volumetric fog. Fog shaders only have
one processing function, the ``fog()`` function.

The resolution of the fog shaders depends on the resolution of the
volumetric fog froxel grid. Accordingly, the level of detail that a fog shader
can add depends on how close the :ref:`FogVolume <class_FogVolume>` is to the
camera.

Fog shaders are a special form of compute shader that is called once for
every froxel that is touched by an axis aligned bounding box of the associated
:ref:`FogVolume <class_FogVolume>`. This means that froxels that just barely
touch a given :ref:`FogVolume <class_FogVolume>` will still be used. 

Built-ins
^^^^^^^^^

Values marked as "in" are read-only. Values marked as "out" are for optional
writing and will not necessarily contain sensible values. Samplers cannot be 
written to so they are not marked.


Global built-ins
^^^^^^^^^^^^^^^^

Global built-ins are available everywhere, including in custom functions.


+---------------------------------+-----------------------------------------------------------------------------------------+
| Built-in                        | Description                                                                             |
+=================================+=========================================================================================+
| in float **TIME**               | Global time, in seconds.                                                                |
+---------------------------------+-----------------------------------------------------------------------------------------+
| in float **PI**                 | A ``PI`` constant (``3.141592``).                                                       |
|                                 | A ratio of a circle's circumference to its diameter and amount of radians in half turn. |
+---------------------------------+-----------------------------------------------------------------------------------------+
| in float **TAU**                | A ``TAU`` constant (``6.283185``).                                                      |
|                                 | An equivalent of ``PI * 2`` and amount of radians in full turn.                         |
+---------------------------------+-----------------------------------------------------------------------------------------+
| in float **E**                  | A ``E`` constant (``2.718281``).                                                        |
|                                 | Euler's number and a base of the natural logarithm.                                     |
+---------------------------------+-----------------------------------------------------------------------------------------+

Fog built-ins
^^^^^^^^^^^^^

All of the output values of fog volumes overlap one another. This allows
:ref:`FogVolumes <class_FogVolume>` to be rendered efficiently as they can all
be drawn at once.

+-------------------------------+-------------------------------------------------------------------------------------------------+
| Built-in                      | Description                                                                                     |
+===============================+=================================================================================================+
| in vec3 **WORLD_POSITION**    | Position of current froxel cell in world space.                                                 |
+-------------------------------+-------------------------------------------------------------------------------------------------+
| in vec3 **OBJECT_POSITION**   | Position of the center of the current :ref:`FogVolume <class_FogVolume>` in world space.        |
+-------------------------------+-------------------------------------------------------------------------------------------------+
| in vec3 **UVW**               | 3-dimensional uv, used to map a 3D texture to the current :ref:`FogVolume <class_FogVolume>`.   |
+-------------------------------+-------------------------------------------------------------------------------------------------+
| in vec3 **SIZE**              | Size of the current :ref:`FogVolume <class_FogVolume>` when its                                 |
|                               | :ref:`shape<class_FogVolume_property_shape>` has a size.                                        |
+-------------------------------+-------------------------------------------------------------------------------------------------+
| in vec3 **SDF**               | Signed distance field to the surface of the :ref:`FogVolume <class_FogVolume>`. Negative if     |
|                               | inside volume, positive otherwise.                                                              |
+-------------------------------+-------------------------------------------------------------------------------------------------+
| out vec3 **ALBEDO**           | Output base color value, interacts with light to produce final color. Only written to fog       |
|                               | volume if used.                                                                                 |
+-------------------------------+-------------------------------------------------------------------------------------------------+
| out float **DENSITY**         | Output density value. Can be negative to allow subtracting one volume from another. Density     |
|                               | must be used for fog shader to write anything at all.                                           |
+-------------------------------+-------------------------------------------------------------------------------------------------+
| out vec3 **EMISSION**         | Output emission color value, added to color during light pass to produce final color. Only      |
|                               | written to fog volume if used.                                                                  |
+-------------------------------+-------------------------------------------------------------------------------------------------+
