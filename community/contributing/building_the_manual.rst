.. _doc_building_the_manual:

Building the manual with Sphinx
===============================

This page explains how to build a local copy of the Godot manual using the
Sphinx docs engine. This allows you to have local HTML files and build the
documentation as a PDF, EPUB, or LaTeX file, for example.

To get started, you need to install:

1. `Sphinx <https://www.sphinx-doc.org/>`__
2. To build the docs as HTML files, the `readthedocs.org theme
   <https://github.com/snide/sphinx_rtd_theme>`__
3. The Sphinx extensions defined in this repository's ``requirements.txt`` file

We recommend using `pip <https://pip.pypa.io>` _, Python’s package manager to
install all these tools. It comes pre-installed with `Python
<https://www.python.org/>`__. Ensure that you install and use Python 3.

.. code:: sh

   pip install -r requirements.txt

.. note:: On Linux distributions, you may need to write ``pip3`` instead of
          ``pip`` because you generally have both Python 2 and 3 installed on
          your system. Alternatively, you can explicitly ask Python 3 to execute
          its version of pip as a module like so: ``python3 -m pip``.

With the programs installed, you can build the HTML documentation from the root
folder of this repository with the following command:

.. code:: sh

   make html

If you run into errors, you may try the following command:

.. code:: sh

   make SPHINXBUILD=~/.local/bin/sphinx-build html

Building the documentation requires at least 8 GB of RAM to run without disk
swapping, which slows it down. If you have at least 16 GB of RAM, you can speed
up compilation by running:

.. code:: bash

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


Building with Sphinx on Windows
-------------------------------

On Windows, you need to:

1. Download the Python installer `here <https://www.python.org/downloads/>`__.
2. Install Python. Be sure to check the “Add Python to PATH” checkbox.
3. Use the above ``pip`` commands to install required programs.

To build the documentation, open the root directory of this repository in your
command line and execute ``make.bat`` like so:

.. code:: sh

   make.bat html

Alternatively, you can build the documentation by running the sphinx-build
program manually:

.. code:: sh

   sphinx-build -b html ./ _build

Note that during the first build, various installation prompts may appear and
ask to install LaTeX plugins. Make sure you don’t miss them, especially if they
open behind other windows. The build may hang until you confirm these prompts.

Building with Sphinx and virtualenv
-----------------------------------

If you want your Sphinx installation scoped to the project, you can install
sphinx-build using virtualenv. To do so, run this command from this repository's
root folder:

.. code:: sh

   virtualenv --system-site-packages env/
   . env/bin/activate
   pip install -r requirements.txt

Then, run ``make html`` as shown above.
