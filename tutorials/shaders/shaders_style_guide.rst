.. _doc_shaders_style_guide:

Shaders style guide
===================

This style guide lists conventions to write elegant shaders. The goal is to
encourage writing clean, readable code and promote consistency across projects,
discussions, and tutorials. Hopefully, this will also support the development of
auto-formatting tools.

Since the Godot shader language is close to C-style languages and GLSL, this
guide is inspired by Godot's own GLSL formatting. You can view examples of
GLSL files in Godot's source code
`here <https://github.com/godotengine/godot/blob/master/drivers/gles3/shaders/>`__.

Style guides aren't meant as hard rulebooks. At times, you may not be able to
apply some of the guidelines below. When that happens, use your best judgment,
and ask fellow developers for insights.

In general, keeping your code consistent in your projects and within your team is
more important than following this guide to a tee.

.. note:: Godot's built-in shader editor uses a lot of these conventions
          by default. Let it help you.

Here is a complete shader example based on these guidelines:

.. code-block:: glsl

    shader_type canvas_item;
    // Screen-space shader to adjust a 2D scene's brightness, contrast
    // and saturation. Taken from
    // https://github.com/godotengine/godot-demo-projects/blob/master/2d/screen_space_shaders/shaders/BCS.gdshader

    uniform sampler2D screen_texture : hint_screen_texture, filter_linear_mipmap;
    uniform float brightness = 0.8;
    uniform float contrast = 1.5;
    uniform float saturation = 1.8;

    void fragment() {
        vec3 c = textureLod(screen_texture, SCREEN_UV, 0.0).rgb;

        c.rgb = mix(vec3(0.0), c.rgb, brightness);
        c.rgb = mix(vec3(0.5), c.rgb, contrast);
        c.rgb = mix(vec3(dot(vec3(1.0), c.rgb) * 0.33333), c.rgb, saturation);

        COLOR.rgb = c;
    }

Formatting
----------

Encoding and special characters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Use line feed (**LF**) characters to break lines, not CRLF or CR. *(editor default)*
* Use one line feed character at the end of each file. *(editor default)*
* Use **UTF-8** encoding without a `byte order mark <https://en.wikipedia.org/wiki/Byte_order_mark>`_. *(editor default)*
* Use **Tabs** instead of spaces for indentation. *(editor default)*

Indentation
~~~~~~~~~~~

Each indent level should be one tab greater than the block containing it.

**Good**:

.. code-block:: glsl

    void fragment() {
        COLOR = vec3(1.0, 1.0, 1.0);
    }

**Bad**:

.. code-block:: glsl

    void fragment() {
            COLOR = vec3(1.0, 1.0, 1.0);
    }

Use 2 indent levels to distinguish continuation lines from
regular code blocks.

**Good**:

.. code-block:: glsl

    vec2 st = vec2(
            atan(NORMAL.x, NORMAL.z),
            acos(NORMAL.y));

**Bad**:

.. code-block:: glsl

    vec2 st = vec2(
        atan(NORMAL.x, NORMAL.z),
        acos(NORMAL.y));


Line breaks and blank lines
~~~~~~~~~~~~~~~~~~~~~~~~~~~

For a general indentation rule, follow
`the "1TBS Style" <https://en.wikipedia.org/wiki/Indentation_style#Variant:_1TBS_(OTBS)>`_
which recommends placing the brace associated with a control statement on the
same line. Always use braces for statements, even if they only span one line.
This makes them easier to refactor and avoids mistakes when adding more lines to
an ``if`` statement or similar.

**Good**:

.. code-block:: glsl

    void fragment() {
        if (true) {
            // ...
        }
    }

**Bad**:

.. code-block:: glsl

    void fragment()
    {
        if (true)
            // ...
    }

Blank lines
~~~~~~~~~~~

Surround function definitions with one (and only one) blank line:

.. code-block:: glsl

    void do_something() {
        // ...
    }

    void fragment() {
        // ...
    }

Use one (and only one) blank line inside functions to separate logical sections.

Line length
~~~~~~~~~~~

Keep individual lines of code under 100 characters.

If you can, try to keep lines under 80 characters. This helps to read the code
on small displays and with two shaders opened side-by-side in an external text
editor. For example, when looking at a differential revision.

One statement per line
~~~~~~~~~~~~~~~~~~~~~~

Never combine multiple statements on a single line.

**Good**:

.. code-block:: glsl

    void fragment() {
        ALBEDO = vec3(1.0);
        EMISSION = vec3(1.0);
    }

**Bad**:

.. code-block:: glsl

    void fragment() {
        ALBEDO = vec3(1.0); EMISSION = vec3(1.0);
    }

The only exception to that rule is the ternary operator:

.. code-block:: glsl

   void fragment() {
        bool should_be_white = true;
        ALBEDO = should_be_white ? vec3(1.0) : vec3(0.0);
    }

Comment spacing
~~~~~~~~~~~~~~~

Regular comments should start with a space, but not code that you comment out.
This helps differentiate text comments from disabled code.

**Good**:

.. code-block:: glsl

    // This is a comment.
    //return;

**Bad**:

.. code-block:: glsl

    //This is a comment.
    // return;

Don't use multiline comment syntax if your comment can fit on a single line:

.. code-block:: glsl

    /* This is another comment. */

.. note::

   In the shader editor, to make the selected code a comment (or uncomment it),
   press :kbd:`Ctrl + K`. This feature adds or removes ``//`` at the start of
   the selected lines.

Documentation comments
~~~~~~~~~~~~~~~~~~~~~~

Use the following format for documentation comments above uniforms, with **two**
leading asterisks (``/**``) and follow-up asterisks on every line:

.. code-block:: glsl

    /**
     * This is a documentation comment.
     * These lines will appear in the inspector when hovering the shader parameter
     * named "Something".
     * You can use [b]BBCode[/b] [i]formatting[/i] in the comment.
     */
    uniform int something = 1;

These comments will appear when hovering a property in the inspector. If you
don't wish the comment to be visible in the inspector, use the standard comment
syntax instead (``// ...`` or ``/* ... */`` with only one leading asterisk).

Whitespace
~~~~~~~~~~

Always use one space around operators and after commas. Also, avoid extraneous spaces
in function calls.

**Good**:

.. code-block:: glsl

    COLOR.r = 5.0;
    COLOR.r = COLOR.g + 0.1;
    COLOR.b = some_function(1.0, 2.0);

**Bad**:

.. code-block:: glsl

    COLOR.r=5.0;
    COLOR.r = COLOR.g+0.1;
    COLOR.b = some_function (1.0,2.0);

Don't use spaces to align expressions vertically:

.. code-block:: glsl

    ALBEDO.r   = 1.0;
    EMISSION.r = 1.0;

Floating-point numbers
~~~~~~~~~~~~~~~~~~~~~~

Always specify at least one digit for both the integer and fractional part. This
makes it easier to distinguish floating-point numbers from integers, as well as
distinguishing numbers greater than 1 from those lower than 1.

**Good**:

.. code-block:: glsl

    void fragment() {
        ALBEDO.rgb = vec3(5.0, 0.1, 0.2);
    }

**Bad**:

.. code-block:: glsl

    void fragment() {
        ALBEDO.rgb = vec3(5., .1, .2);
    }

Accessing vector members
------------------------

Use ``r``, ``g``, ``b``, and ``a`` when accessing a vector's members if it
contains a color. If the vector contains anything else than a color, use ``x``,
``y``, ``z``, and ``w``. This allows those reading your code to better
understand what the underlying data represents.

**Good**:

.. code-block:: glsl

    COLOR.rgb = vec3(5.0, 0.1, 0.2);

**Bad**:

.. code-block:: glsl

    COLOR.xyz = vec3(5.0, 0.1, 0.2);

Naming conventions
------------------

These naming conventions follow the Godot Engine style. Breaking these will make
your code clash with the built-in naming conventions, leading to inconsistent
code.

Functions and variables
~~~~~~~~~~~~~~~~~~~~~~~

Use snake\_case to name functions and variables:

.. code-block:: glsl

   void some_function() {
        float some_variable = 0.5;
   }

Constants
~~~~~~~~~

Write constants with CONSTANT\_CASE, that is to say in all caps with an
underscore (\_) to separate words:

.. code-block:: glsl

    const float GOLDEN_RATIO = 1.618;

Preprocessor directives
~~~~~~~~~~~~~~~~~~~~~~~

:ref:`doc_shader_preprocessor` directives should be written in CONSTANT__CASE.
Directives should be written without any indentation before them, even if
nested within a function.

To preserve the natural flow of indentation when shader errors are printed to
the console, extra indentation should **not** be added within ``#if``,
``#ifdef`` or ``#ifndef`` blocks:

**Good**:

.. code-block:: glsl

    #define HEIGHTMAP_ENABLED

    void fragment() {
        vec2 position = vec2(1.0, 2.0);

    #ifdef HEIGHTMAP_ENABLED
        sample_heightmap(position);
    #endif
    }

**Bad**:

.. code-block:: glsl

    #define heightmap_enabled

    void fragment() {
        vec2 position = vec2(1.0, 2.0);

        #ifdef heightmap_enabled
            sample_heightmap(position);
        #endif
    }

Applying formatting automatically
---------------------------------

To automatically format shader files, you can use
`clang-format <https://clang.llvm.org/docs/ClangFormat.html>`__ on one or several
``.gdshader`` files, as the syntax is close enough to a C-style language.

However, the default style in clang-format doesn't follow this style guide,
so you need to save this file as ``.clang-format`` in your project's root folder:

.. code-block:: yaml

    BasedOnStyle: LLVM
    AlignAfterOpenBracket: DontAlign
    AlignOperands: DontAlign
    AlignTrailingComments:
    Kind: Never
    OverEmptyLines: 0
    AllowAllParametersOfDeclarationOnNextLine: false
    AllowShortFunctionsOnASingleLine: Inline
    BreakConstructorInitializers: AfterColon
    ColumnLimit: 0
    ContinuationIndentWidth: 8
    IndentCaseLabels: true
    IndentWidth: 4
    InsertBraces: true
    KeepEmptyLinesAtTheStartOfBlocks: false
    RemoveSemicolon: true
    SpacesInLineCommentPrefix:
    Minimum: 0 # We want a minimum of 1 for comments, but allow 0 for disabled code.
    Maximum: -1
    TabWidth: 4
    UseTab: Always

While in the project root, you can then call ``clang-format -i path/to/shader.gdshader``
in a terminal to format a single shader file, or ``clang-format -i path/to/folder/*.gdshader``
to format all shaders in a folder.

Code order
----------

We suggest to organize shader code this way:

.. code-block:: glsl

    01. shader type declaration
    02. render mode declaration
    03. // docstring

    04. uniforms
    05. constants
    06. varyings

    07. other functions
    08. vertex() function
    09. fragment() function
    10. light() function

We optimized the order to make it easy to read the code from top to bottom, to
help developers reading the code for the first time understand how it works, and
to avoid errors linked to the order of variable declarations.

This code order follows two rules of thumb:

1. Metadata and properties first, followed by methods.
2. "Public" comes before "private". In a shader language's context, "public"
   refers to what's easily adjustable by the user (uniforms).

Local variables
~~~~~~~~~~~~~~~

Declare local variables as close as possible to their first use. This makes it
easier to follow the code, without having to scroll too much to find where the
variable was declared.
