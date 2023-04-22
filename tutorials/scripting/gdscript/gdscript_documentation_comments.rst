.. _doc_gdscript_documentation_comments:

GDScript documentation comments
===============================

In GDScript, comments can be used to document your code and add description to the
members of a script. There are two differences between a normal comment and a documentation
comment. Firstly, a documentation comment should start with double hash symbols
``##``. Secondly, it must immediately precede a script member, or for script descriptions,
be placed at the top of the script. If an exported variable is documented,
its description is used as a tooltip in the editor. This documentation can be
generated as XML files by the editor.

Documenting a script
--------------------

Comments documenting a script must come before any member documentation. A
suggested format for script documentation can be divided into three parts.

- A brief description of the script.
- Detailed description.
- Tutorials.

To separate these from each other, the documentation comments use special tags.
The tag must be at the beginning of a line (ignoring preceding white space) and has
the format ``@``, followed by the keyword and finishing with a colon.

Tags
~~~~

+-------------------+--------------------------------------------------------+
| Brief description | No tag and lives at the very beginning of              |
|                   | the documentation section.                             |
+-------------------+--------------------------------------------------------+
| Description       | Use one blank line to separate the description from    |
|                   | the brief.                                             |
+-------------------+--------------------------------------------------------+
| Tutorial          | ``@tutorial[( The Title Here )]:``                     |
|                   |                                                        |
+-------------------+--------------------------------------------------------+

**Example:**

::

    extends Node2D

    ## A brief description of your script.
    ##
    ## A more detailed description of the script.
    ##
    ## @tutorial:            https://the/tutorial1/url.com
    ## @tutorial(Tutorial2): https://the/tutorial2/url.com

.. warning:: If there is any space in between the tag name and colon, for example
             ``@tutorial  :``, it won't be treated as a valid tag and will be ignored.

.. note:: When the description spans multiple lines, the preceding and trailing white
          spaces will be stripped and joined with a single space. To preserve the line
          break use ``[br]``. See also `BBCode and class reference`_ below.

Documenting script members
--------------------------

Documentation of a script member must immediately precede the member or its
annotations if it has any. The exception to this is enum values whose description should
be on the same line as the enum for readability.
The description can have more than one line but every line must start
with the double hash symbol ``##`` to be considered as part of the documentation.
The script documentation will update in the editor help window every time the
script is updated. If any member variable or function name starts with an
underscore it will be treated as private. It will not appear in the documentation and
will be ignored in the help window.

Members that are applicable for the documentation:

- Inner class
- Constant
- Function
- Signal
- Variable
- Enum
- Enum value

Examples
--------

::

    extends Node2D

    ## A brief description of your script.
    ##
    ## The description of the script, what it can do,
    ## and any further detail.
    ##
    ## @tutorial:            https://the/tutorial1/url.com
    ## @tutorial(Tutorial2): https://the/tutorial2/url.com

    ## The description of the variable v1.
    var v1

    ## This is a multi line description of the variable v2. The type
    ## information below will be extracted for the documentation.
    var v2: int

    ## If the member has any annotation, the annotation should
    ## immediately precede it.
    @export
    @onready
    var v3 := some_func()

    ## The description of a constant.
    const GRAVITY = 9.8

    ## The description of a signal.
    signal my_signal

    ## This is a description of the below enums. Note below that
    ## the enum values are documented on the same line as the enum.
    enum Direction {
        UP    = 0,  ## Direction up.
        DOWN  = 1,  ## Direction down.
        LEFT  = 2,  ## Direction left.
        RIGHT = 3,  ## Direction right.
    }

    ## As the following function is documented, even though its name starts with
    ## an underscore, it will appear in the help window.
    func _fn(p1: int, p2: String) -> int:
        return 0

    # The below function isn't documented and its name starts with an underscore
    # so it will treated as private and will not be shown in the help window.
    func _internal() -> void:
        pass

    ## Documenting an inner class.
    ##
    ## The same rules apply apply here. The documentation must
    ## immediately precede the class definition.
    ##
    ## @tutorial: https://the/tutorial/url.com
    class Inner:

        ## Inner class variable v4.
        var v4

        ## Inner class function fn.
        func fn(): pass


BBCode and class reference
--------------------------

The editor help window which renders the documentation supports :ref:`bbcode <doc_bbcode_in_richtextlabel>`.
As a result it's possible to align and format the documentation. Color texts, images, fonts, tables,
URLs, animation effects, etc. can be added with the :ref:`bbcode <doc_bbcode_in_richtextlabel>`.

Godot's class reference supports BBCode-like tags. They add nice formatting to the text which could also
be used in the documentation. See also :ref:`class reference bbcode <doc_class_reference_bbcode>`.
Here's the list of available tags:

+---------------------------+--------------------------------+-------------------------------------+-------------------------------------------------------------------------+
| Tag                       | Effect                         | Usage                               | Result                                                                  |
+===========================+================================+=====================================+=========================================================================+
| [Class]                   | Link a class                   | Move the [Sprite2D].                | Move the :ref:`class_Sprite2D`.                                         |
+---------------------------+--------------------------------+-------------------------------------+-------------------------------------------------------------------------+
| [annotation name]         | Link to an annotation in this  | See                                 | See                                                                     |
|                           | class                          | [annotation @export].               | :ref:`@GDScript.@export<class_@GDScript_annotation_@export>`.           |
+---------------------------+--------------------------------+-------------------------------------+-------------------------------------------------------------------------+
| [annotation Class.name]   | Link to another class's        | See                                 | See                                                                     |
|                           | annotation, many default       | [annotation @GDScript.@export].     | :ref:`@GDScript.@export<class_@GDScript_annotation_@export>`.           |
|                           | annotations are in             |                                     |                                                                         |
|                           | ``@GDScript``                  |                                     |                                                                         |
+---------------------------+--------------------------------+-------------------------------------+-------------------------------------------------------------------------+
| [constant name]           | Link to a constant in this     | See                                 | See                                                                     |
|                           | class                          | [constant KEY_ESCAPE].              | :ref:`@GlobalScope.KEY_ESCAPE<class_@GlobalScope_constant_KEY_ESCAPE>`. |
+---------------------------+--------------------------------+-------------------------------------+-------------------------------------------------------------------------+
| [constant Class.name]     | Link to another class's        | See                                 | See                                                                     |
|                           | constant                       | [constant @GlobalScope.KEY_ESCAPE]. | :ref:`@GlobalScope.KEY_ESCAPE<class_@GlobalScope_constant_KEY_ESCAPE>`. |
+---------------------------+--------------------------------+-------------------------------------+-------------------------------------------------------------------------+
| [enum enumname]           | Link to an enum in this class  | See [enum ArrayType].               | See :ref:`ArrayType <enum_Mesh_ArrayType>`.                             |
+---------------------------+--------------------------------+-------------------------------------+-------------------------------------------------------------------------+
| [enum Class.enumname]     | Link to another class's enum   | See [enum Mesh.ArrayType].          | See :ref:`ArrayType <enum_Mesh_ArrayType>`.                             |
+---------------------------+--------------------------------+-------------------------------------+-------------------------------------------------------------------------+
| [method methodname]       | Link to a method in this class | Call [method hide].                 | Call :ref:`hide <class_Node3D_method_hide>`.                            |
+---------------------------+--------------------------------+-------------------------------------+-------------------------------------------------------------------------+
| [method Class.methodname] | Link to another class's method | Call [method Node3D.hide].          | Call :ref:`hide <class_Node3D_method_hide>`.                            |
+---------------------------+--------------------------------+-------------------------------------+-------------------------------------------------------------------------+
| [member membername]       | Link to a member in this class | Get [member scale].                 | Get :ref:`scale <class_Node2D_property_scale>`.                         |
+---------------------------+--------------------------------+-------------------------------------+-------------------------------------------------------------------------+
| [member Class.membername] | Link to another class's member | Get [member Node2D.scale].          | Get :ref:`scale <class_Node2D_property_scale>`.                         |
+---------------------------+--------------------------------+-------------------------------------+-------------------------------------------------------------------------+
| [signal signalname]       | Link to a signal in this class | Emit [signal renamed].              | Emit :ref:`renamed <class_node_signal_renamed>`.                        |
+---------------------------+--------------------------------+-------------------------------------+-------------------------------------------------------------------------+
| [signal Class.signalname] | Link to another class's signal | Emit [signal Node.renamed].         | Emit :ref:`renamed <class_node_signal_renamed>`.                        |
+---------------------------+--------------------------------+-------------------------------------+-------------------------------------------------------------------------+
| [br]                      | Line break                     | | Line 1.[br]                       | | Line 1.                                                               |
|                           |                                | | Line 2.                           | | Line 2.                                                               |
+---------------------------+--------------------------------+-------------------------------------+-------------------------------------------------------------------------+
| [b] [/b]                  | Bold                           | Some [b]bold[/b] text.              | Some **bold** text.                                                     |
+---------------------------+--------------------------------+-------------------------------------+-------------------------------------------------------------------------+
| [i] [/i]                  | Italic                         | Some [i]italic[/i] text.            | Some *italic* text.                                                     |
+---------------------------+--------------------------------+-------------------------------------+-------------------------------------------------------------------------+
| [code] [/code]            | Monospace                      | Some [code]monospace[/code] text.   | Some ``monospace`` text.                                                |
+---------------------------+--------------------------------+-------------------------------------+-------------------------------------------------------------------------+
| [kbd] [/kbd]              | Keyboard/mouse shortcut        | Some [kbd]Ctrl + C[/kbd] key.       | Some :kbd:`Ctrl + C` key.                                               |
+---------------------------+--------------------------------+-------------------------------------+-------------------------------------------------------------------------+
| [codeblock] [/codeblock]  | Multiline preformatted block   | *See below.*                        | *See below.*                                                            |
+---------------------------+--------------------------------+-------------------------------------+-------------------------------------------------------------------------+

.. warning:: Use ``[codeblock]`` for pre-formatted code blocks. Inside
             ``[codeblock]``, always use **four spaces** for indentation
             (the parser will delete tabs).

::

    ## The do_something method for this plugin. before using the
    ## method you first have to initialize [MyPlugin].
    ## see : [method initialize]
    ## [color=yellow]Warning:[/color] always [method clean] after use.
    ## Usage:
    ##     [codeblock]
    ##     func _ready():
    ##         the_plugin.initialize()
    ##         the_plugin.do_something()
    ##         the_plugin.clean()
    ##     [/codeblock]
    func do_something():
        pass
