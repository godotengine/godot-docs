Godot-Blender-Exporter
======================

Details on exporting
--------------------
.. toctree::
   :maxdepth: 1
   :name: toc-learn-workflow-assets-escn_exporter

   material
   physics
   lights
   mesh
   skeleton
   animation


Disabling specific objects
--------------------------
Sometimes you don't want some objects exported (eg high-res models used for
baking). An object will not be exported if it is not rendered in the scene.
This can be set in the outliner:

.. image:: img/hide.jpg

Objects hidden in the viewport will be exported, but will be hidden in the
Godot scene.


Build Pipeline Integration
--------------------------
If you have hundreds of model files, you don't want your artists to waste time
manually exporting their blend files. To combat this, the exporter provides a
python function ``io_scene_godot.export(out_file_path)`` that can be called to
export a file. This allows easy integration with other build systems. An
example Makefile and python script that exports all the blends in a directory
is present in the Godot-Blender-exporter repository.


