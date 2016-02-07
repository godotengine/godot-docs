.. _class_DirectionalLight:

DirectionalLight
================

Inherits: :ref:`Light<class_light>`
-----------------------------------

Category: Core
--------------

Brief Description
-----------------

Directional Light, such as the Sun or the Moon.

Member Functions
----------------

+----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| void                       | :ref:`set_shadow_mode<class_DirectionalLight_set_shadow_mode>`  **(** :ref:`int<class_int>` mode  **)**                                     |
+----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`      | :ref:`get_shadow_mode<class_DirectionalLight_get_shadow_mode>`  **(** **)** const                                                           |
+----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| void                       | :ref:`set_shadow_param<class_DirectionalLight_set_shadow_param>`  **(** :ref:`int<class_int>` param, :ref:`float<class_float>` value  **)** |
+----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`  | :ref:`get_shadow_param<class_DirectionalLight_get_shadow_param>`  **(** :ref:`int<class_int>` param  **)** const                            |
+----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+

Numeric Constants
-----------------

- **SHADOW_ORTHOGONAL** = **0**
- **SHADOW_PERSPECTIVE** = **1**
- **SHADOW_PARALLEL_2_SPLITS** = **2**
- **SHADOW_PARALLEL_4_SPLITS** = **3**
- **SHADOW_PARAM_MAX_DISTANCE** = **0**
- **SHADOW_PARAM_PSSM_SPLIT_WEIGHT** = **1**
- **SHADOW_PARAM_PSSM_ZOFFSET_SCALE** = **2**

Description
-----------

A DirectionalLight is a type of :ref:`Light<class_light>` node that emits light constantly in one direction (the negative z axis of the node). It is used lights with strong intensity that are located far away from the scene to model sunlight or moonlight. The worldpace location of the DirectionalLight transform (origin) is ignored, only the basis is used do determine light direction.

Member Function Description
---------------------------

.. _class_DirectionalLight_set_shadow_mode:

- void  **set_shadow_mode**  **(** :ref:`int<class_int>` mode  **)**

.. _class_DirectionalLight_get_shadow_mode:

- :ref:`int<class_int>`  **get_shadow_mode**  **(** **)** const

.. _class_DirectionalLight_set_shadow_param:

- void  **set_shadow_param**  **(** :ref:`int<class_int>` param, :ref:`float<class_float>` value  **)**

.. _class_DirectionalLight_get_shadow_param:

- :ref:`float<class_float>`  **get_shadow_param**  **(** :ref:`int<class_int>` param  **)** const


