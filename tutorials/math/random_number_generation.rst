.. _doc_random_number_generation:

Random number generation
========================

Many games rely on randomness to implement core game mechanics. This page
guides you through common types of randomness and how to implement them in
Godot.

After giving you a brief overview of useful functions that generate random
numbers, you will learn how to get random elements from arrays, dictionaries,
and how to use a noise generator in GDScript.

.. note::

    Computers cannot generate "true" random numbers. Instead, they rely on
    `pseudorandom number generators
    <https://en.wikipedia.org/wiki/Pseudorandom_number_generator>`__ (PRNGs).

Global scope versus RandomNumberGenerator class
-----------------------------------------------

Godot exposes two ways to generate random numbers: via *global scope* methods or
using the :ref:`class_RandomNumberGenerator` class.

Global scope methods are easier to set up, but they don't offer as much control.

RandomNumberGenerator requires more code to use, but exposes many methods not
found in global scope such as :ref:`randi_range()
<class_RandomNumberGenerator_method_randi_range>` and :ref:`randfn()
<class_RandomNumberGenerator_method_randfn>`. On top of that, it allows creating
multiple instances each with their own seed.

This tutorial uses global scope methods, except when the method only exists in
the RandomNumberGenerator class.

The randomize() method
----------------------

In global scope, you can find a :ref:`randomize()
<class_@GDScript_method_randomize>` method. **This method should be called only
once when your project starts to initialize the random seed.** Calling it
multiple times is unnecessary and may impact performance negatively.

Putting it in your main scene script's ``_ready()`` method is a good choice:

.. tabs::
 .. code-tab:: gdscript GDScript

    func _ready():
        randomize()

 .. code-tab:: csharp

    public override void _Ready()
    {
        GD.Randomize();
    }


You can also set a fixed random seed instead using :ref:`seed()
<class_@GDScript_method_seed>`. Doing so will give you *deterministic* results
across runs:

.. tabs::
 .. code-tab:: gdscript GDScript

    func _ready():
        seed(12345)
        # To use a string as a seed, you can hash it to a number.
        seed("Hello world".hash())

 .. code-tab:: csharp

    // To use a string as a seed, you can hash it to a number.
    GD.Seed((ulong)"Hello world".Hash());

When using the RandomNumberGenerator class, you should call ``randomize()`` on
the instance since it has its own seed:

.. tabs::
 .. code-tab:: gdscript GDScript

    var rng = RandomNumberGenerator.new()
    rng.randomize()

 .. code-tab:: csharp

    var rng = new RandomNumberGenerator();
    rng.Randomize();

Getting a random number
-----------------------

Let's look at some of the most commonly used functions and methods to generate
random numbers in Godot.

The function :ref:`randi() <class_@GDScript_method_randi>` returns a random
number between 0 and 2^32-1. Since the maximum value is huge, you most likely
want to use the modulo operator (``%``) to bound the result between 0 and the
denominator:

.. tabs::
 .. code-tab:: gdscript GDScript

    # Prints a random integer between 0 and 49.
    print(randi() % 50)

    # Prints a random integer between 10 and 60.
    print(randi() % 51 + 10)

 .. code-tab:: csharp

    // Prints a random integer between 0 and 49.
    GD.Print(GD.Randi() % 50);

    // Prints a random integer between 10 and 60
    GD.Print(GD.Randi() % 51 + 10);

:ref:`randf() <class_@GDScript_method_randf>` returns a random floating-point
number between 0 and 1. This is useful to implement a
:ref:`doc_random_number_generation_weighted_random_probability` system, among
other things.

:ref:`randfn() <class_RandomNumberGenerator_method_randfn>` returns a random
floating-point number between 0 and 1. Unlike :ref:`randf()
<class_@GDScript_method_randf>` which follows an uniform distribution, the
returned number follows a `normal distribution
<https://en.wikipedia.org/wiki/Normal_distribution>`__. This means the returned
value is more likely to be around 0.5 compared to the extreme bounds (0 and 1):

.. tabs::
 .. code-tab:: gdscript GDScript

    # Prints a normally distributed floating-point number between 0.0 and 1.0.
    var rng = RandomNumberGenerator.new()
    rng.randomize()
    print(rng.randfn())

 .. code-tab:: csharp

    // Prints a normally distributed floating-point number between 0.0 and 1.0.
    var rng = new RandomNumberGenerator();
    rng.Randomize();
    GD.Print(rng.Randfn());

:ref:`rand_range() <class_@GDScript_method_rand_range>` takes two arguments
``from`` and ``to``, and returns a random floating-point number between ``from``
and ``to``:

.. tabs::
 .. code-tab:: gdscript GDScript

    # Prints a random floating-point number between -4 and 6.5.
    print(rand_range(-4, 6.5))

 .. code-tab:: csharp

    // Prints a random floating-point number between -4 and 6.5.
    GD.Print(GD.RandRange(-4, 6.5));

:ref:`RandomNumberGenerator.randi_range()
<class_RandomNumberGenerator_method_randi_range>` takes two arguments ``from``
and ``to``, and returns a random integer between ``from`` and ``to``:

.. tabs::
 .. code-tab:: gdscript GDScript

    # Prints a random floating-point number between -10 and 10.
    var rng = RandomNumberGenerator.new()
    rng.randomize()
    print(rng.randi_range(-10, 10))

 .. code-tab:: csharp

    // Prints a random floating-point number between -10 and 10.
    var rng = new RandomNumberGenerator();
    rng.Randomize();
    GD.Print(rng.RandiRange(-10, 10));

Get a random array element
--------------------------

We can use random integer generation to get a random element from an array:

.. tabs::
 .. code-tab:: gdscript GDScript

    var fruits = ["apple", "orange", "pear", "banana"]


    func _ready():
        randomize()

        for i in 100:
            # Pick 100 fruits randomly.
            # (``for i in 100`` is a faster shorthand for ``for i in range(100)``.)
            print(get_fruit())


    func get_fruit():
        var random_fruit = fruits[randi() % fruits.size()]
        # Returns "apple", "orange", "pear", or "banana" every time the code runs.
        # We may get the same fruit multiple times in a row.
        return random_fruit

 .. code-tab:: csharp

    string[] fruits = {"apple", "orange", "pear", "banana"};

    public override void _Ready()
    {
        GD.Randomize();

        for (int i = 0; i < 100; i++)
        {
            // Pick 100 fruits randomly.
            GD.Print(get_fruit());
        }
    }

    public string get_fruit()
    {
        string random_fruit = fruits[GD.Randi() % fruits.Length];
        // Returns "apple", "orange", "pear", or "banana" every time the code runs.
        // We may get the same fruit multiple times in a row.
        return random_fruit;
    }

To prevent the same fruit from being picked more than once in a row, we can add
more logic to this method:

.. tabs::
 .. code-tab:: gdscript GDScript

    var fruits = ["apple", "orange", "pear", "banana"]
    var last_fruit = ""


    func _ready():
        randomize()

        # Pick 100 fruits randomly.
        # Note: ``for i in 100`` is a shorthand for ``for i in range(100)``.
        for i in 100:
            print(get_fruit())


    func get_fruit():
        var random_fruit = fruits[randi() % fruits.size()]
        while random_fruit == last_fruit:
            # The last fruit was picked, try again until we get a different fruit.
            random_fruit = fruits[randi() % fruits.size()]

        # Note: if the random element to pick is passed by reference,
        # such as an array or dictionary,
        # use `last_fruit = random_fruit.duplicate()` instead.
        last_fruit = random_fruit

        # Returns "apple", "orange", "pear", or "banana" every time the code runs.
        # The function will never return the same fruit more than once in a row.
        return random_fruit

 .. code-tab:: csharp

    string[] fruits = {"apple", "orange", "pear", "banana"};
    public string lastFruit = "";

    public override void _Ready()
    {
        GD.Randomize();

        for (int i = 0; i < 100; i++)
        {
            // Pick 100 fruits randomly.
            GD.Print(get_fruit());
        }
    }

    public string GetFruit()
    {
        string RandomFruit = fruits[GD.Randi() % fruits.Length];
        while (RandomFruit == LastFruit)
        {
           // The last fruit was picked, try again until we get a different fruit.
           random_fruit = fruits[GD.Randi() % fruits.Length];
        }

        LastFruit = RandomFruit;

        // Returns "apple", "orange", "pear", or "banana" every time the code runs
        // The function will never return the same fruit more than once in a row.
        return random_fruit;
    }

This approach can be useful to make random number generation feel less
repetitive. Still, it doesn't prevent results from "ping-ponging" between a
limited set of values. To prevent this, use the :ref:`shuffle bag
<doc_random_number_generation_shuffle_bags>` pattern instead.

Get a random dictionary value
-----------------------------

We can apply similar logic from arrays to dictionaries as well:

.. tabs::
 .. code-tab:: gdscript GDScript

    var metals = {
        "copper": {"quantity": 50, "price": 50},
        "silver": {"quantity": 20, "price": 150},
        "gold": {"quantity": 3, "price": 500},
    }


    func _ready():
        randomize()

        for i in 20:
            print(get_metal())


    func get_metal():
        var random_metal = metals.values()[randi() % metals.size()]
        # Returns a random metal value dictionary every time the code runs.
        # The same metal may be selected multiple times in succession.
        return random_metal

 .. code-tab:: csharp

    struct MetalInfo
    {
        public MetalInfo(int quantity, int price)
        {
            this.quantity = quantity;
            this.price = price;
        }
        public int quantity;
        public int price;
    }

    enum MetalType
    {
        copper, 
        silver, 
        gold,
    }
    Godot.Collections.Dictionary<MetalType, MetalInfo> metals = new Godot.Collections.Dictionary<MetalType, MetalInfo>
    {
        { MetalType.copper, new MetalInfo(50, 50) }, 
        { MetalType.silver, new MetalInfo(20, 150) }, 
        { MetalType.gold, new MetalInfo(3, 500) }
    };

    public override void _Ready()
    {
        GD.Randomize();
        for (int i = 0; i < 20; i++)
        {
            GD.Print(GetMetal());
        }
    }


.. _doc_random_number_generation_weighted_random_probability:

Weighted random probability
---------------------------

The :ref:`randf() <class_@GDScript_method_randf>` method returns a
floating-point number between 0.0 and 1.0. We can use this to create a
"weighted" probability where different outcomes have different likelihoods:

.. tabs::
 .. code-tab:: gdscript GDScript

    func _ready():
        randomize()

        for i in 100:
            print(get_item_rarity())


    func get_item_rarity():
        var random_float = randf()

        if random_float < 0.8:
            # 80% chance of being returned.
            return "Common"
        elif random_float < 0.95:
            # 15% chance of being returned.
            return "Uncommon"
        else:
            # 5% chance of being returned.
            return "Rare"

 .. code-tab:: csharp

    public override void _Ready()
    {
        GD.Randomize();

        for (int i = 0; i < 100; i++)
        {
            GD.Print(GetItemRarity());
        }
    }

    public string GetItemRarity()
    {
        float RandomFloat = GD.Randf();

        if (RandomFloat < 0.8)
        {
            // 80% chance of being returned
            return "common";
        }
        if (RandomFloat > 0.95)
        {
            // 15% change of being returned
            return "Uncommon";
        }
        else
        {
            // 5% chance of being returned
            return "rare";
        }

.. _doc_random_number_generation_shuffle_bags:

"Better" randomness using shuffle bags
--------------------------------------

Taking the same example as above, we would like to pick fruits at random.
However, relying on random number generation every time a fruit is selected can
lead to a less *uniform* distribution. If the player is lucky (or unlucky), they
could get the same fruit three or more times in a row.

You can accomplish this using the *shuffle bag* pattern. It works by removing an
element from the array after choosing it. After multiple selections, the array
ends up empty. When that happens, you reinitialize it to its default value:

.. tabs::
 .. code-tab:: gdscript GDScript

    var fruits = ["apple", "orange", "pear", "banana"]
    # A copy of the fruits array so we can restore the original value into `fruits`.
    var fruits_full = []


    func _ready():
        randomize()
        fruits_full = fruits.duplicate()
        fruits.shuffle()

        for i in 100:
            print(get_fruit())


    func get_fruit():
        if fruits.empty():
            # Fill the fruits array again and shuffle it.
            fruits = fruits_full.duplicate()
            fruits.shuffle()

        # Get a random fruit, since we shuffled the array,
        # and remove it from the `fruits` array.
        var random_fruit = fruits.pop_front()
        # Prints "apple", "orange", "pear", or "banana" every time the code runs.
        return random_fruit

 .. code-tab:: csharp

When running the above code, there is a chance to get the same fruit twice in a
row. Once we picked a fruit, it will no longer be a possible return value unless
the array is now empty. When the array is empty, we reset it back to its default
value, making it possible to have the same fruit again, but only once.

Random noise
------------

The random number generation shown above can show its limits when you need a
value that *slowly* changes depending on the input. The input can be a position,
time, or anything else.

To achieve this, you can use random *noise* functions. Noise functions are
especially popular in procedural generation to generate realistic-looking
terrain. Godot provides :ref:`class_opensimplexnoise` for this, which supports
1D, 2D, 3D, and 4D noise. Here's an example with 1D noise:

.. tabs::
 .. code-tab:: gdscript GDScript

    var noise = OpenSimplexNoise.new()

    func _ready():
        randomize()
        # Configure the OpenSimplexNoise instance.
        noise.seed = randi()
        noise.octaves = 4
        noise.period = 20.0
        noise.persistence = 0.8

        for i in 100:
            # Prints a slowly-changing series of floating-point numbers
            # between -1.0 and 1.0.
            print(noise.get_noise_1d(i))

 .. code-tab:: csharp

    public override void _Ready()
    {
        var noise = new OpenSimplexNoise();
        GD.Randomize();
        // Configure the OpenSimplexNoise instance.
        noise.Seed = (int)GD.Randi();
        noise.Octaves = 4;
        noise.Period = 20.0f;
        noise.Persistence = 0.8f;

        for (int i = 0; i < 100; i++)
        {
            GD.Print(noise.GetNoise1d(i));
        }
    }
