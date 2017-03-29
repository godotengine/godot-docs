.. _doc_updating_the_class_reference:

Updating the class reference
============================

Godot Engine provides an extensive panel of nodes and singletons that you can
use with GDScript to develop your games. All those classes are listed and
documented in the :ref:`class reference <toc-class-ref>`, which is available
both in the online documentation and offline from within the engine.

The class reference is however not 100% complete. Some methods, constants and
signals have not been described yet, while others may have their implementation
changed and thus need an update. Updating the class reference is a tedious work
and the responsibility of the community: if we all partake in the effort, we
can fill in the blanks and ensure a good documentation level in no time!

**Important notes:**

-  To coordinate the effort and have an overview of the current status, we use
   `a collaborative pad <https://etherpad.net/p/godot-classref-status>`_. Please
   follow the instructions there to notify the other documentation writers about
   what you are working on.
-  We aim at completely filling the class reference in English
   first. Once it nears 90-95% completion, we could start thinking about
   localisating in other languages.

Workflow for updating the class reference
-----------------------------------------

The source file of the class reference is an XML file in the main Godot source
repository on GitHub, `doc/base/classes.xml <https://github.com/godotengine/godot/blob/master/doc/base/classes.xml>`_.
As of now, it is relatively heavy (more than 1 MB), so it can't be edited online
using GitHub's text editor.

The workflow to update the class reference is therefore:

-  Fork the `upstream repository <https://github.com/godotengine/godot>`_ and clone
   your fork.
-  Edit the ``doc/base/classes.xml`` file, commit your changes and push to your
   fork.
-  Make a pull request on the upstream repository.

The following section details this workflow, and gives also additional information
about how to synchronise the XML template with the current state of the source code,
or what should be the formatting of the added text.

**Important:** The class reference is also :ref:`available in the online documentation <toc-class-ref>`,
which is hosted alongside the rest of the documentation in the
`godot-docs <https://github.com/godotengine/godot-docs>`_ git repository. The rST files
should however **not be edited directly**, they are generated via a script from the
``doc/base/classes.xml`` file described above.

Getting started with GitHub
---------------------------

This section describes step-by-step the typical workflow to fork the git repository,
or update an existing local clone of your fork, and then prepare a pull request.

Fork Godot Engine
~~~~~~~~~~~~~~~~~

First of all, you need to fork the Godot Engine on your own GitHub
repository.

You will then need to clone the master branch of Godot Engine in order
to work on the most recent version of the engine, including all of its
features.

::

    git clone https://github.com/your_name/godot.git

Then, create a new git branch that will contain your changes.

::

    git checkout -b classref-edit

The branch you just created is identical to current master branch of
Godot Engine. It already contains a ``doc/`` folder, with the current
state of the class reference. Note that you can set whatever name
you want for the branch, ``classref-edit`` is just an example.

Keeping your local clone up-to-date
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you already have a local clone of your own fork, it might happen
pretty fast that it will diverge with the upstream git repository.
For example other contributors might have updated the class reference
since you last worked on it, or your own commits might have been squashed
together when merging your pull request, and thus appear as diverging
from the upstream master branch.

To keep your local clone up-to-date, you should first add an ``upstream``
git *remote* to work with:

::

    git remote add upstream https://github.com/godotengine/godot
    git fetch upstream

You only need to run this once to define this remote. The following steps
will have to be run each time you want to sync your branch to the state
of the upstream repo:

::

    git pull --rebase upstream/master

This command would reapply your local changes (if any) on top of the current
state of the upstream branch, thus bringing you up-to-date with your own commits
on top. In case you have local commits that should be discarded (e.g. if your
previous pull request had 5 small commits that were all merged into one bigger
commit in the upstream branch), you need to *reset* your branch:

::

    git fetch upstream
    git reset --hard upstream/master

**Warning:** The above command will reset your branch to the state of the
``upstream/master`` branch, i.e. it will discard all changes which are
specific to your local branch. So make sure to run this *before* making new
changes and not afterwards.

Alternatively, you can also keep your own master branch (``origin/master``)
up-to-date and create new branches when wanting to commit changes to the
class reference:

::

    git checkout master
    git branch -d my-previous-doc-branch
    git pull --rebase upstream/master
    git checkout -b my-new-doc-branch

In case of doubt, ask for help on our IRC channels, we have some git gurus
there.

Updating the documentation template
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When classes are modified in the source code, the documentation template
might become outdated. To make sure that you are editing an up-to-date
version, you first need to compile Godot (you can follow the
:ref:`doc_introduction_to_the_buildsystem` page), and then run the
following command (assuming 64-bit Linux):

::

    ./bin/godot.x11.tools.64 -doctool doc/base/classes.xml

The doc/base/classes.xml should then be up-to-date with current Godot
Engine features. You can then check what changed using the
``git diff`` command. If there are changes to other classes than the one
you are planning to document, please commit those changes first before
starting to edit the template:

::

    git add doc/base/classes.xml
    git commit -m "Sync classes reference template with current code base"

You are now ready to edit this file to add stuff.

**Note:** If this has been done recently by another contributor, you don't
forcefully need to go through these steps (unless you know that the class
you plan to edit *has* been modified recently).

Push and request a pull of your changes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once your modifications are finished, push your changes on your GitHub
repository:

::

    git add doc/base/classes.xml
    git commit -m "Explain your modifications."
    git push

When it's done, you can ask for a Pull Request via the GitHub UI of your
Godot fork.

Editing the doc/base/classes.xml file
-------------------------------------

This file is generated and updated by Godot Engine. It is used by the
editor as base for the Help section.

You can edit this file using your favourite text editor. If you use a code
editor, make sure that it won't needlessly change the indentation behaviour
(e.g. change all tabs to spaces).

Formatting of the XML file
~~~~~~~~~~~~~~~~~~~~~~~~~~

Here is an example with the Node2D class:

.. code:: xml

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
                Set the position of the 2d node.
                </description>
            </method>
            <method name="set_rot">
                <argument index="0" name="rot" type="float">
                </argument>
                <description>
                Set the rotation of the 2d node.
                </description>
            </method>
            <method name="set_scale">
                <argument index="0" name="scale" type="Vector2">
                </argument>
                <description>
                Set the scale of the 2d node.
                </description>
            </method>
            <method name="get_pos" qualifiers="const">
                <return type="Vector2">
                </return>
                <description>
                Return the position of the 2D node.
                </description>
            </method>
            <method name="get_rot" qualifiers="const">
                <return type="float">
                </return>
                <description>
                Return the rotation of the 2D node.
                </description>
            </method>
            <method name="get_scale" qualifiers="const">
                <return type="Vector2">
                </return>
                <description>
                Return the scale of the 2D node.
                </description>
            </method>
            <method name="rotate">
                <argument index="0" name="degrees" type="float">
                </argument>
                <description>
            </description>
            </method>
            <method name="move_local_x">
                <argument index="0" name="delta" type="float">
                </argument>
                <argument index="1" name="scaled" type="bool" default="false">
                </argument>
                <description>
                </description>
            </method>
            <method name="move_local_y">
                <argument index="0" name="delta" type="float">
                </argument>
                <argument index="1" name="scaled" type="bool" default="false">
                </argument>
                <description>
                </description>
            </method>
            <method name="get_global_pos" qualifiers="const">
                <return type="Vector2">
                </return>
                <description>
                Return the global position of the 2D node.
                </description>
            </method>
            <method name="set_global_pos">
                <argument index="0" name="arg0" type="Vector2">
                </argument>
                <description>
                </description>
            </method>
            <method name="set_transform">
                <argument index="0" name="xform" type="Matrix32">
                </argument>
                <description>
                </description>
            </method>
            <method name="set_global_transform">
                <argument index="0" name="xform" type="Matrix32">
                </argument>
                <description>
                </description>
            </method>
            <method name="edit_set_pivot">
                <argument index="0" name="arg0" type="Vector2">
                </argument>
                <description>
                </description>
            </method>
        </methods>
        <constants>
        </constants>
    </class>

As you can see, some methods in this class have no description (i.e.
there is no text between their marks). This can also happen for the
``description`` and ``brief_description`` of the class, but in our example
they are already filled. Let's edit the description of the ``rotate()``
method:

.. code:: xml

    <method name="rotate">
        <argument index="0" name="degrees" type="float">
        </argument>
        <description>
        Rotates the node of a given number of degrees.
        </description>
    </method>

That's all!

You simply have to write any missing text between these marks:

-  <description></description>
-  <brief_description></brief_description>
-  <constant></constant>
-  <member></member>
-  <signal></signal>

Describe clearly and shortly what the method does, or what the
constant, member variable or signal mean. You can include an example
of use if needed. Try to use grammatically correct English, and check
the other descriptions to get an impression of the writing style.

For setters/getters, the convention is to describe in depth what the
method does in the setter, and to say only the minimal in the getter to
avoid duplication of the contents.

Tags available for improved formatting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For more control over the formatting of the help, Godot's XML
documentation supports various BBcode-like tags which are
interpreted by both the offline in-editor Help, as well as the
online documentation (via the reST converter).

Those tags are listed below. See existing documentation entries
for more examples of how to use them properly.

+---------------------------+--------------------------------+-----------------------------------+--------------------------------------------+
| Tag                       | Effect                         | Usage                             | Result                                     |
+===========================+================================+===================================+============================================+
| [Class]                   | Link a class                   | Move the [Sprite].                | Move the :ref:`class_sprite`.              |
+---------------------------+--------------------------------+-----------------------------------+--------------------------------------------+
| [method methodname]       | Link a method of this class    | See [method set_pos].             | See :ref:`set_pos <class_node2d_set_pos>`. |
+---------------------------+--------------------------------+-----------------------------------+--------------------------------------------+
| [method Class.methodname] | Link a method of another class | See [method Node2D.set_pos].      | See :ref:`set_pos <class_node2d_set_pos>`. |
+---------------------------+--------------------------------+-----------------------------------+--------------------------------------------+
| [b] [/b]                  | Bold                           | Some [b]bold[/b] text.            | Some **bold** text.                        |
+---------------------------+--------------------------------+-----------------------------------+--------------------------------------------+
| [i] [/i]                  | Italic                         | Some [i]italic[/b] text.          | Some *italic* text.                        |
+---------------------------+--------------------------------+-----------------------------------+--------------------------------------------+
| [code] [/code]            | Monospace                      | Some [code]monospace[/code] text. | Some ``monospace`` text.                   |
+---------------------------+--------------------------------+-----------------------------------+--------------------------------------------+
| [codeblock] [/codeblock]  | Multiline preformatted block   | *See below.*                      | *See below.*                               |
+---------------------------+--------------------------------+-----------------------------------+--------------------------------------------+

The ``[codeblock]`` is meant to be used for pre-formatted code
block, using spaces as indentation (tabs will be removed by the
reST converter). For example:

.. code:: xml

    [codeblock]
    func _ready():
        var sprite = get_node("Sprite")
        print(sprite.get_pos())
    [/codeblock]

Which would be rendered as:

::

    func _ready():
        var sprite = get_node("Sprite")
        print(sprite.get_pos())

I don't know what this method does!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Not a problem. Leave it behind for now, and don't forget to notify the
missing methods when you request a pull of your changes. Another
editor will take care of it.

If you wonder what a method does, you can still have a look at its
implementation in Godot Engine's source code on GitHub. Also, if you
have a doubt, feel free to ask on the
`Q&A website <https://godotengine.org/qa/>`__
and on IRC (freenode, #godotengine).
