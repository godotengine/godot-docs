.. _doc_c_sharp_differences:

C# API differences to GDScript
==============================

This is a (incomplete) list of API differences between C# and GDScript.

General differences
-------------------

As explained in the :ref:`doc_c_sharp`, C# generally uses ``PascalCase`` instead
of the ``snake_case`` used in GDScript and C++.

Global scope
------------

Global functions and some constants had to be moved to classes, since C#
does not allow declaring them in namespaces.
Most global constants were moved to their own enums.

Constants
^^^^^^^^^

In C#, only primitive types can be constant. For example, the ``TAU`` constant
is replaced by the ``Mathf.Tau`` constant, but the ``Vector2.RIGHT`` constant
is replaced by the ``Vector2.Right`` read-only property. This behaves similarly
to a constant, but can't be used in some contexts like ``switch`` statements.

Global enum constants were moved to their own enums.
For example, ``ERR_*`` constants were moved to the ``Error`` enum.

Special cases:

=======================  ===========================================================
GDScript                 C#
=======================  ===========================================================
``SPKEY``                ``GD.SpKey``
``TYPE_*``               ``Variant.Type`` enum
``OP_*``                 ``Variant.Operator`` enum
=======================  ===========================================================

Math functions
^^^^^^^^^^^^^^

Math global functions, like ``abs``, ``acos``, ``asin``, ``atan`` and ``atan2``, are
located under ``Mathf`` as ``Abs``, ``Acos``, ``Asin``, ``Atan`` and ``Atan2``.
The ``PI`` constant can be found as ``Mathf.Pi``.

Random functions
^^^^^^^^^^^^^^^^

Random global functions, like ``rand_range`` and ``rand_seed``, are located under ``GD``.
Example: ``GD.RandRange`` and ``GD.RandSeed``.

Other functions
^^^^^^^^^^^^^^^

Many other global functions like ``print`` and ``var2str`` are located under ``GD``.
Example: ``GD.Print`` and ``GD.Var2Str``.

Exceptions:

===========================  =======================================================
GDScript                     C#
===========================  =======================================================
``weakref(obj)``             ``Object.WeakRef(obj)``
``is_instance_valid(obj)``   ``Object.IsInstanceValid(obj)``
===========================  =======================================================

Tips
^^^^

Sometimes it can be useful to use the ``using static`` directive. This directive allows
to access the members and nested types of a class without specifying the class name.

Example:

.. code-block:: csharp

    using static Godot.GD;

    public class Test
    {
        static Test()
        {
            Print("Hello"); // Instead of GD.Print("Hello");
        }
    }

Export keyword
--------------

Use the ``[Export]`` attribute instead of the GDScript ``export`` keyword.
This attribute can also be provided with optional :ref:`PropertyHint<enum_@GlobalScope_PropertyHint>` and ``hintString`` parameters.
Default values can be set by assigning a value.

Example:

.. code-block:: csharp

    using Godot;

    public class MyNode : Node
    {
        [Export]
        private NodePath _nodePath;

        [Export]
        private string _name = "default";

        [Export(PropertyHint.Range, "0,100000,1000,or_greater")]
        private int _income;

        [Export(PropertyHint.File, "*.png,*.jpg")]
        private string _icon;
    }

Signal keyword
--------------

Use the ``[Signal]`` attribute to declare a signal instead of the GDScript ``signal`` keyword.
This attribute should be used on a `delegate`, whose name signature will be used to define the signal.
The `delegate` must have the ``EventHandler`` suffix, an `event` will be generated in the class with the same name but without the suffix, use that event's name with ``EmitSignal``.

.. code-block:: csharp

    [Signal]
    delegate void MySignalEventHandler(string willSendAString);

See also: :ref:`doc_c_sharp_signals`.

`@onready` annotation
---------------------

GDScript has the ability to defer the initialization of a member variable until the ready function
is called with `@onready` (cf. :ref:`doc_gdscript_onready_annotation`).
For example:

.. code-block:: gdscript

    @onready var my_label = get_node("MyLabel")

However C# does not have this ability. To achieve the same effect you need to do this.

.. code-block:: csharp

    private Label _myLabel;

    public override void _Ready()
    {
        _myLabel = GetNode<Label>("MyLabel");
    }

Singletons
----------

Singletons are available as static classes rather than using the singleton pattern.
This is to make code less verbose than it would be with an ``Instance`` property.

Example:

.. code-block:: csharp

    Input.IsActionPressed("ui_down")

However, in some very rare cases this is not enough. For example, you may want
to access a member from the base class ``Godot.Object``, like ``Connect``.
For such use cases we provide a static property named ``Singleton`` that returns
the singleton instance. The type of this instance is ``Godot.Object``.

Example:

.. code-block:: csharp

    Input.Singleton.JoyConnectionChanged += Input_JoyConnectionChanged;

String
------

Use ``System.String`` (``string``). Most of Godot's String methods have an
equivalent in ``System.String`` or are provided by the ``StringExtensions``
class as extension methods.

Example:

.. code-block:: csharp

    string text = "Bigrams";
    string[] bigrams = text.Bigrams(); // ["Bi", "ig", "gr", "ra", "am", "ms"]

Strings are immutable in .NET, so all methods that manipulate a string don't
modify the original string and return a newly created string with the
modifications applied. To avoid creating multiple string allocations consider
using a `StringBuilder`_.

List of Godot's String methods and their equivalent in C#:

=======================  ==============================================================
GDScript                 C#
=======================  ==============================================================
begins_with              `string.StartsWith`_
bigrams                  StringExtensions.Bigrams
bin_to_int               StringExtensions.BinToInt
c_escape                 StringExtensions.CEscape
c_unescape               StringExtensions.CUnescape
capitalize               StringExtensions.Capitalize
casecmp_to               StringExtensions.CasecmpTo or StringExtensions.CompareTo (Consider using `string.Equals`_ or `string.Compare`_)
chr                      N/A
contains                 `string.Contains`_
count                    StringExtensions.Count (Consider using `RegEx`_)
countn                   StringExtensions.CountN (Consider using `RegEx`_)
dedent                   StringExtensions.Dedent
ends_with                `string.EndsWith`_
find                     StringExtensions.Find (Consider using `string.IndexOf`_ or `string.IndexOfAny`_)
findn                    StringExtensions.FindN (Consider using `string.IndexOf`_ or `string.IndexOfAny`_)
format                   Use `$ string interpolation`_
get_base_dir             StringExtensions.GetBaseDir
get_basename             StringExtensions.GetBaseName
get_extension            StringExtensions.GetExtension
get_file                 StringExtensions.GetFile
get_slice                N/A
get_slice_count          N/A
get_slicec               N/A
hash                     StringExtensions.Hash (Consider using `object.GetHashCode`_ unless you need to guarantee the same behavior as in GDScript)
hex_to_int               StringExtensions.HexToInt (Consider using `int.Parse`_ or `long.Parse`_ with `System.Globalization.NumberStyles.HexNumber`_)
humanize_size            N/A
indent                   StringExtensions.Indent
insert                   `string.Insert`_ (Consider using `StringBuilder`_ to manipulate strings)
is_absolute_path         StringExtensions.IsAbsolutePath
is_empty                 `string.IsNullOrEmpty`_ or `string.IsNullOrWhiteSpace`_
is_relative_path         StringExtensions.IsRelativePath
is_subsequence_of        StringExtensions.IsSubsequenceOf
is_subsequence_ofn       StringExtensions.IsSubsequenceOfN
is_valid_filename        StringExtensions.IsValidFileName
is_valid_float           StringExtensions.IsValidFloat (Consider using `float.TryParse`_ or `double.TryParse`_)
is_valid_hex_number      StringExtensions.IsValidHexNumber
is_valid_html_color      StringExtensions.IsValidHtmlColor
is_valid_identifier      StringExtensions.IsValidIdentifier
is_valid_int             StringExtensions.IsValidInt (Consider using `int.TryParse`_ or `long.TryParse`_)
is_valid_ip_address      StringExtensions.IsValidIPAddress
join                     `string.Join`_
json_escape              StringExtensions.JSONEscape
left                     StringExtensions.Left (Consider using `string.Substring`_ or `string.AsSpan`_)
length                   `string.Length`_
lpad                     `string.PadLeft`_
lstrip                   `string.TrimStart`_
match                    StringExtensions.Match (Consider using `RegEx`_)
matchn                   StringExtensions.MatchN (Consider using `RegEx`_)
md5_buffer               StringExtensions.MD5Buffer (Consider using `System.Security.Cryptography.MD5.HashData`_)
md5_text                 StringExtensions.MD5Text (Consider using `System.Security.Cryptography.MD5.HashData`_ with StringExtensions.HexEncode)
naturalnocasecmp_to      N/A (Consider using `string.Equals`_ or `string.Compare`_)
nocasecmp_to             StringExtensions.NocasecmpTo or StringExtensions.CompareTo (Consider using `string.Equals`_ or `string.Compare`_)
num                      `float.ToString`_ or `double.ToString`_
num_int64                `int.ToString`_ or `long.ToString`_
num_scientific           `float.ToString`_ or `double.ToString`_
num_uint64               `uint.ToString`_ or `ulong.ToString`_
pad_decimals             StringExtensions.PadDecimals
pad_zeros                StringExtensions.PadZeros
path_join                StringExtensions.PathJoin
repeat                   Use `string constructor`_ or a `StringBuilder`_
replace                  `string.Replace`_ or `RegEx`_
replacen                 StringExtensions.ReplaceN (Consider using `string.Replace`_ or `RegEx`_)
rfind                    StringExtensions.RFind (Consider using `string.LastIndexOf`_ or `string.LastIndexOfAny`_)
rfindn                   StringExtensions.RFindN (Consider using `string.LastIndexOf`_ or `string.LastIndexOfAny`_)
right                    StringExtensions.Right (Consider using `string.Substring`_ or `string.AsSpan`_)
rpad                     `string.PadRight`_
rsplit                   N/A
rstrip                   `string.TrimEnd`_
sha1_buffer              StringExtensions.SHA1Buffer (Consider using `System.Security.Cryptography.SHA1.HashData`_)
sha1_text                StringExtensions.SHA1Text (Consider using `System.Security.Cryptography.SHA1.HashData`_ with StringExtensions.HexEncode)
sha256_buffer            StringExtensions.SHA256Buffer (Consider using `System.Security.Cryptography.SHA256.HashData`_)
sha256_text              StringExtensions.SHA256Text (Consider using `System.Security.Cryptography.SHA256.HashData`_ with StringExtensions.HexEncode)
similarity               StringExtensions.Similarity
simplify_path            StringExtensions.SimplifyPath
split                    StringExtensions.Split (Consider using `string.Split`_)
split_floats             StringExtensions.SplitFloat
strip_edges              StringExtensions.StripEdges (Consider using `string.Trim`_, `string.TrimStart`_ or `string.TrimEnd`_)
strip_escapes            StringExtensions.StripEscapes
substr                   StringExtensions.Substr (Consider using `string.Substring`_ or `string.AsSpan`_)
to_ascii_buffer          StringExtensions.ToASCIIBuffer (Consider using `System.Text.Encoding.ASCII.GetBytes`_)
to_camel_case            StringExtensions.ToCamelCase
to_float                 StringExtensions.ToFloat (Consider using `float.TryParse`_ or `double.TryParse`_)
to_int                   StringExtensions.ToInt (Consider using `int.TryParse`_ or `long.TryParse`_)
to_lower                 `string.ToLower`_
to_pascal_case           StringExtensions.ToPascalCase
to_snake_case            StringExtensions.ToSnakeCase
to_upper                 `string.ToUpper`_
to_utf16_buffer          StringExtensions.ToUTF16Buffer (Consider using `System.Text.Encoding.UTF16.GetBytes`_)
to_utf32_buffer          StringExtensions.ToUTF32Buffer (Consider using `System.Text.Encoding.UTF32.GetBytes`_)
to_utf8_buffer           StringExtensions.ToUTF8Buffer (Consider using `System.Text.Encoding.UTF8.GetBytes`_)
trim_prefix              StringExtensions.TrimPrefix
trim_suffix              StringExtensions.TrimSuffix
unicode_at               `string[int]`_ indexer
uri_decode               StringExtensions.URIDecode (Consider using `System.Uri.UnescapeDataString`_)
uri_encode               StringExtensions.URIEncode (Consider using `System.Uri.EscapeDataString`_)
validate_node_name       StringExtensions.ValidateNodeName
xml_escape               StringExtensions.XMLEscape
xml_unescape             StringExtensions.XMLUnescape
=======================  ==============================================================

List of Godot's PackedByteArray methods that create a String and their C# equivalent:

=========================  ==============================================================
GDScript                   C#
=========================  ==============================================================
get_string_from_ascii      StringExtensions.GetStringFromASCII (Consider using `System.Text.Encoding.ASCII.GetString`_)
get_string_from_utf16      StringExtensions.GetStringFromUTF16 (Consider using `System.Text.Encoding.UTF16.GetString`_)
get_string_from_utf32      StringExtensions.GetStringFromUTF32 (Consider using `System.Text.Encoding.UTF32.GetString`_)
get_string_from_utf8       StringExtensions.GetStringFromUTF8 (Consider using `System.Text.Encoding.UTF8.GetString`_)
hex_encode                 StringExtensions.HexEncode (Consider using `System.Convert.ToHexString`_)
=========================  ==============================================================

* .NET contains many path utility methods available under the
  `System.IO.Path`_
  class that can be used when not dealing with Godot paths (paths that start
  with ``res://`` or ``user://``)

.. _$ string interpolation: https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/tokens/interpolated
.. _double.ToString: https://learn.microsoft.com/en-us/dotnet/api/system.double.tostring
.. _double.TryParse: https://learn.microsoft.com/en-us/dotnet/api/system.double.tryparse
.. _float.ToString: https://learn.microsoft.com/en-us/dotnet/api/system.single.tostring
.. _float.TryParse: https://learn.microsoft.com/en-us/dotnet/api/system.single.tryparse
.. _int.Parse: https://learn.microsoft.com/en-us/dotnet/api/system.int32.parse
.. _int.ToString: https://learn.microsoft.com/en-us/dotnet/api/system.int32.tostring
.. _int.TryParse: https://learn.microsoft.com/en-us/dotnet/api/system.int32.tryparse
.. _long.Parse: https://learn.microsoft.com/en-us/dotnet/api/system.int64.parse
.. _long.ToString: https://learn.microsoft.com/en-us/dotnet/api/system.int64.tostring
.. _long.TryParse: https://learn.microsoft.com/en-us/dotnet/api/system.int64.tryparse
.. _uint.ToString: https://learn.microsoft.com/en-us/dotnet/api/system.uint32.tostring
.. _ulong.ToString: https://learn.microsoft.com/en-us/dotnet/api/system.uint64.tostring
.. _object.GetHashCode: https://learn.microsoft.com/en-us/dotnet/api/system.object.gethashcode
.. _RegEx: https://learn.microsoft.com/en-us/dotnet/standard/base-types/regular-expressions
.. _string constructor: https://learn.microsoft.com/en-us/dotnet/api/system.string.-ctor
.. _string[int]: https://learn.microsoft.com/en-us/dotnet/api/system.string.chars
.. _string.AsSpan: https://learn.microsoft.com/en-us/dotnet/api/system.memoryextensions.asspan
.. _string.Compare: https://learn.microsoft.com/en-us/dotnet/api/system.string.compare
.. _string.Contains: https://learn.microsoft.com/en-us/dotnet/api/system.string.contains
.. _string.EndsWith: https://learn.microsoft.com/en-us/dotnet/api/system.string.endswith
.. _string.Equals: https://learn.microsoft.com/en-us/dotnet/api/system.string.equals
.. _string.IndexOf: https://learn.microsoft.com/en-us/dotnet/api/system.string.indexof
.. _string.IndexOfAny: https://learn.microsoft.com/en-us/dotnet/api/system.string.indexofany
.. _string.Insert: https://learn.microsoft.com/en-us/dotnet/api/system.string.insert
.. _string.IsNullOrEmpty: https://learn.microsoft.com/en-us/dotnet/api/system.string.isnullorempty
.. _string.IsNullOrWhiteSpace: https://learn.microsoft.com/en-us/dotnet/api/system.string.isnullorwhitespace
.. _string.Join: https://learn.microsoft.com/en-us/dotnet/api/system.string.join
.. _string.LastIndexOf: https://learn.microsoft.com/en-us/dotnet/api/system.string.lastindexof
.. _string.LastIndexOfAny: https://learn.microsoft.com/en-us/dotnet/api/system.string.lastindexofany
.. _string.Length: https://learn.microsoft.com/en-us/dotnet/api/system.string.length
.. _string.PadLeft: https://learn.microsoft.com/en-us/dotnet/api/system.string.padleft
.. _string.PadRight: https://learn.microsoft.com/en-us/dotnet/api/system.string.padright
.. _string.Replace: https://learn.microsoft.com/en-us/dotnet/api/system.string.replace
.. _string.Split: https://learn.microsoft.com/en-us/dotnet/api/system.string.split
.. _string.StartsWith: https://learn.microsoft.com/en-us/dotnet/api/system.string.startswith
.. _string.Substring: https://learn.microsoft.com/en-us/dotnet/api/system.string.substring
.. _string.Trim: https://learn.microsoft.com/en-us/dotnet/api/system.string.trim
.. _string.TrimEnd: https://learn.microsoft.com/en-us/dotnet/api/system.string.trimend
.. _string.TrimStart: https://learn.microsoft.com/en-us/dotnet/api/system.string.trimstart
.. _string.ToLower: https://learn.microsoft.com/en-us/dotnet/api/system.string.tolower
.. _string.ToUpper: https://learn.microsoft.com/en-us/dotnet/api/system.string.toupper
.. _StringBuilder: https://learn.microsoft.com/en-us/dotnet/api/system.text.stringbuilder
.. _System.Convert.ToHexString: https://learn.microsoft.com/en-us/dotnet/api/system.convert.tohexstring
.. _System.Globalization.NumberStyles.HexNumber: https://learn.microsoft.com/en-us/dotnet/api/system.globalization.numberstyles#system-globalization-numberstyles-hexnumber
.. _System.IO.Path: https://learn.microsoft.com/en-us/dotnet/api/system.io.path
.. _System.Security.Cryptography.MD5.HashData: https://learn.microsoft.com/en-us/dotnet/api/system.security.cryptography.md5.hashdata
.. _System.Security.Cryptography.SHA1.HashData: https://learn.microsoft.com/en-us/dotnet/api/system.security.cryptography.sha1.hashdata
.. _System.Security.Cryptography.SHA256.HashData: https://learn.microsoft.com/en-us/dotnet/api/system.security.cryptography.sha256.hashdata
.. _System.Text.Encoding.ASCII.GetBytes: https://learn.microsoft.com/en-us/dotnet/api/system.text.asciiencoding.getbytes
.. _System.Text.Encoding.ASCII.GetString: https://learn.microsoft.com/en-us/dotnet/api/system.text.asciiencoding.getstring
.. _System.Text.Encoding.UTF16.GetBytes: https://learn.microsoft.com/en-us/dotnet/api/system.text.unicodeencoding.getbytes
.. _System.Text.Encoding.UTF16.GetString: https://learn.microsoft.com/en-us/dotnet/api/system.text.unicodeencoding.getstring
.. _System.Text.Encoding.UTF32.GetBytes: https://learn.microsoft.com/en-us/dotnet/api/system.text.utf32encoding.getbytes
.. _System.Text.Encoding.UTF32.GetString: https://learn.microsoft.com/en-us/dotnet/api/system.text.utf32encoding.getstring
.. _System.Text.Encoding.UTF8.GetBytes: https://learn.microsoft.com/en-us/dotnet/api/system.text.utf8encoding.getbytes
.. _System.Text.Encoding.UTF8.GetString: https://learn.microsoft.com/en-us/dotnet/api/system.text.utf8encoding.getstring
.. _System.Uri.EscapeDataString: https://learn.microsoft.com/en-us/dotnet/api/system.uri.escapedatastring
.. _System.Uri.UnescapeDataString: https://learn.microsoft.com/en-us/dotnet/api/system.uri.unescapedatastring

Basis
-----

Structs cannot have parameterless constructors in C#. Therefore, ``new Basis()``
initializes all primitive members to their default value. Use ``Basis.Identity``
for the equivalent of ``Basis()`` in GDScript and C++.

The following method was converted to a property with a different name:

====================  ==============================================================
GDScript              C#
====================  ==============================================================
``get_scale()``       ``Scale``
====================  ==============================================================

Transform2D
-----------

Structs cannot have parameterless constructors in C#. Therefore, ``new Transform2D()``
initializes all primitive members to their default value.
Please use ``Transform2D.Identity`` for the equivalent of ``Transform2D()`` in GDScript and C++.

The following methods were converted to properties with their respective names changed:

====================  ==============================================================
GDScript              C#
====================  ==============================================================
``get_rotation()``    ``Rotation``
``get_scale()``       ``Scale``
====================  ==============================================================

Plane
-----

The following method was converted to a property with a *slightly* different name:

================  ==================================================================
GDScript          C#
================  ==================================================================
``center()``      ``Center``
================  ==================================================================

Rect2
-----

The following field was converted to a property with a *slightly* different name:

================  ==================================================================
GDScript          C#
================  ==================================================================
``end``           ``End``
================  ==================================================================

The following method was converted to a property with a different name:

================  ==================================================================
GDScript          C#
================  ==================================================================
``get_area()``    ``Area``
================  ==================================================================

Quaternion
----------

Structs cannot have parameterless constructors in C#. Therefore, ``new Quaternion()``
initializes all primitive members to their default value.
Please use ``Quaternion.Identity`` for the equivalent of ``Quaternion()`` in GDScript and C++.

The following methods were converted to a property with a different name:

=====================  =============================================================
GDScript               C#
=====================  =============================================================
``length()``           ``Length``
``length_squared()``   ``LengthSquared``
=====================  =============================================================

Array
-----

*This is temporary. PackedArrays will need their own types to be used the way they are meant to.*

======================  ==============================================================
GDScript                C#
======================  ==============================================================
``Array``                ``Godot.Collections.Array``
``PackedInt32Array``     ``int[]``
``PackedInt64Array``     ``long[]``
``PackedByteArray``      ``byte[]``
``PackedFloat32Array``   ``float[]``
``PackedFloat64Array``   ``double[]``
``PackedStringArray``    ``String[]``
``PackedColorArray``     ``Color[]``
``PackedVector2Array``   ``Vector2[]``
``PackedVector3Array``   ``Vector3[]``
======================  ==============================================================

``Godot.Collections.Array<T>`` is a type-safe wrapper around ``Godot.Collections.Array``.
Use the ``Godot.Collections.Array<T>(Godot.Collections.Array)`` constructor to create one.

Dictionary
----------

Use ``Godot.Collections.Dictionary``.

``Godot.Collections.Dictionary<T>`` is a type-safe wrapper around ``Godot.Collections.Dictionary``.
Use the ``Godot.Collections.Dictionary<T>(Godot.Collections.Dictionary)`` constructor to create one.

Variant
-------

``System.Object`` (``object``) is used instead of ``Variant``.

Communicating with other scripting languages
--------------------------------------------

This is explained extensively in :ref:`doc_cross_language_scripting`.

Yield
-----

Something similar to GDScript's ``yield`` with a single parameter can be achieved with
C#'s `yield keyword <https://docs.microsoft.com/en-US/dotnet/csharp/language-reference/keywords/yield>`_.

The equivalent of yield on signal can be achieved with async/await and ``Godot.Object.ToSignal``.

Example:

.. code-block:: csharp

  await ToSignal(timer, "timeout");
  GD.Print("After timeout");

Other differences
-----------------

``preload``, as it works in GDScript, is not available in C#.
Use ``GD.Load`` or ``ResourceLoader.Load`` instead.

Other differences:

================  ==================================================================
GDScript          C#
================  ==================================================================
``Color8``        ``Color.Color8``
``is_inf``        ``float.IsInfinity``
``is_nan``        ``float.IsNaN``
``dict2inst``     TODO
``inst2dict``     TODO
================  ==================================================================
