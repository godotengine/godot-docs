.. _doc_importing_3d_scenes_model_export_considerations:

Model export considerations
===========================

Before exporting a 3D model from a 3D modeling application, such as Blender,
there are some considerations that should be taken into account to ensure that
the model follows the conventions and best practices for Godot.

3D asset direction conventions
------------------------------

Godot uses a right-handed, Y-is-up coordinate system, with the -Z axis as
the camera's forward direction. This is the same as OpenGL. This implies
that +Z is back, +X is right, and -X is left for a camera.

The convention for 3D assets is to face the opposite direction as the camera,
so that characters and other assets are facing the camera by default.
This convention is extremely common in 3D modeling applications, and is
`codified in glTF as part of the glTF 2.0 specification <https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#coordinate-system-and-units>`__.
This means that for oriented 3D assets (such as characters),
the +Z axis is the direction of the front, so -Z is the rear,
+X is the left side, and -X is the right side for a 3D asset.
In Blender, this means that +Y is rear and -Y is front for an asset.

When rotating an oriented 3D asset in Godot, use the ``use_model_front``
option on the ``look_at`` functions, and use the ``Vector3.MODEL_*``
constants to perform calculations in the oriented asset's local space.

For assets without an intrinsic front side or forward direction, such as
a game map or terrain, take note of the cardinal directions instead.
The convention in Godot and the vast majority of other applications is
that +X is east and -X is west. Due to Godot's right-handed Y-is-up
coordinate system, this implies that +Z is south and -Z is north.
In Blender, this means that +Y is north and -Y is south.

Exporting textures separately
-----------------------------

While textures can be exported with a model in certain file formats, such as glTF 2.0, you can also export them
separately. Godot uses PBR (physically based rendering) for its materials, so if a texturing program can export PBR
textures they can work in Godot. This includes the `Substance suite <https://www.substance3d.com/>`__,
`ArmorPaint (open source) <https://armorpaint.org/>`__, and `Material Maker (open source) <https://github.com/RodZill4/material-maker>`__.

.. note:: For more information on Godot's materials, see :ref:`doc_standard_material_3d`.

Exporting considerations
------------------------

Since GPUs can only render triangles, meshes that contain quads or N-gons have
to be *triangulated* before they can be rendered. Godot can triangulate meshes
on import, but results may be unpredictable or incorrect, especially with
N-gons. Regardless of the target application, triangulating *before* exporting
the scene will lead to more consistent results and should be done whenever
possible.

To avoid issues with incorrect triangulation after importing in Godot, it is
recommended to make the 3D modeling software triangulate objects on its own. In
Blender, this can be done by adding a Triangulate modifier to your objects and
making sure **Apply Modifiers** is checked in the export dialog. Alternatively,
depending on the exporter, you may be able to find and enable a **Triangulate
Faces** option in the export dialog.

To avoid issues with 3D selection in the editor, it is recommended to apply the
object transform in the 3D modeling software before exporting the scene.

.. note::

    It is important that the mesh is not deformed by bones when exporting. Make sure
    that the skeleton is reset to its T-pose or default rest pose before exporting
    with your favorite 3D editor.

Lighting considerations
-----------------------

While it's possible to import lights from a 3D scene using the glTF, ``.blend``
or Collada formats, it's generally advised to design the scene's lighting in the
Godot editor after importing the scene.

This allows you to get a more accurate feel for the final result, as different
engines will render lights in a different manner. This also avoids any issues
with lights appearing excessively strong or faint as a result of the import
process.
