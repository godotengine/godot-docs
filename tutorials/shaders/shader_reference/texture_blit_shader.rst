.. _doc_texture_blit_shader:

TextureBlit shaders
==================

TextureBlit shaders are used to define the behavior of Blit calls on a DrawableTexture2D

TextureBlit shaders only have one processing function, the ``blit()`` function, 
which runs for every pixel of the source texture inside the rect given to ``blit_rect()``

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
| **blend_disabled**              | Disable blending, values (including alpha) are written as-is.        |
+---------------------------------+----------------------------------------------------------------------+

Built-ins
---------

Values marked as ``in`` are read-only. Values marked as ``out`` can optionally be written to and will
not necessarily contain sensible values. Values marked as ``inout`` provide a sensible default
value, and can optionally be written to. Samplers cannot be written to so they are not marked.

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


Blit built-ins
------------------

Source Textures
~~~~~~~~~~~~~~~~~
TextureBlit Shaders have up to 4 Source Textures bound as inputs.
These can be accessed with a ``sampler2D`` 
using ``hint_blit_source0``, ``hint_blit_source1``, ``hint_blit_source2``, and ``hint_blit_source3``.

+---------------------------------------------+---------------------------------------------------------------+
| Built-in                                    | Description                                                   |
+=============================================+===============================================================+
| in vec4 **FRAGCOORD**                       | Coordinate of pixel center. In screen space. ``xy`` specifies |
|                                             | position in viewport. Upper-left of the viewport is the       |
|                                             | origin, ``(0.0, 0.0)``.                                       |
+---------------------------------------------+---------------------------------------------------------------+
| in vec2 **UV**                              | UV from the ``vertex()`` function.                            |
|                                             | This is set to sample all of a source texture.                |
+---------------------------------------------+---------------------------------------------------------------+
| in vec4 **MODULATE**                        | ``MODULATE`` color passed in by RenderingServer API           |
+---------------------------------------------+---------------------------------------------------------------+
| out vec4 **COLOR0**                         | Output Color to blended with the DrawableTexture target.      |
|                                             | Initialized to (0.0, 0.0, 0.0, 0.0)                           |
+---------------------------------------------+---------------------------------------------------------------+
| out vec4 **COLOR1**                         | Output Color to blended with an extra DrawableTexture target. |
|                                             | Initialized to (0.0, 0.0, 0.0, 0.0)                           |
+---------------------------------------------+---------------------------------------------------------------+
| out vec4 **COLOR2**                         | Output Color to blended with an extra DrawableTexture target. |
|                                             | Initialized to (0.0, 0.0, 0.0, 0.0)                           |
+---------------------------------------------+---------------------------------------------------------------+
| out vec4 **COLOR3**                         | Output Color to blended with an extra DrawableTexture target. |
|                                             | Initialized to (0.0, 0.0, 0.0, 0.0)                           |
+---------------------------------------------+---------------------------------------------------------------+

