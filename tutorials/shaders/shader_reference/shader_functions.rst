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
    | mat_type        | mat2, mat3, or mat4                              | mat                      |
    +-----------------+--------------------------------------------------+--------------------------+
    | gsampler2D      | sampler2D, isampler2D, uSampler2D                |                          |
    +-----------------+--------------------------------------------------+--------------------------+
    | gsampler2DArray | sampler2DArray, isampler2DArray, uSampler2DArray |                          |
    +-----------------+--------------------------------------------------+--------------------------+
    | gsampler3D      | sampler3D, isampler3D, uSampler3D                |                          |
    +-----------------+--------------------------------------------------+--------------------------+


    If  any of these are specified for multiple parameters, they must all be the same type unless otherwise noted.


.. rst-class:: classref-reftable-group

Trigonometric Functions
------------------------------------------

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
        The return value is ``(π * degrees) / 180``.

    :rtype: |vec_type|

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
        The return value is ``(radians * 180) / π``.

    :rtype: |vec_type|

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/degrees.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_sin:

.. rst-class:: classref-method

vec_type sin( |vec_type| angle)

    Return the sine of the parameter.

    :param angle:
        The quantity, in radians, of which to return the sine

    :return:
        The return value is the trigonometric sine of ``angle``.

    :rtype: |vec_type|

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/sin.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_cos:

.. rst-class:: classref-method

vec_type cos( |vec_type| angle)

    Return the cosine of the parameter.

    :param angle:
        The quantity, in radians, of which to return the cosine.

    :return:
        The return value is the trigonometric cosine of ``angle``.

    :rtype: |vec_type|

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
        The return value is the trigonometric tangent of ``angle``.

    :rtype: |vec_type|

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
        The return value is the angle whose trigonometric sine is ``x`` and is
        in the range ``[-π/2, π/2]``.

    :rtype: |vec_type|

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
        The return value is the angle whose trigonometric cosine is ``x`` and
        is in the range ``[0, π]``.

    :rtype: |vec_type|

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
        The return value is the trigonometric arc-tangent of ``y_over_x`` and is
        in the range ``[-π/2, π/2]``.

    :rtype: |vec_type|

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
        The return value is the trigonometric arc-tangent of ``y/x`` and is in
        the range ``[-π, π]``.

    :rtype: |vec_type|

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
        The return value is the hyperbolic sine of ``x``.

    :rtype: |vec_type|

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
        The return value is the hyperbolic cosine of ``x``.

    :rtype: |vec_type|

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
        The return value is the hyperbolic tangent of ``x``.

    :rtype: |vec_type|

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
        The return value is the arc hyperbolic sine of ``x`` which is the
        inverse of sinh.

    :rtype: |vec_type|

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
        The return value is the arc hyperbolic cosine of ``x`` which is the
        inverse of cosh.

    :rtype: |vec_type|

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
        The return value is the arc hyperbolic tangent of ``x`` which is the
        inverse of tanh.

    :rtype: |vec_type|

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/atan.xhtml

.. rst-class:: classref-item-separator

----



Exponential and Common Math Functions
------------------------------------------

+-----------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| |vec_type|      | :ref:`pow<shader_func_pow>` ( |vec_type| x, |vec_type| y)                                   | Power (undefined if ``x`` < 0 or if ``x`` == 0 and ``y`` <= 0). |
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
| |vec_type|      | :ref:`sign<shader_func_sign>` ( |vec_type| x)                                               | Sign (returns ``1.0`` if positive, ``-1.0`` if negative,        |
+-----------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| |vec_int_type|  | :ref:`sign<shader_func_sign>` ( |vec_int_type| x)                                           | Sign (returns ``1`` if positive, ``-1`` if negative,            |
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
| |vec_type|      | :ref:`modf<shader_func_modf>` (vecType x, out |vec_type| i)                                 | Fractional of ``x``, with ``i`` as integer part.                |
+-----------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| |vec_type|      | :ref:`min<shader_func_min>` ( |vec_type| a, |vec_type| b)                                   | Lowest value between ``a`` and ``b``.                           |
+-----------------+---------------------------------------------------------------------------------------------+                                                                 |
| |vec_type|      | :ref:`min<shader_func_min>` ( |vec_type| a, float b)                                        |                                                                 |
+-----------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| |vec_int_type|  | :ref:`min<shader_func_min>` ( |vec_int_type| a, |vec_int_type| b)                           | Lowest value between ``a`` and ``b``.                           |
+-----------------+---------------------------------------------------------------------------------------------+                                                                 |
| |vec_int_type|  | :ref:`min<shader_func_min>` ( |vec_int_type| a, int b)                                      |                                                                 |
+-----------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| |vec_uint_type| | :ref:`min<shader_func_min>` ( |vec_uint_type| a, |vec_uint_type| b)                         | Lowest value between ``a`` and ``b``.                           |
+-----------------+---------------------------------------------------------------------------------------------+                                                                 |
| |vec_uint_type| | :ref:`min<shader_func_min>` ( |vec_uint_type| a, uint b)                                    |                                                                 |
+-----------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| |vec_type|      | :ref:`max<shader_func_max>` ( |vec_type| a, |vec_type| b)                                   | Highest value between ``a`` and ``b``.                          |
+-----------------+---------------------------------------------------------------------------------------------+                                                                 |
| |vec_type|      | :ref:`max<shader_func_max>` ( |vec_type| a, float b)                                        |                                                                 |
+-----------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| |vec_uint_type| | :ref:`max<shader_func_max>` ( |vec_uint_type| a, |vec_uint_type| b)                         | Highest value between ``a`` and ``b``.                          |
+-----------------+---------------------------------------------------------------------------------------------+                                                                 |
| |vec_uint_type| | :ref:`max<shader_func_max>` ( |vec_uint_type| a, uint b)                                    |                                                                 |
+-----------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| |vec_int_type|  | :ref:`max<shader_func_max>` ( |vec_int_type| a, |vec_int_type| b)                           | Highest value between ``a`` and ``b``.                          |
+-----------------+---------------------------------------------------------------------------------------------+                                                                 |
| |vec_int_type|  | :ref:`max<shader_func_max>` ( |vec_int_type| a, int b)                                      |                                                                 |
+-----------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| |vec_type|      | :ref:`clamp<shader_func_clamp>` (vecType x, |vec_type| min, |vec_type| max)                 | Clamp ``x`` between ``min`` and ``max`` (inclusive).            |
+-----------------+---------------------------------------------------------------------------------------------+                                                                 |
| |vec_type|      | :ref:`clamp<shader_func_clamp>` ( |vec_type| x, float min, float max)                       |                                                                 |
+-----------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| |vec_uint_type| | :ref:`clamp<shader_func_clamp>` ( |vec_int_type| x, |vec_int_type| min, |vec_int_type| max) | Clamp ``x`` between ``min`` and ``max`` (inclusive).            |
+-----------------+---------------------------------------------------------------------------------------------+                                                                 |
| |vec_uint_type| | ref:`clamp<shader_func_clamp>` ( |vec_int_type| x, float min, float max)                    |                                                                 |
+-----------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| |vec_int_type|  | :ref:`clamp<shader_func_clamp>` (vecType x, |vec_type| min, |vec_type| max)                 | Clamp ``x`` between ``min`` and ``max`` (inclusive).            |
+-----------------+---------------------------------------------------------------------------------------------+                                                                 |
| |vec_int_type|  | :ref:`clamp<shader_func_clamp>` ( |vec_type| x, float min, float max)                       |                                                                 |
+-----------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| float           | :ref:`mix<shader_func_mix>` (float a, float b, float c)                                     | Linear interpolate between ``a`` and ``b`` by ``c``.            |
+-----------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| |vec_type|      | :ref:`mix<shader_func_mix>` (vecType a, |vec_type| b, float c)                              | Linear interpolate between ``a`` and ``b`` by ``c``.            |
+-----------------+---------------------------------------------------------------------------------------------+                                                                 |
| |vec_type|      | :ref:`mix<shader_func_mix>` (vecType a, |vec_type| b, |vec_type| c)                         |                                                                 |
+-----------------+---------------------------------------------------------------------------------------------+                                                                 |
| |vec_type|      |     :ref:`mix<shader_func_mix>` (vecType a, |vec_type| b, |vec_bool_type| c)                |                                                                 |
+-----------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| |vec_type|      | :ref:`fma<shader_func_fma>` (vecType a, |vec_type| b, |vec_type| c)                         | Fused multiply-add operation: ``(a * b + c)``                   |
+-----------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| |vec_type|      | :ref:`step<shader_func_step>` ( |vec_type| a, |vec_type| b)                                 | ``b[i] < a[i] ? 0.0 : 1.0``.                                    |
+-----------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| |vec_type|      | :ref:`step<shader_func_step>` (float a, |vec_type| b)                                       | ``b[i] < a ? 0.0 : 1.0``.                                       |
+-----------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| |vec_type|      | :ref:`smoothstep<shader_func_smoothstep>` (vecType a, |vec_type| b, |vec_type| c)           | Hermite interpolate between ``a`` and ``b`` by ``c``.           |
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





Geometric Functions
------------------------------------------

+------------+----------------------------------------------------------------------------------------+----------------------------------------------------------+
| float      | :ref:`length<shader_func_length>` ( |vec_type| x)                                      | Vector length.                                           |
+------------+----------------------------------------------------------------------------------------+----------------------------------------------------------+
| float      | :ref:`distance<shader_func_distance>` ( |vec_type| a, |vec_type| b)                    | Distance between vectors i.e ``length(a - b)``.          |
+------------+----------------------------------------------------------------------------------------+----------------------------------------------------------+
| float      | :ref:`dot<shader_func_dot>` ( |vec_type| a, |vec_type| b)                              | Dot product.                                             |
+------------+----------------------------------------------------------------------------------------+----------------------------------------------------------+
| vec3       | :ref:`cross<shader_func_cross>` (vec3 a, vec3 b)                                       | Cross product.                                           |
+------------+----------------------------------------------------------------------------------------+----------------------------------------------------------+
| |vec_type| | :ref:`normalize<shader_func_normalize>` ( |vec_type| x)                                | Normalize to unit length.                                |
+------------+----------------------------------------------------------------------------------------+----------------------------------------------------------+
| vec3       | :ref:`reflect<shader_func_reflect>` (vec3 I, vec3 N)                                   | Reflect.                                                 |
+------------+----------------------------------------------------------------------------------------+----------------------------------------------------------+
| vec3       | :ref:`refract<shader_func_refract>` (vec3 I, vec3 N, float eta)                        | Refract.                                                 |
+------------+----------------------------------------------------------------------------------------+----------------------------------------------------------+
| |vec_type| | :ref:`faceforward<shader_func_faceforward>` (vecType N, |vec_type| I, |vec_type| Nref) | If ``dot(Nref, I)`` < 0, return ``N``, otherwise ``-N``. |
+------------+----------------------------------------------------------------------------------------+----------------------------------------------------------+
| |mat_type| | :ref:`matrixCompMult<shader_func_matrixCompMult>` (|mat_type| x, |mat_type| y)         | Matrix component multiplication.                         |
+------------+----------------------------------------------------------------------------------------+----------------------------------------------------------+
| |mat_type| | :ref:`outerProduct<shader_func_outerProduct>` ( |vec_type| column, |vec_type| row)     | Matrix outer product.                                    |
+------------+----------------------------------------------------------------------------------------+----------------------------------------------------------+
| |mat_type| | :ref:`transpose<shader_func_transpose>` (|mat_type| m)                                 | Transpose matrix.                                        |
+------------+----------------------------------------------------------------------------------------+----------------------------------------------------------+
| float      | :ref:`determinant<shader_func_determinant>` (|mat_type| m)                             | Matrix determinant.                                      |
+------------+----------------------------------------------------------------------------------------+----------------------------------------------------------+
| |mat_type| | :ref:`inverse<shader_func_inverse>` (|mat_type| m)                                     | Inverse matrix.                                          |
+------------+----------------------------------------------------------------------------------------+----------------------------------------------------------+

.. rst-class:: classref-section-separator

----------


Comparison Functions
-------------------------

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
------------------------------------------

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
------------------------------------------

+------+--------------------------------------------------------------+--------------------------------------------------------------+
| uint | :ref:`packHalf2x16<shader_func_packHalf2x16>` (vec2 v)       | Convert two 32-bit floating-point numbers into 16-bit        |
|      |                                                              | and pack them into a 32-bit unsigned integer and vice-versa. |
| vec2 | :ref:`unpackHalf2x16<shader_func_unpackHalf2x16>` (uint v)   |                                                              |
+------+--------------------------------------------------------------+--------------------------------------------------------------+
| uint | :ref:`packUnorm2x16<shader_func_packUnorm2x16>` (vec2 v)     | Convert two 32-bit floating-point numbers (clamped           |
|      |                                                              | within 0..1 range) into 16-bit and pack them                 |
| vec2 | :ref:`unpackUnorm2x16<shader_func_unpackUnorm2x16>` (uint v) | into a 32-bit unsigned integer and vice-versa.               |
+------+--------------------------------------------------------------+--------------------------------------------------------------+
| uint | :ref:`packSnorm2x16<shader_func_packSnorm2x16>` (vec2 v)     | Convert two 32-bit floating-point numbers (clamped           |
|      |                                                              | within -1..1 range) into 16-bit and pack them                |
| vec2 | :ref:`unpackSnorm2x16<shader_func_unpackSnorm2x16>` (uint v) | into a 32-bit unsigned integer and vice-versa.               |
+------+--------------------------------------------------------------+--------------------------------------------------------------+
| uint | :ref:`packUnorm4x8<shader_func_packUnorm4x8>` (vec4 v)       | Convert four 32-bit floating-point numbers (clamped          |
|      |                                                              | within 0..1 range) into 8-bit and pack them                  |
| vec4 | :ref:`unpackUnorm4x8<shader_func_unpackUnorm4x8>` (uint v)   | into a 32-bit unsigned integer and vice-versa.               |
+------+--------------------------------------------------------------+--------------------------------------------------------------+
| uint | :ref:`packSnorm4x8<shader_func_packSnorm4x8>` (vec4 v)       | Convert four 32-bit floating-point numbers (clamped          |
|      |                                                              | within -1..1 range) into 8-bit and pack them                 |
| vec4 | :ref:`unpackSnorm4x8<shader_func_unpackSnorm4x8>` (uint v)   | into a 32-bit unsigned integer and vice-versa.               |
+------+--------------------------------------------------------------+--------------------------------------------------------------+

.. rst-class:: classref-section-separator

----




Bitwise operations
------------------------------------------

+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| |vec_int_type|  | :ref:`bitfieldExtract<shader_func_bitfieldExtract>` ( |vec_int_type| value, int offset, int bits)                                                    | Extracts a range of bits from an integer.                           |
|                 |                                                                                                                                                      |                                                                     |
| |vec_uint_type| | :ref:`bitfieldExtract<shader_func_bitfieldExtract>` ( |vec_uint_type| value, int offset, int bits)                                                   |                                                                     |
+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| |vec_int_type|  | :ref:`bitfieldInsert<shader_func_bitfieldInsert>` ( |vec_int_type| base, |vec_int_type| insert,                                                      | Insert a range of bits into an integer.                             |
|                 | int offset, int bits)                                                                                                                                |                                                                     |
+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------+                                                                     |
| |vec_uint_type| | :ref:`bitfieldInsert<shader_func_bitfieldInsert>` (|vec_uint_type| base, |vec_uint_type| insert, int offset,                                         |                                                                     |
|                 | int bits)                                                                                                                                            |                                                                     |
+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| |vec_int_type|  | :ref:`bitfieldReverse<shader_func_bitfieldReverse>` ( |vec_int_type| value)                                                                          | Reverse the order of bits in an integer.                            |
|                 |                                                                                                                                                      |                                                                     |
| |vec_uint_type| | :ref:`bitfieldReverse<shader_func_bitfieldReverse>` ( |vec_uint_type| value)                                                                         |                                                                     |
+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| |vec_int_type|  | :ref:`bitCount<shader_func_bitCount>` ( |vec_int_type| value)                                                                                        | Counts the number of 1 bits in an integer.                          |
|                 |                                                                                                                                                      |                                                                     |
| |vec_uint_type| | :ref:`bitCount<shader_func_bitCount>` ( |vec_uint_type| value)                                                                                       |                                                                     |
+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| |vec_int_type|  | :ref:`findLSB<shader_func_findLSB>` ( |vec_int_type| value)                                                                                          | Find the index of the least significant bit set to 1 in an integer. |
|                 |                                                                                                                                                      |                                                                     |
| |vec_uint_type| | :ref:`findLSB<shader_func_findLSB>` ( |vec_uint_type| value)                                                                                         |                                                                     |
+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| |vec_int_type|  | :ref:`findMSB<shader_func_findMSB>` ( |vec_int_type| value)                                                                                          | Find the index of the most significant bit set to 1 in an integer.  |
|                 |                                                                                                                                                      |                                                                     |
| |vec_uint_type| | :ref:`findMSB<shader_func_findMSB>` ( |vec_uint_type| value)                                                                                         |                                                                     |
+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| |void|          | :ref:`imulExtended<shader_func_imulExtended>` ( |vec_int_type| x, |vec_int_type| y,out |vec_int_type| msb, out |vec_int_type| lsb)                   | Multiplies two 32-bit numbers and produce a 64-bit result.          |
+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------+                                                                     |
| |void|          | :ref:`umulExtended<shader_func_umulExtended>` (|vec_uint_type| x, |vec_uint_type| y, out |vec_uint_type| msb, out |vec_uint_type| lsb)               |                                                                     |
+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| |vec_uint_type| | :ref:`uaddCarry<shader_func_uaddCarry>` (|vec_uint_type| x, |vec_uint_type| y, out |vec_uint_type| carry)                                            | Adds two unsigned integers and generates carry.                     |
+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| |vec_uint_type| | :ref:`usubBorrow<shader_func_usubBorrow>` (|vec_uint_type| x, |vec_uint_type| y, out |vec_uint_type| borrow)                                         | Subtracts two unsigned integers and generates borrow.               |
+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| |vec_type|      | :ref:`ldexp<shader_func_ldexp>` (vecType x, out |vec_int_type| exp)                                                                                  | Assemble a floating-point number from a value and exponent.         |
+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| |vec_type|      | :ref:`frexp<shader_func_frexp>` (vecType x, out |vec_int_type| exp)                                                                                  | Splits a floating-point number (``x``) into significand integral    |
|                 |                                                                                                                                                      | components                                                          |
+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+


.. rst-class:: classref-section-separator

----


vec_type pow( |vec_type| x, |vec_type| y)

    Raises ``x`` to the power of ``y``.

    The result is undefined if ``x < 0`` or  if ``x == 0`` and ``y <= 0``.

    :param x:
        The value to be raised to the power ``y``.

    :param y:
        The power to which ``x`` will be raised.

    :return:
        Returns the value of ``x`` raised to the ``y`` power.

    :rtype: |vec_type|

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/pow.xhtml

.. |void| replace:: :abbr:`void (No return value.)`
.. |vec_type| replace:: :abbr:`vec_type (Any of: float, vec2, vec3, vec4)`
.. |vec_int_type| replace:: :abbr:`vec_int_type (Any of: int, ivec2, ivec3, ivec4)`
.. |vec_uint_type| replace:: :abbr:`vec_uint_type (Any of: float, uvec2, uvec3, uvec4)`
.. |vec_bool_type| replace:: :abbr:`vec_bool_type (Any of: bool, bvec2, bvec3, bvec4)`
.. |gsampler2D| replace:: :abbr:`gsampler2D (Any of: sampler2D, isampler2D, uSampler2D)`
.. |gsampler2DArray| replace:: :abbr:`gsampler2DArray (Any of: sampler2DArray, isampler2DArray, uSampler2DArray)`
.. |gsampler3D| replace:: :abbr:`gsampler3D (Any of: sampler3D, isampler3D, uSampler3D)`
.. |mat_type| replace:: :abbr:`mat_type (Any of: mat2, mat3, mat4)`
