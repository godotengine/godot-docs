.. _doc_list_of_features:

List of features
================

This page aims to list all features currently supported by Godot.

.. note::

    This page lists features supported by the current development version of
    Godot (4.0.dev). Some of these features may not be available in the current
    stable release series (3.2).

Features
--------

Platforms
^^^^^^^^^

**Can run both the editor and exported projects:**

- Windows 7 and later (64-bit and 32-bit).
- macOS 10.12 and later (64-bit, x86 and ARM).
- Linux (64-bit, x86 and ARM).
   - Binaries are statically linked and can run on any distribution if compiled
     on an old enough base distribution.
   - Official binaries are compiled on Ubuntu 14.04.
   - 32-bit binaries can be compiled from source.

**Runs exported projects:**

- Android 4.4 and later.
- iOS 10.0 and later.
- HTML5 via WebAssembly (Firefox, Chrome, Edge, Opera).
- :ref:`Consoles <doc_consoles>`.

Godot aims to be as platform-independent as possible and can be ported to new
platforms with relative ease.

Editor
^^^^^^

**Features:**

- Scene tree editor.
- Script editor.
- Support for :ref:`external script editors <doc_external_editor>` such as
  Visual Studio Code or Vim.
- GDScript :ref:`debugger <doc_debugger_panel>`.
   - No support for debugging in threads yet.
- Visual profiler with CPU and GPU time indications.
- Performance monitoring tools.
- Live script reloading.
- Live scene editing.
   - Changes will reflect in the editor and will be kept after closing the running project.
- Remote inspector.
   - Changes won't reflect in the editor and won't be kept after closing the running project.
- Live camera replication.
   - Move the in-editor camera and see the result in the running project.
- Use the editor in dozens of languages contributed by the community.

**Plugins:**

- Editor plugins can be downloaded from the
  :ref:`asset library <doc_what_is_assetlib>` to extend editor functionality.
- Create your own plugins using GDScript to add new features or speed up your workflow.
- Download projects from the asset library in the project manager and import them directly.

2D graphics
^^^^^^^^^^^

Vulkan renderer.

- Sprite, polygon and line rendering.
   - High-level tools to draw lines and polygons such as Polygon2D and Line2D.
- AnimatedSprite as a helper for creating animated sprites.
- Parallax layers.
   - Pseudo-3D support by automatically duplicating a layer several times.
- 2D lighting with normal maps and specular maps.
   - Hard or soft shadows.
- Font rendering using bitmaps (BitmapFont) or rasterization using FreeType (DynamicFont).
   - Bitmap fonts can be exported using tools like BMFont.
   - DynamicFont supports monochrome fonts as well as colored fonts.
     Supported formats are TTF and OTF.
   - DynamicFont supports optional font outlines with adjustable width and color.
   - Support for font oversampling to keep fonts sharp at higher resolutions.
- GPU-based particles with support for custom particle shaders.
- CPU-based particles.

2D tools
^^^^^^^^

- 2D camera with built-in smoothing and drag margins.
- Path2D node to represent a path in 2D space.
   - Can be drawn in the editor or generated procedurally.
   - PathFollow2D node to make nodes follow a Path2D.
- 2D geometry helper class.
- Line2D node to draw textured 2D lines.

2D physics
^^^^^^^^^^

**Physics bodies:**

- Static bodies.
- Rigid bodies.
- Kinematic bodies.
- Joints.
- Areas to detect bodies entering or leaving it.

**Collision detection:**

- Built-in shapes: line, box, circle, capsule.
- Collision polygons (can be drawn manually or generated from a sprite in the editor).

3D graphics
^^^^^^^^^^^

Vulkan renderer.

- HDR rendering with sRGB.
- Perspective, orthographic and frustum-offset cameras.

**Physically-based rendering:**

- Follows the Disney PBR model.
- Uses a roughness-metallic workflow with support for ORM textures.
- Normal mapping.
- Parallax/relief mapping with automatic level of detail based on distance.
- Sub-surface scattering and transmittance.
- Proximity fade (soft particles) and distance fade.
- Distance fade can use alpha blending or dithering to avoid going through
  the transparent pipeline.
- Dithering can be determined on a per-pixel or per-object basis.

**Real-time lighting:**

- Directional lights (sun/moon). Up to 4 per scene.
- Omnidirectional lights.
- Spot lights with adjustable cone angle and attenuation.
- Adjustable light "size" for fake area lights (will also make shadows blurrier).
- Lights are rendered with clustered forward optimizations to decrease their
  individual cost.

**Shadow mapping:**

- *DirectionalLight:* Orthogonal (fastest), PSSM 2-split and 4-split.
  Supports blending between splits.
- *OmniLight:* Dual parabolid (fast) or cubemap (slower but more accurate).
  Supports colored projector textures in the form of panoramas.
- *SpotLight:* Single texture. Supports colored projector textures.
- Shadow pancaking to decrease the amount of visible shadow acne and peter-panning.
- PCSS-like shadow blur based on the light size and distance from the surface
  the shadow is casted on.
- Adjustable blur on a per-light basis.

**Global illumination with indirect lighting:**

- Baked lightmaps (fast, but can't be updated at run-time).
   - Lightmaps are baked on the GPU using compute shaders.
- GI probes (slower, fully real-time). Supports reflections.
- Signed distance field GI (intermediate, supports dynamic lights but not
  dynamic occluders). Supports reflections.
- Global illumination uses a deferred pass to allow for adaptive subsampling.

**Reflections:**

- Voxel-based reflections (when using GI probes) and SDF-based reflections (when using signed distance field GI).
- Fast baked reflections or slow real-time reflections using ReflectionProbe.
  Parallax correction can optionally be enabled.
- Screen-space reflections.
- Reflection techniques can be mixed together for greater accuracy.

**Sky:**

- Panorama sky (using an HDRI).
- Procedural sky and Physically-based sky that respond to the DirectionalLights in the scene.
- Support for custom sky shaders.
- Radiance can be updated in real-time depending on the quality settings chosen.

**Fog:**

- Depth fog (exponential or with custom attenuation).
- Height fog (floor or ceiling) with adjustable attenuation.
- Support for automatic depth fog color depending on the camera direction
  (to match the sun color).
- Optional transmittance to make lights more visible in the fog.

**Particles:**

- GPU-based particles with support for custom particle shaders.
- CPU-based particles.

**Post-processing:**

- Tonemapping (Linear, Reinhard, Filmic, ACES).
- Automatic exposure adjustments based on viewport brightness.
- Near and far depth of field with adjustable bokeh simulation.
- Screen-space ambient occlusion at half or full resolution.
- Glow/bloom with optional bicubic upscaling and several blend modes available:
  Screen, Soft Light, Add, Replace, Mix.
- Color correction using an one-dimensional ramp.
- Roughness limiter to reduce the impact of specular aliasing.
- Brightness, contrast and saturation adjustments.

**Texture filtering:**

- Nearest, bilinear, trilinear or anisotropic filtering.
- Filtering options are defined on a per-use basis, not a per-texture basis.

**Texture compression:**

- Basis Universal (slow, but results in smaller files).
- BPTC for high-quality compression (not supported on macOS).
- ETC2 (not supported on macOS).
- S3TC (not supported on mobile/Web platforms).

**Anti-aliasing:**

- Fast approximate antialiasing (FXAA).
- Multi-sample antialiasing (MSAA).

Most of these effects can be adjusted for better performance or to further
improve quality. This can be helpful when using Godot for offline rendering.

3D tools
^^^^^^^^

- Built-in meshes: cube, cylinder/cone, (hemi)sphere, prism, plane, quad.
- Tools for :ref:`procedural geometry generation <doc_procedural_geometry>`.
- :ref:`Constructive solid geometry <doc_csg_tools>` (intended for prototyping).
- Path3D node to represent a path in 3D space.
   - Can be drawn in the editor or generated procedurally.
   - PathFollow3D node to make nodes follow a Path3D.
- 3D geometry helper class.

3D physics
^^^^^^^^^^

**Physics bodies:**

- Static bodies.
- Rigid bodies.
- Kinematic bodies.
- Vehicle bodies (intended for arcade physics, not simulation).
- Joints.
- Soft bodies.
- Ragdolls.
- Areas to detect bodies entering or leaving it.

**Collision detection:**

- Built-in shapes: cuboid, sphere, capsule, cylinder (only with Bullet physics).
- Generate triangle collision shapes for any mesh from the editor.
- Generate one or several convex collision shapes for any mesh from the editor.

Shaders
^^^^^^^

- *2D:* Custom vertex, fragment, and light shaders.
- *3D:* Custom vertex, fragment, light, and sky shaders.
- Text-based shaders using a `shader language inspired by GLSL <doc_shading_language>`.
- Visual shader editor.
   - Support for visual shader plugins.

Scripting
^^^^^^^^^

**General:**

- Object-oriented design pattern with scripts extending nodes.
- Signals and groups for communicating between scripts.
- Support for :ref:`cross-language scripting <doc_cross_language_scripting>`.
- Many 2D and 3D linear algebra data types such as vectors and transforms.

:ref:`GDScript: <toc-learn-scripting-gdscript>`

- :ref:`High-level interpreted language <doc_gdscript>` with
  :ref:`optional static typing <doc_gdscript_static_typing>`.
- Syntax inspired by Python.
- Syntax highlighting is provided on GitHub.
- :ref:`Use threads <doc_using_multiple_threads>` to perform asynchronous actions
  or make use of multiple processor cores.

:ref:`C#: <toc-learn-scripting-C#>`

- Packaged in a separate binary to keep file sizes and dependencies down.
- Uses Mono 6.x.
   - Full support for the C# 8.0 syntax and features.
- Supports all platforms.
- Using an external editor is recommended to benefit from IDE functionality.

:ref:`VisualScript: <toc-learn-scripting-visual_script>`

- :ref:`Graph-based visual scripting language <doc_what_is_visual_script>`.
- Works best when used for specific purposes (such as level-specific logic)
  rather than as a language to create entire projects.

**GDNative (C, C++, Rust, D, ...):**

- When you need it, link to native libraries for higher performance and third-party integrations.
   - For scripting game logic, GDScript or C# are recommended if their
     performance is suitable.
- Official bindings for C and C++.
   - Use any build system and language features you wish.
- Maintained D, Kotlin, Python, Nim, and Rust bindings provided by the community.

Audio
^^^^^

**Features:**

- Mono, stereo, 5.1 and 7.1 output.
- Non-positional and positional playback in 2D and 3D.
   - Optional Doppler effect in 2D and 3D.
- Support for re-routable :ref:`audio buses <doc_audio_buses>` and effects.
   - Dozens of effects included.
- Listener3D node to listen from a position different than the camera in 3D.
- Audio input to record microphones.
- MIDI input.
   - No support for MIDI output yet.

**APIs used:**

- *Windows:* WASAPI.
- *macOS:* CoreAudio.
- *Linux:* PulseAudio or ALSA.

Import
^^^^^^

- Support for :ref:`custom import plugins <doc_import_plugins>`.

**Formats:**

- *Images:* See :ref:`doc_importing_images_supported_formats`.
- *Audio:*
   - WAV with optional IMA-ADPCM compression.
   - Ogg Vorbis.
- *3D scenes:*
   - glTF 2.0 *(recommended)*.
   - `ESCN <https://github.com/godotengine/godot-blender-exporter>`__
     (direct export from Blender).
   - FBX.
   - Collada (.dae).
   - Wavefront OBJ (static scenes only, can be loaded directly as a mesh).

Input
^^^^^

- Input mapping system using hardcoded input events or remappable input actions.
   - Axis values can be mapped to two different actions with a configurable deadzone.
   - Use the same code to support both keyboards and gamepads.
- Keyboard input.
   - Keys can be mapped in "physical" mode to be independent of the keyboard layout.
- Mouse input.
   - The mouse cursor can be visible, hidden, captured or confined within the window.
   - When captured, raw input will be used on Windows and Linux to
     sidestep the OS' mouse acceleration settings.
- Gamepad input (up to 8 simulatenous controllers).
- Pen/tablet input with pressure support.

Navigation
^^^^^^^^^^

- A* algorithm in 2D and 3D.
- Navigation meshes with dynamic obstacle avoidance.
- Generate navigation meshes from the editor.

Networking
^^^^^^^^^^

- Low-level TCP networking using StreamPeer and TCP_Server.
- Low-level UDP networking using PacketPeer and UDPServer.
- Low-level HTTP requests using HTTPClient.
- High-level HTTP requests using HTTPRequest.
   - Supports HTTPS out of the box using bundled certificates.
- High-level multiplayer API using UDP and ENet.
   - Automatic replication using remote procedure calls (RPCs).
   - Supports unreliable, reliable and ordered transfers.
- WebSocket client and server, available on all platforms.
- WebRTC client and server, available on all platforms.
- Support for UPnP to sidestep the requirement to forward ports when hosting
  a server behind a NAT.

Internationalization
^^^^^^^^^^^^^^^^^^^^

- Full support for Unicode including emoji.
- Store localization strings using :ref:`CSV <doc_internationalizing_games>`
  or :ref:`gettext <doc_localization_using_gettext>`.
- Use localized strings in your project automatically in GUI elements or by
  using the ``tr()`` function.
- Support for right-to-left typesetting and text shaping planned in Godot 4.0.

Windowing and OS integration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Move, resize, minimize, and maximize windows spawned by the project.
- Change the window title and icon.
- Request attention (will cause the title bar to blink on most platforms).
- Fullscreen mode.
   - Doesn't use exclusive fullscreen, so the screen resolution can't be changed this way.
     Use a Viewport with a different resolution instead.
- Borderless windows (fullscreen or non-fullscreen).
- Ability to keep a window always on top.
- Transparent windows with per-pixel transparency.
- Global menu integration on macOS.
- Execute commands in a blocking or non-blocking manner.
- Open file paths and URLs using default or custom protocol handlers (if registered on the system).
- Parse custom command line arguments.

Mobile
^^^^^^

- In-app purchases on Android and iOS.
- Support for advertisements using third-party modules.

XR support (AR and VR)
^^^^^^^^^^^^^^^^^^^^^^

- Support for ARKit on iOS out of the box.
- Support for the OpenXR and OpenVR APIs.
- Popular VR headsets like the Oculus Quest and HTC Vive are supported thanks to plugins.

GUI system
^^^^^^^^^^

Godot's GUI is built using the same Control nodes used to make games in Godot.
The editor UI can easily be extended in many ways using add-ons.

**Nodes:**

- Buttons.
- Checkboxes, check buttons, radio buttons.
- Text entry using LineEdit (single line) and TextEdit (multiple lines).
- Dropdown menus using PopupMenu and OptionButton.
- Scrollbars.
- Labels.
- RichTextLabel for :ref:`text formatted using BBCode <doc_bbcode_in_richtextlabel>`.
- Trees (can also be used to represent tables).
- Containers (horizontal, vertical, grid, center, margin, draggable splitter, ...).
- Controls can be rotated and scaled.

**Sizing:**

- Anchors to keep GUI elements in a specific corner, edge or centered.
- Containers to place GUI elements automatically following certain rules.
   - :ref:`Stack <class_BoxContainer>` layouts.
   - :ref:`Grid <class_GridContainer>` layouts.
   - :ref:`Margin <class_MarginContainer>` and :ref:`centered <class_CenterContainer>`
     layouts.
   - :ref:`Draggable splitter <class_SplitContainer>` layouts.
- Scale to multiple resolutions using the ``2d`` or ``viewport`` stretch modes.
- Support any aspect ratio using anchors and the ``expand`` stretch aspect.

**Theming:**

- Built-in theme editor.
   - Generate a theme based on the current editor theme settings.
- Procedural vector-based theming using :ref:`class_StyleBoxFlat`.
   - Supports rounded/beveled corners, drop shadows and per-border widths.
- Texture-based theming using :ref:`class_StyleBoxTexture`.

Godot's small distribution size can make it a suitable alternative to frameworks
like Electron or Qt.

Animation
^^^^^^^^^

- Direct kinematics and inverse kinematics.
- Support for animating any property with customizable interpolation.
- Support for calling methods in animation tracks.
- Support for playing sounds in animation tracks.
- Support for Bézier curves in animation.

Formats
^^^^^^^

- Scenes and resources can be saved in :ref:`text-based <doc_tscn_file_format>` or binary formats.
   - Text-based formats are human-readable and more friendly to version control.
   - Binary formats are faster to save/load for large scenes/resources.
- Read and write text or binary files using :ref:`class_File`.
   - Can optionally be compressed or encrypted.
- Read and write :ref:`class_JSON` files.
- Read and write INI-style configuration files using :ref:`class_ConfigFile`.
   - Can (de)serialize any Godot datatype, including Vector, Color, ...
- Read XML files using :ref:`class_XMLParser`.
- Pack game data into a PCK file (custom format optimized for fast seeking),
  into a ZIP archive, or directly into the executable for single-file distribution.
- :ref:`Export additional PCK files<doc_exporting_pcks>` that can be read
  by the engine to support mods and DLCs.

Miscellaneous
^^^^^^^^^^^^^

- :ref:`Low-level access to servers <doc_using_servers>` which allows bypassing
  the scene tree's overhead when needed.
- Command line interface for automation.
   - Export and deploy projects using continuous integration platforms.
   - `Completion scripts <https://github.com/godotengine/godot/tree/master/misc/dist/shell>`__
     are available for Bash, zsh and fish.
- Support for :ref:`C++ modules <doc_custom_modules_in_c++>` statically linked
  into the engine binary.
- Engine and editor written in C++17.
   - Can be :ref:`compiled <doc_introduction_to_the_buildsystem>` using GCC,
     Clang and MSVC. MinGW is also supported.
   - Friendly towards packagers: in most cases, system libraries can be used
     instead of the ones provided by Godot. The build system doesn't download anything.
     Builds can be fully reproducible.
- Licensed under the permissive MIT license.
   - Open developement process with :ref:`contributions welcome <doc_ways_to_contribute>`.

.. seealso::

    The `roadmap <https://github.com/godotengine/godot-roadmap>`__ repository
    documents features that have been agreed upon and may be implemented in
    future Godot releases.
