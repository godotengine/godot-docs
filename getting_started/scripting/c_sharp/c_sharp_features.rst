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

Declaring a signal in C# is done with the ``[Signal]`` attribute on a delegate.

.. code-block:: csharp

    [Signal]
    delegate void MySignal();

    [Signal]
    delegate void MySignalWithArguments(string foo, int bar);

These signals can then be connected either in the editor or from code with ``Connect``.

.. code-block:: csharp

    public void MyCallback()
    {
        GD.Print("My callback!");
    }

    public void MyCallbackWithArguments(string foo, int bar)
    {
        GD.Print("My callback with: ", foo, " and ", bar, "!");
    }

    public void SomeFunction()
    {
        instance.Connect("MySignal", this, "MyCallback");
        instance.Connect(nameof(MySignalWithArguments), this, "MyCallbackWithArguments");
    }

Emitting signals is done with the ``EmitSignal`` method.

.. code-block:: csharp

    public void SomeFunction()
    {
        EmitSignal(nameof(MySignal));
        EmitSignal("MySignalWithArguments", "hello there", 28);
    }

Notice that you can always reference a signal name with the ``nameof`` keyword (applied on the delegate itself).

Finally, signals can be created by calling ``AddUserSignal``, but be aware that it should be executed before any use of said signals (with ``Connect`` or ``EmitSignal``).

.. code-block:: csharp

    public void SomeFunction()
    {
        AddUserSignal("MyOtherSignal");
        EmitSignal("MyOtherSignal");
    }
