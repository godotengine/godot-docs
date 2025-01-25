.. _doc_cross_language_scripting:

Cross-language scripting
========================

Godot allows you to mix and match scripting languages to suit your needs.
This means a single project can define nodes in both C# and GDScript.
This page will go through the possible interactions between two nodes written
in different languages.

The following two scripts will be used as references throughout this page.

.. tabs::

 .. code-tab:: gdscript GDScript

    extends Node

    var my_property: String = "my gdscript value":
        get:
            return my_property
        set(value):
            my_property = value

    signal my_signal
    signal my_signal_with_params(msg: String, n: int)

    func print_node_name(node: Node) -> void:
        print(node.get_name())

    func print_array(arr: Array) -> void:
        for element in arr:
            print(element)

    func print_n_times(msg: String, n: int) -> void:
        for i in range(n):
            print(msg)

    func my_signal_handler():
        print("The signal handler was called!")

    func my_signal_with_params_handler(msg: String, n: int):
        print_n_times(msg, n)

 .. code-tab:: csharp

    using Godot;

    public partial class MyCSharpNode : Node
    {
        public string MyProperty { get; set; } = "my c# value";

        [Signal] public delegate void MySignalEventHandler();
        [Signal] public delegate void MySignalWithParamsEventHandler(string msg, int n);

        public void PrintNodeName(Node node)
        {
            GD.Print(node.Name);
        }

        public void PrintArray(string[] arr)
        {
            foreach (string element in arr)
            {
                GD.Print(element);
            }
        }

        public void PrintNTimes(string msg, int n)
        {
            for (int i = 0; i < n; ++i)
            {
                GD.Print(msg);
            }
        }

        public void MySignalHandler()
        {
            GD.Print("The signal handler was called!");
        }

        public void MySignalWithParamsHandler(string msg, int n)
        {
            PrintNTimes(msg, n);
        }
    }

Instantiating nodes
-------------------

If you're not using nodes from the scene tree, you'll probably want to
instantiate nodes directly from the code.

Instantiating C# nodes from GDScript
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Using C# from GDScript doesn't need much work. Once loaded
(see :ref:`doc_gdscript_classes_as_resources`), the script can be instantiated
with :ref:`new() <class_CSharpScript_method_new>`.

.. code-block:: gdscript

    var MyCSharpScript = load("res://Path/To/MyCSharpNode.cs")
    var my_csharp_node = MyCSharpScript.new()

.. warning::

    When creating ``.cs`` scripts, you should always keep in mind that the class
    Godot will use is the one named like the ``.cs`` file itself. If that class
    does not exist in the file, you'll see the following error:
    ``Invalid call. Nonexistent function `new` in base``.

    For example, MyCoolNode.cs should contain a class named MyCoolNode.

    The C# class needs to derive a Godot class, for example ``GodotObject``.
    Otherwise, the same error will occur.

    You also need to check your ``.cs`` file is referenced in the project's
    ``.csproj`` file. Otherwise, the same error will occur.

Instantiating GDScript nodes from C#
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

From the C# side, everything work the same way. Once loaded, the GDScript can
be instantiated with :ref:`GDScript.New() <class_GDScript_method_new>`.

.. code-block:: csharp

    var myGDScript = GD.Load<GDScript>("res://path/to/my_gd_script.gd");
    var myGDScriptNode = (GodotObject)myGDScript.New(); // This is a GodotObject.

Here we are using an :ref:`class_Object`, but you can use type conversion like
explained in :ref:`doc_c_sharp_features_type_conversion_and_casting`.

Accessing fields
----------------

Accessing C# fields from GDScript
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Accessing C# fields from GDScript is straightforward, you shouldn't have
anything to worry about.

.. code-block:: gdscript

    # Output: "my c# value".
    print(my_csharp_node.MyProperty)
    my_csharp_node.MyProperty = "MY C# VALUE"
    # Output: "MY C# VALUE".
    print(my_csharp_node.MyProperty)

Accessing GDScript fields from C#
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As C# is statically typed, accessing GDScript from C# is a bit more
convoluted. You will have to use :ref:`GodotObject.Get() <class_Object_method_get>`
and :ref:`GodotObject.Set() <class_Object_method_set>`. The first argument is the name of the field you want to access.

.. code-block:: csharp

    // Output: "my gdscript value".
    GD.Print(myGDScriptNode.Get("my_property"));
    myGDScriptNode.Set("my_property", "MY GDSCRIPT VALUE");
    // Output: "MY GDSCRIPT VALUE".
    GD.Print(myGDScriptNode.Get("my_property"));

Keep in mind that when setting a field value you should only use types the
GDScript side knows about.
Essentially, you want to work with built-in types as described in :ref:`doc_gdscript` or classes extending :ref:`class_Object`.

Calling methods
---------------

Calling C# methods from GDScript
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Again, calling C# methods from GDScript should be straightforward. The
marshalling process will do its best to cast the arguments to match
function signatures.
If that's impossible, you'll see the following error: ``Invalid call. Nonexistent function `FunctionName```.

.. code-block:: gdscript

    # Output: "my_gd_script_node" (or name of node where this code is placed).
    my_csharp_node.PrintNodeName(self)
    # This line will fail.
    # my_csharp_node.PrintNodeName()

    # Outputs "Hello there!" twice, once per line.
    my_csharp_node.PrintNTimes("Hello there!", 2)

    # Output: "a", "b", "c" (one per line).
    my_csharp_node.PrintArray(["a", "b", "c"])
    # Output: "1", "2", "3"  (one per line).
    my_csharp_node.PrintArray([1, 2, 3])

Calling GDScript methods from C#
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To call GDScript methods from C# you'll need to use
:ref:`GodotObject.Call() <class_Object_method_call>`. The first argument is the
name of the method you want to call. The following arguments will be passed
to said method.

.. code-block:: csharp

    // Output: "MyCSharpNode" (or name of node where this code is placed).
    myGDScriptNode.Call("print_node_name", this);
    // This line will fail silently and won't error out.
    // myGDScriptNode.Call("print_node_name");

    // Outputs "Hello there!" twice, once per line.
    myGDScriptNode.Call("print_n_times", "Hello there!", 2);

    string[] arr = ["a", "b", "c"];
    // Output: "a", "b", "c" (one per line).
    myGDScriptNode.Call("print_array", arr);
    // Output: "1", "2", "3"  (one per line).
    myGDScriptNode.Call("print_array", new int[] { 1, 2, 3 });
    // Note how the type of each array entry does not matter
    // as long as it can be handled by the marshaller.

.. _connecting_to_signals_cross_language:

Connecting to signals
---------------------

Connecting to C# signals from GDScript
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Connecting to a C# signal from GDScript is the same as connecting to a signal
defined in GDScript:

.. code-block:: gdscript

    my_csharp_node.MySignal.connect(my_signal_handler)

    my_csharp_node.MySignalWithParams.connect(my_signal_with_params_handler)

Connecting to GDScript signals from C#
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Connecting to a GDScript signal from C# only works with the ``Connect`` method
because no C# static types exist for signals defined by GDScript:

.. code-block:: csharp

    myGDScriptNode.Connect("my_signal", Callable.From(MySignalHandler));

    myGDScriptNode.Connect("my_signal_with_params", Callable.From<string, int>(MySignalWithParamsHandler));

Inheritance
-----------

A GDScript file may not inherit from a C# script. Likewise, a C# script may not
inherit from a GDScript file. Due to how complex this would be to implement,
this limitation is unlikely to be lifted in the future. See
`this GitHub issue <https://github.com/godotengine/godot/issues/38352>`__
for more information.
