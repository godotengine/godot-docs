.. _doc_updating_the_class_reference:

Updating the class reference
============================

Godot Engine provides an important number of classes that you can make
use of to create your games. However, the :ref:`toc-class-ref` that
lists all these classes with their methods is quite incomplete. We need
your kind help to fill this reference. This page will explain you how.

> Please note: we aim at filling completely this reference in English
first. Please do not start translating it for the moment.

:ref:`doc_list_of_classes_and_documenters`

Editing with Github
-------------------

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

    git checkout -b reference-edition

The branch you just created is identical to current master branch of
Godot Engine. It already contains a doc/ folder, with the currently
written reference.

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
Engine features. You can then check what changed (or not) using the
``git diff`` command. If there are changes to other classes than the one
you are planning to document, please commit those changes first before
starting to edit the template:

::

    git add doc/base/classes.xml
    git commit -m "Sync classes reference template with current code base"

You are now ready to edit this file to add stuff.

Push and request a pull of your changes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once your modifications are finished, push your changes on your GitHub
repository:

::

    git add doc/base/classes.xml
    git commit -m "Explain your modifications."
    git push

When it's done, you can ask for a Pull Request on the GitHub UI of your
Godot fork.

Edit doc/base/classes.xml file
------------------------------

First of all, check the :ref:`doc_list_of_classes_and_documenters`. Try to work
on classes not already assigned nor filled.

This file is produced by Godot Engine. It is used by the editor, for
example in the Help window (F1, Shift+F1).

You can edit this file using your favourite text editor.

Here is an example with the Node2D class:

.. code:: xml
    <class name="Node2D" inherits="CanvasItem" category="Core">
    <brief_description>
    Base node for 2D system.
    </brief_description>
    <description>
    Base node for 2D system. Node2D contains a position, rotation and scale, which is used to position and animate. It can alternatively be used with a custom 2D transform ([Matrix32]). A tree of Node2Ds allows complex hierachies for animation and positioning.
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
description and the brief_description of the class, but in our case
they are already filled. Let's edit the description of the rotate()
method:

.. code:: xml
    <method name="rotate">
        <argument index="0" name="degrees" type="float">
        </argument>
        <description>
        Rotates the node of "degrees" degrees.
        </description>
    </method>

That's all!

You simply have to write any missing text between these marks:

-  <description></description>
-  <brief_description></brief_description>
-  <constant></constant>

Describe clearly and shortly what it does. You can include an example of
use if needed. Avoid grammar faults.

I don't know what this method does!
-----------------------------------

Not a problem. Leave it behind for now, and don't forget to notify the
missing methods when you request a pull of your changes. Another
editor will take care of it.

If you wonder what a method does, you can still have a look at its
implementation in Godot Engine's source code on GitHub. Also, if you
have a doubt, feel free to ask on the
`Forums <http://www.godotengine.org/projects/godot-engine/boards>`__
and on IRC (freenode, #godotengine).
