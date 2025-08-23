.. _doc_canvas_item_shader:

CanvasItem shaders
==================

CanvasItem shaders are used to draw all 2D elements in Godot. These include
all nodes that inherit from CanvasItems, and all GUI elements.

CanvasItem shaders contain fewer built-in variables and functionality than
:ref:`Spatial shaders<doc_spatial_shader>`, but they maintain the same basic structure
with vertex, fragment, and light processor functions.

Render modes
------------

+---------------------------------+----------------------------------------------------------------------+
| Render mode                     | Description                                                          |
+=================================+======================================================================+
| **blend_mix**                   | Mix blend mode (alpha is transparency), default.                     |
+---------------------------------+----------------------------------------------------------------------+
| **blend_add**                   | Additive blend mode.                                                 |
+---------------------------------+----------------------------------------------------------------------+
| **blend_sub**                   | Subtractive blend mode.                                              |
+---------------------------------+----------------------------------------------------------------------+
| **blend_mul**                   | Multiplicative blend mode.                                           |
+---------------------------------+----------------------------------------------------------------------+
| **blend_premul_alpha**          | Pre-multiplied alpha blend mode.                                     |
+---------------------------------+----------------------------------------------------------------------+
| **blend_disabled**              | Disable blending, values (including alpha) are written as-is.        |
+---------------------------------+----------------------------------------------------------------------+
| **unshaded**                    | Result is just albedo. No lighting/shading happens in material.      |
+---------------------------------+----------------------------------------------------------------------+
| **light_only**                  | Only draw on light pass.                                             |
+---------------------------------+----------------------------------------------------------------------+
| **skip_vertex_transform**       | ``VERTEX`` needs to be transformed manually in the ``vertex()``      |
|                                 | function.                                                            |
+---------------------------------+----------------------------------------------------------------------+
| **world_vertex_coords**         | ``VERTEX`` is modified in world coordinates instead of local.        |
+---------------------------------+----------------------------------------------------------------------+

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

+-------------------+------------------------------------------------------------------------------------------+
| Built-in          | Description                                                                              |
+===================+==========================================================================================+
| in float **TIME** | Global time since the engine has started, in seconds. It repeats after every ``3,600``   |
|                   | seconds (which can  be changed with the                                                  |
|                   | :ref:`rollover<class_ProjectSettings_property_rendering/limits/time/time_rollover_secs>` |
|                   | setting). It's affected by                                                               |
|                   | :ref:`time_scale<class_Engine_property_time_scale>` but not by pausing. If you need a    |
|                   | ``TIME`` variable that is not affected by time scale, add your own                       |
|                   | :ref:`global shader uniform<doc_shading_language_global_uniforms>` and update it each    |
|                   | frame.                                                                                   |
+-------------------+------------------------------------------------------------------------------------------+
| in float **PI**   | A ``PI`` constant (``3.141592``).                                                        |
|                   | A ratio of a circle's circumference to its diameter and amount of radians in half turn.  |
+-------------------+------------------------------------------------------------------------------------------+
| in float **TAU**  | A ``TAU`` constant (``6.283185``).                                                       |
|                   | An equivalent of ``PI * 2`` and amount of radians in full turn.                          |
+-------------------+------------------------------------------------------------------------------------------+
| in float **E**    | An ``E`` constant (``2.718281``).                                                        |
|                   | Euler's number and a base of the natural logarithm.                                      |
+-------------------+------------------------------------------------------------------------------------------+

Vertex built-ins
----------------

Vertex data (``VERTEX``) is presented in local space (pixel coordinates, relative to the Node2D's origin).
If not written to, these values will not be modified and be passed through as they came.

The user can disable the built-in model to world transform (world to screen and projection will still
happen later) and do it manually with the following code:

.. code-block:: glsl

    shader_type canvas_item;
    render_mode skip_vertex_transform;

    void vertex() {

        VERTEX = (MODEL_MATRIX * vec4(VERTEX, 0.0, 1.0)).xy;
    }

Other built-ins, such as ``UV`` and ``COLOR``, are also passed through to the ``fragment()`` function if not modified.

For instancing, the ``INSTANCE_CUSTOM`` variable contains the instance custom data. When using particles, this information
is usually:

* **x**: Rotation angle in radians.
* **y**: Phase during lifetime (``0.0`` to ``1.0``).
* **z**: Animation frame.

+--------------------------------+----------------------------------------------------------------+
| Built-in                       | Description                                                    |
+================================+================================================================+
| in mat4 **MODEL_MATRIX**       | Local space to world space transform. World space              |
|                                | is the coordinates you normally use in the editor.             |
+--------------------------------+----------------------------------------------------------------+
| in mat4 **CANVAS_MATRIX**      | World space to canvas space transform. In canvas               |
|                                | space the origin is the upper-left corner of the               |
|                                | screen and coordinates ranging from ``(0.0, 0.0)``             |
|                                | to viewport size.                                              |
+--------------------------------+----------------------------------------------------------------+
| in mat4 **SCREEN_MATRIX**      | Canvas space to clip space. In clip space                      |
|                                | coordinates ranging from ``(-1.0, -1.0)`` to                   |
|                                | ``(1.0, 1.0).``                                                |
+--------------------------------+----------------------------------------------------------------+
| in int  **INSTANCE_ID**        | Instance ID for instancing.                                    |
+--------------------------------+----------------------------------------------------------------+
| in vec4 **INSTANCE_CUSTOM**    | Instance custom data.                                          |
+--------------------------------+----------------------------------------------------------------+
| in bool **AT_LIGHT_PASS**      | Always ``false``.                                              |
+--------------------------------+----------------------------------------------------------------+
| in vec2 **TEXTURE_PIXEL_SIZE** | Normalized pixel size of default 2D texture.                   |
|                                | For a Sprite2D with a texture of size 64x32px,                 |
|                                | **TEXTURE_PIXEL_SIZE** = ``vec2(1/64, 1/32)``                  |
+--------------------------------+----------------------------------------------------------------+
| inout vec2 **VERTEX**          | Vertex position, in local space.                               |
+--------------------------------+----------------------------------------------------------------+
| in int **VERTEX_ID**           | The index of the current vertex in the vertex                  |
|                                | buffer.                                                        |
+--------------------------------+----------------------------------------------------------------+
| inout vec2 **UV**              | Normalized texture coordinates. Range from ``0.0``             |
|                                | to ``1.0``.                                                    |
+--------------------------------+----------------------------------------------------------------+
| inout vec4 **COLOR**           | Color from vertex primitive multiplied by CanvasItem's         |
|                                | :ref:`modulate<class_CanvasItem_property_modulate>`            |
|                                | multiplied by CanvasItem's                                     |
|                                | :ref:`self_modulate<class_CanvasItem_property_self_modulate>`. |
+--------------------------------+----------------------------------------------------------------+
| inout float **POINT_SIZE**     | Point size for point drawing.                                  |
+--------------------------------+----------------------------------------------------------------+
| in vec4 **CUSTOM0**            | Custom value from vertex primitive.                            |
+--------------------------------+----------------------------------------------------------------+
| in vec4 **CUSTOM1**            | Custom value from vertex primitive.                            |
+--------------------------------+----------------------------------------------------------------+



Fragment built-ins
------------------

COLOR and TEXTURE
~~~~~~~~~~~~~~~~~

The built-in variable ``COLOR`` is used for a few things:

  - In the ``vertex()`` function, ``COLOR`` contains the color from the vertex
    primitive multiplied by the CanvasItem's
    :ref:`modulate<class_CanvasItem_property_modulate>` multiplied by the
    CanvasItem's :ref:`self_modulate<class_CanvasItem_property_self_modulate>`.
  - In the ``fragment()`` function, the input value ``COLOR`` is that same value
    multiplied by the color from the default ``TEXTURE`` (if present).
  - In the ``fragment()`` function, ``COLOR`` is also the final output.

Certain nodes (for example, :ref:`Sprite2D <class_Sprite2D>`) display a texture
by default, for example :ref:`texture <class_Sprite2D_property_texture>`. When
using a custom ``fragment()`` function, you have a few options on how to sample
this texture.

To read only the contents of the default texture, ignoring the vertex ``COLOR``:

.. code-block:: glsl

  void fragment() {
    COLOR = texture(TEXTURE, UV);
  }

To read the contents of the default texture multiplied by vertex ``COLOR``:

.. code-block:: glsl

  void fragment() {
    // Equivalent to an empty fragment() function, since COLOR is also the output variable.
    COLOR = COLOR;
  }

To read only the vertex ``COLOR`` in ``fragment()``, ignoring the main texture,
you must pass ``COLOR`` as a varying, then read it in ``fragment()``:

.. code-block:: glsl

  varying vec4 vertex_color;
  void vertex() {
    vertex_color = COLOR;
  }
  void fragment() {
    COLOR = vertex_color;
  }

NORMAL
~~~~~~

Similarly, if a normal map is used in the :ref:`CanvasTexture <class_CanvasTexture>`, Godot uses
it by default and assigns its value to the built-in ``NORMAL`` variable. If you are using a normal
map meant for use in 3D, it will appear inverted. In order to use it in your shader, you must assign
it to the ``NORMAL_MAP`` property. Godot will handle converting it for use in 2D and overwriting ``NORMAL``.

.. code-block:: glsl

  NORMAL_MAP = texture(NORMAL_TEXTURE, UV).rgb;

+---------------------------------------------+---------------------------------------------------------------+
| Built-in                                    | Description                                                   |
+=============================================+===============================================================+
| in vec4 **FRAGCOORD**                       | Coordinate of pixel center. In screen space. ``xy`` specifies |
|                                             | position in viewport. Upper-left of the viewport is the       |
|                                             | origin, ``(0.0, 0.0)``.                                       |
+---------------------------------------------+---------------------------------------------------------------+
| in vec2 **SCREEN_PIXEL_SIZE**               | Size of individual pixels. Equal to inverse of resolution.    |
+---------------------------------------------+---------------------------------------------------------------+
| in vec4 **REGION_RECT**                     | Visible area of the sprite region in format                   |
|                                             | ``(x, y, width, height)``. Varies according to                |
|                                             | Sprite2D's ``region_enabled`` property.                       |
+---------------------------------------------+---------------------------------------------------------------+
| in vec2 **POINT_COORD**                     | Coordinate for drawing points.                                |
+---------------------------------------------+---------------------------------------------------------------+
| sampler2D **TEXTURE**                       | Default 2D texture.                                           |
+---------------------------------------------+---------------------------------------------------------------+
| in vec2 **TEXTURE_PIXEL_SIZE**              | Normalized pixel size of default 2D texture.                  |
|                                             | For a Sprite2D with a texture of size 64x32px,                |
|                                             | ``TEXTURE_PIXEL_SIZE`` = ``vec2(1/64, 1/32)``                 |
+---------------------------------------------+---------------------------------------------------------------+
| in bool **AT_LIGHT_PASS**                   | Always ``false``.                                             |
+---------------------------------------------+---------------------------------------------------------------+
| sampler2D **SPECULAR_SHININESS_TEXTURE**    | Specular shininess texture of this object.                    |
+---------------------------------------------+---------------------------------------------------------------+
| in vec4 **SPECULAR_SHININESS**              | Specular shininess color, as sampled from the texture.        |
+---------------------------------------------+---------------------------------------------------------------+
| in vec2 **UV**                              | UV from the ``vertex()`` function.                            |
|                                             | For Sprite2D with region enabled, this will sample the entire |
|                                             | texture. Use ``REGION_RECT`` instead to sample only the       |
|                                             | region defined in the Sprite2D's properties.                  |
+---------------------------------------------+---------------------------------------------------------------+
| in vec2 **SCREEN_UV**                       | Screen UV coordinate for current pixel.                       |
+---------------------------------------------+---------------------------------------------------------------+
| sampler2D **SCREEN_TEXTURE**                | Removed in Godot 4. Use a ``sampler2D`` with                  |
|                                             | ``hint_screen_texture`` instead.                              |
+---------------------------------------------+---------------------------------------------------------------+
| inout vec3 **NORMAL**                       | Normal read from ``NORMAL_TEXTURE``. Writable.                |
+---------------------------------------------+---------------------------------------------------------------+
| sampler2D **NORMAL_TEXTURE**                | Default 2D normal texture.                                    |
+---------------------------------------------+---------------------------------------------------------------+
| out vec3 **NORMAL_MAP**                     | Configures normal maps meant for 3D for use in 2D. If used,   |
|                                             | overrides ``NORMAL``.                                         |
+---------------------------------------------+---------------------------------------------------------------+
| out float **NORMAL_MAP_DEPTH**              | Normal map depth for scaling.                                 |
+---------------------------------------------+---------------------------------------------------------------+
| inout vec2 **VERTEX**                       | Pixel position in screen space.                               |
+---------------------------------------------+---------------------------------------------------------------+
| inout vec2 **SHADOW_VERTEX**                | Same as ``VERTEX`` but can be written to alter shadows.       |
+---------------------------------------------+---------------------------------------------------------------+
| inout vec3 **LIGHT_VERTEX**                 | Same as ``VERTEX`` but can be written to alter lighting.      |
|                                             | Z component represents height.                                |
+---------------------------------------------+---------------------------------------------------------------+
| inout vec4 **COLOR**                        | ``COLOR`` from the ``vertex()`` function multiplied by the    |
|                                             | ``TEXTURE`` color. Also output color value.                   |
+---------------------------------------------+---------------------------------------------------------------+

Light built-ins
---------------

Light processor functions work differently in Godot 4.x than they did in Godot
3.x. In Godot 4.x all lighting is done during the regular draw pass. In other
words, Godot no longer draws the object again for each light.

Use the ``unshaded`` render mode if you do not want the ``light()`` function to
run. Use the ``light_only`` render mode if you only want to see the impact of
lighting on an object; this can be useful when you only want the object visible
where it is covered by light.

If you define a ``light()`` function it will replace the built-in light function,
even if your light function is empty.

Below is an example of a light shader that takes a CanvasItem's normal map into account:

.. code-block:: glsl

  void light() {
    float cNdotL = max(0.0, dot(NORMAL, LIGHT_DIRECTION));
    LIGHT = vec4(LIGHT_COLOR.rgb * COLOR.rgb * LIGHT_ENERGY * cNdotL, LIGHT_COLOR.a);
  }

+----------------------------------+------------------------------------------------------------------------------+
| Built-in                         | Description                                                                  |
+==================================+==============================================================================+
| in vec4 **FRAGCOORD**            | Coordinate of pixel center. In screen space. ``xy`` specifies                |
|                                  | position in viewport. Upper-left of the viewport is the origin,              |
|                                  | ``(0.0, 0.0)``.                                                              |
+----------------------------------+------------------------------------------------------------------------------+
| in vec3 **NORMAL**               | Input normal.                                                                |
+----------------------------------+------------------------------------------------------------------------------+
| in vec4 **COLOR**                | Input color. This is the output of the ``fragment()`` function.              |
+----------------------------------+------------------------------------------------------------------------------+
| in vec2 **UV**                   | UV from the ``vertex()`` function, equivalent to the UV in the               |
|                                  | ``fragment()`` function.                                                     |
+----------------------------------+------------------------------------------------------------------------------+
| sampler2D **TEXTURE**            | Current texture in use for CanvasItem.                                       |
+----------------------------------+------------------------------------------------------------------------------+
| in vec2 **TEXTURE_PIXEL_SIZE**   | Normalized pixel size of ``TEXTURE``.                                        |
|                                  | For a Sprite2D with a ``TEXTURE`` of size ``64x32`` pixels,                  |
|                                  | **TEXTURE_PIXEL_SIZE** = ``vec2(1/64, 1/32)``                                |
+----------------------------------+------------------------------------------------------------------------------+
| in vec2 **SCREEN_UV**            | Screen UV coordinate for current pixel.                                      |
+----------------------------------+------------------------------------------------------------------------------+
| in vec2 **POINT_COORD**          | UV for Point Sprite.                                                         |
+----------------------------------+------------------------------------------------------------------------------+
| in vec4 **LIGHT_COLOR**          | :ref:`Color<class_Light2D_property_color>` of the :ref:`class_Light2D`.      |
|                                  | If the light is a :ref:`class_PointLight2D`, multiplied by the light's       |
|                                  | :ref:`texture<class_PointLight2D_property_texture>`.                         |
+----------------------------------+------------------------------------------------------------------------------+
| in float **LIGHT_ENERGY**        | :ref:`Energy multiplier<class_Light2D_property_energy>` of the               |
|                                  | :ref:`class_Light2D`.                                                        |
+----------------------------------+------------------------------------------------------------------------------+
| in vec3 **LIGHT_POSITION**       | Position of the :ref:`class_Light2D` in screen space. If using a             |
|                                  | :ref:`class_DirectionalLight2D` this is always ``(0.0, 0.0, 0.0)``.          |
+----------------------------------+------------------------------------------------------------------------------+
| in vec3 **LIGHT_DIRECTION**      | Direction of the :ref:`class_Light2D` in screen space.                       |
+----------------------------------+------------------------------------------------------------------------------+
| in bool **LIGHT_IS_DIRECTIONAL** | ``true`` if this pass is a :ref:`class_DirectionalLight2D`.                  |
+----------------------------------+------------------------------------------------------------------------------+
| in vec3 **LIGHT_VERTEX**         | Pixel position, in screen space as modified in the ``fragment()`` function.  |
+----------------------------------+------------------------------------------------------------------------------+
| inout vec4 **LIGHT**             | Output color for this :ref:`class_Light2D`.                                  |
+----------------------------------+------------------------------------------------------------------------------+
| in vec4 **SPECULAR_SHININESS**   | Specular shininess, as set in the object's texture.                          |
+----------------------------------+------------------------------------------------------------------------------+
| out vec4 **SHADOW_MODULATE**     | Multiply shadows cast at this point by this color.                           |
+----------------------------------+------------------------------------------------------------------------------+

SDF functions
-------------

There are a few additional functions implemented to sample an automatically
generated Signed Distance Field texture. These functions available for the ``fragment()``
and ``light()`` functions of CanvasItem shaders. Custom functions may also use them as long
as they called from supported functions.

The signed distance field is generated from :ref:`class_LightOccluder2D` nodes
present in the scene with the **SDF Collision** property enabled (which is the
default). See the :ref:`2D lights and shadows <doc_2d_lights_and_shadows_setting_up_shadows>`
documentation for more information.

+-----------------------------------------------+-------------------------------------------+
| Function                                      | Description                               |
+===============================================+===========================================+
| float **texture_sdf** (vec2 sdf_pos)          | Performs an SDF texture lookup.           |
+-----------------------------------------------+-------------------------------------------+
| vec2 **texture_sdf_normal** (vec2 sdf_pos)    | Calculates a normal from the SDF texture. |
+-----------------------------------------------+-------------------------------------------+
| vec2 **sdf_to_screen_uv** (vec2 sdf_pos)      | Converts an SDF to screen UV.             |
+-----------------------------------------------+-------------------------------------------+
| vec2 **screen_uv_to_sdf** (vec2 uv)           | Converts screen UV to an SDF.             |
+-----------------------------------------------+-------------------------------------------+
