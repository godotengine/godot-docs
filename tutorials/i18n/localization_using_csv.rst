.. _doc_localization_using_csv:

Localization using CSV
======================

Introduction
------------

There are two approaches to translate multilingual language games and
applications. Both are based on a key:value system. The first is to use
one of the languages as the key (usually English), the second is to use a
specific identifier (which can be a number, a string, or a combination of both). 
The first approach is the :ref:`gettext PO approach <doc_localization_using_gettext>`, 
while the second approach is the CSV approach, which is what we'll discuss here.

.. note:: There is a `translation demo <https://godotengine.org/asset-library/asset/134>`_ 
          which can be downloaded in the Asset Library where we display how to use CSV 
          translation and resource remapping.

Translation format
------------------

There are two requirements that the CSV translation file must follow:

- It must follow the format shown in table just below.
- It must be saved with UTF-8 encoding without a `byte order mark <https://en.wikipedia.org/wiki/Byte_order_mark>`__.

+--------+----------+----------+----------+
| keys   | <lang1>  | <lang2>  | <langN>  |
+========+==========+==========+==========+
| KEY1   | string   | string   | string   |
+--------+----------+----------+----------+
| KEY2   | string   | string   | string   |
+--------+----------+----------+----------+
| KEYN   | string   | string   | string   |
+--------+----------+----------+----------+

.. warning::

    By default, Microsoft Excel will always save CSV files with ANSI encoding
    rather than UTF-8. There is no built-in way to do this, but there are
    workarounds as described
    `here <https://stackoverflow.com/questions/4221176/excel-to-csv-with-utf8-encoding>`__.

    We recommend using `LibreOffice <https://www.libreoffice.org/>`__ or Google Sheets instead.

The "lang" tags must represent a language, which must be one of the :ref:`valid
locales <doc_locales>` supported by the engine. The "KEY" tags must be
unique and represent a string universally (they are usually in
uppercase, to differentiate from other strings). These keys will be replaced at
runtime by the matching translated string. Note that the case is important,
"KEY1" and "Key1" will be different keys.
The top-left cell is ignored and can be left empty or having any content.
Here's an example:

+-------+-----------------------+------------------------+------------------------------+
| keys  | en                    | es                     | ja                           |
+=======+=======================+========================+==============================+
| GREET | Hello, friend!        | Hola, amigo!           | こんにちは                   |
+-------+-----------------------+------------------------+------------------------------+
| ASK   | How are you?          | Cómo está?             | 元気ですか                   |
+-------+-----------------------+------------------------+------------------------------+
| BYE   | Goodbye               | Adiós                  | さようなら                   |
+-------+-----------------------+------------------------+------------------------------+
| QUOTE | "Hello" said the man. | "Hola" dijo el hombre. | 「こんにちは」男は言いました |
+-------+-----------------------+------------------------+------------------------------+

The same example is shown below as a comma-separated plain text file,
which should be the result of editing the above in a spreadsheet.
When editing the plain text version, be sure to enclose with double
quotes any message that contains commas, line breaks or double quotes,
so that commas are not parsed as delimiters, line breaks don't create new
entries and double quotes are not parsed as enclosing characters. Be sure
to escape any double quotes a message may contain by preceding them with
another double quote. Alternatively, you can select another delimiter than
comma in the import options.

.. code-block:: none

    keys,en,es,ja
    GREET,"Hello, friend!","Hola, amigo!",こんにちは
    ASK,How are you?,Cómo está?,元気ですか
    BYE,Goodbye,Adiós,さようなら
    QUOTE,"""Hello"" said the man.","""Hola"" dijo el hombre.",「こんにちは」男は言いました

Importing the CSV file
----------------------

Godot has its own CSV importer. When you drop a CSV file into your Godot project folder,
a list of translation resources will be generated for all the locales in the CSV. 
There's also an option to compress the translation resources. For a more 
throughout explanation, see :ref:`doc_importing_translations`.

Once you have imported the CSV file, you will need to add the translation resources to be
used in the game. This is done in **Project → Project Settings → Localization**:

.. image:: img/localization_dialog.png

Using the translations in game
------------------------------

Once you have added the translations into your project, you're ready to translate your game.

The first step is to ask ``TranslationServer`` to use the language that you want.
To do this, call the :ref:`TranslationServer.set_locale() <class_TranslationServer_method_set_locale>` function.

To fetch a translation from a key, use the translation API :ref:`tr() <class_Object_method_tr>`. As an example, see 
the ``GDScript`` below. For scene nodes containing user-facing texts, assign key for the text properties 
that you want to be translated. Some of these translated properties are ``Text``, ``Hint_Tooltip`` and ``Placeholder_Text``.

.. note:: All of these is covered in the `translation demo project <https://godotengine.org/asset-library/asset/134>`_.
          
::

    # translation_example.gd
    
    extends Node2D

    func _ready():
        TranslationServer.set_locale("ja")      
    
        print(tr("GREET"))
        
        TranslationServer.set_locale("es")
        
        print(tr("BYE"))

Plural translation
------------------

Plural translation can be tricky and is a common problem in text localization.

In Godot, it is possible to provide plural translation with CSV files. To do this, 
append the subscript ``[0]``, ``[1]``, ``[2]`` and so on for the keys dealing with plural translations.
How far the index of the subscript goes depends on the required number of indices to satisfy the number of 
plural forms of all locales. For example, Arabic has six plural forms. So if Arabic is one of 
the supported locale in the CSV, the plural keys will have up to index ``[5]`` subscript.

+-------------+-----------------------+------------------------+------------------------------+
| keys        | en                    | ja                     | ru                           |
+=============+=======================+========================+==============================+
| KEY_HELLO   | Hello!                | こんにちは!            | Привет!                      |
+-------------+-----------------------+------------------------+------------------------------+
| KEY_DAYS[0] | One day ago           | %d日前                 | %d день назад                |
+-------------+-----------------------+------------------------+------------------------------+
| KEY_DAYS[1] | %d days ago           |                        | %d дня назад                 |
+-------------+-----------------------+------------------------+------------------------------+
| KEY_DAYS[2] |                       |                        | %d дней назад                |
+-------------+-----------------------+------------------------+------------------------------+

In ``GDScript``, use the :ref:`tr_n() <class_Object_method_tr_n>` function for plural translation. You don't need 
to precise the subscript when using the key. Godot engine will concatenate the appropriate subscript for you 
based on the current locale of ``TranslationServer`` and the argument ``n`` passed into the ``tr_n()`` function.
For example (based on the above table):

::

    # translation_example.gd
    
    extends Node2D

    func _ready():
        TranslationServer.set_locale("en")      
    
        print(tr_n(1, "KEY_DAYS")) # Will print "One day ago".
        print(tr_n(6, "KEY_DAYS")) # Will print "%d days ago".
        print(tr_n(6, "KEY_DAYS") % 6) # Will print "6 days ago".
		
        TranslationServer.set_locale("ja")
        
        print(tr_n(1, "KEY_DAYS")) # Will print "%d日前".
        print(tr_n(6, "KEY_DAYS")) # Will print "%d日前".
        print(tr_n(6, "KEY_DAYS") % 6) # Will print "6日前".	

Workflow
--------

One question that often arises is what is the process of adding keys in the CSV and using keys in the game.
Which one comes first?

One recommended workflow is to have a spreadsheet open, then record the key along with the base language source string
in the spreadsheet as soon as a key is needed in the game during development. After the game is finished, the spreadsheet will be 
sent to a translation company or team to be translated. The translated spreadsheet will then be imported into the project.
