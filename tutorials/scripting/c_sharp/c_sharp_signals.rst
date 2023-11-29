.. _doc_c_sharp_signals:

C# signals
==========

For a detailed explanation of signals in general, see the :ref:`doc_signals` section in the step
by step tutorial.

While it is still possible to use signals through the ``Connect``/``Disconnect`` API, C# gives us
a more idiomatic way to implement the :ref:`observer pattern<doc_key_concepts_signals>`.

Signals as C# events
--------------------

To provide more type-safety, Godot signals are also all available through `events <https://learn.microsoft.com/en-us/dotnet/csharp/events-overview>`_.
You can handle these events, as any other event, with the ``+=`` and ``-=`` operators.

.. code-block:: csharp

    Timer myTimer = GetNode<Timer>("Timer");
    myTimer.Timeout += () => GD.Print("Timeout!");

In addition, you can always access signal names associated with a node type through its nested
``SignalName`` class. This is useful when, for example, you want to await on a signal (see :ref:`doc_c_sharp_differences_await`).

.. code-block:: csharp

    await ToSignal(GetTree(), SceneTree.SignalName.ProcessFrame);

.. warning::

    While all engine signals connected as events are automatically disconnected when nodes are freed, custom
    signals aren't. Meaning that: you will need to manually disconnect (using ``-=``) all the custom signals you
    connected as C# events (using ``+=``).

Custom signals as C# events
---------------------------

To declare a custom event in your C# script, use the ``[Signal]`` attribute on a public delegate type.
Note that the name of this delegate needs to end with ``EventHandler``.

.. code-block:: csharp

    [Signal]
    public delegate void MySignalEventHandler();

    [Signal]
    public delegate void MySignalWithArgumentEventHandler(string myString);

Once this is done, Godot will create the appropriate events automatically behind the scenes. You
can then use said events as you'd do for any other Godot signal. Note that events are named using
your delegate's name minus the final ``EventHandler`` part.

.. code-block:: csharp

    public override void _Ready()
    {
        MySignal += () => GD.Print("Hello!");
        MySignalWithArgument += SayHelloTo;
    }

    private void SayHelloTo(string name)
    {
        GD.Print($"Hello {name}!");
    }

.. warning::

    If you want to connect to these signals in the editor, you will need to (re)build the project
    to see them appear.

    You can click the **Build** button in the upper-right corner of the editor to do so.

Signal emission
---------------

To emit signals, use the ``EmitSignal`` method. Note that, as for signals defined by the engine,
your custom signal names are listed under the nested ``SignalName`` class.

.. code-block:: csharp

    public void MyMethodEmittingSignals()
    {
        EmitSignal(SignalName.MySignal);
        EmitSignal(SignalName.MySignalWithArgument, "World");
    }

In contrast with other C# events, you cannot use ``Invoke`` to raise events tied to Godot signals.

Signals support arguments of any :ref:`Variant-compatible <doc_c_sharp_variant>` type.

Consequently, any ``Node`` or ``RefCounted`` will be compatible automatically, but custom data objects will need
to inherit from ``GodotObject`` or one of its subclasses.

.. code-block:: csharp

    using Godot;

    public partial class DataObject : GodotObject
    {
        public string MyFirstString { get; set; }
        public string MySecondString { get; set; }
    }

Bound values
------------

Sometimes you'll want to bind values to a signal when the connection is established, rather than
(or in addition to) when the signal is emitted. To do so, you can use an anonymous function like in
the following example.

Here, the :ref:`Button.Pressed <class_BaseButton_signal_pressed>` signal do not take any argument. But we
want to use the same ``ModifyValue`` for both the "plus" and "minus" buttons. So we bind the
modifier value at the time we're connecting the signals.

.. code-block:: csharp

    public int Value { get; private set; } = 1;

    public override void _Ready()
    {
        Button plusButton = GetNode<Button>("PlusButton");
        plusButton.Pressed += () => ModifyValue(1);

        Button minusButton = GetNode<Button>("MinusButton");
        minusButton.Pressed += () => ModifyValue(-1);
    }

    private void ModifyValue(int modifier)
    {
        Value += modifier;
    }

Signal creation at runtime
--------------------------

Finally, you can create custom signals directly while your game is running. Use the ``AddUserSignal``
method for that. Be aware that it should be executed before any use of said signals (either
connecting to them or emitting them). Also, note that signals created this way won't be visible through the
``SignalName`` nested class.

.. code-block:: csharp

    public override void _Ready()
    {
        AddUserSignal("MyCustomSignal");
        EmitSignal("MyCustomSignal");
    }
