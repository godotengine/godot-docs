.. _doc_localization_using_gettext:

Localization using gettext
==========================

In addition to :ref:`doc_importing_translations` in CSV format, Godot
also supports loading translation files written in the GNU gettext
(``.po``) format.

.. note:: For an introduction to gettext, check out
          `A Quick Gettext Tutorial <https://www.labri.fr/perso/fleury/posts/programming/a-quick-gettext-tutorial.html>`_.
          It's written with C projects in mind, but much of the advice
          also applies to Godot (with the exception of ``xgettext``).

Advantages
----------

- gettext is a standard format, which can be edited using any text editor
  or GUI editors such as `Poedit <https://poedit.net/>`_.
- gettext is supported by translation platforms such as
  `Transifex <https://www.transifex.com/>`_ and `Weblate <https://weblate.org/>`_,
  which makes it easier for people to collaborate to localization.
- Compared to CSV, gettext works better with version control systems like Git,
  as each locale has its own messages file.
- Multiline strings are more convenient to edit in gettext files compared
  to CSV files.

Disadvantages
-------------

- gettext is a more complex format than CSV and can be harder to grasp for
  people new to software localization.
- People who maintain localization files will have to install gettext tools
  on their system. However, as Godot doesn't use compiled message object files
  (``.mo``), translators can test their work without having to install
  gettext tools.

Caveats
-------

- As Godot uses its own PO file parser behind the scenes
  (which is more limited than the reference GNU gettext implementation),
  some features such as pluralization aren't supported.

Installing gettext tools
------------------------

The command line gettext tools are required to perform maintenance operations,
such as updating message files. Therefore, it's strongly recommended to
install them.

- **Windows:** Download an installer from
  `this page <https://mlocati.github.io/articles/gettext-iconv-windows.html>`_.
  Any architecture and binary type (shared or static) works;
  if in doubt, choose the 64-bit static installer.
- **macOS:** Use `Homebrew <https://brew.sh/>`_ to install gettext with the
  ``brew install gettext`` command.
- **Linux:** On most distributions, install the ``gettext`` package from
  your distribution's package manager.

Creating the PO template (POT) manually
---------------------------------------

Godot currently doesn't support extracting source strings using ``xgettext``,
so the ``.pot`` file must be created manually. This file can be placed anywhere
in the project directory, but it's recommended to keep it in a subdirectory, as
each locale will be defined in its own file.

Create a directory named `locale` in the project directory. In this directory,
save a file named ``messages.pot`` with the following contents:

::

    # Don't remove the two lines below, they're required for gettext to work correctly.
    msgid ""
    msgstr ""

    msgid "Hello world!"
    msgstr ""

Messages in gettext are made of ``msgid`` and ``msgstr`` pairs.
``msgid`` is the source string (usually in English), ``msgstr`` will be
the translated string.

The ``msgstr`` value in PO template files (``.pot``) should **always** be empty.
Localization will be done in the generated ``.po`` files instead.

Creating the PO template (POT) using pybabel
--------------------------------------------

The Python tool pybabel has support for Godot and can be used to automatically
create and update the POT file from your scene files and scripts.

After installing ``babel`` and ``babel-godot``, for example using pip:

.. code-block:: shell

    pip install babel babel-godot

Write a mapping file (for example ``babelrc``) which will indicate which files
pybabel needs to process (note that we process GDScript as Python, which is
generally sufficient):

.. code-block:: none

    [python: **.gd]
    encoding = utf-8

    [godot_scene: **.tscn]
    encoding = utf-8

You can then run pybabel like so:

.. code-block:: shell

    pybabel extract -F babelrc -k text -k LineEdit/placeholder_text -k tr -o godot-l10n.pot .

Use the ``-k`` option to specify what needs to be extracted. In this case,
arguments to :ref:`tr() <class_Object_method_tr>` will be translated, as well
as properties named "text" (commonly used by Control nodes) and LineEdit's
"placeholder_text" property.

Creating a messages file from a PO template
-------------------------------------------

The ``msginit`` command is used to turn a PO template into a messages file.
For instance, to create a French localization file, use the following command
while in the ``locale`` directory:

.. code-block:: shell

    msginit --no-translator --input=messages.pot --locale=fr

The command above will create a file named ``fr.po`` in the same directory
as the PO template.

Alternatively, you can do that graphically using Poedit, or by uploading the
POT file to your web platform of choice.

Loading a messages file in Godot
--------------------------------

To register a messages file as a translation in a project, open the
**Project Settings**, then go to the **Localization** tab.
In **Translations**, click **Add…** then choose the ``.po`` file
in the file dialog. The locale will be inferred from the
``"Language: <code>\n"`` property in the messages file.

.. note:: See :ref:`doc_internationalizing_games` for more information on
          importing and testing translations in Godot.

Updating message files to follow the PO template
------------------------------------------------

After updating the PO template, you will have to update message files so
that they contain new strings, while removing strings that are no longer
present in the PO template removed in the PO template. This can be done
automatically using the ``msgmerge`` tool:

.. code-block:: shell

    # The order matters: specify the message file *then* the PO template!
    msgmerge --update --backup=none fr.po messages.pot

If you want to keep a backup of the original message file (which would be
saved as ``fr.po~`` in this example), remove the ``--backup=none`` argument.

Checking the validity of a PO file or template
----------------------------------------------

It is possible to check whether a gettext file's syntax is valid by running
the command below:

.. code-block:: shell

    msgfmt fr.po --check

If there are syntax errors or warnings, they will be displayed in the console.
Otherwise, ``msgfmt`` won't output anything.
