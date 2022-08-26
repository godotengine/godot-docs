.. _doc_list_of_features:

List of features
================

This page aims to list all features currently supported by Godot.

.. note::

    This page lists features supported by the current development version of
    Godot (4.0.alpha). Some of these features may not be available in the
    `current stable release series (3.x) <https://docs.godotengine.org/en/stable/about/list_of_features.html>`__.

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
- :ref:`Consoles <doc_consoles>`.

Godot aims to be as platform-independent as possible and can be ported to new
platforms with relative ease.

Editor
^^^^^^

**Features:**

- Scene tree editor.
- Built-in script editor.
- Support for :ref:`external script editors <doc_external_editor>` such as
  Visual Studio Code or Vim.
- GDScript :ref:`debugger <doc_debugger_panel>`.

   - No support for debugging in threads yet.
- Visual profiler with CPU and GPU time indications for each step of the
  rendering pipeline.
- Performance monitoring tools.
- Live script reloading.
- Live scene editing.

   - Changes will reflect in the editor and will be kept after closing the running project.

- Remote inspector.

   - Changes won't reflect in the editor and won't be kept after closing the running project.

- Live camera replication.

   - Move the in-editor camera and see the result in the running project.

- Built-in offline class reference documentation.
- Use the editor in dozens of languages contributed by the community.

**Plugins:**

- Editor plugins can be downloaded from the
  :ref:`asset library <doc_what_is_assetlib>` to extend editor functionality.
- :ref:`Create your own plugins <doc_making_plugins>` using GDScript to add new
  features or speed up your workflow.
- :ref:`Download projects from the asset library <doc_using_assetlib_editor>`
  in the project manager and import them directly.

2D graphics
^^^^^^^^^^^

Vulkan renderer.

- Sprite, polygon and line rendering.

   - High-level tools to draw lines and polygons such as Polygon2D and Line2D.

- AnimatedSprite2D as a helper for creating animated sprites.
- Parallax layers.

   - Pseudo-3D support including preview in the editor.

- 2D lighting with normal maps and specular maps.

   - Point (omni/spot) and directional 2D lights.
   - Hard or soft shadows (adjustable on a per-light basis).
   - Custom shaders can access a real-time :abbr:`SDF (Signed Distance Field)`
     representation of the 2D scene, which can be used for improved 2D lighting
     effects including 2D global illumination.

- Font rendering using bitmaps, rasterization using FreeType or
  multi-channel signed distance fields (MSDF).

   - Bitmap fonts can be exported using tools like BMFont.
   - Dynamic fonts support monochrome fonts as well as colored fonts (e.g. for emoji).
     Supported formats are TTF, OTF, WOFF1 and WOFF2.
   - Dynamic fonts support optional font outlines with adjustable width and color.
   - Dynamic fonts support variable fonts and OpenType features including ligatures.
   - Dynamic fonts support simulated bold and italic when the font file lacks
     those styles.
   - Dynamic fonts support oversampling to keep fonts sharp at higher resolutions.
   - Dynamic fonts support subpixel positioning to make fonts crisper at low sizes.
   - Signed distance field fonts can be scaled at any resolution without
     requiring re-rasterization. Multi-channel usage makes SDF fonts scale down
     to lower sizes better compared to monochrome SDF fonts.

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

Vulkan renderer compatible with desktop and mobile platforms. Requires full support for
Vulkan 1.0, with Vulkan 1.1 and 1.2 features optionally used.

- HDR rendering with sRGB.
- Perspective, orthographic and frustum-offset cameras.
- When using the Vulkan Clustered backend (default on desktop), a depth prepass
  is used to improve performance in complex scenes by reducing the cost of overdraw.
- Support for rendering 3D at a lower resolution while keeping 2D rendering at
  the original scale. This can be used to improve performance on low-end systems
  or improve visuals on high-end systems.

  - 3D rendering can be scaled with bilinear filtering or
    `AMD FidelityFX Super Resolution 1.0 <https://www.amd.com/en/technologies/fidelityfx-super-resolution>`__.

- `OpenGL support planned for a future Godot 4.x release <https://godotengine.org/article/about-godot4-vulkan-gles3-and-gles2>`__.

  - If you need OpenGL support, use Godot 3.x which remains supported.

**Physically-based rendering (built-in material features):**

- Follows the Disney PBR model.
- Supports Lambert, Lambert Wrap (half-Lambert) and Toon diffuse shading modes.
- Supports Schlick-GGX, Toon and Disabled specular shading modes.
- Uses a roughness-metallic workflow with support for ORM textures.
- Uses horizon specular occlusion (Filament model) to improve material appearance.
- Normal mapping.
- Parallax/relief mapping with automatic level of detail based on distance.
- Detail mapping for the albedo and normal maps.
- Sub-surface scattering and transmittance.
- Refraction with support for material roughness (resulting in blurry refraction).
- Proximity fade (soft particles) and distance fade.
- Distance fade can use alpha blending or dithering to avoid going through
  the transparent pipeline.
- Dithering can be determined on a per-pixel or per-object basis.

**Real-time lighting:**

- Directional lights (sun/moon). Up to 4 per scene.
- Omnidirectional lights.
- Spot lights with adjustable cone angle and attenuation.
- Specular energy can be adjusted on a per-light basis.
- Adjustable light "size" for fake area lights (will also make shadows blurrier).
- Optional distance fade system to fade distant lights and their shadows, improving performance.
- When using the Vulkan Clustered backend (default on desktop), lights are
  rendered with clustered forward optimizations to decrease their individual cost.
  Clustered rendering also lifts any limits on the number of lights that can be used on a mesh.
- When using the Vulkan Mobile backend, up to 8 omni lights and 8 spot lights can
  be displayed per mesh resource. Baked lighting can be used to overcome this limit
  if needed.

**Shadow mapping:**

- *DirectionalLight:* Orthogonal (fastest), PSSM 2-split and 4-split.
  Supports blending between splits.
- *OmniLight:* Dual paraboloid (fast) or cubemap (slower but more accurate).
  Supports colored projector textures in the form of panoramas.
- *SpotLight:* Single texture. Supports colored projector textures.
- Shadow normal offset bias and shadow pancaking to decrease the amount of
  visible shadow acne and peter-panning.
- PCSS-like shadow blur based on the light size and distance from the surface
  the shadow is cast on.
- Adjustable shadow blur on a per-light basis.

**Global illumination with indirect lighting:**

- Baked lightmaps (fast, but can't be updated at run-time).

   - Supports baking indirect light only or baking both direct and indirect lighting.
     The bake mode can be adjusted on a per-light basis to allow for hybrid light
     baking setups.
   - Supports lighting dynamic objects using automatic and manually placed probes.
   - Optionally supports directional lighting and rough reflections based on spherical
     harmonics.
   - Lightmaps are baked on the GPU using compute shaders (much faster compared
     to CPU lightmapping). Baking can only be performed from the editor,
     not in exported projects.

- Voxel-based GI probes. Supports dynamic lights *and* dynamic occluders, while
  also supporting reflections. Requires a fast baking step which can be
  performed in the editor or at run-time (including from an exported project).
- Signed-distance field GI designed for large open worlds.
  Supports dynamic lights, but not dynamic occluders. Supports reflections.
  No baking required.
- Screen-space indirect lighting (SSIL) at half or full resolution.
  Fully real-time and supports any kind of emissive light source (including decals).
- VoxelGI and SDFGI use a deferred pass to allow for rendering GI at half
  resolution to improve performance (while still having working MSAA support).

**Reflections:**

- Voxel-based reflections (when using GI probes) and SDF-based reflections
  (when using signed distance field GI).
- Fast baked reflections or slow real-time reflections using ReflectionProbe.
  Parallax box correction can optionally be enabled.
- Screen-space reflections with support for material roughness.
- Reflection techniques can be mixed together for greater accuracy or scalability.
- When using the Vulkan Clustered backend (default on desktop), reflection probes are
  rendered with clustered forward optimizations to decrease their individual cost.
  Clustered rendering also lifts any limits on the number of reflection probes that can be used on a mesh.
- When using the Vulkan Mobile backend, up to 8 reflection probes can be displayed per mesh
  resource.

**Decals:**

- Supports albedo, emissive, :abbr:`ORM (Occlusion Roughness Metallic)` and normal mapping.
- Texture channels are smoothly overlaid on top of the underlying material,
  with support for normal/ORM-only decals.
- Support for normal fade to fade the decal depending on its incidence angle.
- Does not rely on run-time mesh generation. This means decals can be used on
  complex skinned meshes with no performance penalty, even if the decal moves every frame.
- Support for nearest, bilinear, trilinear or anisotropic texture filtering (configured globally).
- Optional distance fade system to fade distant lights and their shadows, improving performance.
- When using the Vulkan Clustered backend (default on desktop), decals are
  rendered with clustered forward optimizations to decrease their individual cost.
  Clustered rendering also lifts any limits on the number of decals that can be used on a mesh.
- When using the Vulkan Mobile backend, up to 8 decals can be displayed per mesh
  resource.

**Sky:**

- Panorama sky (using an HDRI).
- Procedural sky and Physically-based sky that respond to the DirectionalLights in the scene.
- Support for custom sky shaders, which can be animated.
- The radiance map used for ambient and specular light can be updated in
  real-time depending on the quality settings chosen.

**Fog:**

- Exponential depth fog.
- Exponential height fog.
- Support for automatic fog color depending on the sky color (aerial perspective).
- Support for sun scattering in the fog.

**Volumetric fog:**

- Global volumetric fog that reacts to lights and shadows.
- Volumetric fog can take indirect light into account when using VoxelGI or SDFGI.
- Fog volume nodes that can be placed to add fog to specific areas (or remove fog from specific areas).
- Each fog volume can have its own custom shader.
- Can be used together with traditional fog.

**Particles:**

- GPU-based particles with support for subemitters (2D + 3D), trails (2D + 3D),
  attractors (3D only) and collision (3D only).

  - Particle attractor shapes supported: box, sphere and 3D vector fields.
  - Particle collision shapes supported: box, sphere, baked signed distance field
    and real-time heightmap (suited for open world weather effects).
  - Trails can use the built-in ribbon trail and tube trail meshes, or custom
    meshes with skeletons.
  - Support for custom particle shaders with manual emission.

- CPU-based particles.

**Post-processing:**

- Tonemapping (Linear, Reinhard, Filmic, ACES).
- Automatic exposure adjustments based on viewport brightness (and manual exposure override).
- Near and far depth of field with adjustable bokeh simulation (box, hexagon, circle).
- Screen-space ambient occlusion (SSAO) at half or full resolution.
- Glow/bloom with optional bicubic upscaling and several blend modes available:
  Screen, Soft Light, Add, Replace, Mix.
- Glow can have a colored dirt map texture, acting as a lens dirt effect.
- Color correction using a one-dimensional ramp or a 3D LUT texture.
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
- Super-sample antialiasing (SSAA) using bilinear 3D scaling and a 3D resolution scale above 1.0.
- Alpha antialiasing, alpha to coverage and alpha hashing on a per-material basis.

Most of these effects can be adjusted for better performance or to further
improve quality. This can be helpful when using Godot for offline rendering.

3D tools
^^^^^^^^

- Built-in meshes: cube, cylinder/cone, (hemi)sphere, prism, plane, quad, ribbon, tube.
- Tools for :ref:`procedural geometry generation <doc_procedural_geometry>`.
- :ref:`Constructive solid geometry <doc_csg_tools>` (intended for prototyping).
- Path3D node to represent a path in 3D space.

   - Can be drawn in the editor or generated procedurally.
   - PathFollow3D node to make nodes follow a Path3D.

- 3D geometry helper class.
- Support for exporting the current scene as a glTF 2.0 file, both from the editor
  and at run-time from an exported project.

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

- Built-in shapes: cuboid, sphere, capsule, cylinder.
- Generate triangle collision shapes for any mesh from the editor.
- Generate one or several convex collision shapes for any mesh from the editor.

Shaders
^^^^^^^

- *2D:* Custom vertex, fragment, and light shaders.
- *3D:* Custom vertex, fragment, light, and sky shaders.
- Text-based shaders using a :ref:`shader language inspired by GLSL <doc_shading_language>`.
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
- Syntax inspired by Python. However, GDScript is **not** based on Python.
- Syntax highlighting is provided on GitHub.
- :ref:`Use threads <doc_using_multiple_threads>` to perform asynchronous actions
  or make use of multiple processor cores.

:ref:`C#: <toc-learn-scripting-C#>`

- Packaged in a separate binary to keep file sizes and dependencies down.
- Uses Mono 6.x.

   - Full support for the C# 8.0 syntax and features.

- Supports all platforms.
- Using an external editor is recommended to benefit from IDE functionality.

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

- Support for re-routable :ref:`audio buses <doc_audio_buses>` and effects
  with dozens of effects included.
- Support for polyphony (playing several sounds from a single AudioStreamPlayer node).
- Support for real-time pitch scaling and random pitch.
- Support for sequential/random sample selection, including repetition prevention
  when using random sample selection.
- Listener2D and Listener3D nodes to listen from a position different than the camera.
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

- *Images:* See :ref:`doc_import_images`.
- *Audio:*

   - WAV with optional IMA-ADPCM compression.
   - Ogg Vorbis.
   - MP3.

- *3D scenes:*

   - glTF 2.0 *(recommended)*.
   - `ESCN <https://github.com/godotengine/godot-blender-exporter>`__
     (direct export from Blender).
   - FBX (static meshes only).
   - Collada (.dae).
   - Wavefront OBJ (static scenes only, can be loaded directly as a mesh).

- Support for loading glTF 2.0 scenes at run-time, including from an exported project.
- 3D meshes use `Mikktspace <http://www.mikktspace.com/>`__ to generate tangents
  on import, which ensures consistency with other 3D applications such as Blender.

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

- Gamepad input (up to 8 simultaneous controllers).
- Pen/tablet input with pressure support.

Navigation
^^^^^^^^^^

- A* algorithm in 2D and 3D.
- Navigation meshes with dynamic obstacle avoidance.
- Generate navigation meshes from the editor or at run-time (including from an exported project).

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

  - Support for generating gettext POT and PO files from the editor.

- Use localized strings in your project automatically in GUI elements or by
  using the ``tr()`` function.
- Support for pluralization and translation contexts when using gettext translations.
- Support for bidirectional typesetting, text shaping and OpenType localized forms.
- Automatic UI mirroring for right-to-left locales.
- Support for pseudolocalization to test your project for i18n-friendliness.

Windowing and OS integration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Move, resize, minimize, and maximize windows spawned by the project.
- Change the window title and icon.
- Request attention (will cause the title bar to blink on most platforms).
- Fullscreen mode.

   - Doesn't use exclusive fullscreen, which allows for fast alt-tabbing. The
     downside is that the screen resolution can't be changed this way. For 3D
     resolution scaling, use the appropriate project settings or the equivalent
     Viewport property. For 2D resolution scaling, use a second Viewport node
     to render the game world with a different size.

- Borderless windows (fullscreen or non-fullscreen).
- Ability to keep a window always on top.
- Global menu integration on macOS.
- Execute commands in a blocking or non-blocking manner.
- Open file paths and URLs using default or custom protocol handlers (if registered on the system).
- Parse custom command line arguments.
- Any Godot binary (editor or exported project) can be
  :ref:`used as a headless server <doc_exporting_for_dedicated_servers>`
  by starting it with the ``--headless`` command line argument.
  This allows running the engine without a GPU or display server.

Mobile
^^^^^^

- In-app purchases on Android and iOS.
- Support for advertisements using third-party modules.

XR support (AR and VR)
^^^^^^^^^^^^^^^^^^^^^^

- Out of the box support for OpenXR.

   - Including support for popular headsets like the Meta Quest and the Valve Index.

- Support for ARKit on iOS out of the box.
- Support for the OpenVR APIs.

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
- Color picker with RGB and HSV modes.
- Containers (horizontal, vertical, grid, flow, center, margin, aspect ratio, draggable splitter, ...).
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

   - Supports rounded/beveled corners, drop shadows, per-border widths and antialiasing.

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

File formats
^^^^^^^^^^^^

- Scenes and resources can be saved in :ref:`text-based <doc_tscn_file_format>` or binary formats.

   - Text-based formats are human-readable and more friendly to version control.
   - Binary formats are faster to save/load for large scenes/resources.

- Read and write text or binary files using :ref:`class_File`.

   - Can optionally be compressed or encrypted.

- Read and write :ref:`class_JSON` files.
- Read and write INI-style configuration files using :ref:`class_ConfigFile`.

   - Can (de)serialize any Godot datatype, including Vector2/3, Color, ...

- Read XML files using :ref:`class_XMLParser`.
- Pack game data into a PCK file (custom format optimized for fast seeking),
  into a ZIP archive, or directly into the executable for single-file distribution.
- :ref:`Export additional PCK files<doc_exporting_pcks>` that can be read
  by the engine to support mods and DLCs.

Miscellaneous
^^^^^^^^^^^^^

- :ref:`Low-level access to servers <doc_using_servers>` which allows bypassing
  the scene tree's overhead when needed.
- :ref:`Command line interface <doc_command_line_tutorial>` for automation.

   - Export and deploy projects using continuous integration platforms.
   - `Shell completion scripts <https://github.com/godotengine/godot/tree/master/misc/dist/shell>`__
     are available for Bash, zsh and fish.

- Support for :ref:`C++ modules <doc_custom_modules_in_c++>` statically linked
  into the engine binary.
- Engine and editor written in C++17.

   - Can be :ref:`compiled <doc_introduction_to_the_buildsystem>` using GCC,
     Clang and MSVC. MinGW is also supported.
   - Friendly towards packagers. In most cases, system libraries can be used
     instead of the ones provided by Godot. The build system doesn't download anything.
     Builds can be fully reproducible.

- Licensed under the permissive MIT license.

   - Open development process with :ref:`contributions welcome <doc_ways_to_contribute>`.

.. seealso::

    The `Godot proposals repository <https://github.com/godotengine/godot-proposals>`__
    lists features that have been requested by the community and may be implemented
    in future Godot releases.
