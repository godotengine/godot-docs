.. _doc_gdscript_exports:

GDScript exported properties
============================

In Godot, class members can be exported. This means their value gets saved along
with the resource (such as the :ref:`scene <class_PackedScene>`) they're
attached to. They will also be available for editing in the property editor.
Exporting is done by using the ``@export`` annotation.

::

    @export var number: int = 5

In that example the value ``5`` will be saved and visible in the property editor.

An exported variable must be initialized to a constant expression or have a type specifier
in the variable. Some of the export annotations have a specific type and don't need the variable to be typed (see the
*Examples* section below).

One of the fundamental benefits of exporting member variables is to have
them visible and editable in the editor. This way, artists and game designers
can modify values that later influence how the program runs. For this, a
special export syntax is provided.

.. note::

    Exporting properties can also be done in other languages such as C#.
    The syntax varies depending on the language. See :ref:`doc_c_sharp_exports`
    for information on C# exports.

Basic use
---------

If the exported value assigns a constant or constant expression,
the type will be inferred and used in the editor.

::

    @export var number = 5

If there's no default value, you can add a type to the variable.

::

    @export var number: int

Resources and nodes can be exported.

::

    @export var resource: Resource
    @export var node: Node

Even if a script is not executed in the editor, exported properties
can still be edited. However, getters and setters will only be used
if the script is in :ref:`doc_gdscript_tool_mode`.

Grouping Exports
----------------

It is possible to group your exported properties inside the Inspector
with the :ref:`@export_group <class_@GDScript_annotation_@export_group>`
annotation. Every exported property after this annotation will be added to
the group. Start a new group or use ``@export_group("")`` to break out.

::

    @export_group("My Properties")
    @export var number = 3

The second argument of the annotation can be used to only group properties
with the specified prefix.

Groups cannot be nested, use :ref:`@export_subgroup <class_@GDScript_annotation_@export_subgroup>`
to create subgroups within a group.

::

    @export_subgroup("Extra Properties")
    @export var string = ""
    @export var flag = false

You can also change the name of your main category, or create additional
categories in the property list with the :ref:`@export_category <class_@GDScript_annotation_@export_category>`
annotation.

::

    @export_category("Main Category")
    @export var number = 3
    @export var string = ""

    @export_category("Extra Category")
    @export var flag = false

.. note::

    The list of properties is organized based on the class inheritance and
    new categories break that expectation. Use them carefully, especially
    when creating projects for public use.

Strings as paths
----------------

String as a path to a file.

::

    @export_file var f

String as a path to a directory.

::

    @export_dir var f

String as a path to a file, custom filter provided as hint.

::

    @export_file("*.txt") var f

Using paths in the global filesystem is also possible,
but only in scripts in tool mode.

String as a path to a PNG file in the global filesystem.

::

    @export_global_file("*.png") var tool_image

String as a path to a directory in the global filesystem.

::

    @export_global_dir var tool_dir

The multiline annotation tells the editor to show a large input
field for editing over multiple lines.

::

    @export_multiline var text

Limiting editor input ranges
----------------------------

Allow integer values from 0 to 20.

::

    @export_range(0, 20) var i

Allow integer values from -10 to 20.

::

    @export_range(-10, 20) var j

Allow floats from -10 to 20 and snap the value to multiples of 0.2.

::

    @export_range(-10, 20, 0.2) var k: float

The limits can be only for the slider if you add the hints "or_greater" and/or "or_less".

::

    @export_range(0, 100, 1, "or_greater", "or_less")

.. TODO: Document other hint strings usable with export_range.

Floats with easing hint
-----------------------

Display a visual representation of the 'ease()' function
when editing.

::

    @export_exp_easing var transition_speed

Colors
------

Regular color given as red-green-blue-alpha value.

::

    @export var col: Color

Color given as red-green-blue value (alpha will always be 1).

::

    @export_color_no_alpha var col: Color

Nodes
-----

Since Godot 4.0, nodes can be directly exported as properties in a script
without having to use NodePaths:

::

    # Allows any node.
    @export var node: Node

    # Allows any node that inherits from BaseButton.
    # Custom classes declared with `class_name` can also be used.
    @export var some_button: BaseButton

Exporting NodePaths like in Godot 3.x is still possible, in case you need it:

::

    @export var node_path: NodePath
    var node = get_node(node_path)

If you want to limit the types of nodes for NodePaths, you can use the
:ref:`@export_node_path<class_@GDScript_annotation_@export_node_path>`
annotation:

::

    @export_node_path("Button", "TouchScreenButton") var some_button

Resources
---------

::

    @export var resource: Resource

In the Inspector, you can then drag and drop a resource file
from the FileSystem dock into the variable slot.

Opening the inspector dropdown may result in an
extremely long list of possible classes to create, however.
Therefore, if you specify an extension of Resource such as:

::

    @export var resource: AnimationNode

The drop-down menu will be limited to AnimationNode and all
its derived classes.

Exporting bit flags
-------------------

Integers used as bit flags can store multiple ``true``/``false`` (boolean)
values in one property. By using the ``@export_flags`` annotation, they
can be set from the editor::

    # Set any of the given flags from the editor.
    @export_flags("Fire", "Water", "Earth", "Wind") var spell_elements = 0

You must provide a string description for each flag. In this example, ``Fire``
has value 1, ``Water`` has value 2, ``Earth`` has value 4 and ``Wind``
corresponds to value 8. Usually, constants should be defined accordingly (e.g.
``const ELEMENT_WIND = 8`` and so on).

You can add explicit values using a colon::

    @export_flags("Self:4", "Allies:8", "Foes:16") var spell_targets = 0

Only power of 2 values are valid as bit flags options. The lowest allowed value
is 1, as 0 means that nothing is selected. You can also add options that are a
combination of other flags::

    @export_flags("Self:4", "Allies:8", "Self and Allies:12", "Foes:16")
    var spell_targets = 0

Export annotations are also provided for the physics, render, and navigation layers defined in the project settings::

    @export_flags_2d_physics var layers_2d_physics
    @export_flags_2d_render var layers_2d_render
    @export_flags_2d_navigation var layers_2d_navigation
    @export_flags_3d_physics var layers_3d_physics
    @export_flags_3d_render var layers_3d_render
    @export_flags_3d_navigation var layers_3d_navigation

Using bit flags requires some understanding of bitwise operations.
If in doubt, use boolean variables instead.

Exporting enums
---------------

Properties can be exported with a type hint referencing an enum to limit their values
to the values of the enumeration. The editor will create a widget in the Inspector, enumerating
the following as "Thing 1", "Thing 2", "Another Thing". The value will be stored as an integer.

::

    enum NamedEnum {THING_1, THING_2, ANOTHER_THING = -1}
    @export var x: NamedEnum

Integer and string properties can also be limited to a specific list of values using
the :ref:`@export_enum <class_@GDScript_annotation_@export_enum>` annotation.
The editor will create a widget in the Inspector, enumerating the following as Warrior,
Magician, Thief. The value will be stored as an integer, corresponding to the index
of the selected option (i.e. ``0``, ``1``,  or ``2``).

::

    @export_enum("Warrior", "Magician", "Thief") var character_class: int

You can add explicit values using a colon::

    @export_enum("Slow:30", "Average:60", "Very Fast:200") var character_speed: int

If the type is String, the value will be stored as a string.

::

    @export_enum("Rebecca", "Mary", "Leah") var character_name: String

If you want to set an initial value, you must specify it explicitly::

    @export_enum("Rebecca", "Mary", "Leah") var character_name: String = "Rebecca"

Exporting arrays
----------------

Exported arrays can have initializers, but they must be constant expressions.

If the exported array specifies a type which inherits from Resource, the array
values can be set in the inspector by dragging and dropping multiple files
from the FileSystem dock at once.

The default value **must** be a constant expression.

::

    @export var a = [1, 2, 3]

Exported arrays can specify type (using the same hints as before).

::

    @export var ints: Array[int] = [1, 2, 3]

    # Nested typed arrays such as `Array[Array[float]]` are not supported yet.
    @export var two_dimensional: Array[Array] = [[1.0, 2.0], [3.0, 4.0]]

You can omit the default value, but it would then be ``null`` if not assigned.

::

    @export var b: Array
    @export var scenes: Array[PackedScene]

Arrays with specified types which inherit from resource can be set by
drag-and-dropping multiple files from the FileSystem dock.

::

    @export var textures: Array[Texture] = []
    @export var scenes: Array[PackedScene] = []

Packed type arrays also work, but only initialized empty:

::

    @export var vector3s = PackedVector3Array()
    @export var strings = PackedStringArray()

Other export variants can also be used when exporting arrays:

::

    @export_range(-360, 360, 0.001, "radians") var laser_angles: Array[float] = []
    @export_file("*.json") var skill_trees: Array[String] = []
    @export_color_no_alpha var hair_colors = PackedColorArray()
    @export_enum("Espresso", "Mocha", "Latte", "Capuccino") var barista_suggestions: Array[String] = []

``@export_storage``
-------------------

By default, exporting a property has two effects:

1. makes the property stored in the scene/resource file (:ref:`PROPERTY_USAGE_STORAGE <class_@GlobalScope_constant_PROPERTY_USAGE_STORAGE>`);
2. adds a field to the Inspector (:ref:`PROPERTY_USAGE_EDITOR <class_@GlobalScope_constant_PROPERTY_USAGE_EDITOR>`).

However, sometimes you may want to make a property serializable, but not display it
in the editor to prevent unintentional changes and cluttering the interface.

To do this you can use :ref:`@export_storage <class_@GDScript_annotation_@export_storage>`.
This can be useful for :ref:`@tool <class_@GDScript_annotation_@tool>` scripts.
Also the property value is copied when :ref:`Resource.duplicate() <class_Resource_method_duplicate>`
or :ref:`Node.duplicate() <class_Node_method_duplicate>` is called, unlike non-exported variables.

::

    var a # Not stored in the file, not displayed in the editor.
    @export_storage var b # Stored in the file, not displayed in the editor.
    @export var c: int # Stored in the file, displayed in the editor.

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
:ref:`_set() <class_Object_private_method__set>`,
:ref:`_get() <class_Object_private_method__get>`, and
:ref:`_get_property_list() <class_Object_private_method__get_property_list>` methods as
described in :ref:`doc_accessing_data_or_logic_from_object`.

.. seealso:: For binding properties using the above methods in C++, see
             :ref:`doc_binding_properties_using_set_get_property_list`.

.. warning:: The script must operate in the ``@tool`` mode so the above methods
             can work from within the editor.
