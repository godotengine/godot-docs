.. _doc_spatial_shader:

Spatial shaders
===============

Spatial shaders are used for shading 3D objects. They are the most complex type of shader Godot offers.
Spatial shaders are highly configurable with different render modes and different rendering options
(e.g. Subsurface Scattering, Transmission, Ambient Occlusion, Rim lighting etc). Users can optionally
write vertex, fragment, and light processor functions to affect how objects are drawn.

Render modes
------------
For visual examples of these render modes, see :ref:`Standard Material 3D and ORM Material 3D<doc_standard_material_3d>`.

+-------------------------------+------------------------------------------------------------------------------------------------------+
| Render mode                   | Description                                                                                          |
+===============================+======================================================================================================+
| **blend_mix**                 | Mix blend mode (alpha is transparency), default.                                                     |
+-------------------------------+------------------------------------------------------------------------------------------------------+
| **blend_add**                 | Additive blend mode.                                                                                 |
+-------------------------------+------------------------------------------------------------------------------------------------------+
| **blend_sub**                 | Subtractive blend mode.                                                                              |
+-------------------------------+------------------------------------------------------------------------------------------------------+
| **blend_mul**                 | Multiplicative blend mode.                                                                           |
+-------------------------------+------------------------------------------------------------------------------------------------------+
| **blend_premul_alpha**        | Premultiplied alpha blend mode (fully transparent = add, fully opaque = mix).                        |
+-------------------------------+------------------------------------------------------------------------------------------------------+
| **depth_draw_opaque**         | Only draw depth for opaque geometry (not transparent).                                               |
+-------------------------------+------------------------------------------------------------------------------------------------------+
| **depth_draw_always**         | Always draw depth (opaque and transparent).                                                          |
+-------------------------------+------------------------------------------------------------------------------------------------------+
| **depth_draw_never**          | Never draw depth.                                                                                    |
+-------------------------------+------------------------------------------------------------------------------------------------------+
| **depth_prepass_alpha**       | Do opaque depth pre-pass for transparent geometry.                                                   |
+-------------------------------+------------------------------------------------------------------------------------------------------+
| **depth_test_disabled**       | Disable depth testing.                                                                               |
+-------------------------------+------------------------------------------------------------------------------------------------------+
| **sss_mode_skin**             | Subsurface Scattering mode for skin (optimizes visuals for human skin, e.g. boosted red channel).    |
+-------------------------------+------------------------------------------------------------------------------------------------------+
| **cull_back**                 | Cull back-faces (default).                                                                           |
+-------------------------------+------------------------------------------------------------------------------------------------------+
| **cull_front**                | Cull front-faces.                                                                                    |
+-------------------------------+------------------------------------------------------------------------------------------------------+
| **cull_disabled**             | Culling disabled (double sided).                                                                     |
+-------------------------------+------------------------------------------------------------------------------------------------------+
| **unshaded**                  | Result is just albedo. No lighting/shading happens in material, making it faster to render.          |
+-------------------------------+------------------------------------------------------------------------------------------------------+
| **wireframe**                 | Geometry draws using lines (useful for troubleshooting).                                             |
+-------------------------------+------------------------------------------------------------------------------------------------------+
| **debug_shadow_splits**       | Directional shadows are drawn using different colors for each split (useful for troubleshooting).    |
+-------------------------------+------------------------------------------------------------------------------------------------------+
| **diffuse_burley**            | Burley (Disney PBS) for diffuse (default).                                                           |
+-------------------------------+------------------------------------------------------------------------------------------------------+
| **diffuse_lambert**           | Lambert shading for diffuse.                                                                         |
+-------------------------------+------------------------------------------------------------------------------------------------------+
| **diffuse_lambert_wrap**      | Lambert-wrap shading (roughness-dependent) for diffuse.                                              |
+-------------------------------+------------------------------------------------------------------------------------------------------+
| **diffuse_toon**              | Toon shading for diffuse.                                                                            |
+-------------------------------+------------------------------------------------------------------------------------------------------+
| **specular_schlick_ggx**      | Schlick-GGX for direct light specular lobes (default).                                               |
+-------------------------------+------------------------------------------------------------------------------------------------------+
| **specular_toon**             | Toon for direct light specular lobes.                                                                |
+-------------------------------+------------------------------------------------------------------------------------------------------+
| **specular_disabled**         | Disable direct light specular lobes. Doesn't affect reflected light (use ``SPECULAR = 0.0`` instead).|
+-------------------------------+------------------------------------------------------------------------------------------------------+
| **skip_vertex_transform**     | ``VERTEX``, ``NORMAL``, ``TANGENT``, and ``BITANGENT``                                               |
|                               | need to be transformed manually in the ``vertex()`` function.                                        |
+-------------------------------+------------------------------------------------------------------------------------------------------+
| **world_vertex_coords**       | ``VERTEX``, ``NORMAL``, ``TANGENT``, and ``BITANGENT``                                               |
|                               | are modified in world space instead of model space.                                                  |
+-------------------------------+------------------------------------------------------------------------------------------------------+
| **ensure_correct_normals**    | Use when non-uniform scale is applied to mesh *(note: currently unimplemented)*.                     |
+-------------------------------+------------------------------------------------------------------------------------------------------+
| **shadows_disabled**          | Disable computing shadows in shader. The shader will not receive shadows, but can still cast them.   |
+-------------------------------+------------------------------------------------------------------------------------------------------+
| **ambient_light_disabled**    | Disable contribution from ambient light and radiance map.                                            |
+-------------------------------+------------------------------------------------------------------------------------------------------+
| **shadow_to_opacity**         | Lighting modifies the alpha so shadowed areas are opaque and                                         |
|                               | non-shadowed areas are transparent. Useful for overlaying shadows onto                               |
|                               | a camera feed in AR.                                                                                 |
+-------------------------------+------------------------------------------------------------------------------------------------------+
| **vertex_lighting**           | Use vertex-based lighting instead of per-pixel lighting.                                             |
+-------------------------------+------------------------------------------------------------------------------------------------------+
| **particle_trails**           | Enables the trails when used on particles geometry.                                                  |
+-------------------------------+------------------------------------------------------------------------------------------------------+
| **alpha_to_coverage**         | Alpha antialiasing mode, see `here <https://github.com/godotengine/godot/pull/40364>`_ for more.     |
+-------------------------------+------------------------------------------------------------------------------------------------------+
| **alpha_to_coverage_and_one** | Alpha antialiasing mode, see `here <https://github.com/godotengine/godot/pull/40364>`_ for more.     |
+-------------------------------+------------------------------------------------------------------------------------------------------+
| **fog_disabled**              | Disable receiving depth-based or volumetric fog. Useful for ``blend_add`` materials like particles.  |
+-------------------------------+------------------------------------------------------------------------------------------------------+

Built-ins
---------

Values marked as ``in`` are read-only. Values marked as ``out`` can optionally be written to and will
not necessarily contain sensible values. Values marked as ``inout`` provide a sensible default
value, and can optionally be written to. Samplers cannot be written to so they are not marked.

Not all built-ins are available in all processing functions. To access a vertex
built-in from the ``fragment()`` function, you can use a :ref:`varying <doc_shading_language_varyings>`.
The same applies for accessing fragment built-ins from the ``light()`` function.

Global built-ins
----------------

Global built-ins are available everywhere, including custom functions.

+-----------------------------+-----------------------------------------------------------------------------------------------------+
| Built-in                    | Description                                                                                         |
+=============================+=====================================================================================================+
| in float **TIME**           | Global time since the engine has started, in seconds. It repeats after every ``3,600``              |
|                             | seconds (which can  be changed with the                                                             |
|                             | :ref:`rollover<class_ProjectSettings_property_rendering/limits/time/time_rollover_secs>`            |
|                             | setting). It's affected by :ref:`time_scale<class_Engine_property_time_scale>` but not by pausing.  |
|                             | If you need a ``TIME`` variable that is not affected by time scale, add your own                    |
|                             | :ref:`global shader uniform<doc_shading_language_global_uniforms>` and update it each               |
|                             | frame.                                                                                              |
+-----------------------------+-----------------------------------------------------------------------------------------------------+
| in float **PI**             | A ``PI`` constant (``3.141592``).                                                                   |
|                             | A ratio of a circle's circumference to its diameter and amount of radians in half turn.             |
+-----------------------------+-----------------------------------------------------------------------------------------------------+
| in float **TAU**            | A ``TAU`` constant (``6.283185``).                                                                  |
|                             | An equivalent of ``PI * 2`` and amount of radians in full turn.                                     |
+-----------------------------+-----------------------------------------------------------------------------------------------------+
| in float **E**              | An ``E`` constant (``2.718281``). Euler's number and a base of the natural logarithm.               |
+-----------------------------+-----------------------------------------------------------------------------------------------------+
| in bool **OUTPUT_IS_SRGB**  | ``true`` when output is in sRGB color space (this is ``true`` in the Compatibility                  |
|                             | renderer, ``false`` in Forward+ and Mobile).                                                        |
+-----------------------------+-----------------------------------------------------------------------------------------------------+
| in float **CLIP_SPACE_FAR** | Clip space far ``z`` value.                                                                         |
|                             | In the Forward+ or Mobile renderers, it's ``0.0``.                                                  |
|                             | In the Compatibility renderer, it's ``-1.0``.                                                       |
+-----------------------------+-----------------------------------------------------------------------------------------------------+

Vertex built-ins
----------------

Vertex data (``VERTEX``, ``NORMAL``, ``TANGENT``, and ``BITANGENT``) are presented in model space
(also called local space). If not written to, these values will not be modified and be
passed through as they came, then transformed into view space to be used in ``fragment()``.

They can optionally be presented in world space by using the ``world_vertex_coords`` render mode.

Users can disable the built-in modelview transform (projection will still happen later) and do
it manually with the following code:

.. code-block:: glsl

    shader_type spatial;
    render_mode skip_vertex_transform;

    void vertex() {
        VERTEX = (MODELVIEW_MATRIX * vec4(VERTEX, 1.0)).xyz;
        NORMAL = normalize((MODELVIEW_MATRIX * vec4(NORMAL, 0.0)).xyz);
        BINORMAL = normalize((MODELVIEW_MATRIX * vec4(BINORMAL, 0.0)).xyz);
        TANGENT = normalize((MODELVIEW_MATRIX * vec4(TANGENT, 0.0)).xyz);
    }

Other built-ins, such as ``UV``, ``UV2``, and ``COLOR``, are also passed through to the ``fragment()`` function if not modified.

Users can override the modelview and projection transforms using the ``POSITION`` built-in. If ``POSITION`` is written
to anywhere in the shader, it will always be used, so the user becomes responsible for ensuring that it always has
an acceptable value. When ``POSITION`` is used, the value from ``VERTEX`` is ignored and projection does not happen.
However, the value passed to the fragment shader still comes from ``VERTEX``.

For instancing, the ``INSTANCE_CUSTOM`` variable contains the instance custom data. When using particles, this information
is usually:

* **x**: Rotation angle in radians.
* **y**: Phase during lifetime (``0.0`` to ``1.0``).
* **z**: Animation frame.

This allows you to easily adjust the shader to a particle system using default particles material. When writing a custom particle
shader, this value can be used as desired.

+----------------------------------------+--------------------------------------------------------+
| Built-in                               | Description                                            |
+========================================+========================================================+
| in vec2 **VIEWPORT_SIZE**              | Size of viewport (in pixels).                          |
+----------------------------------------+--------------------------------------------------------+
| in mat4 **VIEW_MATRIX**                | World space to view space transform.                   |
+----------------------------------------+--------------------------------------------------------+
| in mat4 **INV_VIEW_MATRIX**            | View space to world space transform.                   |
+----------------------------------------+--------------------------------------------------------+
| in mat4 **MAIN_CAM_INV_VIEW_MATRIX**   | View space to world space transform of camera used to  |
|                                        | draw the current viewport.                             |
+----------------------------------------+--------------------------------------------------------+
| in mat4 **INV_PROJECTION_MATRIX**      | Clip space to view space transform.                    |
+----------------------------------------+--------------------------------------------------------+
| in vec3 **NODE_POSITION_WORLD**        | Node position, in world space.                         |
+----------------------------------------+--------------------------------------------------------+
| in vec3 **NODE_POSITION_VIEW**         | Node position, in view space.                          |
+----------------------------------------+--------------------------------------------------------+
| in vec3 **CAMERA_POSITION_WORLD**      | Camera position, in world space. Represents the        |
|                                        | midpoint of the two eyes when in multiview/stereo      |
|                                        | rendering.                                             |
+----------------------------------------+--------------------------------------------------------+
| in vec3 **CAMERA_DIRECTION_WORLD**     | Camera direction, in world space.                      |
+----------------------------------------+--------------------------------------------------------+
| in uint **CAMERA_VISIBLE_LAYERS**      | Cull layers of the camera rendering the current pass.  |
+----------------------------------------+--------------------------------------------------------+
| in int **INSTANCE_ID**                 | Instance ID for instancing.                            |
+----------------------------------------+--------------------------------------------------------+
| in vec4 **INSTANCE_CUSTOM**            | Instance custom data (for particles, mostly).          |
+----------------------------------------+--------------------------------------------------------+
| in int **VIEW_INDEX**                  | The view that we are rendering.                        |
|                                        | ``VIEW_MONO_LEFT`` (``0``) for Mono (not multiview) or |
|                                        | left eye, ``VIEW_RIGHT`` (``1``) for right eye.        |
+----------------------------------------+--------------------------------------------------------+
| in int **VIEW_MONO_LEFT**              | Constant for Mono or left eye, always ``0``.           |
+----------------------------------------+--------------------------------------------------------+
| in int **VIEW_RIGHT**                  | Constant for right eye, always ``1``.                  |
+----------------------------------------+--------------------------------------------------------+
| in vec3 **EYE_OFFSET**                 | Position offset for the eye being rendered, in view    |
|                                        | space. Only applicable for multiview rendering.        |
+----------------------------------------+--------------------------------------------------------+
| inout vec3 **VERTEX**                  | Position of the vertex, in model space.                |
|                                        | In world space if ``world_vertex_coords`` is used.     |
+----------------------------------------+--------------------------------------------------------+
| in int **VERTEX_ID**                   | The index of the current vertex in the vertex buffer.  |
+----------------------------------------+--------------------------------------------------------+
| inout vec3 **NORMAL**                  | Normal in model space.                                 |
|                                        | In world space if ``world_vertex_coords`` is used.     |
+----------------------------------------+--------------------------------------------------------+
| inout vec3 **TANGENT**                 | Tangent in model space.                                |
|                                        | In world space if ``world_vertex_coords`` is used.     |
+----------------------------------------+--------------------------------------------------------+
| inout vec3 **BINORMAL**                | Binormal in model space.                               |
|                                        | In world space if ``world_vertex_coords`` is used.     |
+----------------------------------------+--------------------------------------------------------+
| out vec4 **POSITION**                  | If written to, overrides final vertex position in clip |
|                                        | space.                                                 |
+----------------------------------------+--------------------------------------------------------+
| inout vec2 **UV**                      | UV main channel.                                       |
+----------------------------------------+--------------------------------------------------------+
| inout vec2 **UV2**                     | UV secondary channel.                                  |
+----------------------------------------+--------------------------------------------------------+
| inout vec4 **COLOR**                   | Color from vertices.                                   |
+----------------------------------------+--------------------------------------------------------+
| out float **ROUGHNESS**                | Roughness for vertex lighting.                         |
+----------------------------------------+--------------------------------------------------------+
| inout float **POINT_SIZE**             | Point size for point rendering.                        |
+----------------------------------------+--------------------------------------------------------+
| inout mat4 **MODELVIEW_MATRIX**        | Model/local space to view space transform              |
|                                        | (use if possible).                                     |
+----------------------------------------+--------------------------------------------------------+
| inout mat3 **MODELVIEW_NORMAL_MATRIX** |                                                        |
+----------------------------------------+--------------------------------------------------------+
| in mat4 **MODEL_MATRIX**               | Model/local space to world space transform.            |
+----------------------------------------+--------------------------------------------------------+
| in mat3 **MODEL_NORMAL_MATRIX**        |                                                        |
+----------------------------------------+--------------------------------------------------------+
| inout mat4 **PROJECTION_MATRIX**       | View space to clip space transform.                    |
+----------------------------------------+--------------------------------------------------------+
| in uvec4 **BONE_INDICES**              |                                                        |
+----------------------------------------+--------------------------------------------------------+
| in vec4 **BONE_WEIGHTS**               |                                                        |
+----------------------------------------+--------------------------------------------------------+
| in vec4 **CUSTOM0**                    | Custom value from vertex primitive. When using extra   |
|                                        | UVs, ``xy`` is UV3 and ``zw`` is UV4.                  |
+----------------------------------------+--------------------------------------------------------+
| in vec4 **CUSTOM1**                    | Custom value from vertex primitive. When using extra   |
|                                        | UVs, ``xy`` is UV5 and ``zw`` is UV6.                  |
+----------------------------------------+--------------------------------------------------------+
| in vec4 **CUSTOM2**                    | Custom value from vertex primitive. When using extra   |
|                                        | UVs, ``xy`` is UV7 and ``zw`` is UV8.                  |
+----------------------------------------+--------------------------------------------------------+
| in vec4 **CUSTOM3**                    | Custom value from vertex primitive.                    |
+----------------------------------------+--------------------------------------------------------+

.. note::

    ``MODELVIEW_MATRIX`` combines both the ``MODEL_MATRIX`` and ``VIEW_MATRIX`` and is better suited when floating point issues may arise. For example, if the object is very far away from the world origin, you may run into floating point issues when using the separated ``MODEL_MATRIX`` and ``VIEW_MATRIX``.

.. note::

    ``INV_VIEW_MATRIX`` is the matrix used for rendering the object in that pass, unlike ``MAIN_CAM_INV_VIEW_MATRIX``, which is the matrix of the camera in the scene. In the shadow pass, ``INV_VIEW_MATRIX``'s view is based on the camera that is located at the position of the light.

Fragment built-ins
------------------

The default use of a Godot fragment processor function is to set up the material properties of your object
and to let the built-in renderer handle the final shading. However, you are not required to use all
these properties, and if you don't write to them, Godot will optimize away the corresponding functionality.

+----------------------------------------+--------------------------------------------------------------------------------------------------+
| Built-in                               | Description                                                                                      |
+========================================+==================================================================================================+
| in vec2 **VIEWPORT_SIZE**              | Size of viewport (in pixels).                                                                    |
+----------------------------------------+--------------------------------------------------------------------------------------------------+
| in vec4 **FRAGCOORD**                  | Coordinate of pixel center in screen space. ``xy`` specifies position in window. Origin is lower |
|                                        | left. ``z`` specifies fragment depth. It is also used as the output value for the fragment depth |
|                                        | unless ``DEPTH`` is written to.                                                                  |
+----------------------------------------+--------------------------------------------------------------------------------------------------+
| in bool **FRONT_FACING**               | ``true`` if current face is front facing, ``false`` otherwise.                                   |
+----------------------------------------+--------------------------------------------------------------------------------------------------+
| in vec3 **VIEW**                       | Normalized vector from fragment position to camera (in view space). This is the same for both    |
|                                        | perspective and orthogonal cameras.                                                              |
+----------------------------------------+--------------------------------------------------------------------------------------------------+
| in vec2 **UV**                         | UV that comes from the ``vertex()`` function.                                                    |
+----------------------------------------+--------------------------------------------------------------------------------------------------+
| in vec2 **UV2**                        | UV2 that comes from the ``vertex()`` function.                                                   |
+----------------------------------------+--------------------------------------------------------------------------------------------------+
| in vec4 **COLOR**                      | COLOR that comes from the ``vertex()`` function.                                                 |
+----------------------------------------+--------------------------------------------------------------------------------------------------+
| in vec2 **POINT_COORD**                | Point coordinate for drawing points with ``POINT_SIZE``.                                         |
+----------------------------------------+--------------------------------------------------------------------------------------------------+
| in mat4 **MODEL_MATRIX**               | Model/local space to world space transform.                                                      |
+----------------------------------------+--------------------------------------------------------------------------------------------------+
| in mat3 **MODEL_NORMAL_MATRIX**        | Model/local space to world space transform for normals. This is the same as ``MODEL_MATRIX``     |
|                                        | by default unless the object is scaled non-uniformly, in which case this is set to               |
|                                        | ``transpose(inverse(mat3(MODEL_MATRIX)))``.                                                      |
+----------------------------------------+--------------------------------------------------------------------------------------------------+
| in mat4 **VIEW_MATRIX**                | World space to view space transform.                                                             |
+----------------------------------------+--------------------------------------------------------------------------------------------------+
| in mat4 **INV_VIEW_MATRIX**            | View space to world space transform.                                                             |
+----------------------------------------+--------------------------------------------------------------------------------------------------+
| in mat4 **PROJECTION_MATRIX**          | View space to clip space transform.                                                              |
+----------------------------------------+--------------------------------------------------------------------------------------------------+
| in mat4 **INV_PROJECTION_MATRIX**      | Clip space to view space transform.                                                              |
+----------------------------------------+--------------------------------------------------------------------------------------------------+
| in vec3 **NODE_POSITION_WORLD**        | Node position, in world space.                                                                   |
+----------------------------------------+--------------------------------------------------------------------------------------------------+
| in vec3 **NODE_POSITION_VIEW**         | Node position, in view space.                                                                    |
+----------------------------------------+--------------------------------------------------------------------------------------------------+
| in vec3 **CAMERA_POSITION_WORLD**      | Camera position, in world space. Represents the midpoint of the two eyes when in                 |
|                                        | multiview/stereo rendering.                                                                      |
+----------------------------------------+--------------------------------------------------------------------------------------------------+
| in vec3 **CAMERA_DIRECTION_WORLD**     | Camera direction, in world space.                                                                |
+----------------------------------------+--------------------------------------------------------------------------------------------------+
| in uint **CAMERA_VISIBLE_LAYERS**      | Cull layers of the camera rendering the current pass.                                            |
+----------------------------------------+--------------------------------------------------------------------------------------------------+
| in vec3 **VERTEX**                     | Position of the fragment (pixel), in view space. It is the ``VERTEX`` value from ``vertex()``    |
|                                        | interpolated between the face's vertices and transformed into view space.                        |
|                                        | If ``skip_vertex_transform`` is enabled, it may not be in view space.                            |
+----------------------------------------+--------------------------------------------------------------------------------------------------+
| inout vec3 **LIGHT_VERTEX**            | A writable version of ``VERTEX`` that can be used to alter light and shadows. Writing to this    |
|                                        | will not change the position of the fragment.                                                    |
+----------------------------------------+--------------------------------------------------------------------------------------------------+
| in int **VIEW_INDEX**                  | The view that we are rendering. Used to distinguish between views in multiview/stereo rendering. |
|                                        | ``VIEW_MONO_LEFT`` (``0``) for Mono (not multiview) or                                           |
|                                        | left eye, ``VIEW_RIGHT`` (``1``) for right eye.                                                  |
+----------------------------------------+--------------------------------------------------------------------------------------------------+
| in int **VIEW_MONO_LEFT**              | Constant for Mono or left eye, always ``0``.                                                     |
+----------------------------------------+--------------------------------------------------------------------------------------------------+
| in int **VIEW_RIGHT**                  | Constant for right eye, always ``1``.                                                            |
+----------------------------------------+--------------------------------------------------------------------------------------------------+
| in vec3 **EYE_OFFSET**                 | Position offset for the eye being rendered, in view space. Only applicable for multiview         |
|                                        | rendering.                                                                                       |
+----------------------------------------+--------------------------------------------------------------------------------------------------+
| sampler2D **SCREEN_TEXTURE**           | Removed in Godot 4. Use a ``sampler2D`` with ``hint_screen_texture`` instead.                    |
+----------------------------------------+--------------------------------------------------------------------------------------------------+
| in vec2 **SCREEN_UV**                  | Screen UV coordinate for current pixel.                                                          |
+----------------------------------------+--------------------------------------------------------------------------------------------------+
| sampler2D **DEPTH_TEXTURE**            | Removed in Godot 4. Use a ``sampler2D`` with ``hint_depth_texture`` instead.                     |
+----------------------------------------+--------------------------------------------------------------------------------------------------+
| out float **DEPTH**                    | Custom depth value (range of ``[0.0, 1.0]``). If ``DEPTH`` is being written to in any shader     |
|                                        | branch, then you are responsible for setting the ``DEPTH`` for **all** other branches.           |
|                                        | Otherwise, the graphics API will leave them uninitialized.                                       |
+----------------------------------------+--------------------------------------------------------------------------------------------------+
| inout vec3 **NORMAL**                  | Normal that comes from the ``vertex()`` function, in view space.                                 |
|                                        | If ``skip_vertex_transform`` is enabled, it may not be in view space.                            |
+----------------------------------------+--------------------------------------------------------------------------------------------------+
| inout vec3 **TANGENT**                 | Tangent that comes from the ``vertex()`` function, in view space.                                |
|                                        | If ``skip_vertex_transform`` is enabled, it may not be in view space.                            |
+----------------------------------------+--------------------------------------------------------------------------------------------------+
| inout vec3 **BINORMAL**                | Binormal that comes from the ``vertex()`` function, in view space.                               |
|                                        | If ``skip_vertex_transform`` is enabled, it may not be in view space.                            |
+----------------------------------------+--------------------------------------------------------------------------------------------------+
| out vec3 **NORMAL_MAP**                | Set normal here if reading normal from a texture instead of ``NORMAL``.                          |
+----------------------------------------+--------------------------------------------------------------------------------------------------+
| out float **NORMAL_MAP_DEPTH**         | Depth from ``NORMAL_MAP``. Defaults to ``1.0``.                                                  |
+----------------------------------------+--------------------------------------------------------------------------------------------------+
| out vec3 **ALBEDO**                    | Albedo (default white). Base color.                                                              |
+----------------------------------------+--------------------------------------------------------------------------------------------------+
| out float **ALPHA**                    | Alpha (range of ``[0.0, 1.0]``). If read from or written to, the material will go to the         |
|                                        | transparent pipeline.                                                                            |
+----------------------------------------+--------------------------------------------------------------------------------------------------+
| out float **ALPHA_SCISSOR_THRESHOLD**  | If written to, values below a certain amount of alpha are discarded.                             |
+----------------------------------------+--------------------------------------------------------------------------------------------------+
| out float **ALPHA_HASH_SCALE**         | Alpha hash scale when using the alpha hash transparency mode. Defaults to ``1.0``.               |
|                                        | Higher values result in more visible pixels in the dithering pattern.                            |
+----------------------------------------+--------------------------------------------------------------------------------------------------+
| out float **ALPHA_ANTIALIASING_EDGE**  | The threshold below which alpha to coverage antialiasing should be used. Defaults to ``0.0``.    |
|                                        | Requires the ``alpha_to_coverage`` render mode. Should be set to a value lower than              |
|                                        | ``ALPHA_SCISSOR_THRESHOLD`` to be effective.                                                     |
+----------------------------------------+--------------------------------------------------------------------------------------------------+
| out vec2 **ALPHA_TEXTURE_COORDINATE**  | The texture coordinate to use for alpha-to-coverge antialiasing. Requires the                    |
|                                        | ``alpha_to_coverage`` render mode. Typically set to ``UV * vec2(albedo_texture_size)`` where     |
|                                        | ``albedo_texture_size`` is the size of the albedo texture in pixels.                             |
+----------------------------------------+--------------------------------------------------------------------------------------------------+
| out float **PREMUL_ALPHA_FACTOR**      | Premultiplied alpha factor. Only effective if ``render_mode blend_premul_alpha;`` is used.       |
|                                        | This should be written to when using a *shaded* material with premultiplied alpha blending for   |
|                                        | interaction with lighting. This is not required for unshaded materials.                          |
+----------------------------------------+--------------------------------------------------------------------------------------------------+
| out float **METALLIC**                 | Metallic (range of ``[0.0, 1.0]``).                                                              |
+----------------------------------------+--------------------------------------------------------------------------------------------------+
| out float **SPECULAR**                 | Specular (not physically accurate to change). Defaults to ``0.5``. ``0.0`` disables reflections. |
+----------------------------------------+--------------------------------------------------------------------------------------------------+
| out float **ROUGHNESS**                | Roughness (range of ``[0.0, 1.0]``).                                                             |
+----------------------------------------+--------------------------------------------------------------------------------------------------+
| out float **RIM**                      | Rim (range of ``[0.0, 1.0]``). If used, Godot calculates rim lighting.                           |
|                                        | Rim size depends on ``ROUGHNESS``.                                                               |
+----------------------------------------+--------------------------------------------------------------------------------------------------+
| out float **RIM_TINT**                 | Rim Tint, range of ``0.0`` (white) to ``1.0`` (albedo). If used, Godot calculates rim lighting.  |
+----------------------------------------+--------------------------------------------------------------------------------------------------+
| out float **CLEARCOAT**                | Small specular blob added on top of the existing one. If used, Godot calculates clearcoat.       |
+----------------------------------------+--------------------------------------------------------------------------------------------------+
| out float **CLEARCOAT_GLOSS**          | Gloss of clearcoat. If used, Godot calculates clearcoat.                                         |
+----------------------------------------+--------------------------------------------------------------------------------------------------+
| out float **ANISOTROPY**               | For distorting the specular blob according to tangent space.                                     |
+----------------------------------------+--------------------------------------------------------------------------------------------------+
| out vec2 **ANISOTROPY_FLOW**           | Distortion direction, use with flowmaps.                                                         |
+----------------------------------------+--------------------------------------------------------------------------------------------------+
| out float **SSS_STRENGTH**             | Strength of subsurface scattering. If used, subsurface scattering will be applied to the object. |
+----------------------------------------+--------------------------------------------------------------------------------------------------+
| out vec4 **SSS_TRANSMITTANCE_COLOR**   | Color of subsurface scattering transmittance. If used, subsurface scattering transmittance       |
|                                        | will be applied to the object.                                                                   |
+----------------------------------------+--------------------------------------------------------------------------------------------------+
| out float **SSS_TRANSMITTANCE_DEPTH**  | Depth of subsurface scattering transmittance. Higher values allow the effect to reach deeper     |
|                                        | into the object.                                                                                 |
+----------------------------------------+--------------------------------------------------------------------------------------------------+
| out float **SSS_TRANSMITTANCE_BOOST**  | Boosts the subsurface scattering transmittance if set above ``0.0``. This makes the effect       |
|                                        | show up even on directly lit surfaces                                                            |
+----------------------------------------+--------------------------------------------------------------------------------------------------+
| inout vec3 **BACKLIGHT**               | Color of backlighting (works like direct light, but it's received even if the normal             |
|                                        | is slightly facing away from the light). If used, backlighting will be applied to the object.    |
|                                        | Can be used as a cheaper approximation of subsurface scattering.                                 |
+----------------------------------------+--------------------------------------------------------------------------------------------------+
| out float **AO**                       | Strength of ambient occlusion. For use with pre-baked AO.                                        |
+----------------------------------------+--------------------------------------------------------------------------------------------------+
| out float **AO_LIGHT_AFFECT**          | How much ambient occlusion affects direct light (range of ``[0.0, 1.0]``, default ``0.0``).      |
+----------------------------------------+--------------------------------------------------------------------------------------------------+
| out vec3 **EMISSION**                  | Emission color (can go over ``(1.0, 1.0, 1.0)`` for HDR).                                        |
+----------------------------------------+--------------------------------------------------------------------------------------------------+
| out vec4 **FOG**                       | If written to, blends final pixel color with ``FOG.rgb`` based on ``FOG.a``.                     |
+----------------------------------------+--------------------------------------------------------------------------------------------------+
| out vec4 **RADIANCE**                  | If written to, blends environment map radiance with ``RADIANCE.rgb`` based on ``RADIANCE.a``.    |
+----------------------------------------+--------------------------------------------------------------------------------------------------+
| out vec4 **IRRADIANCE**                | If written to, blends environment map irradiance with ``IRRADIANCE.rgb`` based on                |
|                                        | ``IRRADIANCE.a``.                                                                                |
+----------------------------------------+--------------------------------------------------------------------------------------------------+

.. note::

    Shaders going through the transparent pipeline when ``ALPHA`` is written to
    may exhibit transparency sorting issues. Read the
    :ref:`transparency sorting section in the 3D rendering limitations page <doc_3d_rendering_limitations_transparency_sorting>`
    for more information and ways to avoid issues.

Light built-ins
---------------

Writing light processor functions is completely optional. You can skip the ``light()`` function by using
the ``unshaded`` render mode. If no light function is written, Godot will use the material properties
written to in the ``fragment()`` function to calculate the lighting for you (subject to the render mode).

The ``light()`` function is called for every light in every pixel. It is called within a loop for each light type.

Below is an example of a custom ``light()`` function using a Lambertian lighting model:

.. code-block:: glsl

    void light() {
        DIFFUSE_LIGHT += clamp(dot(NORMAL, LIGHT), 0.0, 1.0) * ATTENUATION * LIGHT_COLOR / PI;
    }

If you want the lights to add together, add the light contribution to ``DIFFUSE_LIGHT`` using ``+=``, rather than overwriting it.

.. warning::

    The ``light()`` function won't be run if the ``vertex_lighting`` render mode is enabled, or if
    :ref:`Rendering > Quality > Shading > Force Vertex Shading<class_ProjectSettings_property_rendering/shading/overrides/force_vertex_shading>`
    is enabled in the Project Settings. (It's enabled by default on mobile platforms.)

+-----------------------------------+------------------------------------------------------------------------+
| Built-in                          | Description                                                            |
+===================================+========================================================================+
| in vec2 **VIEWPORT_SIZE**         | Size of viewport (in pixels).                                          |
+-----------------------------------+------------------------------------------------------------------------+
| in vec4 **FRAGCOORD**             | Coordinate of pixel center in screen space.                            |
|                                   | ``xy`` specifies position in window, ``z``                             |
|                                   | specifies fragment depth if ``DEPTH`` is not used.                     |
|                                   | Origin is lower-left.                                                  |
+-----------------------------------+------------------------------------------------------------------------+
| in mat4 **MODEL_MATRIX**          | Model/local space to world space transform.                            |
+-----------------------------------+------------------------------------------------------------------------+
| in mat4 **INV_VIEW_MATRIX**       | View space to world space transform.                                   |
+-----------------------------------+------------------------------------------------------------------------+
| in mat4 **VIEW_MATRIX**           | World space to view space transform.                                   |
+-----------------------------------+------------------------------------------------------------------------+
| in mat4 **PROJECTION_MATRIX**     | View space to clip space transform.                                    |
+-----------------------------------+------------------------------------------------------------------------+
| in mat4 **INV_PROJECTION_MATRIX** | Clip space to view space transform.                                    |
+-----------------------------------+------------------------------------------------------------------------+
| in vec3 **NORMAL**                | Normal vector, in view space.                                          |
+-----------------------------------+------------------------------------------------------------------------+
| in vec2 **SCREEN_UV**             | Screen UV coordinate for current pixel.                                |
+-----------------------------------+------------------------------------------------------------------------+
| in vec2 **UV**                    | UV that comes from the ``vertex()`` function.                          |
+-----------------------------------+------------------------------------------------------------------------+
| in vec2 **UV2**                   | UV2 that comes from the ``vertex()`` function.                         |
+-----------------------------------+------------------------------------------------------------------------+
| in vec3 **VIEW**                  | View vector, in view space.                                            |
+-----------------------------------+------------------------------------------------------------------------+
| in vec3 **LIGHT**                 | Light vector, in view space.                                           |
+-----------------------------------+------------------------------------------------------------------------+
| in vec3 **LIGHT_COLOR**           | :ref:`Light color<class_Light3D_property_light_color>` multiplied by   |
|                                   | :ref:`light energy<class_Light3D_property_light_energy>` multiplied by |
|                                   | ``PI``. The ``PI`` multiplication is present because                   |
|                                   | physically-based lighting models include a division by ``PI``.         |
+-----------------------------------+------------------------------------------------------------------------+
| in float **SPECULAR_AMOUNT**      | For :ref:`class_OmniLight3D` and :ref:`class_SpotLight3D`,             |
|                                   | ``2.0`` multiplied by                                                  |
|                                   | :ref:`light_specular<class_Light3D_property_light_specular>`.          |
|                                   | For :ref:`class_DirectionalLight3D`, ``1.0``.                          |
+-----------------------------------+------------------------------------------------------------------------+
| in bool **LIGHT_IS_DIRECTIONAL**  | ``true`` if this pass is a :ref:`class_DirectionalLight3D`.            |
+-----------------------------------+------------------------------------------------------------------------+
| in float **ATTENUATION**          | Attenuation based on distance or shadow.                               |
+-----------------------------------+------------------------------------------------------------------------+
| in vec3 **ALBEDO**                | Base albedo.                                                           |
+-----------------------------------+------------------------------------------------------------------------+
| in vec3 **BACKLIGHT**             |                                                                        |
+-----------------------------------+------------------------------------------------------------------------+
| in float **METALLIC**             | Metallic.                                                              |
+-----------------------------------+------------------------------------------------------------------------+
| in float **ROUGHNESS**            | Roughness.                                                             |
+-----------------------------------+------------------------------------------------------------------------+
| out vec3 **DIFFUSE_LIGHT**        | Diffuse light result.                                                  |
+-----------------------------------+------------------------------------------------------------------------+
| out vec3 **SPECULAR_LIGHT**       | Specular light result.                                                 |
+-----------------------------------+------------------------------------------------------------------------+
| out float **ALPHA**               | Alpha (range of ``[0.0, 1.0]``). If written to, the material will go   |
|                                   | to the transparent pipeline.                                           |
+-----------------------------------+------------------------------------------------------------------------+

.. note::

    Shaders going through the transparent pipeline when ``ALPHA`` is written to
    may exhibit transparency sorting issues. Read the
    :ref:`transparency sorting section in the 3D rendering limitations page <doc_3d_rendering_limitations_transparency_sorting>`
    for more information and ways to avoid issues.

    Transparent materials also cannot cast shadows or appear in
    ``hint_screen_texture`` and ``hint_depth_texture`` uniforms. This in turn prevents those
    materials from appearing in screen-space reflections or refraction.
    :ref:`SDFGI <doc_using_sdfgi>` sharp reflections are not visible on transparent
    materials (only rough reflections are visible on transparent materials).
