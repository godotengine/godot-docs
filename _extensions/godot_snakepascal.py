"""
    godot_snakepascal
    ~~~~~~~~~~~~~~~~~

    Sphinx extension that adds a ``:snakepascal:"snake_case;;PascalCase"`` role.
    The preferred syntax to display can be toggled using JavaScript code.
    When this role is used, JavaScript is required for correct display.
    See https://github.com/godotengine/godot-docs/blob/master/_static/js/custom.js
    for the JavaScript code (search for "snakepascal" in that file).
    See https://github.com/godotengine/godot-docs/blob/master/_static/css/custom.css
    for the snake_case/PascalCase chooser theming (search for "snakepascal" in that file).

    :copyright: Copyright 2020 by The Godot Engine Community
    :license: MIT
"""

from docutils import nodes


def snakepascal_role(
    name, rawtext, text, lineno, inliner, options={}, content=[]
):
    node = nodes.literal(rawtext, text, classes=["snakepascal"], **options)
    return [node], []


def setup(app):
    app.add_role("snakepascal", snakepascal_role)

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
