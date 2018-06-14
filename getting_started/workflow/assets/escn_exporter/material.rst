Materials
=========

Using existing Godot materials
--------------------------------
One way in which the exporter can handle materials is to attempt to match
the Blender material with an existing Godot material. This has the advantage of
being able to use all of the features of Godot's material system, but it means
that you cannot see your model with the material applied inside Blender.

To do this, the exporter attempts to find Godot materials with names that match
those of the material name in Blender. So if you export an object in Blender
with the material name ``PurpleDots`` then the exporter will search for the
file ``PurpleDots.tres`` and assign it to the object. If this file is not a
``SpatialMaterial`` or ``ShaderMaterial`` or if it cannot be found, then the
exporter will fall back to exporting the material from Blender.


Where the exporter searches for the ``.tres`` file is determined by the "Material
Search Paths" option:

.. image:: img/material_search.jpg

This can take the value of:
 - Project Directory - Attempts to find the ``project.Godot`` and recursively
   searches through subdirectories. If ``project.Godot`` cannot be found it
   will throw an error. This is useful for most projects where naming conflicts
   are unlikely.
 - Export Directory - Look for materials in subdirectories of the export
   location. This is useful for projects where you may have duplicate
   material names and need more control over what material gets assigned.
 - None - Do not search for materials. Export them from the Blender file.


Export of Blender materials
---------------------------

The other way materials are handled is for the exporter to export them from
Blender. Currently only the diffuse color and a few flags (eg unshaded) are
exported.

.. warning::
	Export of Blender materials is currently very primitive. However, it is the
	focus of a current GSOC project

.. warning::
	Materials are currently exported using their "Blender Render" settings.
	When Blender 2.8 is released, this will be removed and this part of the
	exporter will change.
