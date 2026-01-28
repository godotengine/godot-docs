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

The Godot documentation uses the default ``sphinx_rtd_theme`` with many
[customizations](_static/) applied on top. It will automatically switch between
the light and dark theme depending on your browser/OS' theming preference.

If you use Firefox and wish to use the dark theme regardless of your OS
configuration, you can install the
[Dark Website Forcer](https://addons.mozilla.org/en-US/firefox/addon/dark-mode-website-switcher/)
add-on.

## Contributing changes

**Pull Requests should use the `master` branch by default. Only make Pull Requests against other branches (e.g. `2.1` or `3.0`) if your changes only apply to that specific version of Godot.**

Though arguably less convenient to edit than a wiki, this Git repository is meant to receive pull requests to always improve the documentation, add new pages, etc. Having direct access to the source files in a revision control system is a big plus to ensure the quality of our documentation.

### Editing existing pages

To edit an existing page, locate its .rst source file and open it in your favorite text editor. You can then commit the changes, push them to your fork and make a pull request.
**Note that the pages in `classes/` should not be edited here, they are automatically generated from Godot's [XML class references](https://github.com/godotengine/godot/tree/master/doc/classes).**
See [Contribute to the Class Reference](https://docs.godotengine.org/en/latest/community/contributing/updating_the_class_reference.html) for details.

### Adding new pages

To add a new page, create a .rst file with a meaningful name in the section you want to add a file to, e.g. `tutorials/3d/light_baking.rst`. Write its content like you would do for any other file, and make sure to define a reference name for Sphinx at the beginning of the file (check other files for the syntax), based on the file name with a "doc_" prefix (e.g. `.. _doc_light_baking:`).

You should then add your page to the relevant "toctree" (table of contents, e.g. `tutorials/3d/index.rst`). By convention, the files used to define the various levels of toctree are prefixed with an underscore, so in the above example the file should be referenced in `tutorials/3d/_3d_graphics.rst`. Add your new filename to the list on a new line, using a relative path and no extension, e.g. here `light_baking`.

### Sphinx and reStructuredText syntax

Check Sphinx's [reST Primer](https://www.sphinx-doc.org/en/stable/rest.html) and the [official reference](http://docutils.sourceforge.net/rst.html) for details on the syntax.

Sphinx uses specific reST comments to do specific operations, like defining the table of contents (`:toctree:`) or cross-referencing pages. Check the [official Sphinx documentation](https://www.sphinx-doc.org/en/stable/index.html) for more details, or see how things are done in existing pages and adapt it to your needs.

### Adding images and attachments

To add images, please put them in an `img/` folder next to the .rst file with a meaningful name and include them in your page with:
```rst
.. image:: img/image_name.png
```

Similarly, you can include attachments (like assets as support material for a tutorial) by placing them into a `files/` folder next to the .rst file, and using this inline markup:
```rst
:download:`myfilename.zip <files/myfilename.zip>`
```

## Building with Sphinx

To build the HTML website (or any other format supported by Sphinx, like PDF, EPUB or LaTeX), you need to install [Sphinx](https://www.sphinx-doc.org/) >= 1.3 as well as (for the HTML) the [readthedocs.org theme](https://github.com/snide/sphinx_rtd_theme).
You also need to install the Sphinx extensions defined in `requirements.txt`.

Those tools are best installed using [pip](https://pip.pypa.io), Python's module installer. The Python 3 version might be provided (on Linux distros) as `pip3` or `python3-pip`. You can then run:

```sh
pip install -r requirements.txt
```

You can then build the HTML documentation from the root folder of this repository with:

```sh
make html
```

or:

```sh
make SPHINXBUILD=~/.local/bin/sphinx-build html
```

Building the documentation requires at least 8 GB of RAM to be done without swapping. If you have at least 16 GB of RAM, you can speed up compilation by using:

```bash
# On Linux/macOS
make html SPHINXOPTS=-j2

# On Windows
set SPHINXOPTS=-j2 && make html
```

The compilation might take some time as the `classes/` folder contains many files to parse.

In case of a `MemoryError` or `EOFError`, you can remove the `classes/` folder and run `make` again. This will drop the class references from the final HTML documentation but will keep the rest intact. Make sure to avoid using `git add .` in this case when working on a pull request, or the whole `classes/` folder will be removed when you make a commit. See [#3157](https://github.com/godotengine/godot-docs/issues/3157) for more details.

You can then test the changes live by opening `_build/html/index.html` in your favorite browser.

### Building with Sphinx on Windows

On Windows, you need to:
* Download the Python installer [here](https://www.python.org/downloads/).
* Install Python. Don't forget to check the "Add Python to PATH" box.
* Use the above `pip` commands.

Building is still done at the root folder of this repository using the provided `make.bat`:
```sh
make.bat html
```

Alternatively, you can build with this command instead:
```sh
sphinx-build -b html ./ _build
```

Note that during the first build, various installation prompts may appear and ask to install LaTeX plugins.
Make sure you don't miss them, especially if they open behind other windows, else the build may appear to hang until you confirm these prompts.

You could also install a normal `make` toolchain (for example via MinGW) and build the docs using the normal `make html`.

### Building with Sphinx and virtualenv

If you want your Sphinx installation scoped to the project, you can install it using virtualenv.
Execute this from the root folder of this repository:

```sh
virtualenv --system-site-packages env/
. env/bin/activate
pip install -r requirements.txt
```

Then do `make html` like above.

## License

At the exception of the `classes/` folder, all the content of this repository is licensed under the Creative Commons Attribution 3.0 Unported license ([CC BY 3.0](https://creativecommons.org/licenses/by/3.0/)) and is to be attributed to "Juan Linietsky, Ariel Manzur and the Godot community".
See [LICENSE.txt](/LICENSE.txt) for details.

The files in the `classes/` folder are derived from [Godot's main source repository](https://github.com/godotengine/godot) and are distributed under the MIT license, with the same authors as above.
