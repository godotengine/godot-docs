.. _class_Camera2D:

Camera2D
========

**Inherits:** :ref:`Node2D<class_node2d>`

**Category:** Core

Camera node for 2D scenes.

Member Functions
----------------

+--------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_offset<class_Camera2D_set_offset>`  **(** :ref:`Vector2<class_vector2>` offset  **)**                                          |
+--------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector2<class_vector2>`  | :ref:`get_offset<class_Camera2D_get_offset>`  **(** **)** const                                                                          |
+--------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_anchor_mode<class_Camera2D_set_anchor_mode>`  **(** :ref:`int<class_int>` anchor_mode  **)**                                   |
+--------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`          | :ref:`get_anchor_mode<class_Camera2D_get_anchor_mode>`  **(** **)** const                                                                |
+--------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_rotating<class_Camera2D_set_rotating>`  **(** :ref:`bool<class_bool>` rotating  **)**                                          |
+--------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`        | :ref:`is_rotating<class_Camera2D_is_rotating>`  **(** **)** const                                                                        |
+--------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`make_current<class_Camera2D_make_current>`  **(** **)**                                                                            |
+--------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`clear_current<class_Camera2D_clear_current>`  **(** **)**                                                                          |
+--------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`        | :ref:`is_current<class_Camera2D_is_current>`  **(** **)** const                                                                          |
+--------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_limit<class_Camera2D_set_limit>`  **(** :ref:`int<class_int>` margin, :ref:`int<class_int>` limit  **)**                       |
+--------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`          | :ref:`get_limit<class_Camera2D_get_limit>`  **(** :ref:`int<class_int>` margin  **)** const                                              |
+--------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_v_drag_enabled<class_Camera2D_set_v_drag_enabled>`  **(** :ref:`bool<class_bool>` enabled  **)**                               |
+--------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`        | :ref:`is_v_drag_enabled<class_Camera2D_is_v_drag_enabled>`  **(** **)** const                                                            |
+--------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_h_drag_enabled<class_Camera2D_set_h_drag_enabled>`  **(** :ref:`bool<class_bool>` enabled  **)**                               |
+--------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`        | :ref:`is_h_drag_enabled<class_Camera2D_is_h_drag_enabled>`  **(** **)** const                                                            |
+--------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_v_offset<class_Camera2D_set_v_offset>`  **(** :ref:`float<class_float>` ofs  **)**                                             |
+--------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`      | :ref:`get_v_offset<class_Camera2D_get_v_offset>`  **(** **)** const                                                                      |
+--------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_h_offset<class_Camera2D_set_h_offset>`  **(** :ref:`float<class_float>` ofs  **)**                                             |
+--------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`      | :ref:`get_h_offset<class_Camera2D_get_h_offset>`  **(** **)** const                                                                      |
+--------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_drag_margin<class_Camera2D_set_drag_margin>`  **(** :ref:`int<class_int>` margin, :ref:`float<class_float>` drag_margin  **)** |
+--------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`      | :ref:`get_drag_margin<class_Camera2D_get_drag_margin>`  **(** :ref:`int<class_int>` margin  **)** const                                  |
+--------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector2<class_vector2>`  | :ref:`get_camera_pos<class_Camera2D_get_camera_pos>`  **(** **)** const                                                                  |
+--------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector2<class_vector2>`  | :ref:`get_camera_screen_center<class_Camera2D_get_camera_screen_center>`  **(** **)** const                                              |
+--------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_zoom<class_Camera2D_set_zoom>`  **(** :ref:`Vector2<class_vector2>` zoom  **)**                                                |
+--------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector2<class_vector2>`  | :ref:`get_zoom<class_Camera2D_get_zoom>`  **(** **)** const                                                                              |
+--------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_follow_smoothing<class_Camera2D_set_follow_smoothing>`  **(** :ref:`float<class_float>` follow_smoothing  **)**                |
+--------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`      | :ref:`get_follow_smoothing<class_Camera2D_get_follow_smoothing>`  **(** **)** const                                                      |
+--------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`set_enable_follow_smoothing<class_Camera2D_set_enable_follow_smoothing>`  **(** :ref:`bool<class_bool>` follow_smoothing  **)**    |
+--------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`        | :ref:`is_follow_smoothing_enabled<class_Camera2D_is_follow_smoothing_enabled>`  **(** **)** const                                        |
+--------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| void                           | :ref:`force_update_scroll<class_Camera2D_force_update_scroll>`  **(** **)**                                                              |
+--------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+

Numeric Constants
-----------------

- **ANCHOR_MODE_DRAG_CENTER** = **1**
- **ANCHOR_MODE_FIXED_TOP_LEFT** = **0**

Description
-----------

Camera node for 2D scenes. It forces the screen (current layer) to scroll following this node. This makes it easier (and faster) to program scrollable scenes than manually changing the position of :ref:`CanvasItem<class_canvasitem>` based nodes.

This node is intended to be a simple helper get get things going quickly and it may happen often that more functionality is desired to change how the camera works. To make your own custom camera node, simply inherit from :ref:`Node2D<class_node2d>` and change the transform of the canvas by calling get_viewport().set_canvas_transform(m) in :ref:`Viewport<class_viewport>`.

Member Function Description
---------------------------

.. _class_Camera2D_set_offset:

- void  **set_offset**  **(** :ref:`Vector2<class_vector2>` offset  **)**

Set the scroll offset. Useful for looking around or camera shake animations.

.. _class_Camera2D_get_offset:

- :ref:`Vector2<class_vector2>`  **get_offset**  **(** **)** const

Return the scroll offset.

.. _class_Camera2D_set_anchor_mode:

- void  **set_anchor_mode**  **(** :ref:`int<class_int>` anchor_mode  **)**

.. _class_Camera2D_get_anchor_mode:

- :ref:`int<class_int>`  **get_anchor_mode**  **(** **)** const

.. _class_Camera2D_set_rotating:

- void  **set_rotating**  **(** :ref:`bool<class_bool>` rotating  **)**

.. _class_Camera2D_is_rotating:

- :ref:`bool<class_bool>`  **is_rotating**  **(** **)** const

.. _class_Camera2D_make_current:

- void  **make_current**  **(** **)**

Make this the current 2D camera for the scene (viewport and layer), in case there's many cameras in the scene.

.. _class_Camera2D_clear_current:

- void  **clear_current**  **(** **)**

.. _class_Camera2D_is_current:

- :ref:`bool<class_bool>`  **is_current**  **(** **)** const

Return true of this is the current camera (see :ref:`Camera2D.make_current<camera2d_make_current>`).

.. _class_Camera2D_set_limit:

- void  **set_limit**  **(** :ref:`int<class_int>` margin, :ref:`int<class_int>` limit  **)**

Set the scrolling limit in pixels.

.. _class_Camera2D_get_limit:

- :ref:`int<class_int>`  **get_limit**  **(** :ref:`int<class_int>` margin  **)** const

Return the scrolling limit in pixels.

.. _class_Camera2D_set_v_drag_enabled:

- void  **set_v_drag_enabled**  **(** :ref:`bool<class_bool>` enabled  **)**

.. _class_Camera2D_is_v_drag_enabled:

- :ref:`bool<class_bool>`  **is_v_drag_enabled**  **(** **)** const

.. _class_Camera2D_set_h_drag_enabled:

- void  **set_h_drag_enabled**  **(** :ref:`bool<class_bool>` enabled  **)**

.. _class_Camera2D_is_h_drag_enabled:

- :ref:`bool<class_bool>`  **is_h_drag_enabled**  **(** **)** const

.. _class_Camera2D_set_v_offset:

- void  **set_v_offset**  **(** :ref:`float<class_float>` ofs  **)**

.. _class_Camera2D_get_v_offset:

- :ref:`float<class_float>`  **get_v_offset**  **(** **)** const

.. _class_Camera2D_set_h_offset:

- void  **set_h_offset**  **(** :ref:`float<class_float>` ofs  **)**

.. _class_Camera2D_get_h_offset:

- :ref:`float<class_float>`  **get_h_offset**  **(** **)** const

.. _class_Camera2D_set_drag_margin:

- void  **set_drag_margin**  **(** :ref:`int<class_int>` margin, :ref:`float<class_float>` drag_margin  **)**

Set the margins needed to drag the camera (relative to the screen size). Margin uses the MARGIN\_\* enum. Drag margins of 0,0,0,0 will keep the camera at the center of the screen, while drag margins of 1,1,1,1 will only move when the camera is at the edges.

.. _class_Camera2D_get_drag_margin:

- :ref:`float<class_float>`  **get_drag_margin**  **(** :ref:`int<class_int>` margin  **)** const

Return the margins needed to drag the camera (see :ref:`set_drag_margin<Camera2D_set_drag_margin>`).

.. _class_Camera2D_get_camera_pos:

- :ref:`Vector2<class_vector2>`  **get_camera_pos**  **(** **)** const

Return the camera position.

.. _class_Camera2D_get_camera_screen_center:

- :ref:`Vector2<class_vector2>`  **get_camera_screen_center**  **(** **)** const

.. _class_Camera2D_set_zoom:

- void  **set_zoom**  **(** :ref:`Vector2<class_vector2>` zoom  **)**

.. _class_Camera2D_get_zoom:

- :ref:`Vector2<class_vector2>`  **get_zoom**  **(** **)** const

.. _class_Camera2D_set_follow_smoothing:

- void  **set_follow_smoothing**  **(** :ref:`float<class_float>` follow_smoothing  **)**

.. _class_Camera2D_get_follow_smoothing:

- :ref:`float<class_float>`  **get_follow_smoothing**  **(** **)** const

.. _class_Camera2D_set_enable_follow_smoothing:

- void  **set_enable_follow_smoothing**  **(** :ref:`bool<class_bool>` follow_smoothing  **)**

.. _class_Camera2D_is_follow_smoothing_enabled:

- :ref:`bool<class_bool>`  **is_follow_smoothing_enabled**  **(** **)** const

.. _class_Camera2D_force_update_scroll:

- void  **force_update_scroll**  **(** **)**

Force the camera to update scroll immediately.


