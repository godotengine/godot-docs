.. _doc_evaluating_expressions:

Evaluating expressions
======================

Godot provides an :ref:`class_Expression` class you can use to evaluate expressions.

An expression can be:

- A mathematical expression such as ``(2 + 4) * 16/4.0``.
- A boolean expression such as ``true && false``.
- A built-in method call like ``deg_to_rad(90)``.
- A method call on a user-provided script like ``update_health()``,
  if ``base_instance`` is set to a value other than ``null`` when calling
  :ref:`Expression.execute() <class_Expression_method_execute>`.

.. note::

    The Expression class is independent from GDScript.
    It's available even if you compile Godot with the GDScript module disabled.

Basic usage
-----------

To evaluate a mathematical expression, use:

::

    var expression = Expression.new()
    expression.parse("20 + 10*2 - 5/2.0")
    var result = expression.execute()
    print(result)  # 37.5

The following operators are available:

+------------------------+-------------------------------------------------------------------------------------+
| Operator               | Notes                                                                               |
+========================+=====================================================================================+
| Addition ``+``         | Can also be used to concatenate strings and arrays:                                 |
|                        | - ``"hello" + " world"`` = ``hello world``                                          |
|                        | - ``[1, 2] + [3, 4]`` = ``[1, 2, 3, 4]``                                            |
+------------------------+-------------------------------------------------------------------------------------+
| Subtraction (``-``)    |                                                                                     |
+------------------------+-------------------------------------------------------------------------------------+
| Multiplication (``*``) |                                                                                     |
+------------------------+-------------------------------------------------------------------------------------+
| Division (``/``)       | Performs and integer division if both operands are integers.                        |
|                        | If at least one of them is a floating-point number, returns a floating-point value. |
+------------------------+-------------------------------------------------------------------------------------+
| Remainder (``%``)      | Returns the remainder of an integer division (modulo).                              |
|                        | The result will always have the sign of the dividend.                               |
+------------------------+-------------------------------------------------------------------------------------+
| Conjunction (``&&``)   | Returns the result of a boolean AND.                                                |
+------------------------+-------------------------------------------------------------------------------------+
| Disjunction (``||``)   | Returns the result of a boolean OR.                                                 |
+------------------------+-------------------------------------------------------------------------------------+
| Negation (``!``)       | Returns the result of a boolean NOT.                                                |
+------------------------+-------------------------------------------------------------------------------------+

Spaces around operators are optional. Also, keep in mind the usual
`order of operations <https://en.wikipedia.org/wiki/Order_of_operations>`__
applies. Use parentheses to override the order of operations if needed.

All the Variant types supported in Godot can be used: integers, floating-point
numbers, strings, arrays, dictionaries, colors, vectors, …

Arrays and dictionaries can be indexed like in GDScript:

::

    # Returns 1.
    [1, 2][0]

    # Returns 3. Negative indices can be used to count from the end of the array.
    [1, 3][-1]

    # Returns "green".
    {"favorite_color": "green"}["favorite_color"]

    # All 3 lines below return 7.0 (Vector3 is floating-point).
    Vector3(5, 6, 7)[2]
    Vector3(5, 6, 7)["z"]
    Vector3(5, 6, 7).z

Passing variables to an expression
----------------------------------

You can pass variables to an expression. These variables will then
become available in the expression's "context" and will be substituted when used
in the expression:

::

    var expression = Expression.new()
    # Define the variable names first in the second parameter of `parse()`.
    # In this example, we use `x` for the variable name.
    expression.parse("20 + 2 * x", ["x"])
    # Then define the variable values in the first parameter of `execute()`.
    # Here, `x` is assigned the integer value 5.
    var result = expression.execute([5])
    print(result)  # 30

Both the variable names and variable values **must** be specified as an array,
even if you only define one variable. Also, variable names are **case-sensitive**.

Setting a base instance for the expression
------------------------------------------

By default, an expression has a base instance of ``null``. This means the
expression has no base instance associated to it.

When calling :ref:`Expression.execute() <class_Expression_method_execute>`,
you can set the value of the ``base_instance`` parameter to a specific object
instance such as ``self``, another script instance or even a singleton:

::

    func double(number):
        return number * 2


    func _ready():
        var expression = Expression.new()
        expression.parse("double(10)")

        # This won't work since we're not passing the current script as the base instance.
        var result = expression.execute([], null)
        print(result)  # null

        # This will work since we're passing the current script (i.e. self)
        # as the base instance.
        result = expression.execute([], self)
        print(result)  # 20

Associating a base instance allows doing the following:

- Reference the instance's constants (``const``) in the expression.
- Reference the instance's member variables (``var``) in the expression.
- Call methods defined in the instance and use their return values in the expression.

.. warning::

    Setting a base instance to a value other than ``null`` allows referencing
    constants, member variables, and calling all methods defined in the script
    attached to the instance. Allowing users to enter expressions may allow
    cheating in your game, or may even introduce security vulnerabilities if you
    allow arbitrary clients to run expressions on other players' devices.

Example script
--------------

The script below demonstrates what the Expression class is capable of:

::

    const DAYS_IN_YEAR = 365
    var script_member_variable = 1000


    func _ready():
        # Constant boolean expression.
        evaluate("true && false")
        # Boolean expression with variables.
        evaluate("!(a && b)", ["a", "b"], [true, false])

        # Constant mathexpression.
        evaluate("2 + 2")
        # Math expression with variables.
        evaluate("x + y", ["x", "y"], [60, 100])

        # Call built-in method (built-in math function call).
        evaluate("deg_to_rad(90)")

        # Call user method (defined in the script).
        # We can do this because the expression execution is bound to `self`
        # in the `evaluate()` method.
        # Since this user method returns a value, we can use it in math expressions.
        evaluate("call_me() + DAYS_IN_YEAR + script_member_variable")
        evaluate("call_me(42)")
        evaluate("call_me('some string')")


    func evaluate(command, variable_names = [], variable_values = []) -> void:
        var expression = Expression.new()
        var error = expression.parse(command, variable_names)
        if error != OK:
            push_error(expression.get_error_text())
            return

        var result = expression.execute(variable_values, self)

        if not expression.has_execute_failed():
            print(str(result))


    func call_me(argument = null):
        print("\nYou called 'call_me()' in the expression text.")
        if argument:
            print("Argument passed: %s" % argument)

        # The method's return value is also the expression's return value.
        return 0

The output from the script will be:

::

    false
    true
    4
    160
    1.5707963267949

    You called 'call_me()' in the expression text.
    1365

    You called 'call_me()' in the expression text.
    Argument passed: 42
    0

    You called 'call_me()' in the expression text.
    Argument passed: some string
    0

Built-in functions
------------------

All methods in the :ref:`Global Scope<class_@GlobalScope>` are available in the
Expression class, even if no base instance is bound to the expression.
The same parameters and return types are available.

However, unlike GDScript, parameters are **always required** even if they're
specified as being optional in the class reference. In contrast, this
restriction on arguments doesn't apply to user-made functions when you bind a
base instance to the expression.
