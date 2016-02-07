.. _class_ColorRamp:

ColorRamp
=========

**Inherits:** :ref:`Resource<class_resource>`

**Category:** Core



Member Functions
----------------

+--------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| void                                 | :ref:`add_point<class_ColorRamp_add_point>`  **(** :ref:`float<class_float>` offset, :ref:`Color<class_color>` color  **)** |
+--------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| void                                 | :ref:`remove_point<class_ColorRamp_remove_point>`  **(** :ref:`int<class_int>` offset  **)**                                |
+--------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| void                                 | :ref:`set_offset<class_ColorRamp_set_offset>`  **(** :ref:`int<class_int>` point, :ref:`float<class_float>` offset  **)**   |
+--------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`            | :ref:`get_offset<class_ColorRamp_get_offset>`  **(** :ref:`int<class_int>` point  **)** const                               |
+--------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| void                                 | :ref:`set_color<class_ColorRamp_set_color>`  **(** :ref:`int<class_int>` point, :ref:`Color<class_color>` color  **)**      |
+--------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| :ref:`Color<class_color>`            | :ref:`get_color<class_ColorRamp_get_color>`  **(** :ref:`int<class_int>` point  **)** const                                 |
+--------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| :ref:`Color<class_color>`            | :ref:`interpolate<class_ColorRamp_interpolate>`  **(** :ref:`float<class_float>` offset  **)**                              |
+--------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`                | :ref:`get_point_count<class_ColorRamp_get_point_count>`  **(** **)** const                                                  |
+--------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| void                                 | :ref:`set_offsets<class_ColorRamp_set_offsets>`  **(** :ref:`RealArray<class_realarray>` offsets  **)**                     |
+--------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| :ref:`RealArray<class_realarray>`    | :ref:`get_offsets<class_ColorRamp_get_offsets>`  **(** **)** const                                                          |
+--------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| void                                 | :ref:`set_colors<class_ColorRamp_set_colors>`  **(** :ref:`ColorArray<class_colorarray>` colors  **)**                      |
+--------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| :ref:`ColorArray<class_colorarray>`  | :ref:`get_colors<class_ColorRamp_get_colors>`  **(** **)** const                                                            |
+--------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+

Member Function Description
---------------------------

.. _class_ColorRamp_add_point:

- void  **add_point**  **(** :ref:`float<class_float>` offset, :ref:`Color<class_color>` color  **)**

.. _class_ColorRamp_remove_point:

- void  **remove_point**  **(** :ref:`int<class_int>` offset  **)**

.. _class_ColorRamp_set_offset:

- void  **set_offset**  **(** :ref:`int<class_int>` point, :ref:`float<class_float>` offset  **)**

.. _class_ColorRamp_get_offset:

- :ref:`float<class_float>`  **get_offset**  **(** :ref:`int<class_int>` point  **)** const

.. _class_ColorRamp_set_color:

- void  **set_color**  **(** :ref:`int<class_int>` point, :ref:`Color<class_color>` color  **)**

.. _class_ColorRamp_get_color:

- :ref:`Color<class_color>`  **get_color**  **(** :ref:`int<class_int>` point  **)** const

.. _class_ColorRamp_interpolate:

- :ref:`Color<class_color>`  **interpolate**  **(** :ref:`float<class_float>` offset  **)**

.. _class_ColorRamp_get_point_count:

- :ref:`int<class_int>`  **get_point_count**  **(** **)** const

.. _class_ColorRamp_set_offsets:

- void  **set_offsets**  **(** :ref:`RealArray<class_realarray>` offsets  **)**

.. _class_ColorRamp_get_offsets:

- :ref:`RealArray<class_realarray>`  **get_offsets**  **(** **)** const

.. _class_ColorRamp_set_colors:

- void  **set_colors**  **(** :ref:`ColorArray<class_colorarray>` colors  **)**

.. _class_ColorRamp_get_colors:

- :ref:`ColorArray<class_colorarray>`  **get_colors**  **(** **)** const


