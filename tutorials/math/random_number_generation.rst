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

RandomNumberGenerator requires more code to use, but allows creating
multiple instances, each with their own seed and state.

This tutorial uses global scope methods, except when the method only exists in
the RandomNumberGenerator class.

The randomize() method
----------------------

In global scope, you can find a :ref:`randomize()
<class_@GlobalScope_method_randomize>` method. **This method should be called only
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
<class_@GlobalScope_method_seed>`. Doing so will give you *deterministic* results
across runs:

.. tabs::
 .. code-tab:: gdscript GDScript

    func _ready():
        seed(12345)
        # To use a string as a seed, you can hash it to a number.
        seed("Hello world".hash())

 .. code-tab:: csharp

    public override void _Ready()
    {
        GD.Seed(12345);
        GD.Seed("Hello world".Hash());
    }

When using the RandomNumberGenerator class, you should call ``randomize()`` on
the instance since it has its own seed:

.. tabs::
 .. code-tab:: gdscript GDScript

    var random = RandomNumberGenerator.new()
    random.randomize()

 .. code-tab:: csharp

    var random = new RandomNumberGenerator();
    random.Randomize();

Getting a random number
-----------------------

Let's look at some of the most commonly used functions and methods to generate
random numbers in Godot.

The function :ref:`randi() <class_@GlobalScope_method_randi>` returns a random
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

    // Prints a random integer between 10 and 60.
    GD.Print(GD.Randi() % 51 + 10);

:ref:`randf() <class_@GlobalScope_method_randf>` returns a random floating-point
number between 0 and 1. This is useful to implement a
:ref:`doc_random_number_generation_weighted_random_probability` system, among
other things.

:ref:`randfn() <class_RandomNumberGenerator_method_randfn>` returns a random
floating-point number following a `normal distribution
<https://en.wikipedia.org/wiki/Normal_distribution>`__. This means the returned
value is more likely to be around the mean (0.0 by default),
varying by the deviation (1.0 by default):

.. tabs::
 .. code-tab:: gdscript GDScript

    # Prints a random floating-point number from a normal distribution with a mean 0.0 and deviation 1.0.
    print(randfn(0.0, 1.0))

 .. code-tab:: csharp

    // Prints a random floating-point number from a normal distribution with a mean 0.0 and deviation 1.0.
    GD.Print(GD.Randfn(0.0, 1.0));

:ref:`randf_range() <class_@GlobalScope_method_randf_range>` takes two arguments
``from`` and ``to``, and returns a random floating-point number between ``from``
and ``to``:

.. tabs::
 .. code-tab:: gdscript GDScript

    # Prints a random floating-point number between -4 and 6.5.
    print(randf_range(-4, 6.5))

 .. code-tab:: csharp

    // Prints a random floating-point number between -4 and 6.5.
    GD.Print(GD.RandRange(-4.0, 6.5));

:ref:`RandomNumberGenerator.randi_range()
<class_RandomNumberGenerator_method_randi_range>` takes two arguments ``from``
and ``to``, and returns a random integer between ``from`` and ``to``:

.. tabs::
 .. code-tab:: gdscript GDScript

    # Prints a random integer between -10 and 10.
    print(randi_range(-10, 10))

 .. code-tab:: csharp

    // Prints a random integer number between -10 and 10.
    GD.Print(GD.RandRange(-10, 10));

Get a random array element
--------------------------

We can use random integer generation to get a random element from an array:

.. tabs::
 .. code-tab:: gdscript GDScript

    var _fruits = ["apple", "orange", "pear", "banana"]

    func _ready():
        for i in range(100):
            # Pick 100 fruits randomly.
            print(get_fruit())


    func get_fruit():
        var random_fruit = _fruits[randi() % _fruits.size()]
        # Returns "apple", "orange", "pear", or "banana" every time the code runs.
        # We may get the same fruit multiple times in a row.
        return random_fruit

 .. code-tab:: csharp

    private string[] _fruits = { "apple", "orange", "pear", "banana" };

    public override void _Ready()
    {
        for (int i = 0; i < 100; i++)
        {
            // Pick 100 fruits randomly.
            GD.Print(GetFruit());
        }
    }

    public string GetFruit()
    {
        string randomFruit = _fruits[GD.Randi() % _fruits.Length];
        // Returns "apple", "orange", "pear", or "banana" every time the code runs.
        // We may get the same fruit multiple times in a row.
        return randomFruit;
    }

To prevent the same fruit from being picked more than once in a row, we can add
more logic to this method:

.. tabs::
 .. code-tab:: gdscript GDScript

    var _fruits = ["apple", "orange", "pear", "banana"]
    var _last_fruit = ""


    func _ready():
        # Pick 100 fruits randomly.
        for i in range(100):
            print(get_fruit())


    func get_fruit():
        var random_fruit = _fruits[randi() % _fruits.size()]
        while random_fruit == _last_fruit:
            # The last fruit was picked, try again until we get a different fruit.
            random_fruit = _fruits[randi() % _fruits.size()]

        # Note: if the random element to pick is passed by reference,
        # such as an array or dictionary,
        # use `_last_fruit = random_fruit.duplicate()` instead.
        _last_fruit = random_fruit

        # Returns "apple", "orange", "pear", or "banana" every time the code runs.
        # The function will never return the same fruit more than once in a row.
        return random_fruit

 .. code-tab:: csharp

    private string[] _fruits = { "apple", "orange", "pear", "banana" };
    private string _lastFruit = "";

    public override void _Ready()
    {
        for (int i = 0; i < 100; i++)
        {
            // Pick 100 fruits randomly.
            GD.Print(GetFruit());
        }
    }

    public string GetFruit()
    {
        string randomFruit = _fruits[GD.Randi() % _fruits.Length];
        while (randomFruit == _lastFruit)
        {
            // The last fruit was picked, try again until we get a different fruit.
            randomFruit = _fruits[GD.Randi() % _fruits.Length];
        }

        _lastFruit = randomFruit;

        // Returns "apple", "orange", "pear", or "banana" every time the code runs.
        // The function will never return the same fruit more than once in a row.
        return randomFruit;
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

    var _metals = {
        "copper": {"quantity": 50, "price": 50},
        "silver": {"quantity": 20, "price": 150},
        "gold": {"quantity": 3, "price": 500},
    }


    func _ready():
        for i in range(20):
            print(get_metal())


    func get_metal():
        var random_metal = _metals.values()[randi() % metals.size()]
        # Returns a random metal value dictionary every time the code runs.
        # The same metal may be selected multiple times in succession.
        return random_metal

 .. code-tab:: csharp

    private Godot.Collections.Dictionary<string, Godot.Collections.Dictionary<string, int>> _metals = new()
    {
        {"copper", new Godot.Collections.Dictionary<string, int>{{"quantity", 50}, {"price", 50}}},
        {"silver", new Godot.Collections.Dictionary<string, int>{{"quantity", 20}, {"price", 150}}},
        {"gold", new Godot.Collections.Dictionary<string, int>{{"quantity", 3}, {"price", 500}}},
    };

    public override void _Ready()
    {
        for (int i = 0; i < 20; i++)
        {
            GD.Print(GetMetal());
        }
    }

    public Godot.Collections.Dictionary<string, int> GetMetal()
    {
        var (_, randomMetal) = _metals.ElementAt((int)(GD.Randi() % _metals.Count));
        // Returns a random metal value dictionary every time the code runs.
        // The same metal may be selected multiple times in succession.
        return randomMetal;
    }

.. _doc_random_number_generation_weighted_random_probability:

Weighted random probability
---------------------------

The :ref:`randf() <class_@GlobalScope_method_randf>` method returns a
floating-point number between 0.0 and 1.0. We can use this to create a
"weighted" probability where different outcomes have different likelihoods:

.. tabs::
 .. code-tab:: gdscript GDScript

    func _ready():
        for i in range(100):
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
        for (int i = 0; i < 100; i++)
        {
            GD.Print(GetItemRarity());
        }
    }

    public string GetItemRarity()
    {
        float randomFloat = GD.Randf();

        if (randomFloat < 0.8f)
        {
            // 80% chance of being returned.
            return "Common";
        }
        else if (randomFloat < 0.95f)
        {
            // 15% chance of being returned
            return "Uncommon";
        }
        else
        {
            // 5% chance of being returned.
            return "Rare";
        }
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

    var _fruits = ["apple", "orange", "pear", "banana"]
    # A copy of the fruits array so we can restore the original value into `fruits`.
    var _fruits_full = []


    func _ready():
        _fruits_full = _fruits.duplicate()
        _fruits.shuffle()

        for i in 100:
            print(get_fruit())


    func get_fruit():
        if _fruits.is_empty():
            # Fill the fruits array again and shuffle it.
            _fruits = _fruits_full.duplicate()
            _fruits.shuffle()

        # Get a random fruit, since we shuffled the array,
        # and remove it from the `_fruits` array.
        var random_fruit = _fruits.pop_front()
        # Returns "apple", "orange", "pear", or "banana" every time the code runs, removing it from the array.
        # When all fruit are removed, it refills the array.
        return random_fruit

 .. code-tab:: csharp

    private Godot.Collections.Array<string> _fruits = new() { "apple", "orange", "pear", "banana" };
    // A copy of the fruits array so we can restore the original value into `fruits`.
    private Godot.Collections.Array<string> _fruitsFull;

    public override void _Ready()
    {
        _fruitsFull = _fruits.Duplicate();
        _fruits.Shuffle();

        for (int i = 0; i < 100; i++)
        {
            GD.Print(GetFruit());
        }
    }

    public string GetFruit()
    {
        if(_fruits.Count == 0)
        {
            // Fill the fruits array again and shuffle it.
            _fruits = _fruitsFull.Duplicate();
            _fruits.Shuffle();
        }

        // Get a random fruit, since we shuffled the array,
        string randomFruit = _fruits[0];
        // and remove it from the `_fruits` array.
        _fruits.RemoveAt(0);
        // Returns "apple", "orange", "pear", or "banana" every time the code runs, removing it from the array.
        // When all fruit are removed, it refills the array.
        return randomFruit;
    }

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
terrain. Godot provides :ref:`class_fastnoiselite` for this, which supports
1D, 2D and 3D noise. Here's an example with 1D noise:

.. tabs::
 .. code-tab:: gdscript GDScript

    var _noise = FastNoiseLite.new()

    func _ready():
        # Configure the FastNoiseLite instance.
        _noise.noise_type = FastNoiseLite.NoiseType.TYPE_SIMPLEX_SMOOTH
        _noise.seed = randi()
        _noise.fractal_octaves = 4
        _noise.frequency = 1.0 / 20.0

        for i in 100:
            # Prints a slowly-changing series of floating-point numbers
            # between -1.0 and 1.0.
            print(_noise.get_noise_1d(i))

 .. code-tab:: csharp

    private FastNoiseLite _noise = new FastNoiseLite();

    public override void _Ready()
    {
        // Configure the FastNoiseLite instance.
        _noise.NoiseType = NoiseTypeEnum.SimplexSmooth;
        _noise.Seed = (int)GD.Randi();
        _noise.FractalOctaves = 4;
        _noise.Frequency = 1.0f / 20.0f;

        for (int i = 0; i < 100; i++)
        {
            GD.Print(_noise.GetNoise1D(i));
        }
    }
