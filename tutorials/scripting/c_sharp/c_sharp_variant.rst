.. _doc_c_sharp_variant:

C# Variant
==========

For a detailed explanation of Variant in general, see the :ref:`Variant <class_Variant>` documentation page.

``Godot.Variant`` is used to represent Godot's native :ref:`Variant <class_Variant>` type. Any Variant-compatible type can be converted from/to it.
We recommend avoiding ``Godot.Variant`` unless it is necessary to interact with untyped engine APIs.
Take advantage of C#'s type safety when possible.

Any of ``Variant.As{TYPE}`` methods or the generic ``Variant.As<T>`` method can be used to convert
a ``Godot.Variant`` to a C# type. Since the ``Godot.Variant`` type contains implicit conversions
defined for all the supported types, calling these methods directly is usually not necessary.

Use ``CreateFrom`` method overloads or the generic ``Variant.From<T>`` method to convert a C# type
to a ``Godot.Variant``.

.. note::

    Since the Variant type in C# is a struct, it can't be null. To create a "null"
    Variant use the ``default`` keyword or the parameterless constructor.

Variant-compatible types
------------------------

* All the `built-in value types <https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/built-in-types-table>`_,
  except ``decimal``, ``nint`` and ``nuint``.
* ``string``.
* Classes derived from :ref:`GodotObject <class_Object>`.
* Collections types defined in the ``Godot.Collections`` namespace.

Full list of Variant types and their equivalent C# type:

=======================  ===========================================================
Variant.Type             C# Type
=======================  ===========================================================
``Nil``                  ``null`` (Not a type)
``Bool``                 ``bool``
``Int``                  ``long`` (Godot stores 64-bit integers in Variant)
``Float``                ``double`` (Godot stores 64-bit floats in Variant)
``String``               ``string``
``Vector2``              ``Godot.Vector2``
``Vector2I``             ``Godot.Vector2I``
``Rect2``                ``Godot.Rect2``
``Rect2I``               ``Godot.Rect2I``
``Vector3``              ``Godot.Vector3``
``Vector3I``             ``Godot.Vector3I``
``Transform2D``          ``Godot.Transform2D``
``Vector4``              ``Godot.Vector4``
``Vector4I``             ``Godot.Vector4I``
``Plane``                ``Godot.Plane``
``Quaternion``           ``Godot.Quaternion``
``Aabb``                 ``Godot.Aabb``
``Basis``                ``Godot.Basis``
``Transform3D``          ``Godot.Transform3D``
``Projection``           ``Godot.Projection``
``Color``                ``Godot.Color``
``StringName``           ``Godot.StringName``
``NodePath``             ``Godot.NodePath``
``Rid``                  ``Godot.Rid``
``Object``               ``Godot.GodotObject`` or any derived type.
``Callable``             ``Godot.Callable``
``Signal``               ``Godot.Signal``
``Dictionary``           ``Godot.Collections.Dictionary``
``Array``                ``Godot.Collections.Array``
``PackedByteArray``      ``byte[]``
``PackedInt32Array``     ``int[]``
``PackedInt64Array``     ``long[]``
``PackedFloat32Array``   ``float[]``
``PackedFloat64Array``   ``double[]``
``PackedStringArray``    ``string[]``
``PackedVector2Array``   ``Godot.Vector2[]``
``PackedVector3Array``   ``Godot.Vector3[]``
``PackedColorArray``     ``Godot.Color[]``
=======================  ===========================================================

.. warning::

    Godot uses 64-bit integers and floats in Variant. Smaller integer and float types
    such as ``int``, ``short`` and ``float`` are supported since they can fit in the
    bigger type. Be aware that an implicit conversion is performed so using the wrong
    type will result in potential precision loss.

.. warning::

    Enums are supported by ``Godot.Variant`` since their underlying type is an integer
    type which are all compatible. However, implicit conversions don't exist, enums must
    be manually converted to their underlying integer type before they can converted to/from
    ``Godot.Variant`` or use the generic ``Variant.As<T>`` and ``Variant.From<T>`` methods
    to convert them.

    .. code-block:: csharp

        enum MyEnum { A, B, C }

        Variant variant1 = (int)MyEnum.A;
        MyEnum enum1 = (MyEnum)(int)variant1;

        Variant variant2 = Variant.From(MyEnum.A);
        MyEnum enum2 = variant2.As<MyEnum>();

Using Variant in a generic context
----------------------------------

When using generics, you may be interested in restricting the generic ``T`` type to be
only one of the Variant-compatible types. This can be achieved using the ``[MustBeVariant]``
attribute.

.. code-block:: csharp

    public void MethodThatOnlySupportsVariants<[MustBeVariant] T>(T onlyVariant)
    {
        // Do something with the Variant-compatible value.
    }

Combined with the generic ``Variant.From<T>`` allows you to obtain an instance of ``Godot.Variant``
from an instance of a generic ``T`` type. Then it can be used in any API that only supports the
``Godot.Variant`` struct.

.. code-block:: csharp

    public void Method1<[MustBeVariant] T>(T variantCompatible)
    {
        Variant variant = Variant.From(variantCompatible);
        Method2(variant);
    }

    public void Method2(Variant variant)
    {
        // Do something with variant.
    }

In order to invoke a method with a generic parameter annotated with the ``[MustBeVariant]``
attribute, the value must be a Variant-compatible type or a generic ``T`` type annotated
with the ``[MustBeVariant]`` attribute as well.

.. code-block:: csharp

    public class ObjectDerivedClass : GodotObject { }

    public class NonObjectDerivedClass { }

    public void Main<[MustBeVariant] T1, T2>(T1 someGeneric1, T2 someGeneric2)
    {
        MyMethod(42); // Works because `int` is a Variant-compatible type.
        MyMethod(new ObjectDerivedClass()); // Works because any type that derives from `GodotObject` is a Variant-compatible type.
        MyMethod(new NonObjectDerivedClass()); // Does NOT work because the type is not Variant-compatible.
        MyMethod(someGeneric1); // Works because `T1` is annotated with the `[MustBeVariant]` attribute.
        MyMethod(someGeneric2); // Does NOT work because `T2` is NOT annotated with the `[MustBeVariant]` attribute.
    }

    public void MyMethod<[MustBeVariant] T>(T variant)
    {
        // Do something with variant.
    }
