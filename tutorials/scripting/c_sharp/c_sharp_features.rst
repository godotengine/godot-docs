.. _doc_c_sharp_features:

C# language features
====================

This page provides an overview of the commonly used features of both C# and Godot
and how they are used together.

.. _doc_c_sharp_features_type_conversion_and_casting:

Type conversion and casting
---------------------------

C# is a statically typed language. Therefore, you can't do the following:

.. code-block:: csharp

    var mySprite = GetNode("MySprite");
    mySprite.SetFrame(0);

The method ``GetNode()`` returns a ``Node`` instance.
You must explicitly convert it to the desired derived type, ``Sprite2D`` in this case.

For this, you have various options in C#.

**Casting and Type Checking**

Throws ``InvalidCastException`` if the returned node cannot be cast to Sprite2D.
You would use it instead of the ``as`` operator if you are pretty sure it won't fail.

.. code-block:: csharp

    Sprite2D mySprite = (Sprite2D)GetNode("MySprite");
    mySprite.SetFrame(0);

**Using the AS operator**

The ``as`` operator returns ``null`` if the node cannot be cast to Sprite2D,
and for that reason, it cannot be used with value types.

.. code-block:: csharp

    Sprite2D mySprite = GetNode("MySprite") as Sprite2D;
    // Only call SetFrame() if mySprite is not null
    mySprite?.SetFrame(0);

**Using the generic methods**

Generic methods are also provided to make this type conversion transparent.

``GetNode<T>()`` casts the node before returning it. It will throw an ``InvalidCastException`` if the node cannot be cast to the desired type.

.. code-block:: csharp

    Sprite2D mySprite = GetNode<Sprite2D>("MySprite");
    mySprite.SetFrame(0);

``GetNodeOrNull<T>()`` uses the ``as`` operator and will return ``null`` if the node cannot be cast to the desired type.

.. code-block:: csharp

    Sprite2D mySprite = GetNodeOrNull<Sprite2D>("MySprite");
    // Only call SetFrame() if mySprite is not null
    mySprite?.SetFrame(0);

**Type checking using the IS operator**

To check if the node can be cast to Sprite2D, you can use the ``is`` operator.
The ``is`` operator returns false if the node cannot be cast to Sprite2D,
otherwise it returns true. Note that when the ``is`` operator is used against ``null``
the result is always going to be ``false``.

.. code-block:: csharp

    if (GetNode("MySprite") is Sprite2D)
    {
        // Yup, it's a Sprite2D!
    }

    if (null is Sprite2D)
    {
        // This block can never happen.
    }

You can also declare a new variable to conditionally store the result of the cast
if the ``is`` operator returns ``true``.

.. code-block:: csharp

    if (GetNode("MySprite") is Sprite2D mySprite)
    {
        // The mySprite variable only exists inside this block, and it's never null.
        mySprite.SetFrame(0);
    }

For more advanced type checking, you can look into `Pattern Matching <https://docs.microsoft.com/en-us/dotnet/csharp/pattern-matching>`_.


Preprocessor defines
--------------------

Godot has a set of defines that allow you to change your C# code
depending on the environment you are compiling to.

.. note:: If you created your project before Godot 3.2, you have to modify
          or regenerate your `csproj` file to use this feature
          (compare ``<DefineConstants>`` with a new 3.2+ project).

Examples
~~~~~~~~

For example, you can change code based on the platform:

.. code-block:: csharp

        public override void _Ready()
        {
    #if GODOT_SERVER
            // Don't try to load meshes or anything, this is a server!
            LaunchServer();
    #elif GODOT_32 || GODOT_MOBILE || GODOT_WEB
            // Use simple objects when running on less powerful systems.
            SpawnSimpleObjects();
    #else
            SpawnComplexObjects();
    #endif
        }

Or you can detect which engine your code is in, useful for making cross-engine libraries:

.. code-block:: csharp

        public void MyPlatformPrinter()
        {
    #if GODOT
            GD.Print("This is Godot.");
    #elif UNITY_5_3_OR_NEWER
            print("This is Unity.");
    #else
            throw new NotSupportedException("Only Godot and Unity are supported.");
    #endif
        }

Or you can write scripts that target multiple Godot versions and take
advantage of features that are only available on some of those versions:

.. code-block:: csharp

        public void UseCoolFeature()
        {
    #if GODOT4_3_OR_GREATER || GODOT4_2_2_OR_GREATER
            // Use CoolFeature, that was added to Godot in 4.3 and cherry-picked into 4.2.2, here.
    #else
            // Use a workaround for the absence of CoolFeature here.
    #endif
        }

Full list of defines
~~~~~~~~~~~~~~~~~~~~

* ``GODOT`` is always defined for Godot projects.

* ``TOOLS`` is defined when building with the Debug configuration (editor and editor player).

* ``GODOT_REAL_T_IS_DOUBLE`` is defined when the ``GodotFloat64`` property is set to ``true``.

* One of ``GODOT_64`` or ``GODOT_32`` is defined depending on if the architecture is 64-bit or 32-bit.

* One of ``GODOT_LINUXBSD``, ``GODOT_WINDOWS``, ``GODOT_OSX``,
  ``GODOT_ANDROID``, ``GODOT_IOS``, ``GODOT_HTML5``, or ``GODOT_SERVER``
  depending on the OS. These names may change in the future.
  These are created from the ``get_name()`` method of the
  :ref:`OS <class_OS>` singleton, but not every possible OS
  the method returns is an OS that Godot with .NET runs on.

* ``GODOTX``, ``GODOTX_Y``, ``GODOTX_Y_Z``, ``GODOTx_OR_GREATER``,
  ``GODOTX_y_OR_GREATER``, and ``GODOTX_Y_z_OR_GREATER``, where ``X``, ``Y``,
  and ``Z`` are replaced by the current major, minor and patch version of Godot.
  ``x``, ``y``, and ``z`` are replaced by all values from 0 to the current version number for that
  component.

  .. note::

    These defines were first added in Godot 4.0.4 and 4.1. Version defines for
    prior versions do not exist, regardless of the current Godot version.

  For example: Godot 4.0.5 defines ``GODOT4``, ``GODOT4_OR_GREATER``,
  ``GODOT4_0``, ``GODOT4_0_OR_GREATER``, ``GODOT4_0_5``,
  ``GODOT4_0_4_OR_GREATER``, and ``GODOT4_0_5_OR_GREATER``. Godot 4.3.2 defines
  ``GODOT4``, ``GODOT4_OR_GREATER``, ``GODOT4_3``, ``GODOT4_0_OR_GREATER``,
  ``GODOT4_1_OR_GREATER``, ``GODOT4_2_OR_GREATER``, ``GODOT4_3_OR_GREATER``,
  ``GODOT4_3_2``, ``GODOT4_3_0_OR_GREATER``, ``GODOT4_3_1_OR_GREATER``, and
  ``GODOT4_3_2_OR_GREATER``.

When **exporting**, the following may also be defined depending on the export features:

* One of ``GODOT_PC``, ``GODOT_MOBILE``, or ``GODOT_WEB`` depending on the platform type.

* One of ``GODOT_WINDOWS``, ``GODOT_LINUXBSD``, ``GODOT_MACOS``, ``GODOT_ANDROID``, ``GODOT_IOS``, or ``GODOT_WEB`` depending on the platform.

To see an example project, see the OS testing demo:
https://github.com/godotengine/godot-demo-projects/tree/master/misc/os_test
