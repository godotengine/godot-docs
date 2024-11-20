GD0002: Missing partial modifier on declaration of type which contains nested classes that derive from GodotObject
==================================================================================================================

====================================  ======================================
                                      Value
====================================  ======================================
**Rule ID**                           GD0002
**Category**                          Usage
**Fix is breaking or non-breaking**   Non-breaking
**Enabled by default**                Yes
====================================  ======================================

Cause
-----

A type that derives from ``GodotObject`` is contained in a non-partial type declaration.

Rule description
----------------

Godot source generators add generated code to user-defined types to implement
the integration with the engine. Source generators can't add generated code to
types that aren't declared partial.

.. code-block:: csharp

    public class InvalidParentType
    {
        // MyNode is contained in a non-partial type so the source generators
        // can't enhance this type to work with Godot.
        public partial class MyNode : Node { }
    }

    public partial class ValidParentType
    {
        // MyNode is contained in a partial type so the source generators
        // can enhance this type to work with Godot.
        public partial class MyNode : Node { }
    }

How to fix violations
---------------------

To fix a violation of this rule, add the ``partial`` keyword to the type
declaration.

When to suppress warnings
-------------------------

Do not suppress a warning from this rule. Types that derive from ``GodotObject``
but aren't partial can't be enhanced by the source generators, resulting in
unexpected runtime errors.
