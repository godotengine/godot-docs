Lights
======

.. warning::
    This chapter covers the Blender plugin
    `Godot Blender Exporter <https://github.com/godotengine/godot-blender-exporter>`__,
    which is deprecated in Godot 4.x. To export from Blender to Godot 4.x, use
    one of the :ref:`available 3D formats <doc_importing_3d_scenes_available_formats>`.

.. warning::
    By default, lamps in Blender have shadows enabled. This can cause
    performance issues in Godot.

.. warning::
    Lamps are exported using their "Blender Render" settings. When Blender 2.8
    is released, this will be removed and this part of the exporter will change.

Sun, point and spot lamps are all exported from Blender along with many of their
properties:

.. image:: img/light_properties.jpg

There are some things to note:

 - In Blender, a light casts light all the way to infinity. In Godot, it is
   clamped by the attenuation distance. To most closely match between the
   viewport and Godot, enable the "Sphere" checkbox. (Highlighted green)
 - Light attenuation models differ between Godot and Blender. The exporter
   attempts to make them match, but it isn't always very good.
 - Spotlight angular attenuation models also differ between Godot and Blender.
   The exporter attempts to make them similar, but it doesn't always look the
   same.
 - There is no difference between buffer shadow and ray shadow in the export.
