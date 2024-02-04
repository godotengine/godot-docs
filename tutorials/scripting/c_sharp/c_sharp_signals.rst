.. _doc_c_sharp_signals:

C# signals
==========

For a detailed explanation of signals in general, see the :ref:`doc_signals` section in the step
by step tutorial.

Signals are implemented using C# events, the idiomatic way to represent
:ref:`the observer pattern<doc_key_concepts_signals>` in C#. This is the
recommended way to use signals in C# and the focus of this page.

In some cases it's necessary to use the older
:ref:`Connect()<class_object_method_connect>` and
:ref:`Disconnect()<class_object_method_disconnect>` APIs.
See :ref:`using_connect_and_disconnect` for more details.

If you encounter a ``System.ObjectDisposedException`` while handling a signal,
you might be missing a signal disconnection. See
:ref:`disconnecting_automatically_when_the_receiver_is_freed` for more details.

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

Signals support arguments of any :ref:`Variant-compatible type <c_sharp_variant_compatible_types>`.

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

.. _using_connect_and_disconnect:

Using Connect and Disconnect
----------------------------

In general, it isn't recommended to use
:ref:`Connect()<class_object_method_connect>` and
:ref:`Disconnect()<class_object_method_disconnect>`. These APIs don't provide as
much type safety as the events. However, they're necessary for
:ref:`connecting to signals defined by GDScript <connecting_to_signals_cross_language>`
and passing :ref:`ConnectFlags<enum_Object_ConnectFlags>`.

In the following example, pressing the button for the first time prints
``Greetings!``. ``OneShot`` disconnects the signal, so pressing the button again
does nothing.

.. code-block:: csharp

    public override void _Ready()
    {
        Button button = GetNode<Button>("GreetButton");
        button.Connect(Button.SignalName.Pressed, Callable.From(OnButtonPressed), (uint)GodotObject.ConnectFlags.OneShot);
    }

    public void OnButtonPressed()
    {
        GD.Print("Greetings!");
    }

.. _disconnecting_automatically_when_the_receiver_is_freed:

Disconnecting automatically when the receiver is freed
------------------------------------------------------

Normally, when any ``GodotObject`` is freed (such as any ``Node``), Godot
automatically disconnects all connections associated with that object. This
happens for both signal emitters and signal receivers.

For example, a node with this code will print "Hello!" when the button is
pressed, then free itself. Freeing the node disconnects the signal, so pressing
the button again doesn't do anything:

.. code-block:: csharp

    public override void _Ready()
    {
        Button myButton = GetNode<Button>("../MyButton");
        myButton.Pressed += SayHello;
    }

    private void SayHello()
    {
        GD.Print("Hello!");
        Free();
    }

When a signal receiver is freed while the signal emitter is still alive, in some
cases automatic disconnection won't happen:

- The signal is connected to a lambda expression that captures a variable.
- The signal is a custom signal.

The following sections explain these cases in more detail and include
suggestions for how to disconnect manually.

.. note::

    Automatic disconnection is totally reliable if a signal emitter is freed
    before any of its receivers are freed. With a project style that prefers
    this pattern, the above limits may not be a concern.

No automatic disconnection: a lambda expression that captures a variable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you connect to a lambda expression that captures variables, Godot can't tell
that the lambda is associated with the instance that created it. This causes
this example to have potentially unexpected behavior:

.. code-block:: csharp

    Timer myTimer = GetNode<Timer>("../Timer");
    int x = 0;
    myTimer.Timeout += () =>
    {
        x++; // This lambda expression captures x.
        GD.Print($"Tick {x} my name is {Name}");
        if (x == 3)
        {
            GD.Print("Time's up!");
            Free();
        }
    };

.. code-block:: text

    Tick 1, my name is ExampleNode
    Tick 2, my name is ExampleNode
    Tick 3, my name is ExampleNode
    Time's up!
    [...] System.ObjectDisposedException: Cannot access a disposed object.

On tick 4, the lambda expression tries to access the ``Name`` property of the
node, but the node has already been freed. This causes the exception.

To disconnect, keep a reference to the delegate created by the lambda expression
and pass that to ``-=``. For example, this node connects and disconnects using
the ``_EnterTree`` and ``_ExitTree`` lifecycle methods:

.. code-block:: csharp

    [Export]
    public Timer MyTimer { get; set; }

    private Action _tick;

    public override void _EnterTree()
    {
        int x = 0;
        _tick = () =>
        {
            x++;
            GD.Print($"Tick {x} my name is {Name}");
            if (x == 3)
            {
                GD.Print("Time's up!");
                Free();
            }
        };
        MyTimer.Timeout += _tick;
    }

    public override void _ExitTree()
    {
        MyTimer.Timeout -= _tick;
    }

In this example, ``Free`` causes the node to leave the tree, which calls
``_ExitTree``. ``_ExitTree`` disconnects the signal, so ``_tick`` is never
called again.

The lifecycle methods to use depend on what the node does. Another option is to
connect to signals in ``_Ready`` and disconnect in ``Dispose``.

.. note::

    Godot uses `Delegate.Target <https://learn.microsoft.com/en-us/dotnet/api/system.delegate.target>`_
    to determine what instance a delegate is associated with. When a lambda
    expression doesn't capture a variable, the generated delegate's ``Target``
    is the instance that created the delegate. When a variable is captured, the
    ``Target`` instead points at a generated type that stores the captured
    variable. This is what breaks the association. If you want to see if a
    delegate will be automatically cleaned up, try checking its ``Target``.

    ``Callable.From`` doesn't affect the ``Delegate.Target``, so connecting a
    lambda that captures variables using ``Connect`` doesn't work any better
    than ``+=``.

No automatic disconnection: a custom signal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Connecting to a custom signal using ``+=`` doesn't disconnect automatically when
the receiving node is freed.

To disconnect, use ``-=`` at an appropriate time. For example:

.. code-block:: csharp

    [Export]
    public MyClass Target { get; set; }

    public override void _EnterTree()
    {
        Target.MySignal += OnMySignal;
    }

    public override void _ExitTree()
    {
        Target.MySignal -= OnMySignal;
    }

Another solution is to use ``Connect``, which does disconnect automatically with
custom signals:

.. code-block:: csharp

    [Export]
    public MyClass Target { get; set; }

    public override void _EnterTree()
    {
        Target.Connect(MyClass.SignalName.MySignal, Callable.From(OnMySignal));
    }
