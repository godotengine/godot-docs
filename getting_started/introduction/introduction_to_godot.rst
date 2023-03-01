.. _doc_introduction_to_godot:

Introduction to Godot
=====================

This article is here to help you figure out whether Godot might be a good fit
for you. We will introduce some broad features of the engine to give you a feel
for what you can achieve with it and answer questions such as "what do I need to
know to get started?".

This is by no means an exhaustive overview. We will introduce many more features
in this getting started series.

What is Godot?
--------------

Godot is a general-purpose 2D and 3D game engine designed to support all sorts
of projects. You can use it to create games or applications you can then release
on desktop or mobile, as well as on the web.

You can also create console games with it, although you either need strong
programming skills or a developer to port the game for you.

.. note:: The Godot team can't provide an open-source console export due to the
          licensing terms imposed by console manufacturers. Regardless of the
          engine you use, though, releasing games on consoles is always a lot of
          work. You can read more on that here: :ref:`doc_consoles`.

What can the engine do?
-----------------------

Godot was initially developed in-house by an Argentinian game studio. Its
development started in 2001, and the engine was rewritten and improved
tremendously since its open-source release in 2014.

Some examples of games created with Godot include Ex-Zodiac and Helms of Fury.

.. image:: img/introduction_ex_zodiac.png

.. image:: img/introduction_helms_of_fury.jpg

As for applications, the open-source pixel art drawing program Pixelorama is
powered by Godot, and so is the voxel RPG creator RPG in a box.

.. image:: img/introduction_rpg_in_a_box.png

You can find many more examples in the `official showcase videos`_.

How does it work and look?
--------------------------

Godot comes with a fully-fledged game editor with integrated tools to answer the
most common needs. It includes a code editor, an animation editor, a tilemap
editor, a shader editor, a debugger, a profiler, and more.

.. image:: img/introduction_editor.png

The team strives to offer a feature-rich game editor with a consistent user
experience. While there is always room for improvement, the user interface keeps
getting refined.

Of course, if you prefer, you can work with external programs. We officially
support importing 3D scenes designed in Blender_ and maintain plugins to code in
VSCode_ and Emacs_ for GDScript and C#. We also support Visual Studio for C# on
Windows.

.. image:: img/introduction_vscode.png

Programming languages
---------------------

Let's talk about the available programming languages.

You can code your games using :ref:`GDScript <toc-learn-scripting-gdscript>`, a
Godot-specific and tightly integrated language with a lightweight syntax, or
:ref:`C# <toc-learn-scripting-C#>`, which is popular in the games industry.
These are the two main scripting languages we support.

Godot also supports a node-based visual programming language named
:ref:`VisualScript <toc-learn-scripting-visual_script>`.

With the :ref:`GDNative <toc-tutorials-gdnative>` technology, you can also write
gameplay or high-performance algorithms in C or C++ without recompiling the
engine. You can use this technology to integrate third-party libraries and other
Software Development Kits (SDK) in the engine.

Of course, you can also directly add modules and features to the engine, as it's
completely free and open-source.

.. seealso:: These are the five officially supported programming languages. The
             community maintains support for many more. For more information,
             see :ref:`GDNative third-party bindings
             <doc_what_is_gdnative_third_party_bindings>`.

What do I need to know to use Godot?
------------------------------------

Godot is a feature-packed game engine. With its thousands of features, there is
a lot to learn. To make the most of it, you need good programming foundations.
While we try to make the engine accessible, you will benefit a lot from knowing
how to think like a programmer first.

In the next part, we'll show you a free and open-source app you can use to learn
the basics of programming with Godot's GDScript programming language.

.. _Blender: https://www.blender.org/
.. _VSCode: https://github.com/godotengine/godot-vscode-plugin
.. _Emacs: https://github.com/godotengine/emacs-gdscript-mode
.. _official showcase videos: https://www.youtube.com/playlist?list=PLeG_dAglpVo6EpaO9A1nkwJZOwrfiLdQ8
