# -*- coding: utf-8 -*-
"""
    spaces_to_tabs
    ~~~~~~~~~~~~~~~~~~

    Sphinx extension to convert codeblock spaces to tabs

    :copyright: Copyright 2023-present by The Godot Engine Community
    :license: MIT.
"""

import glob

parse_begin = "  <section id="
parse_end = """

</div>
</div>"""

def convert_spaces_to_tabs(app, exception):
    for html in glob.iglob(app.outdir + "/**/*.html", recursive=True):
        with open(html, "r", encoding="utf-8", newline="\n") as f:
            lines = f.read()
            begin = lines.find(parse_begin)
            end = lines.find(parse_end)
            body_spaces = lines[begin:end]
            body_tabs = body_spaces.replace("\n    ", "\n\t")
            while body_tabs.find("\t    ") != -1:
                body_tabs = body_tabs.replace("\t    ", "\t\t")
        with open(html, "w", encoding="utf-8", newline="\n") as f:
            f.write(lines.replace(body_spaces, body_tabs))

def setup(sphinx):
    sphinx.connect("build-finished", convert_spaces_to_tabs)

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
