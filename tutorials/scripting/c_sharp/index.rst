:allow_comments: False

.. _doc_c_sharp:

C#/.NET
=======

C# is a high-level programming language developed by Microsoft. Godot supports
C# as an option for a scripting language, alongside Godot's own
:ref:`GDScript <doc_gdscript>`.

The standard Godot executable does not contain C# support out of the box. Instead,
to enable C# support for your project you need to `download a .NET version <https://godotengine.org/download/>`_
of the editor from the Godot website.

.. toctree::
   :maxdepth: 1
   :name: toc-learn-scripting-C#

   c_sharp_basics
   c_sharp_features
   c_sharp_style_guide
   diagnostics/index

Godot API for C#
----------------

As a general purpose game engine Godot offers some high-level features as a part
of its API. Articles below explain how these features integrate into C# and how
C# API may be different from GDScript.

.. toctree::
   :maxdepth: 1
   :name: toc-learn-scripting-C#-differences

   c_sharp_differences
   c_sharp_collections
   c_sharp_variant
   c_sharp_signals
   c_sharp_exports
   c_sharp_global_classes

.. _doc_c_sharp_platforms:

C# platform support
-------------------

.. seealso::

    See :ref:`doc_system_requirements` for hardware and software version
    requirements for the Godot engine.

.. note::

    Since C# projects use the .NET runtime, also check the system requirements
    for the version of .NET that you'll be using.
    See `supported OS <https://github.com/dotnet/core/tree/main/release-notes#supported-os>`_.

Since Godot 4.2, projects written in C# support all desktop platforms (Windows, Linux,
and macOS), as well as Android and iOS.

Android support is currently experimental.

iOS support is currently experimental and has a few limitations.

- The official export templates for the iOS simulator only supports the ``x64`` architecture.

- Exporting to iOS can only be done from a MacOS device.

Currently, projects written in C# cannot be exported to the web platform. To use C#
on that platform, consider Godot 3 instead.
