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

from pygments.lexer import Lexer, RegexLexer, include, bygroups, using, \
    default, words, combined, do_insertions
from pygments.util import get_bool_opt, shebang_matches
from pygments.token import Text, Comment, Operator, Keyword, Name, String, \
    Number, Punctuation, Generic, Other, Error
from pygments import unistring as uni

__all__ = ['GDScriptLexer']

line_re = re.compile('.*?\n')


class GDScriptLexer(RegexLexer):
    """
    For `Godot source code <https://www.godotengine.org>`_ source code.
    """

    name = 'GDScript'
    aliases = ['gdscript', 'gd']
    filenames = ['*.gd']
    mimetypes = ['text/x-gdscript', 'application/x-gdscript']

    def innerstring_rules(ttype):
        return [
            # the old style '%s' % (...) string formatting
            (r'%(\(\w+\))?[-#0 +]*([0-9]+|[*])?(\.([0-9]+|[*]))?'
             '[hlL]?[E-GXc-giorsux%]', String.Interpol),
            # backslashes, quotes and formatting signs must be parsed one at a time
            (r'[^\\\'"%\n]+', ttype),
            (r'[\'"\\]', ttype),
            # unhandled string formatting sign
            (r'%', ttype),
            # newlines are an error (use "nl" state)
        ]

    tokens = {
        'root': [
            (r'\n', Text),
            (r'^(\s*)([rRuUbB]{,2})("""(?:.|\n)*?""")',
             bygroups(Text, String.Affix, String.Doc)),
            (r"^(\s*)([rRuUbB]{,2})('''(?:.|\n)*?''')",
             bygroups(Text, String.Affix, String.Doc)),
            (r'[^\S\n]+', Text),
            (r'#.*$', Comment.Single),
            (r'[]{}:(),;[]', Punctuation),
            (r'\\\n', Text),
            (r'\\', Text),
            (r'(in|and|or|not)\b', Operator.Word),
            (r'!=|==|<<|>>|&&|\+=|-=|\*=|/=|%=|&=|\|=|\|\||[-~+/*%=<>&^.!|$]', Operator),
            include('keywords'),
            (r'(func)((?:\s|\\\s)+)', bygroups(Keyword, Text), 'funcname'),
            (r'(class)((?:\s|\\\s)+)', bygroups(Keyword, Text), 'classname'),
            include('builtins'),
            ('([rR]|[uUbB][rR]|[rR][uUbB])(""")',
             bygroups(String.Affix, String.Double), 'tdqs'),
            ("([rR]|[uUbB][rR]|[rR][uUbB])(''')",
             bygroups(String.Affix, String.Single), 'tsqs'),
            ('([rR]|[uUbB][rR]|[rR][uUbB])(")',
             bygroups(String.Affix, String.Double), 'dqs'),
            ("([rR]|[uUbB][rR]|[rR][uUbB])(')",
             bygroups(String.Affix, String.Single), 'sqs'),
            ('([uUbB]?)(""")', bygroups(String.Affix, String.Double),
             combined('stringescape', 'tdqs')),
            ("([uUbB]?)(''')", bygroups(String.Affix, String.Single),
             combined('stringescape', 'tsqs')),
            ('([uUbB]?)(")', bygroups(String.Affix, String.Double),
             combined('stringescape', 'dqs')),
            ("([uUbB]?)(')", bygroups(String.Affix, String.Single),
             combined('stringescape', 'sqs')),
            include('name'),
            include('numbers'),
        ],
        'keywords': [
            (words((
                'and', 'in', 'not', 'or', 'as', 'breakpoint', 'class', 'class_name',
                'extends', 'is', 'func', 'setget', 'signal', 'tool', 'const',
                'enum', 'export', 'onready', 'static', 'var', 'break', 'continue',
                'if', 'elif', 'else', 'for', 'pass', 'return', 'match', 'while',
                'remote', 'master', 'puppet', 'remotesync', 'mastersync',
                'puppetsync'), suffix=r'\b'),
             Keyword),
        ],
        'builtins': [
            (words((
                'Color8', 'ColorN', 'abs', 'acos', 'asin', 'assert', 'atan', 'atan2',
                'bytes2var', 'ceil', 'char', 'clamp', 'convert', 'cos', 'cosh',
                'db2linear', 'decimals', 'dectime', 'deg2rad', 'dict2inst',
                'ease', 'exp', 'floor', 'fmod', 'fposmod', 'funcref', 'hash',
                'inst2dict', 'instance_from_id', 'is_inf', 'is_nan', 'lerp',
                'linear2db', 'load', 'log', 'max', 'min', 'nearest_po2', 'pow',
                'preload', 'print', 'print_stack', 'printerr', 'printraw',
                'prints', 'printt', 'rad2deg', 'rand_range', 'rand_seed',
                'randf', 'randi', 'randomize', 'range', 'round', 'seed', 'sign',
                'sin', 'sinh', 'sqrt', 'stepify', 'str', 'str2var', 'tan',
                'tan', 'tanh', 'type_exist', 'typeof', 'var2bytes', 'var2str',
                'weakref', 'yield'),
                prefix=r'(?<!\.)', suffix=r'\b'),
             Name.Builtin),
            (r'((?<!\.)(self|false|true)|(PI|TAU|NAN|INF)'
             r')\b', Name.Builtin.Pseudo),
            (words((
                'bool', 'int', 'float', 'String', 'NodePath'
                'Vector2', 'Rect2', 'Transform2D',
                'Vector3', 'Rect3', 'Plane', 'Quat', 'Basis', 'Transform',
                'Color', "RID", 'Object', 'NodePath', 'Dictionary',
                'Array', 'PoolByteArray', 'PoolIntArray', 'PoolRealArray',
                'PoolStringArray', 'PoolVector2Array', 'PoolVector3Array', 'PoolColorArray',
                'null',
            ), prefix=r'(?<!\.)', suffix=r'\b'), Name.Builtin.Type),
        ],
        'numbers': [
            (r'(\d+\.\d*|\d*\.\d+)([eE][+-]?[0-9]+)?j?', Number.Float),
            (r'\d+[eE][+-]?[0-9]+j?', Number.Float),
            (r'0[xX][a-fA-F0-9]+', Number.Hex),
            (r'\d+j?', Number.Integer)
        ],
        'name': [
            ('[a-zA-Z_]\w*', Name),
        ],
        'funcname': [
            ('[a-zA-Z_]\w*', Name.Function, '#pop'),
            default('#pop'),
        ],
        'classname': [
            ('[a-zA-Z_]\w*', Name.Class, '#pop')
        ],
        'stringescape': [
            (r'\\([\\abfnrtv"\']|\n|N\{.*?\}|u[a-fA-F0-9]{4}|'
             r'U[a-fA-F0-9]{8}|x[a-fA-F0-9]{2}|[0-7]{1,3})', String.Escape)
        ],
        'strings-single': innerstring_rules(String.Single),
        'strings-double': innerstring_rules(String.Double),
        'dqs': [
            (r'"', String.Double, '#pop'),
            (r'\\\\|\\"|\\\n', String.Escape),  # included here for raw strings
            include('strings-double')
        ],
        'sqs': [
            (r"'", String.Single, '#pop'),
            (r"\\\\|\\'|\\\n", String.Escape),  # included here for raw strings
            include('strings-single')
        ],
        'tdqs': [
            (r'"""', String.Double, '#pop'),
            include('strings-double'),
            (r'\n', String.Double)
        ],
        'tsqs': [
            (r"'''", String.Single, '#pop'),
            include('strings-single'),
            (r'\n', String.Single)
        ],
    }

def setup(sphinx):
    sphinx.add_lexer('gdscript', GDScriptLexer())

    return {
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
