.. _doc_editor_icons:

Editor icons
============

When a new class is created and exposed to scripting, the editor's interface
will display it with a default icon representing the base class it inherits
from. In most cases, it's still recommended to create icons for new classes to
improve the user experience.

Creating icons
~~~~~~~~~~~~~~

To create new icons, you first need a vector graphics editor installed.
For instance, you can use the open source `Inkscape <https://inkscape.org/>`_ editor.

Clone the ``godot`` repository containing all the editor icons:

.. code-block:: bash

    git clone https://github.com/godotengine/godot.git

The icons must be created in a vector graphics editor in SVG format. There are
two main requirements to follow:

- Icons must be 16×16. In Inkscape, you can configure the document size in
  **File > Document Properties**.
- Lines should be snapped to pixels whenever possible to remain crisp at lower DPI.
  You can create a 16×16 grid in Inkscape to make this easier.

Once you're satisfied with the icon's design, save the icon in the cloned
repository's ``editor/icons`` folder. The icon name should match the intended
name in a case-sensitive manner. For example, to create an icon for
CPUParticles2D, name the file ``CPUParticles2D.svg``.

Color conversion for light editor themes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If the user has configured their editor to use a light theme, Godot will
convert the icon's colors based on a
`set of predefined color mappings <https://github.com/godotengine/godot/blob/4.0.2-stable/editor/editor_themes.cpp#L60-L160>`__.
This is to ensure the icon always displays with a sufficient contrast rate.
Try to restrict your icon's color palette to colors found in the list above.
Otherwise, your icon may become difficult to read on a light background.

Icon optimization
~~~~~~~~~~~~~~~~~

Because the editor renders SVGs once at load time, they need to be small
in size so they can be efficiently parsed. Editor icons must be first
optimized before being added to the engine, to do so:

1. Install `svgcleaner <https://github.com/RazrFalcon/svgcleaner>`__
   by downloading a binary from its
   `Releases tab <https://github.com/RazrFalcon/svgcleaner/releases/latest>`__
   and placing it into a location in your ``PATH`` environment variable.

2. Run the command below, replacing ``svg_source.svg`` with the path to your
   SVG file (which can be a relative or absolute path):

   .. code-block:: bash

       svgcleaner --multipass svg_source.svg svg_optimized.svg

The ``--multipass`` switch improves compression, so make sure to include it.
The optimized icon will be saved to ``svg_optimized.svg``. You can also change
the destination parameter to any relative or absolute path you'd like.

.. note::

    While this optimization step won't impact the icon's quality noticeably, it
    will still remove editor-only information such as guides. Therefore, it's
    recommended to keep the source SVG around if you need to make further
    changes.

Integrating and sharing the icons
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you're contributing to the engine itself, you should make a pull request to
add optimized icons to ``editor/icons`` in the main repository. Recompile the
engine to make it pick up new icons for classes.

It's also possible to create custom icons within a module. If you're creating
your own module and don't plan to integrate it with Godot, you don't need to
make a separate pull request for your icons to be available within the editor
as they can be self-contained.

For specific instructions on how to create module icons, refer to
:ref:`Creating custom module icons<doc_custom_module_icons>`.

Troubleshooting
~~~~~~~~~~~~~~~

If icons don't appear in the editor, make sure that:

1. Each icon's filename matches the naming requirement as described previously.

2. ``modules/svg`` is enabled (it should be enabled by default). Without it,
   icons won't appear in the editor at all.

References
~~~~~~~~~~

-  `editor/icons <https://github.com/godotengine/godot/tree/master/editor/icons>`__
