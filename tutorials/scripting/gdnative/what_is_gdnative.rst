.. _doc_what_is_gdnative:

What is GDNative?
=================

Introduction
------------

**GDNative** is a Godot-specific technology that lets the engine interact with
native `shared libraries <https://en.wikipedia.org/wiki/Library_(computing)#Shared_libraries>`__
at run-time. You can use it to run native code without compiling it with the engine.

.. note:: GDNative is *not* a scripting language and has no relation to
          :ref:`GDScript <doc_gdscript>`.

Differences between GDNative and C++ modules
--------------------------------------------

You can use both GDNative and :ref:`C++ modules <doc_custom_modules_in_c++>` to
run C or C++ code in a Godot project.

They also both allow you to integrate third-party libraries into Godot. The one
you should choose depends on your needs.

Advantages of GDNative
^^^^^^^^^^^^^^^^^^^^^^

Unlike modules, GDNative doesn't require compiling the engine's source code,
making it easier to distribute your work. It gives you access to most of the API
available to GDScript C#, allowing you to code game logic with full control
regarding performance. It's ideal if you need high-performance code you'd like
to distribute as an add-on in the :ref:`asset library <doc_what_is_assetlib>`.

Also:

- GDNative is not limited to C and C++. Thanks to :ref:`third-party bindings
  <doc_what_is_gdnative_third_party_bindings>`, you can use it with many other
  languages.
- You can use the same compiled GDNative library in the editor and exported
  project. With C++ modules, you have to recompile all the export templates you
  plan to use if you require its functionality at run-time.
- GDNative only requires you to compile your library, not the whole engine.
  That's unlike C++ modules, which are statically compiled into the engine.
  Every time you change a module, you need to recompile the engine. Even with
  incremental builds, this process is slower than using GDNative.

Advantages of C++ modules
^^^^^^^^^^^^^^^^^^^^^^^^^

We recommend :ref:`C++ modules <doc_custom_modules_in_c++>` in cases where
GDNative isn't enough:

- C++ modules provide deeper integration into the engine. GDNative's access is
  limited to what the scripting API exposes.
- You can use C++ modules to provide additional features in a project without
  carrying native library files around. This extends to exported projects.
- C++ modules are supported on all platforms. In contrast, GDNative has only
  limited support on HTML5 (cannot be used together with multi-threading), and
  is not supported on Universal Windows Platform (UWP).
- C++ modules can be faster than GDNative, especially when the code requires a
  lot of communication through the scripting API.

Supported languages
-------------------

The Godot developers officially support the following language bindings for
GDNative:

- C++ :ref:`(tutorial) <doc_gdnative_cpp_example>`
- C :ref:`(tutorial) <doc_gdnative_c_example>`

.. note::

    There are no plans to support additional languages with GDNative officially.
    That said, the community offers several bindings for other languages (see
    below).

.. _doc_what_is_gdnative_third_party_bindings:

The bindings below are developed and maintained by the community:

.. Binding developers: Feel free to open a pull request to add your binding if it's well-developed enough to be used in a project.
.. Please keep languages sorted in alphabetical order.

- `D <https://github.com/godot-d/godot-d>`__
- `Kotlin <https://github.com/utopia-rise/godot-kotlin-jvm>`__
- `Nim <https://github.com/pragmagic/godot-nim>`__
- `Python <https://github.com/touilleMan/godot-python>`__
- `Rust <https://github.com/godot-rust/godot-rust>`__

.. note::

    Not all bindings mentioned here may be production-ready. Make sure to
    research options thoroughly before starting a project with one of those.
    Also, double-check whether the binding is compatible with the Godot version
    you're using.

Version compatibility
---------------------

:ref:`Unlike Godot itself <doc_release_policy>`, GDNative has stricter version
compatibility requirements as it relies on low-level *ptrcalls* to function.

GDNative add-ons compiled for a given Godot version are only guaranteed to work
with the same minor release series. For example, a GDNative add-on compiled for
Godot 3.4 will only work with Godot 3.4, 3.4.1, 3.4.2… but not Godot 3.3 or 3.5.
