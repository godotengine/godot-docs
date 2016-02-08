# -*- coding: utf-8 -*-
#
# Godot Engine documentation build configuration file

import sys
import os

# -- General configuration ------------------------------------------------

needs_sphinx = '1.3'

# Sphinx extension module names and templates location
extensions = ['sphinx.ext.intersphinx']
templates_path = ['_templates']

# You can specify multiple suffix as a list of string: ['.rst', '.md']
source_suffix = '.rst'
source_encoding = 'utf-8-sig'

# The master toctree document
master_doc = 'index'

# General information about the project
project = 'Godot Engine'
copyright = '2014-2016, Juan Linietsky, Ariel Manzur and the Godot community (CC BY 3.0)'
author = 'Juan Linietsky, Ariel Manzur and the Godot community'

# Version info for the project, acts as replacement for |version| and |release|
# The short X.Y version
version = 'latest'
# The full version, including alpha/beta/rc tags
release = 'latest'

language = 'en'

exclude_patterns = ['_build']

# Pygments (syntax highlighting) style to use
pygments_style = 'sphinx'
highlight_language = 'python3'

# intersphinx configuration
intersphinx_mapping = {
  'english': ('http://docs.godotengine.org/en/latest/', None),
}

# -- Options for HTML output ----------------------------------------------

# on_rtd is whether we are on readthedocs.org, this line of code grabbed from docs.readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Output file base name for HTML help builder
htmlhelp_basename = 'GodotEnginedoc'

# -- Options for reStructuredText parser ----------------------------------

# Enable directives that insert the contents of external files
file_insertion_enabled = False

# -- Options for LaTeX output ---------------------------------------------

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  (master_doc, 'GodotEngine.tex', 'Godot Engine Documentation',
   'Juan Linietsky, Ariel Manzur and the Godot community', 'manual'),
]
