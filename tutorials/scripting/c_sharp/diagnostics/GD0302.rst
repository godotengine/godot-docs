GD0302: The generic type parameter must be annotated with the '[MustBeVariant]' attribute
=========================================================================================

====================================  ======================================
                                      Value
====================================  ======================================
**Rule ID**                           GD0302
**Category**                          Usage
**Fix is breaking or non-breaking**   Breaking
**Enabled by default**                Yes
====================================  ======================================

Cause
-----

A generic type is specified for a generic type argument when a
:ref:`Variant-compatible type <c_sharp_variant_compatible_types>` is expected,
but the specified generic type is not annotated with the ``[MustBeVariant]``
attribute.

Rule description
----------------

When a generic type parameter is annotated with the ``[MustBeVariant]`` attribute,
the generic type is required to be a Variant-compatible type. When the type used
is also a generic type, this generic type must be annotated with the ``[MustBeVariant]``
attribute as well. For example, the generic ``Godot.Collections.Array<T>`` type
only supports items of a type that can be converted to Variant, a generic type
can be specified if it's properly annotated.

.. code-block:: csharp

    public void Method1<T>()
    {
        // T is not valid here because it may not a Variant-compatible type.
        var invalidArray = new Godot.Collections.Array<T>();
    }

    public void Method2<[MustBeVariant] T>()
    {
        // T is guaranteed to be a Variant-compatible type because it's annotated
        // with the [MustBeVariant] attribute, so it can be used here.
        var validArray = new Godot.Collections.Array<T>();
    }

How to fix violations
---------------------

To fix a violation of this rule, add the ``[MustBeVariant]`` attribute to the
generic type that is used as a generic type argument that must be Variant-compatible.

When to suppress warnings
-------------------------

Do not suppress a warning from this rule. API that contains generic type arguments
annotated with the ``[MustBeVariant]`` attribute usually has this requirement
because the values will be passed to the engine, if the type can't be marshalled
it will result in runtime errors.
