# Godot Engine documentation

This repository contains the source files of [Godot Engine](https://godotengine.org)'s documentation, in reStructuredText markup language (reST).

They are meant to be parsed with the [Sphinx](https://www.sphinx-doc.org/) documentation builder to build the HTML documentation on [Godot's website](https://docs.godotengine.org).

## Download for offline use

To browse the documentation offline, you can use the mirror of the documentation
hosted on [DevDocs](https://devdocs.io/godot/). To enable offline browsing on
DevDocs, you need to:

- Click the three dots in the top-left corner, choose **Preferences**.
- Enable the desired version of the Godot documentation by checking the box
  next to it in the sidebar.
- Click the three dots in the top-left corner, choose **Offline data**.
- Click the **Install** link next to the Godot documentation.

You can also
[download an HTML copy](https://nightly.link/godotengine/godot-docs/workflows/build_offline_docs/master/godot-docs-html-master.zip)
for offline reading (updated every Monday). Extract the ZIP archive then open
the top-level `index.html` in a web browser.

For mobile devices or e-readers, you can also
[download an ePub copy](https://nightly.link/godotengine/godot-docs/workflows/build_offline_docs/master/godot-docs-epub-master.zip)
for offline reading (updated every Monday). Extract the ZIP archive then open
the `GodotEngine.epub` file in an e-book reader application.

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

To get started, head to the [Contributing section](https://docs.godotengine.org/en/latest/contributing/ways_to_contribute.html#contributing-to-the-documentation) of the online manual. There, you will find all the information you need to write and submit changes.

Here are some quick links to the areas you might be interested in:

1. [Contributing to the online manual](https://docs.godotengine.org/en/latest/contributing/documentation/contributing_to_the_documentation.html)
2. [Contributing to the class reference](https://docs.godotengine.org/en/latest/contributing/documentation/updating_the_class_reference.html)
3. [Content guidelines](https://docs.godotengine.org/en/latest/contributing/documentation/content_guidelines.html)
4. [Writing guidelines](https://docs.godotengine.org/en/latest/contributing/documentation/docs_writing_guidelines.html)
5. [Building the manual](https://docs.godotengine.org/en/latest/contributing/documentation/building_the_manual.html)
6. [Translating the documentation](https://docs.godotengine.org/en/latest/contributing/documentation/editor_and_docs_localization.html)

## License

At the exception of the `classes/` folder, all the content of this repository is licensed under the Creative Commons Attribution 3.0 Unported license ([CC BY 3.0](https://creativecommons.org/licenses/by/3.0/)) and is to be attributed to "Juan Linietsky, Ariel Manzur and the Godot community".
See [LICENSE.txt](/LICENSE.txt) for details.

The files in the `classes/` folder are derived from [Godot's main source repository](https://github.com/godotengine/godot) and are distributed under the MIT license, with the same authors as above.
