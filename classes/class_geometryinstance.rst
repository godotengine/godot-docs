.. _class_GeometryInstance:

GeometryInstance
================

**Inherits:** :ref:`VisualInstance<class_visualinstance>`

**Category:** Core

Base node for geometry based visual instances.

Member Functions
----------------

+------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`set_material_override<class_GeometryInstance_set_material_override>`  **(** :ref:`Object<class_object>` material  **)** |
+------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Object<class_object>`  | :ref:`get_material_override<class_GeometryInstance_get_material_override>`  **(** **)** const                                 |
+------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`set_flag<class_GeometryInstance_set_flag>`  **(** :ref:`int<class_int>` flag, :ref:`bool<class_bool>` value  **)**      |
+------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`      | :ref:`get_flag<class_GeometryInstance_get_flag>`  **(** :ref:`int<class_int>` flag  **)** const                               |
+------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`set_draw_range_begin<class_GeometryInstance_set_draw_range_begin>`  **(** :ref:`float<class_float>` mode  **)**         |
+------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`    | :ref:`get_draw_range_begin<class_GeometryInstance_get_draw_range_begin>`  **(** **)** const                                   |
+------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`set_draw_range_end<class_GeometryInstance_set_draw_range_end>`  **(** :ref:`float<class_float>` mode  **)**             |
+------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`    | :ref:`get_draw_range_end<class_GeometryInstance_get_draw_range_end>`  **(** **)** const                                       |
+------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`set_baked_light_texture_id<class_GeometryInstance_set_baked_light_texture_id>`  **(** :ref:`int<class_int>` id  **)**   |
+------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`        | :ref:`get_baked_light_texture_id<class_GeometryInstance_get_baked_light_texture_id>`  **(** **)** const                       |
+------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`set_extra_cull_margin<class_GeometryInstance_set_extra_cull_margin>`  **(** :ref:`float<class_float>` margin  **)**     |
+------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`    | :ref:`get_extra_cull_margin<class_GeometryInstance_get_extra_cull_margin>`  **(** **)** const                                 |
+------------------------------+-------------------------------------------------------------------------------------------------------------------------------+

Numeric Constants
-----------------

- **FLAG_VISIBLE** = **0**
- **FLAG_CAST_SHADOW** = **3**
- **FLAG_RECEIVE_SHADOWS** = **4**
- **FLAG_BILLBOARD** = **1**
- **FLAG_BILLBOARD_FIX_Y** = **2**
- **FLAG_DEPH_SCALE** = **5**
- **FLAG_VISIBLE_IN_ALL_ROOMS** = **6**
- **FLAG_MAX** = **8**

Description
-----------

Base node for geometry based visual instances. Shares some common functionality like visibility and custom materials.

Member Function Description
---------------------------

.. _class_GeometryInstance_set_material_override:

- void  **set_material_override**  **(** :ref:`Object<class_object>` material  **)**

Set the material override for the whole geometry.

.. _class_GeometryInstance_get_material_override:

- :ref:`Object<class_object>`  **get_material_override**  **(** **)** const

Return the material override for the whole geometry.

.. _class_GeometryInstance_set_flag:

- void  **set_flag**  **(** :ref:`int<class_int>` flag, :ref:`bool<class_bool>` value  **)**

.. _class_GeometryInstance_get_flag:

- :ref:`bool<class_bool>`  **get_flag**  **(** :ref:`int<class_int>` flag  **)** const

.. _class_GeometryInstance_set_draw_range_begin:

- void  **set_draw_range_begin**  **(** :ref:`float<class_float>` mode  **)**

.. _class_GeometryInstance_get_draw_range_begin:

- :ref:`float<class_float>`  **get_draw_range_begin**  **(** **)** const

.. _class_GeometryInstance_set_draw_range_end:

- void  **set_draw_range_end**  **(** :ref:`float<class_float>` mode  **)**

.. _class_GeometryInstance_get_draw_range_end:

- :ref:`float<class_float>`  **get_draw_range_end**  **(** **)** const

.. _class_GeometryInstance_set_baked_light_texture_id:

- void  **set_baked_light_texture_id**  **(** :ref:`int<class_int>` id  **)**

.. _class_GeometryInstance_get_baked_light_texture_id:

- :ref:`int<class_int>`  **get_baked_light_texture_id**  **(** **)** const

.. _class_GeometryInstance_set_extra_cull_margin:

- void  **set_extra_cull_margin**  **(** :ref:`float<class_float>` margin  **)**

.. _class_GeometryInstance_get_extra_cull_margin:

- :ref:`float<class_float>`  **get_extra_cull_margin**  **(** **)** const


