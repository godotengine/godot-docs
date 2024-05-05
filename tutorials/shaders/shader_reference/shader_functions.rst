.. _doc_shader_functions:

Built-in functions
------------------------------------------

Godot supports a large number of built-in functions, conforming roughly to the
GLSL 4.00 specification.

.. note::
    The following type aliases only used in documentation to reduce repetitive function declarations.
    They can each refer to any of several actual types.

    +-----------------+--------------------------------------------------+--------------------------+
    | alias           | actual types                                     | glsl documentation alias |
    +=================+==================================================+==========================+
    | vec_type        | float, vec2, vec3, or vec4                       | genType                  |
    +-----------------+--------------------------------------------------+--------------------------+
    | vec_int_type    | int, ivec2, ivec3, or ivec4                      | genIType                 |
    +-----------------+--------------------------------------------------+--------------------------+
    | vec_uint_type   | uint, uvec2, uvec3, or uvec4                     | genUType                 |
    +-----------------+--------------------------------------------------+--------------------------+
    | vec_bool_type   | bool, bvec2, bvec3, or bvec4                     | genUType                 |
    +-----------------+--------------------------------------------------+--------------------------+
    | mat_type        | mat2, mat3, or mat4                              | mat                      |
    +-----------------+--------------------------------------------------+--------------------------+
    | gvec4_type      | vec4, ivec4, or uvec4                            |                          |
    +-----------------+--------------------------------------------------+--------------------------+
    | gsampler2D      | sampler2D, isampler2D, uSampler2D                |                          |
    +-----------------+--------------------------------------------------+--------------------------+
    | gsampler2DArray | sampler2DArray, isampler2DArray, uSampler2DArray |                          |
    +-----------------+--------------------------------------------------+--------------------------+
    | gsampler3D      | sampler3D, isampler3D, uSampler3D                |                          |
    +-----------------+--------------------------------------------------+--------------------------+

    If  any of these are specified for multiple parameters, they must all be the same type unless otherwise noted.

.. note::
    Most operations on vectors (multiplication, division, etc) are performed component-wise.
    For example, the operation ``vec2(3,4) * vec2(10,20)`` would result in ``vec2(3 * 10, 4 * 20)``.
    or the operation ``min(vec2(3,4), vec2(1,8))`` would result in ``vec2(min(3,1),min(4,8))``.

    The `GLSL Language Specification <http://www.opengl.org/registry/doc/GLSLangSpec.4.30.6.pdf>` says under section 5.10 Vector and Matrix Operations:

        With a few exceptions, operations are component-wise. Usually, when an operator operates on a
        vector or matrix, it is operating independently on each component of the vector or matrix,
        in a component-wise fashion. [...] The exceptions are matrix multiplied by vector,
        vector multiplied by matrix, and matrix multiplied by matrix. These do not operate component-wise,
        but rather perform the correct linear algebraic multiply.

.. rst-class:: classref-reftable-group

Trigonometric Functions
^^^^^^^^^^^^^^^^^^^^^^^

+-----------------+-------------------------------------------------------------+-----------------------------+
|    Return Type  |                          Function                           | Description / Return value  |
+=================+=============================================================+=============================+
| |vec_type|      | :ref:`radians<shader_func_radians>` ( |vec_type| degrees)   | Convert degrees to radians. |
+-----------------+-------------------------------------------------------------+-----------------------------+
| |vec_type|      | :ref:`degrees<shader_func_degrees>` ( |vec_type| radians)   | Convert radians to degrees. |
+-----------------+-------------------------------------------------------------+-----------------------------+
| |vec_type|      | :ref:`sin<shader_func_sin>` ( |vec_type| x)                 | Sine.                       |
+-----------------+-------------------------------------------------------------+-----------------------------+
| |vec_type|      | :ref:`cos<shader_func_cos>` ( |vec_type| x)                 | Cosine.                     |
+-----------------+-------------------------------------------------------------+-----------------------------+
| |vec_type|      | :ref:`tan<shader_func_tan>` ( |vec_type| x)                 | Tangent.                    |
+-----------------+-------------------------------------------------------------+-----------------------------+
| |vec_type|      | :ref:`asin<shader_func_asin>` ( |vec_type| x)               | Arcsine.                    |
+-----------------+-------------------------------------------------------------+-----------------------------+
| |vec_type|      | :ref:`acos<shader_func_acos>` ( |vec_type| x)               | Arccosine.                  |
+-----------------+-------------------------------------------------------------+-----------------------------+
| |vec_type|      | :ref:`atan<shader_func_atan>` ( |vec_type| y_over_x)        | Arctangent.                 |
+-----------------+-------------------------------------------------------------+                             |
| |vec_type|      | :ref:`atan<shader_func_atan>` ( |vec_type| y, |vec_type| x) |                             |
+-----------------+-------------------------------------------------------------+-----------------------------+
| |vec_type|      | :ref:`sinh<shader_func_sinh>` ( |vec_type| x)               | Hyperbolic sine.            |
+-----------------+-------------------------------------------------------------+-----------------------------+
| |vec_type|      | :ref:`cosh<shader_func_cosh>` ( |vec_type| x)               | Hyperbolic cosine.          |
+-----------------+-------------------------------------------------------------+-----------------------------+
| |vec_type|      | :ref:`tanh<shader_func_tanh>` ( |vec_type| x)               | Hyperbolic tangent.         |
+-----------------+-------------------------------------------------------------+-----------------------------+
| |vec_type|      | :ref:`asinh<shader_func_asinh>` ( |vec_type| x)             | Inverse hyperbolic sine.    |
+-----------------+-------------------------------------------------------------+-----------------------------+
| |vec_type|      | :ref:`acosh<shader_func_acosh>` ( |vec_type| x)             | Inverse hyperbolic cosine.  |
+-----------------+-------------------------------------------------------------+-----------------------------+
| |vec_type|      | :ref:`atanh<shader_func_atanh>` ( |vec_type| x)             | Inverse hyperbolic tangent. |
+-----------------+-------------------------------------------------------------+-----------------------------+

.. rst-class:: classref-section-separator

----

.. rst-class:: classref-descriptions-group

.. _shader_func_radians:

.. rst-class:: classref-method

|vec_type| **radians** ( |vec_type| degrees )

    Converts a quantity specified in degrees into radians.

    :param degrees:
        Specify the quantity, in degrees, to be converted to radians.

    :return:
        ``(π * degrees) / 180``.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/radians.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_degrees:

.. rst-class:: classref-method

|vec_type| degrees( |vec_type| radians)

    Converts a quantity specified in radians into degrees.

    :param radians:
        Specify the quantity, in radians, to be converted to degrees.

    :return:
        ``(radians * 180) / π``.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/degrees.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_sin:

.. rst-class:: classref-method

vec_type sin( |vec_type| angle)

    Return the sine of the parameter.

    :param angle:
        takehe quantity, in radians, of which to return the sine

    :return:
        the trigonometric sine of ``angle``.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/sin.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_cos:

.. rst-class:: classref-method

vec_type cos( |vec_type| angle)

    Return the cosine of the parameter.

    :param angle:
        the quantity, in radians, of which to return the cosine.

    :return:
        the trigonometric cosine of ``angle``.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/cos.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_tan:

.. rst-class:: classref-method

vec_type tan( |vec_type| angle)

    Return the tangent of the parameter.

    :param angle:
        The quantity, in radians, of which to return the tangent.

    :return:
        the trigonometric tangent of ``angle``.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/tan.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_asin:

.. rst-class:: classref-method

vec_type asin( |vec_type| x)

    Calculates the angle whose sine is ``x``.
    The result is undefined if ``x < -1`` or ``x > 1``.

    :param x:
        The value whose arccosine to return.
    :return:
        the angle whose trigonometric sine is ``x`` and is
        in the range ``[-π/2, π/2]``.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/asin.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_acos:

.. rst-class:: classref-method

vec_type acos( |vec_type| x)

    Calculates the angle whose cosine is ``x``.
    The result is undefined if ``x < -1`` or ``x > 1``.

    :param x:
        The value whose arccosine to return.

    :return:
        the angle whose trigonometric cosine is ``x`` and
        is in the range ``[0, π]``.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/acos.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_atan:

.. rst-class:: classref-method

vec_type atan( |vec_type| y_over_x)

    Calculate the arctangent given a tangent value of ``y/x``. Note: becuase of
    the sign ambiguity, the function cannot determine with certainty in which
    quadrant the angle falls only by its tangent value. If you need to know the
    quadrant, use ``atan( |vec_type| y, |vec_type| x )``.

    :param y_over_x:
        The fraction whose arctangent to return.

    :return:
        the trigonometric arc-tangent of ``y_over_x`` and is
        in the range ``[-π/2, π/2]``.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/atan.xhtml


.. rst-class:: classref-item-separator

----


.. rst-class:: classref-method

vec_type atan( |vec_type| y, |vec_type| x)

    Calculate the arctangent given a numerator and denominator. The signs of
    ``y`` and ``x`` are used to determine the quadrant that the angle lies in.
    The result is undefined if ``x == 0``.

    :param y:
        The numerator of the fraction whose arctangent to return.

    :param x:
        The denominator of the fraction whose arctangent to return.

    :return:
        the trigonometric arc-tangent of ``y/x`` and is in
        the range ``[-π, π]``.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/atan.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_sinh:

.. rst-class:: classref-method

vec_type sinh( |vec_type| x)

    Calculates the hyperbolic sine using ``(e^x - e^-x)/2``.

    :param x:
        The value whose hyperbolic sine to return.

    :return:
        the hyperbolic sine of ``x``.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/sinh.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_cosh:

.. rst-class:: classref-method

vec_type cosh( |vec_type| x)

    Calculates the hyperbolic cosine using ``(e^x + e^-x)/2``.

    :param x:
        The value whose hyperbolic cosine to return.

    :return:
        the hyperbolic cosine of ``x``.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/cosh.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_tanh:

.. rst-class:: classref-method

vec_type tanh( |vec_type| x)

    Calculates the hyperbolic tangent using ``sinh(x)/cosh(x)``.

    :param x:
        The value whose hyperbolic tangent to return.

    :return:
        the hyperbolic tangent of ``x``.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/tanh.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_asinh:

.. rst-class:: classref-method

vec_type asinh( |vec_type| x)

    Calculates the arc hyperbolic sine of a value.

    :param x:
        The value whose arc hyperbolic sine to return.

    :return:
        the arc hyperbolic sine of ``x`` which is the
        inverse of sinh.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/asinh.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_acosh:

.. rst-class:: classref-method

vec_type acosh( |vec_type| x)

    Calculates the arc hyperbolic cosine of a value.
    The result is undefined if ``x < 1``.

    :param x:
        The value whose arc hyperbolic cosine to return.

    :return:
        <return_description/>

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/acos.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_atanh:

.. rst-class:: classref-method

vec_type atanh( |vec_type| x)

    Calculate the arctangent given a tangent value of ``y/x``. Note: becuase of
    the sign ambiguity, the function cannot determine with certainty in which
    quadrant the angle falls only by its tangent value. If you need to know the
    quadrant, use the other overload of ``atan``.

    The result is undefined if ``x < -1`` or ``x > 1``.

    :param y_over_x:
        The fraction whose arc hyperbolic tangent to return.

    :return:
        the arc hyperbolic tangent of ``x`` which is the
        inverse of tanh.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/atan.xhtml

.. rst-class:: classref-item-separator

----



Exponential and Common Math Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+-----------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| |vec_type|      | :ref:`pow<shader_func_pow>` ( |vec_type| x, |vec_type| y)                                   | Power (undefined if ``x < 0`` or if ``x == 0`` and ``y <= 0``). |
+-----------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| |vec_type|      | :ref:`exp<shader_func_exp>` ( |vec_type| x)                                                 | Base-e exponential.                                             |
+-----------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| |vec_type|      | :ref:`exp2<shader_func_exp2>` ( |vec_type| x)                                               | Base-2 exponential.                                             |
+-----------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| |vec_type|      | :ref:`log<shader_func_log>` ( |vec_type| x)                                                 | Natural logarithm.                                              |
+-----------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| |vec_type|      | :ref:`log2<shader_func_log2>` ( |vec_type| x)                                               | Base-2 logarithm.                                               |
+-----------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| |vec_type|      | :ref:`sqrt<shader_func_sqrt>` ( |vec_type| x)                                               | Square root.                                                    |
+-----------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| |vec_type|      | :ref:`inversesqrt<shader_func_inversesqrt>` ( |vec_type| x)                                 | Inverse square root.                                            |
+-----------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| |vec_type|      | :ref:`abs<shader_func_abs>` ( |vec_type| x)                                                 | Absolute value (returns positive value if negative).            |
+-----------------+---------------------------------------------------------------------------------------------+                                                                 |
| |vec_int_type|  | :ref:`abs<shader_func_abs>` ( |vec_int_type| x)                                             |                                                                 |
+-----------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| |vec_type|      | :ref:`sign<shader_func_sign>` ( |vec_type| x)                                               | returns ``1.0`` if positive, ``-1.0`` if negative,              |
+-----------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| |vec_int_type|  | :ref:`sign<shader_func_sign>` ( |vec_int_type| x)                                           | returns ``1`` if positive, ``-1`` if negative,                  |
+-----------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| |vec_type|      | :ref:`floor<shader_func_floor>` ( |vec_type| x)                                             | Round to the integer below.                                     |
+-----------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| |vec_type|      | :ref:`round<shader_func_round>` ( |vec_type| x)                                             | Round to the nearest integer.                                   |
+-----------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| |vec_type|      | :ref:`roundEven<shader_func_roundEven>` ( |vec_type| x)                                     | Round to the nearest even integer.                              |
+-----------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| |vec_type|      | :ref:`trunc<shader_func_trunc>` ( |vec_type| x)                                             | Truncation.                                                     |
+-----------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| |vec_type|      | :ref:`ceil<shader_func_ceil>` ( |vec_type| x)                                               | Round to the integer above.                                     |
+-----------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| |vec_type|      | :ref:`fract<shader_func_fract>` ( |vec_type| x)                                             | Fractional (returns ``x - floor(x)``).                          |
+-----------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| |vec_type|      | :ref:`mod<shader_func_mod>` ( |vec_type| x, |vec_type| y)                                   | Modulo (division remainder).                                    |
+-----------------+---------------------------------------------------------------------------------------------+                                                                 |
| |vec_type|      | :ref:`mod<shader_func_mod>` ( |vec_type| x, float y)                                        |                                                                 |
+-----------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| |vec_type|      | :ref:`modf<shader_func_modf>` (|vec_type| x, out |vec_type| i)                              | Fractional of ``x``, with ``i`` as integer part.                |
+-----------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| |vec_type|      | :ref:`min<shader_func_min>` ( |vec_type| a, |vec_type| b)                                   | Lowest value between ``a`` and ``b``.                           |
+-----------------+---------------------------------------------------------------------------------------------+                                                                 |
| |vec_type|      | :ref:`min<shader_func_min>` ( |vec_type| a, float b)                                        |                                                                 |
+-----------------+---------------------------------------------------------------------------------------------+                                                                 |
| |vec_int_type|  | :ref:`min<shader_func_min>` ( |vec_int_type| a, |vec_int_type| b)                           |                                                                 |
+-----------------+---------------------------------------------------------------------------------------------+                                                                 |
| |vec_int_type|  | :ref:`min<shader_func_min>` ( |vec_int_type| a, int b)                                      |                                                                 |
+-----------------+---------------------------------------------------------------------------------------------+                                                                 |
| |vec_uint_type| | :ref:`min<shader_func_min>` ( |vec_uint_type| a, |vec_uint_type| b)                         |                                                                 |
+-----------------+---------------------------------------------------------------------------------------------+                                                                 |
| |vec_uint_type| | :ref:`min<shader_func_min>` ( |vec_uint_type| a, uint b)                                    |                                                                 |
+-----------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| |vec_type|      | :ref:`max<shader_func_max>` ( |vec_type| a, |vec_type| b)                                   | Highest value between ``a`` and ``b``.                          |
+-----------------+---------------------------------------------------------------------------------------------+                                                                 |
| |vec_type|      | :ref:`max<shader_func_max>` ( |vec_type| a, float b)                                        |                                                                 |
+-----------------+---------------------------------------------------------------------------------------------+                                                                 |
| |vec_uint_type| | :ref:`max<shader_func_max>` ( |vec_uint_type| a, |vec_uint_type| b)                         |                                                                 |
+-----------------+---------------------------------------------------------------------------------------------+                                                                 |
| |vec_uint_type| | :ref:`max<shader_func_max>` ( |vec_uint_type| a, uint b)                                    |                                                                 |
+-----------------+---------------------------------------------------------------------------------------------+                                                                 |
| |vec_int_type|  | :ref:`max<shader_func_max>` ( |vec_int_type| a, |vec_int_type| b)                           |                                                                 |
+-----------------+---------------------------------------------------------------------------------------------+                                                                 |
| |vec_int_type|  | :ref:`max<shader_func_max>` ( |vec_int_type| a, int b)                                      |                                                                 |
+-----------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| |vec_type|      | :ref:`clamp<shader_func_clamp>` (|vec_type| x, |vec_type| min, |vec_type| max)              | Clamp ``x`` between ``min`` and ``max`` (inclusive).            |
+-----------------+---------------------------------------------------------------------------------------------+                                                                 |
| |vec_type|      | :ref:`clamp<shader_func_clamp>` ( |vec_type| x, float min, float max)                       |                                                                 |
+-----------------+---------------------------------------------------------------------------------------------+                                                                 |
| |vec_uint_type| | :ref:`clamp<shader_func_clamp>` ( |vec_int_type| x, |vec_int_type| min, |vec_int_type| max) |                                                                 |
+-----------------+---------------------------------------------------------------------------------------------+                                                                 |
| |vec_uint_type| | :ref:`clamp<shader_func_clamp>` ( |vec_int_type| x, float min, float max)                   |                                                                 |
+-----------------+---------------------------------------------------------------------------------------------+                                                                 |
| |vec_int_type|  | :ref:`clamp<shader_func_clamp>` (|vec_type| x, |vec_type| min, |vec_type| max)              |                                                                 |
+-----------------+---------------------------------------------------------------------------------------------+                                                                 |
| |vec_int_type|  | :ref:`clamp<shader_func_clamp>` ( |vec_type| x, float min, float max)                       |                                                                 |
+-----------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| |vec_type|      | :ref:`mix<shader_func_mix>` (|vec_type| a, |vec_type| b, |vec_type| c)                      | Linear interpolate between ``a`` and ``b`` by ``c``.            |
+-----------------+---------------------------------------------------------------------------------------------+                                                                 |
| |vec_type|      | :ref:`mix<shader_func_mix>` (|vec_type| a, |vec_type| b, float c)                           |                                                                 |
+-----------------+---------------------------------------------------------------------------------------------+                                                                 |
| |vec_type|      | :ref:`mix<shader_func_mix>` (|vec_type| a, |vec_type| b, |vec_bool_type| c)                 |                                                                 |
+-----------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| |vec_type|      | :ref:`fma<shader_func_fma>` (|vec_type| a, |vec_type| b, |vec_type| c)                      | Fused multiply-add operation: ``(a * b + c)``                   |
+-----------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| |vec_type|      | :ref:`step<shader_func_step>` ( |vec_type| a, |vec_type| b)                                 | ``b[i] < a[i] ? 0.0 : 1.0``.                                    |
+-----------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| |vec_type|      | :ref:`step<shader_func_step>` (float a, |vec_type| b)                                       | ``b[i] < a ? 0.0 : 1.0``.                                       |
+-----------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| |vec_type|      | :ref:`smoothstep<shader_func_smoothstep>` (|vec_type| a, |vec_type| b, |vec_type| c)        | Hermite interpolate between ``a`` and ``b`` by ``c``.           |
+-----------------+---------------------------------------------------------------------------------------------+                                                                 |
| |vec_type|      | :ref:`smoothstep<shader_func_smoothstep>` (float a, float b, |vec_type| c)                  |                                                                 |
+-----------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| |vec_bool_type| | :ref:`isnan<shader_func_isnan>` ( |vec_type| x)                                             | Returns ``true`` if scalar or vector component is ``NaN``.      |
+-----------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| |vec_bool_type| | :ref:`isinf<shader_func_isinf>` ( |vec_type| x)                                             | Returns ``true`` if scalar or vector component is ``INF``.      |
+-----------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| |vec_int_type|  | :ref:`floatBitsToInt<shader_func_floatBitsToInt>` ( |vec_type| x)                           | Float->Int bit copying, no conversion.                          |
+-----------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| |vec_uint_type| | :ref:`floatBitsToUint<shader_func_floatBitsToUint>` ( |vec_type| x)                         | Float->UInt bit copying, no conversion.                         |
+-----------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| |vec_type|      | :ref:`intBitsToFloat<shader_func_intBitsToFloat>` ( |vec_int_type| x)                       | Int->Float bit copying, no conversion.                          |
+-----------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| |vec_type|      | :ref:`uintBitsToFloat<shader_func_uintBitsToFloat>` ( |vec_uint_type| x)                    | UInt->Float bit copying, no conversion.                         |
+-----------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------------+

.. rst-class:: classref-section-separator

----


.. _shader_func_pow:

.. rst-class:: classref-method


vec_type pow( |vec_type| x, |vec_type| y)

    Raises ``x`` to the power of ``y``.

    The result is undefined if ``x < 0`` or  if ``x == 0`` and ``y <= 0``.

    :param x:
        The value to be raised to the power ``y``.

    :param y:
        The power to which ``x`` will be raised.

    :return:
        Returns the value of ``x`` raised to the ``y`` power.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/pow.xhtml

.. rst-class:: classref-item-separator

----



.. _shader_func_exp:

.. rst-class:: classref-method

|vec_type| **exp** ( |vec_type| x )

    Return the natural exponentiation of the parameter.

    :param x:
        The value to exponentiate.

    :return:
        The natural exponentiation of x. i.e., e\ :sup:`x`

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/exp.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_exp2:

.. rst-class:: classref-method

|vec_type| **exp2** ( |vec_type| x )

    Return 2 raised to the power of the parameter.

    :param x:
        The value of the power to which 2 will be raised.

    :return:
        2 raised to the power of x. i.e., 2\ :sup:`x`

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/exp2.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_log:

.. rst-class:: classref-method

|vec_type| **log** ( |vec_type| x )

    Return the natural logarithm of the parameter, i.e. the value y which satisfies x=e\ :sup:`y`.
    The result is undefined if x ≤ 0.

    :param x:
        The value of which to take the natural logarithm.

    :return:
        the natural logarithm of x,

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/log.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_log2:

.. rst-class:: classref-method

|vec_type| **log2** ( |vec_type| x )

    Return the base 2 logarithm of the parameter.
    The result is undefined if x ≤ 0.

    :param x:
        the value of which to take the base 2 logarithm.

    :return:
        the base 2 logarithm of x, i.e. the value y which satisfies x=2\ :sup:`y`

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/log2.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_sqrt:

.. rst-class:: classref-method

|vec_type| **sqrt** ( |vec_type| x )

    Returns the square root of x.
    The result is undefined if x < 0.

    :param x:
        the value of which to take the square root.

    :return:
        <return_description/>

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/sqrt.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_inversesqrt:

.. rst-class:: classref-method

|vec_type| **inversesqrt** ( |vec_type| x )

    Returns the inverse of the square root of x.
    The result is undefined if x ≤ 0.


    :param x:
        The value of which to take the inverse of the square root.

    :return:
        The inverse of the square root of the parameter.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/inversesqrt.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_abs:

.. rst-class:: classref-method

|vec_type| **abs** ( |vec_type| x )

    Returns the absolute value of x. Returns X if X is positive or X * -1 if X is negative.

    :param x:
        the value of which to return the absolute.

    :return:
        the absolute value of x

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/abs.xhtml

.. rst-class:: classref-item-separator

----


.. rst-class:: classref-method

|vec_int_type| **abs** ( |vec_int_type| x )

    Returns the absolute value of x. Returns X if X is positive or X * -1 if X is negative.

    :param x:
        the value of which to return the absolute.

    :return:
        the absolute value of x

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/abs.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_sign:

.. rst-class:: classref-method

|vec_type| **sign** ( |vec_type| x )

    Returns -1.0 if x is less than 0.0, 0.0 if x is equal to 0.0, and +1.0 if x is greater than 0.0.

    :param x:
        the value from which to extract the sign.

    :return:
        1, -1 or 0.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/sign.xhtml

.. rst-class:: classref-item-separator

----



.. rst-class:: classref-method

|vec_int_type| **sign** ( |vec_int_type| x )

    Returns -1.0 if x is less than 0.0, 0.0 if x is equal to 0.0, and +1.0 if x is greater than 0.0.

    :param x:
        the value from which to extract the sign.

    :return:
        1, -1 or 0.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/sign.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_floor:

.. rst-class:: classref-method

|vec_type| **floor** ( |vec_type| x )

    Returns a value equal to the nearest integer that is less than or equal to x.

    :param x:
        the value to evaluate.

    :return:
        the nearest integer that is less than or equal to x.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/floor.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_round:

.. rst-class:: classref-method

|vec_type| **round** ( |vec_type| x )

    Returns a value equal to the nearest integer to x.

    The fraction 0.5 will round in a direction chosen by the implementation, presumably the direction
    that is fastest. This includes the possibility that round(x) returns the same value as roundEven(x)
    for all values of x.

    :param x:
        the value to evaluate.

    :return:
        the rounded value.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/round.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_roundEven:

.. rst-class:: classref-method

|vec_type| **roundEven** ( |vec_type| x )

    returns a value equal to the nearest integer to x.

    The fractional part of 0.5 will round toward the nearest even integer.
    For example, both 3.5 and 4.5 will round to 4.0.

    :param x:
        the value to evaluate.

    :return:
        the rounded value.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/roundEven.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_trunc:

.. rst-class:: classref-method

|vec_type| **trunc** ( |vec_type| x )

    Returns a value equal to the nearest integer to x whose absolute value is not larger than the absolute value of x.

    :param x:
        the value to evaluate.

    :return:
        the truncated value.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/trunc.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_ceil:

.. rst-class:: classref-method

|vec_type| **ceil** ( |vec_type| x )

    Returns a value equal to the nearest integer that is greater than or equal to x.

    :param x:
        the value to evaluate.

    :return:
        the ceiling-ed value.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/ceil.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_fract:

.. rst-class:: classref-method

|vec_type| **fract** ( |vec_type| x )

    Returns the fractional part of x.

    This is calculated as x - floor(x).

    :param x:
        the value to evaluate.

    :return:
        the fraction part of x.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/fract.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_mod:

.. rst-class:: classref-method

|vec_type| **mod** ( |vec_type| x, |vec_type| y )

    Returns the value of ``x modulo y``.
    This is also sometimes called the remainder.

    This is computed as ``x - y * floor(x/y)``.

    :param x:
        the value to evaluate.

    :return:
        the value of ``x modulo y``.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/mod.xhtml

.. rst-class:: classref-item-separator

----


.. rst-class:: classref-method

|vec_type| **mod** ( |vec_type| x, float y )

    Returns the value of ``x modulo y``.
    This is also sometimes called the remainder.

    This is computed as ``x - y * floor(x/y)``.

    :param x:
        the value to evaluate.

    :return:
        the value of ``x modulo y``.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/mod.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_modf:

.. rst-class:: classref-method

|vec_type| **modf** ( |vec_type| x, out |vec_type| i )

    Separates a floating point value x into its integer and fractional parts.

    The fractional part of the number is returned from the function.
    The integer part (as a floating point quantity) is returned in the output parameter i.

    :param x:
        the value to separate.

    :param out i:
        a variable that receives the integer part of the argument.

    :return:
        the fractional part of the number.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/modf.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_min:

.. rst-class:: classref-method

|vec_type| **min** ( |vec_type| a, |vec_type| b )

    Returns the minimum of the two parameters.

    It returns y if y is less than x, otherwise it returns x.

    :param a:
        the first value to compare.

    :param b:
        the second value to compare.

    :return:
        the minimum of the two parameters.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/min.xhtml

.. rst-class:: classref-item-separator

----


.. rst-class:: classref-method

|vec_type| **min** ( |vec_type| a, float b )

    Returns the minimum of the two parameters.

    It returns y if y is less than x, otherwise it returns x.

    :param a:
        the first value to compare.

    :param b:
        the second value to compare.

    :return:
        the minimum of the two parameters.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/min.xhtml

.. rst-class:: classref-item-separator

----



.. rst-class:: classref-method

|vec_int_type| **min** ( |vec_int_type| a, |vec_int_type| b )

    Returns the minimum of the two parameters.

    It returns y if y is less than x, otherwise it returns x.

    :param a:
        the first value to compare.

    :param b:
        the second value to compare.

    :return:
        the minimum of the two parameters.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/min.xhtml

.. rst-class:: classref-item-separator

----



.. rst-class:: classref-method

|vec_int_type| **min** ( |vec_int_type| a, int b )

    Returns the minimum of the two parameters.

    It returns y if y is less than x, otherwise it returns x.

    :param a:
        the first value to compare.

    :param b:
        the second value to compare.

    :return:
        the minimum of the two parameters.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/min.xhtml

.. rst-class:: classref-item-separator

----


.. rst-class:: classref-method

|vec_uint_type| **min** ( |vec_uint_type| a, |vec_uint_type| b )

    Returns the minimum of the two parameters.

    It returns y if y is less than x, otherwise it returns x.

    :param a:
        the first value to compare.

    :param b:
        the second value to compare.

    :return:
        the minimum of the two parameters.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/min.xhtml

.. rst-class:: classref-item-separator

----



.. rst-class:: classref-method

|vec_uint_type| **min** ( |vec_uint_type| a, uint b )

    Returns the minimum of the two parameters.

    It returns y if y is less than x, otherwise it returns x.

    :param a:
        the first value to compare.

    :param b:
        the second value to compare.

    :return:
        the minimum of the two parameters.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/min.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_max:

.. rst-class:: classref-method

|vec_type| **max** ( |vec_type| a, |vec_type| b )

    Returns the maximum of the two parameters.

    It returns y if y is greater than x, otherwise it returns x.

    :param a:
        the first value to compare.

    :param b:
        the second value to compare.

    :return:
        the maximum value.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/max.xhtml

.. rst-class:: classref-item-separator

----



.. rst-class:: classref-method

|vec_type| **max** ( |vec_type| a, float b )

    Returns the maximum of the two parameters.

    It returns y if y is greater than x, otherwise it returns x.

    :param a:
        the first value to compare.

    :param b:
        the second value to compare.

    :return:
        the maximum value.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/max.xhtml

.. rst-class:: classref-item-separator

----



.. rst-class:: classref-method

|vec_uint_type| **max** ( |vec_uint_type| a, |vec_uint_type| b )

    Returns the maximum of the two parameters.

    It returns y if y is greater than x, otherwise it returns x.

    :param a:
        the first value to compare.

    :param b:
        the second value to compare.

    :return:
        the maximum value.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/max.xhtml

.. rst-class:: classref-item-separator

----



.. rst-class:: classref-method

|vec_uint_type| **max** ( |vec_uint_type| a, uint b )

    Returns the maximum of the two parameters.

    It returns y if y is greater than x, otherwise it returns x.

    :param a:
        the first value to compare.

    :param b:
        the second value to compare.

    :return:
        the maximum value.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/max.xhtml

.. rst-class:: classref-item-separator

----



.. rst-class:: classref-method

|vec_int_type| **max** ( |vec_int_type| a, |vec_int_type| b )

    Returns the maximum of the two parameters.

    It returns y if y is greater than x, otherwise it returns x.

    :param a:
        the first value to compare.

    :param b:
        the second value to compare.

    :return:
        the maximum value.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/max.xhtml

.. rst-class:: classref-item-separator

----


.. rst-class:: classref-method

|vec_int_type| **max** ( |vec_int_type| a, int b )

    Returns the maximum of the two parameters.

    It returns y if y is greater than x, otherwise it returns x.

    :param a:
        the first value to compare.

    :param b:
        the second value to compare.

    :return:
        the maximum value.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/max.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_clamp:

.. rst-class:: classref-method

|vec_type| **clamp** ( |vec_type| x, |vec_type| min, |vec_type| max )

    Returns the value of x constrained to the range minVal to maxVal.

    The returned value is computed as min(max(x, minVal), maxVal).

    :param x:
        the value to constrain.

    :param min:
        the lower end of the range into which to constrain x.

    :param max:
        the upper end of the range into which to constrain x.

    :return:
        the constrained value.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/clamp.xhtml

.. rst-class:: classref-item-separator

----


.. rst-class:: classref-method

|vec_type| **clamp** ( |vec_type| x, float min, float max )

    Returns the value of x constrained to the range minVal to maxVal.

    The returned value is computed as min(max(x, minVal), maxVal).

    :param x:
        the value to constrain.

    :param min:
        the lower end of the range into which to constrain x.

    :param max:
        the upper end of the range into which to constrain x.

    :return:
        the constrained value.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/clamp.xhtml

.. rst-class:: classref-item-separator

----


.. rst-class:: classref-method

|vec_uint_type| **clamp** ( |vec_int_type| x, |vec_int_type| min, |vec_int_type| max )

    Returns the value of x constrained to the range minVal to maxVal.

    The returned value is computed as min(max(x, minVal), maxVal).

    :param x:
        the value to constrain.

    :param min:
        the lower end of the range into which to constrain x.

    :param max:
        the upper end of the range into which to constrain x.

    :return:
        the constrained value.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/clamp.xhtml

.. rst-class:: classref-item-separator

----


.. rst-class:: classref-method

|vec_uint_type| **clamp** ( |vec_int_type| x, float min, float max )

    Returns the value of x constrained to the range minVal to maxVal.

    The returned value is computed as min(max(x, minVal), maxVal).

    :param x:
        the value to constrain.

    :param min:
        the lower end of the range into which to constrain x.

    :param max:
        the upper end of the range into which to constrain x.

    :return:
        the constrained value.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/clamp.xhtml

.. rst-class:: classref-item-separator

----


.. rst-class:: classref-method

|vec_int_type| **clamp** ( |vec_type| x, |vec_type| min, |vec_type| max )

    Returns the value of x constrained to the range minVal to maxVal.

    The returned value is computed as min(max(x, minVal), maxVal).

    :param x:
        the value to constrain.

    :param min:
        the lower end of the range into which to constrain x.

    :param max:
        the upper end of the range into which to constrain x.

    :return:
        the constrained value.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/clamp.xhtml

.. rst-class:: classref-item-separator

----


.. rst-class:: classref-method

|vec_int_type| **clamp** ( |vec_type| x, float min, float max )

    Returns the value of x constrained to the range minVal to maxVal.

    The returned value is computed as min(max(x, minVal), maxVal).

    :param x:
        the value to constrain.

    :param min:
        the lower end of the range into which to constrain x.

    :param max:
        the upper end of the range into which to constrain x.

    :return:
        the constrained value.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/clamp.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_mix:

.. rst-class:: classref-method

|vec_type| **mix** ( |vec_type| a, |vec_type| b, |vec_type| c )

    Performs a linear interpolation between a and b using c to weight between them.

    computed as ``a × (1 − c) + b × c``.

    :param a:
        the start of the range in which to interpolate.

    :param b:
        the end of the range in which to interpolate.

    :param c:
        the value to use to interpolate between x and y.

    :return:
        The interpolated value.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/mix.xhtml

.. rst-class:: classref-item-separator

----


.. rst-class:: classref-method

|vec_type| **mix** ( |vec_type| a, |vec_type| b, float c )

    Performs a linear interpolation between a and b using c to weight between them.

    computed as ``a × (1 − c) + b × c``.

    :param a:
        the start of the range in which to interpolate.

    :param b:
        the end of the range in which to interpolate.

    :param c:
        the value to use to interpolate between x and y.

    :return:
        The interpolated value.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/mix.xhtml

.. rst-class:: classref-item-separator

----


.. rst-class:: classref-method

|vec_type| **mix** ( |vec_type| a, |vec_type| b, |vec_bool_type| c )

    Selects either value a or value b based on the value of c.
    For a component of c that is false, the corresponding component of a is returned.
    For a component of c that is true, the corresponding component of b is returned.
    Components of a and b that are not selected are allowed to be invalid floating-point values and will have no effect on the results.

    If a, b, and c are vector types the operation is performed component-wise.
    ie. ``mix(vec2(42, 314), vec2(9.8, 6e23), vec_bool_type(true, false)))`` will return ``vec2(9.8, 314)``.

    :param a:
        value returned when a is false.

    :param b:
        value returned when a is true.

    :param c:
        the value to use to interpolate between x and y.

    :return:
        The interpolated value.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/mix.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_fma:

.. rst-class:: classref-method

|vec_type| **fma** ( |vec_type| a, |vec_type| b, |vec_type| c )

    Performs, where possible, a fused multiply-add operation, returning a * b + c. In use cases where the
    return value is eventually consumed by a variable declared as precise:

     - fma() is considered a single operation, whereas the expression a * b + c consumed by a variable declared as precise is considered two operations.

     - The precision of fma() can differ from the precision of the expression a * b + c.

     - fma() will be computed with the same precision as any other fma() consumed by a precise variable,
       giving invariant results for the same input values of a, b and c.

    Otherwise, in the absence of precise consumption, there are no special constraints on the number of operations
    or difference in precision between fma() and the expression a * b + c.

    :param a:
        the first multiplicand.

    :param b:
        the second multiplicand.

    :param c:
        the value to be added to the result.

    :return:
        value of ``a * b + c``

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/fma.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_step:

.. rst-class:: classref-method

|vec_type| **step** ( |vec_type| a, |vec_type| b )

    Generates a step function by comparing b to a.

    Equivalent to ``if (b < a) { return 0.0; } else { return 1.0; }``.
    Or if vec_type is a vector, a vector where the above operation has been performed on each component of the input vectors.
    ie. ``step(vec2(4.2, 314), vec2(2.4, 980))`` would return ``vec2(step(a[0], b[0]), step(a[1], b[1]))``.

    For element i of the return value, 0.0 is returned if b[i] < a[i], and 1.0 is returned otherwise.

    :param a:
        the location of the edge of the step function.

    :param b:
        the value to be used to generate the step function.

    :return:
        0.0 or 1.0

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/step.xhtml

.. rst-class:: classref-item-separator

----


.. rst-class:: classref-method

|vec_type| **step** ( float a, |vec_type| b )

    Generates a step function by comparing b to a.

    Equivalent to ``if (b < a) { return 0.0; } else { return 1.0; }``.
    Or rather, the above operation will be performed on each component of the input vector.
    ie. ``step(4.2, vec2(2.4, 980))`` would return the equivalent of ``vec2(step(42, b[0]), step(42, b[1]))``.

    For element i of the return value, 0.0 is returned if b[i] < a[i], and 1.0 is returned otherwise.

    :param a:
        the location of the edge of the step function.

    :param b:
        the value to be used to generate the step function.

    :return:
        0.0 or 1.0

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/step.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_smoothstep:

.. rst-class:: classref-method

|vec_type| **smoothstep** ( |vec_type| a, |vec_type| b, |vec_type| c )

    Performs smooth Hermite interpolation between 0 and 1 when a < c < b.
    This is useful in cases where a threshold function with a smooth transition is desired.

    Smoothstep is equivalent to::

        vec_type t;
        t = clamp((c - a) / (b - a), 0.0, 1.0);
        return t * t * (3.0 - 2.0 * t);

    Results are undefined if a ≥ b.

    :param a:
        the value of the lower edge of the Hermite function.

    :param b:
        the value of the upper edge of the Hermite function.

    :param c:
        the source value for interpolation.

    :return:
        the interpolated value

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/smoothstep.xhtml

.. rst-class:: classref-item-separator

----


.. rst-class:: classref-method

|vec_type| **smoothstep** ( float a, float b, |vec_type| c )

    Performs smooth Hermite interpolation between 0 and 1 when a < c < b.
    This is useful in cases where a threshold function with a smooth transition is desired.

    Smoothstep is equivalent to::

        vec_type t;
        t = clamp((c - a) / (b - a), 0.0, 1.0);
        return t * t * (3.0 - 2.0 * t);

    Results are undefined if a ≥ b.

    :param a:
        the value of the lower edge of the Hermite function.

    :param b:
        the value of the upper edge of the Hermite function.

    :param c:
        the source value for interpolation.

    :return:
        the interpolated value

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/smoothstep.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_isnan:

.. rst-class:: classref-method

|vec_bool_type| **isnan** ( |vec_type| x )

    For each element i of the result, returns true if x[i] is positive
    or negative floating point NaN (Not a Number) and false otherwise.

    :param x:
        the value to test for NaN.

    :return:
        true or false

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/isnan.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_isinf:

.. rst-class:: classref-method

|vec_bool_type| **isinf** ( |vec_type| x )

    For each element i of the result, returns true if x[i] is positive or negative
    floating point infinity and false otherwise.

    :param x:
        the value to test for infinity.

    :return:
        true or false

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/isinf.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_floatBitsToInt:

.. rst-class:: classref-method

|vec_int_type| **floatBitsToInt** ( |vec_type| x )

    Returns the encoding of the floating-point parameters as int.

    The floating-point bit-level representation is preserved.

    :param x:
        the value whose floating point encoding to return.

    :return:
        the floating-point encoding of x.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/floatBitsToInt.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_floatBitsToUint:

.. rst-class:: classref-method

|vec_uint_type| **floatBitsToUint** ( |vec_type| x )

    Returns the encoding of the floating-point parameters as uint.

    The floating-point bit-level representation is preserved.

    :param x:
        the value whose floating point encoding to return.

    :return:
        the floating-point encoding of x.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/floatBitsToUint.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_intBitsToFloat:

.. rst-class:: classref-method

|vec_type| **intBitsToFloat** ( |vec_int_type| x )

    Converts a bit encoding to a floating-point value. Opposite of `floatBitsToInt<_shader_func_floatBitsToInt>`

    If the encoding of a NaN is passed in x, it will not signal and the resulting value will be undefined.

    If the encoding of a floating point infinity is passed in parameter x, the resulting floating-point value is
    the corresponding (positive or negative) floating point infinity.

    :param x:
        the bit encoding to return as a floating point value.

    :return:
        a floating point value

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/intBitsToFloat.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_uintBitsToFloat:

.. rst-class:: classref-method

|vec_type| **uintBitsToFloat** ( |vec_uint_type| x )

    Converts a bit encoding to a floating-point value. Opposite of `floatBitsToUint<_shader_func_floatBitsToUint>`

    If the encoding of a NaN is passed in x, it will not signal and the resulting value will be undefined.

    If the encoding of a floating point infinity is passed in parameter x, the resulting floating-point value is
    the corresponding (positive or negative) floating point infinity.

    :param x:
        the bit encoding to return as a floating point value.

    :return:
        a floating point value

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/uintBitsToFloat.xhtml

.. rst-class:: classref-item-separator

----







Geometric Functions
^^^^^^^^^^^^^^^^^^^

+------------+-------------------------------------------------------------------------------------------+----------------------------------------------------------+
| float      | :ref:`length<shader_func_length>` ( |vec_type| x)                                         | Vector length.                                           |
+------------+-------------------------------------------------------------------------------------------+----------------------------------------------------------+
| float      | :ref:`distance<shader_func_distance>` ( |vec_type| a, |vec_type| b)                       | Distance between vectors i.e ``length(a - b)``.          |
+------------+-------------------------------------------------------------------------------------------+----------------------------------------------------------+
| float      | :ref:`dot<shader_func_dot>` ( |vec_type| a, |vec_type| b)                                 | Dot product.                                             |
+------------+-------------------------------------------------------------------------------------------+----------------------------------------------------------+
| vec3       | :ref:`cross<shader_func_cross>` (vec3 a, vec3 b)                                          | Cross product.                                           |
+------------+-------------------------------------------------------------------------------------------+----------------------------------------------------------+
| |vec_type| | :ref:`normalize<shader_func_normalize>` ( |vec_type| x)                                   | Normalize to unit length.                                |
+------------+-------------------------------------------------------------------------------------------+----------------------------------------------------------+
| vec3       | :ref:`reflect<shader_func_reflect>` (vec3 I, vec3 N)                                      | Reflect.                                                 |
+------------+-------------------------------------------------------------------------------------------+----------------------------------------------------------+
| vec3       | :ref:`refract<shader_func_refract>` (vec3 I, vec3 N, float eta)                           | Refract.                                                 |
+------------+-------------------------------------------------------------------------------------------+----------------------------------------------------------+
| |vec_type| | :ref:`faceforward<shader_func_faceforward>` (|vec_type| N, |vec_type| I, |vec_type| Nref) | If ``dot(Nref, I)`` < 0, return ``N``, otherwise ``-N``. |
+------------+-------------------------------------------------------------------------------------------+----------------------------------------------------------+
| |mat_type| | :ref:`matrixCompMult<shader_func_matrixCompMult>` (|mat_type| x, |mat_type| y)            | Matrix component multiplication.                         |
+------------+-------------------------------------------------------------------------------------------+----------------------------------------------------------+
| |mat_type| | :ref:`outerProduct<shader_func_outerProduct>` ( |vec_type| column, |vec_type| row)        | Matrix outer product.                                    |
+------------+-------------------------------------------------------------------------------------------+----------------------------------------------------------+
| |mat_type| | :ref:`transpose<shader_func_transpose>` (|mat_type| m)                                    | Transpose matrix.                                        |
+------------+-------------------------------------------------------------------------------------------+----------------------------------------------------------+
| float      | :ref:`determinant<shader_func_determinant>` (|mat_type| m)                                | Matrix determinant.                                      |
+------------+-------------------------------------------------------------------------------------------+----------------------------------------------------------+
| |mat_type| | :ref:`inverse<shader_func_inverse>` (|mat_type| m)                                        | Inverse matrix.                                          |
+------------+-------------------------------------------------------------------------------------------+----------------------------------------------------------+

.. rst-class:: classref-section-separator

----------


Comparison Functions
^^^^^^^^^^^^^^^^^^^^

+-----------------+-------------------------------------------------------------------------------------+---------------------------------------------------------------+
| |vec_bool_type| | :ref:`lessThan<shader_func_lessThan>` ( |vec_type| x, |vec_type| y)                 | Bool vector comparison on < int/uint/float vectors.           |
+-----------------+-------------------------------------------------------------------------------------+---------------------------------------------------------------+
| |vec_bool_type| | :ref:`greaterThan<shader_func_greaterThan>` ( |vec_type| x, |vec_type| y)           | Bool vector comparison on > int/uint/float vectors.           |
+-----------------+-------------------------------------------------------------------------------------+---------------------------------------------------------------+
| |vec_bool_type| | :ref:`lessThanEqual<shader_func_lessThanEqual>` ( |vec_type| x, |vec_type| y)       | Bool vector comparison on <= int/uint/float vectors.          |
+-----------------+-------------------------------------------------------------------------------------+---------------------------------------------------------------+
| |vec_bool_type| | :ref:`greaterThanEqual<shader_func_greaterThanEqual>` ( |vec_type| x, |vec_type| y) | Bool vector comparison on >= int/uint/float vectors.          |
+-----------------+-------------------------------------------------------------------------------------+---------------------------------------------------------------+
| |vec_bool_type| | :ref:`equal<shader_func_equal>` ( |vec_type| x, |vec_type| y)                       | Bool vector comparison on == int/uint/float vectors.          |
+-----------------+-------------------------------------------------------------------------------------+---------------------------------------------------------------+
| |vec_bool_type| | :ref:`notEqual<shader_func_notEqual>` ( |vec_type| x, |vec_type| y)                 | Bool vector comparison on != int/uint/float vectors.          |
+-----------------+-------------------------------------------------------------------------------------+---------------------------------------------------------------+
| bool            | :ref:`any<shader_func_any>` ( |vec_bool_type| x)                                    | ``true`` if any component is ``true``, ``false`` otherwise.   |
+-----------------+-------------------------------------------------------------------------------------+---------------------------------------------------------------+
| bool            | :ref:`all<shader_func_all>` ( |vec_bool_type| x)                                    | ``true`` if all components are ``true``, ``false`` otherwise. |
+-----------------+-------------------------------------------------------------------------------------+---------------------------------------------------------------+
| |vec_bool_type| | :ref:`not<shader_func_not>` ( |vec_bool_type| x)                                    | Invert boolean vector.                                        |
+-----------------+-------------------------------------------------------------------------------------+---------------------------------------------------------------+

.. rst-class:: classref-section-separator

----



Texture Functions
^^^^^^^^^^^^^^^^^

+--------------+-----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| ivec2        | :ref:`textureSize<shader_func_textureSize>` ( |gsampler2D| s, int lod)                              | Get the size of a texture.                                          |
+--------------+-----------------------------------------------------------------------------------------------------+                                                                     |
| ivec2        | :ref:`textureSize<shader_func_textureSize>` (samplerCube s, int lod)                                | The LOD defines which mipmap level is used. An LOD value of ``0``   |
+--------------+-----------------------------------------------------------------------------------------------------+                                                                     |
| ivec2        | :ref:`textureSize<shader_func_textureSize>` (samplerCubeArray s, int lod)                           | will use the full resolution texture.                               |
+--------------+-----------------------------------------------------------------------------------------------------+                                                                     |
| ivec3        | :ref:`textureSize<shader_func_textureSize>` ( |gsampler2DArray| s, int lod)                         |                                                                     |
+--------------+-----------------------------------------------------------------------------------------------------+                                                                     |
| ivec3        | :ref:`textureSize<shader_func_textureSize>` ( |gsampler3D| s, int lod)                              |                                                                     |
+--------------+-----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| vec2         | :ref:`textureQueryLod<shader_func_textureQueryLod>` ( |gsampler2D| s, vec2 p)                       | Compute the level-of-detail that would be used to sample from a     |
+--------------+-----------------------------------------------------------------------------------------------------+ texture. The ``x`` component of the resulted value is the mipmap    |
| vec3         | :ref:`textureQueryLod<shader_func_textureQueryLod>` ( |gsampler2DArray| s, vec2 p)                  | array that would be accessed. The ``y`` component is computed       |
+--------------+-----------------------------------------------------------------------------------------------------+ level-of-detail relative to the base level (regardless of the       |
| vec2         | :ref:`textureQueryLod<shader_func_textureQueryLod>` ( |gsampler3D| s, vec3 p)                       | mipmap levels of the texture).                                      |
+--------------+-----------------------------------------------------------------------------------------------------+                                                                     |
| vec2         | :ref:`textureQueryLod<shader_func_textureQueryLod>` (samplerCube s, vec3 p)                         |                                                                     |
+--------------+-----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| int          | :ref:`textureQueryLevels<shader_func_textureQueryLevels>` ( |gsampler2D| s)                         | Get the number of accessible mipmap levels of a texture.            |
+--------------+-----------------------------------------------------------------------------------------------------+                                                                     |
| int          | :ref:`textureQueryLevels<shader_func_textureQueryLevels>` ( |gsampler2DArray| s)                    | If the texture is unassigned to a sampler, ``1`` is returned (Godot |
+--------------+-----------------------------------------------------------------------------------------------------+ always internally assigns a texture even to an empty sampler).      |
| int          | :ref:`textureQueryLevels<shader_func_textureQueryLevels>` ( |gsampler3D| s)                         |                                                                     |
+--------------+-----------------------------------------------------------------------------------------------------+                                                                     |
| int          | :ref:`textureQueryLevels<shader_func_textureQueryLevels>` (samplerCube s)                           |                                                                     |
+--------------+-----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| |gvec4_type| | :ref:`texture<shader_func_texture>` ( |gsampler2D| s, vec2 p [, float bias])                        | Perform a texture read.                                             |
+--------------+-----------------------------------------------------------------------------------------------------+                                                                     |
| |gvec4_type| | :ref:`texture<shader_func_texture>` ( |gsampler2DArray| s, vec3 p [, float bias])                   |                                                                     |
+--------------+-----------------------------------------------------------------------------------------------------+                                                                     |
| |gvec4_type| | :ref:`texture<shader_func_texture>` ( |gsampler3D| s, vec3 p [, float bias])                        |                                                                     |
+--------------+-----------------------------------------------------------------------------------------------------+                                                                     |
| vec4         | :ref:`texture<shader_func_texture>` (samplerCube s, vec3 p [, float bias])                          |                                                                     |
+--------------+-----------------------------------------------------------------------------------------------------+                                                                     |
| vec4         | :ref:`texture<shader_func_texture>` (samplerCubeArray s, vec4 p [, float bias])                     |                                                                     |
+--------------+-----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| |gvec4_type| | :ref:`textureProj<shader_func_textureProj>` ( |gsampler2D| s, vec3 p [, float bias])                | Perform a texture read with projection.                             |
+--------------+-----------------------------------------------------------------------------------------------------+                                                                     |
| |gvec4_type| | :ref:`textureProj<shader_func_textureProj>` ( |gsampler2D| s, vec4 p [, float bias])                |                                                                     |
+--------------+-----------------------------------------------------------------------------------------------------+                                                                     |
| |gvec4_type| | :ref:`textureProj<shader_func_textureProj>` ( |gsampler3D| s, vec4 p [, float bias])                |                                                                     |
+--------------+-----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| |gvec4_type| | :ref:`textureLod<shader_func_textureLod>` ( |gsampler2D| s, vec2 p, float lod)                      | Perform a texture read at custom mipmap.                            |
+--------------+-----------------------------------------------------------------------------------------------------+                                                                     |
| |gvec4_type| | :ref:`textureLod<shader_func_textureLod>` ( |gsampler2DArray| s, vec3 p, float lod)                 | The LOD defines which mipmap level is used. An LOD value of ``0.0`` |
+--------------+-----------------------------------------------------------------------------------------------------+                                                                     |
|              |                                                                                                     | will use the full resolution texture. If the texture lacks mipmaps, |
| |gvec4_type| | :ref:`textureLod<shader_func_textureLod>` ( |gsampler3D| s, vec3 p, float lod)                      | all LOD values will act like ``0.0``.                               |
+--------------+-----------------------------------------------------------------------------------------------------+                                                                     |
| vec4         | :ref:`textureLod<shader_func_textureLod>` (samplerCube s, vec3 p, float lod)                        |                                                                     |
+--------------+-----------------------------------------------------------------------------------------------------+                                                                     |
| vec4         | :ref:`textureLod<shader_func_textureLod>` (samplerCubeArray s, vec4 p, float lod)                   |                                                                     |
+--------------+-----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| |gvec4_type| | :ref:`textureProjLod<shader_func_textureProjLod>` ( |gsampler2D| s, vec3 p, float lod)              | Performs a texture read with projection/LOD.                        |
+--------------+-----------------------------------------------------------------------------------------------------+                                                                     |
| |gvec4_type| | :ref:`textureProjLod<shader_func_textureProjLod>` ( |gsampler2D| s, vec4 p, float lod)              | The LOD defines which mipmap level is used. An LOD value of ``0.0`` |
|              |                                                                                                     | will use the full resolution texture. If the texture lacks mipmaps, |
+--------------+-----------------------------------------------------------------------------------------------------+                                                                     |
| |gvec4_type| | :ref:`textureProjLod<shader_func_textureProjLod>` ( |gsampler3D| s, vec4 p, float lod)              | all LOD values will act like ``0.0``.                               |
+--------------+-----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| |gvec4_type| | :ref:`textureGrad<shader_func_textureGrad>` ( |gsampler2D| s, vec2 p, vec2 dPdx, vec2 dPdy)         | Performs a texture read with explicit gradients.                    |
+--------------+-----------------------------------------------------------------------------------------------------+                                                                     |
| |gvec4_type| | :ref:`textureGrad<shader_func_textureGrad>` ( |gsampler2DArray| s, vec3 p, vec2 dPdx, vec2 dPdy)    |                                                                     |
+--------------+-----------------------------------------------------------------------------------------------------+                                                                     |
| |gvec4_type| | :ref:`textureGrad<shader_func_textureGrad>` ( |gsampler3D| s, vec3 p, vec2 dPdx, vec2 dPdy)         |                                                                     |
+--------------+-----------------------------------------------------------------------------------------------------+                                                                     |
| vec4         | :ref:`textureGrad<shader_func_textureGrad>` (samplerCube s, vec3 p, vec3 dPdx, vec3 dPdy)           |                                                                     |
+--------------+-----------------------------------------------------------------------------------------------------+                                                                     |
| vec4         | :ref:`textureGrad<shader_func_textureGrad>` (samplerCubeArray s, vec3 p, vec3 dPdx, vec3 dPdy)      |                                                                     |
+--------------+-----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| |gvec4_type| | :ref:`textureProjGrad<shader_func_textureProjGrad>` ( |gsampler2D| s, vec3 p, vec2 dPdx, vec2 dPdy) | Performs a texture read with projection/LOD and with explicit       |
|              |                                                                                                     | gradients.                                                          |
+--------------+-----------------------------------------------------------------------------------------------------+                                                                     |
| |gvec4_type| | :ref:`textureProjGrad<shader_func_textureProjGrad>` ( |gsampler2D| s, vec4 p, vec2 dPdx, vec2 dPdy) |                                                                     |
+--------------+-----------------------------------------------------------------------------------------------------+                                                                     |
| |gvec4_type| | :ref:`textureProjGrad<shader_func_textureProjGrad>` ( |gsampler3D| s, vec4 p, vec3 dPdx, vec3 dPdy) |                                                                     |
+--------------+-----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| |gvec4_type| | :ref:`texelFetch<shader_func_texelFetch>` ( |gsampler2D| s, ivec2 p, int lod)                       | Fetches a single texel using integer coordinates.                   |
+--------------+-----------------------------------------------------------------------------------------------------+                                                                     |
| |gvec4_type| | :ref:`texelFetch<shader_func_texelFetch>` ( |gsampler2DArray| s, ivec3 p, int lod)                  | The LOD defines which mipmap level is used. An LOD value of ``0``   |
|              |                                                                                                     | will use the full resolution texture.                               |
+--------------+-----------------------------------------------------------------------------------------------------+                                                                     |
| |gvec4_type| | :ref:`texelFetch<shader_func_texelFetch>` ( |gsampler3D| s, ivec3 p, int lod)                       |                                                                     |
+--------------+-----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| |gvec4_type| | :ref:`textureGather<shader_func_textureGather>` ( |gsampler2D| s, vec2 p [, int comps])             | Gathers four texels from a texture.                                 |
|              |                                                                                                     | Use ``comps`` within range of 0..3 to                               |
+--------------+-----------------------------------------------------------------------------------------------------+                                                                     |
| |gvec4_type| | :ref:`textureGather<shader_func_textureGather>` ( |gsampler2DArray| s, vec3 p [, int comps])        | define which component (x, y, z, w) is returned.                    |
|              |                                                                                                     | If ``comps`` is not provided: 0 (or x-component) is used.           |
+--------------+-----------------------------------------------------------------------------------------------------+                                                                     |
| vec4         | :ref:`textureGather<shader_func_textureGather>` (samplerCube s, vec3 p [, int comps])               |                                                                     |
+--------------+-----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| |vec_type|   | :ref:`dFdx<shader_func_dFdx>` ( |vec_type| p)                                                       | Derivative in ``x`` using local differencing.                       |
|              |                                                                                                     | Internally, can use either ``dFdxCoarse`` or ``dFdxFine``, but the  |
|              |                                                                                                     | decision for which to use is made by the GPU driver.                |
+--------------+-----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| |vec_type|   | :ref:`dFdxCoarse<shader_func_dFdxCoarse>` ( |vec_type| p)                                           | Calculates derivative with respect to ``x`` window coordinate using |
|              |                                                                                                     | local differencing based on the value of ``p`` for the current      |
|              |                                                                                                     | fragment neighbour(s), and will possibly, but not necessarily,      |
|              |                                                                                                     | include the value for the current fragment.                         |
|              |                                                                                                     | Not available on ``gl_compatibility`` profile.                      |
+--------------+-----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| |vec_type|   | :ref:`dFdxFine<shader_func_dFdxFine>` ( |vec_type| p)                                               | Calculates derivative with respect to ``x`` window coordinate using |
|              |                                                                                                     | local differencing based on the value of ``p`` for the current      |
|              |                                                                                                     | fragment and its immediate neighbour(s).                            |
|              |                                                                                                     | Not available on ``gl_compatibility`` profile.                      |
+--------------+-----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| |vec_type|   | :ref:`dFdy<shader_func_dFdy>` ( |vec_type| p)                                                       | Derivative in ``y`` using local differencing.                       |
|              |                                                                                                     | Internally, can use either ``dFdyCoarse`` or ``dFdyFine``, but the  |
|              |                                                                                                     | decision for which to use is made by the GPU driver.                |
+--------------+-----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| |vec_type|   | :ref:`dFdyCoarse<shader_func_dFdyCoarse>` ( |vec_type| p)                                           | Calculates derivative with respect to ``y`` window coordinate using |
|              |                                                                                                     | local differencing based on the value of ``p`` for the current      |
|              |                                                                                                     | fragment neighbour(s), and will possibly, but not necessarily,      |
|              |                                                                                                     | include the value for the current fragment.                         |
|              |                                                                                                     | Not available on ``gl_compatibility`` profile.                      |
+--------------+-----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| |vec_type|   | :ref:`dFdyFine<shader_func_dFdyFine>` ( |vec_type| p)                                               | Calculates derivative with respect to ``y`` window coordinate using |
|              |                                                                                                     | local differencing based on the value of ``p`` for the current      |
|              |                                                                                                     | fragment and its immediate neighbour(s).                            |
|              |                                                                                                     | Not available on ``gl_compatibility`` profile.                      |
+--------------+-----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| |vec_type|   | :ref:`fwidth<shader_func_fwidth>` ( |vec_type| p)                                                   | Sum of absolute derivative in ``x`` and ``y``.                      |
|              |                                                                                                     | This is the equivalent of using ``abs(dFdx(p)) + abs(dFdy(p))``.    |
+--------------+-----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| |vec_type|   | :ref:`fwidthCoarse<shader_func_fwidthCoarse>` ( |vec_type| p)                                       | Sum of absolute derivative in ``x`` and ``y``.                      |
|              |                                                                                                     | Not available on ``gl_compatibility`` profile.                      |
+--------------+-----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| |vec_type|   | :ref:`fwidthFine<shader_func_fwidthFine>` ( |vec_type| p)                                           | Sum of absolute derivative in ``x`` and ``y``.                      |
|              |                                                                                                     | Not available on ``gl_compatibility`` profile.                      |
+--------------+-----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+

.. rst-class:: classref-section-separator

----




Packing/Unpacking Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^

+------+--------------------------------------------------------------+--------------------------------------------------------------+
| uint | :ref:`packHalf2x16<shader_func_packHalf2x16>` (vec2 v)       | Convert two 32-bit floating-point numbers into 16-bit        |
|      |                                                              | and pack them into a 32-bit unsigned integer and vice-versa. |
+------+--------------------------------------------------------------+                                                              +
| vec2 | :ref:`unpackHalf2x16<shader_func_unpackHalf2x16>` (uint v)   |                                                              |
+------+--------------------------------------------------------------+--------------------------------------------------------------+
| uint | :ref:`packUnorm2x16<shader_func_packUnorm2x16>` (vec2 v)     | Convert two 32-bit floating-point numbers (clamped           |
|      |                                                              | within 0..1 range) into 16-bit and pack them                 |
+------+--------------------------------------------------------------+                                                              +
| vec2 | :ref:`unpackUnorm2x16<shader_func_unpackUnorm2x16>` (uint v) | into a 32-bit unsigned integer and vice-versa.               |
+------+--------------------------------------------------------------+--------------------------------------------------------------+
| uint | :ref:`packSnorm2x16<shader_func_packSnorm2x16>` (vec2 v)     | Convert two 32-bit floating-point numbers (clamped           |
|      |                                                              | within -1..1 range) into 16-bit and pack them                |
+------+--------------------------------------------------------------+                                                              +
| vec2 | :ref:`unpackSnorm2x16<shader_func_unpackSnorm2x16>` (uint v) | into a 32-bit unsigned integer and vice-versa.               |
+------+--------------------------------------------------------------+--------------------------------------------------------------+
| uint | :ref:`packUnorm4x8<shader_func_packUnorm4x8>` (vec4 v)       | Convert four 32-bit floating-point numbers (clamped          |
|      |                                                              | within 0..1 range) into 8-bit and pack them                  |
+------+--------------------------------------------------------------+                                                              +
| vec4 | :ref:`unpackUnorm4x8<shader_func_unpackUnorm4x8>` (uint v)   | into a 32-bit unsigned integer and vice-versa.               |
+------+--------------------------------------------------------------+--------------------------------------------------------------+
| uint | :ref:`packSnorm4x8<shader_func_packSnorm4x8>` (vec4 v)       | Convert four 32-bit floating-point numbers (clamped          |
|      |                                                              | within -1..1 range) into 8-bit and pack them                 |
+------+--------------------------------------------------------------+                                                              +
| vec4 | :ref:`unpackSnorm4x8<shader_func_unpackSnorm4x8>` (uint v)   | into a 32-bit unsigned integer and vice-versa.               |
+------+--------------------------------------------------------------+--------------------------------------------------------------+

.. rst-class:: classref-section-separator

----




Bitwise operations
^^^^^^^^^^^^^^^^^^

+-----------------+----------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| |vec_int_type|  | :ref:`bitfieldExtract<shader_func_bitfieldExtract>` ( |vec_int_type| value, int offset, int bits)                                      | Extracts a range of bits from an integer.                           |
|                 |                                                                                                                                        |                                                                     |
| |vec_uint_type| | :ref:`bitfieldExtract<shader_func_bitfieldExtract>` ( |vec_uint_type| value, int offset, int bits)                                     |                                                                     |
+-----------------+----------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| |vec_int_type|  | :ref:`bitfieldInsert<shader_func_bitfieldInsert>` ( |vec_int_type| base, |vec_int_type| insert,                                        | Insert a range of bits into an integer.                             |
|                 | int offset, int bits)                                                                                                                  |                                                                     |
+-----------------+----------------------------------------------------------------------------------------------------------------------------------------+                                                                     |
| |vec_uint_type| | :ref:`bitfieldInsert<shader_func_bitfieldInsert>` (|vec_uint_type| base, |vec_uint_type| insert, int offset,                           |                                                                     |
|                 | int bits)                                                                                                                              |                                                                     |
+-----------------+----------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| |vec_int_type|  | :ref:`bitfieldReverse<shader_func_bitfieldReverse>` ( |vec_int_type| value)                                                            | Reverse the order of bits in an integer.                            |
+-----------------+----------------------------------------------------------------------------------------------------------------------------------------+                                                                     |
| |vec_uint_type| | :ref:`bitfieldReverse<shader_func_bitfieldReverse>` ( |vec_uint_type| value)                                                           |                                                                     |
+-----------------+----------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| |vec_int_type|  | :ref:`bitCount<shader_func_bitCount>` ( |vec_int_type| value)                                                                          | Counts the number of 1 bits in an integer.                          |
+-----------------+----------------------------------------------------------------------------------------------------------------------------------------+                                                                     |
| |vec_uint_type| | :ref:`bitCount<shader_func_bitCount>` ( |vec_uint_type| value)                                                                         |                                                                     |
+-----------------+----------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| |vec_int_type|  | :ref:`findLSB<shader_func_findLSB>` ( |vec_int_type| value)                                                                            | Find the index of the least significant bit set to 1 in an integer. |
+-----------------+----------------------------------------------------------------------------------------------------------------------------------------+                                                                     |
| |vec_uint_type| | :ref:`findLSB<shader_func_findLSB>` ( |vec_uint_type| value)                                                                           |                                                                     |
+-----------------+----------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| |vec_int_type|  | :ref:`findMSB<shader_func_findMSB>` ( |vec_int_type| value)                                                                            | Find the index of the most significant bit set to 1 in an integer.  |
+-----------------+----------------------------------------------------------------------------------------------------------------------------------------+                                                                     |
| |vec_uint_type| | :ref:`findMSB<shader_func_findMSB>` ( |vec_uint_type| value)                                                                           |                                                                     |
+-----------------+----------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| |void|          | :ref:`imulExtended<shader_func_imulExtended>` ( |vec_int_type| x, |vec_int_type| y,out |vec_int_type| msb, out |vec_int_type| lsb)     | Multiplies two 32-bit numbers and produce a 64-bit result.          |
+-----------------+----------------------------------------------------------------------------------------------------------------------------------------+                                                                     |
| |void|          | :ref:`umulExtended<shader_func_umulExtended>` (|vec_uint_type| x, |vec_uint_type| y, out |vec_uint_type| msb, out |vec_uint_type| lsb) |                                                                     |
+-----------------+----------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| |vec_uint_type| | :ref:`uaddCarry<shader_func_uaddCarry>` (|vec_uint_type| x, |vec_uint_type| y, out |vec_uint_type| carry)                              | Adds two unsigned integers and generates carry.                     |
+-----------------+----------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| |vec_uint_type| | :ref:`usubBorrow<shader_func_usubBorrow>` (|vec_uint_type| x, |vec_uint_type| y, out |vec_uint_type| borrow)                           | Subtracts two unsigned integers and generates borrow.               |
+-----------------+----------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| |vec_type|      | :ref:`ldexp<shader_func_ldexp>` (|vec_type| x, out |vec_int_type| exp)                                                                 | Assemble a floating-point number from a value and exponent.         |
+-----------------+----------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| |vec_type|      | :ref:`frexp<shader_func_frexp>` (|vec_type| x, out |vec_int_type| exp)                                                                 | Splits a floating-point number (``x``) into significand integral    |
|                 |                                                                                                                                        | components                                                          |
+-----------------+----------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+


.. rst-class:: classref-section-separator

----



.. |void| replace:: :abbr:`void (No return value.)`
.. |vec_type| replace:: :abbr:`vec_type (Any of: float, vec2, vec3, vec4)`
.. |vec_int_type| replace:: :abbr:`vec_int_type (Any of: int, ivec2, ivec3, ivec4)`
.. |vec_uint_type| replace:: :abbr:`vec_uint_type (Any of: float, uvec2, uvec3, uvec4)`
.. |vec_bool_type| replace:: :abbr:`vec_bool_type (Any of: bool, bvec2, bvec3, bvec4)`
.. |gsampler2D| replace:: :abbr:`gsampler2D (Any of: sampler2D, isampler2D, uSampler2D)`
.. |gsampler2DArray| replace:: :abbr:`gsampler2DArray (Any of: sampler2DArray, isampler2DArray, uSampler2DArray)`
.. |gsampler3D| replace:: :abbr:`gsampler3D (Any of: sampler3D, isampler3D, uSampler3D)`
.. |mat_type| replace:: :abbr:`mat_type (Any of: mat2, mat3, mat4)`
.. |gvec4_type| replace:: :abbr:`gvec4_type (Any of: vec4, ivec4, uvec4)`
