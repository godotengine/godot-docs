.. _doc_what_is_gdextension:

What is GDExtension?
====================

Introduction
------------

**GDExtension** is a Godot-specific technology that lets the engine interact with
native `shared libraries <https://en.wikipedia.org/wiki/Library_(computing)#Shared_libraries>`__
at runtime. You can use it to run native code without compiling it with the engine.

.. note:: GDExtension is *not* a scripting language and has no relation to
          :ref:`GDScript <doc_gdscript>`.

Differences between GDExtension and C++ modules
-----------------------------------------------

You can use both GDExtension and :ref:`C++ modules <doc_custom_modules_in_cpp>` to
run C or C++ code in a Godot project.

They also both allow you to integrate third-party libraries into Godot. The one
you should choose depends on your needs.

.. warning::

    GDExtension is currently *experimental*, which means that we may
    break compatibility in order to fix major bugs or include critical features.

Advantages of GDExtension
~~~~~~~~~~~~~~~~~~~~~~~~~

Unlike modules, GDExtension doesn't require compiling the engine's source code,
making it easier to distribute your work. It gives you access to most of the API
available to GDScript and C#, allowing you to code game logic with full control
regarding performance. It's ideal if you need high-performance code you'd like
to distribute as an add-on in the :ref:`asset library <doc_what_is_assetlib>`.

Also:

- GDExtension is not limited to C and C++. Thanks to :ref:`third-party bindings
  <doc_what_is_gdnative_third_party_bindings>`, you can use it with many other
  languages.
- You can use the same compiled GDExtension library in the editor and exported
  project. With C++ modules, you have to recompile all the export templates you
  plan to use if you require its functionality at runtime.
- GDExtension only requires you to compile your library, not the whole engine.
  That's unlike C++ modules, which are statically compiled into the engine.
  Every time you change a module, you need to recompile the engine. Even with
  incremental builds, this process is slower than using GDExtension.

Advantages of C++ modules
~~~~~~~~~~~~~~~~~~~~~~~~~

We recommend :ref:`C++ modules <doc_custom_modules_in_cpp>` in cases where
GDExtension isn't enough:

- C++ modules provide deeper integration into the engine. GDExtension's access
  is not as deep as static modules.
- You can use C++ modules to provide additional features in a project without
  carrying native library files around. This extends to exported projects.

.. note::

    If you notice that specific systems are not accessible via GDExtension
    but are via custom modules, feel free to open an issue on the
    `godot-cpp repository <https://github.com/godotengine/godot-cpp>`__
    to discuss implementation options for exposing the missing functionality.

Supported languages
-------------------

The Godot developers officially support the following language bindings for
GDExtension:

- C++ :ref:`(tutorial) <doc_gdextension_cpp_example>`

.. note::

    There are no plans to support additional languages with GDExtension officially.
    That said, the community offers several bindings for other languages (see
    below).

.. _doc_what_is_gdnative_third_party_bindings:

The bindings below are developed and maintained by the community:

.. Binding developers: Feel free to open a pull request to add your binding if it's well-developed enough to be used in a project.
.. Please keep languages sorted in alphabetical order.

- `D <https://github.com/godot-dlang/godot-dlang>`__
- `Go <https://github.com/grow-graphics/gd>`__
- `Nim <https://github.com/godot-nim/gdext-nim>`__
- `Rust <https://github.com/godot-rust/gdext>`__
- `Swift <https://github.com/migueldeicaza/SwiftGodot>`__
- `Odin <https://github.com/dresswithpockets/odin-godot>`__

.. note::

    Not all bindings mentioned here may be production-ready. Make sure to
    research options thoroughly before starting a project with one of those.
    Also, double-check whether the binding is compatible with the Godot version
    you're using.

.. _doc_what_is_gdextension_version_compatibility:

Version compatibility
---------------------

Usually, GDExtensions targeting an earlier version of Godot will work in later
minor versions, but not vice-versa. For example, a GDExtension targeting Godot 4.2
should work just fine in Godot 4.3, but one targeting Godot 4.3 won't work in Godot 4.2.

For this reason, when creating GDExtensions, you may want to target the lowest version of
Godot that has the features you need, *not* the most recent version of Godot. This can
save you from needing to create multiple builds for different versions of Godot.

However, GDExtension is currently *experimental*, which means that we may
break compatibility in order to fix major bugs or include critical features.
For example, GDExtensions created for Godot 4.0 aren't compatible with Godot
4.1 (see :ref:`updating_your_gdextension_for_godot_4_1`).

GDExtensions are also only compatible with engine builds that use the same
level of floating-point precision the extension was compiled for. This means
that if you use an engine build with double-precision floats, the extension must
also be compiled for double-precision floats and use an ``extension_api.json``
file generated by your custom engine build. See :ref:`doc_large_world_coordinates`
for details.

Generally speaking, if you build a custom version of Godot, you should generate an
``extension_api.json`` from it for your GDExtensions, because it may have some differences
from official Godot builds.
