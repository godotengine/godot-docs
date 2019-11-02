.. _doc_importing_translations:

Importing translations
======================

Games and internationalization
------------------------------

The world is full of different markets and cultures and, to maximize
profits™, nowadays games are released in several languages. To solve
this, internationalized text must be supported in any modern game
engine.

In regular desktop or mobile applications, internationalized text is
usually located in resource files (or .po files for GNU stuff). Games,
however, can use several orders of magnitude more text than
applications, so they must support efficient methods for dealing with
loads of multilingual text.

There are two approaches to generate multilingual language games and
applications. Both are based on a key:value system. The first is to use
one of the languages as the key (usually English), the second is to use a
specific identifier. The first approach is probably easier for
development if a game is released first in English, later in other
languages, but a complete nightmare if working with many languages at
the same time.

In general, games use the second approach and a unique ID is used for
each string. This allows you to revise the text while it is being
translated to other languages. The unique ID can be a number, a string,
or a string with a number (it's just a unique string anyway).

.. note:: If you need a more powerful file format, Godot also supports
          loading translations written in the gettext ``.po`` format. See
          :ref:`doc_localization_using_gettext` for details.

Translation format
------------------

To complete the picture and allow efficient support for translations,
Godot has a special importer that can read CSV files. All spreadsheet
editors (be it Libreoffice, Microsoft Office, Google Docs, etc.) can
export to this format, so the only requirement is that the files have
a special arrangement. The CSV files must be saved in UTF-8 encoding
and be formatted as follows:

+--------+----------+----------+----------+
| keys   | <lang1>  | <lang2>  | <langN>  |
+========+==========+==========+==========+
| KEY1   | string   | string   | string   |
+--------+----------+----------+----------+
| KEY2   | string   | string   | string   |
+--------+----------+----------+----------+
| KEYN   | string   | string   | string   |
+--------+----------+----------+----------+

The "lang" tags must represent a language, which must be one of the :ref:`valid
locales <doc_locales>` supported by the engine. The "KEY" tags must be
unique and represent a string universally (they are usually in
uppercase, to differentiate from other strings). These keys will be replaced at
runtime by the matching translated string. Note that the case is important,
"KEY1" and "Key1" will be different keys.
The top-left cell is ignored and can be left empty or having any content.
Here's an example:

+---------+------------------+----------------+--------------+
| keys    | en               | es             | ja           |
+=========+==================+================+==============+
| GREET   | Hello, friend!   | Hola, amigo!   | こんにちは   |
+---------+------------------+----------------+--------------+
| ASK     | How are you?     | Cómo está?     | 元気ですか   |
+---------+------------------+----------------+--------------+
| BYE     | Goodbye          | Adiós          | さようなら   |
+---------+------------------+----------------+--------------+

The same example is shown below as a comma-separated plain text file,
which should be the result of editing the above in a spreadsheet.
When editing the plain text version, be sure to enclose any message
that contains a comma with double quotes, so that the comma is not
parsed as delimiter. Alternatively, you can select another delimiter
in the import options.

.. code-block:: none

    keys,en,es,ja
    GREET,"Hello, friend!","Hola, amigo!",こんにちは
    ASK,How are you?,Cómo está?,元気ですか
    BYE,Goodbye,Adiós,さようなら

CSV importer
------------

Godot will treat CSV files as translations by default. It will import them
and generate one or more compressed translation resource files next to it.

Importing will also add the translation to the list of
translations to load when the game runs, specified in project.godot (or the
project settings). Godot allows loading and removing translations at
runtime as well.

Select the ``.csv`` file and access the "Import" dock to define import
options. You can toggle the compression of the imported translations, and
select the delimiter to use when parsing the CSV file.

.. image:: img/import_csv.png

Be sure to click "Reimport" after any change to these options.
