.. _doc_c_sharp_features:

Features
============

This page provied an overview over the commonly used features of both C# and Godot
and how they are used together.

Type Conversion and Casting
---------------------------

C# is a statically typed language. Therefore you can't do the following:

.. code-block:: csharp

    var mySprite = GetNode("MySprite")
    mySprite.SetFrame(0)

The method ``GetNode()`` returns a ``Node`` instance.
You must explicitly convert it to the desired derived type, ``Sprite`` in this case.

For this, you have various options in C#.

**Casting and Type Checking**

Throws ``InvalidCastException`` if the returned node cannot be casted to Sprite.
You would use it instead of the ``as`` operator if you are pretty sure it won't fail.

.. code-block:: csharp

    Sprite mySprite = (Sprite)GetNode("MySprite");
    mySprite.SetFrame(0);

**Using the AS operator**

The ``as`` operator returns null if the node cannot be casted to Sprite,
and for this reason it cannot be used with value types.

.. code-block:: csharp

    Sprite mySprite = GetNode("MySprite") as Sprite;
    // Only call SetFrame() is mySprite is not null
    mySprite?.SetFrame(0);;

**Type checking using the IS operator**

To check if the node can be casted to Sprite, you can use the ``is`` operator.
The ``is`` operator returns false if the node cannot be casted to Sprite,
otherwise it returns true.

.. code-block:: csharp

    if (GetNode("MySprite") is Sprite)
    {
        // Yup, it's a sprite!
    }

For more advanced type checking, you can look into `Pattern Matching <https://docs.microsoft.com/en-us/dotnet/csharp/pattern-matching>`_.

Signals
-------

For a complete C# example, see the **Handling a signal** section in the step by step :ref:`doc_scripting` tutorial.

You can use ``Connect("SomeSignal", someObject, "SomeMethod")`` to connect to signals.
``AddUserSignal("SignalName")`` is used to define custom signals.
Emitting signals is done with ``EmitSignal("SignalName")``. Params can be given, like ``EmitSignal("SignalName", arg1, arg2, ...)``.

**Custom signals**

.. code-block:: csharp
   :emphasize-lines: 5, 10
   :linenos:

    public class ExampleScript : Node
    {
        public override void _Ready()
        {
            AddUserSignal("YourSignal");
        }

        public override void _Process(float delta)
        {
            EmitSignal("YourSignal");
        }
    }

Above in line 5, ``AddUserSignal()`` is used to define the new custom signal ``YourSignal``.
In line 10 ``EmitSignal()`` is used to emit that custom signal on every frame in ``_Process()``.

Make sure that ``AddUserSignal()`` is always executed before any calls using that signal (``EmitSignal()`` and ``Connect()``).
If you are using both ``AddUserSignal()`` and ``Connect()`` or ``EmitSignal()`` in ``_Ready()``, this is especially important as load order of your node may change,
and thus the order in which your various ``_Ready()`` functions are called.
