.. _doc_c_sharp_exports:

C# Exports
==========

Introduction to exports
-----------------------

In Godot, class members can be exported. This means their value gets saved along
with the resource (such as the :ref:`scene <class_PackedScene>`) they're
attached to. They will also be available for editing in the property editor.
Exporting is done by using the ``[Export]`` attribute.

.. code-block:: csharp

    public class ExportExample : Node3D
    {
        [Export]
        private int Number = 5;
    }

In that example the value ``5`` will be saved, and after building the current project
it will be visible in the property editor. This way, artists and game designers
can modify values that later influence how the program runs. For this, a
special export syntax is provided.

Exporting can only be done with built-in types or objects derived from the :ref:`Resource class <class_Resource>`.

.. note::

    Exporting properties can also be done in GDScript, for information on that
    see :ref:`doc_gdscript_exports`.

Basic use
---------

Exporting can work with and without setting a default value. For int and float
``0`` will then be used as the default.

.. code-block:: csharp

    [Export]
    private int Number;

Export works with resource types.

.. code-block:: csharp

    [Export]
    private Texture CharacterFace;
    [Export]
    private PackedScene SceneFile;

There are many resource types that can be used this way, try e.g.
the following to list them:

.. code-block:: csharp

    [Export]
    private Resource Resource;

..
	Commenting out enum examples because I have been told they
	require extra steps to actually work properly. The examples below
	will show up in the inspector but apparently do not function properly
..
	Integers and strings hint enumerated values.
..
	code-block:: csharp
..
	    // Editor will enumerate as 0, 1 and 2.
	    [Export(PropertyHint.Enum, "Warrior,Magician,Thief")]
	    private int CharacterClass;
..
	If type is String, editor will enumerate with string names.
..
	code-block:: csharp
..
	    [Export(PropertyHint.Enum, "Rebecca,Mary,Leah")]
	    private string CharacterName;
..
	Named enum values
	-----------------
..
	Editor will enumerate as THING_1, THING_2, ANOTHER_THING.
..
	code-block:: csharp
..
	    private enum NamedEnum
	    {
	        Thing1,
	        Thing2,
	        AnotherThing = -1
	    }
	    [Export(PropertyHint.Enum)]
	    private NamedEnum X;

Strings as paths
----------------

Property hints can be used to export strings as paths

String as a path to a file.

.. code-block:: csharp

    [Export(PropertyHint.File)]
    private string GameFile;

String as a path to a directory.

.. code-block:: csharp

    [Export(PropertyHint.Dir)]
    private string GameDirectory;

String as a path to a file, custom filter provided as hint.

.. code-block:: csharp

    [Export(PropertyHint.File, "*.txt,")]
    private string GameFile;

Using paths in the global filesystem is also possible,
but only in scripts in tool mode.

String as a path to a PNG file in the global filesystem.

.. code-block:: csharp

    [Export(PropertyHint.GlobalFile, "*.png")]
    private string ToolImage;

String as a path to a directory in the global filesystem.

.. code-block:: csharp

    [Export(PropertyHint.GlobalDir)]
    private string ToolDir;

The multiline annotation tells the editor to show a large input
field for editing over multiple lines.

.. code-block:: csharp

    [Export(PropertyHint.MultilineText)]
    private string Text;

Limiting editor input ranges
----------------------------

Using the range property hint allows you to limit what can be
input as a value using the editor.

Allow integer values from 0 to 20.

.. code-block:: csharp

    [Export(PropertyHint.Range, "0,20,")]
    private int Number;

Allow integer values from -10 to 20.

.. code-block:: csharp

    [Export(PropertyHint.Range, "-10,20,")]
    private int Number;

Allow floats from -10 to 20 and snap the value to multiples of 0.2.

.. code-block:: csharp

    [Export(PropertyHint.Range, "-10,20,0.2")]
    private float Number;

If you add the hints "or_greater" and/or "or_lesser" you can go above
or below the limits when adjusting the value by typing it instead of using
the slider.

.. code-block:: csharp

    [Export(PropertyHint.Range, "0,100,1,or_greater,or_lesser")]
    private int Number;

Allow values 'y = exp(x)' where 'y' varies between 100 and 1000
while snapping to steps of 20. The editor will present a
slider for easily editing the value. This only works with floats.

.. code-block:: csharp

    [Export(PropertyHint.ExpRange, "100,1000,20")]
    private float Number;

Floats with easing hint
-----------------------

Display a visual representation of the 'ease()' function
when editing.

.. code-block:: csharp

    [Export(PropertyHint.ExpEasing)]
    private float TransitionSpeed;

Colors
------

Regular color given as red-green-blue-alpha value.

.. code-block:: csharp

    [Export]
    private Color Col;

Color given as red-green-blue value (alpha will always be 1).

.. code-block:: csharp

    [Export(PropertyHint.ColorNoAlpha)]
    private Color Col;

Nodes
-----

Nodes can't be directly exported. Instead you need to export
a node path, then use that node path with ``GetNode()``.

.. code-block:: csharp

    [Export]
    private NodePath MyNodePath;
    private Label MyNode;

    public override void _Ready()
    {
        MyNode = GetNode<Label>(MyNodePath);
    }

Resources
---------

.. code-block:: csharp

    [Export]
    private Resource Resource;

In the Inspector, you can then drag and drop a resource file
from the FileSystem dock into the variable slot.

Opening the inspector dropdown may result in an
extremely long list of possible classes to create, however.
Therefore, if you specify an extension of Resource such as:

.. code-block:: csharp

    [Export]
    private AnimationNode Resource;

The drop-down menu will be limited to AnimationNode and all
its inherited classes.

It must be noted that even if the script is not being run while in the
editor, the exported properties are still editable. This can be used
in conjunction with a :ref:`script in "tool" mode <doc_gdscript_tool_mode>`.

Exporting bit flags
-------------------

Integers used as bit flags can store multiple ``true``/``false`` (boolean)
values in one property. By using the ``Flags`` property hint, they
can be set from the editor.

.. code-block:: csharp

    // Set any of the given flags from the editor.
    [Export(PropertyHint.Flags, "Fire,Water,Earth,Wind")]
    private int SpellElements = 0;

You must provide a string description for each flag. In this example, ``Fire``
has value 1, ``Water`` has value 2, ``Earth`` has value 4 and ``Wind``
corresponds to value 8. Usually, constants should be defined accordingly (e.g.
``private const int ElementWind = 8`` and so on).

Export annotations are also provided for the physics and render layers defined in the project settings.

.. code-block:: csharp

    [Export(PropertyHint.Layers2dPhysics)]
    private int Layers2dPhysics;
    [Export(PropertyHint.Layers2dRender)]
    private int Layers2dRender;
    [Export(PropertyHint.Layers3dPhysics)]
    private int layers3dPhysics;
    [Export(PropertyHint.Layers3dRender)]
    private int layers3dRender;

Using bit flags requires some understanding of bitwise operations.
If in doubt, use boolean variables instead.

Exporting arrays
----------------

Exported arrays should be initialized empty.

.. code-block:: csharp

    [Export]
    private Vector3[] Vector3s = new Vector3[0];
    [Export]
    private String[] String = new String[0];


You can omit the default value, but then it would be null if not assigned.

.. code-block:: csharp

    [Export]
    private int[] Numbers;

Arrays with specified types which inherit from resource can be set by
drag-and-dropping multiple files from the FileSystem dock.

.. code-block:: csharp

    [Export]
    private Texture[] Textures;
    [Export]
    private PackedScene[] Scenes;

Arrays where the default value includes run-time values can't
be exported.

.. code-block:: csharp

    private int Number = 1;
    private int[] SeveralNumbers = {Number,2,3};

Setting exported variables from a tool script
---------------------------------------------

When changing an exported variable's value from a script in
:ref:`doc_gdscript_tool_mode`, the value in the inspector won't be updated
automatically. To update it, call
:ref:`notify_property_list_changed() <class_Object_method_notify_property_list_changed>`
after setting the exported variable's value.

Advanced exports
----------------

Not every type of export can be provided on the level of the language itself to
avoid unnecessary design complexity. The following describes some more or less
common exporting features which can be implemented with a low-level API.

Before reading further, you should get familiar with the way properties are
handled and how they can be customized with
:ref:`_set() <class_Object_method__get_property_list>`,
:ref:`_get() <class_Object_method__get_property_list>`, and
:ref:`_get_property_list() <class_Object_method__get_property_list>` methods as
described in :ref:`doc_accessing_data_or_logic_from_object`.

.. seealso:: For binding properties using the above methods in C++, see
             :ref:`doc_binding_properties_using_set_get_property_list`.

.. warning:: The script must operate in the ``tool`` mode so the above methods
             can work from within the editor.
