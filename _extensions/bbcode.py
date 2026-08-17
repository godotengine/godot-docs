
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

    STYLE_BRACKETS = Comment.Doc #Comment.Region
    STYLE_TAG_TYPE = Name.Builtin.Function #Comment.Region
    STYLE_EQUAL_SIGN = Operator
    STYLE_OPTION = String.StringName#Comment.Doc
    STYLE_VALUE = String #Comment.Single

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
        # Known tags. Isn't working as intended.
        # (
        #     r"(\[\/?)(?:(b|i|u|s|code|char|p|br|hr|center|left|right|fill|indent|url|hint|img|font|font_size|dropcap|opentype_features|lang|color|bgcolor|fgcolor|outline_size|outline_color|table|cell|ul|ol|lb|rb)*\b)",
        #     bygroups(Comment.Region, Name.Builtin.Function),
        #     "tag"
        # ),
    }


def setup(sphinx):
    from sphinx.highlighting import lexers

    sphinx.add_lexer("bbcode", BBCodeFormatter)
    lexers["bbcode"] = BBCodeFormatter()

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
