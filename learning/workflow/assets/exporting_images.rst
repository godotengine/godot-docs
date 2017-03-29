.. _doc_exporting_images:

Exporting images
================

It is often desired to do an operation to all or a group of images upon
export. Godot provides some tools for this. Examples of such operations
are:

-  Converting all images from a lossless format to a lossy one (ie: png
   -> WebP) for greater compression.
-  Shrinking all images to half the size, to create a low resolution
   build for smaller screens.
-  Create an atlas for a group of images and crop them, for higher
   performance and less memory usage.

Image export options
--------------------

In the "Project Export Settings" dialog, go to the Images tab:

.. image:: /img/exportimages.png

In this dialog the image extensions for conversion can be selected, and
operations can be performed that apply to all images (except those in
groups, see the next section for those):

-  **Convert Image Format**: Probably the most useful operation is to
   convert to Lossy (WebP) to save disk space. For lossy, a Quality bar
   can set the quality/vs size ratio.
-  **Shrink**: This allows to shrink all images by a given amount. It's
   useful to export a game to half or less resolution for special
   devices.
-  **Compress Formats**: Allows to select which image exensions to
   convert.

On export, Godot will perform the desired operation. The first export
might be really slow, but subsequent exports will be fast, as the
converted images will be cached.

Image group export options
--------------------------

This section is similar to the previous one, except it can operate on a
selected group of images. When a image is in a group, the settings from
the global export options are overridden by the ones from the group. An
image can only be in one group at the same time. So if the image is in
another group different to the current one being edited, it will not be
selectable.

.. image:: /img/imagegroup.png

Atlas
~~~~~

Grouping images allows a texture atlas to be created. When this mode is
active, a button to preview the resulting atlas becomes available. Make
sure that atlases don't become too big, as some hardware will not
support textures bigger than 2048x2048 pixels. If this happens, just
create another atlas.

The atlas can be useful to speed up drawing of some scenes, as state
changes are minimized when drawing from it (through unlike other
engines, Godot is designed so state changes do not affect it as much).
Textures added to an atlas get cropped (empty spaces around the image
are removed), so this is another reason to use them (save space). If
unsure, though, just leave that option disabled.
