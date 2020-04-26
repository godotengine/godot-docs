.. _doc_editor_icons:

Editor icons
============

When a new class is created and exposed to scripting, the editor's interface
will display it with a default icon representing the base class it inherits
from. Yet in most cases it is recommended to create icons for new classes
to improve the user experience.

Creating icons
~~~~~~~~~~~~~~

To create new icons, you first need a vector graphics editor installed.
For instance, you can use the open source `Inkscape <https://inkscape.org/>`_ editor.

Clone the ``godot`` repository containing all the editor icons:

   .. code-block:: bash

       git clone https://github.com/godotengine/godot

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

Icon optimization
~~~~~~~~~~~~~~~~~

Because the editor renders SVGs once at load time, they need to be small
in size so they can be efficiently parsed. Editor icons must be first
optimized before being added to the engine, to do so:

1. Add them to the ``engine/icons/svg`` folder.

2. Run the ``optimize.py`` script. You must have the ``scour`` package installed:

   .. code-block:: bash

       pip install scour
       cd godot-design/engine/icons && ./optimize.py

The optimized icons will be generated in the ``engine/icons/optimized`` folder.

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

If icons don't appear in the editor make sure that:

1. Each icon's filename matches the naming requirement as described previously.

2. ``modules/svg`` is enabled (it should be enabled by default). Without it,
   icons won't appear in the editor at all.

References
~~~~~~~~~~

-  `editor/icons <https://github.com/godotengine/godot/tree/master/editor/icons>`__
