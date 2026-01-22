.. _doc_what_is_gdextension:

What is GDExtension?
====================

**GDExtension** is a Godot-specific technology that lets the engine interact with
native `shared libraries <https://en.wikipedia.org/wiki/Library_(computing)#Shared_libraries>`__
at runtime. You can use it to run native code without compiling it with the engine.

There are three primary methods with which this is achieved:

* ``gdextension_interface.h``: A set of C functions that Godot and a GDExtension can use to communicate.
* ``extension_api.json``: A list of C functions that are exposed from Godot APIs (:ref:`Core Features <doc_scripting_core_features>`).
* :ref:`*.gdextension <doc_gdextension_file>`: A file format read by Godot to load a GDExtension.

Most people create GDExtensions with some existing language binding, such as :ref:`godot-cpp (for C++) <doc_godot_cpp>`,
or one of the :ref:`community-made ones <doc_what_is_gdnative_third_party_bindings>`.

Version compatibility
---------------------

See :ref:`godot-cpp Version Compatibility <doc_what_is_gdextension_version_compatibility>`, which applies to all GDExtensions.
