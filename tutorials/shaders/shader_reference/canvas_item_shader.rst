.. _doc_canvas_item_shader:

CanvasItem shaders
==================

CanvasItem shaders are used to draw all 2D elements in Godot. These include
all nodes that inherit from CanvasItems, and all GUI elements.

CanvasItem shaders contain less built-in variables and functionality than Spatial
shaders, but they maintain the same basic structure with vertex, fragment, and
light processor functions.

Render modes
^^^^^^^^^^^^

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
| **skip_vertex_transform**       | VERTEX needs to be transformed manually in vertex function.          |
+---------------------------------+----------------------------------------------------------------------+
| **world_vertex_coords**         | VERTEX is modified in world coordinates instead of local.            |
+---------------------------------+----------------------------------------------------------------------+

Built-ins
^^^^^^^^^

Values marked as "in" are read-only. Values marked as "out" are for optional writing and will
not necessarily contain sensible values. Values marked as "inout" provide a sensible default
value, and can optionally be written to. Samplers are not subjects of writing and they are
not marked.

Global built-ins
^^^^^^^^^^^^^^^^

Global built-ins are available everywhere, including custom functions.

+-------------------+----------------------------------------------------------------------------------------+
| Built-in          | Description                                                                            |
+===================+========================================================================================+
| in float **TIME** | Global time since the engine has started, in seconds (always positive).                |
|                   | It's subject to the rollover setting (which is 3,600 seconds by default).              |
|                   | It's not affected by :ref:`time_scale<class_Engine_property_time_scale>`               |
|                   | or pausing, but you can define a global shader uniform to add a "scaled"               |
|                   | ``TIME`` variable if desired.                                                          |
+-------------------+----------------------------------------------------------------------------------------+
| in float **PI**   | A ``PI`` constant (``3.141592``).                                                      |
|                   | A ration of circle's circumference to its diameter and amount of radians in half turn. |
+-------------------+----------------------------------------------------------------------------------------+
| in float **TAU**  | A ``TAU`` constant (``6.283185``).                                                     |
|                   | An equivalent of ``PI * 2`` and amount of radians in full turn.                        |
+-------------------+----------------------------------------------------------------------------------------+
| in float **E**    | A ``E`` constant (``2.718281``).                                                       |
|                   | Euler's number and a base of the natural logarithm.                                    |
+-------------------+----------------------------------------------------------------------------------------+

Vertex built-ins
^^^^^^^^^^^^^^^^

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

Other built-ins, such as UV and COLOR, are also passed through to the fragment function if not modified.

For instancing, the INSTANCE_CUSTOM variable contains the instance custom data. When using particles, this information
is usually:

* **x**: Rotation angle in radians.
* **y**: Phase during lifetime (0 to 1).
* **z**: Animation frame.

+--------------------------------+----------------------------------------------------+
| Built-in                       | Description                                        |
+================================+====================================================+
| in mat4 **MODEL_MATRIX**       | Local space to world space transform. World space  |
|                                | is the coordinates you normally use in the editor. |
+--------------------------------+----------------------------------------------------+
| in mat4 **CANVAS_MATRIX**      | World space to canvas space transform. In canvas   |
|                                | space the origin is the upper-left corner of the   |
|                                | screen and coordinates ranging from (0, 0) to      |
|                                | viewport size.                                     |
+--------------------------------+----------------------------------------------------+
| in mat4 **SCREEN_MATRIX**      | Canvas space to clip space. In clip space          |
|                                | coordinates ranging from (-1, -1) to (1, 1).       |
+--------------------------------+----------------------------------------------------+
| in int  **INSTANCE_ID**        | Instance ID for instancing.                        |
+--------------------------------+----------------------------------------------------+
| in vec4 **INSTANCE_CUSTOM**    | Instance custom data.                              |
+--------------------------------+----------------------------------------------------+
| in bool **AT_LIGHT_PASS**      | Always ``false``.                                  |
+--------------------------------+----------------------------------------------------+
| in vec2 **TEXTURE_PIXEL_SIZE** | Normalized pixel size of default 2D texture.       |
|                                | For a Sprite2D with a texture of size 64x32px,     |
|                                | **TEXTURE_PIXEL_SIZE** = ``vec2(1/64, 1/32)``      |
+--------------------------------+----------------------------------------------------+
| inout vec2 **VERTEX**          | Vertex, in local space.                            |
+--------------------------------+----------------------------------------------------+
| in int **VERTEX_ID**           | The index of the current vertex in the vertex      |
|                                | buffer.                                            |
+--------------------------------+----------------------------------------------------+
| inout vec2 **UV**              | Normalized texture coordinates. Range from 0 to 1. |
+--------------------------------+----------------------------------------------------+
| inout vec4 **COLOR**           | Color from vertex primitive.                       |
+--------------------------------+----------------------------------------------------+
| inout float **POINT_SIZE**     | Point size for point drawing.                      |
+--------------------------------+----------------------------------------------------+

Fragment built-ins
^^^^^^^^^^^^^^^^^^

Certain Nodes (for example, :ref:`Sprite2Ds <class_Sprite2D>`) display a texture
by default. However, when a custom fragment function is attached to these nodes,
the texture lookup needs to be done manually. Godot provides the texture color
in the ``COLOR`` built-in variable multiplied by the node's color. To read the
texture color by itself, you can use:

.. code-block:: glsl

  COLOR = texture(TEXTURE, UV);

Similarly, if a normal map is used in the :ref:`CanvasTexture <class_CanvasTexture>`, Godot uses
it by default and assigns its value to the built-in ``NORMAL`` variable. If you are using a normal
map meant for use in 3D, it will appear inverted. In order to use it in your shader, you must assign
it to the ``NORMALMAP`` property. Godot will handle converting it for use in 2D and overwriting ``NORMAL``.

.. code-block:: glsl

  NORMALMAP = texture(NORMAL_TEXTURE, UV).rgb;

+---------------------------------------------+---------------------------------------------------------------+
| Built-in                                    | Description                                                   |
+=============================================+===============================================================+
| in vec4 **FRAGCOORD**                       | Coordinate of pixel center. In screen space. ``xy`` specifies |
|                                             | position in window. Origin is upper-left.                     |
+---------------------------------------------+---------------------------------------------------------------+
| in vec2 **SCREEN_PIXEL_SIZE**               | Size of individual pixels. Equal to inverse of resolution.    |
+---------------------------------------------+---------------------------------------------------------------+
| in vec2 **POINT_COORD**                     | Coordinate for drawing points.                                |
+---------------------------------------------+---------------------------------------------------------------+
| sampler2D **TEXTURE**                       | Default 2D texture.                                           |
+---------------------------------------------+---------------------------------------------------------------+
| in vec2 **TEXTURE_PIXEL_SIZE**              | Normalized pixel size of default 2D texture.                  |
|                                             | For a Sprite2D with a texture of size 64x32px,                |
|                                             | **TEXTURE_PIXEL_SIZE** = ``vec2(1/64, 1/32)``                 |
+---------------------------------------------+---------------------------------------------------------------+
| in bool **AT_LIGHT_PASS**                   | Always ``false``.                                             |
+---------------------------------------------+---------------------------------------------------------------+
| sampler2D **SPECULAR_SHININESS_TEXTURE**    | Specular shininess texture of this object.                    |
+---------------------------------------------+---------------------------------------------------------------+
| in vec4 **SPECULAR_SHININESS**              | Specular shininess color, as sampled from the texture.        |
+---------------------------------------------+---------------------------------------------------------------+
| in vec2 **UV**                              | UV from vertex function.                                      |
+---------------------------------------------+---------------------------------------------------------------+
| in vec2 **SCREEN_UV**                       | Screen UV coordinate for current pixel.                       |
+---------------------------------------------+---------------------------------------------------------------+
| sampler2D **SCREEN_TEXTURE**                | Removed in Godot 4. Use a ``sampler2D`` with                  |
|                                             | ``hint_screen_texture`` instead.                              |
+---------------------------------------------+---------------------------------------------------------------+
| inout vec3 **NORMAL**                       | Normal read from **NORMAL_TEXTURE**. Writable.                |
+---------------------------------------------+---------------------------------------------------------------+
| sampler2D **NORMAL_TEXTURE**                | Default 2D normal texture.                                    |
+---------------------------------------------+---------------------------------------------------------------+
| out vec3 **NORMAL_MAP**                     | Configures normal maps meant for 3D for use in 2D. If used,   |
|                                             | overrides **NORMAL**.                                         |
+---------------------------------------------+---------------------------------------------------------------+
| out float **NORMAL_MAP_DEPTH**              | Normalmap depth for scaling.                                  |
+---------------------------------------------+---------------------------------------------------------------+
| inout vec2 **VERTEX**                       | Pixel position in screen space.                               |
+---------------------------------------------+---------------------------------------------------------------+
| inout vec2 **SHADOW_VERTEX**                | Same as ``VERTEX`` but can be written to alter shadows.       |
+---------------------------------------------+---------------------------------------------------------------+
| inout vec3 **LIGHT_VERTEX**                 | Same as ``VERTEX`` but can be written to alter lighting.      |
|                                             | Z component represents height.                                |
+---------------------------------------------+---------------------------------------------------------------+
| inout vec4 **COLOR**                        | Color from vertex function multiplied by the **TEXTURE**      |
|                                             | color. Also output color value.                               |
+---------------------------------------------+---------------------------------------------------------------+

Light built-ins
^^^^^^^^^^^^^^^

Light processor functions work differently in Godot 4.x than they did in Godot
3.x. In Godot 4.x all lighting is done during the regular draw pass. In other
words, Godot no longer draws the object again for each light.

Use render_mode ``unshaded`` if you do not want the light processor function to
run. Use render_mode ``light_only`` if you only want to see the impact of
lighting on an object; this can be useful when you only want the object visible
where it is covered by light. 

If you define a light function it will replace the built in light function,
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
|                                  | position in window. Origin is lower-left.                                    |
+----------------------------------+------------------------------------------------------------------------------+
| in vec3 **NORMAL**               | Input Normal.                                                                |
+----------------------------------+------------------------------------------------------------------------------+
| in vec4 **COLOR**                | Input Color. This is the output of the fragment function.                    |
+----------------------------------+------------------------------------------------------------------------------+
| in vec2 **UV**                   | UV from vertex function, equivalent to the UV in the fragment function.      |
+----------------------------------+------------------------------------------------------------------------------+
| sampler2D **TEXTURE**            | Current texture in use for CanvasItem.                                       |
+----------------------------------+------------------------------------------------------------------------------+
| in vec2 **TEXTURE_PIXEL_SIZE**   | Normalized pixel size of **TEXTURE**.                                        |
|                                  | For a Sprite2D with a **TEXTURE** of size 64x32px,                           |
|                                  | **TEXTURE_PIXEL_SIZE** = ``vec2(1/64, 1/32)``                                |
+----------------------------------+------------------------------------------------------------------------------+
| in vec2 **SCREEN_UV**            | Screen UV coordinate for current pixel.                                      |
+----------------------------------+------------------------------------------------------------------------------+
| in vec2 **POINT_COORD**          | UV for Point Sprite.                                                         |
+----------------------------------+------------------------------------------------------------------------------+
| in vec4 **LIGHT_COLOR**          | Color of Light multiplied by Light's texture.                                |
+----------------------------------+------------------------------------------------------------------------------+
| in float **LIGHT_ENERGY**        | Energy multiplier of Light.                                                  |
+----------------------------------+------------------------------------------------------------------------------+
| in vec3 **LIGHT_POSITION**       | Position of Light in screen space. If using a ``DirectionalLight2D``         |
|                                  | this is always ``vec3(0,0,0)``.                                              |
+----------------------------------+------------------------------------------------------------------------------+
| in vec3 **LIGHT_DIRECTION**      | Direction of Light in screen space.                                          |
+----------------------------------+------------------------------------------------------------------------------+
| in bool **LIGHT_IS_DIRECTIONAL** | ``true`` if this pass is a ``DirectionalLight2D``.                           |
+----------------------------------+------------------------------------------------------------------------------+
| in vec3 **LIGHT_VERTEX**         | Pixel position, in screen space as modified in the fragment function.        |
+----------------------------------+------------------------------------------------------------------------------+
| inout vec4 **LIGHT**             | Output color for this Light.                                                 |
+----------------------------------+------------------------------------------------------------------------------+
| in vec4 **SPECULAR_SHININESS**   | Specular shininess, as set in the object's texture.                          |
+----------------------------------+------------------------------------------------------------------------------+
| out vec4 **SHADOW_MODULATE**     | Multiply shadows cast at this point by this color.                           |
+----------------------------------+------------------------------------------------------------------------------+

SDF functions
^^^^^^^^^^^^^

There are a few additional functions implemented to sample an automatically
generated Signed Distance Field texture. These functions available for Fragment
and Light functions of CanvasItem shaders.

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
| vec2 **sdf_to_screen_uv** (vec2 sdf_pos)      | Converts a SDF to screen UV.              |
+-----------------------------------------------+-------------------------------------------+
| vec2 **screen_uv_to_sdf** (vec2 uv)           | Converts screen UV to a SDF.              |
+-----------------------------------------------+-------------------------------------------+
