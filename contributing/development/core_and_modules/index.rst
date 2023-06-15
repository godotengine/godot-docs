:allow_comments: False

Engine core and modules
=======================

The following pages are meant to introduce the global organization of Godot Engine's
source code, and give useful tips for extending and fixing the engine on the C++ side.

Getting started with Godot's source code
----------------------------------------

This section covers the basics that you will encounter in (almost) every source file.

.. toctree::
   :maxdepth: 1
   :name: toc-devel-cpp-source-beginner

   godot_architecture_diagram
   common_engine_methods_and_macros
   core_types
   variant_class
   object_class
   inheritance_class_tree
   internal_rendering_architecture
   2d_coordinate_systems

Extending Godot by modifying its source code
--------------------------------------------

This section covers what you can do by modifying Godot's C++ source code.

.. toctree::
   :maxdepth: 1
   :name: toc-devel-cpp-source-advanced

   custom_modules_in_cpp
   binding_to_external_libraries
   custom_godot_servers
   custom_resource_format_loaders
   custom_audiostreams
   custom_platform_ports
   unit_testing
