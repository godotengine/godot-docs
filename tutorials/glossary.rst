.. _doc_glossary:

Glossary
========

This page contains definitions for common terms that you will see throughout the
manual. It includes many Godot-specific terms, as well as some common game 
evelopment and graphics terms that may be unfamiliar to you.

.. glossary::

    Antialiasing
        A rendering technique to make edges appear smoother. Godot supports several antialiasing techniques. See :ref:`doc_3d_antialiasing`.

    Compatibility renderer
        A fast, simple renderer for desktop and mobile that uses OpenGL. See :ref:`doc_renderers`.

    CPU
        Central processing unit. Executes code mostly in sequence, one instruction at a time. Godot uses the CPU for all processing except for rendering graphics. 

    Direct3D 12
        A modern, low-level graphics API, developed by Microsoft. 

    DOF
        Depth of field.

    Forward+ renderer
        An advanced renderer for desktop that uses modern graphics drivers. See :ref:`doc_renderers`.

    FXAA
        Fast approximate antialiasing. See :ref:`doc_3d_antialiasing_fxaa`.

    GDExtension
        A Godot-specific technology that lets the engine interact with native shared libraries at run-time. See :ref:`doc_what_is_gdextension`

    GDScript
        A high-level, object-oriented, imperative, and gradually typed programming language built for Godot. See :ref:`doc_gdscript`.

    GPU
        Graphics Processor Unit. Executes code mostly in parallel, and very fast. Godot uses the GPU for rendering graphics.

    HDR
        High dynamic range. See :ref:`doc_high_dynamic_range`.

    Linear color space
        The color space used internally by the Forward+ and Mobile renderers. See :ref:`doc_high_dynamic_range`.

    Metal
        A modern, low-level graphics API developed by Apple.

    Mobile renderer
       A renderer for mobile and desktop that uses modern graphics drivers. See :ref:`doc_renderers`.

    MSAA
        Multisample antialiasing. See :ref:`doc_3d_antialiasing_msaa`.

    OpenGL
        A cross-platform graphics API. Used by Godot for the Compatibility renderer.

    Renderer
        The rendering engine used to draw graphics. Godot has multiple renderers, with different features. See :ref:`doc_renderers`.

    Rendering method
        Another term for renderer.

    Rendering driver
        The rendering driver tells the GPU what to do, by communicating with a graphics API such as OpenGL or Vulkan.

    Shader
        A program that runs on the GPU, used to draw graphics. See :ref:`doc_introduction_to_shaders`.

    SDFGI
        Signed distance field global illumination. A kind of global illumation. See :ref:`doc_using_sdfgi`.

    SDR
        Standard dynamic range. See :ref:`doc_high_dynamic_range`.

    sRGB color space
        Standard RGB (red, green, blue). See :ref:`doc_high_dynamic_range`.

    SSAA
        Supersample antialiasing. See :ref:`doc_3d_antialiasing_ssaa`.

    SSAO
        Screen-space ambient occlusion. See :ref:`doc_environment_and_post_processing_ssao`.

    SSIL
        Screen-space indirect lighting. A kind of global illumination. See :ref`doc_environment_and_post_processing_ssil`.

    Viewport
        A view into the screen, used to render nodes. See :ref:`doc_viewports`.

    VisualShader
        A shader created using a graph-based visual editor. See :ref:`doc_visual_shaders`.

    Vulkan
        A modern, low-level, cross-platform graphics API. 
