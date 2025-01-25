# -*- coding: utf-8 -*-
"""
    godot_descriptions
    ~~~~~~~~~~~~~~~~~~

    Sphinx extension to automatically generate HTML meta description tags
    for all pages. Also comes with some special support for Godot class docs.

    :copyright: Copyright 2021 by The Godot Engine Community
    :license: MIT.

    based on the work of Takayuki Shimizukawa on OpenGraph support for Sphinx,
    see: https://github.com/sphinx-contrib/ogp
"""

import re
from docutils import nodes
from sphinx import addnodes


class DescriptionGenerator:
    def __init__(self, document, pagename="", n_sections_max=3, max_length=220):
        self.document = document
        self.text_list = []
        self.max_length = max_length
        self.current_length = 0
        self.n_sections = 0
        self.n_sections_max = n_sections_max
        self.pagename = pagename
        self.is_class = pagename.startswith("classes/")
        self.stop_word_reached = False

    def dispatch_visit(self, node):
        if (
            self.stop_word_reached
            or self.current_length > self.max_length
            or self.n_sections > self.n_sections_max
        ):
            return

        if isinstance(node, addnodes.compact_paragraph) and node.get("toctree"):
            raise nodes.SkipChildren

        add = True

        if isinstance(node, nodes.paragraph):
            text = node.astext()

            if self.is_class:
                # Skip OOP hierarchy info for description
                if (
                    text.startswith("Inherits:")
                    or text.startswith("Inherited By:")
                    or text.strip() == "Example:"
                ):
                    add = False

                # If we're in a class doc and reached the first table,
                # stop adding to the description
                if text.strip() == "Properties":
                    self.stop_word_reached = True
                    add = False

            if add:
                self.text_list.append(text)
                self.current_length = self.current_length + len(text)

        if add and isinstance(node, nodes.section):
            self.n_sections += 1

    def dispatch_departure(self, node):
        pass

    def format_description(self, desc):
        # Replace newlines with spaces
        desc = re.sub("\r|\n", " ", desc)

        # Replace multiple spaces with single spaces
        desc = re.sub("\\s+", " ", desc)

        # Escape double quotes for HTML
        desc = re.sub('"', "&quot;", desc)

        return desc

    def create_description(self, cutoff_suffix="..."):
        text = " ".join(self.text_list)

        text = self.format_description(text)

        # Cut to self.max_length, add cutoff_suffix at end
        if len(text) > self.max_length:
            text = text[: self.max_length - len(cutoff_suffix)].strip() + cutoff_suffix

        return text


def generate_description(app, pagename, templatename, context, doctree):
    if not doctree:
        return

    generator = DescriptionGenerator(doctree, pagename)
    doctree.walkabout(generator)

    description = (
        '<meta name="description" content="' + generator.create_description() + '" />\n'
    )

    if not '<meta name="description"' in context["metatags"]:
        context["metatags"] += description


def setup(app):
    # Hook into Sphinx for all pages to
    # generate meta description tag and add to meta tag list
    app.connect("html-page-context", generate_description)

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
