.. _class_SpatialSamplePlayer:

SpatialSamplePlayer
===================

**Inherits:** :ref:`SpatialPlayer<class_spatialplayer>` **<** :ref:`Spatial<class_spatial>` **<** :ref:`Node<class_node>` **<** :ref:`Object<class_object>`

**Category:** Core

Brief Description
-----------------



Member Functions
----------------

+--------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                       | :ref:`set_sample_library<class_SpatialSamplePlayer_set_sample_library>`  **(** :ref:`SampleLibrary<class_samplelibrary>` library  **)**                       |
+--------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`SampleLibrary<class_samplelibrary>`  | :ref:`get_sample_library<class_SpatialSamplePlayer_get_sample_library>`  **(** **)** const                                                                    |
+--------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                       | :ref:`set_polyphony<class_SpatialSamplePlayer_set_polyphony>`  **(** :ref:`int<class_int>` voices  **)**                                                      |
+--------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`                      | :ref:`get_polyphony<class_SpatialSamplePlayer_get_polyphony>`  **(** **)** const                                                                              |
+--------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`                      | :ref:`play<class_SpatialSamplePlayer_play>`  **(** :ref:`String<class_string>` sample, :ref:`int<class_int>` voice=-2  **)**                                  |
+--------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                       | :ref:`voice_set_pitch_scale<class_SpatialSamplePlayer_voice_set_pitch_scale>`  **(** :ref:`int<class_int>` voice, :ref:`float<class_float>` ratio  **)**      |
+--------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                       | :ref:`voice_set_volume_scale_db<class_SpatialSamplePlayer_voice_set_volume_scale_db>`  **(** :ref:`int<class_int>` voice, :ref:`float<class_float>` db  **)** |
+--------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`                    | :ref:`is_voice_active<class_SpatialSamplePlayer_is_voice_active>`  **(** :ref:`int<class_int>` voice  **)** const                                             |
+--------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                       | :ref:`stop_voice<class_SpatialSamplePlayer_stop_voice>`  **(** :ref:`int<class_int>` voice  **)**                                                             |
+--------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                       | :ref:`stop_all<class_SpatialSamplePlayer_stop_all>`  **(** **)**                                                                                              |
+--------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

Numeric Constants
-----------------

- **INVALID_VOICE** = **-1**
- **NEXT_VOICE** = **-2**

Member Function Description
---------------------------

.. _class_SpatialSamplePlayer_set_sample_library:

- void  **set_sample_library**  **(** :ref:`SampleLibrary<class_samplelibrary>` library  **)**

.. _class_SpatialSamplePlayer_get_sample_library:

- :ref:`SampleLibrary<class_samplelibrary>`  **get_sample_library**  **(** **)** const

.. _class_SpatialSamplePlayer_set_polyphony:

- void  **set_polyphony**  **(** :ref:`int<class_int>` voices  **)**

.. _class_SpatialSamplePlayer_get_polyphony:

- :ref:`int<class_int>`  **get_polyphony**  **(** **)** const

.. _class_SpatialSamplePlayer_play:

- :ref:`int<class_int>`  **play**  **(** :ref:`String<class_string>` sample, :ref:`int<class_int>` voice=-2  **)**

.. _class_SpatialSamplePlayer_voice_set_pitch_scale:

- void  **voice_set_pitch_scale**  **(** :ref:`int<class_int>` voice, :ref:`float<class_float>` ratio  **)**

.. _class_SpatialSamplePlayer_voice_set_volume_scale_db:

- void  **voice_set_volume_scale_db**  **(** :ref:`int<class_int>` voice, :ref:`float<class_float>` db  **)**

.. _class_SpatialSamplePlayer_is_voice_active:

- :ref:`bool<class_bool>`  **is_voice_active**  **(** :ref:`int<class_int>` voice  **)** const

.. _class_SpatialSamplePlayer_stop_voice:

- void  **stop_voice**  **(** :ref:`int<class_int>` voice  **)**

.. _class_SpatialSamplePlayer_stop_all:

- void  **stop_all**  **(** **)**


