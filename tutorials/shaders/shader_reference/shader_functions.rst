.. _doc_shader_functions:

Built-in functions
==================

Godot supports a large number of built-in functions, conforming roughly to the
GLSL ES 3.0 specification.

.. note::
    The following type aliases only used in documentation to reduce repetitive function declarations.
    They can each refer to any of several actual types.

    +-----------------+-----------------------------------------------------+--------------------------+
    | alias           | actual types                                        | glsl documentation alias |
    +=================+=====================================================+==========================+
    | vec_type        | float, vec2, vec3, or vec4                          | genType                  |
    +-----------------+-----------------------------------------------------+--------------------------+
    | vec_int_type    | int, ivec2, ivec3, or ivec4                         | genIType                 |
    +-----------------+-----------------------------------------------------+--------------------------+
    | vec_uint_type   | uint, uvec2, uvec3, or uvec4                        | genUType                 |
    +-----------------+-----------------------------------------------------+--------------------------+
    | vec_bool_type   | bool, bvec2, bvec3, or bvec4                        | genBType                 |
    +-----------------+-----------------------------------------------------+--------------------------+
    | mat_type        | mat2, mat3, or mat4                                 | mat                      |
    +-----------------+-----------------------------------------------------+--------------------------+
    | gvec4_type      | vec4, ivec4, or uvec4                               | gvec4                    |
    +-----------------+-----------------------------------------------------+--------------------------+
    | gsampler2D      | sampler2D, isampler2D, or uSampler2D                | gsampler2D               |
    +-----------------+-----------------------------------------------------+--------------------------+
    | gsampler2DArray | sampler2DArray, isampler2DArray, or uSampler2DArray | gsampler2DArray          |
    +-----------------+-----------------------------------------------------+--------------------------+
    | gsampler3D      | sampler3D, isampler3D, or uSampler3D                | gsampler3D               |
    +-----------------+-----------------------------------------------------+--------------------------+

    If any of these are specified for multiple parameters, they must all be the same type unless otherwise noted.

.. _shading_componentwise:

.. note::
    Many functions that accept one or more vectors or matrices perform the described function on each component of the vector/matrix.
    Some examples:

    .. table::
        :class: nowrap-col2 nowrap-col1
        :widths: auto

        +---------------------------------------+-----------------------------------------------------+
        | Operation                             | Equivalent Scalar Operation                         |
        +=======================================+=====================================================+
        | ``sqrt(vec2(4, 64))``                 | ``vec2(sqrt(4), sqrt(64))``                         |
        +---------------------------------------+-----------------------------------------------------+
        | ``min(vec2(3, 4), 1)``                | ``vec2(min(3, 1), min(4, 1))``                      |
        +---------------------------------------+-----------------------------------------------------+
        | ``min(vec3(1, 2, 3),vec3(5, 1, 3))``  | ``vec3(min(1, 5), min(2, 1), min(3, 3))``           |
        +---------------------------------------+-----------------------------------------------------+
        | ``pow(vec3(3, 8, 5 ), 2)``            | ``vec3(pow(3, 2), pow(8, 2), pow(5, 2))``           |
        +---------------------------------------+-----------------------------------------------------+
        | ``pow(vec3(3, 8, 5), vec3(1, 2, 4))`` | ``vec3(pow(3, 1), pow(8, 2), pow(5, 4))``           |
        +---------------------------------------+-----------------------------------------------------+

    The `GLSL Language Specification <http://www.opengl.org/registry/doc/GLSLangSpec.4.30.6.pdf>`_ says under section 5.10 Vector and Matrix Operations:

        With a few exceptions, operations are component-wise. Usually, when an operator operates on a
        vector or matrix, it is operating independently on each component of the vector or matrix,
        in a component-wise fashion. [...] The exceptions are matrix multiplied by vector,
        vector multiplied by matrix, and matrix multiplied by matrix. These do not operate component-wise,
        but rather perform the correct linear algebraic multiply.

These function descriptions are adapted and modified from
`official OpenGL documentation <https://registry.khronos.org/OpenGL-Refpages/gl4/>`__
originally published by Khronos Group under the
`Open Publication License <https://opencontent.org/openpub>`__.
Each function description links to the corresponding official OpenGL
documentation. Modification history for this page can be found on
`GitHub <https://github.com/godotengine/godot-docs/blob/master/tutorials/shaders/shader_reference/shader_functions.rst>`__.

.. rst-class:: classref-section-separator

----



.. rst-class:: classref-reftable-group

Trigonometric functions
-----------------------

.. table::
    :class: nowrap-col2
    :widths: auto

    +-----------------+-----------------------------------------------------------------+-----------------------------+
    |    Return Type  |                          Function                               | Description / Return value  |
    +=================+=================================================================+=============================+
    | |vec_type|      | :ref:`radians<shader_func_radians>`\ (\ |vec_type| degrees)     | Convert degrees to radians. |
    +-----------------+-----------------------------------------------------------------+-----------------------------+
    | |vec_type|      | :ref:`degrees<shader_func_degrees>`\ (\ |vec_type| radians)     | Convert radians to degrees. |
    +-----------------+-----------------------------------------------------------------+-----------------------------+
    | |vec_type|      | :ref:`sin<shader_func_sin>`\ (\ |vec_type| x)                   | Sine.                       |
    +-----------------+-----------------------------------------------------------------+-----------------------------+
    | |vec_type|      | :ref:`cos<shader_func_cos>`\ (\ |vec_type| x)                   | Cosine.                     |
    +-----------------+-----------------------------------------------------------------+-----------------------------+
    | |vec_type|      | :ref:`tan<shader_func_tan>`\ (\ |vec_type| x)                   | Tangent.                    |
    +-----------------+-----------------------------------------------------------------+-----------------------------+
    | |vec_type|      | :ref:`asin<shader_func_asin>`\ (\ |vec_type| x)                 | Arc sine.                   |
    +-----------------+-----------------------------------------------------------------+-----------------------------+
    | |vec_type|      | :ref:`acos<shader_func_acos>`\ (\ |vec_type| x)                 | Arc cosine.                 |
    +-----------------+-----------------------------------------------------------------+-----------------------------+
    | | |vec_type|    | | :ref:`atan<shader_func_atan>`\ (\ |vec_type| y_over_x)        | Arc tangent.                |
    | | |vec_type|    | | :ref:`atan<shader_func_atan2>`\ (\ |vec_type| y, |vec_type| x)|                             |
    +-----------------+-----------------------------------------------------------------+-----------------------------+
    | |vec_type|      | :ref:`sinh<shader_func_sinh>`\ (\ |vec_type| x)                 | Hyperbolic sine.            |
    +-----------------+-----------------------------------------------------------------+-----------------------------+
    | |vec_type|      | :ref:`cosh<shader_func_cosh>`\ (\ |vec_type| x)                 | Hyperbolic cosine.          |
    +-----------------+-----------------------------------------------------------------+-----------------------------+
    | |vec_type|      | :ref:`tanh<shader_func_tanh>`\ (\ |vec_type| x)                 | Hyperbolic tangent.         |
    +-----------------+-----------------------------------------------------------------+-----------------------------+
    | |vec_type|      | :ref:`asinh<shader_func_asinh>`\ (\ |vec_type| x)               | Arc hyperbolic sine.        |
    +-----------------+-----------------------------------------------------------------+-----------------------------+
    | |vec_type|      | :ref:`acosh<shader_func_acosh>`\ (\ |vec_type| x)               | Arc hyperbolic cosine.      |
    +-----------------+-----------------------------------------------------------------+-----------------------------+
    | |vec_type|      | :ref:`atanh<shader_func_atanh>`\ (\ |vec_type| x)               | Arc hyperbolic tangent.     |
    +-----------------+-----------------------------------------------------------------+-----------------------------+


.. rst-class:: classref-descriptions-group

Trigonometric function descriptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _shader_func_radians:

.. rst-class:: classref-method

|vec_type| **radians**\ (\ |vec_type| degrees) :ref:`🔗<shader_func_radians>`

    |componentwise|

    Converts a quantity specified in degrees into radians, with the formula
    ``degrees * (PI / 180)``.

    :param degrees:
        The quantity, in degrees, to be converted to radians.

    :return:
        The input ``degrees`` converted to radians.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/radians.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_degrees:

.. rst-class:: classref-method

|vec_type| **degrees**\ (\ |vec_type| radians) :ref:`🔗<shader_func_degrees>`

    |componentwise|

    Converts a quantity specified in radians into degrees, with the formula
    ``radians * (180 / PI)``

    :param radians:
        The quantity, in radians, to be converted to degrees.

    :return:
        The input ``radians`` converted to degrees.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/degrees.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_sin:

.. rst-class:: classref-method

|vec_type| **sin**\ (\ |vec_type| angle) :ref:`🔗<shader_func_sin>`

    |componentwise|

    Returns the trigonometric sine of ``angle``.

    :param angle:
        The quantity, in radians, of which to return the sine.

    :return:
        The sine of ``angle``.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/sin.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_cos:

.. rst-class:: classref-method

|vec_type| **cos**\ (\ |vec_type| angle) :ref:`🔗<shader_func_cos>`

    |componentwise|

    Returns the trigonometric cosine of ``angle``.

    :param angle:
        The quantity, in radians, of which to return the cosine.

    :return:
        The cosine of ``angle``.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/cos.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_tan:

.. rst-class:: classref-method

|vec_type| **tan**\ (\ |vec_type| angle) :ref:`🔗<shader_func_tan>`

    |componentwise|

    Returns the trigonometric tangent of ``angle``.

    :param angle:
        The quantity, in radians, of which to return the tangent.

    :return:
        The tangent of ``angle``.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/tan.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_asin:

.. rst-class:: classref-method

|vec_type| **asin**\ (\ |vec_type| x) :ref:`🔗<shader_func_asin>`

    |componentwise|

    Arc sine, or inverse sine.
    Calculates the angle whose sine is ``x`` and is in the range ``[-PI/2, PI/2]``.
    The result is undefined if ``x < -1`` or ``x > 1``.

    :param x:
        The value whose arc sine to return.
    :return:
        The angle whose trigonometric sine is ``x``.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/asin.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_acos:

.. rst-class:: classref-method

|vec_type| **acos**\ (\ |vec_type| x) :ref:`🔗<shader_func_acos>`

    |componentwise|

    Arc cosine, or inverse cosine.
    Calculates the angle whose cosine is ``x`` and is in the range ``[0, PI]``.

    The result is undefined if ``x < -1`` or ``x > 1``.

    :param x:
        The value whose arc cosine to return.

    :return:
        The angle whose trigonometric cosine is ``x``.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/acos.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_atan:

.. rst-class:: classref-method

|vec_type| **atan**\ (\ |vec_type| y_over_x) :ref:`🔗<shader_func_atan>`

    |componentwise|

    Calculates the arc tangent given a tangent value of ``y/x``.

    .. Note::
        Because of the sign ambiguity, the function cannot determine with certainty in
        which quadrant the angle falls only by its tangent value. If you need to know the
        quadrant, use :ref:`atan(vec_type y, vec_type x)<shader_func_atan2>`.

    :param y_over_x:
        The fraction whose arc tangent to return.

    :return:
        The trigonometric arc-tangent of ``y_over_x`` and is
        in the range ``[-PI/2, PI/2]``.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/atan.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_atan2:

.. rst-class:: classref-method

|vec_type| **atan**\ (\ |vec_type| y, |vec_type| x) :ref:`🔗<shader_func_atan2>`

    |componentwise|

    Calculates the arc tangent given a numerator and denominator. The signs of
    ``y`` and ``x`` are used to determine the quadrant that the angle lies in.
    The result is undefined if ``x == 0``.

    Equivalent to :ref:`atan2() <class_@GlobalScope_method_atan2>` in GDScript.

    :param y:
        The numerator of the fraction whose arc tangent to return.

    :param x:
        The denominator of the fraction whose arc tangent to return.

    :return:
        The trigonometric arc tangent of ``y/x`` and is in
        the range ``[-PI, PI]``.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/atan.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_sinh:

.. rst-class:: classref-method

|vec_type| **sinh**\ (\ |vec_type| x) :ref:`🔗<shader_func_sinh>`

    |componentwise|

    Calculates the hyperbolic sine using ``(e^x - e^-x)/2``.

    :param x:
        The value whose hyperbolic sine to return.

    :return:
        The hyperbolic sine of ``x``.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/sinh.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_cosh:

.. rst-class:: classref-method

|vec_type| **cosh**\ (\ |vec_type| x) :ref:`🔗<shader_func_cosh>`

    |componentwise|

    Calculates the hyperbolic cosine using ``(e^x + e^-x)/2``.

    :param x:
        The value whose hyperbolic cosine to return.

    :return:
        The hyperbolic cosine of ``x``.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/cosh.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_tanh:

.. rst-class:: classref-method

|vec_type| **tanh**\ (\ |vec_type| x) :ref:`🔗<shader_func_tanh>`

    |componentwise|

    Calculates the hyperbolic tangent using ``sinh(x)/cosh(x)``.

    :param x:
        The value whose hyperbolic tangent to return.

    :return:
        The hyperbolic tangent of ``x``.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/tanh.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_asinh:

.. rst-class:: classref-method

|vec_type| **asinh**\ (\ |vec_type| x) :ref:`🔗<shader_func_asinh>`

    |componentwise|

    Calculates the arc hyperbolic sine of ``x``, or the inverse of ``sinh``.

    :param x:
        The value whose arc hyperbolic sine to return.

    :return:
        The arc hyperbolic sine of ``x``.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/asinh.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_acosh:

.. rst-class:: classref-method

|vec_type| **acosh**\ (\ |vec_type| x) :ref:`🔗<shader_func_acosh>`

    |componentwise|

    Calculates the arc hyperbolic cosine of ``x``, or the non-negative inverse of ``cosh``.
    The result is undefined if ``x < 1``.

    :param x:
        The value whose arc hyperbolic cosine to return.

    :return:
        The arc hyperbolic cosine of ``x``.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/acosh.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_atanh:

.. rst-class:: classref-method

|vec_type| **atanh**\ (\ |vec_type| x) :ref:`🔗<shader_func_atanh>`

    |componentwise|

    Calculates the arc hyperbolic tangent of ``x``, or the inverse of ``tanh``.
    The result is undefined if ``abs(x) > 1``.

    :param x:
        The value whose arc hyperbolic tangent to return.

    :return:
        The arc hyperbolic tangent of ``x``.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/atanh.xhtml


.. rst-class:: classref-section-separator

----








.. rst-class:: classref-reftable-group

Exponential and math functions
------------------------------

.. table::
    :class: nowrap-col2
    :widths: auto

    +---------------------+----------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
    |    Return Type      | Function                                                                                           | Description / Return value                                      |
    +=====================+====================================================================================================+=================================================================+
    | |vec_type|          | :ref:`pow<shader_func_pow>`\ (\ |vec_type| x, |vec_type| y)                                        | Power (undefined if ``x < 0`` or if ``x == 0`` and ``y <= 0``). |
    +---------------------+----------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
    | |vec_type|          | :ref:`exp<shader_func_exp>`\ (\ |vec_type| x)                                                      | Base-e exponential.                                             |
    +---------------------+----------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
    | |vec_type|          | :ref:`exp2<shader_func_exp2>`\ (\ |vec_type| x)                                                    | Base-2 exponential.                                             |
    +---------------------+----------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
    | |vec_type|          | :ref:`log<shader_func_log>`\ (\ |vec_type| x)                                                      | Natural (base-e) logarithm.                                     |
    +---------------------+----------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
    | |vec_type|          | :ref:`log2<shader_func_log2>`\ (\ |vec_type| x)                                                    | Base-2 logarithm.                                               |
    +---------------------+----------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
    | |vec_type|          | :ref:`sqrt<shader_func_sqrt>`\ (\ |vec_type| x)                                                    | Square root.                                                    |
    +---------------------+----------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
    | |vec_type|          | :ref:`inversesqrt<shader_func_inversesqrt>`\ (\ |vec_type| x)                                      | Inverse square root.                                            |
    +---------------------+----------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
    | | |vec_type|        | | :ref:`abs<shader_func_abs>`\ (\ |vec_type| x)                                                    | Absolute value (returns positive value if negative).            |
    | | |vec_int_type|    | | :ref:`abs<shader_func_abs>`\ (\ |vec_int_type| x)                                                |                                                                 |
    +---------------------+----------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
    | |vec_type|          | :ref:`sign<shader_func_sign>`\ (\ |vec_type| x)                                                    | Returns ``1.0`` if positive, ``-1.0`` if negative,              |
    |                     |                                                                                                    | ``0.0`` otherwise.                                              |
    +---------------------+----------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
    | |vec_int_type|      | :ref:`sign<shader_func_sign>`\ (\ |vec_int_type| x)                                                | Returns ``1`` if positive, ``-1`` if negative,                  |
    |                     |                                                                                                    | ``0`` otherwise.                                                |
    +---------------------+----------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
    | |vec_type|          | :ref:`floor<shader_func_floor>`\ (\ |vec_type| x)                                                  | Rounds to the integer below.                                    |
    +---------------------+----------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
    | |vec_type|          | :ref:`round<shader_func_round>`\ (\ |vec_type| x)                                                  | Rounds to the nearest integer.                                  |
    +---------------------+----------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
    | |vec_type|          | :ref:`roundEven<shader_func_roundEven>`\ (\ |vec_type| x)                                          | Rounds to the nearest even integer.                             |
    +---------------------+----------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
    | |vec_type|          | :ref:`trunc<shader_func_trunc>`\ (\ |vec_type| x)                                                  | Truncation.                                                     |
    +---------------------+----------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
    | |vec_type|          | :ref:`ceil<shader_func_ceil>`\ (\ |vec_type| x)                                                    | Rounds to the integer above.                                    |
    +---------------------+----------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
    | |vec_type|          | :ref:`fract<shader_func_fract>`\ (\ |vec_type| x)                                                  | Fractional (returns ``x - floor(x)``).                          |
    +---------------------+----------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
    | | |vec_type|        | | :ref:`mod<shader_func_mod>`\ (\ |vec_type| x, |vec_type| y)                                      | Modulo (division remainder).                                    |
    | | |vec_type|        | | :ref:`mod<shader_func_mod>`\ (\ |vec_type| x, float y)                                           |                                                                 |
    +---------------------+----------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
    | |vec_type|          | :ref:`modf<shader_func_modf>`\ (\ |vec_type| x, out |vec_type| i)                                  | Fractional of ``x``, with ``i`` as integer part.                |
    +---------------------+----------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
    | | |vec_type|        | | :ref:`min<shader_func_min>`\ (\ |vec_type| a, |vec_type| b)                                      | Lowest value between ``a`` and ``b``.                           |
    | | |vec_type|        | | :ref:`min<shader_func_min>`\ (\ |vec_type| a, float b)                                           |                                                                 |
    | | |vec_int_type|    | | :ref:`min<shader_func_min>`\ (\ |vec_int_type| a, |vec_int_type| b)                              |                                                                 |
    | | |vec_int_type|    | | :ref:`min<shader_func_min>`\ (\ |vec_int_type| a, int b)                                         |                                                                 |
    | | |vec_uint_type|   | | :ref:`min<shader_func_min>`\ (\ |vec_uint_type| a, |vec_uint_type| b)                            |                                                                 |
    | | |vec_uint_type|   | | :ref:`min<shader_func_min>`\ (\ |vec_uint_type| a, uint b)                                       |                                                                 |
    +---------------------+----------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
    | | |vec_type|        | | :ref:`max<shader_func_max>`\ (\ |vec_type| a, |vec_type| b)                                      | Highest value between ``a`` and ``b``.                          |
    | | |vec_type|        | | :ref:`max<shader_func_max>`\ (\ |vec_type| a, float b)                                           |                                                                 |
    | | |vec_int_type|    | | :ref:`max<shader_func_max>`\ (\ |vec_int_type| a, |vec_int_type| b)                              |                                                                 |
    | | |vec_int_type|    | | :ref:`max<shader_func_max>`\ (\ |vec_int_type| a, int b)                                         |                                                                 |
    | | |vec_uint_type|   | | :ref:`max<shader_func_max>`\ (\ |vec_uint_type| a, |vec_uint_type| b)                            |                                                                 |
    | | |vec_uint_type|   | | :ref:`max<shader_func_max>`\ (\ |vec_uint_type| a, uint b)                                       |                                                                 |
    +---------------------+----------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
    | | |vec_type|        | | :ref:`clamp<shader_func_clamp>`\ (\ |vec_type| x, |vec_type| min, |vec_type| max)                | Clamps ``x`` between ``min`` and ``max`` (inclusive).           |
    | | |vec_type|        | | :ref:`clamp<shader_func_clamp>`\ (\ |vec_type| x, float min, float max)                          |                                                                 |
    | | |vec_int_type|    | | :ref:`clamp<shader_func_clamp>`\ (\ |vec_int_type| x, |vec_int_type| min, |vec_int_type| max)    |                                                                 |
    | | |vec_int_type|    | | :ref:`clamp<shader_func_clamp>`\ (\ |vec_int_type| x, int min, int max)                          |                                                                 |
    | | |vec_uint_type|   | | :ref:`clamp<shader_func_clamp>`\ (\ |vec_uint_type| x, |vec_uint_type| min, |vec_uint_type| max) |                                                                 |
    | | |vec_uint_type|   | | :ref:`clamp<shader_func_clamp>`\ (\ |vec_uint_type| x, uint min, uint max)                       |                                                                 |
    +---------------------+----------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
    | | |vec_type|        | | :ref:`mix<shader_func_mix>`\ (\ |vec_type| a, |vec_type| b, |vec_type| c)                        | Linear interpolate between ``a`` and ``b`` by ``c``.            |
    | | |vec_type|        | | :ref:`mix<shader_func_mix>`\ (\ |vec_type| a, |vec_type| b, float c)                             |                                                                 |
    | | |vec_type|        | | :ref:`mix<shader_func_mix>`\ (\ |vec_type| a, |vec_type| b, |vec_bool_type| c)                   |                                                                 |
    +---------------------+----------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
    | |vec_type|          | :ref:`fma<shader_func_fma>`\ (\ |vec_type| a, |vec_type| b, |vec_type| c)                          | Fused multiply-add operation: ``(a * b + c)``                   |
    +---------------------+----------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
    | | |vec_type|        | | :ref:`step<shader_func_step>`\ (\ |vec_type| a, |vec_type| b)                                    | ``b < a ? 0.0 : 1.0``                                           |
    | | |vec_type|        | | :ref:`step<shader_func_step>`\ (\ float a, |vec_type| b)                                         |                                                                 |
    +---------------------+----------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
    | | |vec_type|        | | :ref:`smoothstep<shader_func_smoothstep>`\ (\ |vec_type| a, |vec_type| b, |vec_type| c)          | Hermite interpolate between ``a`` and ``b`` by ``c``.           |
    | | |vec_type|        | | :ref:`smoothstep<shader_func_smoothstep>`\ (\ float a, float b, |vec_type| c)                    |                                                                 |
    +---------------------+----------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
    | |vec_bool_type|     | :ref:`isnan<shader_func_isnan>`\ (\ |vec_type| x)                                                  | Returns ``true`` if scalar or vector component is ``NaN``.      |
    +---------------------+----------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
    | |vec_bool_type|     | :ref:`isinf<shader_func_isinf>`\ (\ |vec_type| x)                                                  | Returns ``true`` if scalar or vector component is ``INF``.      |
    +---------------------+----------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
    | |vec_int_type|      | :ref:`floatBitsToInt<shader_func_floatBitsToInt>`\ (\ |vec_type| x)                                | ``float`` to ``int`` bit copying, no conversion.                |
    +---------------------+----------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
    | |vec_uint_type|     | :ref:`floatBitsToUint<shader_func_floatBitsToUint>`\ (\ |vec_type| x)                              | ``float`` to ``uint`` bit copying, no conversion.               |
    +---------------------+----------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
    | |vec_type|          | :ref:`intBitsToFloat<shader_func_intBitsToFloat>`\ (\ |vec_int_type| x)                            | ``int`` to ``float`` bit copying, no conversion.                |
    +---------------------+----------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
    | |vec_type|          | :ref:`uintBitsToFloat<shader_func_uintBitsToFloat>`\ (\ |vec_uint_type| x)                         | ``uint`` to ``float`` bit copying, no conversion.               |
    +---------------------+----------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+


.. rst-class:: classref-descriptions-group

Exponential and math function descriptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. _shader_func_pow:

.. rst-class:: classref-method

|vec_type| **pow**\ (\ |vec_type| x, |vec_type| y) :ref:`🔗<shader_func_pow>`

    |componentwise|

    Raises ``x`` to the power of ``y``.

    The result is undefined if ``x < 0`` or  if ``x == 0`` and ``y <= 0``.

    :param x:
        The value to be raised to the power ``y``.

    :param y:
        The power to which ``x`` will be raised.

    :return:
        The value of ``x`` raised to the ``y`` power.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/pow.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_exp:

.. rst-class:: classref-method

|vec_type| **exp**\ (\ |vec_type| x) :ref:`🔗<shader_func_exp>`

    |componentwise|

    Raises ``e`` to the power of ``x``, or the the natural exponentiation.

    Equivalent to ``pow(e, x)``.

    :param x:
        The value to exponentiate.

    :return:
        The natural exponentiation of ``x``.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/exp.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_exp2:

.. rst-class:: classref-method

|vec_type| **exp2**\ (\ |vec_type| x) :ref:`🔗<shader_func_exp2>`

    |componentwise|

    Raises ``2`` to the power of ``x``.

    Equivalent to ``pow(2.0, x)``.


    :param x:
        The value of the power to which ``2`` will be raised.

    :return:
        ``2`` raised to the power of x.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/exp2.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_log:

.. rst-class:: classref-method

|vec_type| **log**\ (\ |vec_type| x) :ref:`🔗<shader_func_log>`

    |componentwise|

    Returns the natural logarithm of ``x``, i.e. the value ``y`` which satisfies ``x == pow(e, y)``.
    The result is undefined if ``x <= 0``.

    :param x:
        The value of which to take the natural logarithm.

    :return:
        The natural logarithm of ``x``.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/log.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_log2:

.. rst-class:: classref-method

|vec_type| **log2**\ (\ |vec_type| x) :ref:`🔗<shader_func_log2>`

    |componentwise|

    Returns the base-2 logarithm of ``x``, i.e. the value ``y`` which satisfies ``x == pow(2, y)``.
    The result is undefined if ``x <= 0``.

    :param x:
        The value of which to take the base-2 logarithm.

    :return:
        The base-2 logarithm of ``x``.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/log2.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_sqrt:

.. rst-class:: classref-method

|vec_type| **sqrt**\ (\ |vec_type| x) :ref:`🔗<shader_func_sqrt>`

    |componentwise|

    Returns the square root of ``x``.
    The result is undefined if ``x < 0``.

    :param x:
        The value of which to take the square root.

    :return:
        The square root of ``x``.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/sqrt.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_inversesqrt:

.. rst-class:: classref-method

|vec_type| **inversesqrt**\ (\ |vec_type| x) :ref:`🔗<shader_func_inversesqrt>`

    |componentwise|

    Returns the inverse of the square root of ``x``, or ``1.0 / sqrt(x)``.
    The result is undefined if ``x <= 0``.

    :param x:
        The value of which to take the inverse of the square root.

    :return:
        The inverse of the square root of ``x``.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/inversesqrt.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_abs:

.. rst-class:: classref-method

|vec_type| **abs**\ (\ |vec_type| x) :ref:`🔗<shader_func_abs>`

.. rst-class:: classref-method

|vec_int_type| **abs**\ (\ |vec_int_type| x) :ref:`🔗<shader_func_abs>`

    |componentwise|

    Returns the absolute value of ``x``. Returns ``x`` if ``x`` is positive, otherwise returns ``-1 * x``.

    :param x:
        The value of which to return the absolute.

    :return:
        The absolute value of ``x``.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/abs.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_sign:

.. rst-class:: classref-method

|vec_type| **sign**\ (\ |vec_type| x) :ref:`🔗<shader_func_sign>`

.. rst-class:: classref-method

|vec_int_type| **sign**\ (\ |vec_int_type| x) :ref:`🔗<shader_func_sign>`

    |componentwise|

    Returns ``-1`` if ``x < 0``, ``0`` if ``x == 0``, and ``1`` if ``x > 0``.

    :param x:
        The value from which to extract the sign.

    :return:
        The sign of ``x``.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/sign.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_floor:

.. rst-class:: classref-method

|vec_type| **floor**\ (\ |vec_type| x) :ref:`🔗<shader_func_floor>`

    |componentwise|

    Returns a value equal to the nearest integer that is less than or equal to ``x``.

    :param x:
        The value to floor.

    :return:
        The nearest integer that is less than or equal to ``x``.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/floor.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_round:

.. rst-class:: classref-method

|vec_type| **round**\ (\ |vec_type| x) :ref:`🔗<shader_func_round>`

    |componentwise|

    Rounds ``x`` to the nearest integer.

    .. note::
        Rounding of values with a fractional part of ``0.5`` is implementation-dependent.
        This includes the possibility that ``round(x)`` returns the same value as
        ``roundEven(x)``for all values of ``x``.

    :param x:
        The value to round.

    :return:
        The rounded value.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/round.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_roundEven:

.. rst-class:: classref-method

|vec_type| **roundEven**\ (\ |vec_type| x) :ref:`🔗<shader_func_roundEven>`

    |componentwise|

    Rounds ``x`` to the nearest integer. A value with a fractional part of ``0.5``
    will always round toward the nearest even integer.
    For example, both ``3.5`` and ``4.5`` will round to ``4.0``.

    :param x:
        The value to round.

    :return:
        The rounded value.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/roundEven.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_trunc:

.. rst-class:: classref-method

|vec_type| **trunc**\ (\ |vec_type| x) :ref:`🔗<shader_func_trunc>`

    |componentwise|

    Truncates ``x``. Returns a value equal to the nearest integer to ``x`` whose
    absolute value is not larger than the absolute value of ``x``.

    :param x:
        The value to evaluate.

    :return:
        The truncated value.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/trunc.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_ceil:

.. rst-class:: classref-method

|vec_type| **ceil**\ (\ |vec_type| x) :ref:`🔗<shader_func_ceil>`

    |componentwise|

    Returns a value equal to the nearest integer that is greater than or equal to ``x``.

    :param x:
        The value to evaluate.

    :return:
        The ceiling-ed value.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/ceil.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_fract:

.. rst-class:: classref-method

|vec_type| **fract**\ (\ |vec_type| x) :ref:`🔗<shader_func_fract>`

    |componentwise|

    Returns the fractional part of ``x``.

    This is calculated as ``x - floor(x)``.

    :param x:
        The value to evaluate.

    :return:
        The fractional part of ``x``.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/fract.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_mod:

.. rst-class:: classref-method

|vec_type| **mod**\ (\ |vec_type| x, |vec_type| y) :ref:`🔗<shader_func_mod>`

.. rst-class:: classref-method

|vec_type| **mod**\ (\ |vec_type| x, float y) :ref:`🔗<shader_func_mod>`

    |componentwise|

    Returns the value of ``x modulo y``.
    This is also sometimes called the remainder.

    This is computed as ``x - y * floor(x/y)``.

    :param x:
        The value to evaluate.

    :return:
        The value of ``x modulo y``.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/mod.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_modf:

.. rst-class:: classref-method

|vec_type| **modf**\ (\ |vec_type| x, out |vec_type| i) :ref:`🔗<shader_func_modf>`

    |componentwise|

    Separates a floating-point value ``x`` into its integer and fractional parts.

    The fractional part of the number is returned from the function.
    The integer part (as a floating-point quantity) is returned in the output parameter ``i``.

    :param x:
        The value to separate.

    :param out i:
        A variable that receives the integer part of ``x``.

    :return:
        The fractional part of the number.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/modf.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_min:

.. rst-class:: classref-method

|vec_type| **min**\ (\ |vec_type| a, |vec_type| b) :ref:`🔗<shader_func_min>`

.. rst-class:: classref-method

|vec_type| **min**\ (\ |vec_type| a, float b) :ref:`🔗<shader_func_min>`

.. rst-class:: classref-method

|vec_int_type| **min**\ (\ |vec_int_type| a, |vec_int_type| b) :ref:`🔗<shader_func_min>`

.. rst-class:: classref-method

|vec_int_type| **min**\ (\ |vec_int_type| a, int b) :ref:`🔗<shader_func_min>`

.. rst-class:: classref-method

|vec_uint_type| **min**\ (\ |vec_uint_type| a, |vec_uint_type| b) :ref:`🔗<shader_func_min>`

.. rst-class:: classref-method

|vec_uint_type| **min**\ (\ |vec_uint_type| a, uint b) :ref:`🔗<shader_func_min>`

    |componentwise|

    Returns the minimum of two values ``a`` and ``b``.

    Returns ``b`` if ``b < a``, otherwise returns ``a``.

    :param a:
        The first value to compare.

    :param b:
        The second value to compare.

    :return:
        The minimum value.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/min.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_max:

.. rst-class:: classref-method

|vec_type| **max**\ (\ |vec_type| a, |vec_type| b) :ref:`🔗<shader_func_max>`

.. rst-class:: classref-method

|vec_type| **max**\ (\ |vec_type| a, float b) :ref:`🔗<shader_func_max>`

.. rst-class:: classref-method

|vec_uint_type| **max**\ (\ |vec_uint_type| a, |vec_uint_type| b) :ref:`🔗<shader_func_max>`

.. rst-class:: classref-method

|vec_uint_type| **max**\ (\ |vec_uint_type| a, uint b) :ref:`🔗<shader_func_max>`

.. rst-class:: classref-method

|vec_int_type| **max**\ (\ |vec_int_type| a, |vec_int_type| b) :ref:`🔗<shader_func_max>`

.. rst-class:: classref-method

|vec_int_type| **max**\ (\ |vec_int_type| a, int b) :ref:`🔗<shader_func_max>`

    |componentwise|

    Returns the maximum of two values ``a`` and ``b``.

    It returns ``b`` if ``b > a``, otherwise it returns ``a``.

    :param a:
        The first value to compare.

    :param b:
        The second value to compare.

    :return:
        The maximum value.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/max.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_clamp:

.. rst-class:: classref-method

|vec_type| **clamp**\ (\ |vec_type| x, |vec_type| minVal, |vec_type| maxVal) :ref:`🔗<shader_func_clamp>`

.. rst-class:: classref-method

|vec_type| **clamp**\ (\ |vec_type| x, float minVal, float maxVal) :ref:`🔗<shader_func_clamp>`

.. rst-class:: classref-method

|vec_int_type| **clamp**\ (\ |vec_int_type| x, |vec_int_type| minVal, |vec_int_type| maxVal) :ref:`🔗<shader_func_clamp>`

.. rst-class:: classref-method

|vec_int_type| **clamp**\ (\ |vec_int_type| x, int minVal, int maxVal) :ref:`🔗<shader_func_clamp>`

.. rst-class:: classref-method

|vec_uint_type| **clamp**\ (\ |vec_uint_type| x, |vec_uint_type| minVal, |vec_uint_type| maxVal) :ref:`🔗<shader_func_clamp>`

.. rst-class:: classref-method

|vec_uint_type| **clamp**\ (\ |vec_uint_type| x, uint minVal, uint maxVal) :ref:`🔗<shader_func_clamp>`

    |componentwise|

    Returns the value of ``x`` constrained to the range ``minVal`` to ``maxVal``.

    The returned value is computed as ``min(max(x, minVal), maxVal)``.

    :param x:
        The value to constrain.

    :param minVal:
        The lower end of the range into which to constrain ``x``.

    :param maxVal:
        The upper end of the range into which to constrain ``x``.

    :return:
        The clamped value.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/clamp.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_mix:

.. rst-class:: classref-method

|vec_type| **mix**\ (\ |vec_type| a, |vec_type| b, |vec_type| c) :ref:`🔗<shader_func_mix>`

.. rst-class:: classref-method

|vec_type| **mix**\ (\ |vec_type| a, |vec_type| b, float c) :ref:`🔗<shader_func_mix>`

    |componentwise|

    Performs a linear interpolation between ``a`` and ``b`` using ``c`` to weight between them.

    Computed as ``a * (1 - c) + b * c``.

    Equivalent to :ref:`lerp() <class_@GlobalScope_method_lerp>` in GDScript.

    :param a:
        The start of the range in which to interpolate.

    :param b:
        The end of the range in which to interpolate.

    :param c:
        The value to use to interpolate between ``a`` and ``b``.

    :return:
        The interpolated value.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/mix.xhtml

.. rst-class:: classref-item-separator

----


.. rst-class:: classref-method

|vec_type| **mix**\ (\ |vec_type| a, |vec_type| b, |vec_bool_type| c) :ref:`🔗<shader_func_mix>`

    Selects either value ``a`` or value ``b`` based on the value of ``c``.
    For a component of ``c`` that is false, the corresponding component of ``a`` is returned.
    For a component of ``c`` that is true, the corresponding component of ``b`` is returned.
    Components of ``a`` and ``b`` that are not selected are allowed to be invalid floating-point values and will have no effect on the results.

    If ``a``, ``b``, and ``c`` are vector types the operation is performed :ref:`component-wise <shading_componentwise>`.
    ie. ``mix(vec2(42, 314), vec2(9.8, 6e23), bvec2(true, false)))`` will return ``vec2(9.8, 314)``.

    :param a:
        Value returned when ``c`` is false.

    :param b:
        Value returned when ``c`` is true.

    :param c:
        The value used to select between ``a`` and ``b``.

    :return:
        The interpolated value.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/mix.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_fma:

.. rst-class:: classref-method

|vec_type| **fma**\ (\ |vec_type| a, |vec_type| b, |vec_type| c) :ref:`🔗<shader_func_fma>`

    |componentwise|

    Performs, where possible, a fused multiply-add operation, returning ``a * b + c``. In use cases where the
    return value is eventually consumed by a variable declared as precise:

     - ``fma()`` is considered a single operation, whereas the expression ``a * b + c`` consumed by a variable declared as precise is considered two operations.

     - The precision of ``fma()`` can differ from the precision of the expression ``a * b + c``.

     - ``fma()`` will be computed with the same precision as any other ``fma()`` consumed by a precise variable,
       giving invariant results for the same input values of a, b and c.

    Otherwise, in the absence of precise consumption, there are no special constraints on the number of operations
    or difference in precision between ``fma()`` and the expression ``a * b + c``.

    :param a:
        The first value to be multiplied.

    :param b:
        The second value to be multiplied.

    :param c:
        The value to be added to the result.

    :return:
        The value of ``a * b + c``.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/fma.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_step:

.. rst-class:: classref-method

|vec_type| **step**\ (\ |vec_type| a, |vec_type| b) :ref:`🔗<shader_func_step>`

.. rst-class:: classref-method

|vec_type| **step**\ (\ float a, |vec_type| b) :ref:`🔗<shader_func_step>`

    |componentwise|

    Generates a step function by comparing b to a.

    Equivalent to ``if (b < a) { return 0.0; } else { return 1.0; }``.
    For element i of the return value, 0.0 is returned if b[i] < a[i], and 1.0 is returned otherwise.

    :param a:
        The location of the edge of the step function.

    :param b:
        The value to be used to generate the step function.

    :return:
        ``0.0`` or ``1.0``.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/step.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_smoothstep:

.. rst-class:: classref-method

|vec_type| **smoothstep**\ (\ |vec_type| a, |vec_type| b, |vec_type| c) :ref:`🔗<shader_func_smoothstep>`

.. rst-class:: classref-method

|vec_type| **smoothstep**\ (\ float a, float b, |vec_type| c) :ref:`🔗<shader_func_smoothstep>`

    |componentwise|

    Performs smooth Hermite interpolation between ``0`` and ``1`` when a < c < b.
    This is useful in cases where a threshold function with a smooth transition is desired.

    Smoothstep is equivalent to:

    ::

        vec_type t;
        t = clamp((c - a) / (b - a), 0.0, 1.0);
        return t * t * (3.0 - 2.0 * t);

    Results are undefined if ``a >= b``.

    :param a:
        The value of the lower edge of the Hermite function.

    :param b:
        The value of the upper edge of the Hermite function.

    :param c:
        The source value for interpolation.

    :return:
        The interpolated value.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/smoothstep.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_isnan:

.. rst-class:: classref-method

|vec_bool_type| **isnan**\ (\ |vec_type| x) :ref:`🔗<shader_func_isnan>`

    |componentwise|

    For each element i of the result, returns ``true`` if x[i] is positive
    or negative floating-point NaN (Not a Number) and false otherwise.

    :param x:
        The value to test for NaN.

    :return:
        ``true`` or ``false``.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/isnan.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_isinf:

.. rst-class:: classref-method

|vec_bool_type| **isinf**\ (\ |vec_type| x) :ref:`🔗<shader_func_isinf>`

    |componentwise|

    For each element i of the result, returns ``true`` if x[i] is positive or negative
    floating-point infinity and false otherwise.

    :param x:
        The value to test for infinity.

    :return:
        ``true`` or ``false``.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/isinf.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_floatBitsToInt:

.. rst-class:: classref-method

|vec_int_type| **floatBitsToInt**\ (\ |vec_type| x) :ref:`🔗<shader_func_floatBitsToInt>`

    |componentwise|

    Returns the encoding of the floating-point parameters as ``int``.

    The floating-point bit-level representation is preserved.

    :param x:
        The value whose floating-point encoding to return.

    :return:
        The floating-point encoding of ``x``.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/floatBitsToInt.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_floatBitsToUint:

.. rst-class:: classref-method

|vec_uint_type| **floatBitsToUint**\ (\ |vec_type| x) :ref:`🔗<shader_func_floatBitsToUint>`

    |componentwise|

    Returns the encoding of the floating-point parameters as ``uint``.

    The floating-point bit-level representation is preserved.

    :param x:
        The value whose floating-point encoding to return.

    :return:
        The floating-point encoding of ``x``.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/floatBitsToInt.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_intBitsToFloat:

.. rst-class:: classref-method

|vec_type| **intBitsToFloat**\ (\ |vec_int_type| x) :ref:`🔗<shader_func_intBitsToFloat>`

    |componentwise|

    Converts a bit encoding to a floating-point value. Opposite of `floatBitsToInt<shader_func_floatBitsToInt>`

    If the encoding of a ``NaN`` is passed in ``x``, it will not signal and the resulting value will be undefined.

    If the encoding of a floating-point infinity is passed in parameter ``x``, the resulting floating-point value is
    the corresponding (positive or negative) floating-point infinity.

    :param x:
        The bit encoding to return as a floating-point value.

    :return:
        A floating-point value.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/intBitsToFloat.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_uintBitsToFloat:

.. rst-class:: classref-method

|vec_type| **uintBitsToFloat**\ (\ |vec_uint_type| x) :ref:`🔗<shader_func_uintBitsToFloat>`

    |componentwise|

    Converts a bit encoding to a floating-point value. Opposite of `floatBitsToUint<shader_func_floatBitsToUint>`

    If the encoding of a ``NaN`` is passed in ``x``, it will not signal and the resulting value will be undefined.

    If the encoding of a floating-point infinity is passed in parameter ``x``, the resulting floating-point value is
    the corresponding (positive or negative) floating-point infinity.

    :param x:
        The bit encoding to return as a floating-point value.

    :return:
        A floating-point value.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/intBitsToFloat.xhtml


.. rst-class:: classref-section-separator

----



















.. rst-class:: classref-reftable-group

Geometric functions
-------------------

.. table::
    :class: nowrap-col2
    :widths: auto

    +------------+-----------------------------------------------------------------------------------------------+----------------------------------------------------------+
    | float      | :ref:`length<shader_func_length>`\ (\ |vec_type| x)                                           | Vector length.                                           |
    +------------+-----------------------------------------------------------------------------------------------+----------------------------------------------------------+
    | float      | :ref:`distance<shader_func_distance>`\ (\ |vec_type| a, |vec_type| b)                         | Distance between vectors i.e ``length(a - b)``.          |
    +------------+-----------------------------------------------------------------------------------------------+----------------------------------------------------------+
    | float      | :ref:`dot<shader_func_dot>`\ (\ |vec_type| a, |vec_type| b)                                   | Dot product.                                             |
    +------------+-----------------------------------------------------------------------------------------------+----------------------------------------------------------+
    | vec3       | :ref:`cross<shader_func_cross>`\ (\ vec3 a, vec3 b)                                           | Cross product.                                           |
    +------------+-----------------------------------------------------------------------------------------------+----------------------------------------------------------+
    | |vec_type| | :ref:`normalize<shader_func_normalize>`\ (\ |vec_type| x)                                     | Normalize to unit length.                                |
    +------------+-----------------------------------------------------------------------------------------------+----------------------------------------------------------+
    | vec3       | :ref:`reflect<shader_func_reflect>`\ (\ vec3 I, vec3 N)                                       | Reflect.                                                 |
    +------------+-----------------------------------------------------------------------------------------------+----------------------------------------------------------+
    | vec3       | :ref:`refract<shader_func_refract>`\ (\ vec3 I, vec3 N, float eta)                            | Refract.                                                 |
    +------------+-----------------------------------------------------------------------------------------------+----------------------------------------------------------+
    | |vec_type| | :ref:`faceforward<shader_func_faceforward>`\ (\ |vec_type| N, |vec_type| I, |vec_type| Nref)  | If ``dot(Nref, I)`` < 0, return ``N``, otherwise ``-N``. |
    +------------+-----------------------------------------------------------------------------------------------+----------------------------------------------------------+
    | |mat_type| | :ref:`matrixCompMult<shader_func_matrixCompMult>`\ (\ |mat_type| x, |mat_type| y)             | Matrix component multiplication.                         |
    +------------+-----------------------------------------------------------------------------------------------+----------------------------------------------------------+
    | |mat_type| | :ref:`outerProduct<shader_func_outerProduct>`\ (\ |vec_type| column, |vec_type| row)          | Matrix outer product.                                    |
    +------------+-----------------------------------------------------------------------------------------------+----------------------------------------------------------+
    | |mat_type| | :ref:`transpose<shader_func_transpose>`\ (\ |mat_type| m)                                     | Transpose matrix.                                        |
    +------------+-----------------------------------------------------------------------------------------------+----------------------------------------------------------+
    | float      | :ref:`determinant<shader_func_determinant>`\ (\ |mat_type| m)                                 | Matrix determinant.                                      |
    +------------+-----------------------------------------------------------------------------------------------+----------------------------------------------------------+
    | |mat_type| | :ref:`inverse<shader_func_inverse>`\ (\ |mat_type| m)                                         | Inverse matrix.                                          |
    +------------+-----------------------------------------------------------------------------------------------+----------------------------------------------------------+


.. rst-class:: classref-descriptions-group

Geometric function descriptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. _shader_func_length:

.. rst-class:: classref-method

float **length**\ (\ |vec_type| x) :ref:`🔗<shader_func_length>`

    Returns the length of the vector.
    ie. ``sqrt(x[0] * x[0] + x[1] * x[1] + ... + x[n] * x[n])``

    :param x:
        The vector

    :return:
        The length of the vector.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/length.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_distance:

.. rst-class:: classref-method

float **distance**\ (\ |vec_type| a, |vec_type| b) :ref:`🔗<shader_func_distance>`

    Returns the distance between the two points a and b.

    i.e., ``length(b - a);``

    :param a:
        The first point.

    :param b:
        The second point.

    :return:
        The scalar distance between the points

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/distance.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_dot:

.. rst-class:: classref-method

float **dot**\ (\ |vec_type| a, |vec_type| b) :ref:`🔗<shader_func_dot>`

    Returns the dot product of two vectors, ``a`` and ``b``.
    i.e., ``a.x * b.x + a.y * b.y + ...``

    :param a:
        The first vector.

    :param b:
        The second vector.

    :return:
        The dot product.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/dot.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_cross:

.. rst-class:: classref-method

vec3 **cross**\ (\ vec3 a, vec3 b) :ref:`🔗<shader_func_cross>`

    Returns the cross product of two vectors. i.e.:

    .. code-block:: glsl

        vec2( a.y * b.z - b.y * a.z,
              a.z * b.x - b.z * a.x,
              a.x * b.z - b.x * a.y)

    :param a:
        The first vector.

    :param b:
        The second vector.

    :return:
        The cross product of ``a`` and ``b``.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/cross.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_normalize:

.. rst-class:: classref-method

|vec_type| **normalize**\ (\ |vec_type| x) :ref:`🔗<shader_func_normalize>`

    Returns a vector with the same direction as ``x`` but with length ``1.0``.

    :param x:
        The vector to normalize.

    :return:
        The normalized vector.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/normalize.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_reflect:

.. rst-class:: classref-method

vec3 **reflect**\ (\ vec3 I, vec3 N) :ref:`🔗<shader_func_reflect>`

    Calculate the reflection direction for an incident vector.

    For a given incident vector ``I`` and surface normal ``N`` reflect returns the reflection direction calculated as ``I - 2.0 * dot(N, I) * N``.

    .. Note::
        ``N`` should be normalized in order to achieve the desired result.

    :param I:
        The incident vector.

    :param N:
        The normal vector.

    :return:
        The reflection vector.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/reflect.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_refract:

.. rst-class:: classref-method

vec3 **refract**\ (\ vec3 I, vec3 N, float eta) :ref:`🔗<shader_func_refract>`

    Calculate the refraction direction for an incident vector.

    For a given incident vector ``I``, surface normal ``N`` and ratio of indices of refraction, ``eta``, refract returns the refraction vector, ``R``.

    ``R`` is calculated as:

    .. code-block:: glsl

        k = 1.0 - eta * eta * (1.0 - dot(N, I) * dot(N, I));
        if (k < 0.0)
            R = genType(0.0);       // or genDType(0.0)
        else
            R = eta * I - (eta * dot(N, I) + sqrt(k)) * N;

    .. Note::
        The input parameters I and N should be normalized in order to achieve the desired result.

    :param I:
        The incident vector.

    :param N:
        The normal vector.

    :param eta:
        The ratio of indices of refraction.

    :return:
        The refraction vector.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/refract.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_faceforward:

.. rst-class:: classref-method

|vec_type| **faceforward**\ (\ |vec_type| N, |vec_type| I, |vec_type| Nref) :ref:`🔗<shader_func_faceforward>`

    Returns a vector pointing in the same direction as another.

    Orients a vector to point away from a surface as defined by its normal.
    If ``dot(Nref, I) < 0`` faceforward returns ``N``, otherwise it returns ``-N``.

    :param N:
        The vector to orient.

    :param I:
        The incident vector.

    :param Nref:
        The reference vector.

    :return:
        The oriented vector.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/faceforward.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_matrixCompMult:

.. rst-class:: classref-method

|mat_type| **matrixCompMult**\ (\ |mat_type| x, |mat_type| y) :ref:`🔗<shader_func_matrixCompMult>`

    Perform a :ref:`component-wise <shading_componentwise>` multiplication of two matrices.

    Performs a component-wise multiplication of two matrices, yielding a result
    matrix where each component, ``result[i][j]`` is computed as the scalar
    product of ``x[i][j]`` and ``y[i][j]``.

    :param x:
        The first matrix multiplicand.

    :param y:
        The second matrix multiplicand.

    :return:
        The resultant matrix.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/matrixCompMult.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_outerProduct:

.. rst-class:: classref-method

|mat_type| **outerProduct**\ (\ |vec_type| column, |vec_type| row) :ref:`🔗<shader_func_outerProduct>`

    Calculate the outer product of a pair of vectors.

    Does a linear algebraic matrix multiply ``column * row``, yielding a matrix whose number of
    rows is the number of components in ``column`` and whose number of columns is the number of
    components in ``row``.

    :param column:
        The column vector for multiplication.

    :param row:
        The row vector for multiplication.

    :return:
        The outer product matrix.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/outerProduct.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_transpose:

.. rst-class:: classref-method

|mat_type| **transpose**\ (\ |mat_type| m) :ref:`🔗<shader_func_transpose>`

    Calculate the transpose of a matrix.

    :param m:
        The matrix to transpose.

    :return:
        A new matrix that is the transpose of the input matrix ``m``.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/transpose.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_determinant:

.. rst-class:: classref-method

float **determinant**\ (\ |mat_type| m) :ref:`🔗<shader_func_determinant>`

    Calculate the determinant of a matrix.

    :param m:
        The matrix.

    :return:
        The determinant of the input matrix ``m``.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/determinant.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_inverse:

.. rst-class:: classref-method

|mat_type| **inverse**\ (\ |mat_type| m) :ref:`🔗<shader_func_inverse>`

    Calculate the inverse of a matrix.

    The values in the returned matrix are undefined if ``m`` is singular or poorly-conditioned (nearly singular).

    :param m:
        The matrix of which to take the inverse.

    :return:
        A new matrix which is the inverse of the input matrix ``m``.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/inverse.xhtml

.. rst-class:: classref-section-separator

----













.. rst-class:: classref-reftable-group

Comparison functions
--------------------

.. table::
    :class: nowrap-col2
    :widths: auto

    +-----------------+-----------------------------------------------------------------------------------------+---------------------------------------------------------------+
    | |vec_bool_type| | :ref:`lessThan<shader_func_lessThan>`\ (\ |vec_type| x, |vec_type| y)                   | Bool vector comparison on < int/uint/float vectors.           |
    +-----------------+-----------------------------------------------------------------------------------------+---------------------------------------------------------------+
    | |vec_bool_type| | :ref:`greaterThan<shader_func_greaterThan>`\ (\ |vec_type| x, |vec_type| y)             | Bool vector comparison on > int/uint/float vectors.           |
    +-----------------+-----------------------------------------------------------------------------------------+---------------------------------------------------------------+
    | |vec_bool_type| | :ref:`lessThanEqual<shader_func_lessThanEqual>`\ (\ |vec_type| x, |vec_type| y)         | Bool vector comparison on <= int/uint/float vectors.          |
    +-----------------+-----------------------------------------------------------------------------------------+---------------------------------------------------------------+
    | |vec_bool_type| | :ref:`greaterThanEqual<shader_func_greaterThanEqual>`\ (\  |vec_type| x, |vec_type| y)  | Bool vector comparison on >= int/uint/float vectors.          |
    +-----------------+-----------------------------------------------------------------------------------------+---------------------------------------------------------------+
    | |vec_bool_type| | :ref:`equal<shader_func_equal>`\ (\ |vec_type| x, |vec_type| y)                         | Bool vector comparison on == int/uint/float vectors.          |
    +-----------------+-----------------------------------------------------------------------------------------+---------------------------------------------------------------+
    | |vec_bool_type| | :ref:`notEqual<shader_func_notEqual>`\ (\ |vec_type| x, |vec_type| y)                   | Bool vector comparison on != int/uint/float vectors.          |
    +-----------------+-----------------------------------------------------------------------------------------+---------------------------------------------------------------+
    | bool            | :ref:`any<shader_func_any>`\ (\ |vec_bool_type| x)                                      | ``true`` if any component is ``true``, ``false`` otherwise.   |
    +-----------------+-----------------------------------------------------------------------------------------+---------------------------------------------------------------+
    | bool            | :ref:`all<shader_func_all>`\ (\ |vec_bool_type| x)                                      | ``true`` if all components are ``true``, ``false`` otherwise. |
    +-----------------+-----------------------------------------------------------------------------------------+---------------------------------------------------------------+
    | |vec_bool_type| | :ref:`not<shader_func_not>`\ (\ |vec_bool_type| x)                                      | Invert boolean vector.                                        |
    +-----------------+-----------------------------------------------------------------------------------------+---------------------------------------------------------------+


.. rst-class:: classref-descriptions-group

Comparison function descriptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. _shader_func_lessThan:

.. rst-class:: classref-method

|vec_bool_type| **lessThan**\ (\ |vec_type| x, |vec_type| y) :ref:`🔗<shader_func_lessThan>`

    Performs a :ref:`component-wise<shading_componentwise>` less-than comparison of two vectors.

    :param x:
        The first vector to compare.

    :param y:
        The second vector to compare.

    :return:
        A boolean vector in which each element ``i`` is computed as ``x[i] < y[i]``.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/lessThan.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_greaterThan:

.. rst-class:: classref-method

|vec_bool_type| **greaterThan**\ (\ |vec_type| x, |vec_type| y) :ref:`🔗<shader_func_greaterThan>`

    Performs a :ref:`component-wise<shading_componentwise>` greater-than comparison of two vectors.

    :param x:
        The first vector to compare.

    :param y:
        The second vector to compare.

    :return:
        A boolean vector in which each element ``i`` is computed as ``x[i] > y[i]``.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/greaterThan.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_lessThanEqual:

.. rst-class:: classref-method

|vec_bool_type| **lessThanEqual**\ (\ |vec_type| x, |vec_type| y) :ref:`🔗<shader_func_lessThanEqual>`

    Performs a :ref:`component-wise<shading_componentwise>` less-than-or-equal comparison of two vectors.

    :param x:
        The first vector to compare.

    :param y:
        The second vector to compare.

    :return:
        A boolean vector in which each element ``i`` is computed as ``x[i] <= y[i]``.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/lessThanEqual.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_greaterThanEqual:

.. rst-class:: classref-method

|vec_bool_type| **greaterThanEqual**\ (\ |vec_type| x, |vec_type| y) :ref:`🔗<shader_func_greaterThanEqual>`

    Performs a :ref:`component-wise<shading_componentwise>` greater-than-or-equal comparison of two vectors.

    :param x:
        The first vector to compare.

    :param y:
        The second vector to compare.

    :return:
        A boolean vector in which each element ``i`` is computed as ``x[i] >= y[i]``.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/greaterThanEqual.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_equal:

.. rst-class:: classref-method

|vec_bool_type| **equal**\ (\ |vec_type| x, |vec_type| y) :ref:`🔗<shader_func_equal>`

    Performs a :ref:`component-wise<shading_componentwise>` equal-to comparison of two vectors.

    :param x:
        The first vector to compare.

    :param y:
        The second vector to compare.

    :return:
        A boolean vector in which each element ``i`` is computed as ``x[i] == y[i]``.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/equal.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_notEqual:

.. rst-class:: classref-method

|vec_bool_type| **notEqual**\ (\ |vec_type| x, |vec_type| y) :ref:`🔗<shader_func_notEqual>`

    Performs a :ref:`component-wise<shading_componentwise>` not-equal-to comparison of two vectors.

    :param x:
        The first vector for comparison.

    :param y:
        The second vector for comparison.

    :return:
        A boolean vector in which each element ``i`` is computed as ``x[i] != y[i]``.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/notEqual.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_any:

.. rst-class:: classref-method

bool **any**\ (\ |vec_bool_type| x) :ref:`🔗<shader_func_any>`

    Returns ``true`` if any element of a boolean vector is ``true``, ``false`` otherwise.

    Functionally equivalent to:

    ::

        bool any(bvec x) {     // bvec can be bvec2, bvec3 or bvec4
            bool result = false;
            int i;
            for (i = 0; i < x.length(); ++i) {
                result |= x[i];
            }
            return result;
        }

    :param x:
        The vector to be tested for truth.

    :return:
        True if any element of x is true and false otherwise.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/any.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_all:

.. rst-class:: classref-method

bool **all**\ (\ |vec_bool_type| x) :ref:`🔗<shader_func_all>`

    Returns ``true`` if all elements of a boolean vector are ``true``, ``false`` otherwise.

    Functionally equivalent to:

    ::

        bool all(bvec x)       // bvec can be bvec2, bvec3 or bvec4
        {
            bool result = true;
            int i;
            for (i = 0; i < x.length(); ++i)
            {
                result &= x[i];
            }
            return result;
        }

    :param x:
        The vector to be tested for truth.

    :return:
        ``true`` if all elements of ``x`` are ``true`` and ``false`` otherwise.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/all.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_not:

.. rst-class:: classref-method

|vec_bool_type| **not**\ (\ |vec_bool_type| x) :ref:`🔗<shader_func_not>`

    Logically invert a boolean vector.

    :param x:
        The vector to be inverted.

    :return:
        A new boolean vector for which each element i is computed as !x[i].

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/not.xhtml


.. rst-class:: classref-section-separator

----










.. rst-class:: classref-reftable-group

Texture functions
-----------------

.. table::
    :class: nowrap-col2
    :widths: auto

    +------------------+---------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
    | | ivec2          | | :ref:`textureSize<shader_func_textureSize>`\ (\ |gsampler2D| s, int lod)                              | Get the size of a texture.                                          |
    | | ivec2          | | :ref:`textureSize<shader_func_textureSize>`\ (\ samplerCube s, int lod)                               |                                                                     |
    | | ivec2          | | :ref:`textureSize<shader_func_textureSize>`\ (\ samplerCubeArray s, int lod)                          |                                                                     |
    | | ivec3          | | :ref:`textureSize<shader_func_textureSize>`\ (\ |gsampler2DArray| s, int lod)                         |                                                                     |
    | | ivec3          | | :ref:`textureSize<shader_func_textureSize>`\ (\ |gsampler3D| s, int lod)                              |                                                                     |
    +------------------+---------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
    | | vec2           | | :ref:`textureQueryLod<shader_func_textureQueryLod>`\ (\ |gsampler2D| s, vec2 p)                       | Compute the level-of-detail that would be used to sample from a     |
    | | vec3           | | :ref:`textureQueryLod<shader_func_textureQueryLod>`\ (\ |gsampler2DArray| s, vec2 p)                  | texture.                                                            |
    | | vec2           | | :ref:`textureQueryLod<shader_func_textureQueryLod>`\ (\ |gsampler3D| s, vec3 p)                       |                                                                     |
    | | vec2           | | :ref:`textureQueryLod<shader_func_textureQueryLod>`\ (\ samplerCube s, vec3 p)                        |                                                                     |
    +------------------+---------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
    | | int            | | :ref:`textureQueryLevels<shader_func_textureQueryLevels>`\ (\ |gsampler2D| s)                         | Get the number of accessible mipmap levels of a texture.            |
    | | int            | | :ref:`textureQueryLevels<shader_func_textureQueryLevels>`\ (\ |gsampler2DArray| s)                    |                                                                     |
    | | int            | | :ref:`textureQueryLevels<shader_func_textureQueryLevels>`\ (\ |gsampler3D| s)                         |                                                                     |
    | | int            | | :ref:`textureQueryLevels<shader_func_textureQueryLevels>`\ (\ samplerCube s)                          |                                                                     |
    +------------------+---------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
    | | |gvec4_type|   | | :ref:`texture<shader_func_texture>`\ (\ |gsampler2D| s, vec2 p [, float bias] )                       | Performs a texture read.                                            |
    | | |gvec4_type|   | | :ref:`texture<shader_func_texture>`\ (\ |gsampler2DArray| s, vec3 p [, float bias] )                  |                                                                     |
    | | |gvec4_type|   | | :ref:`texture<shader_func_texture>`\ (\ |gsampler3D| s, vec3 p [, float bias] )                       |                                                                     |
    | | vec4           | | :ref:`texture<shader_func_texture>`\ (\ samplerCube s, vec3 p [, float bias] )                        |                                                                     |
    | | vec4           | | :ref:`texture<shader_func_texture>`\ (\ samplerCubeArray s, vec4 p [, float bias] )                   |                                                                     |
    | | vec4           | | :ref:`texture<shader_func_texture>`\ (\ samplerExternalOES s, vec2 p [, float bias] )                 |                                                                     |
    +------------------+---------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
    | | |gvec4_type|   | | :ref:`textureProj<shader_func_textureProj>`\ (\ |gsampler2D| s, vec3 p [, float bias] )               | Performs a texture read with projection.                            |
    | | |gvec4_type|   | | :ref:`textureProj<shader_func_textureProj>`\ (\ |gsampler2D| s, vec4 p [, float bias] )               |                                                                     |
    | | |gvec4_type|   | | :ref:`textureProj<shader_func_textureProj>`\ (\ |gsampler3D| s, vec4 p [, float bias] )               |                                                                     |
    +------------------+---------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
    | | |gvec4_type|   | | :ref:`textureLod<shader_func_textureLod>`\ (\ |gsampler2D| s, vec2 p, float lod)                      | Performs a texture read at custom mipmap.                           |
    | | |gvec4_type|   | | :ref:`textureLod<shader_func_textureLod>`\ (\ |gsampler2DArray| s, vec3 p, float lod)                 |                                                                     |
    | | |gvec4_type|   | | :ref:`textureLod<shader_func_textureLod>`\ (\ |gsampler3D| s, vec3 p, float lod)                      |                                                                     |
    | | vec4           | | :ref:`textureLod<shader_func_textureLod>`\ (\ samplerCube s, vec3 p, float lod)                       |                                                                     |
    | | vec4           | | :ref:`textureLod<shader_func_textureLod>`\ (\ samplerCubeArray s, vec4 p, float lod)                  |                                                                     |
    +------------------+---------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
    | | |gvec4_type|   | | :ref:`textureProjLod<shader_func_textureProjLod>`\ (\ |gsampler2D| s, vec3 p, float lod)              | Performs a texture read with projection/LOD.                        |
    | | |gvec4_type|   | | :ref:`textureProjLod<shader_func_textureProjLod>`\ (\ |gsampler2D| s, vec4 p, float lod)              |                                                                     |
    | | |gvec4_type|   | | :ref:`textureProjLod<shader_func_textureProjLod>`\ (\ |gsampler3D| s, vec4 p, float lod)              |                                                                     |
    +------------------+---------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
    | | |gvec4_type|   | | :ref:`textureGrad<shader_func_textureGrad>`\ (\ |gsampler2D| s, vec2 p, vec2 dPdx, vec2 dPdy)         | Performs a texture read with explicit gradients.                    |
    | | |gvec4_type|   | | :ref:`textureGrad<shader_func_textureGrad>`\ (\ |gsampler2DArray| s, vec3 p, vec2 dPdx, vec2 dPdy)    |                                                                     |
    | | |gvec4_type|   | | :ref:`textureGrad<shader_func_textureGrad>`\ (\ |gsampler3D| s, vec3 p, vec2 dPdx, vec2 dPdy)         |                                                                     |
    | | vec4           | | :ref:`textureGrad<shader_func_textureGrad>`\ (\ samplerCube s, vec3 p, vec3 dPdx, vec3 dPdy)          |                                                                     |
    | | vec4           | | :ref:`textureGrad<shader_func_textureGrad>`\ (\ samplerCubeArray s, vec3 p, vec3 dPdx, vec3 dPdy)     |                                                                     |
    +------------------+---------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
    | | |gvec4_type|   | | :ref:`textureProjGrad<shader_func_textureProjGrad>`\ (\ |gsampler2D| s, vec3 p, vec2 dPdx, vec2 dPdy) | Performs a texture read with projection/LOD and with explicit       |
    | | |gvec4_type|   | | :ref:`textureProjGrad<shader_func_textureProjGrad>`\ (\ |gsampler2D| s, vec4 p, vec2 dPdx, vec2 dPdy) |                                                                     |
    | | |gvec4_type|   | | :ref:`textureProjGrad<shader_func_textureProjGrad>`\ (\ |gsampler3D| s, vec4 p, vec3 dPdx, vec3 dPdy) |                                                                     |
    +------------------+---------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
    | | |gvec4_type|   | | :ref:`texelFetch<shader_func_texelFetch>`\ (\ |gsampler2D| s, ivec2 p, int lod)                       | Fetches a single texel using integer coordinates.                   |
    | | |gvec4_type|   | | :ref:`texelFetch<shader_func_texelFetch>`\ (\ |gsampler2DArray| s, ivec3 p, int lod)                  |                                                                     |
    | | |gvec4_type|   | | :ref:`texelFetch<shader_func_texelFetch>`\ (\ |gsampler3D| s, ivec3 p, int lod)                       |                                                                     |
    +------------------+---------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
    | | |gvec4_type|   | | :ref:`textureGather<shader_func_textureGather>`\ (\ |gsampler2D| s, vec2 p [, int comps] )            | Gathers four texels from a texture.                                 |
    | | |gvec4_type|   | | :ref:`textureGather<shader_func_textureGather>`\ (\ |gsampler2DArray| s, vec3 p [, int comps] )       |                                                                     |
    | | vec4           | | :ref:`textureGather<shader_func_textureGather>`\ (\ samplerCube s, vec3 p [, int comps] )             |                                                                     |
    +------------------+---------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
    | |vec_type|       | :ref:`dFdx<shader_func_dFdx>`\ (\ |vec_type| p)                                                         | Derivative with respect to ``x`` window coordinate,                 |
    |                  |                                                                                                         | automatic granularity.                                              |
    +------------------+---------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
    | |vec_type|       | :ref:`dFdxCoarse<shader_func_dFdxCoarse>`\ (\ |vec_type| p)                                             | Derivative with respect to ``x`` window coordinate,                 |
    |                  |                                                                                                         | course granularity.                                                 |
    |                  |                                                                                                         |                                                                     |
    |                  |                                                                                                         | Not available when using the Compatibility renderer.                |
    +------------------+---------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
    | |vec_type|       | :ref:`dFdxFine<shader_func_dFdxFine>`\ (\ |vec_type| p)                                                 | Derivative with respect to ``x`` window coordinate,                 |
    |                  |                                                                                                         | fine granularity.                                                   |
    |                  |                                                                                                         |                                                                     |
    |                  |                                                                                                         | Not available when using the Compatibility renderer.                |
    +------------------+---------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
    | |vec_type|       | :ref:`dFdy<shader_func_dFdy>`\ (\ |vec_type| p)                                                         | Derivative with respect to ``y`` window coordinate,                 |
    |                  |                                                                                                         | automatic granularity.                                              |
    +------------------+---------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
    | |vec_type|       | :ref:`dFdyCoarse<shader_func_dFdyCoarse>`\ (\ |vec_type| p)                                             | Derivative with respect to ``y`` window coordinate,                 |
    |                  |                                                                                                         | course granularity.                                                 |
    |                  |                                                                                                         |                                                                     |
    |                  |                                                                                                         | Not available when using the Compatibility renderer.                |
    +------------------+---------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
    | |vec_type|       | :ref:`dFdyFine<shader_func_dFdyFine>`\ (\ |vec_type| p)                                                 | Derivative with respect to ``y`` window coordinate,                 |
    |                  |                                                                                                         | fine granularity.                                                   |
    |                  |                                                                                                         |                                                                     |
    |                  |                                                                                                         | Not available when using the Compatibility renderer.                |
    +------------------+---------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
    | |vec_type|       | :ref:`fwidth<shader_func_fwidth>`\ (\ |vec_type| p)                                                     | Sum of absolute derivative in ``x`` and ``y``.                      |
    +------------------+---------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
    | |vec_type|       | :ref:`fwidthCoarse<shader_func_fwidthCoarse>`\ (\ |vec_type| p)                                         | Sum of absolute derivative in ``x`` and ``y``.                      |
    |                  |                                                                                                         |                                                                     |
    |                  |                                                                                                         | Not available when using the Compatibility renderer.                |
    +------------------+---------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
    | |vec_type|       | :ref:`fwidthFine<shader_func_fwidthFine>`\ (\ |vec_type| p)                                             | Sum of absolute derivative in ``x`` and ``y``.                      |
    |                  |                                                                                                         |                                                                     |
    |                  |                                                                                                         | Not available when using the Compatibility renderer.                |
    +------------------+---------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+


.. rst-class:: classref-descriptions-group

Texture function descriptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _shader_func_textureSize:

.. rst-class:: classref-method

ivec2 **textureSize**\ (\ |gsampler2D| s, int lod) :ref:`🔗<shader_func_textureSize>`

.. rst-class:: classref-method

ivec2 **textureSize**\ (\ samplerCube s, int lod) :ref:`🔗<shader_func_textureSize>`

.. rst-class:: classref-method

ivec2 **textureSize**\ (\ samplerCubeArray s, int lod) :ref:`🔗<shader_func_textureSize>`

.. rst-class:: classref-method

ivec3 **textureSize**\ (\ |gsampler2DArray| s, int lod) :ref:`🔗<shader_func_textureSize>`

.. rst-class:: classref-method

ivec3 **textureSize**\ (\ |gsampler3D| s, int lod) :ref:`🔗<shader_func_textureSize>`

    Retrieves the dimensions of a level of a texture.

    Returns the dimensions of level ``lod`` (if present) of the texture bound to sampler.

    The components in the return value are filled in, in order, with the width, height and depth
    of the texture. For the array forms, the last component of the return value is
    the number of layers in the texture array.

    :param s:
        The sampler to which the texture whose dimensions to retrieve is bound.

    :param lod:
        The level of the texture for which to retrieve the dimensions.

    :return:
        The dimensions of level ``lod`` (if present) of the texture bound to sampler.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/textureSize.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_textureQueryLod:

.. rst-class:: classref-method

vec2 **textureQueryLod**\ (\ |gsampler2D| s, vec2 p) :ref:`🔗<shader_func_textureQueryLod>`

.. rst-class:: classref-method

vec2 **textureQueryLod**\ (\ |gsampler2DArray| s, vec2 p) :ref:`🔗<shader_func_textureQueryLod>`

.. rst-class:: classref-method

vec2 **textureQueryLod**\ (\ |gsampler3D| s, vec3 p) :ref:`🔗<shader_func_textureQueryLod>`

.. rst-class:: classref-method

vec2 **textureQueryLod**\ (\ samplerCube s, vec3 p) :ref:`🔗<shader_func_textureQueryLod>`

    .. note:: Available only in the fragment shader.

    Compute the level-of-detail that would be used to sample from a texture.

    The mipmap array(s) that would be accessed is returned in the x component of
    the return value. The computed level-of-detail relative to the base level is
    returned in the y component of the return value.

    If called on an incomplete texture, the result of the operation is undefined.

    :param s:
        The sampler to which the texture whose level-of-detail will be queried is bound.

    :param p:
        The texture coordinates at which the level-of-detail will be queried.

    :return:
        See description.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/textureQueryLod.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_textureQueryLevels:

.. rst-class:: classref-method

int **textureQueryLevels**\ (\ |gsampler2D| s) :ref:`🔗<shader_func_textureQueryLevels>`

.. rst-class:: classref-method

int **textureQueryLevels**\ (\ |gsampler2DArray| s) :ref:`🔗<shader_func_textureQueryLevels>`

.. rst-class:: classref-method

int **textureQueryLevels**\ (\ |gsampler3D| s) :ref:`🔗<shader_func_textureQueryLevels>`

.. rst-class:: classref-method

int **textureQueryLevels**\ (\ samplerCube s) :ref:`🔗<shader_func_textureQueryLevels>`

    Compute the number of accessible mipmap levels of a texture.

    If called on an incomplete texture, or if no texture is associated with sampler, ``0`` is returned.

    :param s:
        The sampler to which the texture whose mipmap level count will be queried is bound.

    :return:
        The number of accessible mipmap levels in the texture, or ``0``.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/textureQueryLevels.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_texture:

.. rst-class:: classref-method

|gvec4_type| **texture**\ (\ |gsampler2D| s, vec2 p [, float bias] ) :ref:`🔗<shader_func_texture>`

.. rst-class:: classref-method

|gvec4_type| **texture**\ (\ |gsampler2DArray| s, vec3 p [, float bias] ) :ref:`🔗<shader_func_texture>`

.. rst-class:: classref-method

|gvec4_type| **texture**\ (\ |gsampler3D| s, vec3 p [, float bias] ) :ref:`🔗<shader_func_texture>`

.. rst-class:: classref-method

vec4 **texture**\ (\ samplerCube s, vec3 p [, float bias] ) :ref:`🔗<shader_func_texture>`

.. rst-class:: classref-method

vec4 **texture**\ (\ samplerCubeArray s, vec4 p [, float bias] ) :ref:`🔗<shader_func_texture>`

.. rst-class:: classref-method

vec4 **texture**\ (\ samplerExternalOES s, vec2 p [, float bias] ) :ref:`🔗<shader_func_texture>`

    Retrieves texels from a texture.

    Samples texels from the texture bound to ``s`` at texture coordinate ``p``. An optional bias, specified in ``bias`` is
    included in the level-of-detail computation that is used to choose mipmap(s) from which to sample.

    For shadow forms, the last component of ``p`` is used as Dsub and the array layer is specified in the second to last
    component of ``p``. (The second component of ``p`` is unused for 1D shadow lookups.)

    For non-shadow variants, the array layer comes from the last component of P.

    :param s:
        The sampler to which the texture from which texels will be retrieved is bound.

    :param p:
        The texture coordinates at which texture will be sampled.

    :param bias:
        An optional bias to be applied during level-of-detail computation.

    :return:
        A texel.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/texture.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_textureProj:

.. rst-class:: classref-method

|gvec4_type| **textureProj**\ (\ |gsampler2D| s, vec3 p [, float bias] ) :ref:`🔗<shader_func_textureProj>`

.. rst-class:: classref-method

|gvec4_type| **textureProj**\ (\ |gsampler2D| s, vec4 p [, float bias] ) :ref:`🔗<shader_func_textureProj>`

.. rst-class:: classref-method

|gvec4_type| **textureProj**\ (\ |gsampler3D| s, vec4 p [, float bias] ) :ref:`🔗<shader_func_textureProj>`

    Perform a texture lookup with projection.

    The texture coordinates consumed from ``p``, not including the last component of ``p``, are
    divided by the last component of ``p``. The resulting 3rd component of ``p`` in the shadow
    forms is used as Dref. After these values are computed, the texture lookup proceeds as in texture.

    :param s:
        The sampler to which the texture from which texels will be retrieved is bound.

    :param p:
        The texture coordinates at which texture will be sampled.

    :param bias:
        Optional bias to be applied during level-of-detail computation.

    :return:
        A texel.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/textureProj.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_textureLod:

.. rst-class:: classref-method

|gvec4_type| **textureLod**\ (\ |gsampler2D| s, vec2 p, float lod) :ref:`🔗<shader_func_textureLod>`

.. rst-class:: classref-method

|gvec4_type| **textureLod**\ (\ |gsampler2DArray| s, vec3 p, float lod) :ref:`🔗<shader_func_textureLod>`

.. rst-class:: classref-method

|gvec4_type| **textureLod**\ (\ |gsampler3D| s, vec3 p, float lod) :ref:`🔗<shader_func_textureLod>`

.. rst-class:: classref-method

vec4 **textureLod**\ (\ samplerCube s, vec3 p, float lod) :ref:`🔗<shader_func_textureLod>`

.. rst-class:: classref-method

vec4 **textureLod**\ (\ samplerCubeArray s, vec4 p, float lod) :ref:`🔗<shader_func_textureLod>`

    Performs a texture lookup at coordinate ``p`` from the texture bound to sampler with
    an explicit level-of-detail as specified in ``lod``. ``lod`` specifies λbase and sets the
    partial derivatives as follows:

    ::

        δu/δx=0, δv/δx=0, δw/δx=0
        δu/δy=0, δv/δy=0, δw/δy=0

    :param s:
        The sampler to which the texture from which texels will be retrieved is bound.

    :param p:
        The texture coordinates at which texture will be sampled.

    :param lod:
        The explicit level-of-detail.

    :return:
        A texel.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/textureLod.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_textureProjLod:

.. rst-class:: classref-method

|gvec4_type| **textureProjLod**\ (\ |gsampler2D| s, vec3 p, float lod) :ref:`🔗<shader_func_textureProjLod>`

.. rst-class:: classref-method

|gvec4_type| **textureProjLod**\ (\ |gsampler2D| s, vec4 p, float lod) :ref:`🔗<shader_func_textureProjLod>`

.. rst-class:: classref-method

|gvec4_type| **textureProjLod**\ (\ |gsampler3D| s, vec4 p, float lod) :ref:`🔗<shader_func_textureProjLod>`

    Performs a texture lookup with projection from an explicitly specified level-of-detail.

    The texture coordinates consumed from P, not including the last component of ``p``, are
    divided by the last component of ``p``. The resulting 3rd component of ``p`` in the shadow
    forms is used as Dref. After these values are computed, the texture lookup proceeds as in
    `textureLod<shader_func_textureLod>`, with ``lod`` used to specify the level-of-detail from
    which the texture will be sampled.

    :param s:
        The sampler to which the texture from which texels will be retrieved is bound.

    :param p:
        The texture coordinates at which texture will be sampled.

    :param lod:
        The explicit level-of-detail from which to fetch texels.

    :return:
       a texel

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/textureProjLod.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_textureGrad:

.. rst-class:: classref-method

|gvec4_type| **textureGrad**\ (\ |gsampler2D| s, vec2 p, vec2 dPdx, vec2 dPdy) :ref:`🔗<shader_func_textureGrad>`

.. rst-class:: classref-method

|gvec4_type| **textureGrad**\ (\ |gsampler2DArray| s, vec3 p, vec2 dPdx, vec2 dPdy) :ref:`🔗<shader_func_textureGrad>`

.. rst-class:: classref-method

|gvec4_type| **textureGrad**\ (\ |gsampler3D| s, vec3 p, vec2 dPdx, vec2 dPdy) :ref:`🔗<shader_func_textureGrad>`

.. rst-class:: classref-method

vec4 **textureGrad**\ (\ samplerCube s, vec3 p, vec3 dPdx, vec3 dPdy) :ref:`🔗<shader_func_textureGrad>`

.. rst-class:: classref-method

vec4 **textureGrad**\ (\ samplerCubeArray s, vec3 p, vec3 dPdx, vec3 dPdy) :ref:`🔗<shader_func_textureGrad>`

    Performs a texture lookup at coordinate ``p`` from the texture bound to sampler with explicit texture coordinate gradiends as specified in ``dPdx`` and ``dPdy``. Set:
     - ``δs/δx=δp/δx`` for a 1D texture, ``δp.s/δx`` otherwise
     - ``δs/δy=δp/δy`` for a 1D texture, ``δp.s/δy`` otherwise
     - ``δt/δx=0.0`` for a 1D texture, ``δp.t/δx`` otherwise
     - ``δt/δy=0.0`` for a 1D texture, ``δp.t/δy`` otherwise
     - ``δr/δx=0.0`` for a 1D or 2D texture, ``δp.p/δx`` otherwise
     - ``δr/δy=0.0``  for a 1D or 2D texture, ``δp.p/δy`` otherwise

    For the cube version, the partial derivatives of ``p`` are assumed to be in the coordinate system used before texture coordinates are projected onto the appropriate cube face.

    :param s:
        The sampler to which the texture from which texels will be retrieved is bound.

    :param p:
        The texture coordinates at which texture will be sampled.

    :param dPdx:
        The partial derivative of P with respect to window x.

    :param dPdy:
        The partial derivative of P with respect to window y.

    :return:
        A texel.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/textureGrad.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_textureProjGrad:

.. rst-class:: classref-method

|gvec4_type| **textureProjGrad**\ (\ |gsampler2D| s, vec3 p, vec2 dPdx, vec2 dPdy) :ref:`🔗<shader_func_textureProjGrad>`

.. rst-class:: classref-method

|gvec4_type| **textureProjGrad**\ (\ |gsampler2D| s, vec4 p, vec2 dPdx, vec2 dPdy) :ref:`🔗<shader_func_textureProjGrad>`

.. rst-class:: classref-method

|gvec4_type| **textureProjGrad**\ (\ |gsampler3D| s, vec4 p, vec3 dPdx, vec3 dPdy) :ref:`🔗<shader_func_textureProjGrad>`

    Perform a texture lookup with projection and explicit gradients.

    The texture coordinates consumed from ``p``, not including the last component of ``p``, are divided by the last component of ``p``.
    After these values are computed, the texture lookup proceeds as in `textureGrad<shader_func_textureGrad>`, passing ``dPdx`` and ``dPdy`` as gradients.

    :param s:
        The sampler to which the texture from which texels will be retrieved is bound.

    :param p:
        The texture coordinates at which texture will be sampled.

    :param dPdx:
        The partial derivative of ``p`` with respect to window x.

    :param dPdy:
        The partial derivative of ``p`` with respect to window y.

    :return:
        A texel.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/textureProjGrad.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_texelFetch:

.. rst-class:: classref-method

|gvec4_type| **texelFetch**\ (\ |gsampler2D| s, ivec2 p, int lod) :ref:`🔗<shader_func_texelFetch>`

.. rst-class:: classref-method

|gvec4_type| **texelFetch**\ (\ |gsampler2DArray| s, ivec3 p, int lod) :ref:`🔗<shader_func_texelFetch>`

.. rst-class:: classref-method

|gvec4_type| **texelFetch**\ (\ |gsampler3D| s, ivec3 p, int lod) :ref:`🔗<shader_func_texelFetch>`

    Performs a lookup of a single texel from texture coordinate ``p`` in the texture bound to sampler.

    :param s:
        The sampler to which the texture from which texels will be retrieved is bound.

    :param p:
        The texture coordinates at which texture will be sampled.

    :param lod:
        Specifies the level-of-detail within the texture from which the texel will be fetched.

    :return:
        A texel.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/texelFetch.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_textureGather:

.. rst-class:: classref-method

|gvec4_type| **textureGather**\ (\ |gsampler2D| s, vec2 p [, int comps] ) :ref:`🔗<shader_func_textureGather>`

.. rst-class:: classref-method

|gvec4_type| **textureGather**\ (\ |gsampler2DArray| s, vec3 p [, int comps] ) :ref:`🔗<shader_func_textureGather>`

.. rst-class:: classref-method

vec4 **textureGather**\ (\ samplerCube s, vec3 p [, int comps] ) :ref:`🔗<shader_func_textureGather>`

    Gathers four texels from a texture.

    Returns the value:

    ::

        vec4(Sample_i0_j1(p, base).comps,
             Sample_i1_j1(p, base).comps,
             Sample_i1_j0(p, base).comps,
             Sample_i0_j0(p, base).comps);

    :param s:
        The sampler to which the texture from which texels will be retrieved is bound.

    :param p:
        The texture coordinates at which texture will be sampled.

    :param comps:
        *optional* the component of the source texture (0 -> x, 1 -> y, 2 -> z, 3 -> w) that will be used to generate the resulting vector. Zero if not specified.

    :return:
        The gathered texel.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/textureGather.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_dFdx:

.. rst-class:: classref-method

|vec_type| **dFdx**\ (\ |vec_type| p) :ref:`🔗<shader_func_dFdx>`

    .. note:: Available only in the fragment shader.

    Returns the partial derivative of ``p`` with respect to the window x coordinate using local differencing.

    Returns either :ref:`dFdxCoarse<shader_func_dFdxCoarse>` or :ref:`dFdxFine<shader_func_dfdxFine>`.
    The implementation may choose which calculation to perform based upon factors
    such as performance or the value of the API ``GL_FRAGMENT_SHADER_DERIVATIVE_HINT`` hint.


    .. warning::
        Expressions that imply higher order derivatives such as ``dFdx(dFdx(n))``
        have undefined results, as do mixed-order derivatives such as ``dFdx(dFdy(n))``.

    :param p:
        The expression of which to take the partial derivative.

        .. note:: It is assumed that the expression ``p`` is continuous and therefore expressions evaluated via non-uniform control flow may be undefined.

    :return:
        The partial derivative of ``p``.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/dFdx.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_dFdxCoarse:

.. rst-class:: classref-method

|vec_type| **dFdxCoarse**\ (\ |vec_type| p) :ref:`🔗<shader_func_dFdxCoarse>`

    .. note::
        Available only in the fragment shader.
        Not available when using the Compatibility renderer.

    Returns the partial derivative of ``p`` with respect to the window x coordinate.

    Calculates derivatives using local differencing based on the value of ``p``
    for the current fragment's neighbors, and will possibly, but not necessarily,
    include the value for the current fragment. That is, over a given area, the
    implementation can compute derivatives in fewer unique locations than would
    be allowed for the corresponding :ref:`dFdxFine<shader_func_dFdxFine>` function.

    .. warning::
        Expressions that imply higher order derivatives such as ``dFdx(dFdx(n))``
        have undefined results, as do mixed-order derivatives such as ``dFdx(dFdy(n))``.

    :param p:
        The expression of which to take the partial derivative.

        .. note:: It is assumed that the expression ``p`` is continuous and therefore
            expressions evaluated via non-uniform control flow may be undefined.

    :return:
        The partial derivative of ``p``.

    https://registry.khronos.org/OpenGL-Refpages/gl4/html/dFdx.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_dFdxFine:

.. rst-class:: classref-method

|vec_type| **dFdxFine**\ (\ |vec_type| p) :ref:`🔗<shader_func_dFdxFine>`

    .. note::
        Available only in the fragment shader.
        Not available when using the Compatibility renderer.

    Returns the partial derivative of ``p`` with respect to the window x coordinate.

    Calculates derivatives using local differencing based on the value of ``p`` for the current fragment and its immediate neighbor(s).

    .. warning::
        Expressions that imply higher order derivatives such as ``dFdx(dFdx(n))``
        have undefined results, as do mixed-order derivatives such as ``dFdx(dFdy(n))``.

    :param p:
        The expression of which to take the partial derivative.

        .. note:: It is assumed that the expression ``p`` is continuous and therefore expressions evaluated via non-uniform control flow may be undefined.

    :return:
        The partial derivative of ``p``.

    https://registry.khronos.org/OpenGL-Refpages/gl4/html/dFdx.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_dFdy:

.. rst-class:: classref-method

|vec_type| **dFdy**\ (\ |vec_type| p) :ref:`🔗<shader_func_dFdy>`

    .. note:: Available only in the fragment shader.

    Returns the partial derivative of ``p`` with respect to the window y coordinate using local differencing.

    Returns either :ref:`dFdyCoarse<shader_func_dFdyCoarse>` or :ref:`dFdyFine<shader_func_dfdyFine>`.
    The implementation may choose which calculation to perform based upon factors
    such as performance or the value of the API ``GL_FRAGMENT_SHADER_DERIVATIVE_HINT`` hint.

    .. warning::
        Expressions that imply higher order derivatives such as ``dFdx(dFdx(n))``
        have undefined results, as do mixed-order derivatives such as ``dFdx(dFdy(n))``.

    :param p:
        The expression of which to take the partial derivative.

        .. note:: It is assumed that the expression ``p`` is continuous and therefore expressions evaluated via non-uniform control flow may be undefined.

    :return:
        The partial derivative of ``p``.

    https://registry.khronos.org/OpenGL-Refpages/gl4/html/dFdx.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_dFdyCoarse:

.. rst-class:: classref-method

|vec_type| **dFdyCoarse**\ (\ |vec_type| p) :ref:`🔗<shader_func_dFdyCoarse>`

    .. note::
        Available only in the fragment shader.
        Not available when using the Compatibility renderer.

    Returns the partial derivative of ``p`` with respect to the window y coordinate.

    Calculates derivatives using local differencing based on the value of ``p`` for the current fragment's neighbors, and will possibly,
    but not necessarily, include the value for the current fragment. That is, over a given area, the implementation can compute derivatives in fewer unique locations than
    would be allowed for the corresponding dFdyFine and dFdyFine functions.

    .. warning:: Expressions that imply higher order derivatives such as ``dFdx(dFdx(n))`` have undefined results, as do mixed-order derivatives such as ``dFdx(dFdy(n))``.

    :param p:
        The expression of which to take the partial derivative.

        .. note:: It is assumed that the expression ``p`` is continuous and therefore expressions evaluated via non-uniform control flow may be undefined.

    :return:
        The partial derivative of ``p``.

    https://registry.khronos.org/OpenGL-Refpages/gl4/html/dFdx.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_dFdyFine:

.. rst-class:: classref-method

|vec_type| **dFdyFine**\ (\ |vec_type| p) :ref:`🔗<shader_func_dFdyFine>`

    .. note::
        Available only in the fragment shader.
        Not available when using the Compatibility renderer.

    Returns the partial derivative of ``p`` with respect to the window y coordinate.

    Calculates derivatives using local differencing based on the value of ``p`` for the current fragment and its immediate neighbor(s).

    .. warning:: Expressions that imply higher order derivatives such as ``dFdx(dFdx(n))`` have undefined results, as do mixed-order derivatives such as ``dFdx(dFdy(n))``.

    :param p:
        The expression of which to take the partial derivative.

        .. note:: It is assumed that the expression ``p`` is continuous and therefore expressions evaluated via non-uniform control flow may be undefined.

    :return:
        The partial derivative of ``p``.

    https://registry.khronos.org/OpenGL-Refpages/gl4/html/dFdx.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_fwidth:

.. rst-class:: classref-method

|vec_type| **fwidth**\ (\ |vec_type| p) :ref:`🔗<shader_func_fwidth>`

    Returns the sum of the absolute value of derivatives in x and y.

    Uses local differencing for the input argument ``p``.

    Equivalent to ``abs(dFdx(p)) + abs(dFdy(p))``.

    :param p:
        The expression of which to take the partial derivative.

    :return:
        The partial derivative.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/fwidth.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_fwidthCoarse:

.. rst-class:: classref-method

|vec_type| **fwidthCoarse**\ (\ |vec_type| p) :ref:`🔗<shader_func_fwidthCoarse>`

    .. note::
        Available only in the fragment shader.
        Not available when using the Compatibility renderer.

    Returns the sum of the absolute value of derivatives in x and y.

    Uses local differencing for the input argument p.

    Equivalent  to ``abs(dFdxCoarse(p)) + abs(dFdyCoarse(p))``.

    :param p:
        The expression of which to take the partial derivative.

    :return:
        The partial derivative.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/fwidth.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_fwidthFine:

.. rst-class:: classref-method

|vec_type| **fwidthFine**\ (\ |vec_type| p) :ref:`🔗<shader_func_fwidthFine>`

    .. note::
        Available only in the fragment shader.
        Not available when using the Compatibility renderer.

    Returns the sum of the absolute value of derivatives in x and y.

    Uses local differencing for the input argument p.

    Equivalent to ``abs(dFdxFine(p)) + abs(dFdyFine(p))``.

    :param p:
        The expression of which to take the partial derivative.

    :return:
        The partial derivative.

    https://registry.khronos.org/OpenGL-Refpages/gl4/html/fwidth.xhtml


.. rst-class:: classref-section-separator

----













.. rst-class:: classref-reftable-group

Packing and unpacking functions
-------------------------------

These functions convert floating-point numbers into various sized integers and
then pack those integers into a single 32bit unsigned integer. The 'unpack'
functions perform the opposite operation, returning the original
floating-point numbers.

.. table::
    :class: nowrap-col2
    :widths: auto

    +------------+------------------------------------------------------------------------+--------------------------------------------------------------+
    | | uint     | | :ref:`packHalf2x16<shader_func_packHalf2x16>`\ (\ vec2 v)            | Convert two 32-bit floats to 16 bit floats and pack them.    |
    | | vec2     | | :ref:`unpackHalf2x16<shader_func_unpackHalf2x16>`\ (\ uint v)        |                                                              |
    +------------+------------------------------------------------------------------------+--------------------------------------------------------------+
    | | uint     | | :ref:`packUnorm2x16<shader_func_packUnorm2x16>`\ (\ vec2 v)          | Convert two normalized (range 0..1) 32-bit floats            |
    | | vec2     | | :ref:`unpackUnorm2x16<shader_func_unpackUnorm2x16>`\ (\ uint v)      | to 16-bit unsigned ints and pack them.                       |
    +------------+------------------------------------------------------------------------+--------------------------------------------------------------+
    | | uint     | | :ref:`packSnorm2x16<shader_func_packSnorm2x16>`\ (\ vec2 v)          | Convert two signed normalized (range -1..1) 32-bit floats    |
    | | vec2     | | :ref:`unpackSnorm2x16<shader_func_unpackSnorm2x16>`\ (\ uint v)      | to 16-bit signed ints and pack them.                         |
    +------------+------------------------------------------------------------------------+--------------------------------------------------------------+
    | | uint     | | :ref:`packUnorm4x8<shader_func_packUnorm4x8>`\ (\ vec4 v)            | Convert four normalized (range 0..1) 32-bit floats           |
    | | vec4     | | :ref:`unpackUnorm4x8<shader_func_unpackUnorm4x8>`\ (\ uint v)        | into 8-bit unsigned ints and pack them.                      |
    +------------+------------------------------------------------------------------------+--------------------------------------------------------------+
    | | uint     | | :ref:`packSnorm4x8<shader_func_packSnorm4x8>`\ (\ vec4 v)            | Convert four signed normalized (range -1..1) 32-bit floats   |
    | | vec4     | | :ref:`unpackSnorm4x8<shader_func_unpackSnorm4x8>`\ (\ uint v)        | into 8-bit signed ints and pack them.                        |
    +------------+------------------------------------------------------------------------+--------------------------------------------------------------+

.. rst-class:: classref-descriptions-group

Packing and unpacking function descriptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _shader_func_packHalf2x16:

.. rst-class:: classref-method

uint **packHalf2x16**\ (\ vec2 v) :ref:`🔗<shader_func_packHalf2x16>`

    Converts two 32-bit floating-point quantities to 16-bit floating-point
    quantities and packs them into a single 32-bit integer.

    Returns an unsigned integer obtained by converting the components of a two-component floating-point vector to
    the 16-bit floating-point representation found in the OpenGL Specification, and then packing these two
    16-bit integers into a 32-bit unsigned integer. The first vector component specifies the 16 least-significant
    bits of the result; the second component specifies the 16 most-significant bits.

    :param v:
        A vector of two 32-bit floating-point values that are to be converted to 16-bit representation and packed into the result.

    :return:
        The packed value.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/packHalf2x16.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_unpackHalf2x16:

.. rst-class:: classref-method

vec2 **unpackHalf2x16**\ (\ uint v) :ref:`🔗<shader_func_unpackHalf2x16>`

    Inverse of :ref:`packHalf2x16<shader_func_packHalf2x16>`.

    Unpacks a 32-bit integer into two 16-bit floating-point values, converts them to 32-bit floating-point values, and puts them into a vector.
    The first component of the vector is obtained from the 16 least-significant bits of ``v``; the second component is obtained from the
    16 most-significant bits of ``v``.

    :param v:
        A single 32-bit unsigned integer containing 2 packed 16-bit floating-point values.

    :return:
        Two unpacked floating-point values.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/unpackHalf2x16.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_packUnorm2x16:

.. rst-class:: classref-method

uint **packUnorm2x16**\ (\ vec2 v) :ref:`🔗<shader_func_packUnorm2x16>`

    Pack floating-point values into an unsigned integer.

    Converts each component of the normalized floating-point value v into 16-bit integer values and then packs the results into a 32-bit unsigned integer.

    The conversion for component c of ``v`` to fixed-point is performed as follows:

    ::

        round(clamp(c, 0.0, 1.0) * 65535.0)

    The first component of the vector will be written to the least significant bits of the output; the last component will be written to the most significant bits.


    :param v:
        A vector of values to be packed into an unsigned integer.

    :return:
        Unsigned 32 bit integer containing the packed encoding of the vector.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/packUnorm.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_unpackUnorm2x16:

.. rst-class:: classref-method

vec2 **unpackUnorm2x16**\ (\ uint v) :ref:`🔗<shader_func_unpackUnorm2x16>`

    Unpack floating-point values from an unsigned integer.

    Unpack single 32-bit unsigned integers into a pair of 16-bit unsigned integers.
    Then, each component is converted to a normalized floating-point value to generate the returned two-component vector.

    The conversion for unpacked fixed point value f to floating-point is performed as follows:

        f / 65535.0

    The first component of the returned vector will be extracted from the least significant bits of the input; the last component will be extracted from the most significant bits.

    :param v:
        An unsigned integer containing packed floating-point values.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/unpackUnorm.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_packSnorm2x16:

.. rst-class:: classref-method

uint **packSnorm2x16**\ (\ vec2 v) :ref:`🔗<shader_func_packSnorm2x16>`

    Packs floating-point values into an unsigned integer.

    Convert each component of the normalized floating-point value ``v`` into 16-bit integer values and then packs the results into a 32-bit unsigned integer.

    The conversion for component c of ``v`` to fixed-point is performed as follows:

    ::

        round(clamp(c, -1.0, 1.0) * 32767.0)

    The first component of the vector will be written to the least significant bits of the output; the last component will be written to the most significant bits.

    :param v:
        A vector of values to be packed into an unsigned integer.

    :return:
        Unsigned 32 bit integer containing the packed encoding of the vector.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/packUnorm.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_unpackSnorm2x16:

.. rst-class:: classref-method

vec2 **unpackSnorm2x16**\ (\ uint v) :ref:`🔗<shader_func_unpackSnorm2x16>`

    Unpacks floating-point values from an unsigned integer.

    Unpacks single 32-bit unsigned integers into a pair of 16-bit signed integers.
    Then, each component is converted to a normalized floating-point value to generate the returned two-component vector.

    The conversion for unpacked fixed point value f to floating-point is performed as follows:

        clamp(f / 32727.0, -1.0, 1.0)

    The first component of the returned vector will be extracted from the least significant bits of the input; the last component will be extracted from the most significant bits.

    :param v:
        An unsigned integer containing packed floating-point values.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/unpackUnorm.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_packUnorm4x8:

.. rst-class:: classref-method

uint **packUnorm4x8**\ (\ vec4 v) :ref:`🔗<shader_func_packUnorm4x8>`

    Packs floating-point values into an unsigned integer.

    Converts each component of the normalized floating-point value ``v`` into 16-bit integer values and then packs the results into a 32-bit unsigned integer.

    The conversion for component c of ``v`` to fixed-point is performed as follows:

    ::

        round(clamp(c, 0.0, 1.0) * 255.0)

    The first component of the vector will be written to the least significant bits of the output; the last component will be written to the most significant bits.


    :param v:
        A vector of values to be packed into an unsigned integer.

    :return:
        Unsigned 32 bit integer containing the packed encoding of the vector.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/packUnorm.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_unpackUnorm4x8:

.. rst-class:: classref-method

vec4 **unpackUnorm4x8**\ (\ uint v) :ref:`🔗<shader_func_unpackUnorm4x8>`

    Unpacks floating-point values from an unsigned integer.

    Unpacks single 32-bit unsigned integers into four 8-bit unsigned integers.
    Then, each component is converted to a normalized floating-point value to generate the returned four-component vector.

    The conversion for unpacked fixed point value f to floating-point is performed as follows:

        f / 255.0

    The first component of the returned vector will be extracted from the least significant bits of the input; the last component will be extracted from the most significant bits.

    :param v:
        An unsigned integer containing packed floating-point values.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/unpackUnorm.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_packSnorm4x8:

.. rst-class:: classref-method

uint **packSnorm4x8**\ (\ vec4 v) :ref:`🔗<shader_func_packSnorm4x8>`

    Packs floating-point values into an unsigned integer.

    Convert each component of the normalized floating-point value ``v`` into 16-bit integer values and then packs the results into a 32-bit unsigned integer.

    The conversion for component c of ``v`` to fixed-point is performed as follows:

    ::

        round(clamp(c, -1.0, 1.0) * 127.0)

    The first component of the vector will be written to the least significant bits of the output; the last component will be written to the most significant bits.


    :param v:
        A vector of values to be packed into an unsigned integer.

    :return:
        Unsigned 32 bit integer containing the packed encoding of the vector.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/packUnorm.xhtml

.. rst-class:: classref-item-separator

----




.. _shader_func_unpackSnorm4x8:

.. rst-class:: classref-method

vec4 **unpackSnorm4x8**\ (\ uint v) :ref:`🔗<shader_func_unpackSnorm4x8>`

    Unpack floating-point values from an unsigned integer.

    Unpack single 32-bit unsigned integers into four 8-bit signed integers.
    Then, each component is converted to a normalized floating-point value to generate the returned four-component vector.

    The conversion for unpacked fixed point value f to floating-point is performed as follows:

        clamp(f / 127.0, -1.0, 1.0)

    The first component of the returned vector will be extracted from the least significant bits of the input; the last component will be extracted from the most significant bits.

    :param v:
        An unsigned integer containing packed floating-point values.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/unpackUnorm.xhtml


.. rst-class:: classref-section-separator

----














.. rst-class:: classref-reftable-group

Bitwise functions
-------------------

.. table::
    :class: nowrap-col2
    :widths: auto

    +-------------------+---------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
    | | |vec_int_type|  | | :ref:`bitfieldExtract<shader_func_bitfieldExtract>`\ (\ |vec_int_type| value, int offset, int bits)                                       | Extracts a range of bits from an integer.                           |
    | | |vec_uint_type| | | :ref:`bitfieldExtract<shader_func_bitfieldExtract>`\ (\ |vec_uint_type| value, int offset, int bits)                                      |                                                                     |
    +-------------------+---------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
    | | |vec_int_type|  | | :ref:`bitfieldInsert<shader_func_bitfieldInsert>`\ (\ |vec_int_type| base, |vec_int_type| insert, int offset, int bits)                   | Insert a range of bits into an integer.                             |
    | | |vec_uint_type| | | :ref:`bitfieldInsert<shader_func_bitfieldInsert>`\ (\ |vec_uint_type| base, |vec_uint_type| insert, int offset, int bits)                 |                                                                     |
    +-------------------+---------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
    | | |vec_int_type|  | | :ref:`bitfieldReverse<shader_func_bitfieldReverse>`\ (\ |vec_int_type| value)                                                             | Reverse the order of bits in an integer.                            |
    | | |vec_uint_type| | | :ref:`bitfieldReverse<shader_func_bitfieldReverse>`\ (\ |vec_uint_type| value)                                                            |                                                                     |
    +-------------------+---------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
    | | |vec_int_type|  | | :ref:`bitCount<shader_func_bitCount>`\ (\ |vec_int_type| value)                                                                           | Counts the number of 1 bits in an integer.                          |
    | | |vec_uint_type| | | :ref:`bitCount<shader_func_bitCount>`\ (\ |vec_uint_type| value)                                                                          |                                                                     |
    +-------------------+---------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
    | | |vec_int_type|  | | :ref:`findLSB<shader_func_findLSB>`\ (\ |vec_int_type| value)                                                                             | Find the index of the least significant bit set to 1 in an integer. |
    | | |vec_uint_type| | | :ref:`findLSB<shader_func_findLSB>`\ (\ |vec_uint_type| value)                                                                            |                                                                     |
    +-------------------+---------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
    | | |vec_int_type|  | | :ref:`findMSB<shader_func_findMSB>`\ (\ |vec_int_type| value)                                                                             | Find the index of the most significant bit set to 1 in an integer.  |
    | | |vec_uint_type| | | :ref:`findMSB<shader_func_findMSB>`\ (\ |vec_uint_type| value)                                                                            |                                                                     |
    +-------------------+---------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
    | | |void|          | | :ref:`imulExtended<shader_func_imulExtended>`\ (\ |vec_int_type| x, |vec_int_type| y, out |vec_int_type| msb, out |vec_int_type| lsb)     | Multiplies two 32-bit numbers and produce a 64-bit result.          |
    | | |void|          | | :ref:`umulExtended<shader_func_umulExtended>`\ (\ |vec_uint_type| x, |vec_uint_type| y, out |vec_uint_type| msb, out |vec_uint_type| lsb) |                                                                     |
    +-------------------+---------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
    | |vec_uint_type|   | :ref:`uaddCarry<shader_func_uaddCarry>`\ (\ |vec_uint_type| x, |vec_uint_type| y, out |vec_uint_type| carry)                                | Adds two unsigned integers and generates carry.                     |
    +-------------------+---------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
    | |vec_uint_type|   | :ref:`usubBorrow<shader_func_usubBorrow>`\ (\ |vec_uint_type| x, |vec_uint_type| y, out |vec_uint_type| borrow)                             | Subtracts two unsigned integers and generates borrow.               |
    +-------------------+---------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
    | |vec_type|        | :ref:`ldexp<shader_func_ldexp>`\ (\ |vec_type| x, out |vec_int_type| exp)                                                                   | Assemble a floating-point number from a value and exponent.         |
    +-------------------+---------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
    | |vec_type|        | :ref:`frexp<shader_func_frexp>`\ (\ |vec_type| x, out |vec_int_type| exp)                                                                   | Splits a floating-point number (``x``) into significand integral    |
    |                   |                                                                                                                                             | components                                                          |
    +-------------------+---------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+


.. rst-class:: classref-descriptions-group

Bitwise function descriptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _shader_func_bitfieldExtract:

.. rst-class:: classref-method

|vec_int_type| **bitfieldExtract**\ (\ |vec_int_type| value, int offset, int bits) :ref:`🔗<shader_func_bitfieldExtract>`

    Extracts a subset of the bits of ``value`` and returns it in the least significant bits of the result.
    The range of bits extracted is ``[offset, offset + bits - 1]``.

    The most significant bits of the result will be set to zero.

    .. note::
        If bits is zero, the result will be zero.

    .. warning::
        The result will be undefined if:

        - offset or bits is negative.
        - if the sum of offset and bits is greater than the number of bits used to store the operand.

    :param value:
        The integer from which to extract bits.

    :param offset:
        The index of the first bit to extract.

    :param bits:
        The number of bits to extract.

    :return:
        Integer with the requested bits.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/bitfieldExtract.xhtml

.. rst-class:: classref-item-separator

----


.. rst-class:: classref-method

|vec_uint_type| **bitfieldExtract**\ (\ |vec_uint_type| value, int offset, int bits) :ref:`🔗<shader_func_bitfieldExtract>`

    |componentwise|

    Extracts a subset of the bits of ``value`` and returns it in the least significant bits of the result.
    The range of bits extracted is ``[offset, offset + bits - 1]``.

    The most significant bits will be set to the value of ``offset + base - 1`` (i.e., it is sign extended to the width of the return type).

    .. note::
        If bits is zero, the result will be zero.

    .. warning::
        The result will be undefined if:

        - offset or bits is negative.
        - if the sum of offset and bits is greater than the number of bits used to store the operand.

    :param value:
        The integer from which to extract bits.

    :param offset:
        The index of the first bit to extract.

    :param bits:
        The number of bits to extract.

    :return:
        Integer with the requested bits.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/bitfieldExtract.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_bitfieldInsert:

.. rst-class:: classref-method

|vec_uint_type| **bitfieldExtract**\ (\ |vec_uint_type| value, int offset, int bits) :ref:`🔗<shader_func_bitfieldInsert>`

.. rst-class:: classref-method

|vec_uint_type| **bitfieldInsert**\ (\ |vec_uint_type| base, |vec_uint_type| insert, int offset, int bits) :ref:`🔗<shader_func_bitfieldInsert>`

    |componentwise|

    Inserts the ``bits`` least significant bits of ``insert`` into ``base`` at offset ``offset``.

    The returned value will have bits [offset, offset + bits + 1] taken from [0, bits - 1] of ``insert`` and
    all other bits taken directly from the corresponding bits of base.

    .. note:: If bits is zero, the result will be the original value of base.

    .. warning::
        The result will be undefined if:

        - offset or bits is negative.
        - if the sum of offset and bits is greater than the number of bits used to store the operand.

    :param base:
        The integer into which to insert ``insert``.

    :param insert:
        The value of the bits to insert.

    :param offset:
        The index of the first bit to insert.

    :param bits:
        The number of bits to insert.

    :return:
        ``base`` with inserted bits.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/bitfieldInsert.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_bitfieldReverse:

.. rst-class:: classref-method

|vec_int_type| **bitfieldReverse**\ (\ |vec_int_type| value) :ref:`🔗<shader_func_bitfieldReverse>`

.. rst-class:: classref-method

|vec_uint_type| **bitfieldReverse**\ (\ |vec_uint_type| value) :ref:`🔗<shader_func_bitfieldReverse>`

    |componentwise|

    Reverse the order of bits in an integer.

    The bit numbered ``n`` will be taken from bit ``(bits - 1) - n`` of ``value``, where bits is the total number of bits used to represent ``value``.

    :param value:
        The value whose bits to reverse.

    :return:
        ``value`` but with its bits reversed.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/bitfieldReverse.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_bitCount:

.. rst-class:: classref-method

|vec_int_type| **bitCount**\ (\ |vec_int_type| value) :ref:`🔗<shader_func_bitCount>`

.. rst-class:: classref-method

|vec_uint_type| **bitCount**\ (\ |vec_uint_type| value) :ref:`🔗<shader_func_bitCount>`

    |componentwise|

    Counts the number of 1 bits in an integer.

    :param value:
        The value whose bits to count.

    :return:
        The number of bits that are set to 1 in the binary representation of ``value``.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/bitCount.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_findLSB:

.. rst-class:: classref-method

|vec_int_type| **findLSB**\ (\ |vec_int_type| value) :ref:`🔗<shader_func_findLSB>`

.. rst-class:: classref-method

|vec_uint_type| **findLSB**\ (\ |vec_uint_type| value) :ref:`🔗<shader_func_findLSB>`

    |componentwise|

    Find the index of the least significant bit set to ``1``.

    .. note:: If ``value`` is zero, ``-1`` will be returned.

    :param value:
        The value whose bits to scan.

    :return:
        The bit number of the least significant bit that is set to 1 in the binary representation of value.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/findLSB.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_findMSB:

.. rst-class:: classref-method

|vec_int_type| **findMSB**\ (\ |vec_int_type| value) :ref:`🔗<shader_func_findMSB>`

.. rst-class:: classref-method

|vec_uint_type| **findMSB**\ (\ |vec_uint_type| value) :ref:`🔗<shader_func_findMSB>`

    |componentwise|

    Find the index of the most significant bit set to 1.

    .. note::
        For signed integer types, the sign bit is checked first and then:
         - For positive integers, the result will be the bit number of the most significant bit that is set to 1.
         - For negative integers, the result will be the bit number of the most significant bit set to 0.

    .. note:: For a value of zero or negative 1, -1 will be returned.

    :param value:
        The value whose bits to scan.

    :return:
        The bit number of the most significant bit that is set to 1 in the binary representation of value.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/findMSB.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_imulExtended:

.. rst-class:: classref-method

|void| **imulExtended**\ (\ |vec_int_type| x, |vec_int_type| y, out |vec_int_type| msb, out |vec_int_type| lsb) :ref:`🔗<shader_func_imulExtended>`

    |componentwise|

    Perform 32-bit by 32-bit signed multiplication to produce a 64-bit result.

    The 32 least significant bits of this product are returned in ``lsb`` and the 32 most significant bits are returned in ``msb``.

    :param x:
        The first multiplicand.

    :param y:
        The second multiplicand.

    :param msb:
        The variable to receive the most significant word of the product.

    :param lsb:
        The variable to receive the least significant word of the product.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/umulExtended.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_umulExtended:

.. rst-class:: classref-method

|void| **umulExtended**\ (\ |vec_uint_type| x, |vec_uint_type| y, out |vec_uint_type| msb, out |vec_uint_type| lsb) :ref:`🔗<shader_func_umulExtended>`

    |componentwise|

    Perform 32-bit by 32-bit unsigned multiplication to produce a 64-bit result.

    The 32 least significant bits of this product are returned in ``lsb`` and the 32 most significant bits are returned in ``msb``.

    :param x:
        The first multiplicand.

    :param y:
        The second multiplicand.

    :param msb:
        The variable to receive the most significant word of the product.

    :param lsb:
        The variable to receive the least significant word of the product.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/umulExtended.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_uaddCarry:

.. rst-class:: classref-method

|vec_uint_type| **uaddCarry**\ (\ |vec_uint_type| x, |vec_uint_type| y, out |vec_uint_type| carry) :ref:`🔗<shader_func_uaddCarry>`

    |componentwise|

    Add unsigned integers and generate carry.

    adds two 32-bit unsigned integer variables (scalars or vectors) and generates a 32-bit unsigned integer result, along with a carry output.
    The value carry is .

    :param x:
        The first operand.

    :param y:
        The second operand.

    :param carry:
        0 if the sum is less than 2\ :sup:`32`, otherwise 1.

    :return:
        ``(x + y) % 2^32``.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/uaddCarry.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_usubBorrow:

.. rst-class:: classref-method

|vec_uint_type| **usubBorrow**\ (\ |vec_uint_type| x, |vec_uint_type| y, out |vec_uint_type| borrow) :ref:`🔗<shader_func_usubBorrow>`

    |componentwise|

    Subtract unsigned integers and generate borrow.

    :param x:
        The first operand.

    :param y:
        The second operand.

    :param borrow:
        ``0`` if ``x >= y``, otherwise ``1``.

    :return:
        The difference of ``x`` and ``y`` if non-negative, or 2\ :sup:`32` plus that difference otherwise.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/usubBorrow.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_ldexp:

.. rst-class:: classref-method

|vec_type| **ldexp**\ (\ |vec_type| x, out |vec_int_type| exp) :ref:`🔗<shader_func_ldexp>`

    |componentwise|

    Assembles a floating-point number from a value and exponent.

    .. warning::
        If this product is too large to be represented in the floating-point
        type, the result is undefined.

    :param x:
        The value to be used as a source of significand.

    :param exp:
        The value to be used as a source of exponent.

    :return:
        ``x * 2^exp``

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/ldexp.xhtml

.. rst-class:: classref-item-separator

----


.. _shader_func_frexp:

.. rst-class:: classref-method

|vec_type| **frexp**\ (\ |vec_type| x, out |vec_int_type| exp) :ref:`🔗<shader_func_frexp>`

    |componentwise|

    Extracts ``x`` into a floating-point significand in the range ``[0.5, 1.0)`` and in integral exponent of two, such that:

    ::

        x = significand * 2 ^ exponent

    For a floating-point value of zero, the significand and exponent are both zero.

    .. warning:: For a floating-point value that is an infinity or a floating-point NaN, the results are undefined.

    :param x:
        The value from which significand and exponent are to be extracted.

    :param exp:
        The variable into which to place the exponent of ``x``.

    :return:
        The significand of ``x``.

    https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/frexp.xhtml


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
.. |componentwise| replace:: :ref:`Component-wise Function<shading_componentwise>`.
