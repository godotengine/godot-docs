.. _doc_building_the_manual:

Building the manual with Sphinx
===============================

This page explains how to build a local copy of the Godot manual using the
Sphinx docs engine. This allows you to have local HTML files and build the
documentation as a PDF, EPUB, or LaTeX file, for example.

To get started, you need to:

1. Clone the `godot-docs repository <https://github.com/godotengine/godot-docs/>`__.
2. Install `Sphinx <https://www.sphinx-doc.org/>`__
3. To build the docs as HTML files, install the `readthedocs.org theme
   <https://github.com/snide/sphinx_rtd_theme>`__.
4. Install the Sphinx extensions defined in the `godot-docs repository
   <https://github.com/godotengine/godot-docs/>`__ ``requirements.txt`` file.

We recommend using `pip <https://pip.pypa.io>`__, Python’s package manager to
install all these tools. It comes pre-installed with `Python
<https://www.python.org/>`__. Ensure that you install and use Python 3. Here are
the commands to clone the repository and then install all requirements.

.. note:: You may need to write ``python3 -m pip`` (Unix) or  ``py -m pip`` (Windows) instead of ``pip3``.
          If both approaches fail, `check that you have pip3 installed <https://pip.pypa.io/en/stable/installation/>`__.

.. code:: sh

    git clone https://github.com/godotengine/godot-docs.git
    pip3 install -r requirements.txt


With the programs installed, you can build the HTML documentation from the root
folder of this repository with the following command:

.. code:: sh

    # On Linux and macOS
    make html

    # On Windows, you need to execute the ``make.bat`` file instead.
    make.bat html

If you run into errors, you may try the following command:

.. code:: sh

    make SPHINXBUILD=~/.local/bin/sphinx-build html

Building the documentation requires at least 8 GB of RAM to run without disk
swapping, which slows it down. If you have at least 16 GB of RAM, you can speed
up compilation by running:

.. code:: sh

    # On Linux/macOS
    make html SPHINXOPTS=-j2

    # On Windows
    set SPHINXOPTS=-j2 && make html

The compilation will take some time as the ``classes/`` folder contains hundreds
of files.

You can then browse the documentation by opening ``_build/html/index.html`` in
your web browser.

In case you of a ``MemoryError`` or ``EOFError``, you can remove the
``classes/`` folder and run ``make`` again. This will drop the class references
from the final HTML documentation but will keep the rest intact.

.. note:: If you delete the ``classes/`` folder, do not use ``git add .`` when
          working on a pull request or the whole ``classes/`` folder will be
          removed when you commit. See `#3157
          <https://github.com/godotengine/godot-docs/issues/3157>`__ for more
          detail.

Alternatively, you can build the documentation by running the sphinx-build
program manually:

.. code:: sh

   sphinx-build -b html ./ _build

Building with Sphinx and virtualenv
-----------------------------------

If you want your Sphinx installation scoped to the project, you can install
sphinx-build using virtualenv. To do so, run this command from this repository's
root folder:

.. code:: sh

   virtualenv --system-site-packages env/
   . env/bin/activate
   pip3 install -r requirements.txt

Then, run ``make html`` as shown above.
