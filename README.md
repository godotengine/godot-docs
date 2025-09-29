# Redot Engine documentation

This repository contains the source files of [Redot Engine](https://redotengine.org)'s documentation, in reStructuredText markup language (reST).

They are meant to be parsed with the [Sphinx](https://www.sphinx-doc.org/) documentation builder to build the HTML documentation on [Redot's website](https://docs.redotengine.org).

## Download for offline use

To browse the documentation offline, you can download an HTML copy (updated every Monday):
[stable](https://download.redotengine.org/docs/redot-docs-html-stable.zip),
[latest](https://download.redotengine.org/docs/redot-docs-html-master.zip). Extract
the ZIP archive then open the top-level `index.html` in a web browser.

For mobile devices or e-readers, you can also download an ePub copy (updated every Monday):
[stable](https://download.redotengine.org/docs/redot-docs-epub-stable.zip),
[latest](https://download.redotengine.org/docs/redot-docs-epub-master.zip). Extract
the ZIP archive then open the `RedotEngine.epub` file in an e-book reader application.

## Migrating

We are transitioning from Godot to Redot. In this period, a temporary solution is available.

```
python migrate.py . _migrated True
```

After the docs are converted, you can build with

```
sphinx-build -b html ./_migrated/ _build/html
```

## Theming

The Redot documentation uses the default `sphinx_rtd_theme` with many
[customizations](_static/) applied on top. It will automatically switch between
the light and dark theme depending on your browser/OS' theming preference.

If you use Firefox and wish to use the dark theme regardless of your OS
configuration, you can install the
[Dark Website Forcer](https://addons.mozilla.org/en-US/firefox/addon/dark-mode-website-switcher/)
add-on.

## Contributing

All contributors are welcome to help on the Redot documentation.

To get started, head to the [Contributing section](https://docs.redotengine.org/contributing/how_to_contribute.html) of the online manual. There, you will find all the information you need to write and submit changes.

Here are some quick links to the areas you might be interested in:

1. [Contributing to the online manual](https://docs.redotengine.org/contributing/documentation/contributing_to_the_documentation.html)
2. [Contributing to the class reference](https://docs.redotengine.org/contributing/documentation/updating_the_class_reference.html)
3. [Content guidelines](https://docs.redotengine.org/contributing/documentation/content_guidelines.html)
4. [Writing guidelines](https://docs.redotengine.org/contributing/documentation/docs_writing_guidelines.html)
5. [Building the manual](https://docs.redotengine.org/contributing/documentation/building_the_manual.html)
6. [Translating the documentation](https://docs.redotengine.org/contributing/documentation/editor_and_docs_localization.html)

### How to build with anaconda/miniconda

```
# 1) create env with Python 3.11
conda create -n redot-docs python=3.11 -y

# 2) activate it
conda activate redot-docs

# 3) ensure pip is available (usually is)
conda install pip -y

# 4) from the repo root, install requirements via pip
python -m pip install -r requirements.txt

# 5) Migration
python migrate.py . _migrated True

# 6) build the docs
sphinx-build -b html ./_migrated/ _build/html
```

## License

With the exception of the `classes/` folder, all the content of this repository is licensed under the Creative Commons Attribution
3.0 Unported license ([CC BY 3.0](https://creativecommons.org/licenses/by/3.0/)) and is to be attributed to "the Redot community, modified from an original work by Juan Linietsky, Ariel Manzur and the Godot community".
See [LICENSE.txt](/LICENSE.txt) for details.

The files in the `classes/` folder are derived from [Redot's main source repository](https://github.com/redot-engine/redot) and are distributed under the MIT license, with the same authors as above.
