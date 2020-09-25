.. _doc_class_reference_writing_guidelines:

Class reference writing guidelines
==================================

This page explains how to write the class reference. You will learn where to
write new descriptions for the classes, methods, and properties for Godot's
built-in node types.

.. seealso::

    To learn to submit your changes to the Godot project using the Git version
    control system, see :ref:`doc_updating_the_class_reference`.

Each class's reference is contained in an XML file like the one below:

.. code-block:: xml

    <class name="Node2D" inherits="CanvasItem" category="Core">
        <brief_description>
            Base node for 2D system.
        </brief_description>
        <description>
            Base node for 2D system. Node2D contains a position, rotation and scale, which is used to position and animate. It can alternatively be used with a custom 2D transform ([Matrix32]). A tree of Node2Ds allows complex hierarchies for animation and positioning.
        </description>
        <methods>
            <method name="set_pos">
                <argument index="0" name="pos" type="Vector2">
                </argument>
                <description>
                    Sets the position of the 2D node.
                </description>
            </method>
            [...]
            <method name="edit_set_pivot">
                <argument index="0" name="arg0" type="Vector2">
                </argument>
                <description>
                </description>
            </method>
        </methods>
        <members>
            <member name="global_position" type="Vector2" setter="set_global_position" getter="get_global_position" brief="">
            </member>
            [...]
            <member name="z_as_relative" type="bool" setter="set_z_as_relative" getter="is_z_relative" brief="">
            </member>
        </members>
        <constants>
        </constants>
    </class>


It starts with brief and long descriptions. In the generated docs, the brief
description is always at the top of the page, while the long description lies
below the list of methods, variables, and constants. You can find methods,
member variables, constants, and signals in separate XML nodes. For each, learn
how they work in Godot's source code, and fill their <description> tag.

Our job is to complete or improve the text in these tags:

- <description></description>
- <brief_description></brief_description>
- <constant></constant>
- <method></method>
- <member></member>
- <signal></signal>

Write in a clear and simple language. Always follow the :ref:`writing guidelines
<doc_docs_writing_guidelines>` to keep your descriptions short and easy to read.
**Do not leave empty lines** in the descriptions: each line in the XML file will
result in a new paragraph, even if it is empty.

How to edit class XML
---------------------

Edit the file for your chosen class in ``doc/classes/`` to update the class
reference. The folder contains an XML file for each class. The XML lists the
constants and methods you will find in the class reference. Godot generates and
updates the XML automatically.

Edit it using your favorite text editor. If you use a code editor, make sure
that it doesn't change the indent style: you should use tabs for the XML, and
four spaces inside BBCode-style blocks. More on that below.

To check that the modifications you've made are correct in the
generated documentation, you need to build Godot. To learn how, read the
:ref:`compilation guide <toc-devel-compiling>`. Then, run the editor and open
the help for the page you modified.

We recommend using a code editor that supports XML files like Vim, Atom, Code,
Notepad++, or another to comfortably edit the file. You can also use their
search feature to find classes and properties quickly.

.. _doc_updating_the_class_reference_bbcode:

Improve formatting with BBCode style tags
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Godot's class reference supports BBCode-like tags. They add nice formatting to
the text. Here's the list of available tags:

+---------------------------+--------------------------------+-----------------------------------+---------------------------------------------------+
| Tag                       | Effect                         | Usage                             | Result                                            |
+===========================+================================+===================================+===================================================+
| [Class]                   | Link a class                   | Move the [Sprite].                | Move the :ref:`class_sprite`.                     |
+---------------------------+--------------------------------+-----------------------------------+---------------------------------------------------+
| [method methodname]       | Link to a method in this class | Call [method hide].               | See :ref:`hide <class_spatial_method_hide>`.      |
+---------------------------+--------------------------------+-----------------------------------+---------------------------------------------------+
| [method Class.methodname] | Link to another class's method | Call [method Spatial.hide].       | See :ref:`hide <class_spatial_method_hide>`.      |
+---------------------------+--------------------------------+-----------------------------------+---------------------------------------------------+
| [member membername]       | Link to a member in this class | Get [member scale].               | Get :ref:`scale <class_node2d_property_scale>`.   |
+---------------------------+--------------------------------+-----------------------------------+---------------------------------------------------+
| [member Class.membername] | Link to another class's member | Get [member Node2D.scale].        | Get :ref:`scale <class_node2d_property_scale>`.   |
+---------------------------+--------------------------------+-----------------------------------+---------------------------------------------------+
| [signal signalname]       | Link to a signal in this class | Emit [signal renamed].            | Emit :ref:`renamed <class_node_signal_renamed>`.  |
+---------------------------+--------------------------------+-----------------------------------+---------------------------------------------------+
| [signal Class.signalname] | Link to another class's signal | Emit [signal Node.renamed].       | Emit :ref:`renamed <class_node_signal_renamed>`.  |
+---------------------------+--------------------------------+-----------------------------------+---------------------------------------------------+
| [b] [/b]                  | Bold                           | Some [b]bold[/b] text.            | Some **bold** text.                               |
+---------------------------+--------------------------------+-----------------------------------+---------------------------------------------------+
| [i] [/i]                  | Italic                         | Some [i]italic[/i] text.          | Some *italic* text.                               |
+---------------------------+--------------------------------+-----------------------------------+---------------------------------------------------+
| [code] [/code]            | Monospace                      | Some [code]monospace[/code] text. | Some ``monospace`` text.                          |
+---------------------------+--------------------------------+-----------------------------------+---------------------------------------------------+
| [kbd] [/kbd]              | Keyboard/mouse shortcut        | Some [kbd]Ctrl + C[/kbd] key.     | Some :kbd:`Ctrl + C` key.                         |
+---------------------------+--------------------------------+-----------------------------------+---------------------------------------------------+
| [codeblock] [/codeblock]  | Multiline preformatted block   | *See below.*                      | *See below.*                                      |
+---------------------------+--------------------------------+-----------------------------------+---------------------------------------------------+

Use ``[codeblock]`` for pre-formatted code blocks. Inside ``[codeblock]``,
always use **four spaces** for indentation. The parser will delete tabs. For
example:

.. code-block:: none

    [codeblock] func _ready(): var sprite = get_node("Sprite")
    print(sprite.get_pos()) [/codeblock]

Will display as:

.. code-block:: gdscript

    func _ready(): var sprite = get_node("Sprite") print(sprite.get_pos())

To denote important information, add a paragraph starting with "[b]Note:[/b]" at
the end of the description:

.. code-block:: none

    [b]Note:[/b] Only available when using the Vulkan renderer.

To denote crucial information that could cause security issues or loss of data
if not followed carefully, add a paragraph starting with "[b]Warning:[/b]" at
the end of the description:

.. code-block:: none

    [b]Warning:[/b] If this property is set to [code]true[/code], it allows
    clients to execute arbitrary code on the server.

For deprecated properties, add a paragraph starting with "[i]Deprecated.[/i]".
Notice the use of italics instead of bold:

.. code-block:: none

    [i]Deprecated.[/i] This property has been replaced by [member
    other_property].

In all the paragraphs described above, make sure the punctuation is part of the
BBCode tags for consistency.

I don't know what this method does!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No problem. Leave it behind, and list the methods you skipped when you request a
pull of your changes. Another writer will take care of it.

You can still look at the methods' implementation in Godot's source code on
GitHub. If you have doubts, feel free to ask on the `Q&A website
<https://godotengine.org/qa/>`__ and IRC (Freenode, #godotengine).
