.. _doc_updating_the_class_reference:

Contributing to the class reference
===================================

.. highlight:: shell

The class reference is available online in the :ref:`classes <doc_class_reference>`
section of the documentation and in the Godot editor, from the help menu.

In the class reference, some methods, variables, and signals lack descriptions.
Others changed with recent releases and need updates. The developers can't write
the entire reference on their own. Godot needs you, and all of us, to
contribute.

**Important:** If you plan to make large changes, you should create an issue on
the `godot-docs repository <https://github.com/godotengine/godot-docs/>`_
or comment on an existing issue. Doing so lets others know you're already
taking care of a given class.

.. seealso::

    You can find the writing guidelines for the class reference :ref:`here <doc_class_reference_writing_guidelines>`.

    For details on Git usage and the pull request workflow, please
    refer to the :ref:`doc_pr_workflow` page.

    If you want to translate the class reference from English to another
    language, see :ref:`doc_editor_and_docs_localization`.

    This guide is also available as a `video tutorial on YouTube
    <https://www.youtube.com/watch?v=5jeHXxeX-JY>`_.

.. seealso::

    Not sure which class to contribute to? Take a look at the class reference's
    completion status `here <https://godotengine.github.io/doc-status/>`_.

You can find the source files for the class reference in Godot's GitHub
repository: `doc/classes/
<https://github.com/godotengine/godot/tree/master/doc/classes>`_.

.. note:: For some modules in the engine's source code, you'll find the XML
          files in the ``modules/<module_name>/doc_classes/`` directory instead.

.. warning:: Always edit the API reference through these source XML files. Do
             not edit the generated ``.rst`` files :ref:`in the online documentation
             <doc_class_reference>`, hosted in the `godot-docs
             <https://github.com/godotengine/godot-docs>`_ repository.

.. warning::

    Unless you make minor changes, like fixing a typo, we do not recommend using the GitHub web editor to edit the class reference's XML.

    It lacks features to edit XML well, like keeping indentations consistent, and it does not allow amending commits based on reviews.

    Also, it doesn't allow you to test your changes in the engine or with validation
    scripts as described in
    :ref:`doc_class_reference_writing_guidelines_editing_xml`.

Updating the documentation template
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When you create a new class or modify the engine's API, you need to re-generate the XML files in ``doc/classes/``.

To do so, you first need to compile Godot. See the
:ref:`doc_introduction_to_the_buildsystem` page to learn how. Then, execute the
compiled Godot binary from the Godot root directory with the ``--doctool`` option.
For example, if you're on 64-bit Linux, the command is::

    ./bin/godot.linuxbsd.tools.64 --doctool

The XML files in doc/classes should then be up-to-date with current Godot Engine
features. You can then check what changed using the ``git diff`` command. Please
only include changes that are relevant to your work on the API in your commits.
You can discard changes in other XML files using ``git checkout``.
