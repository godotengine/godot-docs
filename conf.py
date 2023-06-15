# -*- coding: utf-8 -*-
#
# Godot Engine documentation build configuration file

import sphinx
import sphinx_rtd_theme
import sys
import os

# -- General configuration ------------------------------------------------

needs_sphinx = "1.3"

# Sphinx extension module names and templates location
sys.path.append(os.path.abspath("_extensions"))
extensions = [
    "sphinx_tabs.tabs",
    "notfound.extension",
    "sphinxext.opengraph",
    "sphinx_copybutton",
]

# Warning when the Sphinx Tabs extension is used with unknown
# builders (like the dummy builder) - as it doesn't cause errors,
# we can ignore this so we still can treat other warnings as errors.
sphinx_tabs_nowarn = True

# Disable collapsing tabs for codeblocks.
sphinx_tabs_disable_tab_closing = True

# Custom 4O4 page HTML template.
# https://github.com/readthedocs/sphinx-notfound-page
notfound_context = {
    "title": "Page not found",
    "body": """
        <h1>Page not found</h1>
        <p>
            Sorry, we couldn't find that page. It may have been renamed or removed
            in the version of the documentation you're currently browsing.
        </p>
        <p>
            If you're currently browsing the
            <em>latest</em> version of the documentation, try browsing the
            <a href="/en/stable/"><em>stable</em> version of the documentation</a>.
        </p>
        <p>
            Alternatively, use the
            <a href="#" onclick="$('#rtd-search-form [name=\\'q\\']').focus()">Search docs</a>
            box on the left or <a href="/">go to the homepage</a>.
        </p>
    """,
}

# on_rtd is whether we are on readthedocs.org, this line of code grabbed from docs.readthedocs.org
on_rtd = os.environ.get("READTHEDOCS", None) == "True"

# Don't add `/en/latest` prefix during local development.
# This makes it easier to test the custom 404 page by loading `/404.html`
# on a local web server.
if not on_rtd:
    notfound_urls_prefix = ''

# Specify the site name for the Open Graph extension.
ogp_site_name = "Godot Engine documentation"

if not os.getenv("SPHINX_NO_GDSCRIPT"):
    extensions.append("gdscript")

if not os.getenv("SPHINX_NO_DESCRIPTIONS"):
    extensions.append("godot_descriptions")

templates_path = ["_templates"]

# You can specify multiple suffix as a list of string: ['.rst', '.md']
source_suffix = ".rst"
source_encoding = "utf-8-sig"

# The master toctree document
master_doc = "index"

# General information about the project
project = "Godot Engine"
copyright = (
    "2014-present Juan Linietsky, Ariel Manzur and the Godot community (CC BY 3.0)"
)
author = "Juan Linietsky, Ariel Manzur and the Godot community"

# Version info for the project, acts as replacement for |version| and |release|
# The short X.Y version
version = os.getenv("READTHEDOCS_VERSION", "latest")
# The full version, including alpha/beta/rc tags
release = version

# Parse Sphinx tags passed from RTD via environment
env_tags = os.getenv("SPHINX_TAGS")
if env_tags is not None:
    for tag in env_tags.split(","):
        print("Adding Sphinx tag: %s" % tag.strip())
        tags.add(tag.strip())  # noqa: F821

# Language / i18n

supported_languages = {
    "en": "Godot Engine %s documentation in English",
    "de": "Godot Engine %s Dokumentation auf Deutsch",
    "es": "Documentación de Godot Engine %s en español",
    "fr": "Documentation de Godot Engine %s en français",
    "fi": "Godot Engine %s dokumentaatio suomeksi",
    "it": "Godot Engine %s documentazione in italiano",
    "ja": "Godot Engine %sの日本語のドキュメント",
    "ko": "Godot Engine %s 문서 (한국어)",
    "pl": "Dokumentacja Godot Engine %s w języku polskim",
    "pt_BR": "Documentação da Godot Engine %s em Português Brasileiro",
    "ru": "Документация Godot Engine %s на русском языке",
    "uk": "Документація до Godot Engine %s українською мовою",
    "zh_CN": "Godot Engine %s 简体中文文档",
    "zh_TW": "Godot Engine %s 正體中文 (台灣) 文件",
}

# RTD normalized their language codes to ll-cc (e.g. zh-cn),
# but Sphinx did not and still uses ll_CC (e.g. zh_CN).
# `language` is the Sphinx configuration so it needs to be converted back.
language = os.getenv("READTHEDOCS_LANGUAGE", "en")
if "-" in language:
    (lang_name, lang_country) = language.split("-")
    language = lang_name + "_" + lang_country.upper()

if not language in supported_languages.keys():
    print("Unknown language: " + language)
    print("Supported languages: " + ", ".join(supported_languages.keys()))
    print(
        "The configured language is either wrong, or it should be added to supported_languages in conf.py. Falling back to 'en'."
    )
    language = "en"

is_i18n = tags.has("i18n")  # noqa: F821
print("Build language: {}, i18n tag: {}".format(language, is_i18n))

exclude_patterns = ["_build"]

# fmt: off
# These imports should *not* be moved to the start of the file,
# they depend on the sys.path.append call registering "_extensions".
# GDScript syntax highlighting
from gdscript import GDScriptLexer
from sphinx.highlighting import lexers

lexers["gdscript"] = GDScriptLexer()
# fmt: on

smartquotes = False

# Pygments (syntax highlighting) style to use
pygments_style = "sphinx"
highlight_language = "gdscript"

# -- Options for HTML output ----------------------------------------------

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
if on_rtd:
    using_rtd_theme = True

# Theme options
html_theme_options = {
    # if we have a html_logo below, this shows /only/ the logo with no title text
    "logo_only": True,
    # Collapse navigation (False makes it tree-like)
    "collapse_navigation": False,
    # Hide the documentation version name/number under the logo
    "display_version": False,
}

html_title = supported_languages[language] % ( "(" + version + ")" )

# VCS options: https://docs.readthedocs.io/en/latest/vcs.html#github
html_context = {
    "display_github": not is_i18n,  # Integrate GitHub
    "github_user": "godotengine",  # Username
    "github_repo": "godot-docs",  # Repo name
    "github_version": "master",  # Version
    "conf_py_path": "/",  # Path in the checkout to the docs root
    "godot_inject_language_links": True,
    "godot_docs_supported_languages": list(supported_languages.keys()),
    "godot_docs_title": supported_languages[language],
    "godot_docs_basepath": "https://docs.godotengine.org/",
    "godot_docs_suffix": ".html",
    "godot_default_lang": "en",
    "godot_canonical_version": "stable",
    # Distinguish local development website from production website.
    # This prevents people from looking for changes on the production website after making local changes :)
    "godot_title_prefix": "" if on_rtd else "(DEV) ",
    # Set this to `True` when in the `latest` branch to clearly indicate to the reader
    # that they are not reading the `stable` documentation.
    "godot_is_latest": True,
    "godot_version": "4.3",
    # Enables a banner that displays the up-to-date status of each article.
    "godot_show_article_status": True,
    # Display user-contributed notes at the bottom of pages that don't have `:allow_comments: False` at the top.
    "godot_show_article_comments": on_rtd and not is_i18n,
}

html_logo = "img/docs_logo.svg"

# These folders are copied to the documentation's HTML output
html_static_path = ["_static"]

html_extra_path = ["robots.txt"]

# These paths are either relative to html_static_path
# or fully qualified paths (e.g. https://...)
html_css_files = [
    'css/algolia.css',
    'https://cdn.jsdelivr.net/npm/docsearch.js@2/dist/cdn/docsearch.min.css',
    "css/custom.css?10", # Increment the number at the end when the file changes to bust the cache.
]

if not on_rtd:
    html_css_files.append("css/dev.css")

html_js_files = [
    "js/custom.js?7", # Increment the number at the end when the file changes to bust the cache.
]

# Output file base name for HTML help builder
htmlhelp_basename = "GodotEnginedoc"

# -- Options for reStructuredText parser ----------------------------------

# Enable directives that insert the contents of external files
file_insertion_enabled = False

# -- Options for LaTeX output ---------------------------------------------

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        "GodotEngine.tex",
        "Godot Engine Documentation",
        "Juan Linietsky, Ariel Manzur and the Godot community",
        "manual",
    ),
]

# -- Options for linkcheck builder ----------------------------------------

# disable checking urls with about.html#this_part_of_page anchors
linkcheck_anchors = False

linkcheck_timeout = 10

# -- I18n settings --------------------------------------------------------

# Godot localization is handled via https://github.com/godotengine/godot-docs-l10n
# where the main docs repo is a submodule. Therefore the translated material is
# actually in the parent folder of this conf.py, hence the "../".

locale_dirs = ["../sphinx/po/"]
gettext_compact = False

# We want to host the localized images in godot-docs-l10n, but Sphinx does not provide
# the necessary feature to do so. `figure_language_filename` has `{root}` and `{path}`,
# but they resolve to (host) absolute paths, so we can't use them as is to access "../".
# However, Python is glorious and lets us redefine Sphinx's internal method that handles
# `figure_language_filename`, so we do our own post-processing to fix the absolute path
# and point to the parallel folder structure in godot-docs-l10n.
# Note: Sphinx's handling of `figure_language_filename` may change in the future, monitor
# https://github.com/sphinx-doc/sphinx/issues/7768 to see what would be relevant for us.
figure_language_filename = "{root}.{language}{ext}"

cwd = os.getcwd()

sphinx_original_get_image_filename_for_language = sphinx.util.i18n.get_image_filename_for_language


def godot_get_image_filename_for_language(filename, env):
    """
    Hack the absolute path returned by Sphinx based on `figure_language_filename`
    to insert our `../images` relative path to godot-docs-l10n's images folder,
    which mirrors the folder structure of the docs repository.
    The returned string should also be absolute so that `os.path.exists` can properly
    resolve it when trying to concatenate with the original doc folder.
    """
    path = sphinx_original_get_image_filename_for_language(filename, env)
    path = os.path.abspath(os.path.join("../images/", os.path.relpath(path, cwd)))
    return path

sphinx.util.i18n.get_image_filename_for_language = godot_get_image_filename_for_language

# Similar story for the localized class reference, it's out of tree and there doesn't
# seem to be an easy way for us to tweak the toctree to take this into account.
# So we're deleting the existing class reference and adding a symlink instead...
if is_i18n and os.path.exists("../classes/" + language):
    import shutil

    if os.path.islink("classes"):  # Previously made symlink.
        os.unlink("classes")
    else:
        shutil.rmtree("classes")

    os.symlink("../classes/" + language, "classes")

# Couldn't find a way to retrieve variables nor do advanced string
# concat from reST, so had to hardcode this in the "epilog" added to
# all pages. This is used in index.rst to display the Weblate badge.
# On English pages, the badge points to the language-neutral engage page.
rst_epilog = """
.. |weblate_widget| image:: https://hosted.weblate.org/widgets/godot-engine/{image_locale}/godot-docs/287x66-white.png
    :alt: Translation status
    :target: https://hosted.weblate.org/engage/godot-engine{target_locale}/?utm_source=widget
    :width: 287
    :height: 66
""".format(
    image_locale="-" if language == "en" else language,
    target_locale="" if language == "en" else "/" + language,
)
