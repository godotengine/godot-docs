.. _doc_navigation_debug_tools:

Navigation Debug Tools
======================

.. note::

    The debug tools, properties and functions are only available in Godot debug builds. 
    Do not use any of them in code that will be part of a release build.

Enabling debug navigation
-------------------------

The navigation debug visualization is enabled by default inside the Editor.
To visualize navigation meshes and connections also at runtime 
enable the option ``Visible Navigation`` in the editor debug menu.

.. image:: img/navigation_debug_toggle.png

In Godot debug builds the navigation debug can also be toggled on the NavigationServers from scripts.

.. tabs::
 .. code-tab:: gdscript GDScript
    
    NavigationServer2D.set_debug_enabled(false)
    NavigationServer3D.set_debug_enabled(true)

Debug navigation settings
-------------------------

The appearance of navigation debug can be change in the ProjectSettings under ``debug/shapes/navigation``. 
Certain debug features can also be enabled or disabled at will but may require a scene restart to apply.

.. image:: img/nav_debug_settings.png

Debug navigation mesh polygons
------------------------------

If ``enable_edge_lines`` is enabled the edges of navigation mesh polygons will be highlighted.
If ``enable_edge_lines_xray`` is also enabled the edges of navigationmeshes will be visible through geometry.

if ``enable_geometry_face_random_color`` is enabled each navigation mesh face receives 
a random color that is mixed with the main color from ``geometry_face_color``.

.. image:: img/nav_debug_xray_edge_lines.png


Debug edge connections
----------------------

Different navigation meshes connected within ``edge_connection_margin`` distance are overlaid.
The color of the overlay is controlled with the navigation debug ``edge_connection_color``.
The connections can be made visible through geometry with the navigation debug ``enable_edge_connections_xray`` property.

.. image:: img/nav_edge_connection2d.gif

.. image:: img/nav_edge_connection3d.gif

.. note::

    Edge connections are only visible when the NavigationServer is active.
