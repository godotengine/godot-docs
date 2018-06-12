.. _doc_c_sharp_differences:

API differences to GDScript
===========================

This is a (incomplete) list of API differences between C# and GDScript.

General Differences
-------------------

As explained in the :ref:`doc_c_sharp`, C# generally uses ``PascalCase`` instead
of the ``snake_case`` in GDScript and C++.

Global Scope
------------

Available under ``Godot.GD``.
Some things were moved to their own classes, like Math and Random. See below.

Global functions like ``print``, ``var2str`` and ``weakref`` are located under
``GD`` in C#.

``ERR_*`` constants were moved to ``Godot.Error``.

Math
----

Math functions like ``abs``, ``acos``, ``asin``, ``atan`` and ``atan2`` are
located under ``Mathf`` instead of in global scope.
``PI`` is ``Mathf.PI``

Random
------

Random functions like ``rand_range`` and ``rand_seed`` are located under ``Random``,
so use ``Random.RandRange`` instead of ``rand_range``.

Export keyword
--------------

Use the ``[Export]`` attribute instead of the GDScript ``export`` keyword.

Signal keyword
--------------

Use the ``[Signal]`` attribute instead of the GDScript ``signal`` keyword.
This attribute should be used on a `delegate`, whose name signature will be used to define the signal.

.. code-block:: csharp

    [Signal]
    delegate void MySignal(string willSendsAString);

See also: :ref:`c_sharp_signals`

Singletons
----------

Singletons provide static methods rather than using the singleton pattern in C#.
This is to make code less verbose and similar to GDScript. Example:

.. code-block:: csharp

    Input.IsActionPressed("ui_down")

String
------

Use ``System.String`` (``string``). All the Godot String methods are provided
by the ``StringExtensions`` class as extension methods. Example:

.. code-block:: csharp

    string upper = "I LIKE SALAD FORKS";
    string lower = upper.ToLower();

There are a few differences though:

* ``erase``: Strings are immutable in C#, so we cannot modify the string
  passed to the extension method. For this reason ``Erase`` was added as an
  extension method of ``StringBuilder`` instead of string.
  Alternatively you can use ``string.Remove``.
* ``IsSubsequenceOf``/``IsSubsequenceOfi``: An additional method is provided
  which is an overload of ``IsSubsequenceOf`` allowing to explicitly specify
  case sensitivity:

.. code-block:: csharp

  str.IsSubsequenceOf("ok"); // Case sensitive
  str.IsSubsequenceOf("ok", true); // Case sensitive
  str.IsSubsequenceOfi("ok"); // Case insensitive
  str.IsSubsequenceOf("ok", false); // Case insensitive

* ``Match``/``Matchn``/``ExprMatch``: An additional method is provided besides
  ``Match`` and ``Matchn``, which allows to explicitly specify case sensitivity:

.. code-block:: csharp

  str.Match("*.txt"); // Case sensitive
  str.ExprMatch("*.txt", true); // Case sensitive
  str.Matchn("*.txt"); // Case insensitive
  str.ExprMatch("*.txt", false); // Case insensitive

Basis
-----

Structs cannot have parameterless constructors in C#, therefore ``new Basis()``
initializes all primitive members to their default value. Use ``Basis.Identity``
for the equivalent to ``Basis()`` in GDScript and C++.

The following methods were converted to properties with their respective names changed:

================  ==================================================================
GDScript          C#
================  ==================================================================
get_scale()       Scale
================  ==================================================================

Transform2D
-----------

Structs cannot have parameterless constructors in C#, therefore ``new Transform2D()``
initializes all primitive members to their default value.
Please use ``Transform2D.Identity`` for the equivalent to ``Transform2D()`` in GDScript and C++.

The following methods were converted to properties with their respective names changed:

================  ==================================================================
GDScript          C#
================  ==================================================================
get_origin()      Origin
get_rotation()    Rotation
get_scale()       Scale
================  ==================================================================

Plane
-----

The following methods were converted to properties with their respective names changed:

================  ==================================================================
GDScript          C#
================  ==================================================================
center()          Center
================  ==================================================================

Rect2
-----

The following fields were converted to properties with their respective names changed:

================  ==================================================================
GDScript          C#
================  ==================================================================
end               End
================  ==================================================================

The following methods were converted to properties with their respective names changed:

================  ==================================================================
GDScript          C#
================  ==================================================================
get_area()        Area
================  ==================================================================

Quat
----

Structs cannot have parameterless constructors in C#, therefore ``new Quat()``
initializes all primitive members to their default value.
Please use ``Quat.Identity`` for the equivalent to ``Quat()`` in GDScript and C++.

Array
-----

*This is temporary. Array is ref-counted, so it will need its own type that wraps the native side.
PoolArrays will also need their own type to be used the way they are meant to.*

================  ==================================================================
GDScript          C#
================  ==================================================================
Array             object[]
PoolIntArray      int[]
PoolByteArray     byte[]
PoolFloatArray    float[]
PoolStringArray   String[]
PoolColorArray    Color[]
PoolVector2Array  Vector2[]
PoolVector3Array  Vector3[]
================  ==================================================================

In some exceptional cases a raw array (``type[]``) may be required instead of a ``List``.

Dictionary
----------

*This is temporary. Array is ref-counted, so it will need its own type that wraps the native side.*

Use ``Dictionary<object, object>``.

Variant
-------

``System.Object`` (``object``) is used in place of ``Variant``.

Communicating with other scripting languages
--------------------------------------------

The methods ``object Object.call(string method, params object[] args)``,
``object Object.get(string field)`` and ``object Object.set(string field, object value)``
are provided to communicate with instances of other
scripting languages via the Variant API.

Other differences
-----------------

``preload``, ``assert`` and ``yield`` as they work in GDScript are currently
not available in C#.

Other differences:

================  ==================================================================
GDScript          C#
================  ==================================================================
Color8            Color.Color8
is_inf            float.IsInfinity
is_nan            float.IsNaN
dict2inst         ? TODO
inst2dict         ? TODO
load              GD.load which is the same as ResourceLoader.load
================  ==================================================================


