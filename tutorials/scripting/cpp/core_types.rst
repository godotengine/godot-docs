.. _doc_godot_cpp_core_types:

Core functions and types
========================

godot-cpp's API is designed to be as similar as possible to Godot's internal API.

This means that, in general, you can use the :ref:`Engine details <doc_engine_architecture>` section to learn how to
work with godot-cpp. In addition, it can often be useful to browse the `engine's code <https://github.com/godotengine/godot>`__
for examples for how to work with Godot's API.

That being said, there are some differences to be aware of, which are documented here.

Common functions and macros
---------------------------

Please refer to :ref:`doc_common_engine_methods_and_macros` for information on this. The functions and macros documented
there are also available in godot-cpp.

Core types
----------

Godot's :ref:`Core types <doc_core_types>` are also available in godot-cpp, and the same recommendations apply
as described in that article. The types are regularly synchronized with the Godot codebase.

In your own code, you can also use `C++ STL types <https://en.cppreference.com/w/cpp/container.html>`__, or types from
any library you choose, but they won't be compatible with Godot's APIs.

Packed arrays
~~~~~~~~~~~~~

While in Godot, the ``Packed*Array`` types are aliases of ``Vector``, in godot-cpp, they're their own types, using the
Godot bindings. This is because these types, along with their methods, are exposed through the GDExtension interface,
which would not be compatible with the templated nature of ``Vector``.

In general though, the ``Packed*Array`` types work the same way as their ``Vector`` aliases. However, you should be
aware that the ``Variant`` wrappers for ``Packed*Array`` treat them as pass-by-reference, while the ``Packed*Array``
types themselves are pass-by-value (implemented as copy-on-write).

In addition, it may be of interest that GDScript calls use the ``Variant`` call interface: Any ``Packed*Array``
arguments to your functions will be passed in a ``Variant``, and unpacked from there. This can create copies of the
types, so the argument you receive may be a copy of the argument that the function was called with. In practice, this
means you cannot rely on that the argument passed to you can be modified at the caller's site.

Variant class
-------------

Please refer to :ref:`doc_variant_class` to learn about how to work with ``Variant``.

Most importantly, you should be aware that all functions exposed through the GDExtension API must be compatible with
``Variant``.

Object class
------------

Please refer to :ref:`doc_object_class` to learn how to register and work with your own ``Object`` types.

We are not aware of any major differences between the godot-cpp ``Object`` API and Godot's internal ``Object`` API,
except that some methods are available in Godot's internal API that are not available in godot-cpp.

You should be aware that the pointer to your godot-cpp ``Object`` is different from the pointer that Godot uses
internally. This is because the godot-cpp version is an extension instance, allocated separately from the original
``Object``. However, in practice, this difference is usually not noticeable.
