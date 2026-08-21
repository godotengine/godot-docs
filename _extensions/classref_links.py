# -*- coding: utf-8 -*-
"""
    classref_links
    ~~~~~~~~~~~~~~

    Sphinx extension to format links to Godot's class reference,
    including classes, methods, properties, etc.

    :copyright: Copyright 2026 by The Godot Engine Community
    :license: MIT.
"""

import re
from dataclasses import dataclass

from docutils import nodes

from sphinx.addnodes import pending_xref
from sphinx.application import Sphinx
from sphinx.roles import XRefRole
from sphinx.util.typing import ExtensionMetadata


_NO_CLASS = "~"
_THEME_ITEMS = r"(?:theme_(?:color|constant|font_size|font|icon|style))"
_CLASS_DEFINITION = r"class_([A-Za-z0-9]+)(?:_(private_)?({_THEME_ITEMS}|[a-z]+)_([_a-zA-Z0-9]+))?"
_ENUM = r"enum_([A-Za-z0-9]+)_([A-Za-z0-9]+)"
_CLASSREF_RE = re.compile(rf"^({_NO_CLASS})?(?:{_CLASS_DEFINITION}|{_ENUM})$")


def parse_classref_label(label: str) -> str:
    match = _CLASSREF_RE.fullmatch(label)
    if match is None:
        return label

    no_class = match.group(1) == _NO_CLASS
    is_enum = match.group(6) != None
    class_name = match.group(7) if is_enum else match.group(2)
    private_method = False if is_enum else match.group(3) == "private"
    definition_type = "enum" if is_enum else match.group(4)
    identifier = match.group(7) if is_enum else match.group(5)

    if identifier == None:
        return class_name
    if private_method:
        identifier = f"_{identifier}"
    title = identifier
    if not no_class:
        title = f"{class_name}.{identifier}"
    if definition_type == "method":
        title += "()"
    return title


class ClassRefRole(XRefRole):
    def __init__(self) -> None:
        super().__init__(
            lowercase=True,
            innernodeclass=nodes.inline,
            warn_dangling=True,
        )

    def process_link(
        self,
        env,
        refnode,
        has_explicit_title: bool,
        title: str,
        target: str,
    ) -> tuple[str, str]:
        if target[0] == _NO_CLASS:
            target = target[1:]
        return parse_classref_label(title), target

    def run(self) -> tuple[list[nodes.Node], list[nodes.system_message]]:
        self.has_explicit_title = True
        result_nodes, messages = super().run()
        for node in result_nodes:
            if isinstance(node, pending_xref):
                node["refdomain"] = "std"
                node["reftype"] = "ref"
        return result_nodes, messages


def setup(app: Sphinx) -> ExtensionMetadata:
    app.add_role("classref", ClassRefRole())

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
