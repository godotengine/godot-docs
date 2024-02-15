:article_outdated: True

.. _doc_data_preferences:

Data preferences
================

Ever wondered whether one should approach problem X with data structure
Y or Z? This article covers a variety of topics related to these dilemmas.

.. note::

    This article makes references to "[something]-time" operations. This
    terminology comes from algorithm analysis'
    `Big O Notation <https://rob-bell.net/2009/06/a-beginners-guide-to-big-o-notation/>`_.

    Long-story short, it describes the worst-case scenario of runtime length.
    In laymen's terms:

    "As the size of a problem domain increases, the runtime length of the
    algorithm..."

    - Constant-time, ``O(1)``: "...does not increase."
    - Logarithmic-time, ``O(log n)``: "...increases at a slow rate."
    - Linear-time, ``O(n)``: "...increases at the same rate."
    - Etc.

    Imagine if one had to process 3 million data points within a single frame. It
    would be impossible to craft the feature with a linear-time algorithm since
    the sheer size of the data would increase the runtime far beyond the time allotted.
    In comparison, using a constant-time algorithm could handle the operation without
    issue.

    By and large, developers want to avoid engaging in linear-time operations as
    much as possible. But, if one keeps the scale of a linear-time operation
    small, and if one does not need to perform the operation often, then it may
    be acceptable. Balancing these requirements and choosing the right
    algorithm / data structure for the job is part of what makes programmers'
    skills valuable.

Array vs. Dictionary vs. Object
-------------------------------

Godot stores all variables in the scripting API in the
:ref:`Variant <doc_variant_class>` class.
Variants can store Variant-compatible data structures such as
:ref:`Array <class_Array>` and :ref:`Dictionary <class_Dictionary>` as well
as :ref:`Objects <class_Object>`.

Godot implements Array as a ``Vector<Variant>``. The engine stores the Array
contents in a contiguous section of memory, i.e. they are in a row adjacent
to each other.

.. note::

    For those unfamiliar with C++, a Vector is the name of the
    array object in traditional C++ libraries. It is a "templated"
    type, meaning that its records can only contain a particular type (denoted
    by angled brackets). So, for example, a
    :ref:`PackedStringArray <class_PackedStringArray>` would be something like
    a ``Vector<String>``.

Contiguous memory stores imply the following operation performance:

- **Iterate:** Fastest. Great for loops.

    - Op: All it does is increment a counter to get to the next record.

- **Insert, Erase, Move:** Position-dependent. Generally slow.

    - Op: Adding/removing/moving content involves moving the adjacent records
      over (to make room / fill space).

    - Fast add/remove *from the end*.

    - Slow add/remove *from an arbitrary position*.

    - Slowest add/remove *from the front*.

    - If doing many inserts/removals *from the front*, then...

        1. invert the array.

        2. do a loop which executes the Array changes *at the end*.

        3. re-invert the array.

      This makes only 2 copies of the array (still constant time, but slow)
      versus copying roughly 1/2 of the array, on average, N times (linear time).

- **Get, Set:** Fastest *by position*. E.g. can request 0th, 2nd, 10th record, etc.
  but cannot specify which record you want.

    - Op: 1 addition operation from array start position up to desired index.

- **Find:** Slowest. Identifies the index/position of a value.

    - Op: Must iterate through array and compare values until one finds a match.

        - Performance is also dependent on whether one needs an exhaustive
          search.

    - If kept ordered, custom search operations can bring it to logarithmic
      time (relatively fast). Laymen users won't be comfortable with this
      though. Done by re-sorting the Array after every edit and writing an
      ordered-aware search algorithm.

Godot implements Dictionary as an ``OrderedHashMap<Variant, Variant>``. The engine
stores a small array (initialized to 2^3 or 8 records) of key-value pairs. When
one attempts to access a value, they provide it a key. It then *hashes* the
key, i.e. converts it into a number. The "hash" is used to calculate the index
into the array. As an array, the OHM then has a quick lookup within the "table"
of keys mapped to values. When the HashMap becomes too full, it increases to
the next power of 2 (so, 16 records, then 32, etc.) and rebuilds the structure.

Hashes are to reduce the chance of a key collision. If one occurs, the table
must recalculate another index for the value that takes the previous position
into account. In all, this results in constant-time access to all records at
the expense of memory and some minor operational efficiency.

1. Hashing every key an arbitrary number of times.

    - Hash operations are constant-time, so even if an algorithm must do more
      than one, as long as the number of hash calculations doesn't become
      too dependent on the density of the table, things will stay fast.
      Which leads to...

2. Maintaining an ever-growing size for the table.

    - HashMaps maintain gaps of unused memory interspersed in the table
      on purpose to reduce hash collisions and maintain the speed of
      accesses. This is why it constantly increases in size exponentially by
      powers of 2.

As one might be able to tell, Dictionaries specialize in tasks that Arrays
do not. An overview of their operational details is as follows:

- **Iterate:** Fast.

    - Op: Iterate over the map's internal vector of hashes. Return each key.
      Afterwards, users then use the key to jump to and return the desired
      value.

- **Insert, Erase, Move:** Fastest.

    - Op: Hash the given key. Do 1 addition operation to look up the
      appropriate value (array start + offset). Move is two of these
      (one insert, one erase). The map must do some maintenance to preserve
      its capabilities:

        - update ordered List of records.

        - determine if table density mandates a need to expand table capacity.

    - The Dictionary remembers in what
      order users inserted its keys. This enables it to execute reliable iterations.

- **Get, Set:** Fastest. Same as a lookup *by key*.

    - Op: Same as insert/erase/move.

- **Find:** Slowest. Identifies the key of a value.

    - Op: Must iterate through records and compare the value until a match is
      found.

    - Note that Godot does not provide this feature out-of-the-box (because
      they aren't meant for this task).

Godot implements Objects as stupid, but dynamic containers of data content.
Objects query data sources when posed questions. For example, to answer
the question, "do you have a property called, 'position'?", it might ask
its :ref:`script <class_Script>` or the :ref:`ClassDB <class_ClassDB>`.
One can find more information about what objects are and how they work in
the :ref:`doc_what_are_godot_classes` article.

The important detail here is the complexity of the Object's task. Every time
it performs one of these multi-source queries, it runs through *several*
iteration loops and HashMap lookups. What's more, the queries are linear-time
operations dependent on the Object's inheritance hierarchy size. If the class
the Object queries (its current class) doesn't find anything, the request
defers to the next base class, all the way up until the original Object class.
While these are each fast operations in isolation, the fact that it must make
so many checks is what makes them slower than both of the alternatives for
looking up data.

.. note::

  When developers mention how slow the scripting API is, it is this chain
  of queries they refer to. Compared to compiled C++ code where the
  application knows exactly where to go to find anything, it is inevitable
  that scripting API operations will take much longer. They must locate the
  source of any relevant data before they can attempt to access it.

  The reason GDScript is slow is because every operation it performs passes
  through this system.

  C# can process some content at higher speeds via more optimized bytecode.
  But, if the C# script calls into an engine class'
  content or if the script tries to access something external to it, it will
  go through this pipeline.

  NativeScript C++ goes even further and keeps everything internal by default.
  Calls into external structures will go through the scripting API. In
  NativeScript C++, registering methods to expose them to the scripting API is
  a manual task. It is at this point that external, non-C++ classes will use
  the API to locate them.

So, assuming one extends from Reference to create a data structure, like
an Array or Dictionary, why choose an Object over the other two options?

1. **Control:** With objects comes the ability to create more sophisticated
   structures. One can layer abstractions over the data to ensure the external
   API doesn't change in response to internal data structure changes. What's
   more, Objects can have signals, allowing for reactive behavior.

2. **Clarity:** Objects are a reliable data source when it comes to the data
   that scripts and engine classes define for them. Properties may not hold the
   values one expects, but one doesn't need to worry about whether the property
   exists in the first place.

3. **Convenience:** If one already has a similar data structure in mind, then
   extending from an existing class makes the task of building the data
   structure much easier. In comparison, Arrays and Dictionaries don't
   fulfill all use cases one might have.

Objects also give users the opportunity to create even more specialized data
structures. With it, one can design their own List, Binary Search Tree, Heap,
Splay Tree, Graph, Disjoint Set, and any host of other options.

"Why not use Node for tree structures?" one might ask. Well, the Node
class contains things that won't be relevant to one's custom data structure.
As such, it can be helpful to construct one's own node type when building
tree structures.

.. tabs::
  .. code-tab:: gdscript GDScript

    extends Object
    class_name TreeNode

    var _parent: TreeNode = null
    var _children: = [] setget

    func _notification(p_what):
        match p_what:
            NOTIFICATION_PREDELETE:
                # Destructor.
                for a_child in _children:
                    a_child.free()

  .. code-tab:: csharp

    using Godot;
    using System.Collections.Generic;

    // Can decide whether to expose getters/setters for properties later
    public partial class TreeNode : GodotObject
    {
        private TreeNode _parent = null;

        private List<TreeNode> _children = new();

        public override void _Notification(int what)
        {
            switch (what)
            {
                case NotificationPredelete:
                    foreach (TreeNode child in _children)
                    {
                        node.Free();
                    }
                    break;
            }
        }
    }

From here, one can then create their own structures with specific features,
limited only by their imagination.

Enumerations: int vs. string
----------------------------

Most languages offer an enumeration type option. GDScript is no different, but
unlike most other languages, it allows one to use either integers or strings for
the enum values (the latter only when using the ``export`` keyword in GDScript).
The question then arises, "which should one use?"

The short answer is, "whichever you are more comfortable with." This
is a feature specific to GDScript and not Godot scripting in general;
The languages prioritizes usability over performance.

On a technical level, integer comparisons (constant-time) will happen
faster than string comparisons (linear-time). If one wants to keep
up other languages' conventions though, then one should use integers.

The primary issue with using integers comes up when one wants to *print*
an enum value. As integers, attempting to print ``MY_ENUM`` will print
``5`` or what-have-you, rather than something like ``"MyEnum"``. To
print an integer enum, one would have to write a Dictionary that maps the
corresponding string value for each enum.

If the primary purpose of using an enum is for printing values and one wishes
to group them together as related concepts, then it makes sense to use them as
strings. That way, a separate data structure to execute on the printing is
unnecessary.

AnimatedTexture vs. AnimatedSprite2D vs. AnimationPlayer vs. AnimationTree
--------------------------------------------------------------------------

Under what circumstances should one use each of Godot's animation classes?
The answer may not be immediately clear to new Godot users.

:ref:`AnimatedTexture <class_AnimatedTexture>` is a texture that
the engine draws as an animated loop rather than a static image.
Users can manipulate...

1. the rate at which it moves across each section of the texture (FPS).

2. the number of regions contained within the texture (frames).

Godot's :ref:`RenderingServer <class_RenderingServer>` then draws
the regions in sequence at the prescribed rate. The good news is that this
involves no extra logic on the part of the engine. The bad news is
that users have very little control.

Also note that AnimatedTexture is a :ref:`Resource <class_Resource>` unlike
the other :ref:`Node <class_Node>` objects discussed here. One might create
a :ref:`Sprite2D <class_Sprite2D>` node that uses AnimatedTexture as its texture.
Or (something the others can't do) one could add AnimatedTextures as tiles
in a :ref:`TileSet <class_TileSet>` and integrate it with a
:ref:`TileMap <class_TileMap>` for many auto-animating backgrounds that
all render in a single batched draw call.

The AnimatedSprite2D node, in combination with the
:ref:`SpriteFrames <class_SpriteFrames>` resource, allows one to create a
variety of animation sequences through spritesheets, flip between animations,
and control their speed, regional offset, and orientation. This makes them
well-suited to controlling 2D frame-based animations.

If one needs trigger other effects in relation to animation changes (for
example, create particle effects, call functions, or manipulate other
peripheral elements besides the frame-based animation), then will need to use
an :ref:`AnimationPlayer <class_AnimationPlayer>` node in conjunction with
the AnimatedSprite2D.

AnimationPlayers are also the tool one will need to use if they wish to design
more complex 2D animation systems, such as...

1. **Cut-out animations:** editing sprites' transforms at runtime.

2. **2D Mesh animations:** defining a region for the sprite's texture and
   rigging a skeleton to it. Then one animates the bones which
   stretch and bend the texture in proportion to the bones' relationships to
   each other.

3. A mix of the above.

While one needs an AnimationPlayer to design each of the individual
animation sequences for a game, it can also be useful to combine animations
for blending, i.e. enabling smooth transitions between these animations. There
may also be a hierarchical structure between animations that one plans out for
their object. These are the cases where the :ref:`AnimationTree <class_AnimationTree>`
shines. One can find an in-depth guide on using the AnimationTree
:ref:`here <doc_animation_tree>`.
