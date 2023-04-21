.. _doc_large_world_coordinates:

Large world coordinates
=======================

.. note::

    Large world coordinates are mainly useful in 3D projects; they are rarely
    required in 2D projects. Also, unlike 3D rendering, 2D rendering currently
    doesn't benefit from increased precision when large world coordinates are
    enabled.

Why use large world coordinates?
--------------------------------

In Godot, physics simulation and rendering both rely on *floating-point* numbers.
However, in computing, floating-point numbers have **limited precision and range**.
This can be a problem for games with huge worlds, such as space or planetary-scale
simulation games.

Precision is the greatest when the value is close to ``0.0``. Precision becomes
gradually lower as the value increases or decreases away from ``0.0``. This
occurs every time the floating-point number's *exponent* increases, which
happens when the floating-point number surpasses a power of 2 value (2, 4, 8,
16, …). Every time this occurs, the number's minimum step will *increase*,
resulting in a loss of precision.

In practice, this means that as the player moves away from the world origin
(``Vector2(0, 0)`` in 2D games or ``Vector3(0, 0, 0)`` in 3D games), precision
will decrease.

This loss of precision can result in objects appearing to "vibrate" when far
away from the world origin, as the model's position will snap to the
nearest value that can be represented in a floating-point number. This can also
result in physics glitches that only occur when the player is far from the world
origin.

The range determines the minimum and maximum values that can be stored in the
number. If the player tries to move past this range, they will simply not be
able to. However, in practice, floating-point precision almost always becomes
a problem before the range does.

The range and precision (minimum step between two exponent intervals) are
determined by the floating-point number type. The *theoretical* range allows
extremely high values to be stored in single-precision floats, but with very low
precision. In practice, a floating-point type that cannot represent all integer
values is not very useful. At extreme values, precision becomes so low that the
number cannot even distinguish two separate *integer* values from each other.

This is the range where individual integer values can be represented in a
floating-point number:

- **Single-precision float range (represent all integers):** Between -16,777,216 and 16,777,216
- **Double-precision float range (represent all integers):** Between -9 quadrillon and 9 quadrillon

+----------------------+-----------------------+-----------------------+-----------------------------------------------------------------------------+
| Range                | Single step           | Double step           | Comment                                                                     |
+----------------------+-----------------------+-----------------------+-----------------------------------------------------------------------------+
| [1; 2]               | ~0.0000001            | ~1e-15                | Precision becomes greater near 0.0 (this table is abbreviated).             |
+----------------------+-----------------------+-----------------------+-----------------------------------------------------------------------------+
| [2; 4]               | ~0.0000002            | ~1e-15                |                                                                             |
+----------------------+-----------------------+-----------------------+-----------------------------------------------------------------------------+
| [4; 8]               | ~0.0000005            | ~1e-15                |                                                                             |
+----------------------+-----------------------+-----------------------+-----------------------------------------------------------------------------+
| [8; 16]              | ~0.000001             | ~1e-14                |                                                                             |
+----------------------+-----------------------+-----------------------+-----------------------------------------------------------------------------+
| [16; 32]             | ~0.000002             | ~1e-14                |                                                                             |
+----------------------+-----------------------+-----------------------+-----------------------------------------------------------------------------+
| [32; 64]             | ~0.000004             | ~1e-14                |                                                                             |
+----------------------+-----------------------+-----------------------+-----------------------------------------------------------------------------+
| [64; 128]            | ~0.000008             | ~1e-13                |                                                                             |
+----------------------+-----------------------+-----------------------+-----------------------------------------------------------------------------+
| [128; 256]           | ~0.000015             | ~1e-13                |                                                                             |
+----------------------+-----------------------+-----------------------+-----------------------------------------------------------------------------+
| [256; 512]           | ~0.00003              | ~1e-13                |                                                                             |
+----------------------+-----------------------+-----------------------+-----------------------------------------------------------------------------+
| [512; 1024]          | ~0.00006              | ~1e-12                |                                                                             |
+----------------------+-----------------------+-----------------------+-----------------------------------------------------------------------------+
| [1024; 2048]         | ~0.0001               | ~1e-12                |                                                                             |
+----------------------+-----------------------+-----------------------+-----------------------------------------------------------------------------+
| [2048; 4096]         | ~0.0002               | ~1e-12                | Maximum *recommended* single-precision range for a first-person 3D game     |
|                      |                       |                       | without rendering artifacts or physics glitches.                            |
+----------------------+-----------------------+-----------------------+-----------------------------------------------------------------------------+
| [4096; 8192]         | ~0.0005               | ~1e-12                | Maximum *recommended* single-precision range for a third-person 3D game     |
|                      |                       |                       | without rendering artifacts or physics glitches.                            |
+----------------------+-----------------------+-----------------------+-----------------------------------------------------------------------------+
| [8192; 16384]        | ~0.001                | ~1e-12                |                                                                             |
+----------------------+-----------------------+-----------------------+-----------------------------------------------------------------------------+
| [16384; 32768]       | ~0.0019               | ~1e-11                | Maximum *recommended* single-precision range for a top-down 3D game         |
|                      |                       |                       | without rendering artifacts or physics glitches.                            |
+----------------------+-----------------------+-----------------------+-----------------------------------------------------------------------------+
| [32768; 65536]       | ~0.0039               | ~1e-11                | Maximum *recommended* single-precision range for any 3D game. Double        |
|                      |                       |                       | precision (large world coordinates) is usually required past this point.    |
+----------------------+-----------------------+-----------------------+-----------------------------------------------------------------------------+
| [65536; 131072]      | ~0.0078               | ~1e-11                |                                                                             |
+----------------------+-----------------------+-----------------------+-----------------------------------------------------------------------------+
| [131072; 262144]     | ~0.0156               | ~1e-10                |                                                                             |
+----------------------+-----------------------+-----------------------+-----------------------------------------------------------------------------+
| > 262144             | > ~0.0313             | ~1e-10 (0.0000000001) | Double-precision remains far more precise than single-precision             |
|                      |                       |                       | past this value.                                                            |
+----------------------+-----------------------+-----------------------+-----------------------------------------------------------------------------+

When using single-precision floats, it is possible to go past the suggested
ranges, but more visible artifacting will occur and physics glitches will be
more common (such as the player not walking straight in certain directions).

.. seealso::

    See the `Demystifying Floating Point Precision <https://blog.demofox.org/2017/11/21/>`__
    article for more information.

How large world coordinates work
--------------------------------

Large world coordinates (also known as **double-precision physics**) increase
the precision level of all floating-point computations within the engine.

By default, :ref:`class_float` is 64-bit in GDScript, but :ref:`class_Vector2`,
:ref:`class_Vector3` and :ref:`class_Vector4` are 32-bit. This means that the
precision of vector types is much more limited. To resolve this, we can increase
the number of bits used to represent a floating-point number in a Vector type.
This results in an *exponential* increase in precision, which means the final
value is not just twice as precise, but potentially thousands of times more
precise at high values. The maximum value that can be represented is also
greatly increased by going from a single-precision float to a double-precision
float.

To avoid model snapping issues when far away from the world origin, Godot's 3D
rendering engine will increase its precision for rendering operations when large
world coordinates are enabled. The shaders do not use double-precision floats
for performance reasons, but an `alternative solution <https://github.com/godotengine/godot/pull/66178>`__
is used to emulate double precision for rendering using single-precision floats.

.. note::

    Enabling large world coordinates comes with a performance and memory usage
    penalty, especially on 32-bit CPUs. Only enable large world coordinates if
    you actually need them.

    This feature is tailored towards mid-range/high-end desktop platforms. Large
    world coordinates may not perform well on low-end mobile devices, unless you
    take steps to reduce CPU usage with other means (such as decreasing the
    number of physics ticks per second).

    On low-end platforms, an *origin shifting* approach can be used instead to
    allow for large worlds without using double-precision physics and rendering.
    Origin shifting works with single-precision floats, but it introduces more
    complexity to game logic, especially in multiplayer games. Therefore, origin
    shifting is not detailed on this page.

Who are large world coordinates for?
------------------------------------

Large world coordinates are typically required for 3D space or planetary-scale
simulation games. This extends to games that require supporting *very* fast
movement speeds, but also very slow *and* precise movements at times.

On the other hand, it's important to only use large world coordinates when
actually required (for performance reasons). Large world coordinates are usually
**not** required for:

- 2D games, as precision issues are usually less noticeable.
- Games with small-scale or medium-scale worlds.
- Games with large worlds, but split into different levels with loading
  sequences in between. You can center each level portion around the world
  origin to avoid precision issues without a performance penalty.
- Open world games with a *playable on-foot area* not exceeding 8192×8192 meters
  (centered around the world origin). As shown in the above table, the level of
  precision remains acceptable within that range, even for a first-person game.

**If in doubt**, you probably don't need to use large world coordinates in your
project. For reference, most modern AAA open world titles don't use a large
world coordinates system and still rely on single-precision floats for both
rendering and physics.

Enabling large world coordinates
--------------------------------

This process requires recompiling the editor and all export template binaries
you intend to use. If you only intend to export your project in release mode,
you can skip the compilation of debug export templates. In any case, you'll need
to compile an editor build so you can test your large precision world without
having to export the project every time.

See the :ref:`Compiling <toc-devel-compiling>` section for compiling
instructions for each target platform. You will need to add the ``precision=double``
SCons option when compiling the editor and export templates.

The resulting binaries will be named with a ``.double`` suffix to distinguish
them from single-precision binaries (which lack any precision suffix). You can
then specify the binaries as custom export templates in your project's export
presets in the Export dialog.

Compatibility between single-precision and double-precision builds
------------------------------------------------------------------

When saving a *binary* resource using the :ref:`class_ResourceSaver` singleton,
a special flag is stored in the file if the resource was saved using a build
that uses double-precision numbers. As a result, all binary resources will
change on disk when you switch to a double-precision build and save over them.

Both single-precision and double-precision builds support using the
:ref:`class_ResourceLoader` singleton on resources that use this special flag.
This means single-precision builds can load resources saved using
double-precision builds and vice versa. Text-based resources don't store a
double-precision flag, as they don't require such a flag for correct reading.

Known incompatibilities
^^^^^^^^^^^^^^^^^^^^^^^

- In a networked multiplayer game, the server and all clients should be using
  the same build type to ensure precision remains consistent across clients.
  Using different build types *may* work, but various issues can occur.
- The GDExtension API changes in an incompatible way in double-precision builds.
  This means extensions **must** be rebuilt to work with double-precision
  builds. On the extension developer's end, the ``REAL_T_IS_DOUBLE`` define is
  enabled when building a GDExtension with ``precision=double``.
  ``real_t`` can be used as an alias for ``float`` in single-precision builds,
  and ``double`` in double-precision builds.

Limitations
-----------

Since 3D rendering shaders don't actually use double-precision floats, there are
some limitations when it comes to 3D rendering precision:

- Shaders using the ``skip_vertex_transform`` or ``world_vertex_coords`` don't
  benefit from increased precision.
- :ref:`Triplanar mapping <doc_standard_material_3d_triplanar_mapping>` doesn't
  benefit from increased precision. Materials using triplanar mapping will exhibit
  visible jittering when far away from the world origin.

2D rendering currently doesn't benefit from increased precision when large world
coordinates are enabled. This can cause visible model snapping to occur when
far away from the world origin (starting from a few million pixels at typical
zoom levels). 2D physics calculations will still benefit from increased
precision though.
