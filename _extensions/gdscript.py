# -*- coding: utf-8 -*-
"""
    pygments.lexers.gdscript
    ~~~~~~~~~~~~~~~~~~~~~~

    Lexer for GDScript.

    :copyright: Copyright 2xxx by The Godot Engine Community
    :license: MIT.

    modified by Daniel J. Ramirez <djrmuv@gmail.com> based on the original python.py pygment
    further expanded and consolidated with the godot-docs lexer by Zackery R. Smith <zackery.smith82307@gmail.com> and Ste.
"""

import re
from pygments.lexer import RegexLexer, include, bygroups, words, combined
from pygments.token import (
    Keyword,
    Literal,
    Name,
    Comment,
    String,
    Number,
    Operator,
    Whitespace,
    Punctuation,
)

__all__ = ["GDScriptLexer"]


class GDScriptLexer(RegexLexer):
    """
    For GDScript source code.
    """

    name = "GDScript"
    url = "https://www.godotengine.org"
    aliases = ["gdscript", "gd"]
    filenames = ["*.gd"]
    mimetypes = ["text/x-gdscript", "application/x-gdscript"]

    @staticmethod
    def get_classes(directory: str) -> tuple[str]:
        classes = []
        with open(f"{directory}/index.rst", "r", encoding="utf-8") as file:
            lines = file.readlines()

        inside_toctree = False
        inside_toctree_body = False
        skip_this_block = False

        for i, line in enumerate(lines):
            stripped = line.strip()

            if stripped.startswith(".. toctree::"):
                inside_toctree = True
                skip_this_block = False
                inside_toctree_body = False
                continue

            if not inside_toctree:
                continue

            if stripped.startswith(":name:"):
                name = stripped.split(":", 2)[-1].strip()
                if name in ["toc-class-ref-variants", "toc-class-ref-globals"]:
                    skip_this_block = True
                continue

            if skip_this_block or stripped.startswith(":"):
                continue

            # Avoid skipping the empty line right before the body of the toc
            if not inside_toctree_body and stripped == "":
                inside_toctree_body = True
                continue

            if not line.startswith("    ") or stripped.startswith(".. "):
                inside_toctree = False
                continue

            if stripped.startswith("class_"):
                # Since everything is lowercase in the index, get the actual casing from the file
                with open(f"{directory}/{stripped}.rst", "r", encoding="utf-8") as class_file:
                    for class_line in class_file:
                        match = re.match(r"_class_(\w+):", class_line)
                        if match:
                            classes.append(match.group(1))
        return tuple(classes)

    # taken from pygments/gdscript.py
    @staticmethod
    def inner_string_rules(ttype):
        return [
            # the old style '%s' % (...) string formatting
            (
                r"%(\(\w+\))?[-#0 +]*([0-9]+|[*])?(\.([0-9]+|[*]))?"
                "[hlL]?[E-GXc-giorsux%]",
                String.Interpol,
            ),
            # backslashes, quotes, and formatting signs must be parsed one at a time
            (r'[^\\\'"%\n]+', ttype),
            (r'[\'"\\]', ttype),
            # unhandled string formatting sign
            (r"%", ttype),
            # newlines are an error (use "nl" state)
        ]

    tokens = {
        "whitespace": [(r"\s+", Whitespace)],
        "comment": [
            (r"##.*$", Comment.Doc),
            (r"#(?:end)?region.*$", Comment.Region),
            (r"#.*$", Comment.Single),
        ],
        "punctuation": [
            (r"[]{}(),:;[]", Punctuation),
            (r":\n", Punctuation),
            (r"\\", Punctuation),
        ],
        # NOTE: from github.com/godotengine/godot-docs
        "keyword": [
            (
                words(
                    (
                        # modules/gdscript/gdscript.cpp - GDScriptLanguage::get_reserved_words()
                        # Declarations.
                        "class",
                        "class_name",
                        "const",
                        "enum",
                        "extends",
                        "func",
                        "namespace",  # Reserved for potential future use.
                        "signal",
                        "static",
                        "trait",  # Reserved for potential future use.
                        "var",
                        # Other keywords.
                        "await",
                        "breakpoint",
                        "self",
                        "super",
                        "yield",  # Reserved for potential future use.
                        # Not really keywords, but used in property syntax.
                        # also colored like functions, not keywords
                        #"set",
                        #"get",
                    ),
                    suffix=r"\b",
                ),
                Keyword,
            ),
            (
                words(
                    (
                        # modules/gdscript/gdscript.cpp - GDScriptLanguage::get_reserved_words()
                        # Control flow.
                        "break",
                        "continue",
                        "elif",
                        "else",
                        "for",
                        "if",
                        "match",
                        "pass",
                        "return",
                        "when",
                        "while",
                        "yield",
                    ),
                    suffix=r"\b",
                ),
                # Custom control flow class used to give control flow keywords a different color,
                # like in the Godot editor.
                Keyword.ControlFlow,
            ),
        ],
        "builtin": [
            (
                words(
                    ("true", "false", "PI", "TAU", "NAN", "INF", "null"),
                    prefix=r"(?<!\.)",
                    suffix=r"\b",
                ),
                Literal,
            ),
            # NOTE: from github.com/godotengine/godot-docs
            (
                words(
                    (
                        # doc/classes/@GlobalScope.xml
                        "abs",
                        "absf",
                        "absi",
                        "acos",
                        "acosh",
                        "angle_difference",
                        "asin",
                        "asinh",
                        "atan",
                        "atan2",
                        "atanh",
                        "bezier_derivative",
                        "bezier_interpolate",
                        "bytes_to_var",
                        "bytes_to_var_with_objects",
                        "ceil",
                        "ceilf",
                        "ceili",
                        "clamp",
                        "clampf",
                        "clampi",
                        "cos",
                        "cosh",
                        "cubic_interpolate",
                        "cubic_interpolate_angle",
                        "cubic_interpolate_angle_in_time",
                        "cubic_interpolate_in_time",
                        "db_to_linear",
                        "deg_to_rad",
                        "ease",
                        "error_string",
                        "exp",
                        "floor",
                        "floorf",
                        "floori",
                        "fmod",
                        "fposmod",
                        "hash",
                        "instance_from_id",
                        "inverse_lerp",
                        "is_equal_approx",
                        "is_finite",
                        "is_inf",
                        "is_instance_id_valid",
                        "is_instance_valid",
                        "is_nan",
                        "is_same",
                        "is_zero_approx",
                        "lerp",
                        "lerp_angle",
                        "lerpf",
                        "linear_to_db",
                        "log",
                        "max",
                        "maxf",
                        "maxi",
                        "min",
                        "minf",
                        "mini",
                        "move_toward",
                        "nearest_po2",
                        "pingpong",
                        "posmod",
                        "pow",
                        "print",
                        "print_rich",
                        "print_verbose",
                        "printerr",
                        "printraw",
                        "prints",
                        "printt",
                        "push_error",
                        "push_warning",
                        "rad_to_deg",
                        "rand_from_seed",
                        "randf",
                        "randf_range",
                        "randfn",
                        "randi",
                        "randi_range",
                        "randomize",
                        "remap",
                        "rid_allocate_id",
                        "rid_from_int64",
                        "rotate_toward",
                        "round",
                        "roundf",
                        "roundi",
                        "seed",
                        "sign",
                        "signf",
                        "signi",
                        "sin",
                        "sinh",
                        "smoothstep",
                        "snapped",
                        "snappedf",
                        "snappedi",
                        "sqrt",
                        "step_decimals",
                        "str",
                        "str_to_var",
                        "tan",
                        "tanh",
                        "type_convert",
                        "type_string",
                        "typeof",
                        "var_to_bytes",
                        "var_to_bytes_with_objects",
                        "var_to_str",
                        "weakref",
                        "wrap",
                        "wrapf",
                        "wrapi",

                        # modules/gdscript/doc_classes/@GDScript.xml
                        "Color8",
                        "assert",
                        "char",
                        "convert",
                        "dict_to_inst",
                        "get_stack",
                        "inst_to_dict",
                        "is_instance_of",
                        "len",
                        "load",
                        "ord",
                        "preload",
                        "print_debug",
                        "print_stack",
                        "range",
                        "type_exists",
                    ),
                    prefix=r"(?<!\.)",
                    suffix=r"\b",
                ),
                Name.Builtin.Function,
            ),
            (r"((?<!\.)(self)" r")\b", Name.Builtin.Pseudo),
            # NOTE: from github.com/godotengine/godot-docs
            (
                words(
                    (
                        # core/variant/variant.cpp - Variant::get_type_name()
                        # `Nil` is excluded because it is not allowed in GDScript.
                        "bool",
                        "int",
                        "float",
                        "String",
                        "Vector2",
                        "Vector2i",
                        "Rect2",
                        "Rect2i",
                        "Transform2D",
                        "Vector3",
                        "Vector3i",
                        "Vector4",
                        "Vector4i",
                        "Plane",
                        "AABB",
                        "Quaternion",
                        "Basis",
                        "Transform3D",
                        "Projection",
                        "Color",
                        "RID",
                        "Object",
                        "Callable",
                        "Signal",
                        "StringName",
                        "NodePath",
                        "Dictionary",
                        "Array",
                        "PackedByteArray",
                        "PackedInt32Array",
                        "PackedInt64Array",
                        "PackedFloat32Array",
                        "PackedFloat64Array",
                        "PackedStringArray",
                        "PackedVector2Array",
                        "PackedVector3Array",
                        "PackedColorArray",
                        "PackedVector4Array",
                        # The following are also considered types in GDScript.
                        "Variant",
                        "void",
                    ),
                    prefix=r"(?<!\.)",
                    suffix=r"\b",
                ),
                Name.Builtin.Type,
            ),
            # copied from https://docs.godotengine.org/en/stable/classes/index.html
            (
                words(
                    get_classes("./classes/"),
                    prefix=r"(?<!\.)",
                    suffix=r"\b",
                ),
                Name.Builtin,
            ),
            # NOTE: from github.com/godotengine/godot-docs
            (
                words(
                    (
                        # modules/gdscript/doc_classes/@GDScript.xml
                        "@abstract",
                        "@export",
                        "@export_category",
                        "@export_color_no_alpha",
                        "@export_custom",
                        "@export_dir",
                        "@export_enum",
                        "@export_exp_easing",
                        "@export_file",
                        "@export_file_path",
                        "@export_flags",
                        "@export_flags_2d_navigation",
                        "@export_flags_2d_physics",
                        "@export_flags_2d_render",
                        "@export_flags_3d_navigation",
                        "@export_flags_3d_physics",
                        "@export_flags_3d_render",
                        "@export_flags_avoidance",
                        "@export_global_dir",
                        "@export_global_file",
                        "@export_group",
                        "@export_multiline",
                        "@export_node_path",
                        "@export_placeholder",
                        "@export_range",
                        "@export_storage",
                        "@export_subgroup",
                        "@export_tool_button",
                        "@icon",
                        "@onready",
                        "@rpc",
                        "@static_unload",
                        "@tool",
                        "@warning_ignore",
                        "@warning_ignore_restore",
                        "@warning_ignore_start",
                    ),
                    prefix=r"(?<!\.)",
                    suffix=r"\b",
                ),
                Name.Decorator,
            ),
        ],
        "operator": [
            (
                r"!=|==|<<|>>|&&|\+=|-=|\*=|/=|%=|&=|\|=|\|\||[-~+/*%=<>&^.!|$]",
                Operator,
            ),
            (r"(in|is|and|as|or|not)\b", Operator.Word),
        ],
        "number": [
            (r"([\d_]+\.[\d_]*|[\d_]*\.[\d_]+)([eE][+-]?[\d_]+)?", Number.Float),
            (r"[\d_]+[eE][+-]?[\d_]+", Number.Float),
            (r"0[xX][a-fA-F\d_]+", Number.Hex),
            (r"(-)?0[bB]([01]|(?<=[01])_)+", Number.Bin),
            (r"[\d_]+", Number.Integer),
        ],
        "name": [(r"[a-zA-Z_]\w*", Name)],
        "typehint": [
            (r"[a-zA-Z_]\w*", Name.Class, "#pop"),
        ],
        "string_escape": [
            (
                r'\\([\\abfnrtv"\']|\n|N\{.*?\}|u[a-fA-F0-9]{4}|'
                r"U[a-fA-F0-9]{6}|x[a-fA-F0-9]{2}|[0-7]{1,3})",
                String.Escape,
            )
        ],
        "string_single": inner_string_rules(String.Single),
        "string_double": inner_string_rules(String.Double),
        "string_other": inner_string_rules(String.Other),
        "string_stringname": inner_string_rules(String.StringName),
        "string_nodepath": inner_string_rules(String.NodePath),
        "double_quotes": [
            (r'"', String.Double, "#pop"),
            (r'\\\\|\\"|\\\n', String.Escape),  # included here for raw strings
            include("string_double"),
        ],
        "single_quotes": [
            (r"'", String.Single, "#pop"),
            (r"\\\\|\\'|\\\n", String.Escape),  # included here for raw strings
            include("string_single"),
        ],
        "triple_double_quotes": [
            (r'"""', String.Double, "#pop"),
            include("string_double"),
            include("whitespace"),
        ],
        "triple_single_quotes": [
            (r"'''", String.Single, "#pop"),
            include("string_single"),
            include("whitespace"),
        ],
        "node_reference": [
            (r'[\$%]"', String.Other, include("node_reference_double")),
            (r"[\$%]'", String.Other, include("node_reference_single")),
            (r"[\$%][A-Za-z_][\w/]*/?", String.Other),
        ],
        "node_reference_double": [
            (r'"', String.Other, "#pop"),
            include("string_other"),
        ],
        "node_reference_single": [
            (r"'", String.Other, "#pop"),
            include("string_other"),
        ],
        "stringname": [
            (r'[&]"', String.StringName, include("stringname_double")),
            (r"[&]'", String.StringName, include("stringname_single")),
        ],
        "stringname_double": [
            (r'"', String.StringName, "#pop"),
            include("string_stringname"),
        ],
        "stringname_single": [
            (r"'", String.StringName, "#pop"),
            include("string_stringname"),
        ],
        "nodepath": [
            (r'[\^]"', String.NodePath, include("nodepath_double")),
            (r"[\^]'", String.NodePath, include("nodepath_single")),
        ],
        "nodepath_double": [
            (r'"', String.NodePath, "#pop"),
            include("string_nodepath"),
        ],
        "nodepath_single": [
            (r"'", String.NodePath, "#pop"),
            include("string_nodepath"),
        ],
        "function_name": [(r"[a-zA-Z_]\w*", Name.Function.Declaration, "#pop")],
        "enum_name": [(r"[a-zA-Z_]\w*", Name, "#pop")],
        "function": [
            (r"\b([a-zA-Z_]\w*)\s*(?=\()", Name.Function),
            (
                # colored like functions, even without braces
                words(("set", "get",), suffix=r"\b", ),
                Name.Function,
            ),
        ],

        #######################################################################
        # LEXER ENTRY POINT
        #######################################################################
        "root": [
            include("whitespace"),
            include("comment"),
            include("punctuation"),
            include("builtin"),
            # strings
            include("stringname"),
            include("nodepath"),
            include("node_reference"),
            (
                '(r)(""")',
                bygroups(String.Affix, String.Double),
                "triple_double_quotes",
            ),
            (
                "(r)(''')",
                bygroups(String.Affix, String.Single),
                "triple_single_quotes",
            ),
            (
                '(r)(")',
                bygroups(String.Affix, String.Double),
                "double_quotes",
            ),
            (
                "(r)(')",
                bygroups(String.Affix, String.Single),
                "single_quotes",
            ),
            (
                '(r?)(""")',
                bygroups(String.Affix, String.Double),
                combined("string_escape", "triple_double_quotes"),
            ),
            (
                "(r?)(''')",
                bygroups(String.Affix, String.Single),
                combined("string_escape", "triple_single_quotes"),
            ),
            (
                '(r?)(")',
                bygroups(String.Affix, String.Double),
                combined("string_escape", "double_quotes"),
            ),
            (
                "(r?)(')",
                bygroups(String.Affix, String.Single),
                combined("string_escape", "single_quotes"),
            ),
            # consider Name after a . as instance/members variables
            (r"(?<!\.)(\.)([a-zA-Z_]\w*)\b(?!\s*\()", bygroups(Operator, Name.Variable.Instance)),
            include("operator"),
            # Lookahead to not match the start of function_name to dodge errors on nameless lambdas
            (r"(func)(\s+)(?=[a-zA-Z_])", bygroups(Keyword, Whitespace), "function_name"),
            (r"(enum)(\s+)(?=[a-zA-Z_])", bygroups(Keyword, Whitespace), "enum_name"),
            include("keyword"),
            include("function"),
            # NOTE:
            #   This matches all PascalCase as a class. If this raises issues
            #   please report it.
            # see: https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_styleguide.html#naming-conventions
            #(r"\s*([A-Z][a-zA-Z0-9_]*)", Name.Class),
            # Only PascalCase, but exclude SCREAMING_SNAKE for constants
            (r"\b([A-Z][a-z0-9]+(?:[A-Z][a-z0-9]+)*)\b", Name.Class),
            include("name"),
            include("number"),
        ],
    }


def setup(sphinx):
    sphinx.add_lexer("gdscript", GDScriptLexer)

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
