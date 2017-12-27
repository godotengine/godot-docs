.. _doc_c_sharp:

C#
===

Introduction
--------------

C# is a high-level programming language developed by Microsoft. In Godot it is implemented with the Mono 5.2 .NET framework including full support for C# 7.0.   

.. note:: This is **not** a full-scale tutorial on the C# language as a whole.
        If you aren't already familiar with its syntax or features,
        see the `Microsoft C# guide <https://docs.microsoft.com/en-us/dotnet/csharp/index>`_.

Necessary Downloads
-------------------------

To use C# in Godot you must have `Mono <http://www.mono-project.com/download/>`_
installed (at least version 5.2), and use a Godot version with Mono enabled, which adds C# support next to the existing options of GDScript, visual scripting and C++.

Windows users also need MS Build 15.0, which comes bundled with Visual Studio 2017,
or can be downloaded separately with `build tools for Visual Studio 2017 <https://www.visualstudio.com/thank-you-downloading-visual-studio/?sku=BuildTools&rel=15#>`_.


History
--------

Back in 2016 the Godot team reached out to Microsoft, with Miguel de Icaza's 
support, to see if they would consider funding C# support being added to 
Godot. Microsoft agreed and gave the team a $24,000 donation to work on adding
C# support. Thanks to that donation, Juan Lineietsky and Ignacio Roldán 
Etcheverry were able to work on bringing C# support to Godot using the Mono 
.NET framework. Support was added to Godot version 3.0 using mono 5.2, giving users 
the power of C# in their game making.

Example
-------

Here's a blank C# script with some comments to demonstate how it works. 

.. code-block:: csharp

    using Godot;
    using System;

    public class Path : Path
    {
        // Member variables here, example:
        private int a = 2;
        private string b = "textvar";

        public override void _Ready()
        {
            // Called every time the node is added to the scene.
            // Initialization here
        }

        public override void _Process(float delta)
        {
            // Called every frame. Delta is time since last frame.
            // Update game logic here.
        }
    }


Configuring an external editor
-----------------------------------

While Godot does have its own scripting editor, its support for C# is kept
minimal, and it's reccomended that you use an external IDE or editor, such as
Microsoft Visual Studio Code, or MonoDevelop, which provide auto-completion,
debugging and other features useful when working with C#.
To set it up, in Godot click on ``Editor``, then ``Editor Settings``. Scroll 
down to the bottom, to the ``Mono`` settings. Under Mono click on ``Editor``,
and on that page choose your external editor of choice.