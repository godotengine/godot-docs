. _doc_2d_meshes:

2D meshes
=========

Introduction
------------

In 3D, meshes are the key type of data used to display the world. In 2D, they are rarer as mostly images are used.
Godot's 2D engine is a pure two dimensional engine, so it can't really display 3D meshes directly (this is usually done
via ``Viewport`` and ``ViewportTexture``).

.. seealso:: If you are interested in displaying 3D meshes on a 2D viewport, see the :ref:`doc_viewport_as_texture` tutorial.


From Godot 3.1 onward, support is added for 2D meshes. These are meshes that contain two dimensional geometry (Z can be omitted or ignored) instead of 3D.
You can experiment creating them yourself using ``SurfaceTool`` from code and setting them in a ``Mesh2D`` node.

Currently, the only way to generate a 2D mesh within the editor is by either importing an OBJ file as a mesh, or converting it from a Sprite.

Optimizing pixels drawn
-----------------------

This workflow is useful for optimizing 2D drawing in some situations. When drawing large images with transparency, Godot will draw the whole quad to the screen.
If the image contains large transparent areas, they will still be drawn. 

This can affect performance, specially on mobile devices, when drawing very large images (generally screen sized), or layering multiple images on top of each other
with large transparent areas (usually ``ParallaxBackground``).

Converting to a mesh will ensure that only the opaque parts will be drawn and the rest will be ignored.

Converting Sprites to 2D meshes
-------------------------------

The easiest workflow for this optimization is by converting a ``Sprite`` to a ``Mesh2D``.
Start with an image that conatains large amounts of transparency on the edges, like this tree:

.. image:: img/mesh2d1.png

Put it in a ``Sprite`` and select "Convert to 2D Mesh" from the menu:

.. image:: img/mesh2d2.png

A dialog will appear, showing a preview of how the 2D mesh will be created:

.. image:: img/mesh2d3.png

The default values are good enough for most cases, but you can change growth and simplification according to your needs:

.. image:: img/mesh2d4.png

Finally, push the ``Convert 2D Mesh`` button and your Sprite will be replaced:

.. image:: img/mesh2d5.png
