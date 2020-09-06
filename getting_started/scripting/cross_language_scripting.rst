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

    var str1 : String = "foo"
    var str2 : String setget ,get_str2

    func get_str2() -> String:
        return "foofoo"

    func print_node_name(node : Node) -> void:
        print(node.get_name())

    func print_array(arr : Array) -> void:
        for element in arr:
            print(element)

    func print_x_times(msg : String, n : int) -> void:
        for i in range(n):
            print(msg)

 .. code-tab:: csharp

    public class MyCSharpNode : Node
    {
        public String str1 = "bar";
        public String str2 { get { return "barbar"; } }

        public void PrintNodeName(Node node)
        {
            GD.Print(node.GetName());
        }

        public void PrintArray(String[] arr)
        {
            foreach (String element in arr)
            {
                GD.Print(element);
            }
        }

        public void PrintNTimes(String msg, int n)
        {
            for (int i = 0; i < n; ++i)
            {
                GD.Print(msg);
            }
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

::

    var my_csharp_script = load("res://path_to_cs_file.cs")
    var my_csharp_node = my_csharp_script.new()
    print(my_csharp_node.str2) # barbar

.. warning::

    When creating ``.cs`` scripts, you should always keep in mind that the class
    Godot will use is the one named like the ``.cs`` file itself. If that class
    does not exist in the file, you'll see the following error:
    ``Invalid call. Nonexistent function `new` in base``.

    For example, MyCoolNode.cs should contain a class named MyCoolNode.

    You also need to check your ``.cs`` file is referenced in the project's
    ``.csproj`` file. Otherwise, the same error will occur.

Instantiating GDScript nodes from C#
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

From the C# side, everything work the same way. Once loaded, the GDScript can
be instantiated with :ref:`GDScript.New() <class_GDScript_method_new>`.

.. code-block:: csharp

    GDScript MyGDScript = (GDScript) GD.Load("res://path_to_gd_file.gd");
    Object myGDScriptNode = (Godot.Object) MyGDScript.New(); // This is a Godot.Object

Here we are using an :ref:`class_Object`, but you can use type conversion like
explained in :ref:`doc_c_sharp_features_type_conversion_and_casting`.

Accessing fields
----------------

Accessing C# fields from GDScript
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Accessing C# fields from GDScript is straightforward, you shouldn't have
anything to worry about.

::

    print(my_csharp_node.str1) # bar
    my_csharp_node.str1 = "BAR"
    print(my_csharp_node.str1) # BAR

    print(my_csharp_node.str2) # barbar
    # my_csharp_node.str2 = "BARBAR" # This line will hang and crash

Note that it doesn't matter if the field is defined as a property or an
attribute. However, trying to set a value on a property that does not define
a setter will result in a crash.

Accessing GDScript fields from C#
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As C# is statically typed, accessing GDScript from C# is a bit more
convoluted, you will have to use :ref:`Object.Get() <class_Object_method_get>`
and :ref:`Object.Set() <class_Object_method_set>`. The first argument is the name of the field you want to access.

.. code-block:: csharp

    GD.Print(myGDScriptNode.Get("str1")); // foo
    myGDScriptNode.Set("str1", "FOO");
    GD.Print(myGDScriptNode.Get("str1")); // FOO

    GD.Print(myGDScriptNode.Get("str2")); // foofoo
    // myGDScriptNode.Set("str2", "FOOFOO"); // This line won't do anything

Keep in mind that when setting a field value you should only use types the
GDScript side knows about.
Essentially, you want to work with built-in types as described in :ref:`doc_gdscript` or classes extending :ref:`class_Object`.

Calling methods
---------------

Calling C# methods from GDScript
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Again, calling C# methods from GDScript should be straightforward. The
marshalling process will do its best to cast your the arguments to match
function signatures.
If that's impossible, you'll see the following error: ``Invalid call. Nonexistent function `FunctionName```.

::

    my_csharp_node.PrintNodeName(self) # myGDScriptNode
    # my_csharp_node.PrintNodeName() # This line will fail.

    my_csharp_node.PrintNTimes("Hello there!", 2) # Hello there! Hello there!

    my_csharp_node.PrintArray(["a", "b", "c"]) # a, b, c
    my_csharp_node.PrintArray([1, 2, 3]) # 1, 2, 3

Calling GDScript methods from C#
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To call GDScript methods from C# you'll need to use
:ref:`Object.Call() <class_Object_method_call>`. The first argument is the
name of the method you want to call. The following arguments will be passed
to said method.

.. code-block:: csharp

    myGDScriptNode.Call("print_node_name", this); // my_csharp_node
    // myGDScriptNode.Call("print_node_name"); // This line will fail silently and won't error out.

    myGDScriptNode.Call("print_n_times", "Hello there!", 2); // Hello there! Hello there!

    // When dealing with functions taking a single array as arguments, we need to be careful.
    // If we don't cast it into an object, the engine will treat each element of the array as a separate argument and the call will fail.
    String[] arr = new String[] { "a", "b", "c" };
    // myGDScriptNode.Call("print_array", arr); // This line will fail silently and won't error out.
    myGDScriptNode.Call("print_array", (object)arr); // a, b, c
    myGDScriptNode.Call("print_array", (object)new int[] { 1, 2, 3 }); // 1, 2, 3
    // Note how the type of each array entry does not matter as long as it can be handled by the marshaller

.. warning::

    As you can see, if the first argument of the called method is an array,
    you'll need to cast it as ``object``.
    Otherwise, each element of your array will be treated as a single argument
    and the function signature won't match.

Inheritance
-----------

A GDScript file may not inherit from a C# script. Likewise, a C# script may not
inherit from a GDScript file. Due to how complex this would be to implement,
this limitation is unlikely to be lifted in the future. See
`this GitHub issue <https://github.com/godotengine/godot/issues/38352>`__
for more information.
