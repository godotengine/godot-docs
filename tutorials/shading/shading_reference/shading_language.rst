.. _doc_shading_language:

Shading language
================

Introduction
------------

Godot uses a shading language similar to GLSL ES 3.0. Most datatypes and functions are supported,
and the few remaining ones will likely be added over time.

If you are already familiar with GLSL, the :ref:`Godot Shader Migration Guide<doc_migrating_to_godot_shader_language>`
is a resource that will help you transition from regular GLSL to Godot's shading language.

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
| **bvec2**       | Two-component vector of booleans.                                         |
+-----------------+---------------------------------------------------------------------------+
| **bvec3**       | Three-component vector of booleans.                                       |
+-----------------+---------------------------------------------------------------------------+
| **bvec4**       | Four-component vector of booleans.                                        |
+-----------------+---------------------------------------------------------------------------+
| **int**         | Signed scalar integer.                                                    |
+-----------------+---------------------------------------------------------------------------+
| **ivec2**       | Two-component vector of signed integers.                                  |
+-----------------+---------------------------------------------------------------------------+
| **ivec3**       | Three-component vector of signed integers.                                |
+-----------------+---------------------------------------------------------------------------+
| **ivec4**       | Four-component vector of signed integers.                                 |
+-----------------+---------------------------------------------------------------------------+
| **uint**        | Unsigned scalar integer; can't contain negative numbers.                  |
+-----------------+---------------------------------------------------------------------------+
| **uvec2**       | Two-component vector of unsigned integers.                                |
+-----------------+---------------------------------------------------------------------------+
| **uvec3**       | Three-component vector of unsigned integers.                              |
+-----------------+---------------------------------------------------------------------------+
| **uvec4**       | Four-component vector of unsigned integers.                               |
+-----------------+---------------------------------------------------------------------------+
| **float**       | Floating point scalar.                                                    |
+-----------------+---------------------------------------------------------------------------+
| **vec2**        | Two-component vector of floating point values.                            |
+-----------------+---------------------------------------------------------------------------+
| **vec3**        | Three-component vector of floating point values.                          |
+-----------------+---------------------------------------------------------------------------+
| **vec4**        | Four-component vector of floating point values.                           |
+-----------------+---------------------------------------------------------------------------+
| **mat2**        | 2x2 matrix, in column major order.                                        |
+-----------------+---------------------------------------------------------------------------+
| **mat3**        | 3x3 matrix, in column major order.                                        |
+-----------------+---------------------------------------------------------------------------+
| **mat4**        | 4x4 matrix, in column major order.                                        |
+-----------------+---------------------------------------------------------------------------+
| **sampler2D**   | Sampler type for binding 2D textures, which are read as float.            |
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

    float a = 2; // invalid
    float a = 2.0; // valid
    float a = float(2); // valid

Default integer constants are signed, so casting is always needed to convert to unsigned:

.. code-block:: glsl

    int a = 2; // valid
    uint a = 2; // invalid
    uint a = uint(2); // valid

Members
~~~~~~~

Individual scalar members of vector types are accessed via the "x", "y", "z" and "w" members. 
Alternatively, using "r", "g", "b" and "a" also works and is equivalent. Use whatever fits 
best for your needs.

For matrices, use the ``m[row][column]`` indexing syntax to access each scalar, or ``m[idx]`` to access 
a vector by row index. For example, for accessing the y position of an object in a mat4 you  use 
``m[3][1]``.  

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

Construction of matrix types requires vectors of the same dimension as the matrix. You can 
also build a diagonal matrix using ``matx(float)`` syntax. Accordingly, ``mat4(1.0)`` is 
an identity matrix.

.. code-block:: glsl

    mat2 m2 = mat2(vec2(1.0, 0.0), vec2(0.0, 1.0));
    mat3 m3 = mat3(vec3(1.0, 0.0, 0.0), vec3(0.0, 1.0, 0.0), vec3(0.0, 0.0, 1.0));
    mat4 identity = mat4(1.0);

Matrices can also be built from a matrix of another dimension.
There are two rules :
If a larger matrix is constructed from a smaller matrix, the additional rows and columns are 
set to the values they would have in an identity matrix. If a smaller matrix is constructed 
from a larger matrix, the top, left submatrix of the larger matrix is used.

.. code-block:: glsl
	
	mat3 basis = mat3(WORLD_MATRIX);
	mat4 m4 = mat4(basis);
	mat2 m2 = mat2(m4);

Swizzling
~~~~~~~~~

It is possible to obtain any combination of components in any order, as long as the result 
is another vector type (or scalar). This is easier shown than explained:

.. code-block:: glsl

    vec4 a = vec4(0.0, 1.0, 2.0, 3.0);
    vec3 b = a.rgb; // Creates a vec3 with vec4 components.
    vec3 b = a.aaa; // Also valid; creates a vec3 and fills it with the "a" (alpha/w/4th) component of the vec4 "a".
    vec3 b = a.bgr; // Order does not matter.
    vec3 b = a.xyz; // Also rgba, xyzw are equivalent.
    float c = b.w; // Invalid, because "w" is not present in vec3 b.

Precision
~~~~~~~~~

It is possible to add precision modifiers to datatypes; use them for uniforms, variables, arguments and varyings:

.. code-block:: glsl

    lowp vec4 a = vec4(0.0, 1.0, 2.0, 3.0); // low precision, usually 8 bits per component mapped to 0-1
    mediump vec4 a = vec4(0.0, 1.0, 2.0, 3.0); // medium precision, usually 16 bits or half float
    highp vec4 a = vec4(0.0, 1.0, 2.0, 3.0); // high precision, uses full float or integer range (default)


Using lower precision for some operations can speed up the math involved (at the cost of less precision).
This is rarely needed in the vertex processor function (where full precision is needed most of the time), 
but is often useful in the fragment processor.

Keep in mind that some architectures (mainly mobile) benefit a lot from this, but are also restricted 
(conversion between precisions has a cost). Please read the relevant documentation on the target architecture 
to find out more. In all honesty though, mobile drivers are buggy, so, to stay out of trouble, make simple 
shaders without specifying precision unless you *really* need to.

Operators
---------

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

Flow control
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
Godot can't protect you from this, so be careful not to make this mistake!

Discarding
----------

Fragment and light functions can use the **discard** keyword. If used, the fragment is discarded and nothing is written.

Functions
---------

It is possible to define functions in a Godot shader. They use the following syntax:

.. code-block:: glsl

    ret_type func_name(args) {
        return ret_type; // if returning a value
    }

    // a more specific example:

    int sum2(int a, int b) {
        return a + b;
    }


You can only use functions that have been defined above (higher in the editor) the function from which you are calling 
them.

The function argument can have special qualifiers:

* **in**: Means the argument is only for reading (default).
* **out**: Means the argument is only for writing.
* **inout**: Means the argument is fully passed via reference.

Example below:

.. code-block:: glsl

    void sum2(int a, int b, inout int result) {
        result = a + b;
    }

Varyings
~~~~~~~~

To send data from the vertex to the fragment processor function, *varyings* are used. They are set 
for every primitive vertex in the *vertex processor*, and the value is interpolated for every 
pixel in the fragment processor.

.. code-block:: glsl

    shader_type spatial;

    varying vec3 some_color;
    void vertex() {
        some_color = NORMAL; // Make the normal the color.
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

There are two possible interpolation qualifiers:

+-------------------+---------------------------------------------------------------------------------+
| Qualifier         | Description                                                                     |
+===================+=================================================================================+
| **flat**          | The value is not interpolated.                                                  |
+-------------------+---------------------------------------------------------------------------------+
| **smooth**        | The value is interpolated in a perspective-correct fashion. This is the default.|
+-------------------+---------------------------------------------------------------------------------+


Uniforms
~~~~~~~~

Passing values to shaders is possible. These are global to the whole shader and are called *uniforms*.
When a shader is later assigned to a material, the uniforms will appear as editable parameters in it.
Uniforms can't be written from within the shader.

.. code-block:: glsl

    shader_type spatial;

    uniform float some_value;

You can set uniforms in the editor in the material. Or you can set them through GDScript:

:: 

  material.set_shader_param("some_value", some_value)

.. note:: The first argument to ``set_shader_param`` is the name of the uniform in the shader. It
          must match *exactly* to the name of the uniform in the shader or else it will not be recognized.

Any GLSL type except for *void* can be a uniform. Additionally, Godot provides optional shader hints
to make the compiler understand for what the uniform is used.

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

GDScript uses different variable types than GLSL does, so when passing variables from GDScript
to shaders, Godot converts the type automatically. Below is a table of the corresponding types:

+-----------------+-----------+
| GDScript type   | GLSL type |
+=================+===========+
| **bool**        | **bool**  |
+-----------------+-----------+
| **int**         | **int**   |
+-----------------+-----------+
| **float**       | **float** |
+-----------------+-----------+
| **Vector2**     | **vec2**  |
+-----------------+-----------+
| **Vector3**     | **vec3**  |
+-----------------+-----------+
| **Color**       | **vec4**  |
+-----------------+-----------+
| **Transform**   | **mat4**  |
+-----------------+-----------+
| **Transform2D** | **mat4**  |
+-----------------+-----------+

.. note:: Be careful when setting shader uniforms from GDScript, no error will be thrown if the
          type does not match. Your shader will just exhibit undefined behaviour.

As Godot's 3D engine renders in linear color space, it's important to understand that textures
that are supplied as color (i.e. albedo) need to be specified as such for proper sRGB->linear
conversion.

Uniforms can also be assigned default values:

.. code-block:: glsl

    shader_type spatial;

    uniform vec4 some_vector = vec4(0.0);
    uniform vec4 some_color : hint_color = vec4(1.0);

Built-in functions
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
| vec_type **step** ( vec_type a, vec_type b )                                                  | ``b[i] < a[i] ? 0.0 : 1.0``                |
+-----------------------------------------------------------------------------------------------+------------------------------------------------+
| vec_type **step** ( float a, vec_type b )                                                     | ``b[i] < a ? 0.0 : 1.0``                       |
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
| vec_type **faceforward** ( vec_type N, vec_type I, vec_type Nref )                            | If dot(Nref, I) < 0, return N, otherwise –N    |
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
