.. _doc_editor_icons:

Editor icons
============

When a new class is created and exposed to scripting, the editor's interface
will display it with a default icon representing the base class it inherits
from. Yet in most cases it is recommended to create icons for new classes
to improve the user experience.

Creating icons
~~~~~~~~~~~~~~

In order to create new icons, you first need a vector graphics editor installed.
For instance, you can use the open-source `Inkscape <https://inkscape.org/>`_ editor.

Clone the ``godot-design`` repository containing all the original editor icons:

   .. code:: bash

       git clone https://github.com/godotengine/godot-design

The icons must be created in a vector graphics editor in ``svg`` format. You
can use ``engine/icons/inkscape_template.svg`` with default icon properties
already set up.

Once you're satisfied with the icon's design, save the icon in
``engine/icons/svg/`` folder. But in order for the engine to automatically
pick up the icons, each icon's filename:

1. Must be prefixed with ``icon_``.

2. ``PascalCase`` name should be converted to ``snake_case``, so words
   are separated by ``_`` whenever case changes, and uppercase acronyms must
   also have all letters, numbers, and special characters separated as distinct
   words. Some examples:

   +--------------------+----------------------------------+
   | Name               | Filename                         |
   +====================+==================================+
   | ``Polygon2D``      | ``icon_polygon_2_d.svg``         |
   +--------------------+----------------------------------+
   | ``CSGPolygon``     | ``icon_c_s_g_polygon.svg``       |
   +--------------------+----------------------------------+
   | ``CPUParticles2D`` | ``icon_c_p_u_particles_2_d.svg`` |
   +--------------------+----------------------------------+
   | ``C#``             | ``icon_c_#.svg``                 |
   +--------------------+----------------------------------+

Icon optimization
~~~~~~~~~~~~~~~~~

Because the editor renders the ``svg``'s at runtime, they need to be small
in size, so they can be efficiently parsed. Editor icons must be first
optimized before being added to the engine, to do so:

1. Add them to the ``engine/icons/svg`` folder.

2. Run the ``optimize.py`` script. You must have the ``scour`` package installed:

   .. code:: bash

       pip install scour
       cd godot-design/engine/icons && ./optimize.py

The optimized icons will be generated in the ``engine/icons/optimized`` folder.

Integrating and sharing the icons
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you're contributing to the engine itself, you should make a pull request to
add optimized icons to ``godot/editor/icons`` in the main repository. Recompile
the engine to make sure it does pick up new icons for classes. Once merged,
don't forget to add the original version of the icons to the ``godot-design``
repository so that the icon can be improved upon by other contributors.

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

2. ``modules/svg`` is enabled (should be enabled by default). Without it, icons
   won't appear in the editor at all.

References:
~~~~~~~~~~~

-  `editor/icons <https://github.com/godotengine/godot/tree/master/editor/icons>`__
