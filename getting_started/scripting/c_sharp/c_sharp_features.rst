.. _doc_c_sharp_features:

Features
============

This page provides an overview over the commonly used features of both C# and Godot
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
    // Only call SetFrame() if mySprite is not null
    mySprite?.SetFrame(0);

**Using the generic methods**

Generic methods are also provided to make this type conversion transparent.

``GetNode<T>()`` casts the node before returning it. It will throw an ``InvalidCastException`` if the node cannot be cast to the desired type.

.. code-block:: csharp

    Sprite mySprite = GetNode<Sprite>("MySprite");
    mySprite.SetFrame(0);

``GetNodeOrNull<T>()`` uses the ``as`` operator and will return ``null`` if the node cannot be cast to the desired type.

.. code-block:: csharp

    Sprite mySprite = GetNodeOrNull<Sprite>("MySprite");
    // Only call SetFrame() if mySprite is not null
    mySprite?.SetFrame(0);

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

.. _c_sharp_signals:

C# Signals
----------

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

It is possible to bind values when establishing a connection by passing an object array.

.. code-block:: csharp

    public int Value { get; private set; } = 0;

    private void ModifyValue(int modifier)
    {
        Value += modifier;
    }

    public void SomeFunction()
    {
        var plusButton = (Button)GetNode("PlusButton");
        var minusButton = (Button)GetNode("MinusButton");
        
        plusButton.Connect("pressed", this, "ModifyValue", new object[] { 1 });
        minusButton.Connect("pressed", this, "ModifyValue", new object[] { -1 });
    }

Signals support parameters and bound values of all the `built-in types <https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/built-in-types-table>`_ and Classes derived from :ref:`Godot.Object <class_Object>`.
Consequently any ``Node`` or ``Reference`` will be compatible automatically but custom data objects will need to extend from `Godot.Object` or one of its subclasses.

.. code-block:: csharp

    public class DataObject : Godot.Object
    {
        public string Field1 { get; set; }
        public string Field2 { get; set; }
    }


Finally, signals can be created by calling ``AddUserSignal``, but be aware that it should be executed before any use of said signals (with ``Connect`` or ``EmitSignal``).

.. code-block:: csharp

    public void SomeFunction()
    {
        AddUserSignal("MyOtherSignal");
        EmitSignal("MyOtherSignal");
    }
