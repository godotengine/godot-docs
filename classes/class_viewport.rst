.. _class_Viewport:

Viewport
========

**Inherits:** :ref:`Node<class_node>` **<** :ref:`Object<class_object>`

**Category:** Core

Brief Description
-----------------

Creates a sub-view into the screen.

Member Functions
----------------

+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                                   | :ref:`set_rect<class_Viewport_set_rect>`  **(** :ref:`Rect2<class_rect2>` rect  **)**                                                                                                                         |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Rect2<class_rect2>`                              | :ref:`get_rect<class_Viewport_get_rect>`  **(** **)** const                                                                                                                                                   |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`World2D<class_world2d>`                          | :ref:`find_world_2d<class_Viewport_find_world_2d>`  **(** **)** const                                                                                                                                         |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                                   | :ref:`set_world<class_Viewport_set_world>`  **(** :ref:`World<class_world>` world  **)**                                                                                                                      |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`World<class_world>`                              | :ref:`get_world<class_Viewport_get_world>`  **(** **)** const                                                                                                                                                 |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`World<class_world>`                              | :ref:`find_world<class_Viewport_find_world>`  **(** **)** const                                                                                                                                               |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                                   | :ref:`set_canvas_transform<class_Viewport_set_canvas_transform>`  **(** :ref:`Matrix32<class_matrix32>` xform  **)**                                                                                          |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Matrix32<class_matrix32>`                        | :ref:`get_canvas_transform<class_Viewport_get_canvas_transform>`  **(** **)** const                                                                                                                           |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                                   | :ref:`set_global_canvas_transform<class_Viewport_set_global_canvas_transform>`  **(** :ref:`Matrix32<class_matrix32>` xform  **)**                                                                            |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Matrix32<class_matrix32>`                        | :ref:`get_global_canvas_transform<class_Viewport_get_global_canvas_transform>`  **(** **)** const                                                                                                             |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Matrix32<class_matrix32>`                        | :ref:`get_final_transform<class_Viewport_get_final_transform>`  **(** **)** const                                                                                                                             |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Rect2<class_rect2>`                              | :ref:`get_visible_rect<class_Viewport_get_visible_rect>`  **(** **)** const                                                                                                                                   |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                                   | :ref:`set_transparent_background<class_Viewport_set_transparent_background>`  **(** :ref:`bool<class_bool>` enable  **)**                                                                                     |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`                                | :ref:`has_transparent_background<class_Viewport_has_transparent_background>`  **(** **)** const                                                                                                               |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                                   | :ref:`set_size_override<class_Viewport_set_size_override>`  **(** :ref:`bool<class_bool>` enable, :ref:`Vector2<class_vector2>` size=Vector2(-1,-1), :ref:`Vector2<class_vector2>` margin=Vector2(0,0)  **)** |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector2<class_vector2>`                          | :ref:`get_size_override<class_Viewport_get_size_override>`  **(** **)** const                                                                                                                                 |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`                                | :ref:`is_size_override_enabled<class_Viewport_is_size_override_enabled>`  **(** **)** const                                                                                                                   |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                                   | :ref:`set_size_override_stretch<class_Viewport_set_size_override_stretch>`  **(** :ref:`bool<class_bool>` enabled  **)**                                                                                      |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`                                | :ref:`is_size_override_stretch_enabled<class_Viewport_is_size_override_stretch_enabled>`  **(** **)** const                                                                                                   |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                                   | :ref:`queue_screen_capture<class_Viewport_queue_screen_capture>`  **(** **)**                                                                                                                                 |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Image<class_image>`                              | :ref:`get_screen_capture<class_Viewport_get_screen_capture>`  **(** **)** const                                                                                                                               |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                                   | :ref:`set_as_render_target<class_Viewport_set_as_render_target>`  **(** :ref:`bool<class_bool>` enable  **)**                                                                                                 |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`                                | :ref:`is_set_as_render_target<class_Viewport_is_set_as_render_target>`  **(** **)** const                                                                                                                     |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                                   | :ref:`set_render_target_vflip<class_Viewport_set_render_target_vflip>`  **(** :ref:`bool<class_bool>` enable  **)**                                                                                           |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`                                | :ref:`get_render_target_vflip<class_Viewport_get_render_target_vflip>`  **(** **)** const                                                                                                                     |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                                   | :ref:`set_render_target_clear_on_new_frame<class_Viewport_set_render_target_clear_on_new_frame>`  **(** :ref:`bool<class_bool>` enable  **)**                                                                 |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`                                | :ref:`get_render_target_clear_on_new_frame<class_Viewport_get_render_target_clear_on_new_frame>`  **(** **)** const                                                                                           |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                                   | :ref:`render_target_clear<class_Viewport_render_target_clear>`  **(** **)**                                                                                                                                   |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                                   | :ref:`set_render_target_filter<class_Viewport_set_render_target_filter>`  **(** :ref:`bool<class_bool>` enable  **)**                                                                                         |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`                                | :ref:`get_render_target_filter<class_Viewport_get_render_target_filter>`  **(** **)** const                                                                                                                   |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                                   | :ref:`set_render_target_gen_mipmaps<class_Viewport_set_render_target_gen_mipmaps>`  **(** :ref:`bool<class_bool>` enable  **)**                                                                               |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`                                | :ref:`get_render_target_gen_mipmaps<class_Viewport_get_render_target_gen_mipmaps>`  **(** **)** const                                                                                                         |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                                   | :ref:`set_render_target_update_mode<class_Viewport_set_render_target_update_mode>`  **(** :ref:`int<class_int>` mode  **)**                                                                                   |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`int<class_int>`                                  | :ref:`get_render_target_update_mode<class_Viewport_get_render_target_update_mode>`  **(** **)** const                                                                                                         |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`RenderTargetTexture<class_rendertargettexture>`  | :ref:`get_render_target_texture<class_Viewport_get_render_target_texture>`  **(** **)** const                                                                                                                 |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                                   | :ref:`set_physics_object_picking<class_Viewport_set_physics_object_picking>`  **(** :ref:`bool<class_bool>` enable  **)**                                                                                     |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`                                | :ref:`get_physics_object_picking<class_Viewport_get_physics_object_picking>`  **(** **)**                                                                                                                     |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`RID<class_rid>`                                  | :ref:`get_viewport<class_Viewport_get_viewport>`  **(** **)** const                                                                                                                                           |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                                   | :ref:`input<class_Viewport_input>`  **(** :ref:`InputEvent<class_inputevent>` local_event  **)**                                                                                                              |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                                   | :ref:`unhandled_input<class_Viewport_unhandled_input>`  **(** :ref:`InputEvent<class_inputevent>` local_event  **)**                                                                                          |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                                   | :ref:`update_worlds<class_Viewport_update_worlds>`  **(** **)**                                                                                                                                               |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                                   | :ref:`set_use_own_world<class_Viewport_set_use_own_world>`  **(** :ref:`bool<class_bool>` enable  **)**                                                                                                       |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`                                | :ref:`is_using_own_world<class_Viewport_is_using_own_world>`  **(** **)** const                                                                                                                               |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Camera<class_camera>`                            | :ref:`get_camera<class_Viewport_get_camera>`  **(** **)** const                                                                                                                                               |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                                   | :ref:`set_as_audio_listener<class_Viewport_set_as_audio_listener>`  **(** :ref:`bool<class_bool>` enable  **)**                                                                                               |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`                                | :ref:`is_audio_listener<class_Viewport_is_audio_listener>`  **(** **)** const                                                                                                                                 |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                                   | :ref:`set_as_audio_listener_2d<class_Viewport_set_as_audio_listener_2d>`  **(** :ref:`bool<class_bool>` enable  **)**                                                                                         |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`                                | :ref:`is_audio_listener_2d<class_Viewport_is_audio_listener_2d>`  **(** **)** const                                                                                                                           |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                                   | :ref:`set_render_target_to_screen_rect<class_Viewport_set_render_target_to_screen_rect>`  **(** :ref:`Rect2<class_rect2>` rect  **)**                                                                         |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`Vector2<class_vector2>`                          | :ref:`get_mouse_pos<class_Viewport_get_mouse_pos>`  **(** **)** const                                                                                                                                         |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                                   | :ref:`warp_mouse<class_Viewport_warp_mouse>`  **(** :ref:`Vector2<class_vector2>` to_pos  **)**                                                                                                               |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`                                | :ref:`gui_has_modal_stack<class_Viewport_gui_has_modal_stack>`  **(** **)** const                                                                                                                             |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| void                                                   | :ref:`set_disable_input<class_Viewport_set_disable_input>`  **(** :ref:`bool<class_bool>` disable  **)**                                                                                                      |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bool<class_bool>`                                | :ref:`is_input_disabled<class_Viewport_is_input_disabled>`  **(** **)** const                                                                                                                                 |
+--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Signals
-------

-  **size_changed**  **(** **)**

Numeric Constants
-----------------

- **RENDER_TARGET_UPDATE_DISABLED** = **0**
- **RENDER_TARGET_UPDATE_ONCE** = **1**
- **RENDER_TARGET_UPDATE_WHEN_VISIBLE** = **2**
- **RENDER_TARGET_UPDATE_ALWAYS** = **3**

Description
-----------

A Viewport creates a different view into the screen, or a sub-view inside another viewport. Children 2D Nodes will display on it, and children Camera 3D nodes will render on it too.

Optionally, a viewport can have its own 2D or 3D world, so they don't share what they draw with other viewports.

If a viewport is a child of a :ref:`Control<class_control>`, it will automatically take up its same rect and position, otherwise they must be set manually.

Viewports can also choose to be audio listeners, so they generate positional audio depending on a 2D or 3D camera child of it.

Also, viewports can be assigned to different screens in case the devices have multiple screens.

Finally, viewports can also behave as render targets, in which case they will not be visible unless the associated texture is used to draw.

Member Function Description
---------------------------

.. _class_Viewport_set_rect:

- void  **set_rect**  **(** :ref:`Rect2<class_rect2>` rect  **)**

Set the viewport rect. If the viewport is child of a control, it will use the same rect as the parent.

.. _class_Viewport_get_rect:

- :ref:`Rect2<class_rect2>`  **get_rect**  **(** **)** const

Return the viewport rect. If the viewport is child of a control, it will use the same rect as the parent. Otherwise, if the rect is empty, the viewport will use all the allowed space.

.. _class_Viewport_find_world_2d:

- :ref:`World2D<class_world2d>`  **find_world_2d**  **(** **)** const

.. _class_Viewport_set_world:

- void  **set_world**  **(** :ref:`World<class_world>` world  **)**

.. _class_Viewport_get_world:

- :ref:`World<class_world>`  **get_world**  **(** **)** const

.. _class_Viewport_find_world:

- :ref:`World<class_world>`  **find_world**  **(** **)** const

.. _class_Viewport_set_canvas_transform:

- void  **set_canvas_transform**  **(** :ref:`Matrix32<class_matrix32>` xform  **)**

.. _class_Viewport_get_canvas_transform:

- :ref:`Matrix32<class_matrix32>`  **get_canvas_transform**  **(** **)** const

.. _class_Viewport_set_global_canvas_transform:

- void  **set_global_canvas_transform**  **(** :ref:`Matrix32<class_matrix32>` xform  **)**

.. _class_Viewport_get_global_canvas_transform:

- :ref:`Matrix32<class_matrix32>`  **get_global_canvas_transform**  **(** **)** const

.. _class_Viewport_get_final_transform:

- :ref:`Matrix32<class_matrix32>`  **get_final_transform**  **(** **)** const

.. _class_Viewport_get_visible_rect:

- :ref:`Rect2<class_rect2>`  **get_visible_rect**  **(** **)** const

Return the final, visible rect in global screen coordinates.

.. _class_Viewport_set_transparent_background:

- void  **set_transparent_background**  **(** :ref:`bool<class_bool>` enable  **)**

If this viewport is a child of another viewport, keep the previously drawn background visible.

.. _class_Viewport_has_transparent_background:

- :ref:`bool<class_bool>`  **has_transparent_background**  **(** **)** const

Return whether the viewport lets whatever is behind it to show.

.. _class_Viewport_set_size_override:

- void  **set_size_override**  **(** :ref:`bool<class_bool>` enable, :ref:`Vector2<class_vector2>` size=Vector2(-1,-1), :ref:`Vector2<class_vector2>` margin=Vector2(0,0)  **)**

.. _class_Viewport_get_size_override:

- :ref:`Vector2<class_vector2>`  **get_size_override**  **(** **)** const

.. _class_Viewport_is_size_override_enabled:

- :ref:`bool<class_bool>`  **is_size_override_enabled**  **(** **)** const

.. _class_Viewport_set_size_override_stretch:

- void  **set_size_override_stretch**  **(** :ref:`bool<class_bool>` enabled  **)**

.. _class_Viewport_is_size_override_stretch_enabled:

- :ref:`bool<class_bool>`  **is_size_override_stretch_enabled**  **(** **)** const

.. _class_Viewport_queue_screen_capture:

- void  **queue_screen_capture**  **(** **)**

.. _class_Viewport_get_screen_capture:

- :ref:`Image<class_image>`  **get_screen_capture**  **(** **)** const

.. _class_Viewport_set_as_render_target:

- void  **set_as_render_target**  **(** :ref:`bool<class_bool>` enable  **)**

.. _class_Viewport_is_set_as_render_target:

- :ref:`bool<class_bool>`  **is_set_as_render_target**  **(** **)** const

.. _class_Viewport_set_render_target_vflip:

- void  **set_render_target_vflip**  **(** :ref:`bool<class_bool>` enable  **)**

.. _class_Viewport_get_render_target_vflip:

- :ref:`bool<class_bool>`  **get_render_target_vflip**  **(** **)** const

.. _class_Viewport_set_render_target_clear_on_new_frame:

- void  **set_render_target_clear_on_new_frame**  **(** :ref:`bool<class_bool>` enable  **)**

.. _class_Viewport_get_render_target_clear_on_new_frame:

- :ref:`bool<class_bool>`  **get_render_target_clear_on_new_frame**  **(** **)** const

.. _class_Viewport_render_target_clear:

- void  **render_target_clear**  **(** **)**

.. _class_Viewport_set_render_target_filter:

- void  **set_render_target_filter**  **(** :ref:`bool<class_bool>` enable  **)**

.. _class_Viewport_get_render_target_filter:

- :ref:`bool<class_bool>`  **get_render_target_filter**  **(** **)** const

.. _class_Viewport_set_render_target_gen_mipmaps:

- void  **set_render_target_gen_mipmaps**  **(** :ref:`bool<class_bool>` enable  **)**

.. _class_Viewport_get_render_target_gen_mipmaps:

- :ref:`bool<class_bool>`  **get_render_target_gen_mipmaps**  **(** **)** const

.. _class_Viewport_set_render_target_update_mode:

- void  **set_render_target_update_mode**  **(** :ref:`int<class_int>` mode  **)**

.. _class_Viewport_get_render_target_update_mode:

- :ref:`int<class_int>`  **get_render_target_update_mode**  **(** **)** const

.. _class_Viewport_get_render_target_texture:

- :ref:`RenderTargetTexture<class_rendertargettexture>`  **get_render_target_texture**  **(** **)** const

.. _class_Viewport_set_physics_object_picking:

- void  **set_physics_object_picking**  **(** :ref:`bool<class_bool>` enable  **)**

.. _class_Viewport_get_physics_object_picking:

- :ref:`bool<class_bool>`  **get_physics_object_picking**  **(** **)**

.. _class_Viewport_get_viewport:

- :ref:`RID<class_rid>`  **get_viewport**  **(** **)** const

Get the viewport RID from the visual server.

.. _class_Viewport_input:

- void  **input**  **(** :ref:`InputEvent<class_inputevent>` local_event  **)**

.. _class_Viewport_unhandled_input:

- void  **unhandled_input**  **(** :ref:`InputEvent<class_inputevent>` local_event  **)**

.. _class_Viewport_update_worlds:

- void  **update_worlds**  **(** **)**

.. _class_Viewport_set_use_own_world:

- void  **set_use_own_world**  **(** :ref:`bool<class_bool>` enable  **)**

.. _class_Viewport_is_using_own_world:

- :ref:`bool<class_bool>`  **is_using_own_world**  **(** **)** const

.. _class_Viewport_get_camera:

- :ref:`Camera<class_camera>`  **get_camera**  **(** **)** const

.. _class_Viewport_set_as_audio_listener:

- void  **set_as_audio_listener**  **(** :ref:`bool<class_bool>` enable  **)**

.. _class_Viewport_is_audio_listener:

- :ref:`bool<class_bool>`  **is_audio_listener**  **(** **)** const

.. _class_Viewport_set_as_audio_listener_2d:

- void  **set_as_audio_listener_2d**  **(** :ref:`bool<class_bool>` enable  **)**

.. _class_Viewport_is_audio_listener_2d:

- :ref:`bool<class_bool>`  **is_audio_listener_2d**  **(** **)** const

.. _class_Viewport_set_render_target_to_screen_rect:

- void  **set_render_target_to_screen_rect**  **(** :ref:`Rect2<class_rect2>` rect  **)**

.. _class_Viewport_get_mouse_pos:

- :ref:`Vector2<class_vector2>`  **get_mouse_pos**  **(** **)** const

.. _class_Viewport_warp_mouse:

- void  **warp_mouse**  **(** :ref:`Vector2<class_vector2>` to_pos  **)**

.. _class_Viewport_gui_has_modal_stack:

- :ref:`bool<class_bool>`  **gui_has_modal_stack**  **(** **)** const

.. _class_Viewport_set_disable_input:

- void  **set_disable_input**  **(** :ref:`bool<class_bool>` disable  **)**

.. _class_Viewport_is_input_disabled:

- :ref:`bool<class_bool>`  **is_input_disabled**  **(** **)** const


