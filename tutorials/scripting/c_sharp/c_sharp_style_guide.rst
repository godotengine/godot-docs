.. _doc_c_sharp_styleguide:

C# style guide
==============

Having well-defined and consistent coding conventions is important for every project, and Godot
is no exception to this rule.

This page contains a coding style guide, which is followed by developers of and contributors to Godot
itself. As such, it is mainly intended for those who want to contribute to the project, but since
the conventions and guidelines mentioned in this article are those most widely adopted by the users
of the language, we encourage you to do the same, especially if you do not have such a guide yet.

.. note:: This article is by no means an exhaustive guide on how to follow the standard coding
        conventions or best practices. If you feel unsure of an aspect which is not covered here,
        please refer to more comprehensive documentation, such as
        `C# Coding Conventions <https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/inside-a-program/coding-conventions>`_ or
        `Framework Design Guidelines <https://docs.microsoft.com/en-us/dotnet/standard/design-guidelines/naming-guidelines>`_.

Language specification
----------------------

Godot currently uses **C# version 12.0** in its engine and example source code,
as this is the version supported by .NET 8.0 (the current baseline requirement).
So, before we move to a newer version, care must be taken to avoid mixing
language features only available in C# 13.0 or later.

For detailed information on C# features in different versions, please see
`What's New in C# <https://docs.microsoft.com/en-us/dotnet/csharp/whats-new/>`_.

Formatting
----------

General guidelines
~~~~~~~~~~~~~~~~~~

* Use line feed (**LF**) characters to break lines, not CRLF or CR.
* Use one line feed character at the end of each file, except for `csproj` files.
* Use **UTF-8** encoding without a `byte order mark <https://en.wikipedia.org/wiki/Byte_order_mark>`_.
* Use **4 spaces** instead of tabs for indentation (which is referred to as "soft tabs").
* Consider breaking a line into several if it's longer than 100 characters.


Line breaks and blank lines
~~~~~~~~~~~~~~~~~~~~~~~~~~~

For a general indentation rule, follow `the "Allman Style" <https://en.wikipedia.org/wiki/Indentation_style#Allman_style>`_
which recommends placing the brace associated with a control statement on the next line, indented to
the same level:

.. code-block:: csharp

    // Use this style:
    if (x > 0)
    {
        DoSomething();
    }

    // NOT this:
    if (x > 0) {
        DoSomething();
    }

However, you may choose to omit line breaks inside brackets:

* For simple property accessors.
* For simple object, array, or collection initializers.
* For abstract auto property, indexer, or event declarations.

.. code-block:: csharp

    // You may put the brackets in a single line in following cases:
    public interface MyInterface
    {
        int MyProperty { get; set; }
    }

    public class MyClass : ParentClass
    {
        public int Value
        {
            get { return 0; }
            set
            {
                ArrayValue = new [] {value};
            }
        }
    }

Insert a blank line:

* After a list of ``using`` statements.
* Between method, properties, and inner type declarations.
* At the end of each file.

Field and constant declarations can be grouped together according to relevance. In that case, consider
inserting a blank line between the groups for easier reading.

Avoid inserting a blank line:

* After ``{``, the opening brace.
* Before ``}``, the closing brace.
* After a comment block or a single-line comment.
* Adjacent to another blank line.

.. code-block:: csharp

    using System;
    using Godot;
                                              // Blank line after `using` list.
    public class MyClass
    {                                         // No blank line after `{`.
        public enum MyEnum
        {
            Value,
            AnotherValue                      // No blank line before `}`.
        }
                                              // Blank line around inner types.
        public const int SomeConstant = 1;
        public const int AnotherConstant = 2;

        private Vector3 _x;                  // Related constants or fields can be
        private Vector3 _y;                  // grouped together.

        private float _width;
        private float _height;

        public int MyProperty { get; set; }
                                              // Blank line around properties.
        public void MyMethod()
        {
            // Some comment.
            AnotherMethod();                  // No blank line after a comment.
        }
                                              // Blank line around methods.
        public void AnotherMethod()
        {
        }
    }


Using spaces
~~~~~~~~~~~~

Insert a space:

* Around a binary and ternary operator.
* Between an opening parenthesis and ``if``, ``for``, ``foreach``, ``catch``, ``while``, ``lock`` or ``using`` keywords.
* Before and within a single line accessor block.
* Between accessors in a single line accessor block.
* After a comma which is not at the end of a line.
* After a semicolon in a ``for`` statement.
* After a colon in a single line ``case`` statement.
* Around a colon in a type declaration.
* Around a lambda arrow.
* After a single-line comment symbol (``//``), and before it if used at the end of a line.
* After the opening brace, and before the closing brace in a single line initializer.

Do not use a space:

* After type cast parentheses.

The following example shows a proper use of spaces, according to some of the above mentioned conventions:

.. code-block:: csharp

    public class MyClass<A, B> : Parent<A, B>
    {
        public float MyProperty { get; set; }

        public float AnotherProperty
        {
            get { return MyProperty; }
        }

        public void MyMethod()
        {
            int[] values = { 1, 2, 3, 4 };
            int sum = 0;

            // Single line comment.
            for (int i = 0; i < values.Length; i++)
            {
                switch (i)
                {
                    case 3: return;
                    default:
                        sum += i > 2 ? 0 : 1;
                        break;
                }
            }

            i += (int)MyProperty; // No space after a type cast.
        }
    }

Naming conventions
------------------

Use **PascalCase** for all namespaces, type names and member level identifiers (i.e. methods, properties,
constants, events), except for private fields:

.. code-block:: csharp

    namespace ExampleProject
    {
        public class PlayerCharacter
        {
            public const float DefaultSpeed = 10f;

            public float CurrentSpeed { get; set; }

            protected int HitPoints;

            private void CalculateWeaponDamage()
            {
            }
        }
    }

Use **camelCase** for all other identifiers (i.e. local variables, method arguments), and use
an underscore (``_``) as a prefix for private fields (but not for methods or properties, as explained above):

.. code-block:: csharp

    private Vector3 _aimingAt; // Use an `_` prefix for private fields.

    private void Attack(float attackStrength)
    {
        Enemy targetFound = FindTarget(_aimingAt);

        targetFound?.Hit(attackStrength);
    }

There's an exception with acronyms which consist of two letters, like ``UI``, which should be written in
uppercase letters where PascalCase would be expected, and in lowercase letters otherwise.

Note that ``id`` is **not** an acronym, so it should be treated as a normal identifier:

.. code-block:: csharp

    public string Id { get; }

    public UIManager UI
    {
        get { return uiManager; }
    }

It is generally discouraged to use a type name as a prefix of an identifier, like ``string strText``
or ``float fPower``, for example. An exception is made, however, for interfaces, which
**should**, in fact, have an uppercase letter ``I`` prefixed to their names, like ``IInventoryHolder`` or ``IDamageable``.

Lastly, consider choosing descriptive names and do not try to shorten them too much if it affects
readability.

For instance, if you want to write code to find a nearby enemy and hit it with a weapon, prefer:

.. code-block:: csharp

    FindNearbyEnemy()?.Damage(weaponDamage);

Rather than:

.. code-block:: csharp

    FindNode()?.Change(wpnDmg);

Member variables
----------------

Don't declare member variables if they are only used locally in a method, as it
makes the code more difficult to follow. Instead, declare them as local
variables in the method's body.

Local variables
---------------

Declare local variables as close as possible to their first use. This makes it
easier to follow the code, without having to scroll too much to find where the
variable was declared.

Implicitly typed local variables
--------------------------------

Consider using implicitly typing (``var``) for declaration of a local variable, but do so
**only when the type is evident** from the right side of the assignment:

.. code-block:: csharp

    // You can use `var` for these cases:

    var direction = new Vector2(1, 0);

    var value = (int)speed;

    var text = "Some value";

    for (var i = 0; i < 10; i++)
    {
    }

    // But not for these:

    var value = GetValue();

    var velocity = direction * 1.5;

    // It's generally a better idea to use explicit typing for numeric values, especially with
    // the existence of the `real_t` alias in Godot, which can either be double or float
    // depending on the build configuration.

    var value = 1.5;

Other considerations
--------------------

 * Use explicit access modifiers.
 * Use properties instead of non-private fields.
 * Use modifiers in this order:
   ``public``/``protected``/``private``/``internal``/``virtual``/``override``/``abstract``/``new``/``static``/``readonly``.
 * Avoid using fully-qualified names or ``this.`` prefix for members when it's not necessary.
 * Remove unused ``using`` statements and unnecessary parentheses.
 * Consider omitting the default initial value for a type.
 * Consider using null-conditional operators or type initializers to make the code more compact.
 * Use safe cast when there is a possibility of the value being a different type, and use direct cast otherwise.
