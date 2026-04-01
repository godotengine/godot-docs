:allow_comments: False

.. _doc_engine_module_api:

Engine extension APIs
=====================

This section introduces various ways in which you can extend the engine with C++ code.
You can use these APIs by creating a :ref:`module <doc_custom_modules_in_cpp>`.
Note that you can change the engine in many more ways than presented here — this section just presents
a subselection of common and useful ways to do it.

Alternatively, some of the functions presented here are also available through the
:ref:`GDExtension <doc_what_is_gdextension>` API.
You can use them in C++ by using creating a :ref:`godot-cpp <doc_about_godot_cpp>` based GDExtension,
or with any of the :ref:`community-created GDExtension implementations <doc_scripting_languages>`. Note though
that some aspects of the code or directory structures may be different in GDExtension compared to the module APIs.

.. toctree::
   :maxdepth: 1
   :name: toc-devel-cpp-source-advanced

   custom_modules_in_cpp
   gdextension/index
   binding_to_external_libraries
   custom_godot_servers
   custom_resource_format_loaders
   custom_audiostreams
   custom_platform_ports
