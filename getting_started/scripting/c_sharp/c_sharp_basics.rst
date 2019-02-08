.. _doc_c_sharp:

Introduction
============

.. warning:: C# support is a new feature available since Godot 3.0.
             As such, you may still run into some issues, or find spots
             where the documentation could be improved.
             Please report issues with C# in Godot on the
             `engine GitHub page <https://github.com/godotengine/godot/issues>`_,
             and any documentation issues on the
             `documentation GitHub page <https://github.com/godotengine/godot-docs/issues>`_.

This page provides a brief introduction to C#, both what it is and
how to use it in Godot. Afterwards, you may want to look at
:ref:`how to use specific features <doc_c_sharp_features>`, read about the
:ref:`differences between the C# and the GDScript API <doc_c_sharp_differences>`
and (re)visit the :ref:`Scripting section <doc_scripting>` of the
step-by-step tutorial.

C# is a high-level programming language developed by Microsoft. In Godot,
it is implemented with the Mono 5.x .NET framework, including full support
for C# 7.0. Mono is an open source implementation of Microsoft's .NET Framework
based on the ECMA standards for C# and the Common Language Runtime.
A good starting point for checking its capabilities is the
`Compatibility <http://www.mono-project.com/docs/about-mono/compatibility/>`_
page in the Mono documentation.

.. note:: This is **not** a full-scale tutorial on the C# language as a whole.
        If you aren't already familiar with its syntax or features,
        see the
        `Microsoft C# guide <https://docs.microsoft.com/en-us/dotnet/csharp/index>`_
        or look for a suitable introduction elsewhere.

Setting up C# for Godot
-----------------------

Windows
~~~~~~~

Download and install the latest version of
`Visual Studio <https://visualstudio.microsoft.com/downloads/>`_
(*not* Visual Studio Code), which contains utilities required to use
C# in Godot. If you don't plan on using the Visual Studio IDE,
you can download just the
`Visual Studio Build Tools <https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=BuildTools&rel=15>`_
instead.

macOS and Linux
~~~~~~~~~~~~~~~

Download and install the latest version of the
`Mono SDK <http://www.mono-project.com/download/>`_. As of Godot 3.1 beta 3,
the version number doesn't matter since Godot bundles its own Mono 5.18
installation. We only need the Mono installation for NuGet and MSBuild
which are required to use C# in Godot.

.. note:: To download Mono on macOS, use the "Stable Channel" link
          from the `Mono Downloads Page <http://www.mono-project.com/download/>`_.
          The Visual Studio channel is an earlier version of Mono and
          will not work.

Additional notes
~~~~~~~~~~~~~~~~

Your Godot version must have Mono support enabled,
so make sure to download the **Mono version** of Godot.
If you are building Godot from source, make sure to follow the steps to
enable Mono support in your build as outlined in the
:ref:`doc_compiling_with_mono` page.

In summary, you must have installed Visual Studio or Mono (depending
on your operating system) **and** the Mono-enabled version of Godot.

Configuring an external editor
------------------------------

While Godot has its own script editor, its support for C# is kept
minimal; it's recommended that you use an external IDE or editor
instead, such as `Visual Studio Code <https://code.visualstudio.com/>`_
or MonoDevelop. These provide auto-completion, debugging and other features
useful when working with C#. To set it up in Godot, click on
**Editor → Editor Settings** and scroll down to the bottom to the
**Mono** settings. Under **Mono**, click on **Editor** then choose
your external editor of choice.

.. note:: If you are using Visual Studio Code, ensure you download and install
          the `C# extension <https://marketplace.visualstudio.com/items?itemName=ms-vscode.csharp>`_
          to enable features like syntax highlighting and IntelliSense.

Creating a C# script
--------------------

After you successfully set up C# for Godot, you should see the following option
when selecting ``Attach script`` in the context menu of a node in your scene:

.. image:: img/attachcsharpscript.png

Note that while some specifics change, most concepts work the same
when using C# for scripting. If you're new to Godot, you may want to follow
the tutorials on :ref:`doc_scripting` at this point.
While some places in the documentation still lack C# examples, most concepts
can be transferred easily from GDScript.

Project setup and workflow
--------------------------

When you create the first C# script, Godot initializes the C# project files
for your Godot project. This includes generating a C# solution (``.sln``)
and a project file (``.csproj``), as well as some utility files and folders
(``.mono`` and ``Properties/AssemblyInfo.cs``).
All of these but ``.mono`` are important and should be committed to your
version control system. ``.mono`` can be safely added to the ignore list of your VCS.
When troubleshooting, it can sometimes help to delete the ``.mono`` folder
and let it regenerate.

Note that currently, there are some issues where Godot and the C# project
don't stay in sync; if you delete, rename or move a C# script, the change
may not be reflected in the C# project file.
In cases like this, you will have to edit the C# project file manually.

For example, if you created a script (e.g. ``Test.cs``) and delete it in Godot,
compilation will fail because the missing file is still expected to be there
by the C# project file. For now, you can simply open up the ``.csproj`` file
and look for the ``ItemGroup``, there should be a line included
like the following:

.. code-block:: xml
    :emphasize-lines: 2

    <ItemGroup>
        <Compile Include="Test.cs" />
        <Compile Include="AnotherTest.cs" />
    </ItemGroup>

Simply remove that line and your project should build correctly again.
Same for renaming and moving things, simply rename and move them
in the project file if needed.

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
            // Initialization here.
            GD.Print("Hello from C# to Godot :)");
        }

        public override void _Process(float delta)
        {
            // Called every frame. Delta is time since the last frame.
            // Update game logic here.
        }
    }

As you can see, functions normally in global scope in GDScript like Godot's
``print`` function are available in the ``GD`` class which is part of
the ``Godot`` namespace. For a list of methods in the ``GD`` class, see the
class reference pages for
:ref:`@GDScript <class_@gdscript>` and :ref:`@GlobalScope <class_@globalscope>`.

.. note::
    Keep in mind that the class you wish to attach to your node should be
    named as the ``.cs`` file. Otherwise, you will get the following error
    and won't be able to run the scene:
    *"Cannot find class XXX for script res://XXX.cs"*

General differences between C# and GDScript
-------------------------------------------

The C# API uses ``PascalCase`` instead of ``snake_case`` in GDScript/C++.
Where possible, fields and getters/setters have been converted to properties.
In general, the C# Godot API strives to be as idiomatic as is reasonably possible.

For more information, see the :ref:`doc_c_sharp_differences` page.

Current gotchas and known issues
--------------------------------

As C# support is quite new in Godot, there are some growing pains and things
that need to be ironed out. Below is a list of the most important issues
you should be aware of when diving into C# in Godot, but if in doubt, also
take a look over the official
`issue tracker for Mono issues <https://github.com/godotengine/godot/labels/topic%3Amono>`_.

- As explained above, the C# project isn't always kept in sync automatically
  when things are deleted, renamed or moved in Godot
  (`#12917 <https://github.com/godotengine/godot/issues/12917>`_).
- Writing editor plugins is possible, but it is currently quite convoluted.
- State is currently not saved and restored when hot-reloading,
  with the exception of exported variables.
- Exporting Mono projects is only supported for desktop platforms
  (Linux, Windows and macOS). Android, iOS, HTML5 and UWP are not currently supported
  (`#20267 <https://github.com/godotengine/godot/issues/20267>`_,
  `#20268 <https://github.com/godotengine/godot/issues/20268>`_
  `#20270 <https://github.com/godotengine/godot/issues/20270>`_
  `#20271 <https://github.com/godotengine/godot/issues/20271>`_).
- Attached C# scripts should refer to a class that has a class name
  that matches the file name.

Performance of C# in Godot
--------------------------

According to some preliminary `benchmarks <https://github.com/cart/godot3-bunnymark>`_,
the performance of C# in Godot — while generally in the same order of magnitude
— is roughly **~4×** that of GDScript in some naive cases. C++ is still
a little faster; the specifics are going to vary according to your use case.
GDScript is likely fast enough for most general scripting workloads.
C# is faster, but requires some expensive marshalling when talking to Godot.

Using NuGet packages in Godot
-----------------------------

`NuGet <https://www.nuget.org/>`_ packages can be installed and used with Godot,
as with any C# project. Many IDEs are able to add packages directly.
They can also be added manually by adding the package reference in
the ``.csproj`` file located in the project root:

.. code-block:: xml
    :emphasize-lines: 2

        <ItemGroup>
            <PackageReference Include="Newtonsoft.Json" Version="11.0.2"/>
        </ItemGroup>
        ...
    </Project>


Whenever packages are added or modified, run ``nuget restore`` in the root of the
project directory. To ensure that NuGet packages will be available for
msbuild to use, run:

.. code-block:: none

    msbuild /t:restore
