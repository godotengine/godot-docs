.. _doc_sky_shader:

Sky shaders
===========

Sky shaders are a special type of shader used for drawing sky backgrounds
and for updating radiance cubemaps which are used for image-based lighting
(IBL). Sky shaders only have one processing function, the ``sky()``
function.

There are three places the sky shader is used.

* First the sky shader is used to draw the sky when you have selected to use
  a Sky as the background in your scene.
* Second, the sky shader is used to update the radiance cubemap
  when using the Sky for ambient color or reflections.
* Third, the sky shader is used to draw the lower res subpasses which can be
  used in the high-res background or cubemap pass.

In total, this means the sky shader can run up
to six times per frame, however, in practice it will be much less than that
because the radiance cubemap does not need to be updated every frame, and
not all subpasses will be used. You can change the behavior of the shader
based on where it is called by checking the ``AT_*_PASS`` booleans. For
example:

.. code-block:: glsl

    shader_type sky;

    void sky() {
        if (AT_CUBEMAP_PASS) {
            // Sets the radiance cubemap to a nice shade of blue instead of doing
            // expensive sky calculations
            COLOR = vec3(0.2, 0.6, 1.0);
        } else {
            // Do expensive sky calculations for background sky only
            COLOR = get_sky_color(EYEDIR);
        }
    }


When using the sky shader to draw a background, the shader will be called for
all non-occluded fragments on the screen. However, for the background's
subpasses, the shader will be called for every pixel of the subpass.

When using the sky shader to update the radiance cubemap, the sky shader
will be called for every pixel in the cubemap. On the other hand, the shader
will only be called when the radiance cubemap needs to be updated. The radiance
cubemap needs to be updated when any of the shader parameters are updated.
For example, if ``TIME`` is used in the shader, then the radiance cubemap
will update every frame. The following list of changes force an update of
the radiance cubemap:

* ``TIME`` is used.
* ``POSITION`` is used and the camera position changes.
* If any ``LIGHTX_*`` properties are used and any
  :ref:`DirectionalLight3D <class_DirectionalLight3D>` changes.
* If any uniform is changed in the shader.
* If the screen is resized and either of the subpasses are used.

Try to avoid updating the radiance cubemap needlessly. If you do need to
update the radiance cubemap each frame, make sure your
:ref:`Sky process mode <class_Sky_property_process_mode>` is set to
:ref:`REALTIME <class_Sky_constant_PROCESS_MODE_REALTIME>`.

Note that the :ref:`process mode <class_Sky_property_process_mode>` only
affects the rendering of the radiance cubemap. The visible sky is always
rendered by calling the fragment shader for every pixel. With complex fragment
shaders, this can result in a high rendering overhead. If the sky is static
(the conditions listed above are met) or changes slowly, running the full
fragment shader every frame is not needed. This can be avoided by rendering the
full sky into the radiance cubemap, and reading from this cubemap when
rendering the visible sky. With a completely static sky, this means that it
needs to be rendered only once.

The following code renders the full sky into the radiance cubemap and reads
from that cubemap for displaying the visible sky:

.. code-block:: glsl

    shader_type sky;

    void sky() {
        if (AT_CUBEMAP_PASS) {
            vec3 dir = EYEDIR;

            vec4 col = vec4(0.0);

            // Complex color calculation

            COLOR = col.xyz;
            ALPHA = 1.0;
        } else {
            COLOR = texture(RADIANCE, EYEDIR).rgb;
        }
    }

This way, the complex calculations happen only in the cubemap pass, which can
be optimized by setting the sky's :ref:`process mode <class_Sky_property_process_mode>`
and the :ref:`radiance size <class_Sky_property_radiance_size>` to get the
desired balance between performance and visual fidelity.

Render modes
^^^^^^^^^^^^

Subpasses allow you to do more expensive calculations at a lower resolution
to speed up your shaders. For example the following code renders clouds at
a lower resolution than the rest of the sky:

.. code-block:: glsl

    shader_type sky;
    render_mode use_half_res_pass;

    void sky() {
        if (AT_HALF_RES_PASS) {
            // Run cloud calculation for 1/4 of the pixels
            vec4 color = generate_clouds(EYEDIR);
            COLOR = color.rgb;
            ALPHA = color.a;
        } else {
            // At full resolution pass, blend sky and clouds together
            vec3 color = generate_sky(EYEDIR);
            COLOR = color + HALF_RES_COLOR.rgb * HALF_RES_COLOR.a;
        }
    }

+--------------------------+-----------------------------------------------------------------------+
| Render mode              | Description                                                           |
+==========================+=======================================================================+
| **use_half_res_pass**    | Allows the shader to write to and access the half resolution pass.    |
+--------------------------+-----------------------------------------------------------------------+
| **use_quarter_res_pass** | Allows the shader to write to and access the quarter resolution pass. |
+--------------------------+-----------------------------------------------------------------------+
| **disable_fog**          | If used, fog will not affect the sky.                                 |
+--------------------------+-----------------------------------------------------------------------+

Built-ins
^^^^^^^^^

Values marked as "in" are read-only. Values marked as "out" are for optional
writing and will not necessarily contain sensible values. Samplers cannot be
written to so they are not marked.

Global built-ins
^^^^^^^^^^^^^^^^

Global built-ins are available everywhere, including in custom functions.

There are 4 ``LIGHTX`` lights, accessed as ``LIGHT0``, ``LIGHT1``, ``LIGHT2``, and ``LIGHT3``.


+---------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Built-in                        | Description                                                                                                              |
+=================================+==========================================================================================================================+
| in float **TIME**               | Global time, in seconds.                                                                                                 |
+---------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| in vec3 **POSITION**            | Camera position in world space                                                                                           |
+---------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| samplerCube **RADIANCE**        | Radiance cubemap. Can only be read from during background pass. Check ``!AT_CUBEMAP_PASS`` before using.                 |
+---------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| in bool **AT_HALF_RES_PASS**    | Currently rendering to half resolution pass.                                                                             |
+---------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| in bool **AT_QUARTER_RES_PASS** | Currently rendering to quarter resolution pass.                                                                          |
+---------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| in bool **AT_CUBEMAP_PASS**     | Currently rendering to radiance cubemap.                                                                                 |
+---------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| in bool **LIGHTX_ENABLED**      | ``LightX`` is visible and in the scene. If ``false``, other light properties may be garbage.                             |
+---------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| in float **LIGHTX_ENERGY**      | Energy multiplier for ``LIGHTX``.                                                                                        |
+---------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| in vec3 **LIGHTX_DIRECTION**    | Direction that ``LIGHTX`` is facing.                                                                                     |
+---------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| in vec3 **LIGHTX_COLOR**        | Color of ``LIGHTX``.                                                                                                     |
+---------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| in float **LIGHTX_SIZE**        | Angular diameter of ``LIGHTX`` in the sky. Expressed in radians. For reference, the sun from earth is about .0087 radians|
|                                 | (0.5 degrees).                                                                                                           |
+---------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| in float **PI**                 | A ``PI`` constant (``3.141592``).                                                                                        |
|                                 | A ratio of a circle's circumference to its diameter and amount of radians in half turn.                                  |
+---------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| in float **TAU**                | A ``TAU`` constant (``6.283185``).                                                                                       |
|                                 | An equivalent of ``PI * 2`` and amount of radians in full turn.                                                          |
+---------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| in float **E**                  | A ``E`` constant (``2.718281``).                                                                                         |
|                                 | Euler's number and a base of the natural logarithm.                                                                      |
+---------------------------------+--------------------------------------------------------------------------------------------------------------------------+

Sky built-ins
^^^^^^^^^^^^^

+-------------------------------+-------------------------------------------------------------------------------------------------+
| Built-in                      | Description                                                                                     |
+===============================+=================================================================================================+
| in vec3 **EYEDIR**            | Normalized direction of current pixel. Use this as your basic direction for procedural effects. |
+-------------------------------+-------------------------------------------------------------------------------------------------+
| in vec2 **SCREEN_UV**         | Screen UV coordinate for current pixel. Used to map a texture to the full screen.               |
+-------------------------------+-------------------------------------------------------------------------------------------------+
| in vec2 **SKY_COORDS**        | Sphere UV. Used to map a panorama texture to the sky.                                           |
+-------------------------------+-------------------------------------------------------------------------------------------------+
| in vec4 **HALF_RES_COLOR**    | Color value of corresponding pixel from half resolution pass. Uses linear filter.               |
+-------------------------------+-------------------------------------------------------------------------------------------------+
| in vec4 **QUARTER_RES_COLOR** | Color value of corresponding pixel from quarter resolution pass. Uses linear filter.            |
+-------------------------------+-------------------------------------------------------------------------------------------------+
| out vec3 **COLOR**            | Output color.                                                                                   |
+-------------------------------+-------------------------------------------------------------------------------------------------+
| out float **ALPHA**           | Output alpha value, can only be used in subpasses.                                              |
+-------------------------------+-------------------------------------------------------------------------------------------------+
| out vec4 **FOG**              |                                                                                                 |
+-------------------------------+-------------------------------------------------------------------------------------------------+
