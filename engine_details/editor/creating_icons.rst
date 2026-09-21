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
three main requirements to follow:

- Icons must be 16×16. In Inkscape, you can configure the document size in
  **File > Document Properties**.
- Lines should be snapped to pixels whenever possible to remain crisp at lower DPI.
  You can create a 16×16 grid in Inkscape to make this easier.
- If the user has configured their editor to use a light theme, Godot will
  convert the icon's colors based on a
  `set of predefined color mappings <https://github.com/godotengine/godot/blob/master/editor/themes/editor_color_map.cpp>`__.
  This is to ensure the icon always displays with a sufficient contrast rate.
  Try to restrict your icon's color palette to colors found in the list above.
  Otherwise, your icon may become difficult to read on a light background.

Once you're satisfied with the icon's design, save the icon in the cloned
repository's ``editor/icons`` folder. The icon name should match the intended
name in a case-sensitive manner. For example, to create an icon for
CPUParticles2D, name the file ``CPUParticles2D.svg``.

.. tip::

    You can also browse all existing icons on the
    `Godot editor icons <https://godotengine.github.io/editor-icons/>`__
    website.

Import options for custom icons
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For custom icons that are present in projects (as opposed to the engine source code),
there are two import options you should enable:

Scaling for hiDPI displays
^^^^^^^^^^^^^^^^^^^^^^^^^^

Icons need to be scaled properly on hiDPI displays to ensure they remain
crisp and large enough to be readable.

To ensure the icon is rendered at a correct scale on hiDPI displays, select the
SVG file in the FileSystem dock, enable the **Editor > Scale with Editor Scale**
option in the Import dock and click :button:`Reimport`. Note that this option is
only available for icons in SVG format, as it requires the use of a vector
format to work.

Color conversion for light editor themes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To ensure the icon has its colors converted when the user is using a light
theme, select the SVG file in the FileSystem dock, enable the **Editor > Convert
Colors with Editor Theme** option in the Import dock and click
:button:`Reimport`. Note that this option is only available for icons in SVG
format, as it requires the use of a vector format to work.

Icon optimization
~~~~~~~~~~~~~~~~~

Because the editor renders SVGs once at load time, they need to be small
in size so they can be efficiently parsed. When the
`pre-commit hook <https://contributing.godotengine.org/en/latest/engine/guidelines/code_style.html#pre-commit-hook>`__ runs, it automatically optimizes
the SVG using `svgo <https://github.com/svg/svgo>`_.

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
:ref:`Creating custom module icons <doc_custom_module_icons>`.

Troubleshooting
~~~~~~~~~~~~~~~

If icons don't appear in the editor, make sure that:

1. Each icon's filename matches the naming requirement as described previously.
2. The ``svg`` module is enabled at compile-time (it is enabled by default).
   Without this module, icons won't appear in the editor at all.

References
~~~~~~~~~~

-  `editor/icons <https://github.com/godotengine/godot/tree/master/editor/icons>`__
