.. _doc_shading_language:

Shading language
================

Introduction
------------

Godot uses a shading language similar to GLSL ES 3.0. Most datatypes and functions are supported,
and the few remaining ones will likely be added over time.

Unlike the shader language in Godot 2.x, this implementation is much closer to the original.

Shader Types
------------

Instead of supplying a general purpose configuration, Godot Shading Language must
specify what a shader is intended for. Depending on the type, different render
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

Data types
----------

Most GLSL ES 3.0 datatypes are supported:

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

Just like GLSL ES 3.0, implicit casting between scalars and vectors of the same size but different type is not allowed.
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

For matrices, use m[row][column] indexing syntax to access each scalar, or m[idx] for access a vector by row index. For example, for accessing y position of object in mat4 you must use m[3][1] syntax.

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

Construction of matrix types requires pass vectors of same dimension as matrix. You could also build a diagonal matrix using matx(float) syntax. So the mat4(1.0) is an identity matrix.

.. code-block:: glsl

    mat2 m2 = mat2(vec2(1.0, 0.0), vec2(0.0, 1.0));
    mat3 m3 = mat3(vec3(1.0, 0.0, 0.0), vec3(0.0, 1.0, 0.0), vec3(0.0, 0.0, 1.0));
    mat4 identity = mat4(1.0);

Matrix can also been builded from matrix of another dimension.
There are two rules :
If a larger matrix is constructed from a smaller matrix, the additional rows and columns are set to the values they would have in an identity matrix.
If a smaller matrix is constructed from a larger matrix, the top, left submatrix of the larger matrix is chosen.

.. code-block:: glsl
	
	mat3 basis = mat3(WORLD_MATRIX);
	mat4 m4 = mat4(basis);
	mat2 m2 = mat2(m4);

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
Please read the relevant documentation on the target architecture to find out more. In all honesty though, mobile drivers are buggy
so to stay out of trouble make simple shaders without specifying precision unless you *really* need to.

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
    for (int i = 0; i < 10; i++) {

    }

    // while
    while (true) {

    }


Keep in mind that, in modern GPUs, an infinite loop can exist and can freeze your application (including editor).
Godot can't protect you from this, so be careful to not make this mistake!

Discarding
-----------

Fragment and light functions can use the **discard** keyword. If used, the fragment is discarded and nothing is written.

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
        DIFFUSE_LIGHT = vec3(0.0, 1.0, 0.0);
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

Interpolation qualifiers
~~~~~~~~~~~~~~~~~~~~~~~~

Certain values are interpolated during the shading pipeline. You can modify how these interpolations
are done by using *interpolation qualifiers*.

.. code-block:: glsl

    shader_type spatial;

    varying flat vec3 our_color;

    void vertex() {
        our_color = COLOR.rgb;
    }

    void fragment() {
        ALBEDO = our_color;
    }

There are three possible interpolation qualifiers:

+-------------------+---------------------------------------------------------------------------------+
| Qualifier         | Description                                                                     |
+===================+=================================================================================+
| **flat**          | The value is not interpolated                                                   |
+-------------------+---------------------------------------------------------------------------------+
| **noperspective** | The value is linearly interpolated in window-space                              |
+-------------------+---------------------------------------------------------------------------------+
| **smooth**        | The value is interpolated in a perspective-correct fashion. This is the default |
+-------------------+---------------------------------------------------------------------------------+


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
    uniform vec4 other_color : hint_color = vec4(1.0);

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
    uniform vec4 some_color : hint_color = vec4(1.0);

Built-in Functions
------------------

A large number of built-in functions are supported, conforming mostly to GLSL ES 3.0.
When vec_type (float), vec_int_type, vec_uint_type, vec_bool_type nomenclature is used, it can be scalar or vector.

+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| Function                                                                                      | Description                                    |
+===============================================================================================+================================================+
| vec_type **radians** ( vec_type )                                                             | Convert degrees to radians                     |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_type **degrees** ( vec_type )                                                             | Convert radians to degrees                     |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_type **sin** ( vec_type )                                                                 | Sine                                           |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_type **cos** ( vec_type )                                                                 | Cosine                                         |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_type **tan** ( vec_type )                                                                 | Tangent                                        |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_type **asin** ( vec_type )                                                                | Arc-Sine                                       |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_type **acos** ( vec_type )                                                                | Arc-Cosine                                     |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_type **atan** ( vec_type )                                                                | Arc-Tangent                                    |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_type **atan** ( vec_type x, vec_type y )                                                  | Arc-Tangent to convert vector to angle         |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_type **sinh** ( vec_type )                                                                | Hyperbolic-Sine                                |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_type **cosh** ( vec_type )                                                                | Hyperbolic-Cosine                              |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_type **tanh** ( vec_type )                                                                | Hyperbolic-Tangent                             |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_type **asinh** ( vec_type )                                                               | Inverse-Hyperbolic-Sine                        |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_type **acosh** ( vec_type )                                                               | Inverse-Hyperbolic-Cosine                      |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_type **atanh** ( vec_type )                                                               | Inverse-Hyperbolic-Tangent                     |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_type **pow** ( vec_type, vec_type )                                                       | Power                                          |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_type **exp** ( vec_type )                                                                 | Base-e Exponential                             |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_type **exp2** ( vec_type )                                                                | Base-2 Exponential                             |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_type **log** ( vec_type )                                                                 | Natural Logarithm                              |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_type **log2** ( vec_type )                                                                | Base-2 Logarithm                               |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_type **sqrt** ( vec_type )                                                                | Square Root                                    |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_type **inversesqrt** ( vec_type )                                                         | Inverse Square Root                            |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_type **abs** ( vec_type )                                                                 | Absolute                                       |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_int_type **abs** ( vec_int_type )                                                         | Absolute                                       |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_type **sign** ( vec_type )                                                                | Sign                                           |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_int_type **sign** ( vec_int_type )                                                        | Sign                                           |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_type **floor** ( vec_type )                                                               | Floor                                          |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_type **round** ( vec_type )                                                               | Round                                          |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_type **roundEven** ( vec_type )                                                           | Round nearest even                             |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_type **trunc** ( vec_type )                                                               | Truncation                                     |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_type **ceil** ( vec_type )                                                                | Ceiling                                        |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_type **fract** ( vec_type )                                                               | Fractional                                     |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_type **mod** ( vec_type, vec_type )                                                       | Remainder                                      |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_type **mod** ( vec_type, float )                                                          | Remainder                                      |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_type **modf** ( vec_type x, out vec_type i )                                              | Fractional of x, with i has integer part       |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_scalar_type **min** ( vec_scalar_type a, vec_scalar_type b )                              | Minimum                                        |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_scalar_type **max** ( vec_scalar_type a, vec_scalar_type b )                              | Maximum                                        |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_scalar_type **clamp** ( vec_scalar_type value, vec_scalar_type min, vec_scalar_type max ) | Clamp to Min-Max                               |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_type **mix** ( vec_type a, vec_type b, float c )                                          | Linear Interpolate (Scalar Coef.)              |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_type **mix** ( vec_type a, vec_type b, vec_type c )                                       | Linear Interpolate (Vector Coef.)              |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_type **mix** ( vec_type a, vec_type b, bool c )                                           | Linear Interpolate (Bool Selection)            |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_type **mix** ( vec_type a, vec_type b, vec_bool_type c )                                  | Linear Interpolate (Bool-Vector Selection)     |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_type **step** ( vec_type a, vec_type b )                                                  | \` b[i] < a[i] ? 0.0 : 1.0 \`                  |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_type **step** ( float a, vec_type b )                                                     | \` b[i] < a ? 0.0 : 1.0 \`                     |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_type **smoothstep** ( vec_type a, vec_type b, vec_type c )                                | Hermite Interpolate                            |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_type **smoothstep** ( float a, float b, vec_type c )                                      | Hermite Interpolate                            |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_bool_type **isnan** ( vec_type )                                                          | Scalar, or vector component being nan          |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_bool_type **isinf** ( vec_type )                                                          | Scalar, or vector component being inf          |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_int_type **floatBitsToInt** ( vec_type )                                                  | Float->Int bit copying, no conversion          |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_uint_type **floatBitsToUint** ( vec_type )                                                | Float->UInt bit copying, no conversion         |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_type **intBitsToFloat** ( vec_int_type )                                                  | Int->Float bit copying, no conversion          |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_type **uintBitsToFloat** ( vec_uint_type )                                                | UInt->Float bit copying, no conversion         |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| float **length** ( vec_type )                                                                 | Vector Length                                  |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| float **distance** ( vec_type, vec_type )                                                     | Distance between vector                        |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| float **dot** ( vec_type, vec_type )                                                          | Dot Product                                    |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec3 **cross** ( vec3, vec3 )                                                                 | Cross Product                                  |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_type **normalize** ( vec_type )                                                           | Normalize to unit length                       |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec3 **reflect** ( vec3 I, vec3 N )                                                           | Reflect                                        |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec3 **refract** ( vec3 I, vec3 N, float eta )                                                | Refract                                        |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_type **faceforward** ( vec_type N, vec_type I, vec_type Nref )                            | If dot(Nref, I) < 0 return N, otherwise –N     |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| mat_type **matrixCompMult** ( mat_type, mat_type )                                            | Matrix Component Multiplication                |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| mat_type **outerProduct** ( vec_type, vec_type )                                              | Matrix Outer Product                           |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| mat_type **transpose** ( mat_type )                                                           | Transpose Matrix                               |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| float **determinant** ( mat_type )                                                            | Matrix Determinant                             |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| mat_type **inverse** ( mat_type )                                                             | Inverse Matrix                                 |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_bool_type **lessThan** ( vec_scalar_type, vec_scalar_type )                               | Bool vector cmp on < int/uint/float vectors    |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_bool_type **greaterThan** ( vec_scalar_type, vec_scalar_type )                            | Bool vector cmp on > int/uint/float vectors    |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_bool_type **lessThanEqual** ( vec_scalar_type, vec_scalar_type )                          | Bool vector cmp on <= int/uint/float vectors   |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_bool_type **greaterThanEqual** ( vec_scalar_type, vec_scalar_type )                       | Bool vector cmp on >= int/uint/float vectors   |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_bool_type **equal** ( vec_scalar_type, vec_scalar_type )                                  | Bool vector cmp on == int/uint/float vectors   |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_bool_type **notEqual** ( vec_scalar_type, vec_scalar_type )                               | Bool vector cmp on != int/uint/float vectors   |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| bool **any** ( vec_bool_type )                                                                | Any component is true                          |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| bool **all** ( vec_bool_type )                                                                | All components are true                        |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| bool **not** ( vec_bool_type )                                                                | No components are true                         |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| ivec2 **textureSize** ( sampler2D_type s, int lod )                                           | Get the size of a texture                      |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| ivec2 **textureSize** ( samplerCube s, int lod )                                              | Get the size of a cubemap                      |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec4_type **texture** ( sampler2D_type s, vec2 uv [, float bias] )                            | Perform a 2D texture read                      |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec4_type **texture** ( samplerCube s, vec3 uv [, float bias] )                               | Perform a Cube texture read                    |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec4_type **textureProj** ( sampler2D_type s, vec3 uv [, float bias] )                        | Perform a texture read with projection         |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec4_type **textureProj** ( sampler2D_type s, vec4 uv [, float bias] )                        | Perform a texture read with projection         |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec4_type **textureLod** ( sampler2D_type s, vec2 uv, float lod )                             | Perform a 2D texture read at custom mipmap     |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec4_type **textureLod** ( samplerCube s, vec3 uv, float lod )                                | Perform a Cube texture read at custom mipmap   |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec4_type **textureProjLod** ( sampler2D_type s, vec3 uv, float lod )                         | Perform a texture read with projection/lod     |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec4_type **textureProjLod** ( sampler2D_type s, vec4 uv, float lod )                         | Perform a texture read with projection/lod     |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec4_type **texelFetch** ( sampler2D_type s, ivec2 uv, int lod )                              | Fetch a single texel using integer coords      |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_type **dFdx** ( vec_type )                                                                | Derivative in x using local differencing       |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_type **dFdy** ( vec_type )                                                                | Derivative in y using local differencing       |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_type **fwidth** ( vec_type )                                                              | Sum of absolute derivative in x and y          |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+



Shader Types In-Depth
---------------------

Spatial
~~~~~~~

Accepted render modes and built-ins for **shader_type spatial;**.

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
| **diffuse_toon**                | Toon shading for diffuse.                                            |
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

+------------------------------------+-------------------------------------------------------+
| Built-In                           | Description                                           |
+====================================+=======================================================+
| out mat4 **WORLD_MATRIX**          | Model space to world space transform.                 |
+------------------------------------+-------------------------------------------------------+
| in mat4 **INV_CAMERA_MATRIX**      | World space to view space transform.                  |
+------------------------------------+-------------------------------------------------------+
| out mat4 **PROJECTION_MATRIX**     | View space to clip space transform.                   |
+------------------------------------+-------------------------------------------------------+
| in mat4 **CAMERA_MATRIX**          | View space to world space transform.                  |
+------------------------------------+-------------------------------------------------------+
| out mat4 **MODELVIEW_MATRIX**      | Model space to view space transform (use if possible).|
+------------------------------------+-------------------------------------------------------+
| out mat4 **INV_PROJECTION_MATRIX** | Clip space to view space transform.                   |
+------------------------------------+-------------------------------------------------------+
| in float **TIME**                  | Elapsed total time in seconds.                        |
+------------------------------------+-------------------------------------------------------+
| in vec2 **VIEWPORT_SIZE**          | Size of viewport (in pixels).                         |
+------------------------------------+-------------------------------------------------------+
| out vec3 **VERTEX**                | Vertex in local coords (see doc below).               |
+------------------------------------+-------------------------------------------------------+
| out vec3 **NORMAL**                | Normal in local coords.                               |
+------------------------------------+-------------------------------------------------------+
| out vec3 **TANGENT**               | Tangent in local coords.                              |
+------------------------------------+-------------------------------------------------------+
| out vec3 **BINORMAL**              | Binormal in local coords.                             |
+------------------------------------+-------------------------------------------------------+
| out vec2 **UV**                    | UV main channel.                                      |
+------------------------------------+-------------------------------------------------------+
| out vec2 **UV2**                   | UV secondary channel.                                 |
+------------------------------------+-------------------------------------------------------+
| out vec4 **COLOR**                 | Color from vertices.                                  |
+------------------------------------+-------------------------------------------------------+
| out float **POINT_SIZE**           | Point size for point rendering.                       |
+------------------------------------+-------------------------------------------------------+
| in int **INSTANCE_ID**             | Instance ID for instancing.                           |
+------------------------------------+-------------------------------------------------------+
| in vec4 **INSTANCE_CUSTOM**        | Instance custom data (for particles, mostly).         |
+------------------------------------+-------------------------------------------------------+
| out float **ROUGHNESS**            | Roughness for vertex lighting.                        |
+------------------------------------+-------------------------------------------------------+

Values marked as "in" are read-only. Values marked as "out" are for optional writing. Samplers are not subjects of writing and they are not marked.

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
        NORMAL = (MODELVIEW_MATRIX * vec4(NORMAL, 0.0)).xyz;
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
| in vec4 **FRAGCOORD**            | Fragment coordinate, pixel adjusted.                                                             |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| in mat4 **WORLD_MATRIX**         | Model space to world space transform.                                                            |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| in mat4 **INV_CAMERA_MATRIX**    | World space to view space transform.                                                             |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| in mat4 **PROJECTION_MATRIX**    | View space to clip space transform.                                                              |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| in mat4 **INV_PROJECTION_MATRIX**| Clip space to view space transform.                                                              |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| in float **TIME**                | Elapsed total time in seconds.                                                                   |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| in vec2 **VIEWPORT_SIZE**        | Size of viewport (in pixels).                                                                    |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| in vec3 **VERTEX**               | Vertex that comes from vertex function, in view space.                                           |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| in bool **FRONT_FACING**         | true whether current face is front face.                                                         |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| out vec3 **NORMAL**              | Normal that comes from vertex function, in view space.                                           |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| out vec3 **TANGENT**             | Tangent that comes from vertex function.                                                         |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| out vec3 **BINORMAL**            | Binormal that comes from vertex function.                                                        |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| out vec3 **NORMALMAP**           | Output this if reading normal from a texture instead of NORMAL.                                  |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| out float **NORMALMAP_DEPTH**    | Depth from variable above. Defaults to 1.0.                                                      |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| in vec2 **UV**                   | UV that comes from vertex function.                                                              |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| in vec2 **UV2**                  | UV2 that comes from vertex function.                                                             |
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
| out vec2 **ANISOTROPY_FLOW**     | Distortion direction, use with flowmaps.                                                         |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| out float **SSS_STRENGTH**       | Strength of Subsurface Scattering (default 0).                                                   |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| out vec3 **TRANSMISSION**        | Transmission mask (default 0,0,0).                                                               |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| out float **AO**                 | Ambient Occlusion (pre-baked).                                                                   |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| out float **AO_LIGHT_AFFECT**    | How much AO affects lights (0..1. default 0, none).                                              |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| out vec3 **EMISSION**            | Emission color (can go over 1,1,1 for HDR).                                                      |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| sampler2D **SCREEN_TEXTURE**     | Built-in Texture for reading from the screen. Mipmaps contain increasingly blurred copies.       |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| sampler2D **DEPTH_TEXTURE**      | Built-in Texture for reading depth from the screen. Must convert to linear using INV_PROJECTION. |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| out vec2 **SCREEN_UV**           | Screen UV coordinate for current pixel.                                                          |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| in vec2 **POINT_COORD**          | Point Coord for drawing points with POINT_SIZE.                                                  |
+----------------------------------+--------------------------------------------------------------------------------------------------+
| out float **ALPHA_SCISSOR**      | If written to, values below a certain amount of alpha are discarded.                             |
+----------------------------------+--------------------------------------------------------------------------------------------------+

Light Built-Ins
^^^^^^^^^^^^^^^

+-----------------------------------+------------------------------------------+
| Built-in                          | Description                              |
+===================================+==========================================+
| in vec4 **FRAGCOORD**             | Fragment coordinate, pixel adjusted.     |
+-----------------------------------+------------------------------------------+
| in mat4 **WORLD_MATRIX**          | Model space to world space transform.    |
+-----------------------------------+------------------------------------------+
| in mat4 **INV_CAMERA_MATRIX**     | World space to view space transform.     |
+-----------------------------------+------------------------------------------+
| in mat4 **PROJECTION_MATRIX**     | View space to clip space transform.      |
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
| in vec3 **LIGHT**                 | Light Vector.                            |
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

Accepted render modes and built-ins for **shader_type canvas_item;**.

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
| out vec2 **VERTEX**            | Vertex in image space.                                         |
+--------------------------------+----------------------------------------------------------------+
| out vec2 **UV**                | UV.                                                            |
+--------------------------------+----------------------------------------------------------------+
| out vec4 **COLOR**             | Color from vertex primitive.                                   |
+--------------------------------+----------------------------------------------------------------+
| out float **POINT_SIZE**       | Point size for point drawing.                                  |
+--------------------------------+----------------------------------------------------------------+

Vertex data (VERTEX) is presented in local space.
If not written to, these values will not be modified and be passed through as they came.

It is possible to completely disable the built-in modelview transform (projection will still
happen later, though) with the following code, so it can be done manually:

.. code-block:: glsl

    shader_type canvas_item;
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

+----------------------------------+----------------------------------------------------------------+
| Built-In                         | Description                                                    |
+==================================+================================================================+
| in vec4 **FRAGCOORD**            | Fragment coordinate, pixel adjusted.                           |
+----------------------------------+----------------------------------------------------------------+
| out vec3 **NORMAL**              | Normal, writable.                                              |
+----------------------------------+----------------------------------------------------------------+
| out vec3 **NORMALMAP**           | Normal from texture, default is read from NORMAL_TEXTURE.      |
+----------------------------------+----------------------------------------------------------------+
| out float **NORMALMAP_DEPTH**    | Normalmap depth for scaling.                                   |
+----------------------------------+----------------------------------------------------------------+
| in vec2 **UV**                   | UV from vertex function.                                       |
+----------------------------------+----------------------------------------------------------------+
| out vec4 **COLOR**               | Color from vertex function.                                    |
+----------------------------------+----------------------------------------------------------------+
| sampler2D **TEXTURE**            | Default 2D texture.                                            |
+----------------------------------+----------------------------------------------------------------+
| sampler2D **NORMAL_TEXTURE**     | Default 2D normal texture.                                     |
+----------------------------------+----------------------------------------------------------------+
| in vec2 **TEXTURE_PIXEL_SIZE**   | Normalized pixel size of default 2D texture.                   |
|                                  | For a Sprite with a texture of size 64x32px,                   |
|                                  | **TEXTURE_PIXEL_SIZE** = :code:`vec2(1/64, 1/32)`              |
+----------------------------------+----------------------------------------------------------------+
| in vec2 **SCREEN_UV**            | Screen UV for use with SCREEN_TEXTURE.                         |
+----------------------------------+----------------------------------------------------------------+
| in vec2 **SCREEN_PIXEL_SIZE**    | Size of individual pixels. Equal to inverse of resolution.     |
+----------------------------------+----------------------------------------------------------------+
| in vec2 **POINT_COORD**          | Coordinate for drawing points.                                 |
+----------------------------------+----------------------------------------------------------------+
| in float **TIME**                | Global time in seconds.                                        |
+----------------------------------+----------------------------------------------------------------+
| in bool **AT_LIGHT_PASS**        | True if this is a light pass (for multi-pass light rendering). |
+----------------------------------+----------------------------------------------------------------+
| sampler2D **SCREEN_TEXTURE**     | Screen texture, mipmaps contain gaussian blurred versions.     |
+----------------------------------+----------------------------------------------------------------+

Light Built-Ins
^^^^^^^^^^^^^^^^

+-------------------------------------+-------------------------------------------------------------------------------+
| Built-In                            | Description                                                                   |
+=====================================+===============================================================================+
| in vec4 **FRAGCOORD**               | Fragment coordinate, pixel adjusted.                                          |
+-------------------------------------+-------------------------------------------------------------------------------+
| in vec3 **NORMAL**                  | Input Normal. Although this value is passed in,                               |
|                                     | **normal calculation still happens outside of this function**.                |
+-------------------------------------+-------------------------------------------------------------------------------+
| in vec2 **UV**                      | UV from vertex function, equivalent to the UV in the fragment function.       |
+-------------------------------------+-------------------------------------------------------------------------------+
| in vec4 **COLOR**                   | Input Color.                                                                  |
|                                     | This is the output of the fragment function with final modulation applied.    |
+-------------------------------------+-------------------------------------------------------------------------------+
| sampler2D **TEXTURE**               | Current texture in use for CanvasItem.                                        |
+-------------------------------------+-------------------------------------------------------------------------------+
| in vec2 **TEXTURE_PIXEL_SIZE**      | Normalized pixel size of default 2D texture.                                  |
|                                     | For a Sprite with a texture of size 64x32px,                                  |
|                                     | **TEXTURE_PIXEL_SIZE** = :code:`vec2(1/64, 1/32)`                             |
+-------------------------------------+-------------------------------------------------------------------------------+
| in vec2 **SCREEN_UV**               | Screen Texture Coordinate (for using with screen texture).                    |
+-------------------------------------+-------------------------------------------------------------------------------+
| in vec2 **POINT_COORD**             | Current UV for Point Sprite.                                                  |
+-------------------------------------+-------------------------------------------------------------------------------+
| in float **TIME**                   | Global time in seconds.                                                       |
+-------------------------------------+-------------------------------------------------------------------------------+
| out vec2 **LIGHT_VEC**              | Vector from light to fragment, can be modified to alter shadow computation.   |
+-------------------------------------+-------------------------------------------------------------------------------+
| out float **LIGHT_HEIGHT**          | Height of Light.                                                              |
+-------------------------------------+-------------------------------------------------------------------------------+
| out vec4 **LIGHT_COLOR**            | Color of Light.                                                               |
+-------------------------------------+-------------------------------------------------------------------------------+
| out vec2 **LIGHT_UV**               | UV for Light texture.                                                         |
+-------------------------------------+-------------------------------------------------------------------------------+
| out vec4 **SHADOW_COLOR**           | Shadow Color of Light. **(not yet implemented)**                              |
+-------------------------------------+-------------------------------------------------------------------------------+
| out vec4 **LIGHT**                  | Value from the Light texture. **(shader is ignored if this is not used).**    |
|                                     | Can be modified.                                                              |
+-------------------------------------+-------------------------------------------------------------------------------+

Particles
~~~~~~~~~

Accepted render modes and built-ins for **shader_type particles;**.

Render Modes
^^^^^^^^^^^^

+---------------------------------+----------------------------------------------------------------------+
| Render Mode                     | Description                                                          |
+=================================+======================================================================+
| **keep_data**                   | Do not clear previous data on restart.                               |
+---------------------------------+----------------------------------------------------------------------+
| **disable_force**               | Disable force.                                                       |
+---------------------------------+----------------------------------------------------------------------+
| **disable_velocity**            | Disable velocity.                                                    |
+---------------------------------+----------------------------------------------------------------------+

Vertex Built-Ins
^^^^^^^^^^^^^^^^

+---------------------------------+-----------------------------------------------------------+
| Built-In                        | Description                                               |
+=================================+===========================================================+
| out vec4 **COLOR**              | Particle color, can be written to.                        |
+---------------------------------+-----------------------------------------------------------+
| out vec3 **VELOCITY**           | Particle velocity, can be modified.                       |
+---------------------------------+-----------------------------------------------------------+
| out float **MASS**              | Particle mass, use for attractors (default 1).            |
+---------------------------------+-----------------------------------------------------------+
| out bool **ACTIVE**             | Particle is active, can be set to false.                  |
+---------------------------------+-----------------------------------------------------------+
| in bool **RESTART**             | Set to true when particle must restart (lifetime cycled). |
+---------------------------------+-----------------------------------------------------------+
| out vec4 **CUSTOM**             | Custom particle data.                                     |
+---------------------------------+-----------------------------------------------------------+
| out mat4 **TRANSFORM**          | Particle transform.                                       |
+---------------------------------+-----------------------------------------------------------+
| in float **TIME**               | Global time in seconds.                                   |
+---------------------------------+-----------------------------------------------------------+
| in float **LIFETIME**           | Particle lifetime.                                        |
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

Particle shades only support vertex processing. They are drawn with any regular material for CanvasItem or Spatial, depending on whether they are 2D or 3D.
