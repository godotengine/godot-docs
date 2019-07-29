# -*- coding: utf-8 -*-
#
# Godot Engine documentation build configuration file

import sys
import os

# -- General configuration ------------------------------------------------

needs_sphinx = '1.3'

# Sphinx extension module names and templates location
sys.path.append(os.path.abspath('extensions'))
extensions = ['gdscript', 'sphinx_tabs.tabs', 'sphinx.ext.imgmath']
templates_path = ['_templates']

# You can specify multiple suffix as a list of string: ['.rst', '.md']
source_suffix = '.rst'
source_encoding = 'utf-8-sig'

# The master toctree document
master_doc = 'index'

# General information about the project
project = 'Godot Engine'
copyright = '2014-2019, Juan Linietsky, Ariel Manzur and the Godot community (CC-BY 3.0)'
author = 'Juan Linietsky, Ariel Manzur and the Godot community'

# Version info for the project, acts as replacement for |version| and |release|
# The short X.Y version
version = 'latest'
# The full version, including alpha/beta/rc tags
release = 'latest'

# Parse Sphinx tags passed from RTD via environment
env_tags = os.getenv('SPHINX_TAGS')
if env_tags != None:
   for tag in env_tags.split(','):
       print("Adding Sphinx tag: %s" % tag.strip())
       tags.add(tag.strip())

# Language / i18n
language = os.getenv('READTHEDOCS_LANGUAGE', 'en')
is_i18n = tags.has('i18n')

exclude_patterns = ['_build']

# GDScript syntax highlighting
from gdscript import GDScriptLexer
from sphinx.highlighting import lexers
lexers['gdscript'] = GDScriptLexer()

# Pygments (syntax highlighting) style to use
pygments_style = 'sphinx'
highlight_language = 'gdscript'

# -- Options for HTML output ----------------------------------------------

# on_rtd is whether we are on readthedocs.org, this line of code grabbed from docs.readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

import sphinx_rtd_theme
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
if on_rtd:
    using_rtd_theme = True

# Theme options
html_theme_options = {
    # 'typekit_id': 'hiw1hhg',
    # 'analytics_id': '',
    # 'sticky_navigation': True  # Set to False to disable the sticky nav while scrolling.
    'logo_only': True,  # if we have a html_logo below, this shows /only/ the logo with no title text
    'collapse_navigation': False,  # Collapse navigation (False makes it tree-like)
    # 'display_version': True,  # Display the docs version
    # 'navigation_depth': 4,  # Depth of the headers shown in the navigation bar
}

# VCS options: https://docs.readthedocs.io/en/latest/vcs.html#github
html_context = {
    "display_github": not is_i18n, # Integrate GitHub
    "github_user": "godotengine", # Username
    "github_repo": "godot-docs", # Repo name
    "github_version": "master", # Version
    "conf_py_path": "/", # Path in the checkout to the docs root
}

html_logo = 'img/docs_logo.png'

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

# -- Options for linkcheck builder ----------------------------------------

# disable checking urls with about.html#this_part_of_page anchors
linkcheck_anchors = False

linkcheck_timeout = 10

# -- I18n settings --------------------------------------------------------

locale_dirs = ['../sphinx/po/']
gettext_compact = False

# Couldn't find a way to retrieve variables nor do advanced string
# concat from reST, so had to hardcode this in the "epilog" added to
# all pages. This is used in index.rst to display the Weblate badge.
# On English pages, the badge points to the language-neutral engage page.
rst_epilog = """
.. |weblate_widget| image:: https://hosted.weblate.org/widgets/godot-engine/{image_locale}/godot-docs/287x66-white.png
    :alt: Translation status
    :target: https://hosted.weblate.org/engage/godot-engine{target_locale}/?utm_source=widget
""".format(
    image_locale='-' if language == 'en' else language,
    target_locale='' if language == 'en' else '/' + language
)

# Exclude class reference when marked with tag i18n.
if is_i18n:
    exclude_patterns = ['classes']
