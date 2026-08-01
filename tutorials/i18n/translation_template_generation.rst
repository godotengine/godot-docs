.. _doc_translation_template_generation:

Generating translation templates
================================

Translation templates collect a project's source strings before translation.
Godot's template generator can create GNU gettext ``.pot`` files and CSV
templates from scenes and scripts. Regenerate a template whenever localizable
content changes so translators work from the current project.

Configuring the generator
-------------------------

Open :menu:`Project > Project Settings > Localization > Template Generation`.
Use :button:`Add...` to include scenes and scripts that contain source strings,
then click :button:`Generate` and choose an output path. Use a ``.pot``
extension for gettext or ``.csv`` for spreadsheet-based translations. The
generator is also available from the Command Palette for quick updates while
you are editing localizable content.

What the generator extracts
---------------------------

The generator collects strings from supported scene properties and from
:ref:`tr() <class_Object_method_tr>` and
:ref:`tr_n() <class_Object_method_tr_n>` calls in scripts. For example, it can
find UI control text. This list is not exhaustive because Godot can add new
localizable properties over time.

Nodes whose **Auto Translate Mode** is disabled do not contribute their
translatable scene strings. Use this for identifiers or content supplied by a
service. Translation contexts are included in templates. For Controls, set
**Translation Context** when an otherwise identical source string has a
different meaning in one part of the interface. See
:ref:`translation contexts <doc_internationalizing_games_translation_contexts>`.

Customizing extracted strings
-----------------------------

Use :ref:`EditorTranslationParserPlugin <class_EditorTranslationParserPlugin>`
for custom file formats or to adjust extracted strings. Its
``_customize_strings()`` method can add, remove, or modify entries before Godot
writes the template. For example, a project can remove placeholder text from
scenes while retaining automatic translation for the rest of a node.

For script-specific extraction details, including comments for translators,
see :ref:`localization using gettext <doc_localization_using_gettext_gdscript>`.
