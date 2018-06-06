.. _doc_scene_from_other_software:

3D Scene From Other Software
=============================

Exporting DAE files from Maya and 3DS Max
-----------------------------------------

Autodesk added built-in collada support to Maya and 3DS Max, but it's
broken by default and should not be used. The best way to export this format
is by using the
`OpenCollada <https://github.com/KhronosGroup/OpenCOLLADA/wiki/OpenCOLLADA-Tools>`__
plugins. They work well, although they are not always up-to date
with the latest version of the software.

Exporting DAE files from Blender
--------------------------------

Blender has built-in collada support too, but it's also broken and
should not be used.

Godot provides a `Python
Plugin <https://github.com/godotengine/collada-exporter>`__
that will do a much better job of exporting the scenes.

Exporting ESCN files from Blender
---------------------------------

The .escn files shares the same format with .tscn (Godot scene file), but
it will be compressed to binary once it is imported to Godot.

Blender plugin `godot
-blender-exporter <https://github.com/godotengine/godot-blender-exporter>`__
is in experimental use.
