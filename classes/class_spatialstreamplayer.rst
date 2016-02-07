.. _class_SpatialStreamPlayer:

SpatialStreamPlayer
===================

**Inherits:** :ref:`SpatialPlayer<class_spatialplayer>` **<** :ref:`Spatial<class_spatial>` **<** :ref:`Node<class_node>` **<** :ref:`Object<class_object>`

**Category:** Core

Brief Description
-----------------



Member Functions
----------------

+------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`set_stream<class_SpatialStreamPlayer_set_stream>`  **(** Stream stream  **)**                                        |
+------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| Stream                       | :ref:`get_stream<class_SpatialStreamPlayer_get_stream>`  **(** **)** const                                                 |
+------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`play<class_SpatialStreamPlayer_play>`  **(** :ref:`float<class_float>` offset=0  **)**                               |
+------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`stop<class_SpatialStreamPlayer_stop>`  **(** **)**                                                                   |
+------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`      | :ref:`is_playing<class_SpatialStreamPlayer_is_playing>`  **(** **)** const                                                 |
+------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`set_paused<class_SpatialStreamPlayer_set_paused>`  **(** :ref:`bool<class_bool>` paused  **)**                       |
+------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`      | :ref:`is_paused<class_SpatialStreamPlayer_is_paused>`  **(** **)** const                                                   |
+------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`set_loop<class_SpatialStreamPlayer_set_loop>`  **(** :ref:`bool<class_bool>` enabled  **)**                          |
+------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`      | :ref:`has_loop<class_SpatialStreamPlayer_has_loop>`  **(** **)** const                                                     |
+------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`set_volume<class_SpatialStreamPlayer_set_volume>`  **(** :ref:`float<class_float>` volume  **)**                     |
+------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`    | :ref:`get_volume<class_SpatialStreamPlayer_get_volume>`  **(** **)** const                                                 |
+------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`set_volume_db<class_SpatialStreamPlayer_set_volume_db>`  **(** :ref:`float<class_float>` db  **)**                   |
+------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`    | :ref:`get_volume_db<class_SpatialStreamPlayer_get_volume_db>`  **(** **)** const                                           |
+------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`set_buffering_msec<class_SpatialStreamPlayer_set_buffering_msec>`  **(** :ref:`int<class_int>` msec  **)**           |
+------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`        | :ref:`get_buffering_msec<class_SpatialStreamPlayer_get_buffering_msec>`  **(** **)** const                                 |
+------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`set_loop_restart_time<class_SpatialStreamPlayer_set_loop_restart_time>`  **(** :ref:`float<class_float>` secs  **)** |
+------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`    | :ref:`get_loop_restart_time<class_SpatialStreamPlayer_get_loop_restart_time>`  **(** **)** const                           |
+------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`String<class_string>`  | :ref:`get_stream_name<class_SpatialStreamPlayer_get_stream_name>`  **(** **)** const                                       |
+------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`        | :ref:`get_loop_count<class_SpatialStreamPlayer_get_loop_count>`  **(** **)** const                                         |
+------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`    | :ref:`get_pos<class_SpatialStreamPlayer_get_pos>`  **(** **)** const                                                       |
+------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`seek_pos<class_SpatialStreamPlayer_seek_pos>`  **(** :ref:`float<class_float>` time  **)**                           |
+------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| void                         | :ref:`set_autoplay<class_SpatialStreamPlayer_set_autoplay>`  **(** :ref:`bool<class_bool>` enabled  **)**                  |
+------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`      | :ref:`has_autoplay<class_SpatialStreamPlayer_has_autoplay>`  **(** **)** const                                             |
+------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`    | :ref:`get_length<class_SpatialStreamPlayer_get_length>`  **(** **)** const                                                 |
+------------------------------+----------------------------------------------------------------------------------------------------------------------------+

Member Function Description
---------------------------

.. _class_SpatialStreamPlayer_set_stream:

- void  **set_stream**  **(** Stream stream  **)**

.. _class_SpatialStreamPlayer_get_stream:

- Stream  **get_stream**  **(** **)** const

.. _class_SpatialStreamPlayer_play:

- void  **play**  **(** :ref:`float<class_float>` offset=0  **)**

.. _class_SpatialStreamPlayer_stop:

- void  **stop**  **(** **)**

.. _class_SpatialStreamPlayer_is_playing:

- :ref:`bool<class_bool>`  **is_playing**  **(** **)** const

.. _class_SpatialStreamPlayer_set_paused:

- void  **set_paused**  **(** :ref:`bool<class_bool>` paused  **)**

.. _class_SpatialStreamPlayer_is_paused:

- :ref:`bool<class_bool>`  **is_paused**  **(** **)** const

.. _class_SpatialStreamPlayer_set_loop:

- void  **set_loop**  **(** :ref:`bool<class_bool>` enabled  **)**

.. _class_SpatialStreamPlayer_has_loop:

- :ref:`bool<class_bool>`  **has_loop**  **(** **)** const

.. _class_SpatialStreamPlayer_set_volume:

- void  **set_volume**  **(** :ref:`float<class_float>` volume  **)**

.. _class_SpatialStreamPlayer_get_volume:

- :ref:`float<class_float>`  **get_volume**  **(** **)** const

.. _class_SpatialStreamPlayer_set_volume_db:

- void  **set_volume_db**  **(** :ref:`float<class_float>` db  **)**

.. _class_SpatialStreamPlayer_get_volume_db:

- :ref:`float<class_float>`  **get_volume_db**  **(** **)** const

.. _class_SpatialStreamPlayer_set_buffering_msec:

- void  **set_buffering_msec**  **(** :ref:`int<class_int>` msec  **)**

.. _class_SpatialStreamPlayer_get_buffering_msec:

- :ref:`int<class_int>`  **get_buffering_msec**  **(** **)** const

.. _class_SpatialStreamPlayer_set_loop_restart_time:

- void  **set_loop_restart_time**  **(** :ref:`float<class_float>` secs  **)**

.. _class_SpatialStreamPlayer_get_loop_restart_time:

- :ref:`float<class_float>`  **get_loop_restart_time**  **(** **)** const

.. _class_SpatialStreamPlayer_get_stream_name:

- :ref:`String<class_string>`  **get_stream_name**  **(** **)** const

.. _class_SpatialStreamPlayer_get_loop_count:

- :ref:`int<class_int>`  **get_loop_count**  **(** **)** const

.. _class_SpatialStreamPlayer_get_pos:

- :ref:`float<class_float>`  **get_pos**  **(** **)** const

.. _class_SpatialStreamPlayer_seek_pos:

- void  **seek_pos**  **(** :ref:`float<class_float>` time  **)**

.. _class_SpatialStreamPlayer_set_autoplay:

- void  **set_autoplay**  **(** :ref:`bool<class_bool>` enabled  **)**

.. _class_SpatialStreamPlayer_has_autoplay:

- :ref:`bool<class_bool>`  **has_autoplay**  **(** **)** const

.. _class_SpatialStreamPlayer_get_length:

- :ref:`float<class_float>`  **get_length**  **(** **)** const


