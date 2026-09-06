
from pygments.lexer import RegexLexer, bygroups
from pygments.token import (
    Name,
    Comment,
    String,
    Operator,
    Text,
    Whitespace,
)

__all__ = ["BBCodeFormatter"]


class BBCodeFormatter(RegexLexer):
    name = "BBCode"
    aliases = ["bbcode", "bb"]

    STYLE_BRACKETS = Comment.Doc
    STYLE_TAG_TYPE = Name.Builtin.Function
    STYLE_EQUAL_SIGN = Operator
    STYLE_OPTION = String.StringName
    STYLE_VALUE = String

    tokens = {
        "root": [
            (r"(\[)(\w*\b)", bygroups(STYLE_BRACKETS, STYLE_TAG_TYPE), "tag"),
            (r"(\[)(\/)(\w*)(\])", bygroups(STYLE_BRACKETS, STYLE_BRACKETS, STYLE_TAG_TYPE, STYLE_BRACKETS)),
            (r"[^\[]+", Text),
        ],
        "tag": [
            (r"=", STYLE_EQUAL_SIGN, "tag_value"),
            (r"[\w\.{}]+", STYLE_OPTION), # The docs use curly brackets as placeholders in examples.
            (r"\s+", Whitespace),
            (r"\]", STYLE_BRACKETS, "#pop"),
        ],
        "tag_value": [
            (r"\"[^\r\n]*?\"", STYLE_VALUE, "#pop"), # Value surrounded by quotes.
            # Sometimes the docs like to concatenate placeholders in curly brackets {like},{this}, or similar.
            (r"\{[^\r\n]*?\}(?!,|x)", STYLE_VALUE, "#pop"), # Value surrounded by curly brackets.
            (r"[^\s\]]+", STYLE_VALUE, "#pop"),
        ],
    }


def setup(sphinx):
    from sphinx.highlighting import lexers

    sphinx.add_lexer("bbcode", BBCodeFormatter)
    lexers["bbcode"] = BBCodeFormatter()

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
