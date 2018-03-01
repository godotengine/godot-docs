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

Translators also usually prefer to work with spreadsheets.

Translation format
------------------

To complete the picture and allow efficient support for translations,
Godot has a special importer that can read CSV files. All spreadsheet
editors (be it Libreoffice, Microsoft Office, Google Docs, etc.) can
export to this format, so the only requirement is that the files have
a special arrangement. The CSV files must be saved in UTF-8 encoding
and be formatted as follows:

+--------+----------+----------+----------+
|        | <lang1>  | <lang2>  | <langN>  |
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
uppercase, to differentiate from other strings). Here's an example:

+---------+------------------+----------------+--------------+
| id      | en               | es             | ja           |
+=========+==================+================+==============+
| GREET   | Hello, friend!   | Hola, Amigo!   | こんにちは   |
+---------+------------------+----------------+--------------+
| ASK     | How are you?     | Cómo está?     | 元気ですか   |
+---------+------------------+----------------+--------------+
| BYE     | Good Bye         | Adiós          | さようなら   |
+---------+------------------+----------------+--------------+

CSV Importer
------------

Godot will treat CSV files as translations by default. It will import them
and generate one or more compressed translation resource files next to it.

Importing will also add the translation to the list of
translations to load when the game runs, specified in project.godot (or the
project settings). Godot allows loading and removing translations at
runtime as well.


