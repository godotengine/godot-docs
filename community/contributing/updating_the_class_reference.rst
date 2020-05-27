.. _doc_updating_the_class_reference:

Contribute to the Class Reference
=================================

.. highlight:: shell

.. note:: This guide also is available as a `video tutorial on YouTube <https://www.youtube.com/watch?v=5jeHXxeX-JY>`_.

Godot ships with many nodes and singletons to help you develop your games. Each is a class, documented in the :ref:`class reference <toc-class-ref>`.
This reference is essential for anyone learning the engine: it is available both online and in the engine.

But it's incomplete. Some methods, variables and signals lack descriptions. Others changed with recent releases and need updates.
The developers can't write the entire reference on their own. Godot needs you, and all of us, to contribute.

**Important:** If you are planning to make larger changes or a more substantial contribution, it is usually a good idea
to create an issue (or a comment in an existing one) to let others know so they don't start working on the same thing too.

.. seealso::

    Not sure where to start contributing? Take a look at the current class reference
    completion status `here <https://godotengine.github.io/doc-status/>`__.

How to contribute
-----------------

The class reference lies in the following XML files, in Godot's GitHub repository: `doc/classes/ <https://github.com/godotengine/godot/tree/master/doc/classes>`_.

There are 5 steps to update the class reference (full guide below):

1. Fork `Godot's repository <https://github.com/godotengine/godot>`_
2. Clone your fork on your computer
3. Edit the class file in ``doc/classes/`` to write documentation
4. Commit your changes and push them to your fork
5. Make a pull request on the Godot repository

.. warning:: Always use these XML files to edit the API reference. Do not edit the generated .rst files :ref:`in the online documentation <toc-class-ref>`, hosted in the `godot-docs <https://github.com/godotengine/godot-docs>`_ repository.

Get started with GitHub
-----------------------

If you're new to Git and GitHub, this guide will help you get started. You'll learn to:

- Fork and clone Godot's repository
- Keep your fork up to date with other contributors
- Create a pull request so your improvements end in the official docs

.. note:: If you're new to Git, the version control system Godot uses, go through `GitHub's interactive guide <https://try.github.io/levels/1/challenges/1>`_. You'll learn some essential vocabulary and get a sense for the tool.

Fork Godot
~~~~~~~~~~

Fork the Godot Engine into a GitHub repository of your own.

Clone the repository on your computer:

::

    git clone https://github.com/your_name/godot.git

Create a new branch to make your changes. It makes it a lot easier to sync your improvements with other docs writers. It's also easier to clean up your repository if you run into any issues with Git.

::

    git checkout -b your-new-branch-name

The new branch is the same as your master branch, until you start to write API docs. In the ``doc/`` folder, you'll find the class reference.

How to keep your local clone up-to-date
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Other writers contribute to Godot's documentation. Your local repository will fall behind it, and you'll have to synchronize it. Especially if other contributors update the class reference while you work on it.

First add an ``upstream`` git *remote* to work with. Remotes are links to online repositories you can download new files from.

::

    git remote add upstream https://github.com/godotengine/godot

You can check the list of all remote servers with:

::

    git remote -v

You should have two: ``origin``, your fork on GitHub that Git adds by default, and ``upstream``, that you just added:


::

    origin  https://github.com/your_name/godot.git (fetch)
    origin  https://github.com/your_name/godot.git (push)
    upstream        https://github.com/godotengine/godot.git (fetch)
    upstream        https://github.com/godotengine/godot.git (push)

Each time you want to sync your branch to the state of the upstream repository, enter:

::

    git pull --rebase upstream master

This command will first ``fetch``, or download the latest version of the Godot repository. Then, it will reapply your local changes on top.

If you made changes you don't want to keep in your local branch, use the following commands instead:

::

    git fetch upstream
    git reset --hard upstream master

**Warning:** The above command will reset your branch to the state of the ``upstream master`` branch. It will discard all local changes. Make sure to only run this *before* you make important changes.

Another option is to delete the branch you're working on, synchronize the master branch with the Godot repository, and create a new branch:

::

    git checkout master
    git branch -d your-new-branch-name
    git pull --rebase upstream master
    git checkout -b your-new-branch-name

If you're feeling lost by now, come to our `IRC channels <https://webchat.freenode.net/?channels=#godotengine>`_ and ask for help. Experienced Git users will give you a hand.

Updating the documentation template
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When classes are modified in the source code, the documentation template might become outdated. To make sure that you are editing an up-to-date version, you first need to compile Godot (you can follow the :ref:`doc_introduction_to_the_buildsystem` page), and then run the following command (assuming 64-bit Linux):

::

    ./bin/godot.x11.tools.64 --doctool .

The XML files in doc/classes should then be up-to-date with current Godot Engine features. You can then check what changed using the ``git diff`` command. If there are changes to other classes than the one you are planning to document, please commit those changes first before starting to edit the template:

::

    git add doc/classes/*.xml
    git commit -m "Sync classes reference template with current code base"

You are now ready to edit this file to add stuff.

**Note:** If this has been done recently by another contributor, you don't forcefully need to go through these steps (unless you know that the class you plan to edit *has* been modified recently).

Push and request a pull of your changes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once your modifications are finished, push your changes on your GitHub
repository:

::

    git add doc/classes/<edited_file>.xml
    git commit -m "Explain your modifications."
    git push

When it's done, you can ask for a Pull Request via the GitHub UI of your Godot fork.

.. warning::

    Although you can edit files on GitHub, it's not recommended. As hundreds of contributors work on Godot, the Git history must stay clean. Each commit should bundle all related improvements you make to the class reference, a new feature, bug fixes... When you edit from GitHub, it will create a new branch and a Pull Request every time you want to save it. If a few days pass before your changes get a review, you won't be able to update to the latest version of the repository cleanly. Also, it's harder to keep clean indents from GitHub. And they're very important in the docs.

    TL;DR: If you don't know what you're doing exactly, do not edit files from GitHub.

How to edit class XML
---------------------

Edit the file for your chosen class in ``doc/classes/`` to update the class reference. The folder contains an XML file for each class. The XML lists the constants and methods you'll find in the class reference. Godot generates and updates the XML automatically.

Edit it using your favorite text editor. If you use a code editor, make sure that it doesn't change the indent style: tabs for the XML, and 4 spaces inside BBcode-style blocks. More on that below.

If you need to check that the modifications you've made are correct in the generated documentation, build Godot as described :ref:`here <toc-devel-compiling>`, run the editor and open the help for the page you modified.

How to write the class reference
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Each class has a brief and a long description. The brief description is always at the top of the page, while the full description lies below the list of methods, variables and constants. Methods, member variables, constants and signals are in separate categories or XML nodes. For each, learn how they work in Godot's source code, and fill their <description>.

Our job is to add the missing text between these marks:

-  <description></description>
-  <brief_description></brief_description>
-  <constant></constant>
-  <method></method>
-  <member></member>
-  <signal></signal>

Write in a clear and simple language. Always follow the :ref:`writing guidelines <doc_docs_writing_guidelines>` to keep your descriptions short and easy to read. **Do not leave empty lines** in the descriptions: each line in the XML file will result in a new paragraph.

Here's how a class looks like in XML:

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


Use a code editor like Vim, Atom, Code, Notepad++ or anything similar to edit the file quickly. Use the search function to find classes fast.


Improve formatting with BBcode style tags
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Godot's class reference supports BBcode-like tags. They add nice formatting to the text. Here's the list of available tags:

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

Use ``[codeblock]`` for pre-formatted code blocks. Inside ``[codeblock]``, always use **four spaces** for indentation (the parser will delete tabs). Example:

.. code-block:: none

    [codeblock]
    func _ready():
        var sprite = get_node("Sprite")
        print(sprite.get_pos())
    [/codeblock]

Will display as:

.. code-block:: gdscript

    func _ready():
        var sprite = get_node("Sprite")
        print(sprite.get_pos())


I don't know what this method does!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No problem. Leave it behind, and list the methods you skipped when you request a pull of your changes. Another writer will take care of it.

You can still have a look at the methods' implementation in Godot's source code on GitHub. Also, if you have doubts, feel free to ask on the `Q&A website <https://godotengine.org/qa/>`__ and on IRC (freenode, #godotengine).


Localization
~~~~~~~~~~~~

The documentation can be translated in any language on `Hosted Weblate
<https://hosted.weblate.org/projects/godot-engine/godot-docs/>`__.

Translated strings are synced manually by documentation maintainers in
the `godot-docs-l10n <https://github.com/godotengine/godot-docs-l10n>`__
repository.

Languages with a good level of completion have their own localized
instances of ReadTheDocs. Open an issue on the ``godot-docs-l10n``
repository if you think that a new language is complete enough to get
its own instance.
