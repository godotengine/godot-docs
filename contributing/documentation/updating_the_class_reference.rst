.. _doc_updating_the_class_reference:

Contributing to the class reference
===================================

.. highlight:: shell

The :ref:`Class reference <doc_class_reference>` is a set of articles describing
the public API of the engine. This includes descriptions for various classes,
methods, properties, and global objects, available for scripting. The class reference
is available online, from the documentation sidebar, and in the Godot editor, from
the help menu.

As the engine grows and features are added or modified, some parts of the class reference
become obsolete and new descriptions and examples need to be added. While developers are
encouraged to document all of their work in the class reference when submitting a pull request,
we can't expect everyone to be able to write high quality documentation, so there is
always work for contributors like you to polish existing and create missing reference material.

The source of the class reference
---------------------------------

As the class reference is available in two places, online and in the editor, we need to
take care to keep things in sync. To achieve this the `main Godot repository <https://github.com/godotengine/godot/>`_
is picked as the source of truth, and the documentation for the class reference is tracked there.

.. warning::

    You should **not** edit ``.rst`` files in the ``classes/`` folder of the
    `documentation repository <https://github.com/godotengine/godot-docs/>`_.
    These files are generated automatically and are synced manually by project
    maintainers. Read further to learn how to correctly edit the class reference.

In the main repository the class reference is stored in XML files, one for each exposed
class or global object. The majority of these files is located in `doc/classes/
<https://github.com/godotengine/godot/tree/master/doc/classes>`_, but some modules
contain their own documentation as well. You will find it in the ``modules/<module_name>/doc_classes/``
directory. To learn more about editing XML files refer to :ref:`doc_class_reference_primer`.

.. seealso::

    For details on Git usage and the pull request workflow, please
    refer to the :ref:`doc_pr_workflow` page.

    If you want to translate the class reference from English to another
    language, see :ref:`doc_editor_and_docs_localization`. This guide is
    also available as a `video tutorial on YouTube
    <https://www.youtube.com/watch?v=5jeHXxeX-JY>`_.

**Important:** If you plan to make large changes, you should create an issue on
the `godot-docs repository <https://github.com/godotengine/godot-docs/>`_
or comment on an existing issue. Doing so lets others know you're already
taking care of a given class.

What to contribute
------------------

The natural place to start contributing is the classes that you are most familiar with.
This ensures that the added description will be based on experience and the necessary
know-how, not just the name of a method or a property. We advise not to add low effort
descriptions, no matter how appealing it may look. Such descriptions obscure the need
for documentation and are hard to identify automatically.

.. seealso::

    Following this principle is important and allows us to create tools for contributors.
    Such as the class reference's `completion status tracker <https://godotengine.github.io/doc-status/>`_.
    You can use it to quickly find documentation pages missing descriptions.

If you decide to document a class, but don't know what a particular method does, don't
worry. Leave it for now, and list the methods you skipped when you open a pull request
with your changes. Another writer will take care of it.

You can still look at the methods' implementation in Godot's source code on GitHub.
If you have doubts, feel free to ask on the `Q&A website <https://ask.godotengine.org/>`_
and `Godot Contributors Chat <https://chat.godotengine.org/>`_.

.. warning::

    Unless you make minor changes, like fixing a typo, we do not recommend using the
    GitHub web editor to edit the class reference's XML files. It lacks features to edit
    XML well, like keeping indentations consistent, and it does not allow amending commits
    based on reviews.

    It also doesn't allow you to test your changes in the engine or with validation
    scripts as described in :ref:`doc_class_reference_editing_xml`.


Updating class reference when working on the engine
---------------------------------------------------

When you create a new class or modify an existing engine's API, you need to re-generate
the XML files in ``doc/classes/``.

To do so, you first need to compile Godot. See the :ref:`doc_introduction_to_the_buildsystem`
page to learn how. Then, execute the compiled Godot binary from the Godot root directory
with the ``--doctool`` option. For example, if you're on 64-bit Linux, the command might be:

::

    ./bin/godot.linuxbsd.editor.x86_64 --doctool

The exact set of suffixes may be different. Carefully read through the linked article to
learn more about that.

The XML files in ``doc/classes/`` should then be up-to-date with current Godot Engine
features. You can then check what changed using the ``git diff`` command.

Please only include changes that are relevant to your work on the API in your commits.
You can discard changes in other XML files using ``git checkout``, but consider reporting
if you notice unrelated files being updated. Ideally, running this command should only
bring up the changes that you yourself have made.
