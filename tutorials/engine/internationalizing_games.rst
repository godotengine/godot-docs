.. _doc_internationalizing_games:

Internationalizing games
========================

Introduction
------------

Sería excelente que el mundo hablara solo un idioma. Unfortunately for
us developers, that is not the case. While not generally a big
requirement when developing indie or niche games, it is also very common
that games going into a more massive market require localization.

Godot offers many tools to make this process more straightforward, so
this tutorial is more like a collection of tips and tricks.

Localization is usually done by specific studios hired for the job and,
despite the huge amount of software and file formats available for this,
the most common way to do localization to this day is still with
spreadsheets. The process of creating the spreadsheets and importing
them is already covered in the :ref:`doc_importing_translations` tutorial, so this
one could be seen more like a follow up to that one.

Configuring the imported translation
------------------------------------

The translations can get updated and re-imported when they change, but
they still have to be added to the project. This is done in Scene
> Project Settings > Localization:

.. image:: /img/localization_dialog.png

This dialog allows to add or remove translations project-wide.

Localizing resources
--------------------

It is also possible to instruct Godot to open alternative versions of
assets (resources) depending on the current language. For this the
"Remaps" tab exists:

.. image:: /img/localization_remaps.png

Select the resource to be remapped, and the alternatives for each
locale.

Converting keys to text
-----------------------

Some controls such as :ref:`Button <class_Button>`, :ref:`Label <class_Label>`,
etc. will automatically fetch a translation each time they are set a key
instead of a text. For example, if a label is assigned
"MAIN_SCREEN_GREETING1" and a key to different languages exists in the
translations, this will be automatically converted. This process is done
upon load though, so if the project in question has a dialog that allows
changing the language in the settings, the scenes (or at least the
settings scene) will have to be re-loaded for new text to have effect.

For code, the :ref:`Object.tr() <class_Object_tr>`
function can be used. This will just look-up the text into the
translations and convert it if found:

::

    level.set_text(tr("LEVEL_5_NAME"))
    status.set_text(tr("GAME_STATUS_" + str(status_index)))

Making controls resizeable
--------------------------

The same text in different languages can vary greatly in length. For
this, make sure to read the tutorial on :ref:`doc_size_and_anchors`, as having
dynamically adjusted control sizes may help.
:ref:`Container <class_Container>` can be very useful, as well as the multiple options in
:ref:`Label <class_Label>` for text wrapping.

TranslationServer
-----------------

Godot has a server for handling the low level translation management
called the :ref:`TranslationServer <class_TranslationServer>`.
Translations can be added or removed during run-time, and the current
language be changed too.

Command line
------------

Language can be tested when running Godot from command line. For
example, to test a game in french, the following arguments can be
supplied:

::

   c:\MyGame> godot -lang fr

Translating the project name
----------------------------

The project name becomes the app name when exporting to different
operating systems and platforms. To specify the project name in more
than one language, create a new setting application/name in the project
settings dialog and append the locale identifier to it. For example:

.. image:: /img/localized_name.png

As always, If you don't know the code of a language or zone, :ref:`check the
list <doc_locales>`.
