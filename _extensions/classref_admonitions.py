# -*- coding: utf-8 -*-
"""
    class_ref_admonitions
    ~~~~~~~~~~~~~~~~~~~~~

    Sphinx extension to format Godot's classref admonitions.

    :copyright: Copyright 2026 by The Godot Engine Community
    :license: MIT.
"""

import re
from docutils import nodes
from docutils.parsers.rst import Directive
from sphinx.writers.html5 import HTML5Translator


class classref_admonition(nodes.General, nodes.Element):
    pass


class classref_important(classref_admonition):
    pass


class classref_note(classref_admonition):
    pass


class classref_tip(classref_admonition):
    pass


class classref_warning(classref_admonition):
    pass


class BaseClassrefDirective(Directive):
    has_content = True

    title = ""
    css_class = ""
    node_class = classref_admonition

    def run(self):
        self.assert_has_content()

        node = self.node_class()
        node["title"] = self.title
        node["classes"].append(self.css_class)

        self.state.nested_parse(
            self.content,
            self.content_offset,
            node,
        )

        return [node]


class ClassrefNoteDirective(BaseClassrefDirective):
    node_class = classref_note
    title = "Note"
    css_class = "note classref-admonition"


class ClassrefWarningDirective(BaseClassrefDirective):
    node_class = classref_warning
    title = "Warning"
    css_class = "warning classref-admonition"


class ClassrefTipDirective(BaseClassrefDirective):
    node_class = classref_tip
    title = "Tip"
    css_class = "tip classref-admonition"


class ClassrefImportantDirective(BaseClassrefDirective):
    node_class = classref_important
    title = "Important"
    css_class = "important classref-admonition"


def visit_inline_html(self, node):
    classes = " ".join(node["classes"])
    self.body.append(f'<p class="{classes}">')
    self.body.append(f'<span class="admonition-title">{node["title"]}:</span> ')


def depart_inline_html(self, node):
    self.body.append("</p>")


def setup(app):
    app.set_translator("html", ClassrefAdmonitionHTMLTranslator, override=True)
    for node in (
        classref_important,
        classref_note,
        classref_tip,
        classref_warning,
    ):
        app.add_node(node, html=(visit_inline_html, depart_inline_html))
    app.add_directive("classref_important", ClassrefImportantDirective)
    app.add_directive("classref_note", ClassrefNoteDirective)
    app.add_directive("classref_tip", ClassrefTipDirective)
    app.add_directive("classref_warning", ClassrefWarningDirective)

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }


class ClassrefAdmonitionHTMLTranslator(HTML5Translator):
    def visit_paragraph(self, node):
        if isinstance(node.parent, classref_admonition):
            return
        super().visit_paragraph(node)

    def depart_paragraph(self, node):
        if isinstance(node.parent, classref_admonition):
            return
        super().depart_paragraph(node)
