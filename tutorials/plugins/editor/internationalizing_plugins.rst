.. _doc_internationalizing_plugins:

Internationalizing plugins
==========================

In the same way :ref:`doc_internationalizing_games` works, you can create translations
for editor plugins. Everything that applies to games also applies to plugins,
but the process of enabling translations for plugins is slightly different.

After generating your CSV or POT file and creating translations, you cannot simply
load the translations in the project settings; instead, you must go through
the :ref:`class_TranslationServer` to add a new :ref:`class_TranslationDomain`.

::

    func _enter_tree():
        var domain = TranslationServer.get_or_add_domain("addons/my_plugin")
        var dir = "res://addons/my_plugin/locale"
        for file in DirAccess.get_files_at(dir):
            var translation = ResourceLoader.load(dir.path_join(file)) as Translation
            if translation:
                domain.add_translation(translation)

        # Existing plugin initialization...

The above code will load all available translations for your plugin, assuming the translations
are located in the ``addons/my_plugin/locale`` directory. You should also choose a unique
translation domain name to avoid collisions with other domains; using your plugin's path
as the domain name ensures this.

If we consider the dock from :ref:`doc_making_plugins_custom_dock`, you now need to tell the dock
to use this translation domain:

::

    dock.set_translation_domain("addons/my_plugin")

The last thing you need to do is remove the translation domain when the plugin is disabled:

::

    func _exit_tree():
        # Existing plugin cleanup...
        TranslationServer.remove_domain("addons/my_plugin")

With all of this done, you can change the editor's language to check your translations.

.. note::

    You will need to disable and re-enable your plugin once, as it needs to call
    :ref:`_enter_tree() <class_Node_private_method__enter_tree>` in order to load translations.
