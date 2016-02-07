.. _class_Particles2D:

Particles2D
===========

**Inherits:** :ref:`Node2D<class_node2d>` **<** :ref:`CanvasItem<class_canvasitem>` **<** :ref:`Node<class_node>` **<** :ref:`Object<class_object>`

**Category:** Core

Brief Description
-----------------



Member Functions
----------------

+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                     | :ref:`set_emitting<class_Particles2D_set_emitting>`  **(** :ref:`bool<class_bool>` active  **)**                                                 |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`                  | :ref:`is_emitting<class_Particles2D_is_emitting>`  **(** **)** const                                                                             |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                     | :ref:`set_amount<class_Particles2D_set_amount>`  **(** :ref:`int<class_int>` amount  **)**                                                       |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`                    | :ref:`get_amount<class_Particles2D_get_amount>`  **(** **)** const                                                                               |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                     | :ref:`set_lifetime<class_Particles2D_set_lifetime>`  **(** :ref:`float<class_float>` lifetime  **)**                                             |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`                | :ref:`get_lifetime<class_Particles2D_get_lifetime>`  **(** **)** const                                                                           |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                     | :ref:`set_time_scale<class_Particles2D_set_time_scale>`  **(** :ref:`float<class_float>` time_scale  **)**                                       |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`                | :ref:`get_time_scale<class_Particles2D_get_time_scale>`  **(** **)** const                                                                       |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                     | :ref:`set_pre_process_time<class_Particles2D_set_pre_process_time>`  **(** :ref:`float<class_float>` time  **)**                                 |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`                | :ref:`get_pre_process_time<class_Particles2D_get_pre_process_time>`  **(** **)** const                                                           |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                     | :ref:`set_emit_timeout<class_Particles2D_set_emit_timeout>`  **(** :ref:`float<class_float>` value  **)**                                        |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`                | :ref:`get_emit_timeout<class_Particles2D_get_emit_timeout>`  **(** **)** const                                                                   |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                     | :ref:`set_param<class_Particles2D_set_param>`  **(** :ref:`int<class_int>` param, :ref:`float<class_float>` value  **)**                         |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`                | :ref:`get_param<class_Particles2D_get_param>`  **(** :ref:`int<class_int>` param  **)** const                                                    |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                     | :ref:`set_randomness<class_Particles2D_set_randomness>`  **(** :ref:`int<class_int>` param, :ref:`float<class_float>` value  **)**               |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`                | :ref:`get_randomness<class_Particles2D_get_randomness>`  **(** :ref:`int<class_int>` param  **)** const                                          |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Texture<class_texture>`            | :ref:`set_texture<class_Particles2D_set_texture>`  **(** :ref:`Object<class_object>` texture  **)**                                              |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Texture<class_texture>`            | :ref:`get_texture<class_Particles2D_get_texture>`  **(** **)** const                                                                             |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                     | :ref:`set_color<class_Particles2D_set_color>`  **(** :ref:`Color<class_color>` color  **)**                                                      |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Color<class_color>`                | :ref:`get_color<class_Particles2D_get_color>`  **(** **)** const                                                                                 |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`ColorRamp<class_colorramp>`        | :ref:`set_color_ramp<class_Particles2D_set_color_ramp>`  **(** :ref:`Object<class_object>` color_ramp  **)**                                     |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`ColorRamp<class_colorramp>`        | :ref:`get_color_ramp<class_Particles2D_get_color_ramp>`  **(** **)** const                                                                       |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                     | :ref:`set_emissor_offset<class_Particles2D_set_emissor_offset>`  **(** :ref:`Vector2<class_vector2>` offset  **)**                               |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector2<class_vector2>`            | :ref:`get_emissor_offset<class_Particles2D_get_emissor_offset>`  **(** **)** const                                                               |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                     | :ref:`set_flip_h<class_Particles2D_set_flip_h>`  **(** :ref:`bool<class_bool>` enable  **)**                                                     |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`                  | :ref:`is_flipped_h<class_Particles2D_is_flipped_h>`  **(** **)** const                                                                           |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                     | :ref:`set_flip_v<class_Particles2D_set_flip_v>`  **(** :ref:`bool<class_bool>` enable  **)**                                                     |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`                  | :ref:`is_flipped_v<class_Particles2D_is_flipped_v>`  **(** **)** const                                                                           |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                     | :ref:`set_h_frames<class_Particles2D_set_h_frames>`  **(** :ref:`int<class_int>` enable  **)**                                                   |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`                    | :ref:`get_h_frames<class_Particles2D_get_h_frames>`  **(** **)** const                                                                           |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                     | :ref:`set_v_frames<class_Particles2D_set_v_frames>`  **(** :ref:`int<class_int>` enable  **)**                                                   |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`                    | :ref:`get_v_frames<class_Particles2D_get_v_frames>`  **(** **)** const                                                                           |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                     | :ref:`set_emission_half_extents<class_Particles2D_set_emission_half_extents>`  **(** :ref:`Vector2<class_vector2>` extents  **)**                |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector2<class_vector2>`            | :ref:`get_emission_half_extents<class_Particles2D_get_emission_half_extents>`  **(** **)** const                                                 |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                     | :ref:`set_color_phases<class_Particles2D_set_color_phases>`  **(** :ref:`int<class_int>` phases  **)**                                           |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`                    | :ref:`get_color_phases<class_Particles2D_get_color_phases>`  **(** **)** const                                                                   |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                     | :ref:`set_color_phase_color<class_Particles2D_set_color_phase_color>`  **(** :ref:`int<class_int>` phase, :ref:`Color<class_color>` color  **)** |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Color<class_color>`                | :ref:`get_color_phase_color<class_Particles2D_get_color_phase_color>`  **(** :ref:`int<class_int>` phase  **)** const                            |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                     | :ref:`set_color_phase_pos<class_Particles2D_set_color_phase_pos>`  **(** :ref:`int<class_int>` phase, :ref:`float<class_float>` pos  **)**       |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`                | :ref:`get_color_phase_pos<class_Particles2D_get_color_phase_pos>`  **(** :ref:`int<class_int>` phase  **)** const                                |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                     | :ref:`pre_process<class_Particles2D_pre_process>`  **(** :ref:`float<class_float>` time  **)**                                                   |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                     | :ref:`reset<class_Particles2D_reset>`  **(** **)**                                                                                               |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                     | :ref:`set_use_local_space<class_Particles2D_set_use_local_space>`  **(** :ref:`bool<class_bool>` enable  **)**                                   |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`                  | :ref:`is_using_local_space<class_Particles2D_is_using_local_space>`  **(** **)** const                                                           |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                     | :ref:`set_initial_velocity<class_Particles2D_set_initial_velocity>`  **(** :ref:`Vector2<class_vector2>` velocity  **)**                         |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector2<class_vector2>`            | :ref:`get_initial_velocity<class_Particles2D_get_initial_velocity>`  **(** **)** const                                                           |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                     | :ref:`set_explosiveness<class_Particles2D_set_explosiveness>`  **(** :ref:`float<class_float>` amount  **)**                                     |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`                | :ref:`get_explosiveness<class_Particles2D_get_explosiveness>`  **(** **)** const                                                                 |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                     | :ref:`set_emission_points<class_Particles2D_set_emission_points>`  **(** :ref:`Vector2Array<class_vector2array>` points  **)**                   |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector2Array<class_vector2array>`  | :ref:`get_emission_points<class_Particles2D_get_emission_points>`  **(** **)** const                                                             |
+------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+

Numeric Constants
-----------------

- **PARAM_DIRECTION** = **0**
- **PARAM_SPREAD** = **1**
- **PARAM_LINEAR_VELOCITY** = **2**
- **PARAM_SPIN_VELOCITY** = **3**
- **PARAM_ORBIT_VELOCITY** = **4**
- **PARAM_GRAVITY_DIRECTION** = **5**
- **PARAM_GRAVITY_STRENGTH** = **6**
- **PARAM_RADIAL_ACCEL** = **7**
- **PARAM_TANGENTIAL_ACCEL** = **8**
- **PARAM_DAMPING** = **9**
- **PARAM_INITIAL_ANGLE** = **10**
- **PARAM_INITIAL_SIZE** = **11**
- **PARAM_FINAL_SIZE** = **12**
- **PARAM_HUE_VARIATION** = **13**
- **PARAM_ANIM_SPEED_SCALE** = **14**
- **PARAM_ANIM_INITIAL_POS** = **15**
- **PARAM_MAX** = **16**
- **MAX_COLOR_PHASES** = **4**

Member Function Description
---------------------------

.. _class_Particles2D_set_emitting:

- void  **set_emitting**  **(** :ref:`bool<class_bool>` active  **)**

.. _class_Particles2D_is_emitting:

- :ref:`bool<class_bool>`  **is_emitting**  **(** **)** const

.. _class_Particles2D_set_amount:

- void  **set_amount**  **(** :ref:`int<class_int>` amount  **)**

.. _class_Particles2D_get_amount:

- :ref:`int<class_int>`  **get_amount**  **(** **)** const

.. _class_Particles2D_set_lifetime:

- void  **set_lifetime**  **(** :ref:`float<class_float>` lifetime  **)**

.. _class_Particles2D_get_lifetime:

- :ref:`float<class_float>`  **get_lifetime**  **(** **)** const

.. _class_Particles2D_set_time_scale:

- void  **set_time_scale**  **(** :ref:`float<class_float>` time_scale  **)**

.. _class_Particles2D_get_time_scale:

- :ref:`float<class_float>`  **get_time_scale**  **(** **)** const

.. _class_Particles2D_set_pre_process_time:

- void  **set_pre_process_time**  **(** :ref:`float<class_float>` time  **)**

.. _class_Particles2D_get_pre_process_time:

- :ref:`float<class_float>`  **get_pre_process_time**  **(** **)** const

.. _class_Particles2D_set_emit_timeout:

- void  **set_emit_timeout**  **(** :ref:`float<class_float>` value  **)**

.. _class_Particles2D_get_emit_timeout:

- :ref:`float<class_float>`  **get_emit_timeout**  **(** **)** const

.. _class_Particles2D_set_param:

- void  **set_param**  **(** :ref:`int<class_int>` param, :ref:`float<class_float>` value  **)**

.. _class_Particles2D_get_param:

- :ref:`float<class_float>`  **get_param**  **(** :ref:`int<class_int>` param  **)** const

.. _class_Particles2D_set_randomness:

- void  **set_randomness**  **(** :ref:`int<class_int>` param, :ref:`float<class_float>` value  **)**

.. _class_Particles2D_get_randomness:

- :ref:`float<class_float>`  **get_randomness**  **(** :ref:`int<class_int>` param  **)** const

.. _class_Particles2D_set_texture:

- :ref:`Texture<class_texture>`  **set_texture**  **(** :ref:`Object<class_object>` texture  **)**

.. _class_Particles2D_get_texture:

- :ref:`Texture<class_texture>`  **get_texture**  **(** **)** const

.. _class_Particles2D_set_color:

- void  **set_color**  **(** :ref:`Color<class_color>` color  **)**

.. _class_Particles2D_get_color:

- :ref:`Color<class_color>`  **get_color**  **(** **)** const

.. _class_Particles2D_set_color_ramp:

- :ref:`ColorRamp<class_colorramp>`  **set_color_ramp**  **(** :ref:`Object<class_object>` color_ramp  **)**

.. _class_Particles2D_get_color_ramp:

- :ref:`ColorRamp<class_colorramp>`  **get_color_ramp**  **(** **)** const

.. _class_Particles2D_set_emissor_offset:

- void  **set_emissor_offset**  **(** :ref:`Vector2<class_vector2>` offset  **)**

.. _class_Particles2D_get_emissor_offset:

- :ref:`Vector2<class_vector2>`  **get_emissor_offset**  **(** **)** const

.. _class_Particles2D_set_flip_h:

- void  **set_flip_h**  **(** :ref:`bool<class_bool>` enable  **)**

.. _class_Particles2D_is_flipped_h:

- :ref:`bool<class_bool>`  **is_flipped_h**  **(** **)** const

.. _class_Particles2D_set_flip_v:

- void  **set_flip_v**  **(** :ref:`bool<class_bool>` enable  **)**

.. _class_Particles2D_is_flipped_v:

- :ref:`bool<class_bool>`  **is_flipped_v**  **(** **)** const

.. _class_Particles2D_set_h_frames:

- void  **set_h_frames**  **(** :ref:`int<class_int>` enable  **)**

.. _class_Particles2D_get_h_frames:

- :ref:`int<class_int>`  **get_h_frames**  **(** **)** const

.. _class_Particles2D_set_v_frames:

- void  **set_v_frames**  **(** :ref:`int<class_int>` enable  **)**

.. _class_Particles2D_get_v_frames:

- :ref:`int<class_int>`  **get_v_frames**  **(** **)** const

.. _class_Particles2D_set_emission_half_extents:

- void  **set_emission_half_extents**  **(** :ref:`Vector2<class_vector2>` extents  **)**

.. _class_Particles2D_get_emission_half_extents:

- :ref:`Vector2<class_vector2>`  **get_emission_half_extents**  **(** **)** const

.. _class_Particles2D_set_color_phases:

- void  **set_color_phases**  **(** :ref:`int<class_int>` phases  **)**

.. _class_Particles2D_get_color_phases:

- :ref:`int<class_int>`  **get_color_phases**  **(** **)** const

.. _class_Particles2D_set_color_phase_color:

- void  **set_color_phase_color**  **(** :ref:`int<class_int>` phase, :ref:`Color<class_color>` color  **)**

.. _class_Particles2D_get_color_phase_color:

- :ref:`Color<class_color>`  **get_color_phase_color**  **(** :ref:`int<class_int>` phase  **)** const

.. _class_Particles2D_set_color_phase_pos:

- void  **set_color_phase_pos**  **(** :ref:`int<class_int>` phase, :ref:`float<class_float>` pos  **)**

.. _class_Particles2D_get_color_phase_pos:

- :ref:`float<class_float>`  **get_color_phase_pos**  **(** :ref:`int<class_int>` phase  **)** const

.. _class_Particles2D_pre_process:

- void  **pre_process**  **(** :ref:`float<class_float>` time  **)**

.. _class_Particles2D_reset:

- void  **reset**  **(** **)**

.. _class_Particles2D_set_use_local_space:

- void  **set_use_local_space**  **(** :ref:`bool<class_bool>` enable  **)**

.. _class_Particles2D_is_using_local_space:

- :ref:`bool<class_bool>`  **is_using_local_space**  **(** **)** const

.. _class_Particles2D_set_initial_velocity:

- void  **set_initial_velocity**  **(** :ref:`Vector2<class_vector2>` velocity  **)**

.. _class_Particles2D_get_initial_velocity:

- :ref:`Vector2<class_vector2>`  **get_initial_velocity**  **(** **)** const

.. _class_Particles2D_set_explosiveness:

- void  **set_explosiveness**  **(** :ref:`float<class_float>` amount  **)**

.. _class_Particles2D_get_explosiveness:

- :ref:`float<class_float>`  **get_explosiveness**  **(** **)** const

.. _class_Particles2D_set_emission_points:

- void  **set_emission_points**  **(** :ref:`Vector2Array<class_vector2array>` points  **)**

.. _class_Particles2D_get_emission_points:

- :ref:`Vector2Array<class_vector2array>`  **get_emission_points**  **(** **)** const


