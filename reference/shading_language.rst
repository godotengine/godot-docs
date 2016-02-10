.. _doc_shading_language:

Shading Language
================

Introduction
------------

Godot uses a simplified shader language (almost a subset of GLSL).
Shaders can be used for:

-  Materials
-  Post-Processing
-  2D

and are divided in *Vertex*, *Fragment* and *Light* sections.

Language
--------

Typing
~~~~~~

The language is statically type and supports only a few operations.
Arrays, classes, structures, etc are not supported. Several built-in
datatypes are provided:

Data Types
~~~~~~~~~~

+-------------------+--------------------------------------------------------------+
| DataType          | Description                                                  |
+===================+==============================================================+
| *void*            | Void                                                         |
+-------------------+--------------------------------------------------------------+
| *bool*            | boolean (true or false)                                      |
+-------------------+--------------------------------------------------------------+
| *float*           | floating point                                               |
+-------------------+--------------------------------------------------------------+
| *vec2*            | 2-component vector, float subindices (x,y or r,g )           |
+-------------------+--------------------------------------------------------------+
| *vec3*            | 3-component vector, float subindices (x,y,z or r,g,b )       |
+-------------------+--------------------------------------------------------------+
| *vec4*, *color*   | 4-component vector, float subindices (x,y,z,w or r,g,b,a )   |
+-------------------+--------------------------------------------------------------+
| *mat2*            | 2x2 matrix, vec3 subindices (x,y)                            |
+-------------------+--------------------------------------------------------------+
| *mat3*            | 3x3 matrix, vec3 subindices (x,y,z)                          |
+-------------------+--------------------------------------------------------------+
| *mat4*            | 4x4 matrix, vec4 subindices (x,y,z,w)                        |
+-------------------+--------------------------------------------------------------+
| *texture*         | texture sampler, can only be used as uniform                 |
+-------------------+--------------------------------------------------------------+
| *cubemap*         | cubemap sampler, can only be used as uniform                 |
+-------------------+--------------------------------------------------------------+

Syntax
~~~~~~

| The syntax is similar to C, with statements ending in ; , and comments
  as // and /\* \*/.
| Example:

::

    float a = 3;
    vec3 b;
    b.x = a;

Swizzling
~~~~~~~~~

It is possible to use swizzling to reasigning subindices or groups of
subindices, in order:

::

    vec3 a = vec3(1,2,3);
    vec3 b = a.zyx; // b will contain vec3(3,2,1)
    vec2 c = a.xy; // c will contain vec2(1,2)
    vec4 d = a.xyzz; // d will contain vec4(1,2,3,3)

Constructors
~~~~~~~~~~~~

Constructors take the regular amount of elements, but can also accept
less if the element has more subindices, for example:

::

    vec3 a = vec3( 1, vec2(2,3) );
    vec3 b = vec3( a );
    vec3 c = vec3( vec2(2,3), 1 );
    vec4 d = vec4( a, 5 );
    mat3 m = mat3( a,b,c );

Conditionals
~~~~~~~~~~~~

For now, only the "if" conditional is supported. Example:

::

    if (a < b) {
       c = b;
    }

Uniforms
~~~~~~~~

A variable can be declared as uniform. In this case, it's value will
come from outside the shader (it will be the responsibility of the
material or whatever using the shader to provide it).

::

    uniform vec3 direction;
    uniform color tint;

    vec3 result = tint.rgb * direction;

Functions
~~~~~~~~~

Simple support for functions is provided. Functions can't access
uniforms or other shader variables.

::

    vec3 addtwo( vec3 a, vec3 b) {

        return a+b;
    }

    vec3 c = addtwo(vec3(1,1,1)+vec3(2,2,2));

Built-In Functions
------------------

Several Built-in functions are provided for convenience, listed as
follows:

| \|\ *. Function \|*. Description \|
| \| float *sin*\ ( float ) \| Sine \|
| \| float *cos*\ ( float ) \| Cosine \|
| \| float *tan*\ ( float ) \| Tangent \|
| \| float *asin*\ ( float ) \| arc-Sine \|
| \| float *acos*\ ( float ) \| arc-Cosine \|
| \| float *atan*\ ( float ) \| arc-Tangent \|
| \| vec_type *pow*\ ( vec_type, float ) \| Power \|
| \| vec_type *pow*\ ( vec_type, vec_type ) \| Power (Vec. Exponent)
  \|
| \| vec_type *exp*\ ( vec_type ) \| Base-e Exponential \|
| \| vec_type *log*\ ( vec_type ) \| Natural Logarithm \|
| \| vec_type *sqrt*\ ( vec_type ) \| Square Root \|
| \| vec_type *abs*\ ( vec_type ) \| Absolute \|
| \| vec_type *sign*\ ( vec_type ) \| Sign \|
| \| vec_type *floor*\ ( vec_type ) \| Floor \|
| \| vec_type *trunc*\ ( vec_type ) \| Trunc \|
| \| vec_type *ceil*\ ( vec_type ) \| Ceiling \|
| \| vec_type *fract*\ ( vec_type ) \| Fractional \|
| \| vec_type *mod*\ ( vec_type,vec_type ) \| Remainder \|
| \| vec_type *min*\ ( vec_type,vec_type ) \| Minimum \|
| \| vec_type *min*\ ( vec_type,vec_type ) \| Maximum \|
| \| vec_type *clamp*\ ( vec_type value,vec_type min, vec_type max )
  \| Clamp to Min-Max \|
| \| vec_type *mix*\ ( vec_type a,vec_type b, float c ) \| Linear
  Interpolate \|
| \| vec_type *mix*\ ( vec_type a,vec_type b, vec_type c ) \| Linear
  Interpolate (Vector Coef.)\|
| \| vec_type *step*\ ( vec_type a,vec_type b) \| \` a[i] < b[i] ?
  0.0 : 1.0\`\|
| \| vec_type *smoothstep*\ ( vec_type a,vec_type b,vec_type c) \|
  \|
| \| float *length*\ ( vec_type ) \| Vector Length \|
| \| float *distance*\ ( vec_type, vec_type ) \| Distance between
  vector. \|
| \| float *dot*\ ( vec_type, vec_type ) \| Dot Product \|
| \| vec3 *dot*\ ( vec3, vec3 ) \| Cross Product \|
| \| vec_type *normalize*\ ( vec_type ) \| Normalize to unit length \|
| \| vec3 *reflect*\ ( vec3, vec3 ) \| Reflect \|
| \| color *tex*\ ( texture, vec2 ) \| Read from a texture in
  noormalized coords \|
| \| color *texcube*\ ( texture, vec3 ) \| Read from a cubemap \|
| \| color *texscreen*\ ( vec2 ) \| Read from screen (generates a copy)
  \|

Built-In Variables
------------------

Depending on the shader type, several built-in variables are available,
listed as follows:

Material - VertexShader
~~~~~~~~~~~~~~~~~~~~~~~

| \|\ *. Variable \|*. Description \|
| \| const vec3 *SRC_VERTEX* \| Model-Space Vertex \|
| \| const vec3 *SRC_NORMAL* \| Model-Space Normal \|
| \| const vec3 *SRC_TANGENT* \| Model-Space Tangent \|
| \| const float *SRC_BINORMALF* \| Direction to Compute Binormal \|
| \| vec3 *VERTEX* \| View-Space Vertex \|
| \| vec3 *NORMAL* \| View-Space Normal \|
| \| vec3 *TANGENT* \| View-Space Tangent \|
| \| vec3 *BINORMAL* \| View-Space Binormal \|
| \| vec2 *UV* \| UV \|
| \| vec2 *UV2* \| UV2 \|
| \| color *COLOR* \| Vertex Color \|
| \| out vec4 *VAR1* \| Varying 1 Output \|
| \| out vec4 *VAR2* \| Varying 2 Output \|
| \| out float *SPEC_EXP* \| Specular Exponent (for Vertex Lighting) \|
| \| out float *POINT_SIZE* \| Point Size (for points) \|
| \| const mat4 *WORLD_MATRIX* \| Object World Matrix \|
| \| const mat4 *INV_CAMERA_MATRIX* \| Inverse Camera Matrix \|
| \| const mat4 *PROJECTION_MATRIX* \| Projection Matrix \|
| \| const mat4 *MODELVIEW_MATRIX* \| (InvCamera \* Projection) \|
| \| const float *INSTANCE_ID* \| Instance ID (for multimesh)\|
| \| const float *TIME* \| Time (in seconds) \|

Material - FragmentShader
~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------+----------------------------------------------------------------------------------+
| Variable                         | Description                                                                      |
+==================================+==================================================================================+
| const vec3 *VERTEX*              | View-Space vertex                                                                |
+----------------------------------+----------------------------------------------------------------------------------+
| const vec4 *POSITION*            | View-Space Position                                                              |
+----------------------------------+----------------------------------------------------------------------------------+
| const vec3 *NORMAL*              | View-Space Normal                                                                |
+----------------------------------+----------------------------------------------------------------------------------+
| const vec3 *TANGENT*             | View-Space Tangent                                                               |
+----------------------------------+----------------------------------------------------------------------------------+
| const vec3 *BINORMAL*            | View-Space Binormal                                                              |
+----------------------------------+----------------------------------------------------------------------------------+
| const vec3 *NORMALMAP*           | Alternative to NORMAL, use for normal texture output.                            |
+----------------------------------+----------------------------------------------------------------------------------+
| const vec3 *NORMALMAP_DEPTH*     | Complementary to the above, allows changing depth of normalmap.                  |
+----------------------------------+----------------------------------------------------------------------------------+
| const vec2 *UV*                  | UV                                                                               |
+----------------------------------+----------------------------------------------------------------------------------+
| const vec2 *UV2*                 | UV2                                                                              |
+----------------------------------+----------------------------------------------------------------------------------+
| const color *COLOR*              | Vertex Color                                                                     |
+----------------------------------+----------------------------------------------------------------------------------+
| const vec4 *VAR1*                | Varying 1                                                                        |
+----------------------------------+----------------------------------------------------------------------------------+
| const vec4 *VAR2*                | Varying 2                                                                        |
+----------------------------------+----------------------------------------------------------------------------------+
| const vec2 *SCREEN_UV*           | Screen Texture Coordinate (for using with texscreen)                             |
+----------------------------------+----------------------------------------------------------------------------------+
| const float *TIME*               | Time (in seconds)                                                                |
+----------------------------------+----------------------------------------------------------------------------------+
| const vec2 *POINT_COORD*         | UV for point, when drawing point sprites.                                        |
+----------------------------------+----------------------------------------------------------------------------------+
| out vec3 *DIFFUSE*               | Diffuse Color                                                                    |
+----------------------------------+----------------------------------------------------------------------------------+
| out vec4 *DIFFUSE_ALPHA*         | Diffuse Color with Alpha (using this sends geometry to alpha pipeline)           |
+----------------------------------+----------------------------------------------------------------------------------+
| out vec3 *SPECULAR*              | Specular Color                                                                   |
+----------------------------------+----------------------------------------------------------------------------------+
| out vec3 *EMISSION*              | Emission Color                                                                   |
+----------------------------------+----------------------------------------------------------------------------------+
| out float *SPEC_EXP*             | Specular Exponent (Fragment Version)                                             |
+----------------------------------+----------------------------------------------------------------------------------+
| out float *GLOW*                 | Glow                                                                             |
+----------------------------------+----------------------------------------------------------------------------------+
| out mat4 *INV_CAMERA_MATRIX*     | Inverse camera matrix, can be used to obtain world coords (see example below).   |
+----------------------------------+----------------------------------------------------------------------------------+

Material - LightShader
~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------+-------------------------------+
| Variable                       | Description                   |
+================================+===============================+
| const vec3 *NORMAL*            | View-Space normal             |
+--------------------------------+-------------------------------+
| const vec3 *LIGHT_DIR*         | View-Space Light Direction    |
+--------------------------------+-------------------------------+
| const vec3 *EYE_VEC*           | View-Space Eye-Point Vector   |
+--------------------------------+-------------------------------+
| const vec3 *DIFFUSE*           | Material Diffuse Color        |
+--------------------------------+-------------------------------+
| const vec3 *LIGHT_DIFFUSE*     | Light Diffuse Color           |
+--------------------------------+-------------------------------+
| const vec3 *SPECULAR*          | Material Specular Color       |
+--------------------------------+-------------------------------+
| const vec3 *LIGHT_SPECULAR*    | Light Specular Color          |
+--------------------------------+-------------------------------+
| const float *SPECULAR_EXP*     | Specular Exponent             |
+--------------------------------+-------------------------------+
| const vec1 *SHADE_PARAM*       | Generic Shade Parameter       |
+--------------------------------+-------------------------------+
| const vec2 *POINT_COORD*       | Current UV for Point Sprite   |
+--------------------------------+-------------------------------+
| out vec2 *LIGHT*               | Resulting Light               |
+--------------------------------+-------------------------------+
| const float *TIME*             | Time (in seconds)             |
+--------------------------------+-------------------------------+

CanvasItem (2D) - VertexShader
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| \|\ *. Variable \|*. Description \|
| \| const vec2 *SRC_VERTEX* \| CanvasItem space vertex. \|
| \| vec2 *UV* \| UV \|
| \| out vec2 *VERTEX* \| Output LocalSpace vertex. \|
| \| out vec2 *WORLD_VERTEX* \| Output WorldSpace vertex. (use this or
  the one above) \|
| \| color *COLOR* \| Vertex Color \|
| \| out vec4 *VAR1* \| Varying 1 Output \|
| \| out vec4 *VAR2* \| Varying 2 Output \|
| \| out float *POINT_SIZE* \| Point Size (for points) \|
| \| const mat4 *WORLD_MATRIX* \| Object World Matrix \|
| \| const mat4 *EXTRA_MATRIX* \| Extra (user supplied) matrix via
  :ref:`CanvasItem.draw_set_transform() <class_CanvasItem_draw_set_transform>`.
  Identity by default. \|
| \| const mat4 *PROJECTION_MATRIX* \| Projection Matrix (model coords
  to screen).\|
| \| const float *TIME* \| Time (in seconds) \|

CanvasItem (2D) - FragmentShader
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| \|\ *. Variable \|*. Description \|
| \| const vec4 *SRC_COLOR* \| Vertex color \|
| \| const vec4 *POSITION* \| Screen Position \|
| \| vec2 *UV* \| UV \|
| \| out color *COLOR* \| Output Color \|
| \| out vec3 *NORMAL* \| Optional Normal (used for 2D Lighting) \|
| \| out vec3 *NORMALMAP* \| Optional Normal in standard normalmap
  format (flipped y and Z from 0 to 1) \|
| \| out float *NORMALMAP_DEPTH* \| Depth option for above normalmap
  output, default value is 1.0 \|
| \| const texture *TEXTURE* \| Current texture in use for CanvasItem \|
| \| const vec2 *TEXTURE_PIXEL_SIZE* \| Pixel size for current 2D
  texture \|
| \| in vec4 *VAR1* \| Varying 1 Output \|
| \| in vec4 *VAR2* \| Varying 2 Output \|
| \| const vec2 *SCREEN_UV*\ \| Screen Texture Coordinate (for using
  with texscreen) \|
| \| const vec2 *POINT_COORD* \| Current UV for Point Sprite \|
| \| const float *TIME*\ \| Time (in seconds) \|

CanvasItem (2D) - LightShader
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| \|\ *. Variable \|*. Description \|
| \| const vec4 *POSITION* \| Screen Position \|
| \| in vec3 *NORMAL* \| Input Normal \|
| \| in vec2 *UV* \| UV \|
| \| in color *COLOR* \| Input Color \|
| \| const texture *TEXTURE* \| Current texture in use for CanvasItem \|
| \| const vec2 *TEXTURE_PIXEL_SIZE* \| Pixel size for current 2D
  texture \|
| \| in vec4 *VAR1* \| Varying 1 Output \|
| \| in vec4 *VAR2* \| Varying 2 Output \|
| \| const vec2 *SCREEN_UV*\ \| Screen Texture Coordinate (for using
  with texscreen) \|
| \| const vec2 *POINT_COORD* \| Current UV for Point Sprite \|
| \| const float *TIME*\ \| Time (in seconds) \|
| \| vec2 *LIGHT_VEC* \| Vector from light to fragment, can be modified
  to alter shadow computation. \|
| \| const float *LIGHT_HEIGHT* \| Height of Light \|
| \| const color *LIGHT_COLOR* \| Color of Light \|
| \| out vec4 *LIGHT* \| Light Ouput (shader is ignored if this is not
  used) \|

Examples
--------

Material that reads a texture, a color and multiples them, fragment
program:

::

    uniform color modulate;
    uniform texture source;

    DIFFUSE = modulate.rgb * tex(source,UV).rgb;

Material that glows from red to white:

::

    DIFFUSE = vec3(1,0,0) + vec(1,1,1)*mod(TIME,1.0);

Standard Blinn Lighting Shader

::

    float NdotL = max(0.0,dot( NORMAL, LIGHT_DIR ));
    vec3 half_vec = normalize(LIGHT_DIR + EYE_VEC);
    float eye_light = max(dot(NORMAL, half_vec),0.0);
    LIGHT = LIGHT_DIFFUSE + DIFFUSE + NdotL;
    if (NdotL > 0.0) {
        LIGHT+=LIGHT_SPECULAR + SPECULAR + pow( eye_light, SPECULAR_EXP );
    };

Obtaining world-space normal and position in material fragment program:

::

    //use reverse multiply because INV_CAMERA_MATRIX is world2cam

    vec3 world_normal = NORMAL * mat3(INV_CAMERA_MATRIX);
    vec3 world_pos = (VERTEX-INV_CAMERA_MATRIX.w.xyz) * mat3(INV_CAMERA_MATRIX);

Notes
-----

| \* **Do not** use DIFFUSE_ALPHA unless you really intend to use
  transparency. Transparent materials must be sorted by depth and slow
  down the rendering pipeline. For opaque materials, just use DIFFUSE.
| \* **Do not** use DISCARD unless you really need it. Discard makes
  rendering slower, specially on mobile devices.
| \* TIME may reset after a while (may last an hour or so), it's meant
  for effects that vary over time.
| \* In general, every built-in variable not used results in less shader
  code generated, so writing a single giant shader with a lot of code
  and optional scenarios is often not a good idea.
