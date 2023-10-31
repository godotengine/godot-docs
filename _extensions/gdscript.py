# -*- coding: utf-8 -*-
"""
    pygments.lexers.gdscript
    ~~~~~~~~~~~~~~~~~~~~~~

    Lexer for GDScript.

    :copyright: Copyright 2xxx by The Godot Engine Community
    :license: MIT.

    modified by Daniel J. Ramirez <djrmuv@gmail.com> based on the original python.py pygment
"""

import re

from pygments.lexer import (
    RegexLexer,
    include,
    bygroups,
    default,
    words,
    combined,
)
from pygments.token import (
    Text,
    Comment,
    Operator,
    Keyword,
    Name,
    String,
    Number,
    Punctuation,
    Whitespace,
)

__all__ = ["GDScriptLexer"]

line_re = re.compile(".*?\n")


class GDScriptLexer(RegexLexer):
    """
    For `GDScript source code <https://www.godotengine.org>`_.
    """

    name = "GDScript"
    aliases = ["gdscript", "gd"]
    filenames = ["*.gd"]
    mimetypes = ["text/x-gdscript", "application/x-gdscript"]

    def innerstring_rules(ttype):
        return [
            # the old style '%s' % (...) string formatting
            (
                r"%(\(\w+\))?[-#0 +]*([0-9]+|[*])?(\.([0-9]+|[*]))?"
                "[hlL]?[E-GXc-giorsux%]",
                String.Interpol,
            ),
            # backslashes, quotes and formatting signs must be parsed one at a time
            (r'[^\\\'"%\n]+', ttype),
            (r'[\'"\\]', ttype),
            # unhandled string formatting sign
            (r"%", ttype),
            # newlines are an error (use "nl" state)
        ]

    tokens = {
        "root": [
            (r"\n", Whitespace),
            (
                r'^(\s*)([rRuUbB]{,2})("""(?:.|\n)*?""")',
                bygroups(Whitespace, String.Affix, String.Doc),
            ),
            (
                r"^(\s*)([rRuUbB]{,2})('''(?:.|\n)*?''')",
                bygroups(Whitespace, String.Affix, String.Doc),
            ),
            (r"[^\S\n]+", Whitespace),
            (r"#.*$", Comment.Single),
            (r"[]{}:(),;[]", Punctuation),
            (r"(\\)(\n)", Whitespace),
            (r"\\", Text),
            (r"(in|and|or|not)\b", Operator.Word),
            (
                r"!=|==|<<|>>|&&|\+=|-=|\*=|/=|%=|&=|\|=|\|\||[-~+/*%=<>&^.!|$]",
                Operator,
            ),
            include("keywords"),
            include("control_flow_keywords"),
            (r"(func)((?:\s|\\\s)+)", bygroups(Keyword, Whitespace), "funcname"),
            (r"(class)((?:\s|\\\s)+)", bygroups(Keyword, Whitespace), "classname"),
            include("builtins"),
            include("decorators"),
            (
                '([rR]|[uUbB][rR]|[rR][uUbB])(""")',
                bygroups(String.Affix, String.Double),
                "tdqs",
            ),
            (
                "([rR]|[uUbB][rR]|[rR][uUbB])(''')",
                bygroups(String.Affix, String.Single),
                "tsqs",
            ),
            (
                '([rR]|[uUbB][rR]|[rR][uUbB])(")',
                bygroups(String.Affix, String.Double),
                "dqs",
            ),
            (
                "([rR]|[uUbB][rR]|[rR][uUbB])(')",
                bygroups(String.Affix, String.Single),
                "sqs",
            ),
            (
                '([uUbB]?)(""")',
                bygroups(String.Affix, String.Double),
                combined("stringescape", "tdqs"),
            ),
            (
                "([uUbB]?)(''')",
                bygroups(String.Affix, String.Single),
                combined("stringescape", "tsqs"),
            ),
            (
                '([uUbB]?)(")',
                bygroups(String.Affix, String.Double),
                combined("stringescape", "dqs"),
            ),
            (
                "([uUbB]?)(')",
                bygroups(String.Affix, String.Single),
                combined("stringescape", "sqs"),
            ),
            include("name"),
            include("numbers"),
        ],
        "keywords": [
            (
                words(
                    (
                        "and",
                        "await",
                        "in",
                        "get",
                        "set",
                        "not",
                        "or",
                        "as",
                        "breakpoint",
                        "class",
                        "class_name",
                        "extends",
                        "is",
                        "func",
                        "signal",
                        "const",
                        "enum",
                        "static",
                        "var",
                        "super",
                    ),
                    suffix=r"\b",
                ),
                Keyword,
            ),
        ],
        "control_flow_keywords": [
            (
                words(
                    (
                        "break",
                        "continue",
                        "elif",
                        "else",
                        "if",
                        "for",
                        "match",
                        "pass",
                        "return",
                        "when",
                        "while",
                    ),
                    suffix=r"\b",
                ),
                # Custom control flow class used to give control flow keywords a different color,
                # like in the Godot editor.
                Keyword.ControlFlow,
            ),
        ],
        "builtins": [
            (
                words(
                    (
                        # doc/classes/@GlobalScope.xml
                        "abs",
                        "absf",
                        "absi",
                        "acos",
                        "asin",
                        "atan",
                        "atan2",
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
                        "len",
                        "load",
                        "preload",
                        "print_debug",
                        "print_stack",
                        "range",
                        "str",
                        "type_exists",
                    ),
                    prefix=r"(?<!\.)",
                    suffix=r"\b",
                ),
                Name.Builtin,
            ),
            (r"((?<!\.)(self|super|false|true)|(PI|TAU|NAN|INF)" r")\b", Name.Builtin.Pseudo),
            (
                words(
                    (
                        "bool",
                        "int",
                        "float",
                        "String",
                        "StringName",
                        "NodePath",
                        "Vector2",
                        "Vector2i",
                        "Rect2",
                        "Rect2i",
                        "Transform2D",
                        "Vector3",
                        "Vector3i",
                        "AABB",
                        "Plane",
                        "Quaternion",
                        "Basis",
                        "Transform3D",
                        "Color",
                        "RID",
                        "Object",
                        "Dictionary",
                        "Array",
                        "PackedByteArray",
                        "PackedInt32Array",
                        "PackedInt64Array",
                        "PackedFloat32Array",
                        "PackedFloat64Array",
                        "PackedStringArray",
                        "PackedVector2Array",
                        "PackedVector2iArray",
                        "PackedVector3Array",
                        "PackedVector3iArray",
                        "PackedColorArray",
                        "null",
                        "void",
                    ),
                    prefix=r"(?<!\.)",
                    suffix=r"\b",
                ),
                Name.Builtin.Type,
            ),
        ],
        "decorators": [
            (
                words(
                    (
                        "@export",
                        "@export_category",
                        "@export_color_no_alpha",
                        "@export_dir",
                        "@export_enum",
                        "@export_exp_easing",
                        "@export_file",
                        "@export_flags",
                        "@export_flags_2d_navigation",
                        "@export_flags_2d_physics",
                        "@export_flags_2d_render",
                        "@export_flags_3d_navigation",
                        "@export_flags_3d_physics",
                        "@export_flags_3d_render",
                        "@export_global_dir",
                        "@export_global_file",
                        "@export_group",
                        "@export_multiline",
                        "@export_node_path",
                        "@export_placeholder",
                        "@export_range",
                        "@export_subgroup",
                        "@icon",
                        "@onready",
                        "@rpc",
                        "@tool",
                        "@warning_ignore",
                    ),
                    prefix=r"(?<!\.)",
                    suffix=r"\b",
                ),
                Name.Decorator,
            ),
        ],
        "numbers": [
            (
                r"(-)?((\d|(?<=\d)_)+\.(\d|(?<=\d)_)*|(\d|(?<=\d)_)*\.(\d|(?<=\d)_)+)([eE][+-]?(\d|(?<=\d)_)+)?j?",
                Number.Float,
            ),
            (r"(-)?(\d|(?<=\d)_)+[eE][+-]?(\d|(?<=\d)_)+j?", Number.Float),
            (r"(-)?0[xX]([a-fA-F0-9]|(?<=[a-fA-F0-9])_)+", Number.Hex),
            (r"(-)?0[bB]([01]|(?<=[01])_)+", Number.Bin),
            (r"(-)?(\d|(?<=\d)_)+j?", Number.Integer),
        ],
        "name": [(r"@?[a-zA-Z_]\w*", Name)],
        "funcname": [(r"[a-zA-Z_]\w*", Name.Function, "#pop"), default("#pop")],
        "classname": [(r"[a-zA-Z_]\w*", Name.Class, "#pop")],
        "stringescape": [
            (
                r'\\([\\abfnrtv"\']|\n|N\{.*?\}|u[a-fA-F0-9]{4}|'
                r"U[a-fA-F0-9]{8}|x[a-fA-F0-9]{2}|[0-7]{1,3})",
                String.Escape,
            )
        ],
        "strings-single": innerstring_rules(String.Single),
        "strings-double": innerstring_rules(String.Double),
        "dqs": [
            (r'"', String.Double, "#pop"),
            (r'\\\\|\\"|\\\n', String.Escape),  # included here for raw strings
            include("strings-double"),
        ],
        "sqs": [
            (r"'", String.Single, "#pop"),
            (r"\\\\|\\'|\\\n", String.Escape),  # included here for raw strings
            include("strings-single"),
        ],
        "tdqs": [
            (r'"""', String.Double, "#pop"),
            include("strings-double"),
            (r"\n", Whitespace),
        ],
        "tsqs": [
            (r"'''", String.Single, "#pop"),
            include("strings-single"),
            (r"\n", Whitespace),
        ],
    }


def setup(sphinx):
    sphinx.add_lexer("gdscript", GDScriptLexer)

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
