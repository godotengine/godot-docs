.. _doc_importing_translations:

Importing translations
======================

CSV importer
------------

Godot will treat CSV files as translations by default. It will import them
and generate one or more compressed translation resource files next to it.

Importing will also add the translation to the list of
translations to load when the game runs, specified in project.godot (or the
project settings). Godot allows loading and removing translations at
runtime as well.

Select the ``.csv`` file and access the **Import** dock to define import
options. You can toggle the compression of the imported translations, and
select the delimiter to use when parsing the CSV file.

.. note:: For translation tutorial using CSV files, see 
          :ref:`doc_localization_using_csv` for details.

.. image:: img/import_csv.png

Be sure to click **Reimport** after any change to these options.

PO files
--------

The other translation file format which Godot accepts is the ``.po`` file
format. To import these files, just drag and drop them into your Godot project 
folder.

.. note:: For translation tutorial using PO files, see 
          :ref:`doc_localization_using_gettext` for details.
