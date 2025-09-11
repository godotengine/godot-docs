# Godot Engine documentation

This repository contains the source files of [Godot Engine](https://godotengine.org)'s documentation, in reStructuredText markup language (reST).

They are meant to be parsed with the [Sphinx](https://www.sphinx-doc.org/) documentation builder to build the HTML documentation on [Godot's website](https://docs.godotengine.org).

## Download for offline use

To browse the documentation offline, you can download an HTML copy (updated every Monday):
[stable](https://nightly.link/godotengine/godot-docs/workflows/build_offline_docs/master/godot-docs-html-stable.zip),
[latest](https://nightly.link/godotengine/godot-docs/workflows/build_offline_docs/master/godot-docs-html-master.zip),
[3.6](https://nightly.link/godotengine/godot-docs/workflows/build_offline_docs/master/godot-docs-html-3.6.zip). Extract
the ZIP archive then open the top-level `index.html` in a web browser.

For mobile devices or e-readers, you can also download an ePub copy (updated every Monday):
[stable](https://nightly.link/godotengine/godot-docs/workflows/build_offline_docs/master/godot-docs-epub-stable.zip),
[latest](https://nightly.link/godotengine/godot-docs/workflows/build_offline_docs/master/godot-docs-epub-master.zip),
[3.6](https://nightly.link/godotengine/godot-docs/workflows/build_offline_docs/master/godot-docs-epub-3.6.zip). Extract
the ZIP archive then open the `GodotEngine.epub` file in an e-book reader application.

## Theming

The Godot documentation uses the default `sphinx_rtd_theme` with many
[customizations](_static/) applied on top. It will automatically switch between
the light and dark theme depending on your browser/OS' theming preference.

If you use Firefox and wish to use the dark theme regardless of your OS
configuration, you can install the
[Dark Website Forcer](https://addons.mozilla.org/en-US/firefox/addon/dark-mode-website-switcher/)
add-on.

## Contributing

All contributors are welcome to help on the Godot documentation.

To get started, head to the [Contributing documentation](https://contributing.godotengine.org/en/latest/organization/how_to_contribute.html). There, you will find all the information you need to write and submit changes.

Here are some quick links to the areas you might be interested in:

1. [Contributing to the online manual](https://contributing.godotengine.org/en/latest/documentation/manual/index.html)
2. [Contributing to the class reference](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)
3. [Content guidelines](https://contributing.godotengine.org/en/latest/documentation/guidelines/content_guidelines.html)
4. [Writing guidelines](https://contributing.godotengine.org/en/latest/documentation/guidelines/docs_writing_guidelines.html)
5. [Building the manual](https://contributing.godotengine.org/en/latest/documentation/manual/building_the_manual.html)
6. [Translating the documentation](https://contributing.godotengine.org/en/latest/documentation/translation/index.html)

## License

With the exception of the `classes/` folder, all the content of this repository is licensed under the Creative Commons Attribution 3.0 Unported license ([CC BY 3.0](https://creativecommons.org/licenses/by/3.0/)) and is to be attributed to "Juan Linietsky, Ariel Manzur and the Godot community".
See [LICENSE.txt](/LICENSE.txt) for details.

The files in the `classes/` folder are derived from [Godot's main source repository](https://github.com/godotengine/godot) and are distributed under the MIT license, with the same authors as above.
