.. _doc_shading_language:

Shading language
================

Introduction
------------

Godot uses a shading language very similar to GLSL ES 3.0. Most datatypes and functions are supported,
and the remaining will likely be added over time.

Unlike the shader language in Godot 2.x, this implementaiton is much closer to the original.

Shader Types
------------

Instead of supplying a general purpose configuration, Godot Shading Language must
specify what shader is intended for. Depending on the type, different render
modes, built-in variables and processing functions are supported.

Any shader needs a first line specifying this type, in the following format:

.. highlight:: glsl
	shader_type <type>;

Valid types are:

* "spatial": For 3D rendering.
* "canvas_item": For 2D rendering.
* "particles": For particle systems.


Render Modes
------------

Different shader types support different render modes. They are optional but, if specified, must
be after the *shader_type*. Example syntax is:

.. highlight:: glsl
	shader_type spatial;
	render_mode unshaded,cull_disabled;

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
| **int**         | Signed scalar integer                                                     |
+-----------------+---------------------------------------------------------------------------+
| **ivec2**       | Two component vector of signed integers                                   |
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

Just like GLSL ES 3.0, implicit castling is not allowed between scalars and vectors of the same size but different type.
Casting of types of different size is also not allowed. Conversion must be done explicitly via constructors.

Example:

.. highlight:: glsl
	float a = 2; // valid
	float a = 2.0; // valid
	float a = float(2); // valid
 
Default integer constants are signed, so casting is always needed to convert to unsigned:

.. highlight:: glsl
	int a = 2; // valid
	uint a = 2; // invalid
	uint a = uint(2); // valid

Members
~~~~~~~

Individual scalar members of vector types are accessed via the "x", "y", "z" and "w" members. Alternatively, using "r", "g", "b" and "a" also works and is equivalent. 
Use whathever fits best for your use case.

For matrices, use [idx] indexing syntax to access each vector.

Constructing
~~~~~~~~~~~~

Construction of vector types must always pass:

.. highlight:: glsl
	// The required amount of scalars
	vec4 a = vec4(0.0, 1.0, 2.0, 3.0);
	// Complementary vectors and/or scalars
	vec4 a = vec4( vec2(0.0, 1.0), vec2(2.0, 3.0) );
	vec4 a = vec4( vec3(0.0, 1.0, 2.0), 3.0 );
	// A single scalar for the whole vector
	vec4 a = vec4( 0.0 );

Swizzling
~~~~~~~~~

It is possible to obtain any combination of them in any order, as long as the result is another vector type (or scalar). 
This is easier shown than explained:

.. highlight:: glsl
	vec4 a = vec4(0.0, 1.0, 2.0, 3.0);
	vec3 b = a.rgb; // Creates a vec3 with vec4 components 
	vec3 b = a.aaa; // Also valid, creates a vec3 and fills it with "a".
	vec3 b = a.bgr; // Order does not matter
	vec3 b = a.xyz; // Also rgba, xyzw are equivalent
	float c = b.w; // Invalid, because "w" is not present in vec3 b

Precision
~~~~~~~~~

It is possible to add precision modifiers to datatypes, use them for uniforms, variables, arguments and varyings:

.. highlight:: glsl
	lowp vec4 a = vec4(0.0, 1.0, 2.0, 3.0); // low precision, usually 8 bits per component mapped to 0-1
	mediump vec4 a = vec4(0.0, 1.0, 2.0, 3.0); // medium precision, usually 16 bits or half float
	highp vec4 a = vec4(0.0, 1.0, 2.0, 3.0); // high precision, uses full float or integer range (default)


Using lower precision for some operations can speed up the math involved (at the cost of, of course, less precision).
This is rarely needed in the vertex shader (where full precision is needed most of the time), but often needed in the fragment one.

Keep in mind that some architectures (mainly mobile) benefit a lot on this, but are also restricted (conversion between precisions has a cost).
Please read the relevant documentation on the target architecture to find out more. In all honesty though, mobile drivers are really buggy
so just stay out of trouble and make simple shaders without specifying precission unless you *really* need to.

Operators:
----------

Godot shading language supports the same set of operators as GLSL ES 3.0. Below is the list of them in precedence order:

+-------------+-----------------------+--------------------+
| Precedence  | Class                 | Operator           |
+-------------+-----------------------+--------------------+
| 1 (highest) | parenthical grouping  | **()**             |
+-------------+-----------------------+--------------------+
| 2           | unary                 | **+, -, !, ~**     |
+-------------+-----------------------+--------------------+
| 3           | multiplicative        | **/, *, % **       |
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

.. highlight:: glsl
	//if and else
	if (cond) {

	} else {

	}

	//for loops
	for(int i=0;i<10;i++) {

	}

	//whiles
	while (true) {

	}
	

Keep in mind that, in modern GPUs, an infinite loop can exist and can freeze your application (including editor).
Godot can't protect you from this, so be careful to not make this mistake!

Functions
---------

It's possible to define any function in a Godot shader. They take the following syntax:

.. highlight:: glsl
	ret_type func_name(args) {

		return ret_type; // if returning a value
	}

	// a better example:

	int sum2(int a, int b) {
		return a+b;
	}


Functions can be used from any other function that is below it.

Function argument can have special qualifiers:

* **in**: Means the argument is only for reading (default).
* **out**: Means the argument is only for writing.
* **inout**: Means the argument is fully passed via reference.

Example below:

.. highlight:: glsl

	void sum2(int a, int b, inout int result) {
		result = a+b;
	}


 
Processor Functions
-------------------

Depending on shader type, processor functions may be available to optionally override.
For "spatial" and "canvas_item", it is possible to override "vertex", "fragment" and "light".
For "particles", only "vertex" can be overriden.

Vertex Processor
~~~~~~~~~~~~~~~~~

The "vertex" processing function is called for every vertex, 2D or 3D. For particles, it's called for every
particle.

Depending on shader type, a different set of built-in inputs and outputs are provided. In general,
vertex functions are not that commonly used.

.. highlight:: glsl

	shader_type spatial;

	void vertex() {
		VERTEX.x+=sin(TIME); //offset vertex x by sine function on time elapsed
	}


Fragment Processor
~~~~~~~~~~~~~~~~~~

The "fragent" processor is used to set up the Godot material parameters per pixel. This code
runs on every visible pixel the object or primitive is drawn to.

.. highlight:: glsl

	shader_type spatial;

	void fragment() {
		ALBEDO=vec3(1.0,0.0,0.0); // use red for material albedo
	}

Light Processor
~~~~~~~~~~~~~~~

The "light" processor runs per pixel too, but also runs for every light that affects the object (
and does not run if no lights affect the object).

.. highlight:: glsl

	shader_type spatial;

	void light() {
		COLOR=vec3(0.0,1.0,0.0); 
	}


Varyings
~~~~~~~~

To send data from vertex to fragment shader, *varyings* are used. They are set for every primitive vertex
in the *vertex processor*, and the value is interpolated (and perspective corrected) when reaching every
pixel in the fragment processor.


.. highlight:: glsl

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
Uniforms can't be written from within the shadr.

.. highlight:: glsl

	shader_type spatial;

	uniform float some_value;


Any type except for *void* can be a uniform. Additionally, Godot provides optional shader hints
to make the compiler understand what the uniform is used for.


.. highlight:: glsl

	shader_type spatial;

	uniform vec4 color : hint_color;
	uniform float amonut : hint_range(0,1);


Full list of hints below:

+-------------------+-------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Type              | Hint                          | Description                                                                                                                                                                                                            |
+===================+===============================+========================================================================================================================================================================================================================+
| **vec4**          | hint_color                    | This uniform is exported as a color parameter in property editor. Color is also converted from SRGB for 3D shaders.                                                                                                    |
+-------------------+-------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **int**, **float**| hint_range(min,max [,step] )  | This scalar uniform is exported as a given range in property editor.                                                                                                                                                   |
+-------------------+-------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **sampler2D**     | hint_albedo                   | This texture is used as albedo color. Godot will try to make sure the texture has SRGB -> Linear conversion turned on. If no texture is supplied, this is assumed to be white.                                         |
+-------------------+-------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **sampler2D**     | hint_black_albedo             | Same as above but, if no texture is supplied, it's assumed to be black.                                                                                                                                                |
+-------------------+-------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **sampler2D**     | hint_normal                   | The texture supplied is a normal map. Godot will attempt to convert the texture to a more efficient normalmap format when used here. Also, an empty texture results in a vec3(0.0,0.0,1.0) normal assigned by default. |
+-------------------+-------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **sampler2D**     | hint_white                    | Regular texture (non albedo). White is used if unasigned.                                                                                                                                                              |
+-------------------+-------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **sampler2D**     | hint_black                    | Regular texture (non albedo). Black is used if unassigned.                                                                                                                                                             |
+-------------------+-------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **sampler2D**     | hint_aniso                    | Same as above, but vec3(1.0, 0.5, 0.0) is assigned by default (useful for flowmaps)                                                                                                                                    |
+-------------------+-------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


Uniforms can also be assigned default values:


.. highlight:: glsl

	shader_type spatial;

	uniform vec4 some_vector = vec4(0.0);



Built-in Functions
------------------

A large amount of built-in functions is supported, confirming mostly to GLSL ES 3.0.
When vec_type (float), vec_int_type, vec_uint_type, vec_bool_type, nomenclature is used, it can be scalar or vcetor.



+-----------------------------------------------------------------------+---------------------------------------------+
| Function                                                              | Description                                 |
+=======================================================================+=============================================+
| float *sin* ( float )                                                 | Sine                                        |
+-----------------------------------------------------------------------+---------------------------------------------+
| float *cos* ( float )                                                 | Cosine                                      |
+-----------------------------------------------------------------------+---------------------------------------------+
| float *tan* ( float )                                                 | Tangent                                     |
+-----------------------------------------------------------------------+---------------------------------------------+
| float *asin* ( float )                                                | arc-Sine                                    |
+-----------------------------------------------------------------------+---------------------------------------------+
| float *acos* ( float )                                                | arc-Cosine                                  |
+-----------------------------------------------------------------------+---------------------------------------------+
| float *atan* ( float )                                                | arc-Tangent                                 |
+-----------------------------------------------------------------------+---------------------------------------------+
| float *atan2* ( float x, float y)                                     | arc-Tangent to convert vector to angle      |
+-----------------------------------------------------------------------+---------------------------------------------+
| float *sinh* ( float )                                                | Hyperbolic-Sine                             |
+-----------------------------------------------------------------------+---------------------------------------------+
| float *cosh* ( float )                                                | Hyperbolic-Cosine                           |
+-----------------------------------------------------------------------+---------------------------------------------+
| float *tanh* ( float )                                                | Hyperbolic-Tangent                          |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec\_type *pow* ( float x, float y)                                   | Power, x elevated to y                      |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec\_type *pow* ( vec\_type, vec\_type )                              | Power (Vec. Exponent)                       |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec\_type *exp* ( vec\_type )                                         | Base-e Exponential                          |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec\_type *log* ( vec\_type )                                         | Natural Logarithm                           |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec\_type *sqrt* ( vec\_type )                                        | Square Root                                 |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec\_type *inversesqrt* ( vec\_type )                                 | Inverse Square Root                         |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec\_type *abs* ( vec\_type )                                         | Absolute                                    |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec\_type *sign* ( vec\_type )                                        | Sign                                        |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec\_type *floor* ( vec\_type )                                       | Floor                                       |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec\_type *round* ( vec\_type )                                       | Round                                       |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec\_type *trunc* ( vec\_type )                                       | Trunc                                       |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec\_type *ceil* ( vec\_type )                                        | Ceiling                                     |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec\_type *fract* ( vec\_type )                                       | Fractional                                  |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec\_type *mod* ( vec\_type,vec\_type )                               | Remainder                                   |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec\_type *modf* ( vec\_type x,out vec\_type i)                       | Fractional of x, with i has integer part    |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec\_type *min* ( vec\_type,vec\_type )                               | Minimum                                     |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec\_type *min* ( vec\_type,vec\_type )                               | Maximum                                     |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec\_type *clamp* ( vec\_type value,vec\_type min, vec\_type max )    | Clamp to Min-Max                            |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec\_type *mix* ( vec\_type a,vec\_type b, float c )                  | Linear Interpolate                          |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec\_type *mix* ( vec\_type a,vec\_type b, vec\_type c )              | Linear Interpolate (Vector Coef.)           |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec\_type *step* ( vec\_type a,vec\_type b)                           | \` a[i] < b[i] ? 0.0 : 1.0\`                |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec\_type *smoothstep* ( vec\_type a,vec\_type b,vec\_type c)         |                                             |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec_bool_type *isnan* ( vec\_type )                                   | scalar, or vector component being nan       |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec_bool_type *isinf* ( vec\_type )                                   | scalar, or vector component being inf       |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec_int_type *floatBitsToInt* ( vec_type )                            | Float->Int bit copying, no conversion       |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec_uint_type *floatBitsToUInt* ( vec_type )                          | Float->UInt bit copying, no conversion      |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec_type *intBitsToFloat* ( vec_int_type )                            | Int->Float bit copying, no conversion       |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec_type *uintBitsToFloat* ( vec_uint_type )                          | UInt->Float bit copying, no conversion      |
+-----------------------------------------------------------------------+---------------------------------------------+
| float *length* ( vec\_type )                                          | Vector Length                               |
+-----------------------------------------------------------------------+---------------------------------------------+
| float *distance* ( vec\_type, vec\_type )                             | Distance between vector.                    |
+-----------------------------------------------------------------------+---------------------------------------------+
| float *dot* ( vec\_type, vec\_type )                                  | Dot Product                                 |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec3 *cross* ( vec3, vec3 )                                           | Cross Product                               |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec\_type *normalize* ( vec\_type )                                   | Normalize to unit length                    |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec3 *reflect* ( vec3, vec3 )                                         | Reflect                                     |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec3 *refract* ( vec3, vec3 )                                         | Refract                                     |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec_type *faceforward* ( vec_type N, vec_type I, vec_type NRef)       | If dot(Nref, I) < 0 return N, otherwise –N  |
+-----------------------------------------------------------------------+---------------------------------------------+
| mat_type *matrixCompMult* ( mat_type, mat_type )                      | Matrix Component Multiplication             |
+-----------------------------------------------------------------------+---------------------------------------------+
| mat_type *outerProduct* ( vec_type, vec_type )                        | Matrix Outer Product                        |
+-----------------------------------------------------------------------+---------------------------------------------+
| mat_type *transpose* ( mat_type )                                     | Transpose Matrix                            |
+-----------------------------------------------------------------------+---------------------------------------------+
| float *determinant* ( mat_type )                                      | Matrix Determinant                          |
+-----------------------------------------------------------------------+---------------------------------------------+
| mat_type *inverse* ( mat_type )                                       | Inverse Matrix                              |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec\_bool_type *lessThan* ( vec_scalar_type )                         | Bool vector cmp on < int/uint/float vectors |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec\_bool_type *greaterThan* ( vec_scalar_type )                      | Bool vector cmp on > int/uint/float vectors |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec\_bool_type *lessThanEqual* ( vec_scalar_type )                    | Bool vector cmp on <=int/uint/float vectors |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec\_bool_type *greaterThanEqual* ( vec_scalar_type )                 | Bool vector cmp on >=int/uint/float vectors |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec\_bool_type *equal* ( vec_scalar_type )                            | Bool vector cmp on ==int/uint/float vectors |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec\_bool_type *notEqual* ( vec_scalar_type )                         | Bool vector cmp on !=int/uint/float vectors |
+-----------------------------------------------------------------------+---------------------------------------------+
| bool *any* ( vec_bool_type )                                          | Any component is true                       |
+-----------------------------------------------------------------------+---------------------------------------------+
| bool *all* ( vec_bool_type )                                          | All components are true                     |
+-----------------------------------------------------------------------+---------------------------------------------+
| bool *not* ( vec_bool_type )                                          | No components are true                      |
+-----------------------------------------------------------------------+---------------------------------------------+
| ivec2 *textureSize* ( sampler2D_type s, int lod )                     | Get the size of a texture                   |
+-----------------------------------------------------------------------+---------------------------------------------+
| ivec2 *textureSize* ( samplerCube s, int lod )                        | Get the size of a cubemap                   |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec4_type *texture* ( sampler2D_type s, vec2 uv [, float bias])       | Perform a 2D texture read                   |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec4 *texture* ( samplerCube s, vec3 uv [, float bias])               | Perform a Cube texture read                 |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec4_type *textureProj* ( sampler2d_type s, vec3 uv [, float bias])   | Perform a texture read with projection      |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec4_type *textureProj* ( sampler2d_type s, vec4 uv [, float bias])   | Perform a texture read with projection      |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec4_type *textureLod* ( sampler2D_type s, vec2 uv , float lod)       | Perform a 2D texture read at custom mipmap  |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec4_type *textureProjLod* ( sampler2d_type s, vec3 uv , float lod)   | Perform a texture read with projection/lod  |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec4_type *textureProjLod* ( sampler2d_type s, vec4 uv , float lod)   | Perform a texture read with projection/lod  |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec_type *texelFetch* ( samplerCube s, ivec2 uv, int lod )            | Fetch a single texel using integer coords   |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec_type *dFdx* ( vec_type )                                          | Derivative in x using local differencing    |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec_type *dFdy* ( vec_type )                                          | Derivative in y using local differencing    |
+-----------------------------------------------------------------------+---------------------------------------------+
| vec_type *fwidth* ( vec_type )                                        | Sum of absolute derivative in x and y       |
+-----------------------------------------------------------------------+---------------------------------------------+











