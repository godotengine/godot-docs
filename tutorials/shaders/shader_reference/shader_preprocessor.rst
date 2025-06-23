.. _doc_shader_preprocessor:

Shader preprocessor
===================

Why use a shader preprocessor?
------------------------------

In programming languages, a *preprocessor* allows changing the code before the
compiler reads it. Unlike the compiler, the preprocessor does not care about
whether the syntax of the preprocessed code is valid. The preprocessor always
performs what the *directives* tell it to do. A directive is a statement
starting with a hash symbol (``#``). It is not a *keyword* of the shader
language (such as ``if`` or ``for``), but a special kind of token within the
language.

From Godot 4.0 onwards, you can use a shader preprocessor within text-based
shaders. The syntax is similar to what most GLSL shader compilers support
(which in turn is similar to the C/C++ preprocessor).

.. note::

    The shader preprocessor is not available in :ref:`visual shaders <doc_visual_shaders>`.
    If you need to introduce preprocessor statements to a visual shader, you can
    convert it to a text-based shader using the **Convert to Shader** option in
    the VisualShader inspector resource dropdown. This conversion is a one-way
    operation; text shaders cannot be converted back to visual shaders.

Directives
----------

General syntax
~~~~~~~~~~~~~~

- Preprocessor directives do not use brackets (``{}``), but can use parentheses.
- Preprocessor directives **never** end with semicolons (with the exception of ``#define``,
  where this is allowed but potentially dangerous).
- Preprocessor directives can span several lines by ending each line with a
  backslash (``\``). The first line break *not* featuring a backslash will end
  the preprocessor statement.

#define
~~~~~~~

**Syntax:** ``#define <identifier> [replacement_code]``.

Defines the identifier after that directive as a macro, and replaces all
successive occurrences of it with the replacement code given in the shader.
Replacement is performed on a "whole words" basis, which means no replacement is
performed if the string is part of another string (without any spaces or
operators separating it).

Defines with replacements may also have one or more *arguments*, which can then
be passed when referencing the define (similar to a function call).

If the replacement code is not defined, the identifier may only be used with
``#ifdef`` or ``#ifndef`` directives.

If the *concatenation* symbol (``##``) is present in the replacement code then
it will be removed upon macro insertion, together with any space surrounding
it, and join the surrounding words and arguments into a new token.

.. code-block:: glsl

    uniform sampler2D material0;

    #define SAMPLE(N) vec4 tex##N = texture(material##N, UV)

    void fragment() {
        SAMPLE(0);
        ALBEDO = tex0.rgb;
    }

Compared to constants (``const CONSTANT = value;``), ``#define`` can be used
anywhere within the shader (including in uniform hints).
``#define`` can also be used to insert arbitrary shader code at any location,
while constants can't do that.

.. code-block:: glsl

    shader_type spatial;

    // Notice the lack of semicolon at the end of the line, as the replacement text
    // shouldn't insert a semicolon on its own.
    // If the directive ends with a semicolon, the semicolon is inserted in every usage
    // of the directive, even when this causes a syntax error.
    #define USE_MY_COLOR
    #define MY_COLOR vec3(1, 0, 0)

    // Replacement with arguments.
    // All arguments are required (no default values can be provided).
    #define BRIGHTEN_COLOR(r, g, b) vec3(r + 0.5, g + 0.5, b + 0.5)

    // Multiline replacement using backslashes for continuation:
    #define SAMPLE(param1, param2, param3, param4) long_function_call( \
            param1, \
            param2, \
            param3, \
            param4 \
    )

    void fragment() {
    #ifdef USE_MY_COLOR
        ALBEDO = MY_COLOR;
    #endif
    }


Defining a ``#define`` for an identifier that is already defined results in an
error. To prevent this, use ``#undef <identifier>``.

#undef
~~~~~~

**Syntax:** ``#undef identifier``

The ``#undef`` directive may be used to cancel a previously defined ``#define`` directive:

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

    // Like in most preprocessors, undefining a define that was not previously defined is allowed
    // (and won't print any warning or error).
    #undef THIS_DOES_NOT_EXIST

Without ``#undef`` in the above example, there would be a macro redefinition error.

#if
~~~

**Syntax:** ``#if <condition>``

The ``#if`` directive checks whether the ``condition`` passed. If it evaluates
to a non-zero value, the code block is included, otherwise it is skipped.

To evaluate correctly, the condition must be an expression giving a simple
floating-point, integer or boolean result. There may be multiple condition
blocks connected by ``&&`` (AND) or ``||`` (OR) operators. It may be continued
by an ``#else`` block, but **must** be ended with the ``#endif`` directive.

.. code-block:: glsl

    #define VAR 3
    #define USE_LIGHT 0 // Evaluates to `false`.
    #define USE_COLOR 1 // Evaluates to `true`.

    #if VAR == 3 && (USE_LIGHT || USE_COLOR)
    // Condition is `true`. Include this portion in the final shader.
    #endif

Using the ``defined()`` *preprocessor function*, you can check whether the
passed identifier is defined a by ``#define`` placed above that directive. This
is useful for creating multiple shader versions in the same file. It may be
continued by an ``#else`` block, but must be ended with the ``#endif`` directive.

The ``defined()`` function's result can be negated by using the ``!`` (boolean NOT)
symbol in front of it. This can be used to check whether a define is *not* set.

.. code-block:: glsl

    #define USE_LIGHT
    #define USE_COLOR

    // Correct syntax:
    #if defined(USE_LIGHT) || defined(USE_COLOR) || !defined(USE_REFRACTION)
    // Condition is `true`. Include this portion in the final shader.
    #endif

Be careful, as ``defined()`` must only wrap a single identifier within parentheses, never more:

.. code-block:: glsl

    // Incorrect syntax (parentheses are not placed where they should be):
    #if defined(USE_LIGHT || USE_COLOR || !USE_REFRACTION)
    // This will cause an error or not behave as expected.
    #endif

.. tip::

    In the shader editor, preprocessor branches that evaluate to ``false`` (and
    are therefore excluded from the final compiled shader) will appear grayed
    out. This does not apply to runtime ``if`` statements.

**#if preprocessor versus if statement: Performance caveats**

The :ref:`shading language <doc_shading_language>` supports runtime ``if`` statements:

.. code-block:: glsl

    uniform bool USE_LIGHT = true;

    if (USE_LIGHT) {
        // This part is included in the compiled shader, and always run.
    } else {
        // This part is included in the compiled shader, but never run.
    }

If the uniform is never changed, this behaves identical to the following usage
of the ``#if`` preprocessor statement:

.. code-block:: glsl

    #define USE_LIGHT

    #if defined(USE_LIGHT)
    // This part is included in the compiled shader, and always run.
    #else
    // This part is *not* included in the compiled shader (and therefore never run).
    #endif

However, the ``#if`` variant can be faster in certain scenarios. This is because
all runtime branches in a shader are still compiled and variables within
those branches may still take up register space, even if they are never run in
practice.

Modern GPUs are `quite effective <https://medium.com/@jasonbooth_86226/branching-on-a-gpu-18bfc83694f2>`__
at performing "static" branching. "Static" branching refers to ``if`` statements where
*all* pixels/vertices evaluate to the same result in a given shader invocation. However,
high amounts of :abbr:`VGPRs (Vector General-Purpose Register)` (which can be caused by
having too many branches) can still slow down shader execution significantly.

#elif
~~~~~

The ``#elif`` directive stands for "else if" and checks the condition passed if
the above ``#if`` evaluated to ``false``. ``#elif`` can only be used within an
``#if`` block. It is possible to use several ``#elif`` statements after an ``#if`` statement.

.. code-block:: glsl

    #define VAR 2

    #if VAR == 0
    // Not included.
    #elif VAR == 1
    // Not included.
    #elif VAR == 2
    // Condition is `true`. Include this portion in the final shader.
    #else
    // Not included.
    #endif

Like with ``#if``, the ``defined()`` preprocessor function can be used:

.. code-block:: glsl

    #define SHADOW_QUALITY_MEDIUM

    #if defined(SHADOW_QUALITY_HIGH)
    // High shadow quality.
    #elif defined(SHADOW_QUALITY_MEDIUM)
    // Medium shadow quality.
    #else
    // Low shadow quality.
    #endif

#ifdef
~~~~~~

**Syntax:** ``#ifdef <identifier>``

This is a shorthand for ``#if defined(...)``. Checks whether the passed
identifier is defined by ``#define`` placed above that directive. This is useful
for creating multiple shader versions in the same file. It may be continued by an
``#else`` block, but must be ended with the ``#endif`` directive.

.. code-block:: glsl

    #define USE_LIGHT

    #ifdef USE_LIGHT
    // USE_LIGHT is defined. Include this portion in the final shader.
    #endif

The processor does *not* support ``#elifdef`` as a shortcut for ``#elif defined(...)``.
Instead, use the following series of ``#ifdef`` and ``#else`` when you need more
than two branches:

.. code-block:: glsl

    #define SHADOW_QUALITY_MEDIUM

    #ifdef SHADOW_QUALITY_HIGH
    // High shadow quality.
    #else
    #ifdef SHADOW_QUALITY_MEDIUM
    // Medium shadow quality.
    #else
    // Low shadow quality.
    #endif // This ends `SHADOW_QUALITY_MEDIUM`'s branch.
    #endif // This ends `SHADOW_QUALITY_HIGH`'s branch.

#ifndef
~~~~~~~

**Syntax:** ``#ifndef <identifier>``

This is a shorthand for ``#if !defined(...)``. Similar to ``#ifdef``, but checks
whether the passed identifier is **not** defined by ``#define`` before that
directive.

This is the exact opposite of ``#ifdef``; it will always match in situations
where ``#ifdef`` would never match, and vice versa.

.. code-block:: glsl

    #define USE_LIGHT

    #ifndef USE_LIGHT
    // Evaluates to `false`. This portion won't be included in the final shader.
    #endif

    #ifndef USE_COLOR
    // Evaluates to `true`. This portion will be included in the final shader.
    #endif

#else
~~~~~

**Syntax:** ``#else``

Defines the optional block which is included when the previously defined ``#if``,
``#elif``, ``#ifdef`` or ``#ifndef`` directive evaluates to false.

.. code-block:: glsl

    shader_type spatial;

    #define MY_COLOR vec3(1.0, 0, 0)

    void fragment() {
    #ifdef MY_COLOR
        ALBEDO = MY_COLOR;
    #else
        ALBEDO = vec3(0, 0, 1.0);
    #endif
    }

#endif
~~~~~~

**Syntax:** ``#endif``

Used as terminator for the ``#if``, ``#ifdef``, ``#ifndef`` or subsequent ``#else`` directives.

#error
~~~~~~

**Syntax:** ``#error <message>``

The ``#error`` directive forces the preprocessor to emit an error with optional message.
For example, it's useful when used within ``#if`` block to provide a strict limitation of the
defined value.

.. code-block:: glsl

    #define MAX_LOD 3
    #define LOD 4

    #if LOD > MAX_LOD
    #error LOD exceeds MAX_LOD
    #endif

#include
~~~~~~~~

**Syntax:** ``#include "path"``

The ``#include`` directive includes the *entire* content of a shader include
file in a shader. ``"path"`` can be an absolute ``res://`` path or relative to
the current shader file. Relative paths are only allowed in shaders that are
saved to ``.gdshader`` or ``.gdshaderinc`` files, while absolute paths can be
used in shaders that are built into a scene/resource file.

You can create new shader includes by using the **File > Create Shader Include**
menu option of the shader editor, or by creating a new :ref:`ShaderInclude<class_ShaderInclude>` resource
in the FileSystem dock.

Shader includes can be included from within any shader, or other shader include, at
any point in the file.

When including shader includes in the global scope of a shader, it is recommended
to do this after the initial ``shader_type`` statement.

You can also include shader includes from within the body a function. Please note that
the shader editor is likely going to report errors for your shader include's code, as it
may not be valid outside of the context that it was written for. You can either choose
to ignore these errors (the shader will still compile fine), or you can wrap the include
in an ``#ifdef`` block that checks for a define from your shader.

``#include`` is useful for creating libraries of helper functions (or macros)
and reducing code duplication. When using ``#include``, be careful about naming
collisions, as redefining functions or macros is not allowed.

``#include`` is subject to several restrictions:

- Only shader include resources (ending with ``.gdshaderinc``) can be included.
  ``.gdshader`` files cannot be included by another shader, but a
  ``.gdshaderinc`` file can include other ``.gdshaderinc`` files.
- Cyclic dependencies are **not** allowed and will result in an error.
- To avoid infinite recursion, include depth is limited to 25 steps.

Example shader include file:

.. code-block:: glsl

    // fancy_color.gdshaderinc

    // While technically allowed, there is usually no `shader_type` declaration in include files.

    vec3 get_fancy_color() {
        return vec3(0.3, 0.6, 0.9);
    }

Example base shader (using the include file we created above):

.. code-block:: glsl

    // material.gdshader

    shader_type spatial;

    #include "res://fancy_color.gdshaderinc"

    void fragment() {
        // No error, as we've included a definition for `get_fancy_color()` via the shader include.
        COLOR = get_fancy_color();
    }

#pragma
~~~~~~~

**Syntax:** ``#pragma value``

The ``#pragma`` directive provides additional information to the preprocessor or compiler.

Currently, it may have only one value: ``disable_preprocessor``. If you don't need
the preprocessor, use that directive to speed up shader compilation by excluding
the preprocessor step.

.. code-block:: glsl

    #pragma disable_preprocessor

    #if USE_LIGHT
    // This causes a shader compilation error, as the `#if USE_LIGHT` and `#endif`
    // are included as-is in the final shader code.
    #endif

Built-in defines
----------------

Current renderer
~~~~~~~~~~~~~~~~

Since Godot 4.4, you can check which renderer is currently used with the built-in
defines ``CURRENT_RENDERER``, ``RENDERER_COMPATIBILITY``, ``RENDERER_MOBILE``,
and ``RENDERER_FORWARD_PLUS``:

- ``CURRENT_RENDERER`` is set to either ``0``, ``1``, or ``2`` depending on the
  current renderer.
- ``RENDERER_COMPATIBILITY`` is always ``0``.
- ``RENDERER_MOBILE`` is always ``1``.
- ``RENDERER_FORWARD_PLUS`` is always ``2``.

As an example, this shader sets ``ALBEDO`` to a different color in each renderer:

.. code-block:: glsl

    shader_type spatial;

    void fragment() {
    #if CURRENT_RENDERER == RENDERER_COMPATIBILITY
        ALBEDO = vec3(0.0, 0.0, 1.0);
    #elif CURRENT_RENDERER == RENDERER_MOBILE
        ALBEDO = vec3(1.0, 0.0, 0.0);
    #else // CURRENT_RENDERER == RENDERER_FORWARD_PLUS
        ALBEDO = vec3(0.0, 1.0, 0.0);
    #endif
    }
