.. _doc_class_reference_primer:

Class reference primer
======================

This page explains how to write the class reference. You will learn where to
write new descriptions for the classes, methods, and properties for Godot's
built-in node types.

.. seealso::

    To learn to submit your changes to the Godot project using the Git version
    control system, see :ref:`doc_updating_the_class_reference`.

The reference for each class is contained in an XML file like the one below:

.. code-block:: xml

    <class name="Node2D" inherits="CanvasItem" version="4.0">
        <brief_description>
            A 2D game object, inherited by all 2D-related nodes. Has a position, rotation, scale, and Z index.
        </brief_description>
        <description>
            A 2D game object, with a transform (position, rotation, and scale). All 2D nodes, including physics objects and sprites, inherit from Node2D. Use Node2D as a parent node to move, scale and rotate children in a 2D project. Also gives control of the node's render order.
        </description>
        <tutorials>
            <link title="Custom drawing in 2D">https://docs.godotengine.org/en/latest/tutorials/2d/custom_drawing_in_2d.html</link>
            <link title="All 2D Demos">https://github.com/godotengine/godot-demo-projects/tree/master/2d</link>
        </tutorials>
        <methods>
            <method name="apply_scale">
                <return type="void">
                </return>
                <argument index="0" name="ratio" type="Vector2">
                </argument>
                <description>
                    Multiplies the current scale by the [code]ratio[/code] vector.
                </description>
            </method>
            [...]
            <method name="translate">
                <return type="void">
                </return>
                <argument index="0" name="offset" type="Vector2">
                </argument>
                <description>
                    Translates the node by the given [code]offset[/code] in local coordinates.
                </description>
            </method>
        </methods>
        <members>
            <member name="global_position" type="Vector2" setter="set_global_position" getter="get_global_position">
                Global position.
            </member>
            [...]
            <member name="z_index" type="int" setter="set_z_index" getter="get_z_index" default="0">
                Z index. Controls the order in which the nodes render. A node with a higher Z index will display in front of others.
            </member>
        </members>
        <constants>
        </constants>
    </class>


It starts with brief and long descriptions. In the generated docs, the brief
description is always at the top of the page, while the long description lies
below the list of methods, variables, and constants. You can find methods,
member variables, constants, and signals in separate XML nodes.

For each, you want to learn how they work in Godot's source code. Then, fill
their documentation by completing or improving the text in these tags:

- `<brief_description>`
- `<description>`
- `<constant>`
- `<method>` (in its `<description>` tag; return types and arguments don't take separate
  documentation strings)
- `<member>`
- `<signal>` (in its `<description>` tag; arguments don't take separate documentation strings)
- `<constant>`

Write in a clear and simple language. Always follow the :ref:`writing guidelines
<doc_docs_writing_guidelines>` to keep your descriptions short and easy to read.
**Do not leave empty lines** in the descriptions: each line in the XML file will
result in a new paragraph, even if it is empty.

.. _doc_class_reference_editing_xml:

How to edit class XML
---------------------

Edit the file for your chosen class in ``doc/classes/`` to update the class
reference. The folder contains an XML file for each class. The XML lists the
constants and methods you will find in the class reference. Godot generates and
updates the XML automatically.

.. note:: For some modules in the engine's source code, you'll find the XML
          files in the ``modules/<module_name>/doc_classes/`` directory instead.

Edit it using your favorite text editor. If you use a code editor, make sure
that it doesn't change the indent style: you should use tabs for the XML and
four spaces inside BBCode-style blocks. More on that below.

To check that the modifications you've made are correct in the generated
documentation, navigate to the ``doc/`` folder and run the command ``make rst``.
This will convert the XML files to the online documentation's format and output
errors if anything's wrong.

Alternatively, you can build Godot and open the modified page in the built-in
code reference. To learn how to compile the engine, read the :ref:`compilation
guide <toc-devel-compiling>`.

We recommend using a code editor that supports XML files like Vim, Atom, Visual Studio Code,
Notepad++, or another to comfortably edit the file. You can also use their
search feature to find classes and properties quickly.

.. tip::

    If you use Visual Studio Code, you can install the
    `vscode-xml extension <https://marketplace.visualstudio.com/items?itemName=redhat.vscode-xml>`__
    to get linting for class reference XML files.

.. _doc_class_reference_bbcode:

Improve formatting with BBCode style tags
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Godot's XML class reference supports BBCode-like tags for linking as well as formatting text and code.
In the tables below you can find the available tags, usage examples and the results after conversion to reStructuredText.

Linking
"""""""

Whenever you link to a member of another class, you need to specify the class name.
For links to the same class, the class name is optional and can be omitted.

+-------------------------------+-----------------------------------------+----------------------------------------------------------------------+
| Tag and Description           | Example                                 | Result                                                               |
+===============================+=========================================+======================================================================+
| | ``[Class]``                 | ``Move the [Sprite2D].``                | Move the :ref:`class_Sprite2D`.                                      |
| | Link to class               |                                         |                                                                      |
+-------------------------------+-----------------------------------------+----------------------------------------------------------------------+
| | ``[annotation Class.name]`` | ``See [annotation @GDScript.@export].`` | See :ref:`@GDScript.@export <class_@GDScript_annotation_@export>`.   |
| | Link to annotation          |                                         |                                                                      |
+-------------------------------+-----------------------------------------+----------------------------------------------------------------------+
| | ``[constant Class.name]``   | ``See [constant @GlobalScope.KEY_F1].`` | See :ref:`@GlobalScope.KEY_F1 <class_@GlobalScope_constant_KEY_F1>`. |
| | Link to constant            |                                         |                                                                      |
+-------------------------------+-----------------------------------------+----------------------------------------------------------------------+
| | ``[enum Class.name]``       | ``See [enum Mesh.ArrayType].``          | See :ref:`Mesh.ArrayType <enum_Mesh_ArrayType>`.                     |
| | Link to enum                |                                         |                                                                      |
+-------------------------------+-----------------------------------------+----------------------------------------------------------------------+
| | ``[method Class.name]``     | ``Call [method Node3D.hide].``          | Call :ref:`Node3D.hide() <class_Node3D_method_hide>`.                |
| | Link to method              |                                         |                                                                      |
+-------------------------------+-----------------------------------------+----------------------------------------------------------------------+
| | ``[member Class.name]``     | ``Get [member Node2D.scale].``          | Get :ref:`Node2D.scale <class_Node2D_property_scale>`.               |
| | Link to member              |                                         |                                                                      |
+-------------------------------+-----------------------------------------+----------------------------------------------------------------------+
| | ``[signal Class.name]``     | ``Emit [signal Node.renamed].``         | Emit :ref:`Node.renamed <class_Node_signal_renamed>`.                |
| | Link to signal              |                                         |                                                                      |
+-------------------------------+-----------------------------------------+----------------------------------------------------------------------+
| | ``[theme_item Class.name]`` | ``See [theme_item Label.font].``        | See :ref:`Label.font <class_Label_theme_font_font>`.                 |
| | Link to theme item          |                                         |                                                                      |
+-------------------------------+-----------------------------------------+----------------------------------------------------------------------+

.. note::

    Currently only :ref:`class_@GDScript` has annotations.

Formatting text
"""""""""""""""

+--------------------------------------+--------------------------------------+------------------------------+
| Tag and Description                  | Example                              | Result                       |
+======================================+======================================+==============================+
| | ``[param name]``                   | ``Takes [param size] for the size.`` | Takes ``size`` for the size. |
| | Formats a parameter name (as code) |                                      |                              |
+--------------------------------------+--------------------------------------+------------------------------+
| | ``[br]``                           | | ``Line 1.[br]``                    | | Line 1.                    |
| | Line break                         | | ``Line 2.``                        | | Line 2.                    |
+--------------------------------------+--------------------------------------+------------------------------+
| | ``[b]`` ``[/b]``                   | ``Some [b]bold[/b] text.``           | Some **bold** text.          |
| | Bold                               |                                      |                              |
+--------------------------------------+--------------------------------------+------------------------------+
| | ``[i]`` ``[/i]``                   | ``Some [i]italic[/i] text.``         | Some *italic* text.          |
| | Italic                             |                                      |                              |
+--------------------------------------+--------------------------------------+------------------------------+
| | ``[kbd]`` ``[/kbd]``               | ``Some [kbd]Ctrl + C[/kbd] key.``    | Some :kbd:`Ctrl + C` key.    |
| | Keyboard/mouse shortcut            |                                      |                              |
+--------------------------------------+--------------------------------------+------------------------------+

Formatting code
"""""""""""""""

+----------------------------------------+---------------------------------------+--------------------------+
| Tag and Description                    | Example                               | Result                   |
+========================================+=======================================+==========================+
| | ``[code]`` ``[/code]``               | ``Some [code]monospace[/code] text.`` | Some ``monospace`` text. |
| | Monospace                            |                                       |                          |
+----------------------------------------+---------------------------------------+--------------------------+
| | ``[codeblock]`` ``[/codeblock]``     | *See below.*                          | *See below.*             |
| | Multiline preformatted block         |                                       |                          |
+----------------------------------------+---------------------------------------+--------------------------+
| | ``[codeblocks]`` ``[/codeblocks]``   | *See below.*                          | *See below.*             |
| | Codeblock for multiple languages     |                                       |                          |
+----------------------------------------+---------------------------------------+--------------------------+
| | ``[gdscript]`` ``[/gdscript]``       | *See below.*                          | *See below.*             |
| | GDScript codeblock tab in codeblocks |                                       |                          |
+----------------------------------------+---------------------------------------+--------------------------+
| | ``[csharp]`` ``[/csharp]``           | *See below.*                          | *See below.*             |
| | C# codeblock tab in codeblocks       |                                       |                          |
+----------------------------------------+---------------------------------------+--------------------------+

.. note::

    1. ``[code]`` disables BBCode until the parser encounters ``[/code]``.
    2. ``[codeblock]`` disables BBCode until the parser encounters ``[/codeblock]``.

.. warning::

    Use ``[codeblock]`` for pre-formatted code blocks. Inside ``[codeblock]``,
    always use **four spaces** for indentation. The parser will delete tabs.

For example:

.. code-block:: none

    [codeblock]
    func _ready():
        var sprite = get_node("Sprite2D")
        print(sprite.get_pos())
    [/codeblock]

Will display as:

.. code-block:: gdscript

    func _ready():
        var sprite = get_node("Sprite2D")
        print(sprite.get_pos())

If you need to have different code version in GDScript and C#, use
``[codeblocks]`` instead. If you use ``[codeblocks]``, you also need to have at
least one of the language-specific tags, ``[gdscript]`` and ``[csharp]``.

Always write GDScript code examples first! You can use this `experimental code
translation tool <https://github.com/HaSa1002/codetranslator>`_ to speed up your
workflow.

.. code-block:: none

    [codeblocks]
    [gdscript]
    func _ready():
        var sprite = get_node("Sprite2D")
        print(sprite.get_pos())
    [/gdscript]
    [csharp]
    public override void _Ready()
    {
        var sprite = GetNode("Sprite2D");
        GD.Print(sprite.GetPos());
    }
    [/csharp]
    [/codeblocks]

The above will display as:

.. tabs::
 .. code-tab:: gdscript GDScript

    func _ready():
        var sprite = get_node("Sprite2D")
        print(sprite.get_pos())

 .. code-tab:: csharp

    public override void _Ready()
    {
        var sprite = GetNode("Sprite2D");
        GD.Print(sprite.GetPos());
    }

To denote important information, add a paragraph starting with "[b]Note:[/b]" at
the end of the description:

.. code-block:: none

    [b]Note:[/b] Only available when using the Vulkan renderer.

To denote crucial information that could cause security issues or loss of data
if not followed carefully, add a paragraph starting with "[b]Warning:[/b]" at
the end of the description:

.. code-block:: none

    [b]Warning:[/b] If this property is set to [code]true[/code], it allows clients to execute arbitrary code on the server.

For deprecated properties, add a paragraph starting with "[i]Deprecated.[/i]".
Notice the use of italics instead of bold:

.. code-block:: none

    [i]Deprecated.[/i] This property has been replaced by [member other_property].

In all the paragraphs described above, make sure the punctuation is part of the
BBCode tags for consistency.
