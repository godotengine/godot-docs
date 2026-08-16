
from pygments.lexer import bygroups, words, inherit
from pygments.token import (
    Keyword,
    Name,
    Comment,
    String,
    Operator,
    Whitespace,
)
from pygments.lexers.graphics import GLShaderLexer

__all__ = ["GDShaderLexer"]

KEYWORDS = (
    "shader_type",
    "render_mode",

    # Uniform hints.
    "source_color",
    "hint_enum",
    "hint_range",
    "hint_normal",
    "hint_default_white",
    "hint_default_black",
    "hint_default_transparent",
    "hint_anisotropy",
    "hint_roughness_r",
    "hint_roughness_g",
    "hint_roughness_b",
    "hint_roughness_a",
    "hint_roughness_normal",
    "hint_roughness_gray",
    "filter_nearest",
    "filter_nearest_mipmap",
    "filter_nearest_mipmap_anisotropic",
    "filter_linear",
    "filter_linear_mipmap",
    "filter_linear_mipmap_anisotropic",
    "repeat_enable",
    "repeat_disable",
    "hint_screen_texture",
    "hint_depth_texture",
    "hint_normal_roughness_texture",
    "no_editor",
    "no_storage",

    # Data types.
    "samplerExternalOES",

    # Other.
    "group_uniforms",
    "global",
    "instance",
)
KEYWORDS_CONTROL_FLOW = (
    "break",
    "case"
    "continue",
    "do",
    "elif",
    "else",
    "for",
    "if",
    "return",
    "switch",
    "while",
)

BUILT_IN_FUNCTIONS = (
    "radians",
    "degrees",
    "sin",
    "cos",
    "tan",
    "asin",
    "acos",
    "atan",
    "sinh",
    "cosh",
    "tanh",
    "asinh",
    "acosh",
    "atanh",

    "pow",
    "exp",
    "exp2",
    "log",
    "log2",
    "sqrt",
    "inversesqrt",
    "abs",
    "sign",
    "floor",
    "round",
    "roundEven",
    "trunc",
    "ceil",
    "fract",
    "mod",
    "modf",
    "min",
    "max",
    "clamp",
    "mix",
    "fma",
    "step",
    "smoothstep",
    "isnan",
    "isinf",
    "floatBitsToInt",
    "floatBitsToUint",
    "intBitsToFloat",
    "uintBitsToFloat",

    "length",
    "distance",
    "dot",
    "cross",
    "normalize",
    "reflect",
    "refract",
    "faceforward",
    "matrixCompMult",
    "outerProduct",
    "transpose",
    "determinant",
    "inverse",

    "lessThan",
    "greaterThan",
    "lessThanEqual",
    "greaterThanEqual",
    "equal",
    "notEqual",
    "any",
    "all",
    "not",

    "textureSize",
    "textureQueryLod",
    "textureQueryLevels",
    "texture",
    "textureProj",
    "textureLod",
    "textureProjLod",
    "textureProjGrad",
    "texelFetch",
    "dFdx",
    "dFdxCoarse",
    "dFdxFine",
    "dFdy",
    "dFdyCoarse",
    "dFdyFine",
    "fwidth",
    "fwidthCoarse",
    "fwidthFine",

    "packHalf2x16",
    "unpackHalf2x16",
    "packUnorm2x16",
    "unpackUnorm2x16",
    "packSnorm2x16",
    "unpackSnorm2x16",
    "packUnorm4x8",
    "unpackUnorm4x8",
    "packSnorm4x8",
    "unpackSnorm4x8",

    "bitfieldExtract",
    "bitfieldInsert",
    "bitfieldReverse",
    "bitCount",
    "findLSB",
    "findMSB",
    "imulExtended",
    "umulExtended",
    "uaddCarry",
    "usubBorrow",
    "idexp",
    "frexp",

    # Exclusive to canvas_item shaders.
    "texture_sdf",
    "texture_sdf_normal",
    "sdf_to_screen_uv",
    "screen_uv_to_sdf",

    # Exclusive to particle shaders.
    "emit_subparticle",
)

class GDShaderLexer(GLShaderLexer):
    name = "GDShader"
    aliases = ["gdshader"]
    filenames = ["*.gdshader"]

    tokens = {
        "root": [
            # We are not keeping track of a whole list. It would tend to be out-of-date.
            # The following is less reliable, but it's okay for the docs.
            # Assume that anything in uppercase is a built-in variable.
            (r"\b[A-Z][A-Z_0-9]+\b", Name.Variable),
            (r"render_mode\s+", Keyword, "mode_list"),
            (r"stencil_mode\s+", Keyword, "mode_list"),
            (words(KEYWORDS, prefix=r"\b", suffix=r"\b"), Keyword),
            (words(KEYWORDS_CONTROL_FLOW, prefix=r"\b", suffix=r"\b"), Keyword.ControlFlow),
            (words(BUILT_IN_FUNCTIONS, prefix=r"\b", suffix=r"\b"), Keyword),
            # Anything after a dot is a component.
            (r"(?<!\.)(\.)([a-zA-Z_]\w*)\b(?!\s*\()", bygroups(Operator, Name.Variable.Instance)),
            (r"/(\\\n)?\*\*(.|\n)*?\*(\\\n)?/", Comment.Doc),
            # Function declaration.
            (r"\w+(?=\([\w\s,]*\)\s*{)", Name.Function),
            (r"\"", String, "string"),
            # Preprocessor directive.
            (r"(#)(\w+)", bygroups(Operator, Keyword.ControlFlow)),
            inherit
        ],
        "mode_list": [
             # We are not keeping track of a whole list, as it's prone to be out-of-date.
            (r"\w+", Name.Class),
            (r"\s+", Whitespace),
            (r",", Operator),
            (r";", Operator, "#pop"),
        ],
        "string": [
            (r"\"", String.Double, "#pop"),
            (r"\\\\|\\\"|\\\n", String.Escape),
            (r"[^\\\'\"%\n]+", String),
            (r"[\'\"\\]", String),
        ]
    }

def setup(sphinx):
    from sphinx.highlighting import lexers

    sphinx.add_lexer("gdshader", GDShaderLexer)
    lexers["gdshader"] = GDShaderLexer()

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
