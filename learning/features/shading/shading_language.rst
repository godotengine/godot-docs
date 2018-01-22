.. _doc_shading_language:

Shading language
================

Introduction
------------

Godot uses a shading language very similar to GLSL ES 3.0. Most datatypes and functions are supported,
and the remaining will likely be added over time.

Unlike the shader language in Godot 2.x, this implementation is much closer to the original.

Shader Types
------------

Instead of supplying a general purpose configuration, Godot Shading Language must
specify what shader is intended for. Depending on the type, different render
modes, built-in variables and processing functions are supported.

Any shader needs a first line specifying this type, in the following format:

.. code-block:: glsl

    shader_type <type>;

Valid types are:

* "spatial": For 3D rendering.
* "canvas_item": For 2D rendering.
* "particles": For particle systems.


Render Modes
------------

Different shader types support different render modes. They are optional but, if specified, must
be after the *shader_type*. Example syntax is:

.. code-block:: glsl

    shader_type spatial;
    render_mode unshaded, cull_disabled;

Data types:
-----------

Most GLSL ES 3.0 datatypes are supported. Following is the list:

+-----------------+---------------------------------------------------------------------------+
| Type            | Description                                                               |
+=================+===========================================================================+
| **void**        | Void datatype, useful only for functions that return nothing.             |
+-----------------+---------------------------------------------------------------------------+
| **bool**        | Boolean datatype, can only contain "true" or "false"                      |
+-----------------+---------------------------------------------------------------------------+
| **bvec2**       | Two component vector of booleans.                                         |
+-----------------+---------------------------------------------------------------------------+
| **bvec3**       | Three component vector of booleans.                                       |
+-----------------+---------------------------------------------------------------------------+
| **bvec4**       | Four component vector of booleans.                                        |
+-----------------+---------------------------------------------------------------------------+
| **int**         | Signed scalar integer.                                                    |
+-----------------+---------------------------------------------------------------------------+
| **ivec2**       | Two component vector of signed integers.                                  |
+-----------------+---------------------------------------------------------------------------+
| **ivec3**       | Three component vector of signed integers.                                |
+-----------------+---------------------------------------------------------------------------+
| **ivec4**       | Four component vector of signed integers.                                 |
+-----------------+---------------------------------------------------------------------------+
| **uint**        | Unsigned scalar integer, can't contain negative numbers.                  |
+-----------------+---------------------------------------------------------------------------+
| **uvec2**       | Two component vector of unsigned integers.                                |
+-----------------+---------------------------------------------------------------------------+
| **uvec3**       | Three component vector of unsigned integers.                              |
+-----------------+---------------------------------------------------------------------------+
| **uvec4**       | Four component vector of unsigned integers.                               |
+-----------------+---------------------------------------------------------------------------+
| **float**       | Floating point scalar.                                                    |
+-----------------+---------------------------------------------------------------------------+
| **vec2**        | Two component vector of floating point values.                            |
+-----------------+---------------------------------------------------------------------------+
| **vec3**        | Three component vector of floating point values.                          |
+-----------------+---------------------------------------------------------------------------+
| **vec4**        | Four component vector of floating point values.                           |
+-----------------+---------------------------------------------------------------------------+
| **mat2**        | 2x2 matrix, in column major order.                                        |
+-----------------+---------------------------------------------------------------------------+
| **mat3**        | 3x3 matrix, in column major order.                                        |
+-----------------+---------------------------------------------------------------------------+
| **mat4**        | 4x4 matrix, in column major order.                                        |
+-----------------+---------------------------------------------------------------------------+
| **sampler2D**   | Sampler type, for binding 2D textures, which are read as float.           |
+-----------------+---------------------------------------------------------------------------+
| **isampler2D**  | Sampler type for binding 2D textures, which are read as signed integer.   |
+-----------------+---------------------------------------------------------------------------+
| **usampler2D**  | Sampler type for binding 2D textures, which are read as unsigned integer. |
+-----------------+---------------------------------------------------------------------------+
| **samplerCube** | Sampler type for binding Cubemaps, which are read as floats.              |
+-----------------+---------------------------------------------------------------------------+


Casting
~~~~~~~

Just like GLSL ES 3.0, implicit casting is not allowed between scalars and vectors of the same size but different type.
Casting of types of different size is also not allowed. Conversion must be done explicitly via constructors.

Example:

.. code-block:: glsl

    float a = 2; // valid
    float a = 2.0; // valid
    float a = float(2); // valid

Default integer constants are signed, so casting is always needed to convert to unsigned:

.. code-block:: glsl

    int a = 2; // valid
    uint a = 2; // invalid
    uint a = uint(2); // valid

Members
~~~~~~~

Individual scalar members of vector types are accessed via the "x", "y", "z" and "w" members. Alternatively, using "r", "g", "b" and "a" also works and is equivalent.
Use whatever fits best for your use case.

For matrices, use [idx] indexing syntax to access each vector.

Constructing
~~~~~~~~~~~~

Construction of vector types must always pass:

.. code-block:: glsl

    // The required amount of scalars
    vec4 a = vec4(0.0, 1.0, 2.0, 3.0);
    // Complementary vectors and/or scalars
    vec4 a = vec4(vec2(0.0, 1.0), vec2(2.0, 3.0));
    vec4 a = vec4(vec3(0.0, 1.0, 2.0), 3.0);
    // A single scalar for the whole vector
    vec4 a = vec4(0.0);

Swizzling
~~~~~~~~~

It is possible to obtain any combination of them in any order, as long as the result is another vector type (or scalar).
This is easier shown than explained:

.. code-block:: glsl

    vec4 a = vec4(0.0, 1.0, 2.0, 3.0);
    vec3 b = a.rgb; // Creates a vec3 with vec4 components
    vec3 b = a.aaa; // Also valid, creates a vec3 and fills it with "a".
    vec3 b = a.bgr; // Order does not matter
    vec3 b = a.xyz; // Also rgba, xyzw are equivalent
    float c = b.w; // Invalid, because "w" is not present in vec3 b

Precision
~~~~~~~~~

It is possible to add precision modifiers to datatypes, use them for uniforms, variables, arguments and varyings:

.. code-block:: glsl

    lowp vec4 a = vec4(0.0, 1.0, 2.0, 3.0); // low precision, usually 8 bits per component mapped to 0-1
    mediump vec4 a = vec4(0.0, 1.0, 2.0, 3.0); // medium precision, usually 16 bits or half float
    highp vec4 a = vec4(0.0, 1.0, 2.0, 3.0); // high precision, uses full float or integer range (default)


Using lower precision for some operations can speed up the math involved (at the cost of, of course, less precision).
This is rarely needed in the vertex shader (where full precision is needed most of the time), but often needed in the fragment one.

Keep in mind that some architectures (mainly mobile) benefit a lot from this, but are also restricted (conversion between precisions has a cost).
Please read the relevant documentation on the target architecture to find out more. In all honesty though, mobile drivers are really buggy
so just stay out of trouble and make simple shaders without specifying precision unless you *really* need to.

Operators:
----------

Godot shading language supports the same set of operators as GLSL ES 3.0. Below is the list of them in precedence order:

+-------------+-----------------------+--------------------+
| Precedence  | Class                 | Operator           |
+-------------+-----------------------+--------------------+
| 1 (highest) | parenthetical grouping| **()**             |
+-------------+-----------------------+--------------------+
| 2           | unary                 | **+, -, !, ~**     |
+-------------+-----------------------+--------------------+
| 3           | multiplicative        | **/, \*, %**       |
+-------------+-----------------------+--------------------+
| 4           | additive              | **+, -**           |
+-------------+-----------------------+--------------------+
| 5           | bit-wise shift        | **<<, >>**         |
+-------------+-----------------------+--------------------+
| 6           | relational            | **<, >, <=, >=**   |
+-------------+-----------------------+--------------------+
| 7           | equality              | **==, !=**         |
+-------------+-----------------------+--------------------+
| 8           | bit-wise and          | **&**              |
+-------------+-----------------------+--------------------+
| 9           | bit-wise exclusive or | **^**              |
+-------------+-----------------------+--------------------+
| 10          | bit-wise inclusive or | **|**              |
+-------------+-----------------------+--------------------+
| 11          | logical and           | **&&**             |
+-------------+-----------------------+--------------------+
| 12 (lowest) | logical inclusive or  | **||**             |
+-------------+-----------------------+--------------------+

Flow Control
------------

Godot Shading language supports the most common types of flow control:

.. code-block:: glsl

    // if and else
    if (cond) {

    } else {

    }

    // for loops
    for     (int i = 0; i < 10; i++) {

    }

    // while
    while (true) {

    }


Keep in mind that, in modern GPUs, an infinite loop can exist and can freeze your application (including editor).
Godot can't protect you from this, so be careful to not make this mistake!

Discarding
-----------

Fragment and light functions can use the *discard* keyword. If used, the fragment is discarded and nothing is written.

Functions
---------

It's possible to define any function in a Godot shader. They take the following syntax:

.. code-block:: glsl

    ret_type func_name(args) {

        return ret_type; // if returning a value
    }

    // a better example:

    int sum2(int a, int b) {
        return a + b;
    }


Functions can be used from any other function that is below it.

Function argument can have special qualifiers:

* **in**: Means the argument is only for reading (default).
* **out**: Means the argument is only for writing.
* **inout**: Means the argument is fully passed via reference.

Example below:

.. code-block:: glsl

    void sum2(int a, int b, inout int result) {
        result = a + b;
    }



Processor Functions
-------------------

Depending on shader type, processor functions may be available to optionally override.
For "spatial" and "canvas_item", it is possible to override "vertex", "fragment" and "light".
For "particles", only "vertex" can be overridden.

Vertex Processor
~~~~~~~~~~~~~~~~~

The "vertex" processing function is called for every vertex, 2D or 3D. For particles, it's called for every
particle.

Depending on shader type, a different set of built-in inputs and outputs are provided. In general,
vertex functions are not that commonly used.

.. code-block:: glsl

    shader_type spatial;

    void vertex() {
        VERTEX.x += sin(TIME); // offset vertex x by sine function on time elapsed
    }


Fragment Processor
~~~~~~~~~~~~~~~~~~

The "fragment" processor is used to set up the Godot material parameters per pixel. This code
runs on every visible pixel the object or primitive is drawn to.

.. code-block:: glsl

    shader_type spatial;

    void fragment() {
        ALBEDO = vec3(1.0, 0.0, 0.0); // use red for material albedo
    }

Light Processor
~~~~~~~~~~~~~~~

The "light" processor runs per pixel too, but also runs for every light that affects the object (
and does not run if no lights affect the object).

.. code-block:: glsl

    shader_type spatial;

    void light() {
        COLOR = vec3(0.0, 1.0, 0.0);
    }


Varyings
~~~~~~~~

To send data from vertex to fragment shader, *varyings* are used. They are set for every primitive vertex
in the *vertex processor*, and the value is interpolated (and perspective corrected) when reaching every
pixel in the fragment processor.


.. code-block:: glsl

    shader_type spatial;

    varying vec3 some_color;
    void vertex() {
        some_color = NORMAL; // make the normal the color
    }

    void fragment() {
        ALBEDO = some_color;
    }

Uniforms
~~~~~~~~

Passing values to shaders is possible. These are global to the whole shader and called *uniforms*.
When a shader is later assigned to a material, the uniforms will appear as editable parameters on it.
Uniforms can't be written from within the shader.

.. code-block:: glsl

    shader_type spatial;

    uniform float some_value;


Any type except for *void* can be a uniform. Additionally, Godot provides optional shader hints
to make the compiler understand what the uniform is used for.


.. code-block:: glsl

    shader_type spatial;

    uniform vec4 color : hint_color;
    uniform float amount : hint_range(0, 1);


Full list of hints below:

+----------------+-------------------------------+-------------------------------------+
| Type           | Hint                          | Description                         |
+================+===============================+=====================================+
| **vec4**       | hint_color                    | Used as color                       |
+----------------+-------------------------------+-------------------------------------+
| **int, float** | hint_range(min,max [,step] )  | Used as range (with min/max/step)   |
+----------------+-------------------------------+-------------------------------------+
| **sampler2D**  | hint_albedo                   | Used as albedo color, default white |
+----------------+-------------------------------+-------------------------------------+
| **sampler2D**  | hint_black_albedo             | Used as albedo color, default black |
+----------------+-------------------------------+-------------------------------------+
| **sampler2D**  | hint_normal                   | Used as normalmap                   |
+----------------+-------------------------------+-------------------------------------+
| **sampler2D**  | hint_white                    | As value, default to white.         |
+----------------+-------------------------------+-------------------------------------+
| **sampler2D**  | hint_black                    | As value, default to black          |
+----------------+-------------------------------+-------------------------------------+
| **sampler2D**  | hint_aniso                    | As flowmap, default to right.       |
+----------------+-------------------------------+-------------------------------------+


As Godot 3D engine renders in linear color space, it's important to understand that textures
that are supplied as color (ie, albedo) need to be specified as such for proper SRGB->linear
conversion.


Uniforms can also be assigned default values:


.. code-block:: glsl

    shader_type spatial;

    uniform vec4 some_vector = vec4(0.0);



Built-in Functions
------------------

A large number of built-in functions are supported, conforming mostly to GLSL ES 3.0.
When vec_type (float), vec_int_type, vec_uint_type, vec_bool_type nomenclature is used, it can be scalar or vector.


+-----------------------------------------------------------------------+---------------------------------------------+
| Function                                                              | Description                                 |
+=======================================================================+=============================================+
| float **sin** ( float )                                               | Sine                                        |
+-----------------------------------------------------------------------+---------------------------------------------+
| float **cos** ( float )                                               | Cosine                                      |
+-----------------------------------------------------------------------+---------------------------------------------+
| float **tan** ( float )                                               | Tangent                                     |
+-----------------------------------------------------------------------+---------------------------------------------+
| float **asin** ( float )                                              | arc-Sine                                    |
+-----------------------------------------------------------------------+---------------------------------------------+
| float **acos** ( float )                                              | arc-Cosine                                  |
+-----------------------------------------------------------------------+---------------------------------------------+
| float **atan** ( float )                                              | arc-Tangent                                 |
+-----------------------------------------------------------------------+---------------------------------------------+
| float **atan2** ( float x, float y)                                   | arc-Tangent to convert vector to angle      |
+-----------------------------------------------------------------------+---------------------------------------------+
| float **sinh** ( float )                                              | Hyperbolic-Sine                             |
+-----------------------------------------------------------------------+---------------------------------------------+
| float **cosh** ( float )                                              | Hyperbolic-Cosine                           |
+-----------------------------------------------------------------------+---------------------------------------------+
| float **tanh** ( float )                                              | Hyperbolic-Tangent                          |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec\_type **pow** ( float x, float y)                                 | Power, x elevated to y                      |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec\_type **pow** ( vec\_type, vec\_type )                            | Power (Vec. Exponent)                       |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec\_type **exp** ( vec\_type )                                       | Base-e Exponential                          |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec\_type **log** ( vec\_type )                                       | Natural Logarithm                           |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec\_type **sqrt** ( vec\_type )                                      | Square Root                                 |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec\_type **inversesqrt** ( vec\_type )                               | Inverse Square Root                         |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec\_type **abs** ( vec\_type )                                       | Absolute                                    |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec\_type **sign** ( vec\_type )                                      | Sign                                        |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec\_type **floor** ( vec\_type )                                     | Floor                                       |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec\_type **round** ( vec\_type )                                     | Round                                       |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec\_type **trunc** ( vec\_type )                                     | Trunc                                       |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec\_type **ceil** ( vec\_type )                                      | Ceiling                                     |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec\_type **fract** ( vec\_type )                                     | Fractional                                  |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec\_type **mod** ( vec\_type,vec\_type )                             | Remainder                                   |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec\_type **modf** ( vec\_type x,out vec\_type i)                     | Fractional of x, with i has integer part    |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec\_type **min** ( vec\_type,vec\_type )                             | Minimum                                     |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec\_type **max** ( vec\_type,vec\_type )                             | Maximum                                     |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec\_type **clamp** ( vec\_type value,vec\_type min, vec\_type max )  | Clamp to Min-Max                            |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec\_type **mix** ( vec\_type a,vec\_type b, float c )                | Linear Interpolate                          |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec\_type **mix** ( vec\_type a,vec\_type b, vec\_type c )            | Linear Interpolate (Vector Coef.)           |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec\_type **step** ( vec\_type a,vec\_type b)                         | \` a[i] < b[i] ? 0.0 : 1.0\`                |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec\_type **smoothstep** ( vec\_type a,vec\_type b,vec\_type c)       |                                             |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec_bool_type **isnan** ( vec\_type )                                 | scalar, or vector component being nan       |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec_bool_type **isinf** ( vec\_type )                                 | scalar, or vector component being inf       |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec_int_type **floatBitsToInt** ( vec_type )                          | Float->Int bit copying, no conversion       |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec_uint_type **floatBitsToUInt** ( vec_type )                        | Float->UInt bit copying, no conversion      |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec_type **intBitsToFloat** ( vec_int_type )                          | Int->Float bit copying, no conversion       |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec_type **uintBitsToFloat** ( vec_uint_type )                        | UInt->Float bit copying, no conversion      |
+-----------------------------------------------------------------------+---------------------------------------------+
| float **length** ( vec\_type )                                        | Vector Length                               |
+-----------------------------------------------------------------------+---------------------------------------------+
| float **distance** ( vec\_type, vec\_type )                           | Distance between vector.                    |
+-----------------------------------------------------------------------+---------------------------------------------+
| float **dot** ( vec\_type, vec\_type )                                | Dot Product                                 |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec3 **cross** ( vec3, vec3 )                                         | Cross Product                               |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec\_type **normalize** ( vec\_type )                                 | Normalize to unit length                    |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec3 **reflect** ( vec3, vec3 )                                       | Reflect                                     |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec3 **refract** ( vec3, vec3 )                                       | Refract                                     |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec_type **faceforward** ( vec_type N, vec_type I, vec_type NRef)     | If dot(Nref, I) < 0 return N, otherwise –N  |
+-----------------------------------------------------------------------+---------------------------------------------+
| mat_type **matrixCompMult** ( mat_type, mat_type )                    | Matrix Component Multiplication             |
+-----------------------------------------------------------------------+---------------------------------------------+
| mat_type **outerProduct** ( vec_type, vec_type )                      | Matrix Outer Product                        |
+-----------------------------------------------------------------------+---------------------------------------------+
| mat_type **transpose** ( mat_type )                                   | Transpose Matrix                            |
+-----------------------------------------------------------------------+---------------------------------------------+
| float **determinant** ( mat_type )                                    | Matrix Determinant                          |
+-----------------------------------------------------------------------+---------------------------------------------+
| mat_type **inverse** ( mat_type )                                     | Inverse Matrix                              |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec\_bool_type **lessThan** ( vec_scalar_type )                       | Bool vector cmp on < int/uint/float vectors |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec\_bool_type **greaterThan** ( vec_scalar_type )                    | Bool vector cmp on > int/uint/float vectors |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec\_bool_type **lessThanEqual** ( vec_scalar_type )                  | Bool vector cmp on <= int/uint/float vectors|
+-----------------------------------------------------------------------+---------------------------------------------+
| vec\_bool_type **greaterThanEqual** ( vec_scalar_type )               | Bool vector cmp on >= int/uint/float vectors|
+-----------------------------------------------------------------------+---------------------------------------------+
| vec\_bool_type **equal** ( vec_scalar_type )                          | Bool vector cmp on == int/uint/float vectors|
+-----------------------------------------------------------------------+---------------------------------------------+
| vec\_bool_type **notEqual** ( vec_scalar_type )                       | Bool vector cmp on != int/uint/float vectors|
+-----------------------------------------------------------------------+---------------------------------------------+
| bool **any** ( vec_bool_type )                                        | Any component is true                       |
+-----------------------------------------------------------------------+---------------------------------------------+
| bool **all** ( vec_bool_type )                                        | All components are true                     |
+-----------------------------------------------------------------------+---------------------------------------------+
| bool **not** ( vec_bool_type )                                        | No components are true                      |
+-----------------------------------------------------------------------+---------------------------------------------+
| ivec2 **textureSize** ( sampler2D_type s, int lod )                   | Get the size of a texture                   |
+-----------------------------------------------------------------------+---------------------------------------------+
| ivec2 **textureSize** ( samplerCube s, int lod )                      | Get the size of a cubemap                   |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec4_type **texture** ( sampler2D_type s, vec2 uv [, float bias])     | Perform a 2D texture read                   |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec4_type **texture** ( samplerCube s, vec3 uv [, float bias])        | Perform a Cube texture read                 |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec4_type **textureProj** ( sampler2d_type s, vec3 uv [, float bias]) | Perform a texture read with projection      |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec4_type **textureProj** ( sampler2d_type s, vec4 uv [, float bias]) | Perform a texture read with projection      |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec4_type **textureLod** ( sampler2D_type s, vec2 uv , float lod)     | Perform a 2D texture read at custom mipmap  |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec4_type **textureProjLod** ( sampler2d_type s, vec3 uv , float lod) | Perform a texture read with projection/lod  |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec4_type **textureProjLod** ( sampler2d_type s, vec4 uv , float lod) | Perform a texture read with projection/lod  |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec_type **texelFetch** ( samplerCube s, ivec2 uv, int lod )          | Fetch a single texel using integer coords   |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec_type **dFdx** ( vec_type )                                        | Derivative in x using local differencing    |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec_type **dFdy** ( vec_type )                                        | Derivative in y using local differencing    |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec_type **fwidth** ( vec_type )                                      | Sum of absolute derivative in x and y       |
+-----------------------------------------------------------------------+---------------------------------------------+



Shader Types In-Depth
---------------------

Spatial
~~~~~~~

Accepted render modes and built-ins for "shader_type spatial;".

Render Modes
^^^^^^^^^^^^

+---------------------------------+----------------------------------------------------------------------+
| Render Mode                     | Description                                                          |
+=================================+======================================================================+
| **blend_mix**                   | Mix blend mode (alpha is transparency), default.                     |
+---------------------------------+----------------------------------------------------------------------+
| **blend_add**                   | Additive blend mode.                                                 |
+---------------------------------+----------------------------------------------------------------------+
| **blend_sub**                   | Substractive blend mode.                                             |
+---------------------------------+----------------------------------------------------------------------+
| **blend_mul**                   | Multiplicative blend mode.                                           |
+---------------------------------+----------------------------------------------------------------------+
| **depth_draw_opaque**           | Only draw depth for opaque geometry (not transparent).               |
+---------------------------------+----------------------------------------------------------------------+
| **depth_draw_always**           | Always draw depth (opaque and transparent).                          |
+---------------------------------+----------------------------------------------------------------------+
| **depth_draw_never**            | Never draw depth.                                                    |
+---------------------------------+----------------------------------------------------------------------+
| **depth_draw_alpha_prepass**    | Do opaque depth pre-pass for transparent geometry.                   |
+---------------------------------+----------------------------------------------------------------------+
| **depth_test_disable**          | Disable depth testing.                                               |
+---------------------------------+----------------------------------------------------------------------+
| **cull_front**                  | Cull front-faces.                                                    |
+---------------------------------+----------------------------------------------------------------------+
| **cull_back**                   | Cull back-faces (default).                                           |
+---------------------------------+----------------------------------------------------------------------+
| **cull_disabled**               | Culling disabled (double sided).                                     |
+---------------------------------+----------------------------------------------------------------------+
| **unshaded**                    | Result is just albedo. No lighting/shading happens in material.      |
+---------------------------------+----------------------------------------------------------------------+
| **diffuse_lambert**             | Lambert shading for diffuse (default).                               |
+---------------------------------+----------------------------------------------------------------------+
| **diffuse_lambert_wrap**        | Lambert wrapping (roughness dependent) for diffuse.                  |
+---------------------------------+----------------------------------------------------------------------+
| **diffuse_oren_nayar**          | Oren Nayar for diffuse.                                              |
+---------------------------------+----------------------------------------------------------------------+
| **diffuse_burley**              | Burley (Disney PBS) for diffuse.                                     |
+---------------------------------+----------------------------------------------------------------------+
| **diffuse toon**                | Toon shading for diffuse.                                            |
+---------------------------------+----------------------------------------------------------------------+
| **specular_schlick_ggx**        | Schlick-GGX for specular (default).                                  |
+---------------------------------+----------------------------------------------------------------------+
| **specular_blinn**              | Blinn for specular (compatibility).                                  |
+---------------------------------+----------------------------------------------------------------------+
| **specular_phong**              | Phong for specular (compatibility).                                  |
+---------------------------------+----------------------------------------------------------------------+
| **specular_toon**               | Toon for specular.                                                   |
+---------------------------------+----------------------------------------------------------------------+
| **specular_disabled**           | Disable specular.                                                    |
+---------------------------------+----------------------------------------------------------------------+
| **skip_vertex_transform**       | VERTEX/NORMAL/etc need to be transformed manually in VS.             |
+---------------------------------+----------------------------------------------------------------------+
| **world_vertex_coords**         | VERTEX/NORMAL/etc are modified in world coordinates instead of local.|
+---------------------------------+----------------------------------------------------------------------+
| **vertex_lighting**             | Use vertex-based lighting.                                           |
+---------------------------------+----------------------------------------------------------------------+


Vertex Built-Ins
^^^^^^^^^^^^^^^^

+----------------------------------+-------------------------------------------------------+
| Built-In                         | Object vertex to world space transform.               |
+==================================+=======================================================+
| mat4 **WORLD_MATRIX**            | Model space to world space transform.                 |
+----------------------------------+-------------------------------------------------------+
| mat4 **INV_CAMERA_MATRIX**       | World space to view space transform.                  |
+----------------------------------+-------------------------------------------------------+
| mat4 **PROJECTION_MATRIX**       | View space to clip space transform.                   |
+----------------------------------+-------------------------------------------------------+
| mat4 **CAMERA_MATRIX**           | View space to world space transform.                  |
+----------------------------------+-------------------------------------------------------+
| mat4 **MODELVIEW_MATRIX**        | Model space to view space transform (use if possible).|
+----------------------------------+-------------------------------------------------------+
| mat4 **INV_PROJECTION_MATRIX**   | Clip space to view space transform.                   |
+----------------------------------+-------------------------------------------------------+
| float **TIME**                   | Elapsed total time in seconds.                        |
+----------------------------------+-------------------------------------------------------+
| vec2 **VIEWPORT_SIZE**           | Size of viewport (in pixels).                         |
+----------------------------------+-------------------------------------------------------+
| vec3 **VERTEX**                  | Vertex in local coords (see doc below).               |
+----------------------------------+-------------------------------------------------------+
| vec3 **NORMAL**                  | Normal in local coords.                               |
+----------------------------------+-------------------------------------------------------+
| vec3 **TANGENT**                 | Tangent in local coords.                              |
+----------------------------------+-------------------------------------------------------+
| vec3 **BINORMAL**                | Binormal in local coords.                             |
+----------------------------------+-------------------------------------------------------+
| vec2 **UV**                      | UV main channel.                                      |
+----------------------------------+-------------------------------------------------------+
| vec2 **UV2**                     | UV secondary channel.                                 |
+----------------------------------+-------------------------------------------------------+
| vec4 **COLOR**                   | Color from vertices.                                  |
+----------------------------------+-------------------------------------------------------+
| vec2 **POINT_SIZE**              | Point size for point rendering.                       |
+----------------------------------+-------------------------------------------------------+
| int **INSTANCE_ID**              | Instance ID for instancing.                           |
+----------------------------------+-------------------------------------------------------+
| vec4 **INSTANCE_CUSTOM**         | Instance custom data (for particles, mostly).         |
+----------------------------------+-------------------------------------------------------+
| float **ROUGHNESS**              | Roughness for vertex lighting.                        |
+----------------------------------+-------------------------------------------------------+


Vertex data (VERTEX, NORMAL, TANGENT, BITANGENT) is presented in local model space. If not
written to, these values will not be modified and be passed through as they came.

They can be optionally set to be presented in world space (after being transformed by world)
by adding the *world_vertex_coords* render mode.

It is also possible to completely disable the built-in modelview transform (projection will still
happen later, though) with the following code, so it can be done manually:

.. code-block:: glsl

    shader_type spatial;
    render_mode skip_vertex_transform;

    void vertex() {

        VERTEX = (MODELVIEW_MATRIX * vec4(VERTEX, 1.0)).xyz;
        NORMAL = (MODELVIEW_MATRIX * vec4(VERTEX, 0.0)).xyz;
        // same as above for binormal and tangent, if normal mapping is used
    }


Other built-ins such as UV, UV2 and COLOR are also passed through to the fragment function if not modified.

For instancing, the INSTANCE_CUSTOM variable contains the instance custom data. When using particles, this information
is usually:

* **x**: Rotation angle in radians.
* **y**: Phase during lifetime (0 to 1).
* **z**: Animation frame.

This allows to easily adjust the shader to a particle system using default particles material. When writing a custom particles
shader, this value can be used as desired.


Fragment Built-Ins
^^^^^^^^^^^^^^^^^^

+----------------------------------+--------------------------------------------------------------------------------------------------+
| Built-In                         | Description                                                                                      |
+==================================+==================================================================================================+
| in mat4 **WORLD_MATRIX**         | Model space to world space transform.                                                            |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| in mat4 **INV_CAMERA_MATRIX**    | World space to view space transform.                                                             |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| in mat4 **PROJECTION_MATRIX**    | View space to clip space transform.                                                              |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| in mat4 **CAMERA_MATRIX**        | View space to world space transform.                                                             |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| in mat4 **INV_PROJECTION_MATRIX**| Clip space to view space transform.                                                              |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| float **TIME**                   | Elapsed total time in seconds.                                                                   |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| vec2 **VIEWPORT_SIZE**           | Size of viewport (in pixels).                                                                    |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| vec3 **VERTEX**                  | Vertex that comes from vertex function, in view space.                                           |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| in vec4 **FRAGCOORD**            | Fragment cordinate, pixel adjusted.                                                              |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| in bool **FRONT_FACING**         | true whether current face is front face.                                                         |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| inout vec3 **NORMAL**            | Normal that comes from vertex function, in view space.                                           |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| inout vec3 **TANGENT**           | Tangent that comes from vertex function.                                                         |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| inout vec3 **BINORMAL**          | Binormal that comes from vertex function.                                                        |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| out vec3 **NORMALMAP**           | Output this if reading normal from a texture instead of NORMAL.                                  |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| out float **NORMALMAP_DEPTH**    | Depth from variable above. Defaults to 1.0.                                                      |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| in vec2 **UV**                   | UV that comes from vertex function.                                                              |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| in vec2 **UV2**                  | UV2 that coems from vertex function.                                                             |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| in vec4 **COLOR**                | COLOR that comes from vertex function.                                                           |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| out vec3 **ALBEDO**              | Albedo (default white).                                                                          |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| out float **ALPHA**              | Alpha (0..1), if written to the material will go to transparent pipeline.                        |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| out float **METALLIC**           | Metallic (0..1).                                                                                 |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| out float **SPECULAR**           | Specular. Defaults to 0.5, best to not modify unless you want to change IOR.                     |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| out float **ROUGHNESS**          | Roughness (0..1).                                                                                |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| out float **RIM**                | Rim (0..1).                                                                                      |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| out float **RIM_TINT**           | Rim Tint, goes from 0 (white) to 1 (albedo).                                                     |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| out float **CLEARCOAT**          | Small added specular blob.                                                                       |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| out float **CLEARCOAT_GLOSS**    | Gloss of Clearcoat.                                                                              |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| out float **ANISOTROPY**         | For distorting the specular blob according to tangent space.                                     |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| out float **ANISOTROPY_FLOW**    | Distortion direction, use with flowmaps.                                                         |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| out float **SSS_STRENGTH**       | Strength of Subsurface Scattering (default 0).                                                   |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| out vec3 **TRANSMISSION**        | Transmission mask (default 0,0,0).                                                               |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| out foat **AO**                  | Ambient Occlusion (pre-baked).                                                                   |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| out float **AO_LIGHT_AFFECT**    | How much AO affects lights (0..1. default 0, none).                                              |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| out vec3 **EMISSION**            | Emission color (can go over 1,1,1 for HDR).                                                      |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| in sampler2D **SCREEN_TEXTURE**  | Built-in Texture for reading from the screen. Mipmaps contain increasingly blurred copies.       |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| in sampler2D **DEPTH_TEXTURE**   | Built-in Texture for reading depth from the screen. Must convert to linear using INV_PROJECTION. |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| in vec2 **SCREEN_UV**            | Screen UV coordinate for current pixel.                                                          |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| in vec2 **POINT_COORD**          | Point Coord for drawing points with POINT_SIZE.                                                  |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| in float **SIDE**                | SIDE multiplier, for double sided materials.                                                     |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| out float **ALPHA_SCISSOR**      | If written to, values below a certain amount of alpha are discarded.                             |
+----------------------------------+--------------------------------------------------------------------------------------------------+


Values marked as "in" are read-only. Values marked as "out" are for optional writing. If nothing is written, a default value is used.

Light Built-Ins
^^^^^^^^^^^^^^^

+-----------------------------------+------------------------------------------+
| Built-in                          | Description                              |
+===================================+==========================================+
| in mat4 **WORLD_MATRIX**          | Model space to world space transform.    |
+-----------------------------------+------------------------------------------+
| in mat4 **INV_CAMERA_MATRIX**     | World space to view space transform.     |
+-----------------------------------+------------------------------------------+
| in mat4 **PROJECTION_MATRIX**     | View space to clip space transform.      |
+-----------------------------------+------------------------------------------+
| in mat4 **CAMERA_MATRIX**         | View space to world space transform.     |
+-----------------------------------+------------------------------------------+
| in mat4 **INV_PROJECTION_MATRIX** | Clip space to view space transform.      |
+-----------------------------------+------------------------------------------+
| in float **TIME**                 | Elapsed total time in seconds.           |
+-----------------------------------+------------------------------------------+
| in vec2 **VIEWPORT_SIZE**         | Size of viewport (in pixels).            |
+-----------------------------------+------------------------------------------+
| in vec3 **NORMAL**                | Normal vector.                           |
+-----------------------------------+------------------------------------------+
| in vec3 **VIEW**                  | View vector.                             |
+-----------------------------------+------------------------------------------+
| in vec3  **LIGHT**                | Light Vector.                            |
+-----------------------------------+------------------------------------------+
| in vec3 **LIGHT_COLOR**           | Color of light multiplied by energy.     |
+-----------------------------------+------------------------------------------+
| in vec3 **ATTENUATION**           | Attenuation based on distance or shadow. |
+-----------------------------------+------------------------------------------+
| in vec3 **ALBEDO**                | Base albedo.                             |
+-----------------------------------+------------------------------------------+
| in vec3 **TRANSMISSION**          | Transmission mask.                       |
+-----------------------------------+------------------------------------------+
| in float **ROUGHNESS**            | Roughness.                               |
+-----------------------------------+------------------------------------------+
| out vec3 **DIFFUSE_LIGHT**        | Diffuse light result.                    |
+-----------------------------------+------------------------------------------+
| out vec3 **SPECULAR_LIGHT**       | Specular light result.                   |
+-----------------------------------+------------------------------------------+

Writing light shaders is completely optional. Unlike other game engines, they don't affect
performance or force a specific pipeline.

To write a light shader, simply make sure to assign something to DIFFUSE_LIGHT or SPECULAR_LIGHT.
Assigning nothing means no light is processed.


Canvas Item
~~~~~~~~~~~~

Accepted render modes and built-ins for "shader_type canvas_item;".

Render Modes
^^^^^^^^^^^^

+---------------------------------+----------------------------------------------------------------------+
| Render Mode                     | Description                                                          |
+=================================+======================================================================+
| **blend_mix**                   | Mix blend mode (alpha is transparency), default.                     |
+---------------------------------+----------------------------------------------------------------------+
| **blend_add**                   | Additive blend mode.                                                 |
+---------------------------------+----------------------------------------------------------------------+
| **blend_sub**                   | Subtractive blend mode.                                              |
+---------------------------------+----------------------------------------------------------------------+
| **blend_mul**                   | Multiplicative blend mode.                                           |
+---------------------------------+----------------------------------------------------------------------+
| **blend_premul_alpha**          | Premultiplied alpha blend mode.                                      |
+---------------------------------+----------------------------------------------------------------------+
| **unshaded**                    | Result is just albedo. No lighting/shading happens in material.      |
+---------------------------------+----------------------------------------------------------------------+
| **light_only**                  | Only draw for light pass (when multipass is used).                   |
+---------------------------------+----------------------------------------------------------------------+
| **skip_vertex_transform**       | VERTEX/NORMAL/etc need to be transformed manually in VS.             |
+---------------------------------+----------------------------------------------------------------------+

Vertex Built-Ins
^^^^^^^^^^^^^^^^

+--------------------------------+----------------------------------------------------------------+
| Built-In                       | Description                                                    |
+================================+================================================================+
| in mat4 **WORLD_MATRIX**       | Image to World transform.                                      |
+--------------------------------+----------------------------------------------------------------+
| in mat4 **EXTRA_MATRIX**       | Extra transform.                                               |
+--------------------------------+----------------------------------------------------------------+
| in mat4 **PROJECTION_MATRIX**  | World to view transform.                                       |
+--------------------------------+----------------------------------------------------------------+
| in float **TIME**              | Global time, in seconds.                                       |
+--------------------------------+----------------------------------------------------------------+
| in vec4 **INSTANCE_CUSTOM**    | Instance custom data.                                          |
+--------------------------------+----------------------------------------------------------------+
| in bool **AT_LIGHT_PASS**      | True if this is a light pass (for multi-pass light rendering). |
+--------------------------------+----------------------------------------------------------------+
| inout vec2 **VERTEX**          | Vertex in image space.                                         |
+--------------------------------+----------------------------------------------------------------+
| inout vec2 **UV**              | UV.                                                            |
+--------------------------------+----------------------------------------------------------------+
| inout vec4 **COLOR**           | Color from vertex primitive.                                   |
+--------------------------------+----------------------------------------------------------------+
| out vec2 **POINT_SIZE**        | Point size for point drawing.                                  |
+--------------------------------+----------------------------------------------------------------+


Vertex data (VERTEX) is presented in local space.
If not written to, these values will not be modified and be passed through as they came.

It is possible to completely disable the built-in modelview transform (projection will still
happen later, though) with the following code, so it can be done manually:

.. code-block:: glsl

    shader_type spatial;
    render_mode skip_vertex_transform;

    void vertex() {

        VERTEX = (EXTRA_MATRIX * (WORLD_MATRIX * vec4(VERTEX, 0.0, 1.0))).xy;
    }


Other built-ins such as UV and COLOR are also passed through to the fragment function if not modified.

For instancing, the INSTANCE_CUSTOM variable contains the instance custom data. When using particles, this information
is usually:

* **x**: Rotation angle in radians.
* **y**: Phase during lifetime (0 to 1).
* **z**: Animation frame.

This allows to easily adjust the shader to a particle system using default particles material. When writing a custom particles
shader, this value can be used as desired.

Fragment Built-Ins
^^^^^^^^^^^^^^^^^^

+----------------------------------+------------------------------------------------------------+
| Built-In                         | Description                                                |
+==================================+============================================================+
| in vec4 **FRAGCOORD**            | Fragment coordinate, pixel adjusted.                       |
+----------------------------------+------------------------------------------------------------+
| out  vec3 **NORMAL**             | Normal, writable.                                          |
+----------------------------------+------------------------------------------------------------+
| out vec3 **NORMALMAP**           | Normal from texture, default is read from NORMAL_TEXTURE.  |
+----------------------------------+------------------------------------------------------------+
| out float **NORMALMAP_DEPTH**    | Normalmap depth for scaling.                               |
+----------------------------------+------------------------------------------------------------+
| in vec2 **UV**                   | UV from vertex function.                                   |
+----------------------------------+------------------------------------------------------------+
| out vec4 **COLOR**               | Color from vertex function.                                |
+----------------------------------+------------------------------------------------------------+
| in sampler2D **TEXTURE**         | Default 2D texture.                                        |
+----------------------------------+------------------------------------------------------------+
| in sampler2D **NORMAL_TEXTURE**  | Default 2D normal texture.                                 |
+----------------------------------+------------------------------------------------------------+
| in vec2 **TEXTURE_PIXEL_SIZE**   | Default 2D texture pixel size.                             |
+----------------------------------+------------------------------------------------------------+
| in vec2 **SCREEN_UV**            | Screen UV for use with SCREEN_TEXTURE.                     |
+----------------------------------+------------------------------------------------------------+
| in vec2 **SCREEN_PIXEL_SIZE**    | Screen pixel size.                                         |
+----------------------------------+------------------------------------------------------------+
| in vec2 **POINT_COORD**          | Coordinate for drawing points.                             |
+----------------------------------+------------------------------------------------------------+
| in float **TIME**                | Global time in seconds.                                    |
+----------------------------------+------------------------------------------------------------+
| in sampler2D **SCREEN_TEXTURE**  | Screen texture, mipmaps contain gaussian blurred versions. |
+----------------------------------+------------------------------------------------------------+

Light Built-Ins
^^^^^^^^^^^^^^^^

+-------------------------------------+-------------------------------------------------------------------------------+
| Built-In                            | Description                                                                   |
+=====================================+===============================================================================+
| in vec4 **POSITION**                | Screen Position.                                                              |
+-------------------------------------+-------------------------------------------------------------------------------+
| in vec3 **NORMAL**                  | Input Normal.                                                                 |
+-------------------------------------+-------------------------------------------------------------------------------+
| in vec2 **UV**                      | UV.                                                                           |
+-------------------------------------+-------------------------------------------------------------------------------+
| in vec4 **COLOR**                   | Input Color.                                                                  |
+-------------------------------------+-------------------------------------------------------------------------------+
| in sampler2D **TEXTURE**            | Current texture in use for CanvasItem.                                        |
+-------------------------------------+-------------------------------------------------------------------------------+
| in vec2 **TEXTURE_PIXEL_SIZE**      | Pixel size for current 2D texture.                                            |
+-------------------------------------+-------------------------------------------------------------------------------+
| in vec2 **SCREEN_UV**               | Screen Texture Coordinate (for using with texscreen).                         |
+-------------------------------------+-------------------------------------------------------------------------------+
| in vec2 **POINT_COORD**             | Current UV for Point Sprite.                                                  |
+-------------------------------------+-------------------------------------------------------------------------------+
| in float **TIME**                   | Time (in seconds).                                                            |
+-------------------------------------+-------------------------------------------------------------------------------+
| vec2 **LIGHT\_VEC**                 | Vector from light to fragment, can be modified to alter shadow computation.   |
+-------------------------------------+-------------------------------------------------------------------------------+
| in float **LIGHT\_HEIGHT**          | Height of Light.                                                              |
+-------------------------------------+-------------------------------------------------------------------------------+
| in color **LIGHT\_COLOR**           | Color of Light.                                                               |
+-------------------------------------+-------------------------------------------------------------------------------+
| in color **LIGHT\_SHADOW\_COLOR**   | Color of Light shadow.                                                        |
+-------------------------------------+-------------------------------------------------------------------------------+
| in vec2 **LIGHT\_UV**               | UV for light image.                                                           |
+-------------------------------------+-------------------------------------------------------------------------------+
| in vec4 **SHADOW**                  | Light shadow color override.                                                  |
+-------------------------------------+-------------------------------------------------------------------------------+
| out vec4 **LIGHT**                  | Light Output (shader is ignored if this is not used).                         |
+-------------------------------------+-------------------------------------------------------------------------------+


Particles
~~~~~~~~~

Accepted render modes and built-ins for "shader_type particles;".

Render Modes
^^^^^^^^^^^^

+---------------------------------+----------------------------------------------------------------------+
| Render Mode                     | Description                                                          |
+=================================+======================================================================+
| **billboard**                   | Particle will be shown as a billboard.                               |
+---------------------------------+----------------------------------------------------------------------+
| **keep_data**                   | Do not clear previous data on restart.                               |
+---------------------------------+----------------------------------------------------------------------+

Vertex Built-Ins
^^^^^^^^^^^^^^^^

+---------------------------------+-----------------------------------------------------------+
| Built-In                        | Description                                               |
+=================================+===========================================================+
| inout vec4 **COLOR**            | Particle color, can be written to.                        |
+---------------------------------+-----------------------------------------------------------+
| inout vec3 **VELOCITY**         | Particle velocity, can be modified.                       |
+---------------------------------+-----------------------------------------------------------+
| out float **MASS**              | Particle mass, use for attractors (default 1).            |
+---------------------------------+-----------------------------------------------------------+
| inout bool **ACTIVE**           | Particle is active, can be set to false.                  |
+---------------------------------+-----------------------------------------------------------+
| in bool **RESTART**             | Set to true when particle must restart (lifetime cycled). |
+---------------------------------+-----------------------------------------------------------+
| inout vec4 **CUSTOM**           | Custom particle data.                                     |
+---------------------------------+-----------------------------------------------------------+
| inout mat4 **TRANSFORM**        | Particle transform.                                       |
+---------------------------------+-----------------------------------------------------------+
| in float **TIME**               | Global time in seconds.                                   |
+---------------------------------+-----------------------------------------------------------+
| in float **DELTA**              | Delta process time.                                       |
+---------------------------------+-----------------------------------------------------------+
| in uint **NUMBER**              | Unique number since emission start.                       |
+---------------------------------+-----------------------------------------------------------+
| in int **INDEX**                | Particle index (from total particles).                    |
+---------------------------------+-----------------------------------------------------------+
| in mat4 **EMISSION_TRANSFORM**  | Emitter transform (used for non-local systems).           |
+---------------------------------+-----------------------------------------------------------+
| in uint **RANDOM_SEED**         | Random seed used as base for random.                      |
+---------------------------------+-----------------------------------------------------------+

Particle shades only support vertex processing. They are drawn with any regular material for CanvasItem or Spatial, depending on
whether they are 2D or 3D.
