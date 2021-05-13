.. _doc_internationalizing_games:

Internationalizing games
========================

Introduction
------------

Sería excelente que el mundo hablara solo un idioma (It would be great if the
world spoke only one language). Unfortunately for
us developers, that is not the case. While indie or niche games usually
do not need localization, games targeting a more massive market
often require localization. Godot offers many tools to make this process
more straightforward, so this tutorial is more like a collection of
tips and tricks.

Localization is usually done by specific studios hired for the job and,
despite the huge amount of software and file formats available for this,
the most common way to do localization to this day is still with
spreadsheets. The process of creating the spreadsheets and importing
them is already covered in the :ref:`doc_importing_translations` tutorial,
so this one could be seen more like a follow-up to that one.


.. note:: We will be using the official demo as an example; you can
          `download it from the Asset Library <https://godotengine.org/asset-library/asset/134>`_.

Configuring the imported translation
------------------------------------

Translations can get updated and re-imported when they change, but
they still have to be added to the project. This is done in
**Project → Project Settings → Localization**:

.. image:: img/localization_dialog.png

The above dialog is used to add or remove translations project-wide.

Localizing resources
--------------------

It is also possible to instruct Godot to use alternate versions of
assets (resources) depending on the current language. The **Remaps** tab
can be used for this:

.. image:: img/localization_remaps.png

Select the resource to be remapped, then add some alternatives for each
locale.

Converting keys to text
-----------------------

Some controls, such as :ref:`Button <class_Button>` and :ref:`Label <class_Label>`,
will automatically fetch a translation if their text matches a translation key.
For example, if a label's text is "MAIN_SCREEN_GREETING1" and that key exists
in the current translation, then the text will automatically be translated.

This automatic translation behavior may be undesirable in certain cases. For
instance, when using a Label to display a player's name, you most likely don't
want the player's name to be translated if it matches a translation key. To
disable automatic translation on a specific node, use
:ref:`Object.set_message_translation<class_Object_method_set_message_translation>`
and send a :ref:`Object.notification<class_Object_method_notification>` to update the
translation::

    func _ready():
        # This assumes you have a node called "Label" as a child of the node
        # that has the script attached.
        var label = get_node("Label")
        label.set_message_translation(false)
        label.notification(NOTIFICATION_TRANSLATION_CHANGED)

For more complex UI nodes such as OptionButtons, you may have to use this instead::

    func _ready():
        var option_button = get_node("OptionButton")
        option_button.set_message_translation(false)
        option_button.notification(NOTIFICATION_TRANSLATION_CHANGED)
        option_button.get_popup().set_message_translation(false)
        option_button.get_popup().notification(NOTIFICATION_TRANSLATION_CHANGED)

In code, the :ref:`Object.tr() <class_Object_method_tr>`
function can be used. This will just look up the text in the
translations and convert it if found:

::

    level.set_text(tr("LEVEL_5_NAME"))
    status.set_text(tr("GAME_STATUS_" + str(status_index)))

Making controls resizable
--------------------------

The same text in different languages can vary greatly in length. For
this, make sure to read the tutorial on :ref:`doc_size_and_anchors`, as
dynamically adjusting control sizes may help.
:ref:`Container <class_Container>` can be useful, as well as the text wrapping
options available in :ref:`Label <class_Label>`.

TranslationServer
-----------------

Godot has a server handling low-level translation management
called the :ref:`TranslationServer <class_TranslationServer>`.
Translations can be added or removed during run-time;
the current language can also be changed at run-time.

Command line
------------

Language can be tested when running Godot from the command line.
For example, to test a game in French, the following argument can be
supplied:

.. code-block:: shell

   godot --language fr

Translating the project name
----------------------------

The project name becomes the app name when exporting to different
operating systems and platforms. To specify the project name in more
than one language, create a new setting ``application/name`` in the **Project
Settings** and append the locale identifier to it.
For instance, for Spanish, this would be ``application/name_es``:

.. image:: img/localized_name.png

If you are unsure about the language code to use, refer to the
:ref:`list of locale codes <doc_locales>`.
