.. _doc_dae_exporter:

DAE Exporters
==============

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
