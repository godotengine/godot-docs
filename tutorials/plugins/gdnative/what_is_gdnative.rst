.. _doc_what_is_gdnative:

What is GDNative?
=================

Introduction
------------

**GDNative** is a Godot-specific technology that lets the engine interact with
native shared libraries at run-time. This means it can be used to run native
code that was not originally supplied with the engine.

GDNative is *not* a scripting language and has no relation to :ref:`GDScript <doc_gdscript>`.

Differences between GDNative and C++ modules
--------------------------------------------

Both GDNative and :ref:`C++ modules <doc_custom_modules_in_c++>` can be used to
run C/C++ code in a Godot project.
Both GDNative and C++ modules also make it possible to integrate third-party
libraries into Godot. Which one to choose depends on your needs:

Advantages of GDNative
^^^^^^^^^^^^^^^^^^^^^^

GDNative is most suited to game logic (although GDScript/C# will still be more
convenient for this use case). The easier setup for end users also makes
GDNative more suitable for add-ons published to the :ref:`asset library
<doc_what_is_assetlib>`.

- GDNative is not limited to C/C++. Thanks to
  :ref:`third-party bindings <doc_what_is_gdnative_third_party_bindings>`,
  it can be used with many other languages.
- The same compiled GDNative library can be used both in the editor and exported
  project. With C++ modules, you have to recompile all the export templates you
  plan to use if module functionality is required at run-time.
- C++ modules are statically compiled into the engine. Every time you make a
  change, you need to recompile the engine. Even with incremental builds, this
  process often takes more than 10 seconds on most machines. In contrast, GDNative
  only requires you to compile your library, not the whole engine.

Advantages of C++ modules
^^^^^^^^^^^^^^^^^^^^^^^^^

:ref:`C++ modules <doc_custom_modules_in_c++>` are mainly recommended in cases
where GDNative doesn't suffice for the reasons outlined below:

- C++ modules provide deeper integration into the engine. GDNative is more
  limited and can only access what the scripting API exposes (more or less).
- C++ modules can be used to provide additional features in a project without
  having to carry native library files around. This extends to exported projects
  as well.
- C++ modules are supported on all platforms. In contrast, GDNative isn't
  supported on HTML5 and UWP yet.
- C++ modules can be faster than GDNative, especially when lots of communication
  through the scripting API is involved.

Supported languages
-------------------

Official
^^^^^^^^

- C++ :ref:`(tutorial) <doc_gdnative_cpp_example>`
- C :ref:`(tutorial) <doc_gdnative_c_example>`

There are no plans to officially support additional languages with GDNative.
That said, the community offers several bindings for other languages (see
below).

.. _doc_what_is_gdnative_third_party_bindings:

Third-party
^^^^^^^^^^^

The bindings below are developed by the community and are sorted by alphabetical order.

.. Binding developers: Feel free to open a pull request to add your binding
.. if it's well-developed enough to be used in a project.

- `D <https://github.com/godot-d/godot-d>`__
- `Kotlin <https://github.com/utopia-rise/godot-kotlin>`__
- `Nim <https://github.com/pragmagic/godot-nim>`__
- `Python <https://github.com/touilleMan/godot-python>`__
- `Rust <https://github.com/godot-rust/godot-rust>`__

.. note::

    Not all bindings mentioned here may be production-ready. Make sure to
    research options thoroughly before starting a project with one of those
    bindings. Also, double-check whether the binding is compatible with the
    Godot version you're using.
