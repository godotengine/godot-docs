.. _doc_c_sharp_troubleshooting:

C# troubleshooting
==================

This page covers common issues that appear when setting up, building, or
running a C# project in Godot: scripts that are silently ignored because of
their file name, configuration silently overwritten by the editor, build
errors caused by the Godot project's intermediate build directories, and
mismatches between the installed .NET runtime and the project's target
framework.

.. seealso::

    See :doc:`c_sharp_basics` for an introduction to C# in Godot and
    :ref:`doc_c_sharp_diagnostics` for errors reported by Godot's C# analyzers
    during compilation.

.. note::

    The examples on this page were verified with Godot 4.7.2 and the .NET SDK
    10. None of the issues described here are specific to these versions, but
    details such as the exact wording of error messages can vary between
    releases.

.. _doc_c_sharp_troubleshooting_script_file_name:

The script file name must match the class name
----------------------------------------------

**Symptom.** A C# script attached to a node, or used as an autoload, doesn't
run. Running the project prints an error such as:

.. code-block:: none

    ERROR: Failed to instantiate an autoload, script 'res://autoload/game_manager.cs' does not inherit from 'Node'.

    ERROR: Cannot instantiate C# script because the associated class could not be found.
    Make sure the script exists and contains a class definition with a name that matches
    the filename of the script exactly (it's case-sensitive).

**Cause.** Godot's C# source generator only registers a class with the engine
when the file name (without extension) matches the class name exactly,
including the letter case. A file named ``game_manager.cs`` containing a class
named ``GameManager`` looks normal but is silently ignored: no error is
reported at build time, and the class can't be found at runtime.

**Fix.** Rename the file so that it matches the class name:

.. code-block:: shell

    mv autoload/game_manager.cs autoload/GameManager.cs

.. warning::

    The comparison is case-sensitive: ``GameManager.cs`` works, but
    ``gameManager.cs`` or ``game_manager.cs`` do not. Create new C# scripts
    with the editor's **New Script** dialog rather than hand-writing file
    names.

.. note::

    If a class is split across multiple ``partial`` files, only the file whose
    name matches the class name participates in class registration. Keep the
    main class file aligned with the class name, and avoid declaring classes
    in partial files whose names don't match their file names.

.. seealso::

    This rule is also documented for global classes on the
    :ref:`doc_c_sharp_global_classes` page.

.. _doc_c_sharp_troubleshooting_project_godot_overwrite:

External edits to project.godot can be overwritten by the editor
----------------------------------------------------------------

**Symptom.** Changes made with a text editor to ``project.godot`` disappear
after the editor saves the project. For example, an ``[autoload]`` section you
added is gone, and code that relied on the autoload fails at runtime with a
``NullReferenceException``.

**Cause.** While a project is open, the editor keeps its own copy of
``project.godot`` in memory and writes it back to disk whenever the project
settings are saved. Changes made to the file from outside the editor are not
reloaded automatically: the editor may warn that the file changed on disk,
but any save from the editor writes the in-memory copy, discarding the
external changes.

**Fix.** Edit ``project.godot`` only through the editor's **Project Settings**
window. If you need to edit the file with a text editor, close the editor
first, make your changes, then reopen the editor so it reads the updated file.

.. seealso::

    See :ref:`doc_project_settings_manually_editing` for more information on
    editing ``project.godot`` manually.

.. _doc_c_sharp_troubleshooting_build_pollution:

CS0579: duplicate attributes after repeated builds
--------------------------------------------------

**Symptom.** ``dotnet build`` fails with errors pointing at generated files
under ``.godot/mono/temp/obj/``:

.. code-block:: none

    error CS0579: Duplicate 'System.Reflection.AssemblyCompanyAttribute' attribute
    error CS0579: Duplicate 'global::System.Runtime.Versioning.TargetFrameworkAttribute' attribute

**Cause.** A Godot project's default ``**/*.cs`` compile glob includes every
``.cs`` file under the project folder. In a multi-project setup, leftover
generated files from other projects' ``bin/`` or ``obj/`` folders (for
example, a test project's generated ``AssemblyInfo.cs``) can be compiled into
the Godot project, producing its assembly attributes twice. The errors point
at the Godot project's own generated files under ``.godot/mono/temp/obj/``,
even though the duplicated files are the ones swept in from the other
project. Building from the command line while the editor is open makes this
worse, since the editor also builds the project automatically and both
processes write to the same ``.godot/mono/temp/`` directory.

.. note::

    A single Godot project is not affected: the default excludes already
    cover its own ``.godot/mono/temp/`` directory. The problem appears when
    other projects share the same folder structure and their ``bin/`` or
    ``obj/`` folders are inside the Godot project's folder.

**Fix.** Apply one or more of the following, depending on your workflow:

- Close the editor before running ``dotnet build`` from the command line to
  avoid concurrent writes to ``.godot/mono/temp/``. In CI there is no editor,
  so command-line builds are inherently safe.
- In multi-project setups, exclude the other projects' folders from the
  Godot project's default compile glob. A root-level ``Directory.Build.props``
  applies the excludes to every project below it:

  .. code-block:: xml

      <Project>
        <PropertyGroup>
          <DefaultItemExcludes>$(DefaultItemExcludes);tests/**;tools/**;engine/**</DefaultItemExcludes>
        </PropertyGroup>
        <ItemGroup>
          <Compile Remove="tests/**" />
          <Compile Remove="tools/**" />
          <Compile Remove="engine/**" />
        </ItemGroup>
      </Project>

- As a last resort, delete the ``.godot/mono`` folder and let it regenerate.

.. note::

    The exact conditions under which leftover files are re-compiled can differ
    between .NET SDK versions. If the excludes above don't take effect, check
    the behavior documented for the Godot.NET.Sdk version used by your
    project.

.. _doc_c_sharp_troubleshooting_roll_forward:

Test projects fail to run: "You must install or update .NET"
------------------------------------------------------------

**Symptom.** A test or console project targeting ``net8.0`` compiles, but the
test host crashes as soon as it runs:

.. code-block:: none

    Testhost process exited with error: You must install or update .NET to run this application.
    Framework: 'Microsoft.NETCore.App', version '8.0.0' (x64)
    The following frameworks were found: 9.0.19 at [...]

**Cause.** The .NET SDK can compile projects that target an older framework
version than the SDK itself, but running the project requires a runtime that
matches the target framework. By default, the .NET runtime doesn't roll
forward to a newer major version on its own.

**Fix.** In the project that needs to run (for example, the test project),
allow rolling forward to a newer major version:

.. code-block:: xml

    <PropertyGroup>
      <RollForward>LatestMajor</RollForward>
    </PropertyGroup>

.. note::

    ``RollForward`` only affects which *runtime* version is selected. It does
    not change the compile-time target framework: ``<TargetFramework>`` stays
    as-is. Rolling forward to a newer major version can introduce minor API
    behavior differences, so prefer installing the exact runtime in
    production. In CI, pin the SDK with ``global.json`` and install the target
    runtime rather than relying on roll-forward.

.. _doc_c_sharp_troubleshooting_type_ambiguity:

Ambiguous references between Godot types and .NET types
-------------------------------------------------------

**Symptom.** Code using a Godot type fails to compile with an ambiguity error,
for example:

.. code-block:: none

    error CS0104: 'Timer' is an ambiguous reference between 'Godot.Timer' and 'System.Threading.Timer'

**Cause.** C# projects enable implicit usings by default, which includes
``System.Threading``. When the script also imports the ``Godot`` namespace,
types that exist in both namespaces, such as ``Timer``, become ambiguous and
the compiler can't decide for you.

**Fix.** Qualify the type explicitly, both for the field and the constructor:

.. code-block:: csharp

    private Godot.Timer _timer = null!;
    _timer = new Godot.Timer { OneShot = true, WaitTime = 2.0f };

Alternatively, if the project uses ``System`` types heavily, disable implicit
usings and add the ones you need manually:

.. code-block:: xml

    <PropertyGroup>
      <ImplicitUsings>disable</ImplicitUsings>
    </PropertyGroup>

.. note::

    ``Timer.WaitTime`` is a ``double`` in seconds. ``System.Timers.Timer`` and
    ``System.Threading.Timer`` are completely different APIs with a different
    callback model and threading semantics, so don't mix them up.
