.. _doc_c_sharp:

Introduction
============

.. warning:: C# support is a new feature in Godot 3.0.
             As such, you may still run into some issues, or find spots where the documentation could be improved.
             Please report issues with C# in Godot on the `engine Github page <https://github.com/godotengine/godot/issues>`_.
             And any documentation issues on the `documentation Github Page <https://github.com/godotengine/godot-docs/issues>`_.

This page provides a brief intro to C#, both what it is and how to use it in Godot.
Afterwards, you may want to look at :ref:`how to use specific features <doc_c_sharp_features>`,
read about the :ref:`differences between the C# and the GDScript API <doc_c_sharp_differences>`
and (re)visit the :ref:`Scripting section <doc_scripting>` of the step-by-step tutorial.

C# is a high-level programming language developed by Microsoft. In Godot it is implemented with the Mono 5.2 .NET framework including full support for C# 7.0.
Mono is an open source implementation of Microsoft's .NET Framework based on the ECMA standards for C# and the Common Language Runtime.
A good starting point for checking its capabilities is the `Compatibility <http://www.mono-project.com/docs/about-mono/compatibility/>`_ page in the Mono documentation.

.. note:: This is **not** a full-scale tutorial on the C# language as a whole.
        If you aren't already familiar with its syntax or features,
        see the `Microsoft C# guide <https://docs.microsoft.com/en-us/dotnet/csharp/index>`_ or look for a suitable introduction elsewhere.

Setup C# for Godot
------------------

To use C# in Godot you must have `Mono <http://www.mono-project.com/download/>`_ installed (at least version 5.2), as well 
as MSBuild (at least version 15.0) which should come with the Mono installation. 

Additionally, your Godot version must have Mono support enabled, so take care to download the **Mono version** of Godot.
If you are building Godot from source, make sure to follow the steps to include Mono support in your build outlined on the  :ref:`doc_compiling_with_mono` page.

Configuring an external editor
------------------------------

While Godot does have its own scripting editor, its support for C# is kept
minimal, and it's recommended that you use an external IDE or editor, such as
Microsoft Visual Studio Code, or MonoDevelop, which provide auto-completion,
debugging and other features useful when working with C#.
To set it up, in Godot click on ``Editor``, then ``Editor Settings``. Scroll 
down to the bottom, to the ``Mono`` settings. Under Mono click on ``Editor``,
and on that page choose your external editor of choice.

Creating a C# script
--------------------

After you successfully setup C# for Godot, you should see the following option when selecting ``Attach script`` in the context menu of a node in your scene:

.. image:: img/attachcsharpscript.png

Note that while some specifics change, most of the things work the same when using C# for scripting.
If you're new to Godot, you may want to peruse the tutorials on :ref:`doc_scripting` at this point.
While some places in the documentation still lack C# examples, most things can be transferred easily from GDScript.

Project setup and workflow
--------------------------

When you create the first C# script, Godot initializes the C# project files for your Godot project.
This includes generating a C# solution (``.sln``) and project (``.csproj``) as well as some utility files and folders (``.mono``, sometimes ``Properties``).
All of these but ``.mono`` are important and should be kept in your version control system. ``.mono`` can be safely added to the ignore list of your VCS.
When troubleshooting, it sometimes can help to delete the ``.mono`` folder and let it regenerate.

Note that currently there are some issues where the Godot and the C# project don't stay in sync; if you delete, rename or move things like scripts or nodes, they may no longer match up.
In this case, it can help to edit the solution files manually.

Example: If you created a script (e.g. ``Test.cs``) and delete it in Godot, compilation will fail because the now missing file is still expected to be there by the CS project.
You can for now simply open up the ``.csproj`` and look for the ``ItemGroup``, there should be a line included like the following:

.. code-block:: xml
   :emphasize-lines: 2

    <ItemGroup>
        <Compile Include="Test.cs" />``
        <Compile Include="AnotherTest.cs" />``
    </ItemGroup>

Simply remove that line and your project should now again build fine. Same for renaming and moving things, simply rename and move them in the project file if needed.

Example
-------

Here's a blank C# script with some comments to demonstrate how it works. 

.. code-block:: csharp

    using Godot;
    using System;

    public class YourCustomClass : Node
    {
        // Member variables here, example:
        private int a = 2;
        private string b = "textvar";

        public override void _Ready()
        {
            // Called every time the node is added to the scene.
            // Initialization here
            GD.Print("Hello from C# to Godot :)");
        }

        public override void _Process(float delta)
        {
            // Called every frame. Delta is time since last frame.
            // Update game logic here.
        }
    }

As you can see, the things normally in global scope in GDScript like Godot's ``print`` function are available in the ``GD`` namespace.
For a list of those, see the class reference pages for :ref:`@GDScript <class_@gdscript>` and :ref:`@GlobalScope <class_@globalscope>`.

.. note::
    Keep in mind that the class you wish to attach to your node should be named as the ``.cs`` file.
    If not, you will get the following error and won't be able to run the scene: ``Cannot find class XXX for script res://XXX.cs``.

General differences between C# and GDScript
-------------------------------------------

The C# API uses ``PascalCase`` instead of ``snake_case`` in GDScript/C++.
Where possible, fields and getters/setters have been converted to properties.
In general, the C# Godot API strives to be as idiomatic as is reasonably possible.

For more, see the :ref:`doc_c_sharp_differences` page.

Current gotchas and known issues
--------------------------------

As C# support is quite new to Godot, there are some growing pains and things that still need to be ironed out.
Below is a list of the most important issues you should be aware of when diving into C# in Godot, but if in doubt also take a look over the official `issue tracker for Mono issues <https://github.com/godotengine/godot/labels/topic%3Amono>`_.

- As explained above, the C# project isn't always kept in sync automatically when things are deleted, renamed or moved in Godot (`#12917 <https://github.com/godotengine/godot/issues/12917>`_)
- Writing editor plugins and tool scripts in C# is not yet supported
- Exporting a project may not yet work (`#15615 <https://github.com/godotengine/godot/issues/15615>`_)
- Signals with parameters are broken in 3.0.2-stable (`#17553 <https://github.com/godotengine/godot/issues/17553>`_)

Performance of C# in Godot
--------------------------

According to some preliminary `benchmarks <https://github.com/cart/godot3-bunnymark>`_, performance of C# in Godot - while generally in the same order of magnitude - is roughly **~4x** that of GDScript in some naive cases.
For full performance, C++ is still a little faster; the specifics are going to vary according to your use case. GDScript is likely fast enough for most general scripting workloads.
C# is faster, but requires some expensive marshalling when talking to Godot.
