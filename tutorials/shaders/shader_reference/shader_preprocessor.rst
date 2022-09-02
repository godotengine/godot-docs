.. _doc_shader_preprocessor:

Shader Preprocessor
===================

The shader preprocessor is an optional step before shader compilation of text shaders in Godot.
If you don't need it, you may ignore it, but it contains some useful macros which may speed up your productivity.

#define
^^^^^^^
\ **Syntax:** `#define identifier <replacement_code>`.

Defines the identifier after that directive as a macro, and replaces all successive occurrence of it with the replacement code given in the shader.
If the replacement code is not defined, it may only be used within `#ifdef` or `#ifndef` directives.

.. code-block:: glsl

    shader_type spatial;

    #define USE_MY_COLOR
    #define MY_COLOR vec3(1, 0, 0)

    void fragment() {
    #ifdef USE_MY_COLOR
        ALBEDO = MY_COLOR;
    #endif
    }

#if
^^^
\ **Syntax:** `#if condition`.

The `#if` directive checks the condition and if it evaluates to a non-zero value, the code block is included, otherwise it is skipped.
In order to evaluate, the condition must be an expression giving a simple floating-point, integer or boolean result. There may be multiple condition blocks connected by `||` or `&&` operators.
It may be continued by a `#else` block, but must be ended with the `#endif` directive.

.. code-block:: glsl

    #define VAR 3
    #define USE_LIGHT 0 // evaluates to false
    #define USE_COLOR 1 // evaluates to true

    #if VAR == 3 && (USE_LIGHT || USE_COLOR)


    #endif

#ifdef
^^^^^^
\ **Syntax:** `#ifdef identifier`.

Checks whether the passed identifier is defined by `#define` before that directive. Useful for creating multiple shader versions in the same file.
It may be continued by a `#else` block, but must be ended with the `#endif` directive.

.. code-block:: glsl

    #define USE_LIGHT
    #ifdef USE_LIGHT

    #endif

#ifndef
^^^^^^^
\ **Syntax:** `#ifndef identifier`.

Similar to `#ifdef` but checks whether the passed identifier is not defined by `#define` before that directive.

#else
^^^^^
\ **Syntax:** `#else`.

Defines the optional block which is included when the previously defined `#if`, `#ifdef` or `#ifndef` directive evaluates to false.

.. code-block:: glsl

    shader_type spatial;

    #define MY_COLOR vec3(1, 0, 0)

    void fragment() {
    #ifndef MY_COLOR
        ALBEDO = MY_COLOR;
    #else
        ALBEDO = vec3(0, 0, 1);
    #endif
    }

#endif
^^^^^^
\ **Syntax:** `#endif`.

Used as terminator for the `#if`, `#ifdef`, `#ifndef` or subsequent `#else` directives.

#undef
^^^^^^
\ **Syntax:** `#undef identifier`.

The `#undef` directive may be used to cancel the previously defined `#define` directive: 

.. code-block:: glsl

    #define MY_COLOR vec3(1, 0, 0)

    vec3 get_red_color() {
        return MY_COLOR;
    }

    #undef MY_COLOR
    #define MY_COLOR vec3(0, 1, 0)

    vec3 get_green_color() {
        return MY_COLOR;
    }

Without `#undef` in that case there will be a macro redefinition error.

#include
^^^^^^^^
\ **Syntax:** `#include "path"`.

The `#include` directive includes the content of shader include to a shader. It may be used in any place, but is recommended at the beginning of the shader file, 
after the `shader_type` to prevent possible errors. The shader include may be created by using a `File → Create Shader Include` menu option of the shader editor.

.. code-block:: glsl

    #include "my_shader_inc.gdshaderinc"

#pragma
^^^^^^^
\ **Syntax:** `#pragma value`.

The `#pragma` directive provides additional information to the preprocessor or compiler.

Currently, it may have only one value: `disable_preprocessor`.
If you don't need the preprocessor, use that directive, and it will speed up the shader compilation by excluding the preprocessor step. 

.. code-block:: glsl

    #pragma disable_preprocessor
