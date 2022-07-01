.. _doc_importing_translations:

Importing translations
======================

Games and internationalization
------------------------------

The gaming community isn't monolingual or monocultural. It's made up of
many different languages and cultures - just like the Godot community!
If you want to allow players to experience your game in their language,
one of things you'll need to provide is text translations, which Godot
supports via internationalized text.

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

Supported formats
-----------------

To complete the picture and allow efficient support for translations,
Godot has a special importer that can read CSV files. Most spreadsheet
editors can export to this format, so the only requirement is that the
files have a special arrangement. See
:ref:`doc_localization_using_spreadsheets` for detailed info on
formatting and importing CSVs.

If you need a more powerful file format, Godot also supports loading
translations written in the gettext ``.po`` format. See
:ref:`doc_localization_using_gettext` for details.
